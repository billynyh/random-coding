---
layout: post
title: "Y U NO public (or protected)"
date: 2014-07-20 20:47:27 +0800
comments: true
categories: [android]
---

Recently started a new project in work so I finally have a chance to use SwipeRefreshLayout in work. The integration is very simple and does not change the structure of ListView like [Android-PullToRefresh](https://github.com/chrisbanes/android-pulltorefresh) (I still love that library).

I also like the progress bar embeded in the view very much, and would like to use it in other components to make my apps's UI consistent. A quick look to the [source code](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/master/v4/java/android/support/v4/widget/SwipeRefreshLayout.java) and found that it is implemented in the class [SwipeProgressBar](https://android.googlesource.com/platform/frameworks/support/+/refs/heads/master/v4/java/android/support/v4/widget/SwipeProgressBar.java). It is sad that the class is not public and it seems there is no similar class in the framework and support library. 

So, I just copy the code of SwipeProgressBar and BakedBezierInterpolator myself and put it in my common lib, then use it in my app.

I understand that there are some kind of design principle of the class/methods visibility, but sometime it is quite frustrating that after going through the framework source code and found that you cannot to extend the class because some properties are private and does not have a public/protected getter.

<img src="{{root_url}}/images/posts/20140720/yuno.jpg" style="width:300px" />

## Reference

* [Controlling Access to Members of a Class](http://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
