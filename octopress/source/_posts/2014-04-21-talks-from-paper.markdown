---
layout: post
title: Talks from Facebook, Paper team
date: 2014-04-21 21:10:00 +0800
comments: true
categories: [android, ui, A/B test, facebook, paper]
---

During the long weekend of Easter holiday, I spent some time on watching tech talks from Facebook. The newly uploaded "Building Paper 2014" series is really cool. Even I don't do iOS, seeing how they tackle the problems and share their approach is totally enjoyable. 

Android and iOS apps may have different platform structures, but when your app goes bigger, most likely you will need another level of abstraction to handle large amount of logic, UI and communication betweens components. And when you want further performance tuning, you may need to go beyond the platform like what Paper team did. At that stage, although you are using different languages, the architecture will be similar across platforms.

<div class="video-container">
<iframe src="http://www.youtube.com/embed/ZdiBPHpxGd0" frameborder="0" allowfullscreen></iframe>
</div>

I also like the part about [contextually aware tutorials](https://www.youtube.com/watch?v=-KrF4bIofeo), if you have time, you should watch the [whole event](https://www.youtube.com/watch?v=OiY1cheLpmI).

## UI details and A/B test

Besides new talks, I also watched an old talk from "Mobile Developer Day by Facebook + Parse 2013". Not sure why I skipped this talk before, probably because the title is so generic - [Mobile at Facebook](https://www.youtube.com/watch?v=e2w8z6mI47U). The part that caught my attention is the A/B testing on their drawer to nav bar changes. It's not about what framework they used, not about how many users they put in the AB test, it's about how you see the numbers. 

She mentioned that after changing the drawer to nav bar, the result in internal test is good, navigation experience is improved, users feel the app faster. However, when they shipped to 1% test, they find that users liking and commenting less, because users are kind of distracted by the nav bar notification. 

This is very interesting to me. We do not have a very detailed metrics system on mobile (have some, but not detailed), I am sure if we do AB test like that, we will not be able to see the abnormal usage changes. This even put me in a doubt that what if we already did changes like that and we still don't know that?

This is like a regression test, not on code but on usage.

<div class="video-container">
<iframe src="http://www.youtube.com/embed/e2w8z6mI47U" frameborder="0" allowfullscreen></iframe>
</div>
