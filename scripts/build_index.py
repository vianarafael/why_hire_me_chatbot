import os, glob, shutil
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv(override=True)

db_name = "./chroma"

# Take everything in all the sub-folders of our knowledgebase 
# those are the result of scraping line campus material (scrape_shinsen.py and scrape_manabu.py)
# since you need to be logged in to access the material I saved the cookies (just ran save_cookies.py and logged in)

folders = glob.glob("knowledge_base/*")

def add_metadata(doc, doc_type):
    doc.metadata["doc_type"] = doc_type
    return doc

text_loader_kwargs = {'encoding': 'utf-8'}

documents = []
for folder in folders:
    doc_type = os.path.basename(folder)
    loader = DirectoryLoader(folder, glob="**/*.md", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
    folder_docs = loader.load()
    documents.extend([add_metadata(doc, doc_type) for doc in folder_docs])

# 1. Split raw docs into small, overlapping chunks (~300 tokens each)
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,         # roughly 300‑350 tokens
    chunk_overlap=150,
)
chunks = splitter.split_documents(documents)   

print(f"Prepared {len(chunks)} chunks.")

# 2. Create an embedding object that will respect OpenAI limits
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",  # very fast, good quality
    chunk_size=1000                   # ≤200 chunks per API call → ≤~60k tokens
)

# 3. (Re)build the vector DB
if os.path.exists(db_name):
    Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=db_name,
)
print(f"Vectorstore ready with {vectorstore._collection.count()} chunks.")
