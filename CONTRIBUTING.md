# Contributing to LLM Engineering Roadmap

First off — **thank you** for taking the time to contribute! 🙏

This project is a community-driven roadmap. The more high-quality, well-curated
content we add, the more useful it becomes for everyone learning LLM engineering.

## 📋 Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Before You Start](#before-you-start)
- [How to Submit Changes](#how-to-submit-changes)
- [Content Guidelines](#content-guidelines)
- [Adding a Translation](#adding-a-translation)
- [Adding a Notebook or Project](#adding-a-notebook-or-project)
- [Style Guide](#style-guide)
- [Review Process](#review-process)

---

## Ways to Contribute

- 🐛 **Report issues** — broken links, outdated info, typos
- 📚 **Add resources** — papers, courses, tools, tutorials
- 🌍 **Translate** the roadmap into another language
- 📓 **Add notebooks / starter projects** for any phase
- 🎨 **Improve diagrams** (SVG roadmap, architecture schemas)
- 💡 **Suggest new sections** — open an issue with the `enhancement` label
- 🗣 **Share your story** — case studies, real-world architectures

## Before You Start

1. **Search existing issues & PRs** to avoid duplicates.
2. For large changes (new phase, new section, translation), **open an issue
   first** to discuss scope and avoid wasted work.
3. Keep the roadmap **opinionated but balanced** — present trade-offs, not
   dogma.

## How to Submit Changes

```bash
# 1. Fork & clone
git clone https://github.com/<your-username>/LLM-Engineering.git
cd LLM-Engineering

# 2. Create a branch
git checkout -b feat/add-mcp-section

# 3. Make your changes (keep commits focused)
git add -A
git commit -m "feat: add MCP server example and resources"

# 4. Push and open a PR against `main`
git push -u origin feat/add-mcp-section
```

Use [Conventional Commits](https://www.conventionalcommits.org) prefixes:

| Type     | Use for                                   |
| -------- | ----------------------------------------- |
| `feat`   | New content, sections, projects           |
| `fix`    | Broken links, typos, factual errors       |
| `docs`   | Documentation improvements                |
| `chore`  | Repo config, CI, templates                |
| `i18n`   | Translations                              |

## Content Guidelines

- **Curate, don't dump.** Every link should earn its place. Prefer official
  docs over blog spam.
- **Stay current.** If a tool is deprecated or acquired, update or remove it.
- **Show trade-offs.** Use comparison tables (cost, latency, complexity).
- **Cite sources.** For claims about performance or security, link the paper
  or official source.
- **No affiliate links.** This is an educational resource.
- **License-compatible.** Only link to content that can be freely referenced.
  Do not paste copyrighted material.

## Adding a Translation

1. Create `translations/<lang-code>/README.md` (e.g. `translations/es/README.md`).
2. Translate the full README — keep code blocks, URLs, and table structure intact.
3. Add a row to the **Translations** table in the main README.
4. Open a PR titled `i18n: add <language> translation`.

## Adding a Notebook or Project

```
notebooks/
  phase-1-foundations/
    01_token_counter.ipynb
    02_prompt_playground.ipynb
projects/
  rag-chatbot/
    README.md
    docker-compose.yml
    app/
mcp-servers/
  filesystem-server/
    server.py
    README.md
```

Each notebook/project must:
- Include a `README.md` explaining setup and learning outcomes
- Pin dependencies in `requirements.txt`
- Run with `python -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
- Not require paid API keys to run (use Ollama or a free tier where possible)

## Style Guide

- **Markdown:** GitHub-flavored, 80-char soft wrap where practical.
- **Tables:** Always include a header row. Keep columns short.
- **Code blocks:** Always specify the language (` ```python `, ` ```bash `).
- **Links:** Use reference-style for long URLs inside tables to keep them readable.
- **Emojis:** Used as section anchors only (🧠 ⚙️ 🔐 🚀). Don't sprinkle mid-sentence.
- **Tone:** Direct, technical, no hype. "GPT-4o is faster" → "GPT-4o has lower
  median latency than GPT-4-Turbo on the MMLU benchmark (cite)."

## Review Process

1. A maintainer will review within **7 days**.
2. CI checks (markdown lint, link check) must pass.
3. For content changes, at least one maintainer approval is required.
4. We may request edits for tone, accuracy, or formatting — this is normal.

## Recognition

Contributors are added to the **Contributors** section of the README after
their first merged PR. Significant contributors may be invited as
collaborators.

---

Questions? Open a [Discussion](https://github.com/tal7aouy/LLM-Engineering/discussions)
or join our Discord (link in README).

Happy contributing! 🚀
