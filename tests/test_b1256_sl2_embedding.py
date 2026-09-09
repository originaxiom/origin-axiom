"""B1256 — which sl2? Four embeddings type h^1 = 3 as three chiral; one needs no assumption."""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "frontier" / "B1256_sl2_embedding" / "verification" / "sl2_embedding.py"


def test_the_script_runs_and_selftests():
    r = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-3000:] + r.stderr[-3000:]
    assert "SELFTEST: PASS" in r.stdout, r.stdout[-500:]


def _mod():
    sys.path.insert(0, str(SCRIPT.parent))
    import sl2_embedding as S
    return S


def test_the_machinery_validates_against_banked_work():
    """Principal must return orbit dim 72 and sl2 index 156 (B1242's banked Dynkin index)."""
    S = _mod()
    WT, Cinv, roots = S.weights_27(), S.CARTAN.inv(), S.roots_E6()
    assert len(roots) == 72
    assert S.orbit_dim(S.PRINCIPAL, roots) == 72
    d = S.decompose([int(v) for v in S.h_on_27(S.PRINCIPAL, WT, Cinv)])
    assert [k + 1 for k in d] == [17, 9, 1]
    assert sum(n * (n + 1) * (n + 2) // 6 for n in d) // 6 == 156


def test_four_candidates_and_exactly_one_is_assumption_free():
    """The corrected criterion: 3 nontrivial ODD summands, 0 trivial. Four hits, one clean."""
    S = _mod()
    import itertools
    WT, Cinv, roots = S.weights_27(), S.CARTAN.inv(), S.roots_E6()
    ok, free = [], []
    for c in itertools.product((0, 1, 2), repeat=6):
        vals = S.h_on_27(c, WT, Cinv)
        if any(v != int(v) for v in vals):
            continue
        d = S.decompose([int(v) for v in vals])
        if d is None:
            continue
        dims = [k + 1 for k in d]
        if sum(1 for t in dims if t % 2 == 1 and t > 1) == 3 and 1 not in dims:
            ok.append((c, dims))
            if all(t % 2 == 1 for t in dims):
                free.append((c, dims))
    assert len(ok) == 4, ok
    assert len(free) == 1 and free[0] == ((2, 2, 2, 0, 2, 2), [13, 9, 5]), free


def test_9_9_9_does_not_exist_but_7_7_7_does():
    """The correction: non-existence is real for 9+9+9; three identical summands DO exist."""
    S = _mod()
    import itertools
    WT, Cinv = S.weights_27(), S.CARTAN.inv()
    trip = []
    for c in itertools.product((0, 1, 2), repeat=6):
        vals = S.h_on_27(c, WT, Cinv)
        if any(v != int(v) for v in vals):
            continue
        d = S.decompose([int(v) for v in vals])
        if d is None:
            continue
        dims = [k + 1 for k in d]
        nod = [t for t in dims if t % 2 == 1 and t > 1]
        if len(nod) == 3 and len(set(nod)) == 1:
            trip.append(dims)
    assert any(t.count(7) == 3 for t in trip), "7+7+7 exists"
    assert not any(t.count(9) == 3 for t in trip), "9+9+9 does not"


def test_I25_registered_UNEARNED_with_a_documented_raise():
    led = (ROOT / "docs" / "IDENTIFICATION_LEDGER.md").read_text(encoding="utf-8")
    row = next(l for l in led.splitlines() if l.startswith("| I-25 |"))
    assert "**UNEARNED**" in row and "B1256" in row
    b = json.loads((ROOT / "docs" / "IDENTIFICATION_BASELINE.json").read_text(encoding="utf-8"))
    raise_ = next(r for r in b["_baseline_raises"] if r.get("row") == "I-25")
    assert raise_["from"] == 9 and raise_["to"] == 10 and raise_.get("reason")
    assert "I-25" in b["rows"]
