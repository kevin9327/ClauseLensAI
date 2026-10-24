import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from backend.clause_engine import PRESET_CONTRACTS, analyze_custom_contract


def test_presets_and_three_tier_stance_redlines():
    assert len(PRESET_CONTRACTS) == 3
    for preset in PRESET_CONTRACTS:
        assert len(preset["clauses"]) >= 2
        for cl in preset["clauses"]:
            assert set(cl["redlines"].keys()) == {"warm", "balanced", "firm"}
            assert cl["quote"] in preset["document_text"]


def test_custom_contract_trap_scanner():
    sample = (
        "All preliminary sketches and pre-existing templates vest immediately in Client. "
        "This Agreement shall automatically renew for successive 12 month periods. "
        "Invoices are payable Net-90 and Client may terminate at any time without owing any kill fee."
    )
    res = analyze_custom_contract(sample, "Sample Custom MSA")
    assert res["title"] == "Sample Custom MSA"
    assert len(res["clauses"]) == 3
    assert res["base_fairness_score"] < 50


def test_official_learn_ai_basics_devpost_artifacts():
    gitignore = (ROOT_DIR / ".gitignore").read_text(encoding="utf-8")
    assert "devpost/learner-profile.md" in gitignore

    required_files = ["scope.md", "prd.md", "spec.md", "checklist.md", "app-map.html"]
    for fn in required_files:
        p = ROOT_DIR / "devpost" / fn
        assert p.exists(), f"Missing devpost/{fn}"
        content = p.read_text(encoding="utf-8")
        if fn.endswith(".md"):
            assert "status: approved" in content
