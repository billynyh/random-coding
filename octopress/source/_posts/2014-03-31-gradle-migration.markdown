---
layout: post
title: "Notes on migrating Android project from ant to gradle"
date: 2014-03-31 00:44:28 +0800
comments: true
categories: [gradle, android]
---


Few months ago, I spent a little time to try migrating my Android project from to gradle, although it is announced in last Google IO (May 2013), and saw some big companies switched to it early, I considered that not ready that time and decided to wait for later version.

### Projects structures

The project I am working on used some library projects like pull to refresh, facebook sdk, google play services, etc, due to the limitation of the old ant build system, you have to include the source and compile with your app. We also splitted some of our own components to separate library projects for reuseing in other projects. Currently my app is depending on 14 other library projects, and it takes about 3 minutes to have do a clean build. 

We also use git submodules to include projects from other repositories. I am still not sure if this is the right way to manage projects especially when we keep modifying the libraries. It increases the complexity when we have multiple branches in development, and causes some pains when merging codes.

### First migration attempt

I tried to migrate to gradle few months ago, when Android studio was in version 0.2 I think. One of the unknown part of the migration, it's 0 or 100, no 50% migrated. Even you build every library successfully, it does not mean you are getting close to finish the migration. In my case, I first made a simple app to get familiar with the build system, then migrated my libraries one by one, but guess what I got when I tried to have a complete build? Out of memory... I googled a little bit and found a way to increase the memory limit but still got the same error, in both command line and Android studio. 

I didn't put more time on that since the ant scripts still work at that time and I got (many) other tasks pending.

### Second attempt

I recently reopened the migration task, mainly for 3 reasons.

1. Eclipse can't handle the project anymore. When I tried to add some code in a core library project that is also used in 3 other library projects, eclipse just hangs there and I have to kill it myself. 
2. Need more tools for development. Actually this is one of the reason of my first attempt of migration, I had some (simple) scripts/code generators to help development, some are standalone but some are hooked into the build flow. It does not make sense to keep developing scripts based on ant if there is a migration coming, so I didn't add any scripts in the last 6 months. In order to continue the development, the migration task now becomes a blocker.
3. Team expand. We are expecting more man power on Android, the migration has to be done before they start.

Not like last time, this is no longer a "try out", it has to be done, no matter how many effort required. 

After reinstalling the Android studio and gradle, I still got the out of memory error during compile. At this point, even I can get through the compile task of each library, I may got other error when combining everything in the app project, so I have to do some experiments first. I compiled all library projects to aar and uploaded to local maven repositories, this also required me to modify the build.gradle of the app project to use aar instead of compile form source. With some luck, I can compile the app with those aar successfully.

Next step is to make it fits my development workflow. Some library projects need to compile from source and those relatively stable libraries can use aar. Fortunately it worked as expect and did not gave me out of memory error, and even better, it also worked on Android studio without any extra modification.

Migrating the basic workflow is just the beginning, there are still many things to test before using it to do release, like app signing, proguard, build with different package names, etc... But before those tasks, there is still one problem needed to work on. I am not sure it is just me, but the gradle configure time seems very long with multi projects setup, and it may not suppose to be that slow. I posted my question on [Google plus](https://plus.google.com/u/0/105980838674582844427/posts/8sYLTN6WyCt) and got some quick responses from Xavier Ducrohet. He said the configure time should be around 3s if run with daemon, but what I got is at least 10s for every one, even a simple "gradle projects" command call. I am not sure if this is the best I can get but it would not be a great development experience if every run need to wait for 10s and the actual compile is just 2s. 



