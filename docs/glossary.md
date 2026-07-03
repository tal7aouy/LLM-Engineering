# LLM Engineering Glossary

> 100+ terms, plain-English definitions. Alphabetical. PRs welcome.

| Term | Definition |
| --- | --- |
| **A2A** | Agent-to-Agent protocol (Google, 2025) for inter-agent communication. |
| **Agent** | LLM system that plans, calls tools, and iterates toward a goal. |
| **Agentic RAG** | RAG where an LLM agent drives multi-step retrieval + reasoning. |
| **Attention** | Mechanism weighing token relevance; core of transformers. |
| **AWQ** | Activation-aware Weight Quantization (INT4); fast on GPU. |
| **BM25** | Sparse lexical retrieval algorithm (TF-IDF-like). |
| **BPE** | Byte-Pair Encoding; common tokenization scheme. |
| **Chain-of-Thought (CoT)** | Prompting the model to reason step by step. |
| **Chunking** | Splitting documents into retrievable units. |
| **Computer Use** | Agent driving a real GUI (mouse/keyboard) via vision. |
| **Context engineering** | Designing everything in the context window (2026 superset of prompt engineering). |
| **Context window** | Max tokens a model can process in one request. |
| **Continuous batching** | Batching new requests mid-flight in an inference engine. |
| **CRAG** | Corrective RAG; scores retrieval, falls back to web search. |
| **DPO** | Direct Preference Optimization; preference learning without a reward model. |
| **Embedding** | Dense vector representing text/image meaning. |
| **Episodic memory** | Memory of past events/interactions. |
| **FAISS** | Facebook's local vector search library. |
| **Few-shot** | Providing examples in the prompt to guide output. |
| **Fine-tuning** | Updating model weights on task-specific data. |
| **FlashAttention** | Memory-efficient attention implementation. |
| **Function calling** | Model emitting structured calls to external functions. |
| **GGUF** | Quantized model format for llama.cpp / Ollama. |
| **GRPO** | Group Relative Policy Optimization; RL method used by DeepSeek-R1. |
| **Hallucination** | Confident output not grounded in facts. |
| **HITL** | Human-in-the-loop; human approval before agent actions. |
| **HyDE** | Hypothetical Document Embeddings; embed a generated answer for retrieval. |
| **Inference** | Running a model to produce output. |
| **Instructor** | Library for structured LLM outputs via Pydantic. |
| **KV cache** | Cached key/value tensors speeding autoregressive generation. |
| **LangChain** | LLM orchestration framework. |
| **LangGraph** | Stateful agent graph framework (LangChain). |
| **Letta** | Agent memory/state framework (ex-MemGPT). |
| **LiteLLM** | Unified proxy over many LLM providers/engines. |
| **LLaVA** | Open vision-language model. |
| **LoRA** | Low-Rank Adaptation; PEFT method. |
| **Lost in the middle** | Models recall start/end of context better than middle. |
| **MCP** | Model Context Protocol; standard for LLM↔tools. |
| **mem0** | Self-improving memory layer for agents. |
| **MCTS** | Monte-Carlo Tree Search; used in some reasoning approaches. |
| **Mixture-of-Experts (MoE)** | Architecture routing tokens to expert sub-networks. |
| **Multimodal** | Model handling multiple modalities (text+image+audio). |
| **Nucleus sampling** | Sampling from the smallest token set with cumulative prob ≥ p (top-p). |
| **Ollama** | Easiest local LLM server. |
| **ORPO** | Odds Ratio Preference Optimization; no reference model needed. |
| **PagedAttention** | vLLM's efficient KV-cache memory management. |
| **PEFT** | Parameter-Efficient Fine-Tuning (LoRA, QLoRA, etc.). |
| **pgvector** | Postgres extension for vector similarity search. |
| **Plan-and-Execute** | Agent pattern: plan steps, then execute each. |
| **Prefix caching** | Reusing KV cache for shared prompt prefixes. |
| **Prompt caching** | Provider feature caching static prefix tokens. |
| **Qdrant** | Open-source vector database. |
| **QLoRA** | Quantized LoRA; fine-tune big models on small GPUs. |
| **Quantization** | Reducing model precision (INT4/8) to save memory. |
| **RAG** | Retrieval-Augmented Generation. |
| **RAGAS** | RAG evaluation framework (faithfulness, relevance, recall). |
| **ReAct** | Reason + Act agent pattern. |
| **Reasoning model** | Model trained for extended inference-time thinking (o1, R1). |
| **Reflexion** | Agent pattern with self-critique + retry. |
| **Reranking** | Re-scoring retrieved results for relevance (Cohere, BGE). |
| **RLHF** | Reinforcement Learning from Human Feedback. |
| **Safetensors** | Safe model serialization format (no code execution). |
| **Self-RAG** | RAG where the model decides when to retrieve + self-critiques. |
| **SFT** | Supervised Fine-Tuning on instruction data. |
| **SGLang** | Fast inference engine with RadixAttention. |
| **Speculative decoding** | Small model drafts, big model verifies → lower latency. |
| **Structured output** | Forcing the model to emit JSON/schema-valid output. |
| **Test-time compute** | Inference-time compute scaling (reasoning models). |
| **TGI** | HuggingFace Text Generation Inference server. |
| **Token** | Sub-word unit; the currency of LLM cost. |
| **Tree of Thoughts (ToT)** | Exploring multiple reasoning branches. |
| **TruLens** | LLM app tracking + evaluation. |
| **TTFT** | Time To First Token; key latency metric. |
| **vLLM** | High-throughput inference engine with PagedAttention. |
| **Whisper** | Open ASR model (OpenAI). |
| **Zep** | Long-term memory service for agents. |

> Missing a term? Open a PR — see [Contributing](../CONTRIBUTING.md).
