---
layout: post
title: "ViewCompat.canScrollVertically()"
date: 2014-06-22 19:56:29 +0800
comments: true
categories: android
---


Due to watching world cup evey night through out the week, I spent most of my time these two weekends sleeping. Even not able to do some serious coding, I tried to clean up my long pending reading list, and I just took a look of [SwipeRefreshLayout](http://developer.android.com/reference/android/support/v4/widget/SwipeRefreshLayout.html). 

Saw this class a while ago, just from the name of this class, I expected it to be a ViewGroup that handles the pull gesture of the Android style pull to refresh. I was not very interested in this class because there is no plan to touch the refresh UI in work, but it is always good to know it is in the support library. 

What really caught my attention is the canChildScrollUp() method in SwipeRefreshLayout. It used ViewCompat.canScrollVertically and special handled pre-ICS. 


[Source line 348](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/master/v4/java/android/support/v4/widget/SwipeRefreshLayout.java)

``` java 

public boolean canChildScrollUp() {
    if (android.os.Build.VERSION.SDK_INT < 14) {
        if (mTarget instanceof AbsListView) {
            final AbsListView absListView = (AbsListView) mTarget;
            return absListView.getChildCount() > 0
                    && (absListView.getFirstVisiblePosition() > 0 || absListView.getChildAt(0)
                            .getTop() < absListView.getPaddingTop());
        } else {
            return mTarget.getScrollY() > 0;
        }
    } else {
        return ViewCompat.canScrollVertically(mTarget, -1);
    }
}

```

(Well I don't understand why the ViewCompat method cannot(?) handle pre-ICS... then what's the point of Compat?)

I wasn't aware there is a canScrollVertically() method in View since ICS, and the ViewCompat also provides some interesting method that could simplify some custom ViewGroup implementation. Should put more time to review what's new in those commonly used classes as I believe there is no need to support pre-ICS soon. 

Refrerence: http://antonioleiva.com/swiperefreshlayout/

