---
layout: post
title: My 2013 Android development
date: 2013-12-23 23:48:54 +0800
comments: true
categories: [android, github]
---

2013 was a fresh start for me. I joined a new team, started the Android product from scratch, get a nice number of active users and keep it growing. During my development, I referenced many opensource projects and learnt alot from them.

### [kevinsawicki/http-request](https://github.com/kevinsawicki/http-request)

This is the very first library I added to my project (support-v4 does not count). This library provided a nice wrap of http call. I am not sure if this can be used with other network library like square/okhttp and android/volley, hope I have time to try it out in 2014.

### [jfeinstein10/SlidingMenu](https://github.com/jfeinstein10/SlidingMenu)

This is the sliding menu I used at the beginning, I like the effect very much. Although I switched to Android DrawerLayout after it was introduced in support-v4, I do like the old SlidingMenu more. Personally I like to have the drawer push the content out, DrawerLayout is more like an overlay, they both make sense to me, let see will the design guideline include this kind of UI also.

### [square/otto](https://github.com/square/otto)

I am a big fan of Square opensource projects but I was not using any event bus so when I saw otto I did not get it at first. When things getting complicated that you cannot write everything in your Activity/Fragment, you will try to split the logic to different components. The old school way to communicate between components is implements some kind of listener, it works for a while, a short while... The app goes complicated way faster than I expect, so I decided to make a big structure change by using an event bus system. I have not compared other event bus library but otto works for me perfectly.


### ActionBar

Before the official actionbar-compact was released after GoogleIO, I think most people will use ActionBarSherlock. However, I implmented my own. I think it gives me more flexibility if you implemented your own, especially when you dont need those inflate from menu support. The down side is you lost support from all opensource projects, I have to implement my own refresh/progress buttons, ShareActionProvider, cannot play with those fancy fading actionbar, not boring actionbar library, may even need to write my own android style pull to refresh. Those disadvantage are usually enough to stop me from using my own implementation, but I decided to keep it. Mostly because it turns out not that hard to migrate to my own actionbar as long as it is opensourced and I do not have to worry about two libraries not working together (because I am not using any...).

