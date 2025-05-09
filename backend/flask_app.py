import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from openai import OpenAI

load_dotenv()

app = Flask(__name__)
CORS(app)  
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
vectorstore = Chroma(
    persist_directory="./chroma",
    embedding_function=embeddings
)

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    resp = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user", "content": prompt}]
    )
    return jsonify(answer=resp.choices[0].message.content)

if __name__ == "__main__":
    app.run(debug=True, port=7860)
