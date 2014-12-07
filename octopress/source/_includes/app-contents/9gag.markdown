
## 9GAG Android (2013 - 2014)

### Description

The 9GAG official Android app provides native Android experience to their large user base. The app supports all core features available on 9GAG web site including viewing posts in different lists, login, upvote, comment and share. This app got over 5M downloads and was featured on Google Play store.

### My role and challenges

I joined 9GAG as their first Android developer, I built the whole Android app from scratch and did weekly release for almost a year. I was also responsible to refactor codes into components for other projects reuse and guide new hired Android developers to pick up the code base.

One of the challenging problem only 9GAG (and may be a few other apps) faces is the [long image problem](http://9gag.com/gag/6394428). As the site supports one image in each post, some creative users tried to concatenate multiple images to one post, or just want to keep other users scrolling, and resulted in very long images. Turned out there is a size limit for ImageView and openGL (mostly 1024px, some newer devices can do 2048px) so I have to implement tile generation in client side, custom view for display, and have to make it usable in ListView.

The image feed is the core of the app, displaying image smoothly is the most important task otherwise users will go for [mobile web](http://m.9gag.com) or other 3rd party apps. So besides doing all the performance tricks for efficient layout and drawing, I have also reviewed some opensource image loader library but cannot find one fit my usage so I developed one myself that optimized for the whole flow of image download, tile generation, display.  

To support large amount of active users, my team and I developed a monitoring system to monitor crashes, server errors, and other abnormal cases and send out alert emails. The monitoring system also allowed us to do A/B testing to compare users usage in different features.

I also developed some code generators to convert config file to java code for multiple build support and manage repetitive code to avoid team making mistake when doing copy and paste.

### Links

* [http://9gag.com](http://9gag.com/)
* [Play store](https://play.google.com/store/apps/details?id=com.ninegag.android.app)

