"""Ingest PDFs from ./data into Qdrant via LlamaIndex + Ollama embeddings.

Run once (and again whenever your docs change):
    python ingest.py
"""
from pathlib import Path

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.core.settings import Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

DATA_DIR = Path(__file__).parent / "data"
COLLECTION = "rag-chatbot"

Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text", base_url="http://localhost:11434")
Settings.llm = Ollama(model="qwen2.5:7b", base_url="http://localhost:11434")

client = QdrantClient(url="http://localhost:6333")
vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

print(f"Loading documents from {DATA_DIR} ...")
documents = SimpleDirectoryReader(DATA_DIR).load_data()
print(f"Loaded {len(documents)} document(s). Indexing ...")

index = VectorStoreIndex.from_documents(documents, storage_context=storage_context)
print(f"Done. Indexed into Qdrant collection '{COLLECTION}'.")
