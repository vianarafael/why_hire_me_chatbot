---
title: "I Built a Tiny Offline Linux Teacher with Phi-2"
excerpt: "Because I'm tired of copy-pasting commands I don't understand, I built an offline tutor that explains commands in plain language using a tiny local LLM."
date: "2025-04-28T15:35:07.322Z"
tags: [Phi-2, Linux, RAG, ChromaDB, embeddings]
---

**TL;DR**: I resurrected an old ThinkPad, built a local RAG pipeline with Microsoft’s Phi-2 (2.7B parameters), ChromaDB, and MiniLM embeddings—now I run any shell command with `wtf <cmd>` to execute it and immediately get a clear, contextual explanation, all completely offline.

## Background

Last year I converted an ancient laptop into a home server. My Linux skills were basic—navigation, file moves, minimal commands—so I kept asking ChatGPT to explain every new command. That constant context-switching felt inefficient.

What if my terminal could teach me, right after I executed each command?

## Constraints

- **No GPU**  
- **Limited RAM**  
- **Outdated CPU**  
- **No paid APIs**

I needed a small, self-sufficient model trained on computing topics. Enter Microsoft’s Phi-2.

## System Architecture

1. **Knowledge Collection**  
   Gathered Linux textbooks and community-written TLDR command pages into a focused KB.  
2. **Smart Chunking**  
   Split text into ∼200-token, self-contained paragraphs so Phi-2 sees only relevant context.  
3. **Vector Transformation**  
   Used MiniLM to embed chunks into a semantic space.  
4. **Local Vector Database**  
   Stored embeddings in ChromaDB for fast, semantic retrieval.  
5. **Retrieval & Explanation Pipeline**  
   - Shell command → embed command text  
   - Query ChromaDB for top-3 relevant chunks  
   - Send those chunks + “Explain this command” prompt to Phi-2  
   - Display explanation after command runs  

## Usage

I wrapped it in a shell function:

```bash
wtf() {
  "$@"
  explain_command=$(python3 explain.py "${*}")
  echo -e "\n📖 Explanation:\n$explain_command"
}
```
Now wtf ls -la lists files and then prints a concise, human-friendly explanation drawn from my KB.

Refinement
Through prompt tuning and retrieval-filter constraints, I ensured explanations are factual and backed by KB content—no hallucinations.

Outcome
Offline & Free: No API costs, no internet required.

Practical: Fast enough on old hardware to be part of my daily workflow.

Educational: I understand every flag and option as I use it.

In an era chasing massive cloud models, there’s something empowering about running a capable AI tutor on a decade-old ThinkPad.

 [The Repo](https://github.com/vianarafael/rafterai)
