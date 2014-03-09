---
layout: post
title: "Try out Quartz Composer and Origami"
date: 2014-03-09 19:59:11 +0800
comments: true
categories: 
---

In late Jan, I watched a [talk - Bringing Beautiful Interactions to Android Apps](https://www.youtube.com/watch/?v=s5kNm-DgyjY) from Facebook about how they use Quartz Composer(QC) when developing Facebok Home (and chat head). Compare to other prototyping tools, QC can better illustrate animations and interactions. It is quite impressive and I actually installed QC the day after and tried to play on it. But when I first opened it, I was totally lost, not saying it is hard to use, but it is obvious that there is a learning curve on this tool. I did not spend more time on it that time but kept it in my TODO list.

<div class="video-container">
<iframe src="http://www.youtube.com/embed/s5kNm-DgyjY" frameborder="0" allowfullscreen></iframe>
</div>

Two weeks later, Facebook released [Origami](http://facebook.github.io/origami/), an extension of QC. Followed with some articles about how it is used in Facebook. Yesterday I gave it another try. This time I am more serious compared to last time. My target is at least understand (not fully) how it works and be able to do a simple demo to my team. 

##Let's start
This time I started with the [documentation](https://developer.apple.com/library/mac/documentation/graphicsimaging/conceptual/quartzcomposeruserguide/qc_intro/qc_intro.html), not saying it is poorly documented, but it is not much fun to read it(my bad)... Then I went for tutorials, after a quick look of some articles on QC (not Origami), I had little concept of patches (but missed macro patch...), then I think maybe I can understand the Origami examples.

When I opened the "Photo Grid" example, I only see three patches, I knew that there must be some hierarchy hidden from the interface, I tried to use the patch inspector to look around but have no idea where to go, I was stuck again. Then I found this [video](http://vimeo.com/85578380) on Origami's twitter, which turned out was everything I needed.

<div class="video-container">
<iframe src="http://player.vimeo.com/video/85578380" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> 
</div>

    It is the visual version spaghetti code // 6:50

##Short notes

* "Phone" patch is the basic component for the phone prototype, which displays an image in device frame.
* Use "Render in Image" for the content to display.
* Double click the "Render in Image" patch to edit the macro patch of it.
* A "Layer" patch will be automatically added when you drag in an image.

<img src="{{root_url}}/images/posts/20140309/qc-1.jpg"/></p>

##Reference
* http://facebook.github.io/origami/
* [Introducing Origami for Quartz Composer](https://medium.com/the-year-of-the-looking-glass/f1173d0bd181)
* [Facebook Paper Has Forever Changed the Way We Build Mobile Apps](http://www.wired.com/wiredenterprise/2014/03/facebook-paper/)
* [Vimeo - Prototyping with Facebook Origami](http://vimeo.com/85578380)
    * Asset for the example https://github.com/jaythrash/spy-book
* [Youtube - Bringing Beautiful Interactions to Android Apps - Mobile @ Scale](https://www.youtube.com/watch/?v=s5kNm-DgyjY)
