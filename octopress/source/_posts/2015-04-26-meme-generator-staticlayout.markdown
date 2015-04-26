---
layout: post
title: "Implement meme generator with StaticLayout"
date: 2015-04-26 15:56:48 +0800
comments: true
categories: [android]
---


Two months ago I started writing a meme generator as a side project, what I want to do is not just adding two lines of text on image but a more generic text-on-image solution. 

# StaticLayout 

When implementing custom views, we can use canvas.drawText to display text, but if you want to draw text in multiple lines, a straight forward way is to calculate the y position of each line and draw them one by one. One problem with this method is that, you have to do the line splitting yourself and it seems lots of work.

[StaticLayout](https://developer.android.com/reference/android/text/StaticLayout.html) is a less well-known class in the framework, it is not included in any API Guides or Training documentation. 

> This is used by widgets to control text layout. You should not need to use this class directly unless you are implementing your own widget or custom display object, or would be tempted to call Canvas.drawText() directly.

But if you take a quick look of inside TextView (like 5000 lines, I have not read it in detail), you will find that StaticLayout is used to do the text layout.

# Meme generator structure

## RendererView

A custom view that extends ImageView to provide text on image drawing ability, the actually text drawing logic is implemented in the renderer.

{% codeblock lang:java %}
public class RendererView extends ImageView {
    private Renderer mRenderer;

    // fill in constrcutor
    
    public void setRenderer(MemeRenderer renderer) {
        mRenderer = renderer;
    }


    @Override
    protected void onDraw(Canvas canvas) {
        super.onDraw(canvas);
        if (mRenderer != null) {
            mRenderer.draw(canvas);
        }

    }
}
{% endcodeblock %}

## TextGroup

A basic TextGroup manages the text, Paint and StaticLayout object. 

To draw text with stroke, we need to draw it twice, first draw the stroke (using Paint.Style.STROKE), then draw the text over it. I use a wrapper TextGroup interface to wrap the text and the stroke layout, and can extend to arbitrary number of text layer.


## Renderer

Renderer implements a draw(canvas) function to draw text on canvas. In the case of meme generator, the renderer contains two TextGroup, top and bottom. In the draw function, we translate to proper position and run the draw function implemented in the TextGroup.

{% codeblock lang:java %}
@Override
public void draw(Canvas canvas) {

    // some calculation

    canvas.save();
    canvas.translate(x, topY);
    mTopGroup.draw(canvas);
    canvas.restore();

    canvas.save();
    canvas.translate(x, bottomY);
    mBottomGroup.draw(canvas);
    canvas.restore();

}
{% endcodeblock %}

<img src="{{root_url}}/images/posts/20150426/meme-1.jpg" width="300px" />

## AutoResizer

With the help of StaticLayout, you can get the line count of your current layout and can adjust your text size to provide an auto resize function.


# Play store submission

When I tried to upload my meme generator demo to play store, the new review system rejected my submission as some meme may have copyright issue... So I just changed my images to some free stock photo to get pass the review process.

Here is my [demo app](https://play.google.com/store/apps/details?id=io.github.billynyh.meme)



# Future work

With the structure I have, I suppose it is easy to modify the app to provide different style/layout and create use case other than meme generator. I have few ideas in mind but that may require other data api and image source to make it works.



# Reference

* http://stackoverflow.com/a/8369690/3623175
* http://stackoverflow.com/a/12921000/3623175
* http://www.ivity.asia/2010/12/29/using-android-text-staticlayout/
* http://andrdev.blogspot.hk/2012/04/drawing-text-on-canvas.html

