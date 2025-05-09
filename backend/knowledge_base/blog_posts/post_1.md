---
title: "How I Hacked a Japanese Corporate Exam with a Local AI Model"
excerpt: "What happens when you throw OCR, a local LLM, and a Japanese exam into a DIY RAG pipeline?"
date: "2025-05-07T15:35:07.322Z"
tags: [OCR, RAG, local-LLM, automation]
---

**TL;DR**: I built a DIY RAG pipeline—scraping LINE Campus with Playwright, OCR’ing slides via Google Cloud Vision, embedding everything into ChromaDB, and querying a local Qwen3-14B model—to complete the LINE Green Badge certification with 30/40 correct answers.

### Background

I didn’t memorize flashcards. I didn’t take a course. I don’t even speak fluent Japanese. Instead, I threw together a system: OCR, a vector database, and a local LLM—and let it chew through the entire LINE Green Badge certification material.

The exam is notoriously difficult: the Basic level has about a 60% pass rate, while the Advanced level drops to around 20%. It’s designed to filter out anyone who isn’t fully embedded in the LINE ecosystem (LINE is basically Japan’s version of WhatsApp, but with more ads and APIs).

This post breaks down how I scraped the docs, embedded the content, queried it with an offline LLM, and—yes—ran the exam against it.

---

### Why I Even Bothered

We live in a world where acronyms matter more than skill. Pass the test, get the badge—never mind if you can actually do the work.

And to be honest? I’ve never been good at exams. Even in my native language.

I was gently coerced into taking the exam at work. One minute of reading the material sent me into a drudgery-induced coma. I had a better idea: I wasn’t about to burn my nights drilling corporate trivia I’d never use. Instead, I spent twice as long building an AI to suffer through it for me.

---

### Vanilla LLM

My first attempt was lazy: I fed the exam questions into vanilla GPT. It got 17 out of 40. Not great. Basically the same as guessing—almost as bad as me.

The problem? The real content was locked behind a login and scattered across pages full of images and carousels—slides, diagrams, screenshots with Japanese text baked in.

---

### Scraping & OCR

I built a scraper using Playwright to log in, browse every lesson, and rip out every scrap of data I could get, including:

- Main text content from lessons  
- Canvas-based slide decks (screenshot + OCR)  
- Inline images with embedded text  

Google Cloud Vision handled the OCR. Markdown files were generated for each lesson, combining clean text with the extracted image content. You can see the scraping setup in the [repo](https://github.com/vianarafael/llm-vs-line/):

- `save_cookies.py`: logs into LINE Campus and dumps cookies  
- `scrape_shiken.py`: scrapes the LINE Green Badge course pages (Basic & Advanced)  
- `scrape_manabu.py`: pulls extra training material from the general LINE official account courses  

Everything was converted into local `.md` files—ready for chunking, embedding, and querying.

---

### LLM + RAG

Once I had all the course content—lesson text, slide OCR, and image captions—I chunked it into paragraphs and embedded everything using Hugging Face sentence-transformers. Then, I dumped the embeddings into ChromaDB. I used Qwen3-14B, running locally on my RTX 3060, wired into a basic RAG pipeline.

**Result:** 30 out of 40 correct answers. Pretty good. But not quite enough to pass.

---

### Few-Shot Prompting

After trial and error—and ironically, actually learning a thing or two about the services—I added curated examples to a `FEW_SHOTS = [...]` list:

```python
FEW_SHOTS = [
    (
        "…sample question text 1…",
        """Answer:
            - …correct option full text…
            Reason:
            …short justification…"""
    ),
    # 3–8 more high-value examples
]
```

## LLM + RAG + Few-Shot Prompting + Human Supervision

It still got some questions wrong - including ones from the few-shot list. So I manually corrected those during the test.

And then...

🟢 I passed.

![My Badge](/assets/blog/line.png)

I spent a week building this. I guess I could have just studied.

But memorizing random services (wink wink AWS Certification) wasn’t nearly as fun as using tech to beat the system.

I had fun. I got the result I wanted.

<b>Fuck. LLMs are awesome</b>.

[The Repo](https://github.com/vianarafael/llm-vs-line/)

#
