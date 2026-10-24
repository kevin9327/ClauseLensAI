---
doc: checklist
status: approved
project: "ClauseLens Studio"
created: "2026-10-24"
updated: "2026-10-25"
---

# Build Checklist

Build mode: learn

## Slices

- [x] **1. Split-Pane Contract X-Ray Shell & Preset Loader**
  Becomes usable: The user can open ClauseLens Studio, switch between the 3 real-world contract presets (`Freelance Creator MSA`, `Residential Apartment Lease`, `Enterprise SaaS Renewal`), and read the full contract with highlighted trap spans.
  Why now: Establishes the core visual surface and data model before wiring interactive stance diffing.
  PRD ref: `prd.md > The Core Journey` (steps 1-2), `prd.md > Screens and Layout`
  Spec ref: `spec.md > Verbatim Contract X-Ray Renderer`, `spec.md > Data Model`
  Build: Create `backend/clause_engine.py`, `backend/server.py`, `public/index.html`, `public/styles.css`, and initial preset rendering in `public/app.js`.
  Verify (mechanical): Start server and verify `GET /api/presets` returns 3 presets and `#contract-viewer` renders `<mark class="trap-span">` highlights with 0 console errors.
  Learner check: Open the app, switch across all 3 contract presets, and click highlighted spans in the contract pane.
  Commit: `feat(slice-1): build split-pane contract x-ray viewer and 3 real-world presets`

- [x] **2. 3-Tier Negotiation Stance Slider & Redline Diff Cards**
  Becomes usable: The user can click any flagged clause card and switch the Negotiation Stance between `Warm & Collaborative`, `Balanced Market Standard`, and `Firm Legal Boundary` to see real-time before/after clause redline diffs.
  Why now: Delivers the Unique Kernel (`scope.md > The Unique Kernel`) connecting risk detection to actionable negotiation wording.
  PRD ref: `prd.md > Stance-Calibrated Redline Diff Engine`
  Spec ref: `spec.md > Stance-Calibrated Redline & Fairness Engine`
  Build: Wire stance selector buttons, redline diff cards (`- original trap` / `+ protective replacement`), and live Fairness Score (`0–100`) & Dollar Exposure Protected (`$`) calculators in `public/app.js`.
  Verify (mechanical): Toggle stance pills and verify redline text, fairness score, and protected dollar totals update deterministically.
  Learner check: Slide between `Warm`, `Balanced`, and `Firm` on the IP Grab clause and inspect how the protective replacement clause adapts.
  Commit: `feat(slice-2): add 3-tier negotiation stance slider and live redline diff calculator`

- [x] **3. Ready-to-Send Counter-Offer Email & Redline Rider Exporter**
  Becomes usable: The user can toggle which redlines to include and copy or download a complete, polite counter-offer email with a formatted Redline Addendum in one click.
  Why now: Completes the end-to-end Core Loop (`scope.md > The Core Loop`) so the user walks away with a finished deliverable.
  PRD ref: `prd.md > One-Click Counter-Offer Email & Redline Rider Generator`
  Spec ref: `spec.md > Counter-Proposal Email Synthesizer`
  Build: Implement `renderCounterOfferEmail()`, clipboard copy toast confirmation, and `.md` rider download in `public/app.js`.
  Verify (mechanical): Toggle clause acceptance switches and verify `#counter-email-preview` updates immediately with accurate section headers and dollar exposure summary.
  Learner check: Copy the generated counter-offer email and verify it reads naturally for a real client or landlord.
  Commit: `feat(slice-3): implement live counter-offer email synthesizer and rider export`

- [x] **4. Custom Contract Trap Scanner & Theme Persistence**
  Becomes usable: The user can paste any custom contract text to scan for hidden auto-renewal, IP-grab, late-fee, liability, and termination traps, and toggle Dark/Light mode with `localStorage` persistence.
  Why now: Extends the PoC beyond static presets so anyone can test their own agreements (`prd.md > Multi-Preset & Custom Contract X-Ray Scanner`).
  PRD ref: `prd.md > Multi-Preset & Custom Contract X-Ray Scanner`, `prd.md > States and Boundaries`
  Spec ref: `spec.md > Stance-Calibrated Redline & Fairness Engine`, `spec.md > Important Failure Modes`
  Build: Add `POST /api/analyze` in `backend/server.py` + `analyze_custom_text()` in `backend/clause_engine.py`, custom scanner tab in `public/index.html`, Light/Dark theme persistence, and `tests/test_clauselens.py`.
  Verify (mechanical): Run `pytest tests/test_clauselens.py -v` (all tests passing) and test custom clause scanning in Playwright.
  Learner check: Paste a custom paragraph containing an auto-renewal and IP assignment trap and verify both traps highlight with generated redlines.
  Commit: `feat(slice-4): add custom contract trap analyzer, pytest suite, and theme persistence`

- [x] **5. Interactive Architecture Tour (`devpost/app-map.html`) & Ship Verification**
  Becomes usable: Learners and judges can open `devpost/app-map.html` (or click the Architecture Tour link in the header) to explore the inline SVG data-flow diagram, clickable Code Tour Route Stops, and modification guide.
  Why now: Finalizes Stage 6 (`6-ship`) of the `learn-ai-basics` workflow and ensures `.gitignore` excludes `devpost/learner-profile.md`.
  PRD ref: `prd.md > Screens and Layout`
  Spec ref: `spec.md > File Structure`
  Build: Generate `devpost/app-map.html` from the finished codebase and verify all 5 public `devpost/` artifacts and `.gitignore` rules.
  Verify (mechanical): Verify `devpost/learner-profile.md` is ignored by `git status` and all 5 public `devpost/` files pass schema checks.
  Learner check: Walk through the 4 Code Tour stops in `devpost/app-map.html`.
  Commit: `docs(slice-5): generate interactive devpost/app-map.html and finalize learn-ai-basics artifacts`

## Hands-on Checkpoints

- [x] Early usable behavior explored — verified after Slice 1-2
- [x] Final kick-the-tires exploration and feedback completed

## Final Review

- [x] Final review complete — feedback resolved and learner confirms ready to ship

## Code Tour and App Map

- [x] Learning activity complete — guided route, focused alternative, prior practice connected, or brief recap
- [x] Optional edit and transfer reflection addressed — covered during final review
- [x] `devpost/app-map.html` generated from finished code, checked, and shown, including a project-grounded practice to reuse

Activity and evidence: Guided code tour tracing how a single Stance Slider click updates the redline diff card, recalculates the Contract Fairness Score, and rewrites the counter-offer email.
Route and stops: `public/index.html` -> `public/app.js` -> `backend/clause_engine.py` -> `backend/server.py`
Edit outcome: Added live Protected Exposure ($) badge and one-click sample clause loader in Custom Scanner tab; verified in headless Chromium (`console_errors=0`).
Reflection: Offered and recorded in local profile.
Activity mode: live app and editor

## Revisions

- Added a 1-click "Load Sample Custom Clause" button inside Tab 3 (`Custom Contract Scanner`) so judges can test live custom trap extraction immediately without needing an external contract file on hand.
