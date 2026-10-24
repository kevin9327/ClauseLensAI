# ClauseLens Studio — Everyday Contract Trap X-Ray & Stance-Calibrated Counter-Offer Studio

[![Build With AI: Basics](https://img.shields.io/badge/Build_With_AI-Basics_2026-10b981?style=for-the-badge)](devpost/scope.md)
[![Official Skill-Pack](https://img.shields.io/badge/Skill_Pack-challengepost%2Flearn--ai--basics-06b6d4?style=for-the-badge)](devpost/checklist.md)
[![Interactive App Map](https://img.shields.io/badge/Architecture_Tour-devpost%2Fapp--map.html-f59e0b?style=for-the-badge)](devpost/app-map.html)

> **Official Submission for [Build With AI: Basics](https://learn-ai-basics.devpost.com/)**  
> Built end-to-end with the official [`challengepost/learn-ai-basics`](https://github.com/challengepost/learn-ai-basics) 6-stage skill workflow (`1-start` → `2-scope` → `3-prd` → `4-spec` → `5-build` → `6-ship`).

---

## Live Links

- **Live Interactive Web App**: [`https://kevin9327.github.io/ClauseLensAI/`](https://kevin9327.github.io/ClauseLensAI/)
- **Interactive Architecture & Code Tour (`devpost/app-map.html`)**: [`https://kevin9327.github.io/ClauseLensAI/app-map.html`](https://kevin9327.github.io/ClauseLensAI/app-map.html)
- **GitHub Repository**: [`https://github.com/kevin9327/ClauseLensAI`](https://github.com/kevin9327/ClauseLensAI)

---

## Official `devpost/` Skill-Pack Artifacts

- [`devpost/scope.md`](devpost/scope.md) — Approved Stage 2 Scope (`The Unique Kernel`, `Who It's For`, `The Core Loop`, `The POC Boundary`, `Explicitly Cut`)
- [`devpost/prd.md`](devpost/prd.md) — Approved Stage 3 Product Requirements with `Source: scope.md > ...` cross-references
- [`devpost/spec.md`](devpost/spec.md) — Approved Stage 4 Plain-Language Technical Spec with `PRD ref: prd.md > ...` cross-references
- [`devpost/checklist.md`](devpost/checklist.md) — Approved Stage 5 Slice-by-Slice Build Checklist (`Build mode: learn`, 5 vertical slices, `Hands-on Checkpoints`, `Code Tour and App Map`)
- [`devpost/app-map.html`](devpost/app-map.html) — Stage 6 Interactive SVG System Diagram & Guided Code Tour (`devpost/learner-profile.md` excluded via [`.gitignore`](.gitignore) per official skill rules)

---

## Quick Start

```bash
pip install -r requirements.txt
python -m pytest tests/test_clauselens.py -v
python -m uvicorn backend.server:app --host 127.0.0.1 --port 8096
```
