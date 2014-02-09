---
layout: post
title: Two tech talks from Twitter Android team
date: 2013-10-20 23:48:54 +0800
comments: true
categories: [android, twitter]
---

<p>Watched two Android talks from Twitter today, one is about gradle and one about Vine.</p>

### Building Twitter for Android with Gradle 
(by Jonathan Le - https://twitter.com/jle)

<div class="video-container">
<iframe src="http://www.youtube.com/embed/EM5edIJUA10" frameborder="0" allowfullscreen></iframe>
</div>

<p>The gradle one was short, mostly about the migration process of twitter Android team.
Some interesting points from the talk:</p>

#### Twitter app version
* 1.0: 1 committers, Ant, build time 30s
* 4.0: 15 committers, Ant+Ivy, build time 2min
* 5.0: 80 committers, Gradle, build time 24s
#### Gradle process
* setup private Sonatype Nexus repo
* publish aars to nexus

#### Should not use git submodules
* The talk did not include more detail of this...

### Building Vine on Android 
(by Sara Haider - https://twitter.com/pandemona)

<div class="video-container">
<iframe src="http://www.youtube.com/embed/7zamwc2lXhg" frameborder="0" allowfullscreen></iframe>
</div>

<p>Finally have time to watch the whole video, very nice talk, included many technical tricks of building vine app. Some tricks remind me the time I was working on ActionSnap.</p>

#### Playback tricks
* Use MediaPlayer, TextureView(api 14) to play the video
* Autoplay, prefetch 2 videos
* MediaPlay.setLooping(true) is too slow. Early seek to improve the loop behavior

#### Recording
* MediaRecorder has 700ms delay on start,stop
* use PreviewFrame to get images and record audio (wat?)
* need compare timestamp to synchronize audio/video
* use ~140MB memory for full 6 second cut
* largeHeap = true (of coz)
* separate process to get more memory

#### Cusor
* hybrid cursor
* backed by ArrayList (?)
* update list view and write to db in the bg

#### Crash tracking
* Crashlytics
* real time, tonnes of metadata
* <b>zero unknown crashes #adore#</b>

#### Span
* bug on emoji

#### The f-word - fragmentation
* Device specific hack
    * samsung s4 front facing camera strange aspect ratios
    * htc not support multiple MediaPlayers at once
    * Kindle (dumb)
* Default camera not always back camera
