---
doc: prd
status: approved
project: "ClauseLens Studio"
created: "2026-10-24"
updated: "2026-10-25"
---

# ClauseLens Studio — Product Requirements

One line: An interactive contract x-ray and stance-calibrated counter-offer studio for renters, freelancers, and solo founders.
Source: `scope.md > The Unique Kernel`, `scope.md > Who It's For`.

## The Core Journey
Source: `scope.md > What "Working" Looks Like`, `scope.md > The Core Loop`.

1. **Instant Landing & Preset Triage**: The user lands directly inside the ClauseLens Studio workspace with the **Freelance Creator Master Agreement** loaded by default, immediately displaying the baseline **Contract Fairness Score (`34 / 100`)** and **Total Financial Exposure (`$14,800`)**.
2. **Clause Trap Inspection**: The user clicks any highlighted trap span in the left document viewer or its corresponding card in the right-hand **Red-Flag X-Ray Deck** (`IP Assignment Upon Draft`, `90-Day Silent Auto-Renewal`, `Net-90 Payment + 0% Late Interest`, `Unilateral Termination Without Kill Fee`).
3. **Stance Calibration**: The user switches the **Negotiation Stance Slider** across `Warm & Collaborative`, `Balanced Market Standard`, and `Firm Legal Boundary`, observing immediate updates to the redline diff (`- original` / `+ replacement`) and negotiation talking points.
4. **Redline Acceptance & Counter-Offer Export**: The user toggles `Include in Counter-Offer` on flagged clauses, watching the **Contract Fairness Score** climb from `34` to `94 / 100` and **Protected Exposure** reach `$14,800`, then clicks **Copy Counter-Proposal Email & Redline Rider**.

## Screens and Layout
Source: `scope.md > The Core Loop`, `scope.md > The POC Boundary`.

- **Top Command Header**: Brand badge, Contract Preset Selector (`Freelance Creator MSA`, `Residential Apartment Lease`, `Enterprise SaaS Renewal`, `Custom Paste`), Custom Contract Modal trigger, Light/Dark Theme toggle, and live KPI pills (`Fairness Score`, `Traps Detected`, `Exposure Protected`).
- **Left Pane — Verbatim Contract X-Ray Viewer**: Displays the full contract text with color-coded interactive mark spans (`critical` in rose, `high` in amber, `accepted-redline` in emerald). Clicking any span scrolls and focuses the corresponding redline card.
- **Right Pane — 3-Tab Negotiation Studio**:
  - **Tab 1: Red-Flag Clauses & Diffs**: Stance Selector (`Warm` / `Balanced` / `Firm`) + interactive cards showing Plain-English Risk, Dollar Exposure, Verbatim Quote, Redline Replacement Diff, and `Include in Counter-Offer` toggle.
  - **Tab 2: Ready-to-Send Counter-Offer Email**: Live generated email + formatted Redline Addendum that updates dynamically as clauses are toggled or stance changes, with a 1-click Copy button.
  - **Tab 3: Custom Contract Scanner & Architecture**: Paste any custom contract clause to run the deterministic + AI hybrid red-flag detector in real time.

## Look and Feel
Source: `scope.md > Inspiration & Identity`.

- **Typography**: `Space Grotesk` for crisp headings, `Inter` for high-legibility contract prose, and `JetBrains Mono` for clause citations, dollar exposure metrics, and redline diffs.
- **Palette**: Dark-first obsidian surface (`#090b10` / `#121621`) with high-contrast WCAG AA badges (`#10b981` emerald for protected clauses, `#f59e0b` amber for moderate risk, `#f43f5e` rose for critical traps), plus a full Light Mode (`#f8fafc` paper view) persisted in `localStorage`.

## Features and Behavior

### 1. Multi-Preset & Custom Contract X-Ray Scanner
Source: `scope.md > The Core Loop`, `scope.md > The POC Boundary`.
- As a freelancer or renter, I want to load realistic agreements or paste my own contract text so that I can immediately spot hidden financial and legal traps.
  - [x] Includes 3 curated real-world contracts (`Freelance Creator MSA`, `Residential Apartment Lease`, `SaaS Order Form`) with exact character offsets.
  - [x] Includes a custom contract analyzer endpoint (`POST /api/analyze`) and client-side fallback scanner that detects auto-renewal, IP assignment, indemnity, non-compete, and deposit traps.

### 2. Stance-Calibrated Redline Diff Engine
Source: `scope.md > The Unique Kernel`.
- As a negotiator who wants to preserve client or landlord goodwill, I want to adjust my negotiation stance between `Warm`, `Balanced`, and `Firm` so that the proposed clause wording and email tone match my leverage.
  - [x] Switching stances immediately updates both the replacement clause wording and the email opening/closing framing.
  - [x] Toggling a clause's `Include in Counter-Offer` switch updates the live Fairness Score (`0–100`) and Protected Exposure (`$`) in under 16ms.

### 3. One-Click Counter-Offer Email & Redline Rider Generator
Source: `scope.md > What "Working" Looks Like`.
- As a busy user, I want a complete, polite, copy-pasteable counter-offer email containing only the clauses I selected so that I can reply to the sender in under 60 seconds.
  - [x] Formats each accepted clause with section header, current wording, proposed redline, and concise business rationale.
  - [x] Provides visual confirmation (`Copied to Clipboard!`) and downloadable `.txt` / `.md` rider export.

## States and Boundaries
Source: `scope.md > The POC Boundary`, `scope.md > Explicitly Cut`.

- **First Use State**: Automatically loads the `Freelance Creator MSA` preset with Clause #1 focused and all telemetry active so judges never face a blank screen.
- **Empty / Clean Contract State**: If custom pasted text contains zero risky patterns, displays a green `Clean Clause Verification (Fairness Score 96/100)` banner.
- **Error / Offline Boundary**: If the Python FastAPI backend is unreachable (e.g., on static GitHub Pages), the frontend seamlessly executes its embedded deterministic clause analyzer with zero console errors.
- **Persistence**: Selected theme (`dark` / `light`), active contract preset, negotiation stance, and accepted redline toggles persist in `localStorage`.
