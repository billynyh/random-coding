---
layout: post
title: "Android XMPP Development"
date: 2014-09-28 15:31:48 +0800
comments: true
categories: [android, xmpp]
---

I was working on a chat feature on Android last two months using the aSmack library, here are some notes for future reference, although some detail may already not applicable for latest version of smack.

[Smack](https://github.com/igniterealtime/Smack)

{% blockquote %}
Smack is a library for communicating with XMPP servers to perform real-time communications, including instant messaging and group chat.
    
Extremely simple to use, yet powerful API. Sending a text message to a user can be accomplished in only a few lines of code
{% endblockquote %}


[aSmack](https://github.com/Flowdalic/asmack)

{% blockquote %}
buildsystem for Smack on Android
{% endblockquote %}

## Integration

The sample code is very simple, just create a connection object, .connect(), .login(), create a chat object and send. But to integrate to Android, of course we need to do it in a background service, and here are the items I personally found difficult to handle well.

* Handle connection state, connection listener seems not handle all connection events
* May stuck in strange login state
* User do action while connecting
* Decide when to close the connection and stop background service
* Smack does not have much doc 
* aSmack does not have doc at all
* Smack is still in development
* Not so extensible in some cases and it is hard to modify the library

## Customized login method

If you customized the xmpp server to provide custom authenticate logic to integrate to external service, you can extends SASLMechanism in client side to support that. However, the authenticate call only accept jid and password parameter, and you may need to do some hack to pass more data to it if your authentication api required. Also, the response format of the login call is very limited, you cannot return extra customized error message so there may be some troubles when you want to have different handling on error cases in client side.

## Customized IQ

Adding customized IQ is quite easy in smack, though you need it in a few places and may not work if you missed one. For one IQ type, you need to be clear on two things, the format you sent out and the format you receive. For the ease of development, you may want to put both implementation in one class, just make sure you don't messed with it.

For sent out, you actually just need to construct the xml string and return in getChildElementXML(), no other setup needed. 

For receiving IQ response, first you need to create IQProvider and add to ProviderManager, matching the xmlns in the query object. The IQProvider is used to convert the response packet to your customized IQ object. Then you need to extends PacketListener, and when you create the connection object, add the listener to it, with a PacketTypeFilter to match your IQ class. With both provider and listener setup correctly, you should be able to receive the response of the IQ.

## XEP 0198 - stream management

I have no knowledge of XMPP before working on this project (actually still don't know much about the protocol), but after implemented the basic program flow, we found that it is easy to trigger some message lost conditions. Turned out that xmpp is designed for stable network condition, so the support of mobile usage is actually quite bad.

* http://fnanp.in-ulm.de/blog/2014/01/16/01-woes.html
* http://op-co.de/blog/posts/mobile_xmpp_in_2014/

An extension XEP 0198 is targeted for the message lost condition, I am not sure if it can really solve the problem, but at the time I started the development around end of July, XEP 0198 is not supported in Smack. The project seems quite active and the latest alpha version of Smack (4.0) seems included stream management but seems they have quite many changes and need some time to migrate from older version so I have not tried it yet. Also Smack 4.0 have Android support integrated so no need to use aSmack anymore.

* https://github.com/igniterealtime/Smack
* https://igniterealtime.jiveon.com/blogs/ignite/2014/09/13/smack-410-alpha1-available


