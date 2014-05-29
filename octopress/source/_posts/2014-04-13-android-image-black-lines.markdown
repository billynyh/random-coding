---
layout: post
title: Android image decode bug on Samsung devices
date: 2014-04-13 23:21:18 +0800
comments: true
categories: [android, samsung, bitmap]
---


## Image decode bug on Samsung devices

Few weeks ago I got some users reported about seeing "black lines" on the images. In 9GAG app, displaying images is everything so I can't just leave the problem unsolved.

At first I thought it is a problem I worked on before that when multiple download tasks running for the same image, may corrupt the file. However, this time is a little bit different. 

<img src="{{root_url}}/images/posts/20140413/blacklines.png"/>

I checked those reports and find that only users using (high end?) Samsung devices (S4 and Note3) hit this problem, and I cannot reproduce the problem on my testing devices. Luckily, we recently equipped a Samsung Galaxy S4 in office so I can schedule some time on this problem. And they are actually not black lines, they are transparent lines...

Even I suspected it is a manufacture specific problem, I did not expect I can reproduce the problem easily, so I am a little bit surprised to see the problem on the device. There are two possible causes of the problem, 1. the image file corrupted, 2. the image is correct but corrupted during decode to bitmap object. After a little test, I can confirm that I am dealing with (2)... When debugging with logcat, the following logs appear everytime the problem occurs.

    skia  D  JPEG content is corrupt, got a zero length row(272)
    skia  D  JPEG content is corrupt, got a zero length row(273)
    skia  D  JPEG content is corrupt, got a zero length row(274)
    skia  D  JPEG content is corrupt, got a zero length row(275)
    skia  D  JPEG content is corrupt, got a zero length row(276)
    skia  D  JPEG content is corrupt, got a zero length row(277)
    
I thought once I have the error message, I am done, problem like this must be all over google and stackoverflow... 

Nope, [not this time](https://www.google.com/search?q=skia+JPEG+content+is+corrupt).

There is not much I can do when there is only logs but no error message returned, I can't even detect the problem and reload the images. So I approach to tackle the problem is to reduce the chance of happening instead of fixing it. One observation is that, even this is not a step of reproduce, it usually/always comes with a dalvikvm heap grow. Follow on this direction and tuned a bit memory performance, somehow like harder to hit the problem. (magic?)

This is for sure not a "fix", and "looks harder to hit the problem" could actually be luck, but that's all I can get in a few hour scheduled time.
