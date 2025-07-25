---
authors:
- fbetteo
categories:
- AI
- Machine Learning 
comments: true
date: 2025-07-25
description: How Karpathy uses LLMs
draft: false
slug: how-karpathy-uses-llms
tags:
- Machine Learning
---

# How Karpathy uses LLMs

[Original video from Andrej Karpathy.](https://www.youtube.com/watch?v=EWvNQjAaOHw)

---
Models are good at writing.

We collaborate with the assistant in the creation of the context window, both providing tokens, by message or by generation.


**We must be careful with the context**   
The longer the context, the more the model can get "distracted" by old tokens, reducing accuracy.  
With longer context, generation becomes a bit more expensive (computationally) and so the model is slowed down a bit.   
It's the working memory. We should keep it simple and short to make it work better. If the long context is relevant well, then use it of course.
He suggests to start new conversations to clean up the context and obviously when you change subjects.


#### Thinking models

He uses 4o usually but when he thinks the answers could be better, he tries a thinking model. Of course, he doesn't do this for simple questions but for example, for not obvious coding problems.

### How to use Search Tool

Think about it as googling and inserting a bunch of internet text in the context and then it goes back to your question and tries to answer with all the relevant information got from the internet.

Some models detect that they need to search because the question is recent and they use it automatically but  if you know it's needed, just use the search tool. Questions that need recent information require search because the pretraining happened several months ago and have a training cutoff.


### Deep Research
...

### File Upload
Similar, it probably just uploads the text into context.
He starts by asking "can you summarize this paper?"

He reads and uses LLMs. He copy/paste the chapter he is reading to the LLM. "Please summarize this chapter to starts". He reads summary, then he reads the actual book and ask questions. His retention and understanding increases a lot. Specially useful for fields you are not an expert or old books with different language / context / culture.


### Code interpreter

Use python to answer questions, such as calculations that you should do with a calculator at least.

### Advanced Data analysis

Kind of a Junior data analyst.
Needs verification, it might do some assumptions without telling or hallucinate.


### Claude Artifacts

He asked for Flashcards based on the chapter of a book and then asked the artifact to create an app to use those flashcards and the app is usable in the browser.

He doesn't use much but he finds useful to create diagrams.


### Cursor
He uses apps for AI coding, Cursor right now. Using web interpreter is too slow.

### Audio

He speak to models regularly (in the phone or computer)

#### Microphone 
The microphone is to transcript what you say into text (in cellphone)

In computer you don't have the microphone button, you have the audio logo. He then uses some app to transcripts (whisper superwhisper   )
But this doesn't work super well for libraries and programs, and etc. He types that kind of content.
Anyways, this is "fake audio" since in reality is sending the audio as text to the context

There are text to audio apps if you are not using chatgpt which has the functionality 

#### Real audio
Advanced voice mode in chatgpt. 
Here the voice is handled natively in the model, converting into tokens and outputting audio if you want (maybe it's the only option)
It's a bit annoying and rejects many requests but still really insteresting.

### Images

Transform the images into tokens and fill the context. In the end the transformer/model doesn't know that the input originally was an image, they are just tokens for it, but we can know at the decondig stage.

For real use cases, he shows a nutritional table and he wants to know more about the "ingredients".
He uses 2 stages, first transcribe the image, so we can be sure that the model is reading correctly the image.
And then ask questions about the content.

Also for evaluating mathematical formulas.
Paste image, transcript and then ask questions.


Dalle3 outputs (images) are not the direct output of the neural net. It generates a caption and under the hood sends it to another model that is an image generator.

### Video
In advanced mode, there is a video mode where you can ask questions about what you are pointing your phone to.



### Memory

Every new chat erases the whole context but there is a way to keep something in memory across chats (when you see "Memory updated"). Usually you need to invoke it, ask for it to remember.

These memories (what it knows about you) are always prepended to the contexts so it's always available with some things personalized for you.

Custom Instructions. You can tune chatgpt to your like, give it identity and traits.

### Custom GPTs

He uses them mostly for specific actions, like generate flashcards for korean vocabulary