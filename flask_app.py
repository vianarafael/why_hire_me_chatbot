import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from openai import OpenAI

# Load environment
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# 1️⃣ Initialize Chroma (load persisted vectorstore)
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
vectorstore = Chroma(
    persist_directory="./chroma",
    embedding_function=embeddings
)

# 2️⃣ Initialize OpenAI chat client
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "")
    # 3️⃣ Retrieve top-k chunks
    # returns a list of Document objects
    chunks = vectorstore.similarity_search(question, k=4)
    context = "\n\n".join([chunk.page_content for chunk in chunks])

    # 4️⃣ Build prompt
    prompt = f"""
You are Rafael's AI assistant. Use the context below to answer the user's question in a persuasive, factual, and concise way.

Context:
{context}

Question:
{question}

Answer:
"""
    # 5️⃣ Call GPT-4o
    resp = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"user", "content": prompt}]
    )
    return jsonify(answer=resp.choices[0].message.content)

if __name__ == "__main__":
    app.run(debug=True, port=7860)
