# LLM Security Checklist

Use before launching any LLM application.

## OWASP LLM Top 10

- [ ] **LLM01 Prompt Injection** — untrusted text isolated from system instructions; spotlighting + sandwich defense
- [ ] **LLM02 Insecure Output Handling** — LLM output treated as untrusted before render/execute
- [ ] **LLM03 Training Data Poisoning** — fine-tuning data vetted, deduped, provenanced
- [ ] **LLM04 Supply Chain** — deps pinned, models are safetensors + hash-verified
- [ ] **LLM05 Sensitive Info Disclosure** — output scanned for PII/secrets before return
- [ ] **LLM06 Excessive Agency** — tools least-privilege; HITL for irreversible actions
- [ ] **LLM07 System Prompt Leakage** — tested extraction; no secrets in system prompt
- [ ] **LLM08 Vector/Embedding Weaknesses** — vector DB access-controlled; embeddings not poisoned
- [ ] **LLM09 Hallucination** — RAG grounding + citations + self-check
- [ ] **LLM10 Unbounded Consumption** — rate limit + token cap + cache

## Defense in Depth

- [ ] Instruction hierarchy enforced (system > user > tool > retrieval)
- [ ] Input filter (Rebuff / LLM-judge) for injection
- [ ] Output filter (guard model) for safety
- [ ] Tool execution sandboxed (container / microVM), never host OS
- [ ] PII scrubbing (Presidio) on inputs and outputs
- [ ] Audit log of all prompts + tool calls

## Supply Chain

- [ ] `pip-audit` / `safety` clean
- [ ] Models loaded from safetensors, hash verified
- [ ] No floating `latest`/`*` dependency ranges
- [ ] Model + dataset cards reviewed (license, training data, biases)

## Red Team

- [ ] Run `garak` against the deployed model
- [ ] Manual injection test suite (10+ prompts)
- [ ] Try to extract system prompt → confirm it's safe or contains no secrets
- [ ] Test tool actions for privilege escalation

## Compliance

- [ ] EU AI Act risk tier determined
- [ ] NIST AI RMF aligned (if US)
- [ ] GDPR: data retention + deletion + DPA with providers
- [ ] HIPAA: PHI handling if healthcare (BAA with provider)
