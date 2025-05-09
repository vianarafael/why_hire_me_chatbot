# 💸 E.L.I.Z.A.B.E.T.H.

Expense Ledger & Income Zone Assistant for Budgeting, Expenditure, Taxes & Househould-finance.

This is the **backend** for a privacy-first, LLM-enhanced expense tracking system built with **Flask**, **Google Cloud Vision**, **OpenAI**, and **ChromaDB**.

It handles:

- OCR-powered receipt parsing
- CSV ingestion
- Transaction storage
- LLM-powered monthly summaries
- Semantic search using vector embeddings

---

## 🚀 Features

- 📸 **Smart Receipt Uploads**  
  Snap a photo → OCR + GPT parses vendor, date, amount, category

- 📊 **CSV Uploads**  
  Drop bank exports into the system and ingest them into your local DB

- 🧠 **LLM Financial Summary**  
  Generate a monthly report (total spending, top categories, outliers, suggestions)

- 🔍 **Vector Searchable Transactions**  
  All expenses are embedded and stored in a local ChromaDB vector DB — for semantic search and RAG

- 🔌 **Modular Codebase**
  - `Flask` for routing + APIs
  - `OpenAI` for parsing and summarization
  - `ChromaDB` for semantic memory
  - `Google Cloud Vision` or Tesseract for OCR
  - `SQLite` for simple local persistence

---

## 🛠️ Setup

### 1. Clone the project

```bash
git clone https://github.com/yourname/expense-tracker.git
cd expense-tracker
```

### 2. Create a virtual environment

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your environment variables

Create a .env file with the following:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/google/credentials.json
```

## 📡 API Overview

Endpoint Method Description
/upload_receipt POST Upload a photo of a receipt
/upload_csv POST Upload a bank CSV file
/add_expense POST Add an expense manually (JSON)
/transactions GET List all transactions
/transactions/<id> DELETE Delete a transaction by ID
/ GET View summary report (basic HTML)

## 🧠 LLM Summary

Run the following script to generate a GPT-powered monthly spending report (e.g. cron job):

```bash
python rag_query.py
```

## 🧰 Project Structure

```bash
├── app.py                        # Main Flask app
├── utils/
│   └── openai_util.py            # OCR + OpenAI parsing
├── scripts/
│   └── load_db_format_chunks.py  # Format transactions for vector DB
├── rag_query.py                 # Monthly summary via GPT
├── templates/
│   └── report.html               # Jinja template (optional)
├── requirements.txt
├── .env
```

## 📫 Contributing

Feel free to fork, star, or yell at me on [Twitter](https://x.com/vianarafaelds).


