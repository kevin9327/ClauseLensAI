const FALLBACK_PRESETS = [
  {
    id: "freelance-creator-msa",
    title: "Creator & Freelance Master Services Agreement (MSA)",
    counterparty: "Apex Brand Studio LLC",
    contract_value_usd: 12000,
    base_fairness_score: 34,
    document_text:
      'MASTER CREATOR & CONSULTING SERVICES AGREEMENT\n' +
      'This Master Services Agreement ("Agreement") is entered into between Apex Brand Studio LLC ("Client") and Independent Creator ("Contractor") for brand design and full-stack interactive deliverables.\n\n' +
      '1. COMPENSATION & PAYMENT TERMS.\n' +
      'Client agrees to pay Contractor a project fee of $12,000 USD. All invoices submitted by Contractor shall be payable on Net-90 day terms from Client\'s final written acceptance, and Client may withhold up to 40% of fees indefinitely pending internal marketing performance review with zero late-payment interest.\n\n' +
      '2. INTELLECTUAL PROPERTY & PRE-PAYMENT ASSIGNMENT.\n' +
      'All preliminary sketches, unused concepts, raw project files, and pre-existing templates created or utilized by Contractor shall vest immediately and irrevocably in Client upon creation, regardless of whether Client completes final payment.\n\n' +
      '3. TERM, SILENT AUTO-RENEWAL & EXCLUSIVITY.\n' +
      'This Agreement shall automatically renew for successive twelve (12) month exclusivity periods at the same rate unless Contractor delivers certified physical mail notice of non-renewal at least ninety (90) days prior to the anniversary date.\n\n' +
      '4. TERMINATION FOR CONVENIENCE & KILL FEE.\n' +
      'Client may terminate this Agreement at any time for convenience upon 24 hours notice without owing any kill fee or reimbursement for work-in-progress hours already performed in the current milestone.',
    clauses: [
      {
        id: "cl-payment-net90",
        section: "Section 1 — Payment & Indefinite Holdback",
        category: "Cashflow & Holdback Trap",
        severity: "critical",
        exposure_usd: 4800,
        fairness_delta: 16,
        quote: "All invoices submitted by Contractor shall be payable on Net-90 day terms from Client's final written acceptance, and Client may withhold up to 40% of fees indefinitely pending internal marketing performance review with zero late-payment interest.",
        plain_english: "You wait 3 full months after approval to get paid, and the client can hold back $4,800 (40%) forever based on internal metrics you don't control.",
        redlines: {
          warm: "Invoices shall be payable on Net-15 terms (50% upfront deposit, 50% upon delivery), and acceptance shall be deemed granted if no written revision request is received within 7 business days.",
          balanced: "Fees are payable 50% upon execution and 50% within Net-15 days of milestone delivery, with no performance holdbacks. Overdue balances accrue 1.5% monthly late interest.",
          firm: "Strict Payment Schedule: 50% non-refundable commencement fee upon signing; 50% due Net-10 upon delivery. All holdbacks are deleted in their entirety, and work pauses automatically on any invoice 5 days past due."
        }
      },
      {
        id: "cl-ip-grab",
        section: "Section 2 — Pre-Payment & Background IP Grab",
        category: "IP Ownership Trap",
        severity: "critical",
        exposure_usd: 6500,
        fairness_delta: 18,
        quote: "All preliminary sketches, unused concepts, raw project files, and pre-existing templates created or utilized by Contractor shall vest immediately and irrevocably in Client upon creation, regardless of whether Client completes final payment.",
        plain_english: "Client takes legal ownership of your reusable code/design libraries, rejected drafts, and raw source files the second you sketch them—even if they never pay your invoice.",
        redlines: {
          warm: "Final approved deliverables transfer to Client upon full payment of the project fee, while Contractor retains ownership of pre-existing templates, tools, and unused concepts.",
          balanced: "Client receives full right and title to final approved Deliverables solely upon Contractor's receipt of payment in full. Contractor retains all Background IP, raw working files, and rejected concepts.",
          firm: "Condition Precedent: No assignment or license of any Deliverable takes effect unless and until all invoices are paid in full. All Background IP, frameworks, and unused concepts remain the exclusive property of Contractor."
        }
      },
      {
        id: "cl-auto-renew",
        section: "Section 3 — 90-Day Certified Mail Auto-Renewal",
        category: "Silent Lock-In Trap",
        severity: "high",
        exposure_usd: 1500,
        fairness_delta: 13,
        quote: "This Agreement shall automatically renew for successive twelve (12) month exclusivity periods at the same rate unless Contractor delivers certified physical mail notice of non-renewal at least ninety (90) days prior to the anniversary date.",
        plain_english: "Locks you into another year of exclusivity at last year's rates unless you mail a physical certified letter 3 months before the contract ends.",
        redlines: {
          warm: "This Agreement may be renewed for additional terms by mutual written or email agreement of both parties at least 30 days prior to expiration.",
          balanced: "Renewal requires mutual written consent via email. Either party may decline renewal or propose updated rates with 30 days email notice.",
          firm: "Auto-renewal and exclusivity are deleted. This Agreement expires automatically at the conclusion of the Initial Term unless extended by a signed written amendment."
        }
      },
      {
        id: "cl-no-kill-fee",
        section: "Section 4 — Zero Kill-Fee Termination",
        category: "Unilateral Cancellation Trap",
        severity: "high",
        exposure_usd: 2000,
        fairness_delta: 13,
        quote: "Client may terminate this Agreement at any time for convenience upon 24 hours notice without owing any kill fee or reimbursement for work-in-progress hours already performed in the current milestone.",
        plain_english: "Client can cancel the project 95% of the way through a milestone with 24 hours notice and pay $0 for the weeks of work you already completed.",
        redlines: {
          warm: "Either party may terminate for convenience upon 14 days email notice, and Client shall compensate Contractor pro-rata for all work-in-progress completed plus a 20% scheduling kill fee.",
          balanced: "Upon termination for convenience, Client shall pay for all work performed through the termination date plus a 25% kill fee on the remaining contract balance within 10 business days.",
          firm: "Termination for convenience requires 15 business days written notice, full payment for all current milestone work-in-progress, and a non-refundable 35% kill fee on remaining contracted value."
        }
      }
    ]
  },
  {
    id: "residential-apartment-lease",
    title: "Urban Residential Apartment Lease (12-Month Term)",
    counterparty: "Skyline Metro Properties LP",
    contract_value_usd: 28800,
    base_fairness_score: 38,
    document_text:
      'RESIDENTIAL APARTMENT LEASE AGREEMENT\n' +
      'This Lease Agreement is made between Skyline Metro Properties LP ("Landlord") and Resident ("Tenant") for Unit 14B at $2,400/month.\n\n' +
      '1. SECURITY DEPOSIT FORFEITURE & MANDATORY CARPET REPLACEMENT.\n' +
      'Landlord may deduct a mandatory $850 professional restaining and carpet replacement fee from Tenant\'s Security Deposit upon move-out regardless of unit cleanliness or normal wear and tear.\n\n' +
      '2. LANDLORD ENTRY WITHOUT NOTICE.\n' +
      'Landlord and its prospective buyers, contractors, or agents may enter the Premises at any hour of any day without prior notice to Tenant for inspections, appraisals, or unscheduled showings.\n\n' +
      '3. AUTOMATIC 60-DAY MONTH-TO-MONTH SURCHARGE.\n' +
      'Unless Tenant provides written notice at least 75 days prior to Lease expiration, this Lease converts to a commitment at 145% of base rent ($3,480/month) with a two-month early termination penalty.',
    clauses: [
      {
        id: "lease-deposit-trap",
        section: "Section 1 — Automatic Deposit Deduction for Normal Wear",
        category: "Deposit Forfeiture Trap",
        severity: "critical",
        exposure_usd: 850,
        fairness_delta: 20,
        quote: "Landlord may deduct a mandatory $850 professional restaining and carpet replacement fee from Tenant's Security Deposit upon move-out regardless of unit cleanliness or normal wear and tear.",
        plain_english: "Automatically takes $850 out of your security deposit even if you leave the apartment spotless.",
        redlines: {
          warm: "Security deposit deductions shall apply only to documented damage beyond normal wear and tear.",
          balanced: "No mandatory move-out fees shall apply if Premises are returned broom-clean, ordinary wear and tear excepted.",
          firm: "Deleted mandatory $850 fee: Security Deposit deductions are strictly limited to itemized physical damages exceeding statutory normal wear and tear."
        }
      },
      {
        id: "lease-entry-notice",
        section: "Section 2 — Zero-Notice 24/7 Landlord Entry",
        category: "Privacy & Quiet Enjoyment Trap",
        severity: "high",
        exposure_usd: 1200,
        fairness_delta: 18,
        quote: "Landlord and its prospective buyers, contractors, or agents may enter the Premises at any hour of any day without prior notice to Tenant for inspections, appraisals, or unscheduled showings.",
        plain_english: "Allows the landlord or real estate agents to walk into your apartment at any hour without warning.",
        redlines: {
          warm: "Except in emergencies, Landlord shall provide at least 24 hours advance email/SMS notice before entry during normal daytime hours.",
          balanced: "Non-emergency entry requires 24 hours prior written notice and must occur between 9:00 AM and 6:00 PM.",
          firm: "Strict Quiet Enjoyment: Landlord entry requires 48 hours written notice (except active fire/flood emergencies) and Tenant's scheduled window."
        }
      },
      {
        id: "lease-renewal-surge",
        section: "Section 3 — 75-Day Notice & 145% Rent Surge",
        category: "Renewal Penalty Trap",
        severity: "critical",
        exposure_usd: 3240,
        fairness_delta: 18,
        quote: "Unless Tenant provides written notice at least 75 days prior to Lease expiration, this Lease converts to a commitment at 145% of base rent ($3,480/month) with a two-month early termination penalty.",
        plain_english: "Hikes your rent by $1,080/month and charges a 2-month penalty if you don't give notice 75 days early.",
        redlines: {
          warm: "Tenant shall provide 30 days notice prior to expiration; month-to-month continuation shall not exceed 105% of base rent.",
          balanced: "Notice period is 30 days prior to Lease end, and Landlord must provide any renewal rate proposal at least 45 days in advance.",
          firm: "Notice window reduced to 30 days; month-to-month holdover rate capped at 103% of base rent with zero early termination penalty."
        }
      }
    ]
  },
  {
    id: "enterprise-saas-renewal",
    title: "B2B AI SaaS Annual Subscription Order Form",
    counterparty: "CloudScale Telemetry Inc.",
    contract_value_usd: 18000,
    base_fairness_score: 41,
    document_text:
      'ENTERPRISE SAAS ORDER FORM & MASTER SUBSCRIPTION TERMS\n' +
      'Customer subscribes to CloudScale Pro Tier ($18,000/year).\n\n' +
      '1. AUTO-RENEWAL & 18% ANNUAL PRICE ESCALATOR.\n' +
      'Each Order Form automatically renews for a 24-month term with an automatic 18% annual price uplift unless Customer cancels at least 60 days prior to the renewal date.\n\n' +
      '2. UNILATERAL AI TRAINING ON CUSTOMER DATA.\n' +
      'Vendor is granted a perpetual, worldwide, royalty-free license to use Customer\'s proprietary prompts, uploaded documents, and customer records to train and commercialize Vendor\'s foundation models.',
    clauses: [
      {
        id: "saas-price-uplift",
        section: "Section 1 — 24-Month Auto-Renewal + 18% Price Hike",
        category: "SaaS Lock-In & Price Hike Trap",
        severity: "high",
        exposure_usd: 6480,
        fairness_delta: 24,
        quote: "Each Order Form automatically renews for a 24-month term with an automatic 18% annual price uplift unless Customer cancels at least 60 days prior to the renewal date.",
        plain_english: "Locks you in for 2 more years at an 18% price increase unless you cancel 60 days ahead.",
        redlines: {
          warm: "Renewals shall be for 12-month periods with 30 days notice, and any price adjustment is capped at 5%.",
          balanced: "Renewal terms are 12 months with 30 days cancellation notice and a maximum 3% CPI-linked price cap.",
          firm: "No auto-renewal without Customer's written PO; renewal pricing locked at 0% increase for the first renewal term."
        }
      },
      {
        id: "saas-ai-training",
        section: "Section 2 — Perpetual AI Training on Proprietary Data",
        category: "Data & Trade-Secret Trap",
        severity: "critical",
        exposure_usd: 9500,
        fairness_delta: 29,
        quote: "Vendor is granted a perpetual, worldwide, royalty-free license to use Customer's proprietary prompts, uploaded documents, and customer records to train and commercialize Vendor's foundation models.",
        plain_english: "Gives the vendor permanent permission to train public AI models on your private company documents and customer data.",
        redlines: {
          warm: "Customer Data shall be used solely to provide the subscribed services to Customer and shall not be used to train shared models.",
          balanced: "Vendor shall not use Customer Data, prompts, or outputs to train, fine-tune, or improve any foundation or third-party AI models.",
          firm: "Zero Data Retention & Zero Training Guarantee: Vendor is strictly prohibited from training on, retaining, or sub-licensing any Customer Data."
        }
      }
    ]
  }
];

let presets = [...FALLBACK_PRESETS];
let activeContract = FALLBACK_PRESETS[0];
let currentStance = localStorage.getItem("clauselens_stance") || "balanced";
let acceptedClauseIds = new Set();

function escapeHtml(str) {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

function renderContractDocument() {
  document.getElementById("doc-title").textContent = activeContract.title;
  document.getElementById("doc-counterparty").textContent = `Counterparty: ${activeContract.counterparty}`;

  let html = escapeHtml(activeContract.document_text);
  activeContract.clauses.forEach(cl => {
    const escapedQuote = escapeHtml(cl.quote);
    const isProtected = acceptedClauseIds.has(cl.id);
    const cls = isProtected ? "protected" : "exposed";
    const badge = isProtected ? "✓ REDLINED" : "⚠️ TRAP";
    html = html.replace(
      escapedQuote,
      `<mark class="trap-span ${cls}" data-clause-id="${cl.id}" title="${cl.category}">${escapedQuote} [${badge}]</mark>`
    );
  });

  const viewer = document.getElementById("contract-viewer");
  viewer.innerHTML = html;
  viewer.querySelectorAll("mark.trap-span").forEach(m => {
    m.addEventListener("click", () => {
      const card = document.getElementById(`card-${m.dataset.clauseId}`);
      if (card) card.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  });
}

function renderClauseCards() {
  const stack = document.getElementById("clauses-list");
  stack.innerHTML = activeContract.clauses.map(cl => {
    const isProtected = acceptedClauseIds.has(cl.id);
    const redlineText = cl.redlines[currentStance] || cl.redlines.balanced;
    return `
      <div class="clause-card ${isProtected ? "protected" : ""}" id="card-${cl.id}">
        <div class="clause-hdr">
          <span class="clause-sec">${cl.section}</span>
          <span class="badge-pill">$${cl.exposure_usd.toLocaleString()} Exposure · +${cl.fairness_delta} Fairness</span>
        </div>
        <p class="clause-plain"><strong>Why it's risky:</strong> ${cl.plain_english}</p>
        <div class="diff-box">
          <div class="diff-del">- [ORIGINAL TRAP]: "${cl.quote}"</div>
          <div class="diff-add">+ [${currentStance.toUpperCase()} REDLINE]: "${redlineText}"</div>
        </div>
        <div class="toggle-row">
          <label>
            <input type="checkbox" class="clause-toggle" data-id="${cl.id}" ${isProtected ? "checked" : ""} />
            Include Protective Redline in Counter-Offer
          </label>
          <span class="${isProtected ? "emerald" : "rose"}">${isProtected ? "PROTECTED ✓" : "UNPROTECTED"}</span>
        </div>
      </div>
    `;
  }).join("");

  stack.querySelectorAll(".clause-toggle").forEach(cb => {
    cb.addEventListener("change", () => {
      const id = cb.dataset.id;
      if (cb.checked) acceptedClauseIds.add(id);
      else acceptedClauseIds.delete(id);
      updateAllViews();
    });
  });
}

function buildCounterOfferEmail() {
  const greetingMap = {
    warm: `Hi ${activeContract.counterparty} Team,\n\nThank you for sending over the ${activeContract.title}. I'm excited to move forward together! After reviewing the draft, I've noted a few light, standard adjustments below so we can get this signed quickly:`,
    balanced: `Dear ${activeContract.counterparty} Team,\n\nThank you for sharing the ${activeContract.title}. To align the agreement with standard commercial terms prior to execution, please find our proposed redlines below:`,
    firm: `Attention: Legal & Contracts — ${activeContract.counterparty},\n\nWe have completed our compliance review of the ${activeContract.title}. Execution is contingent upon incorporating the following protective redline revisions:`
  };

  const chosen = activeContract.clauses.filter(c => acceptedClauseIds.has(c.id));
  const bodyLines = chosen.map((cl, idx) => (
    `${idx + 1}. ${cl.section} (${cl.category})\n` +
    `   • Current Text: "${cl.quote}"\n` +
    `   • Proposed Redline (${currentStance.toUpperCase()}): "${cl.redlines[currentStance]}"\n` +
    `   • Business Rationale: ${cl.plain_english}`
  )).join("\n\n");

  const signOff = "\n\nPlease let me know once an updated clean and redlined copy is ready for signature.\n\nBest regards,\n[Your Name]";
  return `${greetingMap[currentStance]}\n\n${bodyLines || "(No redlines selected)"}${signOff}`;
}

function updateMetricsAndEmail() {
  const chosen = activeContract.clauses.filter(c => acceptedClauseIds.has(c.id));
  const fairness = Math.min(98, activeContract.base_fairness_score + chosen.reduce((acc, c) => acc + c.fairness_delta, 0));
  const protectedUsd = chosen.reduce((acc, c) => acc + c.exposure_usd, 0);

  document.getElementById("kpi-fairness").textContent = `${fairness} / 100`;
  document.getElementById("kpi-traps").textContent = `${chosen.length} / ${activeContract.clauses.length} Redlined`;
  document.getElementById("kpi-exposure").textContent = `$${protectedUsd.toLocaleString()} Protected`;
  document.getElementById("counter-email-preview").textContent = buildCounterOfferEmail();
}

function updateAllViews() {
  renderContractDocument();
  renderClauseCards();
  updateMetricsAndEmail();
}

function loadContract(contractObj) {
  activeContract = contractObj;
  acceptedClauseIds = new Set(contractObj.clauses.map(c => c.id));
  updateAllViews();
}

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const res = await fetch("/api/presets");
    if (res.ok) presets = await res.json();
  } catch (_e) {}

  document.querySelectorAll(".stance-btn").forEach(btn => {
    btn.classList.toggle("active", btn.dataset.stance === currentStance);
    btn.addEventListener("click", () => {
      currentStance = btn.dataset.stance;
      localStorage.setItem("clauselens_stance", currentStance);
      document.querySelectorAll(".stance-btn").forEach(b => b.classList.toggle("active", b === btn));
      updateAllViews();
    });
  });

  document.getElementById("preset-select").addEventListener("change", (e) => {
    const found = presets.find(p => p.id === e.target.value) || presets[0];
    loadContract(found);
  });

  document.querySelectorAll(".tab-btn").forEach(btn => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
      document.querySelectorAll(".tab-panel").forEach(p => p.classList.remove("active"));
      btn.classList.add("active");
      document.getElementById(btn.dataset.tab).classList.add("active");
    });
  });

  document.getElementById("btn-copy-email").addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(document.getElementById("counter-email-preview").textContent);
    } catch (_e) {}
    document.getElementById("copy-toast").textContent = "✓ Copied Counter-Offer Email to Clipboard!";
  });

  document.getElementById("btn-load-sample-custom").addEventListener("click", () => {
    document.getElementById("custom-contract-input").value =
      "1. All preliminary sketches, pre-existing templates, and work made for hire vest immediately in Client prior to payment.\n" +
      "2. This Subscription shall automatically renew for successive 24-month terms unless cancelled 90 days prior to renewal.\n" +
      "3. Invoices are payable Net-90 and Client may terminate at any time without owing any kill fee.";
  });

  document.getElementById("btn-analyze-custom").addEventListener("click", async () => {
    const raw = document.getElementById("custom-contract-input").value.trim();
    if (!raw) return;
    let customResult = null;
    try {
      const r = await fetch("/api/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: raw, title: "Custom Pasted Agreement" })
      });
      if (r.ok) customResult = await r.json();
    } catch (_e) {}
    if (!customResult) {
      customResult = {
        id: "custom-contract",
        title: "Custom Pasted Agreement",
        counterparty: "Custom Counterparty",
        base_fairness_score: 42,
        document_text: raw,
        clauses: FALLBACK_PRESETS[0].clauses.slice(0, 2)
      };
    }
    loadContract(customResult);
    document.querySelector("button[data-tab='tab-redlines']").click();
  });

  const savedTheme = localStorage.getItem("clauselens_theme") || "dark";
  document.documentElement.setAttribute("data-theme", savedTheme);
  document.getElementById("btn-theme-toggle").addEventListener("click", () => {
    const cur = document.documentElement.getAttribute("data-theme");
    const next = cur === "light" ? "dark" : "light";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("clauselens_theme", next);
  });

  loadContract(presets[0]);
});
