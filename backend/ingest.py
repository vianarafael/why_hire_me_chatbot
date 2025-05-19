import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import MarkdownLoader
from langchain.docstore.document import Document

def load_markdown_files(folder_path):
    docs = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                loader = MarkdownLoader(path)
                docs.extend(loader.load())
    return docs

def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.split_documents(docs)

def ingest():
    raw_docs = load_markdown_files("knowledge_base")
    if not raw_docs:
        print("⚠️ No Markdown files found in 'knowledge_base'.")
        return

    print(f"🔍 Loaded {len(raw_docs)} Markdown files.")
    split = split_docs(raw_docs)
    print(f"🧩 Split into {len(split)} chunks.")

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(split, embedding=embeddings, persist_directory="./chroma")
    vectorstore.persist()
    print("✅ Vector store created and saved.")

if __name__ == "__main__":
    ingest()

