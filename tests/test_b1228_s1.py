"""B1228 -- S1. The locks assert FACTS, and one of them guards the RETRACTION:
if a later seat upgrades this arc to "sigma = 1 established", the suite goes red."""
import itertools, json, pathlib
from fractions import Fraction as F
import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
ARC = ROOT / "frontier" / "B1228_S1_the_nomination"

SL = {"A1":(3,2,1),"A2":(8,3,2),"D4":(28,6,4),"E6":(78,12,6),"E7":(133,18,7),"E8":(248,30,8)}

def test_simply_laced_level1_c_equals_rank():
    for J,(d,h,r) in SL.items():
        assert F(d, 1+h) == r, (J, F(d,1+h), r)

def test_sigma_is_one_for_E6_alone():
    """DATED NOTE, 2026-11-13 (card C17 of the building session; register row P-318, verified by main at B1906, section
    3b): the assertion below holds on its six types, as it stood. Over the sixteen simply-laced algebras of rank 1 to 8
    it does not: sigma = 1 holds at level 1 for A6, D6 and E6, and E6 alone has three primaries. That statement is
    held by test_sigma_is_one_for_three_of_the_sixteen_and_three_primaries_for_e6_alone."""
    ones = [J for J,(d,h,r) in SL.items() if F(d,1+h)/6 == 1]
    assert ones == ["E6"], ones
    # and the near-miss that makes the test non-vacuous
    assert F(SL["A2"][0], 1+SL["A2"][1])/6 == F(1,3)

def test_the_nomination_holds_and_the_control_bites():
    snappy = pytest.importorskip("snappy")
    G = [(a,b,c,d) for a,b,c,d in itertools.product(range(3),repeat=4) if (a*d-b*c)%3==1]
    assert len(G) == 24
    mul = lambda X,Y: ((X[0]*Y[0]+X[1]*Y[2])%3,(X[0]*Y[1]+X[1]*Y[3])%3,
                       (X[2]*Y[0]+X[3]*Y[2])%3,(X[2]*Y[1]+X[3]*Y[3])%3)
    inv = lambda X: (X[3]%3,(-X[1])%3,(-X[2])%3,X[0]%3)
    I = (1,0,0,1)
    def surj_count(name):
        P = snappy.Manifold(name).fundamental_group()
        g, rels = P.generators(), P.relators()
        if len(g) != 2: return None
        n = 0
        for A,B in itertools.product(G, repeat=2):
            asg = {g[0]:A, g[1]:B}
            ok = True
            for r in rels:
                v = I
                for ch in r:
                    m = asg[ch.lower()]
                    v = mul(v, m if ch.islower() else inv(m))
                if v != I: ok = False; break
            if not ok: continue
            S, fr = {I}, [I]
            while fr:
                x = fr.pop()
                for gg in (A,B):
                    for y in (mul(x,gg), mul(x,inv(gg))):
                        if y not in S: S.add(y); fr.append(y)
            if len(S) == 24: n += 1
        return n
    assert surj_count("m004") == 48
    assert surj_count("5_2") == 0, "control must bite -- not every knot nominates 2T"

def test_the_level_is_forced_by_inventory():
    c = lambda k: F(k*78, k+12)
    assert c(1) == 6 and c(1)/6 == 1
    for k in (2,3):
        assert c(k)/6 != 1, k          # blindness to k is load-bearing, not decorative

def test_the_retraction_stands():
    """sigma = 1 is NOT established. If this arc is ever upgraded to claim it, red the suite."""
    v = json.loads((ARC/"arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "OPEN", v["verdict"]
    claim = v["claim_one_line"]
    assert "RETRACT" in claim.upper()
    assert "NOT sigma = 1" in claim or "sigma is NOT deleted" in claim
    txt = (ARC/"FINDINGS.md").read_text(encoding="utf-8")
    assert "The retraction" in txt and "It does not" in txt


def _cartan(kind, n):
    """The Cartan matrix of a simply-laced simple algebra: A_n a chain; D_n a chain with a fork at its end; E_n a chain
    1-3-4-...-n with node 2 on node 4 (Bourbaki's labels)."""
    C = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
    if kind == "A": edges = [(i, i + 1) for i in range(n - 1)]
    elif kind == "D": edges = [(i, i + 1) for i in range(n - 2)] + [(n - 3, n - 1)]
    else: edges = [(0, 2), (1, 3)] + [(i, i + 1) for i in range(2, n - 1)]
    for a, b in edges: C[a][b] = C[b][a] = -1
    return C


def _det(M):
    M = [[F(x) for x in row] for row in M]; n = len(M); d = F(1)
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        if p != c: M[c], M[p] = M[p], M[c]; d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            M[r] = [M[r][k] - f * M[c][k] for k in range(n)]
    return d


def test_sigma_is_one_for_three_of_the_sixteen_and_three_primaries_for_e6_alone():
    """Added 2026-11-13 (card C17; P-318; B1906, section 3b, verified by main): over the sixteen simply-laced simple
    algebras of rank 1 to 8 at level 1, c = dim/(1 + h^v) = rank; sigma = c/6 = 1 for A6, D6 and E6; and of these E6
    alone has three primaries (the classes of P/Q, |det C| of them)."""
    algebras = {}
    for n in range(1, 9): algebras["A%d" % n] = ("A", n, n * (n + 2), n + 1)
    for n in range(4, 9): algebras["D%d" % n] = ("D", n, n * (2 * n - 1), 2 * n - 2)
    for n, d, h in ((6, 78, 12), (7, 133, 18), (8, 248, 30)): algebras["E%d" % n] = ("E", n, d, h)
    assert len(algebras) == 16
    sigma_one = []
    for name, (kind, n, dim, h) in algebras.items():
        assert F(dim, 1 + h) == n, name
        if F(n, 6) == 1: sigma_one.append(name)
    assert sigma_one == ["A6", "D6", "E6"], sigma_one
    primaries = {name: abs(_det(_cartan(algebras[name][0], algebras[name][1]))) for name in sigma_one}
    assert primaries == {"A6": 7, "D6": 4, "E6": 3}, primaries
    assert [x for x in sigma_one if primaries[x] == 3] == ["E6"]
    # the controls: the determinants the closed forms give, on the whole list
    assert all(abs(_det(_cartan(k, n))) == {"A": n + 1, "D": 4, "E": 9 - n}[k] for k, n, _, _ in algebras.values())


def test_the_note_stands_on_the_page_the_verdict_line_and_the_script():
    """Added 2026-11-13 (card C17; P-318): the old words stay, and the dated note stands beside them."""
    import re
    flat = lambda t: re.sub(r"\s+", " ", re.sub(r"^\s*>\s?", "", t, flags=re.M).replace("**", "").replace("`", ""))
    page = flat((ARC / "FINDINGS.md").read_text(encoding="utf-8"))
    old = page.index("σ = c/6 equals 1 for exactly one of nine simply-laced types")
    note = page.index("Dated note, 2026-11-13 (register row P-318", old)
    assert note - old < 2500 and "σ = 1 with exactly three primaries holds for E₆ alone." in page[note:]
    line = json.loads((ARC / "arc_verdict.json").read_text(encoding="utf-8"))["claim_one_line"]
    assert line.index("EXACTLY ONE of nine") < line.index("DATED NOTE 2026-11-13, register row P-318")
    s1 = (ARC / "s1.py").read_text(encoding="utf-8")
    assert "sigma = 1 picks out exactly ONE" in s1 and s1.index("# DATED NOTE, 2026-11-13") < s1.index("ADE = {")
