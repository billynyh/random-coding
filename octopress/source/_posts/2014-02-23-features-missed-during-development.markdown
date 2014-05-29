---
layout: post
title: "Useful features I missed during Android development"
date: 2014-02-23 19:36:59 +0800
comments: true
categories: android
---


This weekend, I am working on my Muzei extension and try to add a setting page to it. It is not hard to write everything myself, but I was not in the mood of writing code from scratch, so I just copy code from [other opensource project](https://github.com/flavienlaurent/muzeihash). Modifying other's code does not always speed up your development when your task is so simple, but you can take this chance to read other's code at the same time. 

I don't consider myself learned Android development correctly, but I guess most people started like me. I started with a small project, lookup the doc for the features I need, then learn other features while doing other projects.When you learn like this, it is easy to miss out simple features. Here are what I found this week:

## Show divider in LinearLayout

Can't believe I missed this, there was a couple times that I need to append dummy view to act as divider. The worst thing about adding divider view yourself is not the extra code you added, is when you try to control visiblity of elements, you need to handle the dividers also.

{% codeblock lang:java %}
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal"
    android:showDividers="middle"
    android:divider="?android:dividerVertical"
    android:dividerPadding="4dp">
    ...
</LinearLayout>
{% endcodeblock %}

## CheckedTextView

The first time when I want to have checkbox put on the right side of the text, I went through the available options of CheckBox class and cannot find any good, then I go to google and stackoverflow, [first solution](http://stackoverflow.com/questions/5000213/how-to-set-the-checkbox-on-the-right-side-of-the-text) is to put a TextView to the left of CheckBox. Usually I will just stop here and start coding, but it is obviously not good enoguh, as now you can only trigger it by clicking the checkbox but not the whole text+checkbox. 

If you tried the multiple choice feature of ListView, you will see it is exactly the behavior you look for, a little [dig in](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/layout/simple_list_item_multiple_choice.xml) will give you CheckedTextView.

{% codeblock lang:java %}
<CheckedTextView xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@android:id/text1"
    android:layout_width="match_parent"
    android:layout_height="?android:attr/listPreferredItemHeightSmall"
    android:textAppearance="?android:attr/textAppearanceListItemSmall"
    android:gravity="center_vertical"
    android:checkMark="?android:attr/listChoiceIndicatorMultiple"
    android:paddingStart="?android:attr/listPreferredItemPaddingStart"
    android:paddingEnd="?android:attr/listPreferredItemPaddingEnd"
/>
{% endcodeblock %}

You can even extend other layout with [Checkable](http://developer.android.com/reference/android/widget/Checkable.html) interface, more detail [here](http://chris.banes.me/2013/03/22/checkable-views/)
