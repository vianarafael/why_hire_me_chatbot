# Why-Hire-Me Chatbot

_A GPT-powered “Why Should OpenAI Hire Me ?” assistant + demo interface_

---

## 🚀 Project Overview

Why-Hire-Me Chatbot is a Retrieval-Augmented Generation (RAG) demo that dynamically answers “Why should OpenAI hire Rafael?” by ingesting my résumé, blog posts, LinkedIn summary and extra bio snippets into a semantic vector store, then wiring it to a Flask API and React front-end.  

- **Tech stack**: Python • Flask • LangChain RAG • ChromaDB • OpenAI API • React/Next.js • Docker • Docker Compose  
- **Domain**: Tokyo-based FDE candidate demoing end-to-end build/deploy skills for large-scale, customer-focused AI solutions.  
- **Goal**: Show real business impact—hands-on embedding, LLM integration, full-stack deploy to Docker, Compose, and server.

---

## ⭐️ Key Features

1. **Custom Knowledge Base**  
   - Ingests: résumé (Markdown/PDF), blog posts, extra bio snippets  
   - Automatic chunking & metadata tagging  
2. **Vector Store**  
   - ChromaDB persisted under `backend/chroma/`  
   - Fast semantic search over your career data  
3. **RAG API**  
   - Flask + Gunicorn, listening on port 10000 internally  
   - `/chat` endpoint: accepts JSON `{ question: string }`, returns `{ answer: string }`  
4. **React Front-End**  
   - ChatGPT-style UI with live streaming responses  
   - Next.js rewrite to proxy `/chat` → `api:10000`  
5. **Dockerized & Compose-Orchestrated**  
   - Two containers: **api** (Python) + **frontend** (Node.js)  
   - Bind-mounts for live code & data (`knowledge_base/`, `chroma/`)  
   - One-off index build via `docker-compose run --rm api python3 scripts/build_index.py`  

---

## 📦 Architecture

```text
┌──────────────┐              ┌──────────────┐
│  React UI    │ ── /chat ──▶ |   Flask API  │
│ (3000)       │              │  (10000)     │
└──────────────┘              │              │
                                    ▼
                            LangChain RAG
                            • ChromaDB (/app/chroma)
                            • OpenAIEmbeddings
                            • Knowledge Base (/app/knowledge_base)
```

## ⚙️ Quickstart (Local)

### 1. Clone

```bash
git clone https://github.com/vianarafael/why_hire_me_chatbot.git
cd why_hire_me_chatbot
```

### 2. Env vars
```bash
# Copy and configure backend env
cp backend/.env.example backend/.env
# Add your OpenAI key:
# OPENAI_API_KEY=sk-...

# Copy and configure frontend env
cp frontend/.env.example frontend/.env
```

### 3. Build & index 
```bash
docker-compose up --build api
docker-compose run --rm api python3 scripts/build_index.py
```

### 4. Bring up full stack
```bash
docker-compose up -d
```

5. Visit
UI: http://localhost:3000

API: http://localhost:5000/chat

## 📄 Why OpenAI Should Hire Me

**Deep Customer-Focus & FDE DNA**  
Built this demo to solve the exact ask: translate my profile into a fully operational, LLM-driven solution.

**End-to-End Technical Delivery**  
From data ingestion and RAG pipelines to Dockerized microservices, zero-touch deploy, and real-time chat UI.

**Hybrid Bilingual Expertise**  
Fluent in English & Japanese, bridging technical teams and strategic customers across Asia Pacific.

**Measured Impact & Thought Leadership**  
Published author, Dev Summit speaker (2024 & 2025 Tokyo), award-winning track record at Nomura & Huge Inc.

**Operational Excellence**  
Comfortable on cloud infra (GCP, AWS), container orchestration, and low-touch scaling—from MVP to production.

🔗 **Live Demo:** https://why-hire-me.rafaelviana.com  
