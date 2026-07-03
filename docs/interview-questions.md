# LLM Engineering Interview Question Bank

> 200+ questions with answers. Community-maintained. Add questions you've been
> asked (see [Contributing](../CONTRIBUTING.md)).

## How to use

- **Self-study:** cover the answer, attempt aloud, then reveal.
- **Interviewing candidates:** pick 1–2 per category; ask follow-ups.
- **Hiring managers:** use as a rubric for LLM Engineer roles.

## Categories

1. [Fundamentals](#1-fundamentals)
2. [Prompting & Context Engineering](#2-prompting--context-engineering)
3. [RAG](#3-rag)
4. [Agents & MCP](#4-agents--mcp)
5. [Fine-Tuning & Post-Training](#5-fine-tuning--post-training)
6. [Inference & Serving](#6-inference--serving)
7. [Production & MLOps](#7-production--mlops)
8. [Evaluation](#8-evaluation)
9. [Security](#9-security)
10. [System Design](#10-system-design)

---

## 1. Fundamentals

**Q: What is the difference between greedy decoding and nucleus sampling?**
A: Greedy decoding picks the highest-probability token at each step
(deterministic, prone to repetition). Nucleus (top-p) sampling picks from the
smallest set of tokens whose cumulative probability ≥ p, giving diverse but
plausible outputs.

**Q: Why is attention O(n²) and how is it reduced?**
A: Standard self-attention computes a similarity score between every pair of
tokens → O(n²) in sequence length. FlashAttention fuses the attention
computation to reduce memory I/O; sparse/linear attention approximations
(Longformer, BigBird) reduce the asymptotic cost.

**Q: What is the KV cache and why does it matter?**
A: During autoregressive generation, each new token attends to all previous
tokens. The key/value projections of past tokens don't change, so they're
cached → avoids recomputing them each step. PagedAttention (vLLM) manages this
cache efficiently across many concurrent requests.

> _More questions added by contributors. PRs welcome._

---

## 2. Prompting & Context Engineering

**Q: What is the "lost in the middle" problem?**
A: Models recall information at the start and end of long contexts better than
the middle. Mitigations: reorder important info to the edges, use retrieval
instead of stuffing, or split into multiple calls.

**Q: When is few-shot better than zero-shot?**
A: When the task needs a specific output format, style, or edge-case behavior
that the model won't reliably produce from instructions alone. Costs more
tokens; prefer zero-shot + clear instructions when possible.

> _More added by contributors._

---

## 3. RAG

**Q: When would you choose GraphRAG over naive RAG?**
A: When queries need multi-hop reasoning across entity relationships (e.g.,
"which companies founded by ex-Googlers raised Series B in 2024?"). GraphRAG
builds a knowledge graph + community summaries; naive vector RAG struggles with
relational queries.

**Q: How do you evaluate a RAG pipeline?**
A: Use RAGAS-style metrics: faithfulness (answer grounded in context?),
answer relevance (addresses the question?), context precision/recall (right
chunks retrieved?). Also measure latency and cost per query.

> _More added by contributors._

---

## 4. Agents & MCP

**Q: What is MCP and how does it differ from function calling?**
A: MCP is a standard client–server protocol for connecting LLM apps to
external tools/data, with built-in discovery and OAuth. Function calling is a
per-vendor capability for a model to emit structured calls. MCP uses function
calling under the hood but standardizes the surrounding plumbing so tools are
reusable across hosts (Claude Desktop, Cursor, your agent).

**Q: How do you prevent an agent loop from running forever?**
A: Max iterations, max tokens, max cost, timeout, and a "stop" tool the model
can call. Also detect repeated tool calls (same args) and break.

> _More added by contributors._

---

## 5. Fine-Tuning & Post-Training

**Q: When is fine-tuning better than RAG?**
A: When you need to change *behavior* (style, tone, format, domain jargon)
rather than *knowledge*. RAG is better for factual, up-to-date knowledge.
Often combine: fine-tune for style + RAG for facts.

**Q: Explain LoRA. What are rank `r` and alpha trade-offs?**
A: LoRA freezes the base model and trains low-rank update matrices (A·B where
A is r×d, B is d×r). Higher `r` = more capacity + more params + more overfit
risk. Alpha scales the updates; common heuristic alpha = 2×r.

> _More added by contributors._

---

## 6. Inference & Serving

**Q: Compare vLLM, SGLang, TGI.**
A: vLLM — industry default, PagedAttention, broad model support. SGLang —
fastest for structured/agent workloads via RadixAttention (prefix caching).
TGI — HuggingFace's server, good integration with HF ecosystem. Pick vLLM by
default; SGLang for heavy agent/structured workloads.

**Q: How does prefix caching work and when does it not help?**
A: Cache the KV of a shared prompt prefix; reuse for requests sharing that
prefix. Doesn't help when prompts have no shared prefix, or when the cache is
evicted before reuse.

> _More added by contributors._

---

## 7. Production & MLOps

**Q: How would you reduce LLM API costs by 50% without hurting quality?**
A: (1) Route easy queries to a cheaper model (model routing). (2) Semantic
cache repeated queries. (3) Compress prompts (LLMLingua). (4) Prompt caching
for static prefixes. (5) Reduce output max_tokens. (6) Batch requests.

**Q: Design a multi-tenant RAG SaaS. How do you isolate tenant data?**
A: Per-tenant vector collections (or tenant-id metadata filter enforced at
query time), per-tenant Postgres schemas (RLS), encryption keys per tenant,
rate limits per tenant, audit logs. Never let one tenant's query retrieve
another's chunks.

> _More added by contributors._

---

## 8. Evaluation

**Q: What metrics would you track for an LLM chatbot in production?**
A: Quality (faithfulness, relevance via RAGAS/LLM-judge), latency (TTFT,
tokens/sec, p99), cost ($/query), error rate, safety (toxicity, PII leaks),
user feedback (thumbs up/down), tool-call success rate (for agents).

> _More added by contributors._

---

## 9. Security

**Q: Walk me through LLM01 (Prompt Injection). How do you defend?**
A: Untrusted text contains instructions that override the system prompt.
Defenses (layered): instruction hierarchy, spotlighting/data-marking,
sandwich defense, input + output filtering, capability scoping (no irreversible
tool actions without HITL), sandbox tool execution.

**Q: What's the risk of loading a `pickle` model from HuggingFace?**
A: `pickle` deserializes arbitrary Python code → malicious models can execute
code on load. Use `safetensors` instead; verify model hashes; pin by commit
SHA.

> _More added by contributors._

---

## 10. System Design

**Q: Design a coding agent like Cursor.**
A: Codebase indexing (embeddings over chunks/files), retrieval at query time,
fill-in-the-middle for completions, agent mode with tool use (run tests, edit
files), context budget management, diff review, cost controls. Discuss
latency targets (<200ms for completions), model routing, and how to handle
large repos (hierarchical retrieval).

> _More added by contributors._

---

## Contributing

Add a question + answer under the right category. Keep answers concise
(2–4 sentences) and technically accurate. Cite sources where useful.
