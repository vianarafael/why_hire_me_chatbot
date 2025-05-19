import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import requests

# Load environment variables
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Flask app setup
app = Flask(__name__)
CORS(app)

# Use HuggingFace embeddings (LangChain-compatible)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Setup Chroma with embeddings
vectorstore = Chroma(
    persist_directory="./chroma",
    embedding_function=embeddings
)

# Mistral API call function
def call_mistral(prompt):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistral-small",  # options: mistral-small, mistral-tiny, mistral-medium
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post("https://api.mistral.ai/v1/chat/completions", headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

# Chat endpoint
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "")
    
    chunks = vectorstore.similarity_search(question, k=4)
    context = "\n\n".join([chunk.page_content for chunk in chunks])

    prompt = f"""
You are ConvinceGPT, Rafael’s personal “get-hired” assistant. Drawing only on the context below, craft an answer that’s:

• Persuasive—sell Rafael’s strengths, not filler  
• Accurate—only use facts from the context  
• Friendly—keep a light, upbeat tone that shows Rafael’s personality  
• Keep it short and concise 

Context:
{context}

Question:
{question}

Answer:
"""
    answer = call_mistral(prompt)
    return jsonify(answer=answer.strip())

# Run app locally (development only)
if __name__ == "__main__":
    app.run(debug=True, port=7860)

