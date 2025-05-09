
import os, glob
from dotenv import load_dotenv
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv(override=True)
db_dir = "./chroma"

# 1. Load docs with metadata
folders = glob.glob("./knowledge_base/*")
documents = []
for folder in folders:
    loader = DirectoryLoader(
        folder,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs={'encoding':'utf-8'}
    )
    docs = loader.load()
    for d in docs:
        d.metadata["source"] = os.path.basename(folder)
    documents.extend(docs)

# 2. Split
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
chunks = splitter.split_documents(documents)

# 3. Embed & persist
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", chunk_size=1000)
if os.path.isdir(db_dir):
    Chroma(persist_directory=db_dir, embedding_function=embeddings).delete_collection()
Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=db_dir,
)
print("✅ Index built:", len(chunks), "chunks")

