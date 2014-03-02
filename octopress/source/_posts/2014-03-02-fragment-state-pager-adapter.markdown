---
layout: post
title: "A deeper look of ViewPager and FragmentStatePagerAdaper"
date: 2014-03-02 21:01:40 +0800
comments: true
categories: [android, viewpager]
---

## Background

Last week I was working on a remove action on ViewPager, so based on the knowledge from ListView's adapter, I tried removing the item and called notifyDataSetChanged, it didn't work. So I googled a little bit and found that I need to override the getItemPosition method in PagerAdapter when removing item.

This is the doc from PagerAdapter
> A data set change may involve pages being added, removed, or changing position. The ViewPager will keep the current page active provided the adapter implements the method getItemPosition(Object).

and description of getItemPosition
> Called when the host view is attempting to determine if an item's position has changed. Returns POSITION_UNCHANGED if the position of the given item has not changed or POSITION_NONE if the item is no longer present in the adapter.


Then I put it in my pager adapter, got a different behavior, but still not work correctly. Three thoughts came to me immediately: 

 1. something wrong in my getItemPosition
 2. something wrong when I integrate with my other code.
 3. something wrong in FragmentStatePagerAdapter
 
For 1, it is easy to verify by printing logs and it looked good to me. 2, I don't think so but still spend some time to check my code first. As expected, problem still existed. I always have a problem with Fragment lifecycle, everytime I thought I understand more, a new problem came out and breaks my understanding of fragment lifecycle. I tried hard to avoid go deep to the implementation of FragmentStatePagerAdapter, but this time I have no choice. 

## FragmentStatePagerAdapter

I am a little bit surprised by the [short code length](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/master/v4/java/android/support/v4/app/FragmentStatePagerAdapter.java) of it. 

{% codeblock lang:java %}
//https://android.googlesource.com/platform/frameworks/support/+/refs/heads/master/v4/java/android/support/v4/app/FragmentStatePagerAdapter.java
private ArrayList<Fragment> mFragments = new ArrayList<Fragment>();

@Override
public Object instantiateItem(ViewGroup container, int position) {
    if (mFragments.size() > position) {
        Fragment f = mFragments.get(position);
        if (f != null) {
            return f;
        }
    }

    if (mCurTransaction == null) {
        mCurTransaction = mFragmentManager.beginTransaction();
    }

    Fragment fragment = getItem(position);
    ...
    mFragments.set(position, fragment);
    mCurTransaction.add(container.getId(), fragment);

    return fragment;
}

@Override
public void destroyItem(ViewGroup container, int position, Object object) {
    Fragment fragment = (Fragment)object;

    if (mCurTransaction == null) {
        mCurTransaction = mFragmentManager.beginTransaction();
    }
    ...
    mSavedState.set(position, mFragmentManager.saveFragmentInstanceState(fragment));
    mFragments.set(position, null);

    mCurTransaction.remove(fragment);
}

{% endcodeblock %}

Here is what FragmentStatePagerAdapter does in instantiateItem and destroyItem, in short, it maintains an ArrayList mFragments which mFragments.get(i) returns the fragment that is in position i, null if fragment not in fragment manager. By default, ViewPager will keep one item before and after current item, so if you are at position 1 (0-based), mFragments will be like

 0 | 1 | 2 | 3 | 4 
---|---|---|---|---
 F0 | F1 | F2 | null | null 

## Remove item

What will happen if I remove F1 and call notifyDataSetChanged? the result of getItemPosition should be
```
F0: 0 (or POSITION_UNCHANGED?)
F1: POSITION_NONE
F2: 1
```
Right?

Then I expect mFragments become

 0 | 1 | 2 | 3 | 4 
---|---|---|---|---
 F0 | F2 | null | null | null 

But from the source of FragmentStatePagerAdapter, I don't think it has any handling of it. I copied the source and added some log to dump mFragments out, and find that it is like

 Step | What I see | 0 | 1 | 2 | 3 | 4 
 :----|------------|---|---|---|---|---
 1 |curr item F1 | F0 | F1 | F2 | null | null 
 2 |after remove F1, F2 becomes curr item | F0 | null |  F2 | null | null 
 3 |swipe next, no item displayed but F4 instantiated | null | null | F2 | F4 | null 
 4 |swipe next, curr item F4 | null | null | F2 | F4 | F5 
 5 |swipe next, curr item F5 | null | null | null | F4 | F5 

then the app crashed on step 5 when it tries to destroy F2. 

## Dafaq?

First of all, what happened in step 2? It just removed F1 and left F2 there, and ViewPager just display it?

Yes, something like that.

1. When F1 is removed and called notifyDataSetChanged, ViewPager will call getItemPosition for each item, in the order of F0, F1, F2. 
2. When POSITION_NONE is returned for F1, adapter's destroyItem is called and F1 is removed from FragmentManager and mFragments. 
3. Then for F2, it returned the new position 1, which match the current position, so ViewPager uses F2 directly, but **leave mFragments in adapter not updated**. 
4. After that, it should create F3 by calling instantiateItem on position 2, however, as mFragments still keeping F2 in position 2, it is directly returned and F3 is never created.
5. In the first swipe after remove, ViewPager tries to display data in position 2 which the fragment F2 is already used in position 1. At the same time, F0 is removed from FragmentManager, F4 is created as item in position 3.
6. Second swipe, position 3(F4) becomes current item, position 1(F2) removed from FragmentManager, F5 created for position 4.
7. Third swipe, position 4(F5) becomes current item, ViewPager tried to destroy position 2, but position 2 is also F2, destroying that cause 
> IllegalStateException: Fragment {} is not currently in the FragmentManager.

## Workaround

When I tried to isolate the problem, I accidentally return POSITION_NONE for all item, and it actually gave the result I want without crash. It worked because all fragments are destroyed in notifyDataSetChanged and re-instantiated, it does the tricks but may cause other performance problem so I am looking for a better solution.

## Possible fix

I have not start yet, but as mFragments in FragmentStatePagerAdapter is private, extending it and override some methods cannot change it at all. Good news is, you can copy the source and compile it yourself. 

To fix this, you need to find a way to update mFragments after checking getItemPosition and destroyItem. My initial thoughts is to handle that in finishUpdate(). The new finishUpdate will become something like:


{% codeblock lang:java %}
@Override
public void finishUpdate(ViewGroup container) {
    if (mCurTransaction != null) {
        mCurTransaction.commitAllowingStateLoss();
        mCurTransaction = null;
        mFragmentManager.executePendingTransactions();
    }
    
    ArrayList<Fragment> update = new ArrayList<Fragment>();
    for (int i=0, n=mFragments.size(); i < n; i++) {
        Fragment f = mFragments.get(i);
        if (f == null) continue;
        int pos = getItemPosition(f);
        while (update.size() <= pos) {
            update.add(null);
        }
        update.set(pos, f);
    }
    mFragments = update;
}
{% endcodeblock %}

One problem is that finishUpdate is also called in other places so need to make sure this change will not break other code and not causing performance issue. 

## About this post...

At first I just want to write a short notes on the problem I met during work, then I tried to isolate the problem and reproduce it, tried to find similar posts on stackoverflow, read the soure code to confirm the problem, and even tried to fix it... This is totally not my plan for this weekend but I actually quite enjoy reading the source code of support library.


## Reference

* [Discussion on gplus](https://plus.google.com/u/0/105980838674582844427/posts/a1xwgEEehCs) thx Adam Powell for replying my post.
* Source of [ViewPager](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/master/v4/java/android/support/v4/view/ViewPager.java) and [FragmentStatePagerAdapter](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/master/v4/java/android/support/v4/app/FragmentStatePagerAdapter.java)
* https://code.google.com/p/android/issues/detail?id=37990
 
