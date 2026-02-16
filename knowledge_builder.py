import os
from sentence_transformers import SentenceTransformer
from langchain_huggingface import HuggingFaceEmbeddings
import pandas as pd
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import time

# ─── Load Gemini API Key ─────────────────────
os.environ["GOOGLE_API_KEY"] = "api_key"

# ─── Embeddings Function ───────────────────
embedding_function = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# ─── Load CSV ──────────────────────────────
df = pd.read_csv("ai_job_dataset.csv")

# ─── Custom Text Splitter ──────────────────
def split_text(text, chunk_size=1000, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

# ─── Convert rows into documents and split ──
all_chunks = []
for _, row in df.iterrows():
    row_text = "\n".join([f"{col}: {row[col]}" for col in df.columns])
    chunks = split_text(row_text)
    all_chunks.extend(chunks)

print(f"Total chunks to embed: {len(all_chunks)}")

# ─── Create Chroma Vector Store ───────────
chroma = Chroma(
    persist_directory="./chroma",
    collection_name="job_dataset",
    embedding_function=embedding_function
)

# ─── Add documents in batches ─────────────
BATCH_SIZE = 50  # adjust based on memory / API limits
for i in range(0, len(all_chunks), BATCH_SIZE):
    batch = all_chunks[i:i+BATCH_SIZE]
    documents = [Document(page_content=chunk) for chunk in batch]
    try:
        chroma.add_documents(documents)
        print(f"Batch {i//BATCH_SIZE + 1} added ({len(batch)} docs)")
    except Exception as e:
        print(f"Error embedding batch {i//BATCH_SIZE + 1}: {e}")
        time.sleep(5)  # wait and retry if needed
