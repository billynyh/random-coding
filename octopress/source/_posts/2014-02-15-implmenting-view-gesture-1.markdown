---
layout: post
title: "Implementing zoomable view - part 1"
date: 2014-02-15 22:27:54 +0800
comments: true
categories: [android, view, gesture]
---

Last year I implemented a custom view that supports different gestures including zoom(scale), scroll, double tap. As a newbie on custom view, the whole measuring and drawing already spent me some time, so the gesture control turned out enough to use but was actually incomplete and not finished. 

Recently, I have a task to embed my custom view to ViewPager and other custom ViewGroup that intercept touch events. As expected, my custom view takes all the touch events so the ViewPager cannot perform horizontal swipe. I woule like to take this chance to review my gesture handling and hopefully can make it work.

What I did last year is mostly referencing Chris Banes's [PhotoView library](https://github.com/chrisbanes/PhotoView/blob/master/library/src/uk/co/senab/photoview/PhotoViewAttacher.java). The basic idea is:

* create a "view attacher" that implements a View.OnTouchListener
* create instance of [ScaleGesutreDetector](http://developer.android.com/reference/android/view/ScaleGestureDetector.html) and [GestureDetector](http://developer.android.com/reference/android/view/GestureDetector.html), notice that [PhotoView's GestureDetector](https://github.com/chrisbanes/PhotoView/blob/master/library/src/uk/co/senab/photoview/gestures/GestureDetector.java) is not the one in Android framework
* use those detectors in OnTouchListener's onTouch method

{% codeblock lang:java %}
public class ZoomableViewAttacher implements View.OnTouchListener {
    GestureDetector mGestureDetector;
    ScaleGestureDetector mScaleGestureDetector;

    ...

    @Override
    public final boolean onTouch(View v, MotionEvent ev) {
        boolean handled = false;

        ...

        if (null != mGestureDetector && mGestureDetector.onTouchEvent(ev)) {
            handled = true;
        }

        if (null != mScaleGestureDetector && mScaleGestureDetector.onTouchEvent(ev)) {
            handled = true;
        }

        return handled; // or just return true;
    }
}
{% endcodeblock %}

So far this worked for me last year as I am using the view alone, I did not have to consider the case that the view's parent intercepted the touch event.

Now the problem is, how do I prevent the ViewPager intercepting my touch event? After digging deeper, I found a requestDisallowInterceptTouchEvent method in ViewParent. According to the framework [doc](http://developer.android.com/reference/android/view/ViewParent.html#requestDisallowInterceptTouchEvent(boolean\)) 

{% blockquote %}
Called when a child does not want this parent and its ancestors to intercept touch events with onInterceptTouchEvent(MotionEvent).

This parent should pass this call onto its parents. This parent must obey this request for the duration of the touch (that is, only clear the flag after this parent has received an up or a cancel.
{% endblockquote %}

Which means, if I call the method in correct time, I should be able to enable and disable ViewPager's onInterceptTouchEvent. Googled a little bit on requestDisallowInterceptTouchEvent, found some example on StackOverflow like

{% codeblock lang:java %}
switch (event.getAction()) {
    case MotionEvent.ACTION_DOWN:
        parent.requestDisallowInterceptTouchEvent(true);
        break;
    case MotionEvent.ACTION_CANCEL:
    case MotionEvent.ACTION_UP:
        parent.requestDisallowInterceptTouchEvent(false);
        break;
    default:
        break;
}
{% endcodeblock %}

This is obviously not enough for me, since it disabled the parent for the whole touch motion, if I touch on my custom and actually want to perform a page swipe on ViewPager, thie code will definitely break the ViewPager usage. 

My first attempt is something like:

{% codeblock lang:java %}
switch (event.getAction()) {
    case MotionEvent.ACTION_DOWN:
        parent.requestDisallowInterceptTouchEvent(true);
        break;
    case MotionEvent.ACTION_CANCEL:
    case MotionEvent.ACTION_UP:
        parent.requestDisallowInterceptTouchEvent(false);
        break;
    default:
        break;

    if (!canScroll()) {
        // re-enable parents' onInterceptTouchEvent
        parent.requestDisallowInterceptTouchEvent(false);
    }

}
{% endcodeblock %}

It would be great if GestureDetector can directly give me the information needed for my canScroll() method. However, it seems that GestureDetector need a few events to determine if it is a scroll, there is a gap of 3-5 events between my first ACTION\_DOWN and onScoll callback, so I need a better way to determine the condition for calling parent.requestDisallowInterceptTouchEvent(). 

In part 2, I will continue with the implementation of canScroll() method.
