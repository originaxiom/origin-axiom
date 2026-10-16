"""B1662 -- the pull-back acts on the records. Live and exact: [LR, RL] = -(unipotent) with trace -2, sign-free;
(L R^-1 L)^2 = (L^-1 R)^3 = -I; no non-negative determinant-1 matrix (entries <= 12) has trace below 2; the mirror sends
L, R to their inverses. Stored: the seeded walks (W1 saturates, W2 grows, W3 positive). The record: GENESIS v1.48 as
amend.py builds it from the received v1.47; the re-grades on B1482, B1479, B1083 and the scope sentences."""
import json, pathlib, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1662_the_pull_back_acts_on_the_records"
I = (1, 0, 0, 1); L = (1, 1, 0, 1); R = (1, 0, 1, 1)
def mul(X, Y): a, b, c, d = X; e, f, g, h = Y; return (a*e + b*g, a*f + b*h, c*e + d*g, c*f + d*h)
def inv(X): a, b, c, d = X; return (d, -b, -c, a)
def neg(X): return tuple(-x for x in X)


def test_live_exact_facts_and_bites():
    LR, RL = mul(L, R), mul(R, L)
    C = mul(mul(LR, RL), mul(inv(LR), inv(RL)))
    assert C[0] + C[3] == -2 and neg(C) != I and neg(C)[0] + neg(C)[3] == 2
    assert all(mul(mul(X, Y), mul(inv(X), inv(Y))) == C for X in (LR, neg(LR)) for Y in (RL, neg(RL)))
    S = mul(mul(L, inv(R)), L); V = mul(inv(L), R)
    assert mul(S, S) == neg(I) and mul(mul(V, V), V) == neg(I)
    assert mul(mul(L, R), L) != S and mul(L, R) != V                                  # bite: no forward word is the rotation
    tr = {a + d for a in range(13) for b in range(13) for c in range(13) for d in range(13) if a*d - b*c == 1}
    assert min(tr) == 2 and not tr & {-2, -1, 0, 1}
    J = (1, 0, 0, -1)
    assert mul(mul(J, L), J) == inv(L) and mul(mul(J, R), J) == inv(R) and mul(mul(J, L), J) != L


def test_stored_walks_and_the_record():
    d = json.load(open(A / "verification" / "the_pull_back_acts.json"))
    assert d["all_hold"] is True
    assert abs(d["W1"]["mean_returns_T4000"] - d["W1"]["mean_returns_T500"]) < 0.15
    assert d["W2"]["mean_returns_T4000"] > 2.2*d["W2"]["mean_returns_T500"] and 0.07 < d["W3"]["escape_rate"] < 0.13
    g = (ROOT / "GENESIS.md").read_text(encoding="utf-8")
    assert "**Version 1.48 · 2026-10-16 · canonical.**" in g
    assert "| GM5b | Inverse moves are legal | **ADOPTED [v1.48]**" in g and "| FK4 | Inverse moves (GM5b) | **[v1.48] ANSWERED**" in g
    r = subprocess.run([sys.executable, str(A / "adoption" / "amend.py"), "--check"], capture_output=True)
    assert r.returncode == 0
    for arc in ("B1482", "B1479", "B1083", "B1640", "B1454", "B1422"):
        f = next((ROOT / "frontier").glob(arc + "_*")) / "FINDINGS.md"
        assert "## Addendum (2026-10-16, B1662)" in f.read_text(encoding="utf-8"), arc
    for arc in ("B1482", "B1479", "B1083"):
        v = json.load(open(next((ROOT / "frontier").glob(arc + "_*")) / "arc_verdict.json"))
        assert "B1662" in v["claim_one_line"], arc
    assert json.load(open(A / "arc_verdict.json"))["verdict"] == "PROVED"
