"""Chat against the indexed Qdrant collection.

Run:
    python chat.py
Type a question, get a grounded answer with sources. Ctrl-C / 'exit' to quit.
"""
from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

COLLECTION = "rag-chatbot"

Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text", base_url="http://localhost:11434")
Settings.llm = Ollama(model="qwen2.5:7b", base_url="http://localhost:11434")

client = QdrantClient(url="http://localhost:6333")
vector_store = QdrantVectorStore(client=client, collection_name=COLLECTION)
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)

query_engine = index.as_query_engine(similarity_top_k=4)

print("RAG chatbot ready. Ask a question (Ctrl-C to quit).\n")
while True:
    try:
        q = input("you> ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nbye.")
        break
    if not q or q.lower() in {"exit", "quit"}:
        break
    resp = query_engine.query(q)
    print(f"\nbot> {resp.response}\n")
    for i, node in enumerate(resp.source_nodes, 1):
        src = node.node.metadata.get("file_name", "?")
        print(f"  [{i}] {src} (score={node.score:.3f})")
    print()
