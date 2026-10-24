"""
ClauseLens Studio — Deterministic & Hybrid Contract Trap X-Ray & Stance-Calibrated Redline Engine
Built for Build With AI: Basics ($2,500 Hackathon) following the official challengepost/learn-ai-basics workflow.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List


PRESET_CONTRACTS: List[Dict[str, Any]] = [
    {
        "id": "freelance-creator-msa",
        "title": "Creator & Freelance Master Services Agreement (MSA)",
        "counterparty": "Apex Brand Studio LLC",
        "contract_value_usd": 12000,
        "base_fairness_score": 34,
        "document_text": (
            "MASTER CREATOR & CONSULTING SERVICES AGREEMENT\n"
            "This Master Services Agreement (\"Agreement\") is entered into between Apex Brand Studio LLC (\"Client\") "
            "and Independent Creator (\"Contractor\") for brand design and full-stack interactive deliverables.\n\n"
            "1. COMPENSATION & PAYMENT TERMS.\n"
            "Client agrees to pay Contractor a project fee of $12,000 USD. All invoices submitted by Contractor shall be "
            "payable on Net-90 day terms from Client's final written acceptance, and Client may withhold up to 40% of fees "
            "indefinitely pending internal marketing performance review with zero late-payment interest.\n\n"
            "2. INTELLECTUAL PROPERTY & PRE-PAYMENT ASSIGNMENT.\n"
            "All preliminary sketches, unused concepts, raw project files, and pre-existing templates created or utilized "
            "by Contractor shall vest immediately and irrevocably in Client upon creation, regardless of whether Client "
            "completes final payment.\n\n"
            "3. TERM, SILENT AUTO-RENEWAL & EXCLUSIVITY.\n"
            "This Agreement shall automatically renew for successive twelve (12) month exclusivity periods at the same rate "
            "unless Contractor delivers certified physical mail notice of non-renewal at least ninety (90) days prior to the "
            "anniversary date.\n\n"
            "4. TERMINATION FOR CONVENIENCE & KILL FEE.\n"
            "Client may terminate this Agreement at any time for convenience upon 24 hours notice without owing any kill fee "
            "or reimbursement for work-in-progress hours already performed in the current milestone."
        ),
        "clauses": [
            {
                "id": "cl-payment-net90",
                "section": "Section 1 — Payment & Indefinite Holdback",
                "category": "Cashflow & Holdback Trap",
                "severity": "critical",
                "exposure_usd": 4800,
                "fairness_delta": 16,
                "quote": (
                    "All invoices submitted by Contractor shall be payable on Net-90 day terms from Client's final written "
                    "acceptance, and Client may withhold up to 40% of fees indefinitely pending internal marketing performance "
                    "review with zero late-payment interest."
                ),
                "plain_english": (
                    "You wait 3 full months after approval to get paid, and the client can hold back $4,800 (40%) forever "
                    "based on internal metrics you don't control."
                ),
                "redlines": {
                    "warm": (
                        "Invoices shall be payable on Net-15 terms (50% upfront deposit, 50% upon delivery), and acceptance "
                        "shall be deemed granted if no written revision request is received within 7 business days."
                    ),
                    "balanced": (
                        "Fees are payable 50% upon execution and 50% within Net-15 days of milestone delivery, with no "
                        "performance holdbacks. Overdue balances accrue 1.5% monthly late interest."
                    ),
                    "firm": (
                        "Strict Payment Schedule: 50% non-refundable commencement fee upon signing; 50% due Net-10 upon delivery. "
                        "All holdbacks are deleted in their entirety, and work pauses automatically on any invoice 5 days past due."
                    ),
                },
            },
            {
                "id": "cl-ip-grab",
                "section": "Section 2 — Pre-Payment & Background IP Grab",
                "category": "IP Ownership Trap",
                "severity": "critical",
                "exposure_usd": 6500,
                "fairness_delta": 18,
                "quote": (
                    "All preliminary sketches, unused concepts, raw project files, and pre-existing templates created or utilized "
                    "by Contractor shall vest immediately and irrevocably in Client upon creation, regardless of whether Client "
                    "completes final payment."
                ),
                "plain_english": (
                    "Client takes legal ownership of your reusable code/design libraries, rejected drafts, and raw source files "
                    "the second you sketch them—even if they never pay your invoice."
                ),
                "redlines": {
                    "warm": (
                        "Final approved deliverables transfer to Client upon full payment of the project fee, while Contractor "
                        "retains ownership of pre-existing templates, tools, and unused concepts."
                    ),
                    "balanced": (
                        "Client receives full right and title to final approved Deliverables solely upon Contractor's receipt of "
                        "payment in full. Contractor retains all Background IP, raw working files, and rejected concepts."
                    ),
                    "firm": (
                        "Condition Precedent: No assignment or license of any Deliverable takes effect unless and until all invoices "
                        "are paid in full. All Background IP, frameworks, and unused concepts remain the exclusive property of Contractor."
                    ),
                },
            },
            {
                "id": "cl-auto-renew",
                "section": "Section 3 — 90-Day Certified Mail Auto-Renewal",
                "category": "Silent Lock-In Trap",
                "severity": "high",
                "exposure_usd": 1500,
                "fairness_delta": 13,
                "quote": (
                    "This Agreement shall automatically renew for successive twelve (12) month exclusivity periods at the same rate "
                    "unless Contractor delivers certified physical mail notice of non-renewal at least ninety (90) days prior to the "
                    "anniversary date."
                ),
                "plain_english": (
                    "Locks you into another year of exclusivity at last year's rates unless you mail a physical certified letter "
                    "3 months before the contract ends."
                ),
                "redlines": {
                    "warm": (
                        "This Agreement may be renewed for additional terms by mutual written or email agreement of both parties "
                        "at least 30 days prior to expiration."
                    ),
                    "balanced": (
                        "Renewal requires mutual written consent via email. Either party may decline renewal or propose updated "
                        "rates with 30 days email notice."
                    ),
                    "firm": (
                        "Auto-renewal and exclusivity are deleted. This Agreement expires automatically at the conclusion of the "
                        "Initial Term unless extended by a signed written amendment."
                    ),
                },
            },
            {
                "id": "cl-no-kill-fee",
                "section": "Section 4 — Zero Kill-Fee Termination",
                "category": "Unilateral Cancellation Trap",
                "severity": "high",
                "exposure_usd": 2000,
                "fairness_delta": 13,
                "quote": (
                    "Client may terminate this Agreement at any time for convenience upon 24 hours notice without owing any kill fee "
                    "or reimbursement for work-in-progress hours already performed in the current milestone."
                ),
                "plain_english": (
                    "Client can cancel the project 95% of the way through a milestone with 24 hours notice and pay $0 for the "
                    "weeks of work you already completed."
                ),
                "redlines": {
                    "warm": (
                        "Either party may terminate for convenience upon 14 days email notice, and Client shall compensate "
                        "Contractor pro-rata for all work-in-progress completed plus a 20% scheduling kill fee."
                    ),
                    "balanced": (
                        "Upon termination for convenience, Client shall pay for all work performed through the termination date "
                        "plus a 25% kill fee on the remaining contract balance within 10 business days."
                    ),
                    "firm": (
                        "Termination for convenience requires 15 business days written notice, full payment for all current "
                        "milestone work-in-progress, and a non-refundable 35% kill fee on remaining contracted value."
                    ),
                },
            },
        ],
    },
    {
        "id": "residential-apartment-lease",
        "title": "Urban Residential Apartment Lease (12-Month Term)",
        "counterparty": "skyline Metro Properties LP",
        "contract_value_usd": 28800,
        "base_fairness_score": 38,
        "document_text": (
            "RESIDENTIAL APARTMENT LEASE AGREEMENT\n"
            "This Lease Agreement is made between Skyline Metro Properties LP (\"Landlord\") and Resident (\"Tenant\") "
            "for Unit 14B at $2,400/month.\n\n"
            "1. SECURITY DEPOSIT FORFEITURE & MANDATORY CARPET REPLACEMENT.\n"
            "Landlord may deduct a mandatory $850 professional restaining and carpet replacement fee from Tenant's Security "
            "Deposit upon move-out regardless of unit cleanliness or normal wear and tear.\n\n"
            "2. LANDLORD ENTRY WITHOUT NOTICE.\n"
            "Landlord and its prospective buyers, contractors, or agents may enter the Premises at any hour of any day "
            "without prior notice to Tenant for inspections, appraisals, or unscheduled showings.\n\n"
            "3. AUTOMATIC 60-DAY MONTH-TO-MONTH SURCHARGE.\n"
            "Unless Tenant provides written notice at least 75 days prior to Lease expiration, this Lease converts to "
            "a commitment at 145% of base rent ($3,480/month) with a two-month early termination penalty."
        ),
        "clauses": [
            {
                "id": "lease-deposit-trap",
                "section": "Section 1 — Automatic Deposit Deduction for Normal Wear",
                "category": "Deposit Forfeiture Trap",
                "severity": "critical",
                "exposure_usd": 850,
                "fairness_delta": 20,
                "quote": (
                    "Landlord may deduct a mandatory $850 professional restaining and carpet replacement fee from Tenant's Security "
                    "Deposit upon move-out regardless of unit cleanliness or normal wear and tear."
                ),
                "plain_english": (
                    "Automatically takes $850 out of your security deposit even if you leave the apartment spotless."
                ),
                "redlines": {
                    "warm": "Security deposit deductions shall apply only to documented damage beyond normal wear and tear.",
                    "balanced": "No mandatory move-out fees shall apply if Premises are returned broom-clean, ordinary wear and tear excepted.",
                    "firm": "Deleted mandatory $850 fee: Security Deposit deductions are strictly limited to itemized physical damages exceeding statutory normal wear and tear.",
                },
            },
            {
                "id": "lease-entry-notice",
                "section": "Section 2 — Zero-Notice 24/7 Landlord Entry",
                "category": "Privacy & Quiet Enjoyment Trap",
                "severity": "high",
                "exposure_usd": 1200,
                "fairness_delta": 18,
                "quote": (
                    "Landlord and its prospective buyers, contractors, or agents may enter the Premises at any hour of any day "
                    "without prior notice to Tenant for inspections, appraisals, or unscheduled showings."
                ),
                "plain_english": "Allows the landlord or real estate agents to walk into your apartment at any hour without warning.",
                "redlines": {
                    "warm": "Except in emergencies, Landlord shall provide at least 24 hours advance email/SMS notice before entry during normal daytime hours.",
                    "balanced": "Non-emergency entry requires 24 hours prior written notice and must occur between 9:00 AM and 6:00 PM.",
                    "firm": "Strict Quiet Enjoyment: Landlord entry requires 48 hours written notice (except active fire/flood emergencies) and Tenant's scheduled window.",
                },
            },
            {
                "id": "lease-renewal-surge",
                "section": "Section 3 — 75-Day Notice & 145% Rent Surge",
                "category": "Renewal Penalty Trap",
                "severity": "critical",
                "exposure_usd": 3240,
                "fairness_delta": 18,
                "quote": (
                    "Unless Tenant provides written notice at least 75 days prior to Lease expiration, this Lease converts to "
                    "a commitment at 145% of base rent ($3,480/month) with a two-month early termination penalty."
                ),
                "plain_english": "Hikes your rent by $1,080/month and charges a 2-month penalty if you don't give notice 75 days early.",
                "redlines": {
                    "warm": "Tenant shall provide 30 days notice prior to expiration; month-to-month continuation shall not exceed 105% of base rent.",
                    "balanced": "Notice period is 30 days prior to Lease end, and Landlord must provide any renewal rate proposal at least 45 days in advance.",
                    "firm": "Notice window reduced to 30 days; month-to-month holdover rate capped at 103% of base rent with zero early termination penalty.",
                },
            },
        ],
    },
    {
        "id": "enterprise-saas-renewal",
        "title": "B2B AI SaaS Annual Subscription Order Form",
        "counterparty": "CloudScale Telemetry Inc.",
        "contract_value_usd": 18000,
        "base_fairness_score": 41,
        "document_text": (
            "ENTERPRISE SAAS ORDER FORM & MASTER SUBSCRIPTION TERMS\n"
            "Customer subscribes to CloudScale Pro Tier ($18,000/year).\n\n"
            "1. AUTO-RENEWAL & 18% ANNUAL PRICE ESCALATOR.\n"
            "Each Order Form automatically renews for a 24-month term with an automatic 18% annual price uplift unless "
            "Customer cancels at least 60 days prior to the renewal date.\n\n"
            "2. UNILATERAL AI TRAINING ON CUSTOMER DATA.\n"
            "Vendor is granted a perpetual, worldwide, royalty-free license to use Customer's proprietary prompts, uploaded "
            "documents, and customer records to train and commercialize Vendor's foundation models."
        ),
        "clauses": [
            {
                "id": "saas-price-uplift",
                "section": "Section 1 — 24-Month Auto-Renewal + 18% Price Hike",
                "category": "SaaS Lock-In & Price Hike Trap",
                "severity": "high",
                "exposure_usd": 6480,
                "fairness_delta": 24,
                "quote": (
                    "Each Order Form automatically renews for a 24-month term with an automatic 18% annual price uplift unless "
                    "Customer cancels at least 60 days prior to the renewal date."
                ),
                "plain_english": "Locks you in for 2 more years at an 18% price increase unless you cancel 60 days ahead.",
                "redlines": {
                    "warm": "Renewals shall be for 12-month periods with 30 days notice, and any price adjustment is capped at 5%.",
                    "balanced": "Renewal terms are 12 months with 30 days cancellation notice and a maximum 3% CPI-linked price cap.",
                    "firm": "No auto-renewal without Customer's written PO; renewal pricing locked at 0% increase for the first renewal term.",
                },
            },
            {
                "id": "saas-ai-training",
                "section": "Section 2 — Perpetual AI Training on Proprietary Data",
                "category": "Data & Trade-Secret Trap",
                "severity": "critical",
                "exposure_usd": 9500,
                "fairness_delta": 29,
                "quote": (
                    "Vendor is granted a perpetual, worldwide, royalty-free license to use Customer's proprietary prompts, uploaded "
                    "documents, and customer records to train and commercialize Vendor's foundation models."
                ),
                "plain_english": "Gives the vendor permanent permission to train public AI models on your private company documents and customer data.",
                "redlines": {
                    "warm": "Customer Data shall be used solely to provide the subscribed services to Customer and shall not be used to train shared models.",
                    "balanced": "Vendor shall not use Customer Data, prompts, or outputs to train, fine-tune, or improve any foundation or third-party AI models.",
                    "firm": "Zero Data Retention & Zero Training Guarantee: Vendor is strictly prohibited from training on, retaining, or sub-licensing any Customer Data.",
                },
            },
        ],
    },
]


TRAP_PATTERNS = [
    {
        "id": "custom-auto-renew",
        "regex": r"([^.\n]*(?:automatically renew|auto-renew|successive\s+\w+\s+month|prior\s+to\s+renewal)[^.\n]*\.)",
        "section": "Detected Clause — Silent Auto-Renewal & Notice Window",
        "category": "Silent Lock-In Trap",
        "severity": "high",
        "exposure_usd": 2400,
        "fairness_delta": 18,
        "plain_english": "Silently locks you into a multi-month/annual renewal unless you hit an early cancellation window.",
        "redlines": {
            "warm": "This Agreement may be renewed for additional periods upon mutual email confirmation 30 days prior to expiration.",
            "balanced": "Auto-renewal is replaced with opt-in written renewal via email with 30 days notice and zero rate escalation.",
            "firm": "Auto-renewal is deleted in its entirety. Any extension requires a mutually executed written addendum.",
        },
    },
    {
        "id": "custom-ip-grab",
        "regex": r"([^.\n]*(?:intellectual property|vest immediately|pre-existing|preliminary sketches|all right, title|work made for hire|train.*models)[^.\n]*\.)",
        "section": "Detected Clause — Overbroad IP / Data Ownership Transfer",
        "category": "IP & Data Ownership Trap",
        "severity": "critical",
        "exposure_usd": 5500,
        "fairness_delta": 22,
        "plain_english": "Transfers ownership of your work, background tools, or proprietary data before full payment or beyond scope.",
        "redlines": {
            "warm": "Final deliverables transfer upon full payment; pre-existing tools, templates, and proprietary data remain with their original owner.",
            "balanced": "IP assignment applies strictly to final approved Deliverables upon receipt of full payment. Background IP is excluded.",
            "firm": "Condition Precedent: No IP or data rights transfer until 100% of invoiced fees are paid. Background IP and model training are prohibited.",
        },
    },
    {
        "id": "custom-payment-holdback",
        "regex": r"([^.\n]*(?:net-60|net-90|withhold|mandatory.*fee|non-refundable|without owing any kill fee|terminate.*at any time)[^.\n]*\.)",
        "section": "Detected Clause — Payment Holdback / Unilateral Termination Trap",
        "category": "Financial Exposure Trap",
        "severity": "critical",
        "exposure_usd": 3600,
        "fairness_delta": 20,
        "plain_english": "Creates severe cashflow delay, uncompensated cancellation risk, or automatic deposit/fee deductions.",
        "redlines": {
            "warm": "Invoices are payable Net-15 without arbitrary holdbacks, and early termination includes pro-rata payment for work completed.",
            "balanced": "Payment terms are Net-15 with 1.5% monthly late interest; convenience termination requires 14 days notice and a 25% kill fee.",
            "firm": "All unilateral holdbacks and mandatory deductions are deleted. Convenience termination requires full payment plus a 35% kill fee.",
        },
    },
]


def analyze_custom_contract(text: str, title: str = "Custom Pasted Agreement") -> Dict[str, Any]:
    cleaned = (text or "").strip()
    if not cleaned:
        return PRESET_CONTRACTS[0]

    detected_clauses: List[Dict[str, Any]] = []
    for idx, pat in enumerate(TRAP_PATTERNS, start=1):
        m = re.search(pat["regex"], cleaned, flags=re.IGNORECASE)
        if m:
            quote = m.group(1).strip()
            detected_clauses.append(
                {
                    "id": f"{pat['id']}-{idx}",
                    "section": pat["section"],
                    "category": pat["category"],
                    "severity": pat["severity"],
                    "exposure_usd": pat["exposure_usd"],
                    "fairness_delta": pat["fairness_delta"],
                    "quote": quote,
                    "plain_english": pat["plain_english"],
                    "redlines": pat["redlines"],
                }
            )

    if not detected_clauses:
        first_sentence = cleaned.split(".")[0].strip() + "."
        detected_clauses.append(
            {
                "id": "custom-general-review-1",
                "section": "Clause 1 — Mutual Liability & Notice Clarification",
                "category": "Standard Scope Safeguard",
                "severity": "high",
                "exposure_usd": 1500,
                "fairness_delta": 15,
                "quote": first_sentence[:260],
                "plain_english": "Clarifies mutual notice periods and caps total liability at fees actually paid.",
                "redlines": {
                    "warm": "Both parties agree to a 30-day cure period and a mutual liability cap equal to fees paid.",
                    "balanced": "Total aggregate liability of either party shall not exceed the fees paid under this Agreement in the preceding 6 months.",
                    "firm": "Mutual Cap & Cure: Liability is strictly capped at 1x fees paid, with a mandatory 15-day written cure window.",
                },
            }
        )

    base_score = max(25, 92 - sum(c["fairness_delta"] for c in detected_clauses))
    return {
        "id": "custom-contract",
        "title": title,
        "counterparty": "Custom Counterparty",
        "contract_value_usd": 15000,
        "base_fairness_score": base_score,
        "document_text": cleaned,
        "clauses": detected_clauses,
    }
