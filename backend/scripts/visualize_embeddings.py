# scripts/visualize_embeddings.py

import os, glob, shutil
import numpy as np
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from collections import defaultdict

load_dotenv(override=True)
db_dir = "./chroma"
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    chunk_size=1000
)
vectorstore = Chroma(persist_directory=db_dir, embedding_function=embeddings)

col = vectorstore._collection
result = col.get(include=["embeddings", "documents", "metadatas"])
vectors = np.array(result["embeddings"])
docs = result["documents"]
mds = result["metadatas"]

print(f"Number of documents: {len(docs)}")
print(f"Number of embeddings: {len(vectors)}")
print(f"Number of metadata entries: {len(mds)}")

if len(docs) == 0:
    print("No documents found in the vector store. Please ensure you have added documents to the store.")
    exit(1)

n_samples = len(vectors)
if n_samples <= 1:
    print("Not enough samples to perform t-SNE visualization")
    exit(1)

perplexity = max(1, min(30, n_samples - 1))
print(f"Using perplexity value: {perplexity}")
tsne = TSNE(n_components=2, random_state=42, perplexity=perplexity)
coords = tsne.fit_transform(vectors)

doc_types = [metadata.get('doc_type', 'unknown') for metadata in mds]
unique_types = list(set(doc_types))
print(f"Found document types: {unique_types}")

color_map = {
    'about': 'blue',
    'blog_posts': 'green',
    'projects': 'red',
    'resume': 'orange',
    'unknown': 'gray'
}

colors = [color_map.get(doc_type, 'gray') for doc_type in doc_types]

fig, ax = plt.subplots(figsize=(10, 8))
scatter = ax.scatter(coords[:,0], coords[:,1], c=colors, s=10, alpha=0.7)

legend_elements = [plt.Line2D([0], [0], marker='o', color='w', 
                            markerfacecolor=color, label=doc_type, markersize=10)
                  for doc_type, color in color_map.items() if doc_type in unique_types]
ax.legend(handles=legend_elements, title="Document Types")

ax.set_title("2D Projection of Knowledge-Base Embeddings")
ax.set_xlabel("TSNE-1")
ax.set_ylabel("TSNE-2")

plt.tight_layout()
plt.show()
