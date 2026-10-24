---
doc: spec
status: approved
project: "ClauseLens Studio"
created: "2026-10-24"
updated: "2026-10-25"
---

# ClauseLens Studio — Technical Spec

## How This Works, In Plain Language
When you open ClauseLens Studio and pick a contract (or paste your own), the app scans the text for risky legal patterns—like automatic 12-month renewals, clauses that take ownership of your rough drafts before you get paid, or uncapped late fees. It wraps each risky sentence in a clickable highlight inside the contract viewer and builds a matching stack of Red-Flag Cards on the right. When you move the **Negotiation Stance Slider** (`Warm`, `Balanced`, or `Firm`) or flip a clause's **Include in Counter-Offer** switch, the app recalculates your **Contract Fairness Score (0–100)** and **Dollar Exposure Protected ($)** and instantly assembles a polite, ready-to-send counter-offer email with exact before/after clause redlines.

## The Core Journey Through the System
PRD ref: `prd.md > The Core Journey`.

1. **Preset Initialization (`app.js -> loadPreset()`)**: On page load, `app.js` fetches `/api/presets` from `backend/server.py` (or uses the deterministic client-side preset store if running on static GitHub Pages) and renders `Freelance Creator MSA` into `#contract-viewer`.
2. **Span Highlighting (`app.js -> renderContractDocument()`)**: The renderer slices the contract string by each trap's `start_char` and `end_char` coordinates, wrapping each trap in a `<mark class="trap-span">` element bound to `selectClause(clauseId)`.
3. **Stance & Redline Recomputation (`app.js -> setStance() / toggleClauseAcceptance()`)**: Changing the Stance pill (`warm`, `balanced`, `firm`) or toggling a clause updates the active state, recomputes `fairnessScore` and `protectedDollars`, updates the `<mark>` color from rose (`trap`) to emerald (`protected`), and regenerates the counter-offer email in `#counter-email-preview`.
4. **Custom Contract Analysis (`app.js -> analyzeCustomContract() -> POST /api/analyze`)**: When the user pastes custom contract text in Tab 3, the app sends it to `backend/clause_engine.py` (with a built-in browser fallback) which runs regex + heuristic risk pattern matchers across 6 trap categories and returns structured clause objects with exact character offsets and 3-tier stance redlines.

## Stack
- **Frontend**: Vanilla HTML5 (`public/index.html`), CSS3 Custom Properties with Dark/Light theme support (`public/styles.css`), and zero-dependency ES2022 JavaScript (`public/app.js`).
- **Backend**: Python 3.11 + FastAPI (`backend/server.py`, `backend/clause_engine.py`) with Pydantic validation and deterministic unit tests (`tests/test_clauselens.py`).
- **Architecture & Code Tour**: Standalone interactive `devpost/app-map.html` with inline SVG data-flow diagram and clickable route stops.

## Where It Runs and How Someone Tries It
- **Instant Live Web App (Zero Setup)**: `https://kevin9327.github.io/ClauseLensAI/`
- **Local Full-Stack Server**:
  ```bash
  pip install -r requirements.txt
  python -m uvicorn backend.server:app --host 127.0.0.1 --port 8096
  ```

## Look and Feel
PRD ref: `prd.md > Look and Feel`.
- Uses `Space Grotesk`, `Inter`, and `JetBrains Mono` with a dark obsidian default (`#090b10`) and a crisp paper light mode (`#f8fafc`) toggled via `#btn-theme-toggle` and persisted in `localStorage`.

## Components

### 1. Verbatim Contract X-Ray Renderer (`public/app.js`)
PRD ref: `prd.md > Screens and Layout`, `prd.md > Multi-Preset & Custom Contract X-Ray Scanner`.
- Renders the full agreement with non-overlapping `<mark>` highlights and synchronizes selection between the document pane and the Red-Flag Card deck.

### 2. Stance-Calibrated Redline & Fairness Engine (`backend/clause_engine.py` & `public/app.js`)
PRD ref: `prd.md > Stance-Calibrated Redline Diff Engine`.
- Stores and generates 3 distinct redline variants (`warm`, `balanced`, `firm`) per trap, computes the weighted `fairness_score` (`0–100`), and sums `exposure_usd` across accepted redlines.

### 3. Counter-Proposal Email Synthesizer (`public/app.js`)
PRD ref: `prd.md > One-Click Counter-Offer Email & Redline Rider Generator`.
- Combines stance-appropriate salutation/framing with a numbered markdown redline schedule (`Current Clause` vs. `Proposed Revision` + `Rationale`) and copies to clipboard.

## Data Model
```json
{
  "id": "freelance-creator-msa",
  "title": "Creator & Freelance Master Services Agreement (MSA)",
  "counterparty": "Apex Brand Studio LLC",
  "base_fairness_score": 34,
  "clauses": [
    {
      "id": "cl-ip-grab",
      "section": "Section 4.2 — Intellectual Property & Pre-Payment Assignment",
      "category": "IP Ownership Trap",
      "severity": "critical",
      "exposure_usd": 6500,
      "fairness_delta": 18,
      "quote": "All preliminary sketches, unused concepts, raw project files, and pre-existing templates created or utilized by Contractor shall vest immediately and irrevocably in Client upon creation, regardless of whether Client completes final payment.",
      "plain_english": "Client takes ownership of your raw files, unused concepts, and reusable templates immediately—even if they never pay your final invoice.",
      "redlines": {
        "warm": "Final deliverables shall assign to Client upon full payment of the applicable invoice. Contractor retains ownership of pre-existing tools, templates, and unused concepts.",
        "balanced": "Client shall receive full right, title, and interest in final approved Deliverables solely upon Contractor's receipt of payment in full. All preliminary drafts and pre-existing IP remain Contractor's property.",
        "firm": "Condition Precedent: No assignment or license of any Deliverable or Intellectual Property shall take effect unless and until all invoices under this Agreement are paid in full. Background IP and raw working files are strictly excluded."
      }
    }
  ]
}
```

## File Structure
```text
ClauseLensAI/
├── .gitignore                   # Ignores devpost/learner-profile.md per official skill-pack rules
├── README.md                    # Quickstart, live links, and architecture overview
├── requirements.txt             # FastAPI, Uvicorn, Pytest
├── backend/
│   ├── __init__.py
│   ├── clause_engine.py         # Preset store + Custom Contract Trap & Stance Redline Analyzer
│   └── server.py                # FastAPI REST endpoints (/api/health, /api/presets, /api/analyze)
├── public/
│   ├── index.html               # Split-pane Contract X-Ray & 3-Tab Negotiation Studio
│   ├── styles.css               # Dark/Light theme tokens & responsive split-pane layout
│   └── app.js                   # Interactive span highlighter, stance slider & email generator
├── devpost/
│   ├── scope.md                 # Official Stage 2 Scope artifact (status: approved)
│   ├── prd.md                   # Official Stage 3 PRD artifact (status: approved)
│   ├── spec.md                  # Official Stage 4 Technical Spec artifact (status: approved)
│   ├── checklist.md             # Official Stage 5 Slice Build Checklist (status: approved)
│   └── app-map.html             # Official Stage 6 Interactive Code Tour & SVG Architecture Map
└── tests/
    └── test_clauselens.py       # Automated pytest verification suite
```

## External Services and Dependencies
- Runs 100% self-contained with FastAPI + Pydantic on the backend and zero external runtime API keys required, ensuring judges can test every feature immediately without rate limits or paywalls.

## Important Failure Modes
- **Unmatched Custom Text**: When a user pastes a short or clean paragraph with no standard trap phrases, the analyzer returns a `Clean Agreement` assessment (`Fairness Score 96/100`) instead of crashing or returning an empty state.
- **Static Hosting Fallback**: When hosted on GitHub Pages where `/api/*` is static, `public/app.js` catches the `fetch` error and runs its embedded deterministic analyzer identically.

## What Was Simplified and Why
- Instead of requiring binary `.docx` or OCR PDF uploads (which fail on scanned mobile photos), we focused on instant text/clause pasting and 3 rich real-world presets so the core loop (`Inspect Trap -> Calibrate Stance -> Export Counter-Offer`) is frictionless.

## Decisions and Open Issues
- **Decision**: Keep all contract text processing in-memory and local (`localStorage`) rather than persisting to an external database to protect user privacy.
- **Open Issue**: Future iterations can add state-by-state statutory citations for residential leases.
