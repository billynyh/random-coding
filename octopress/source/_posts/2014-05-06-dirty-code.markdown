---
layout: post
title: "Write dirty code"
date: 2014-05-06 22:55:49 +0800
comments: true
categories: [dirty, development]
---


## Huh?

As an experienced software engineer, you are expected to write code reusable, modularized, clean, blah blah. Of course you do that in your product, but sometime you need dirty code to do dirty work, and I enjoy doing that. :)

## Code generator

One of my favorite dirty code is code generator. When writing Java, sometime you need to write lots of getter setter, at first you just copy and paste, but after a few months, you will find the class goes big and messy, and it is easy to make mistakes, you may forget to change a variable, or put in wrong default value...

So, how about a little code generator? Make a config file containing the fields and data type, and just generate the java class for you. You don't even need to write the generator in Java, in my case, I have a python script that reads yaml config file and generates Java code.

That script is simple and ad hoc, you are not going to maintain that so when you want to "reuse" it, just copy the script, modify it, do whatever you want.

## Custom build scripts

I have been using ant to build Android for a long time, just migrated to Gradle recently. One of the problem with the old system is lack of multiple build support. What I did in last 3 years is, have a custom ant task that modify the package name in AndroidManifest.xml and update all import of R in code. 

And combine with code generator scripts, I can create builds with different config files which is one very important during development.

It is generally not a good idea to modify every .java files before compile, but with the limitation of the build system and you don't have the resources to dig deep, I would just use the dirty way (proudly).

## Get your hands dirty

After working for some years, we switched our mind set from a programmer to an engineer, we may forget how to get dirty, forget how we used to "hack" things, forget how we rushed a course project in one night. By being a better engineer, we write better code, but we should not lose the ability of being dirty.

Use dirty code to do dirty work is just an example of use the right tool for the task.
