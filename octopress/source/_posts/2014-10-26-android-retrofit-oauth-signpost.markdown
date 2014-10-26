---
layout: post
title: "Android OAuth with signpost and retrofit"
date: 2014-10-26 17:34:45 +0800
comments: true
categories: [android, oauth, retrofit, signpost]
---

This week I finally got time to play with square's retrofit library. The first thing I wanted to try is to use it to for Twitter API. I immediately met a problem - how to do oauth? I was hoping retrofit would just work out of the box, but I can't find any example in the site, and even not much results when google/stackoverflow around.

It seems that twitter4j provide full support of twitter api from oauth to getting posts, but as my goal is to try out retrofit, I decided not to use twitter4j at this point. Moreover, I will call different api later so it's better for me to figure out how to do oauth on Android.

## Scribe-java

I first found this [Scribe](https://github.com/fernandezpablo85/scribe-java) java library, I like the way the author describe the library.

    Who said OAuth was difficult? Configuring scribe is so easy your grandma can do it! check it out:
   
 And it supports many existing oauth library including Google, Facebook, Yahoo, LinkedIn, Twitter, etc...  It is easy to find [example on integrating scribe with android](http://schwiz.net/blog/2011/using-scribe-with-android/). I tried this library and can successfully get pass the authorization steps, but one problem is that the library wrapped the request object so it may not work well with retrofit, I stopped here and did not dig deeper with this library even I like this a lot.

## Signpost

Then I tried [Signpost](https://code.google.com/p/oauth-signpost/) ([github](https://github.com/mttkay/signpost)), this is a simple library that focus on signing the request and does not wrap request with custom object. Not like Scribe, Signpost does not implement any existing service, but implementing one is just providing the corresponding oauth api url.

{% codeblock lang:java %}
OAuthConsumer consumer = new DefaultOAuthConsumer(
        API_KEY, API_SECRET);

OAuthProvider provider = new DefaultOAuthProvider(
        "https://api.twitter.com/oauth/request_token",
        "https://api.twitter.com/oauth/access_token",
        "https://api.twitter.com/oauth/authorize");
{% endcodeblock %}

The Android integration of signpost is similar to scribe. After the authorization steps, it can hook into retrofit by [extending the client](https://gist.github.com/julianshen/5889097). 

Here is my code for integration - [gist](https://gist.github.com/billynyh/9e96d228b0e64c7c3251)



## Reference

* Signpost
    * https://github.com/mttkay/signpost
    * https://code.google.com/p/oauth-signpost/
    * https://gist.github.com/julianshen/5889097
    * http://julianshen.blogspot.hk/2013/06/android-retrofit-signpost-retrofitoauth.html
    * https://github.com/square/retrofit/issues/185

* Scribe
    * https://github.com/fernandezpablo85/scribe-java
    * https://github.com/fernandezpablo85/scribe-java/wiki/getting-started
    * [scribe twitter example](https://github.com/fernandezpablo85/scribe-java/blob/master/src/test/java/org/scribe/examples/TwitterExample.java)


