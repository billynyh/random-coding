---
layout: post
title: "First play on Muzei"
date: 2014-02-16 23:05:43 +0800
comments: true
categories: [android, muzei, github]
---

[Muzei live wallpaper](https://github.com/romannurik/muzei) is a new opensource project from Roman Nurik which provide a nice API for other developers to build extension on it easily. Just a few days after its release on Feb 12, you can already find quite many different [data source](https://play.google.com/store/search?q=muzei&c=apps) for it. So I played for a while today and found that it is... really easy to implement your own data source.

Here is a quick start on creating the extension.

{% codeblock lang:java %}

public class MyArtSource extends RemoteMuzeiArtSource {
    
    private static final int UPDATE_INTERVAL = 60 * 60 * 1000; // 60min
    
    public MyArtSource() {
        super("my-art-source");
    }


    @Override
    public void onCreate() {
        super.onCreate();
        setUserCommands(BUILTIN_COMMAND_ID_NEXT_ARTWORK); // manual switch image
    }
    
    @Override
    protected void onTryUpdate(int reason) throws RetryException {
        // fetch title, imageUrl, id, url from remote or hardcode

        publishArtwork(new Artwork.Builder()
            .title(title)
            .imageUri(Uri.parse(imageUrl))
            .token(id)
            .viewIntent(new Intent(Intent.ACTION_VIEW, Uri.parse(url)))
            .build());
     
        scheduleUpdate(System.currentTimeMillis() + UPDATE_INTERVAL); // switch image after 60min
    }
}
{% endcodeblock %}

You can find my Muzei 9GAG extension on [Play store](https://play.google.com/store/apps/details?id=com.billynyh.muzei9gag), source code available on [Github](https://github.com/billynyh/android-muzei-9gag)
