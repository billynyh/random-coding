---
layout: post
title: "Little experience on solving dex method count limit"
date: 2014-11-01 20:02:45 +0800
comments: true
categories: [android, dex, method limit]
---


I have heard about the dex 65536 method count limit long time ago and I finally meet this problem recently. After digging around, I decided to strip off some unused method in an external jar, using jarjar.

Here are some little steps I used, using asmack jar as example.

### Before fix

    # convert jar to dex
    >> $BUILD_TOOL_PATH/dx --dex --output asmack.dex asmack.jar
    # method count
    >> dex-method-count asmack.dex
    5584
    >> dex-method-count-by-package asmack.dex
    ...
    113 com.novell
    ...
    61  de.measite
    ...
    1894    org.jivesoftware.smack
    ...
    3585    org.jivesoftware.smackx
    ...
    423 org.apachea
    ...

### Create rule.txt with this line
    
    zap org.jivesoftware.**

### Run jarjar

    # run modify jar
    >> java -jar jarjar.jar process rule.txt asmack.jar asmack-modified.jar

    # build dex file again
    >> $BUILD_TOOL_PATH/dx --dex --output asmack-modified.dex asmack-modified.jar

    # see the difference
    >> dex-method-count asmack-modified.dex
    554

 


## Reference

* https://code.google.com/p/jarjar/
* https://medium.com/@rotxed/dex-skys-the-limit-no-65k-methods-is-28e6cb40cf71
* http://jakewharton.com/play-services-is-a-monolith/
* dex.sh - https://gist.github.com/JakeWharton/6002797 




