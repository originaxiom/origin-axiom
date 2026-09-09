"""B1302 setup: m202 from SnapPy (facts), an EXACT holonomy over Q(zeta_12) in Fricke form (tr a = tr b = omega-bar, tr ab = -sqrt3),
the relator and both cusps checked exactly, and the automorphism census by exact traces (word pairs of length <= 5, classes by the
exact H1 action) -- fc R72b / sm:B1282 report 180 pairs in 12 classes."""
import os, sys, json, itertools, warnings
warnings.filterwarnings("ignore")
import numpy as np, snappy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1297_the_spectral_cover_index", "verification"))
import d2lib as L
from d2lib import K, OMEGA, ONE, ZERO, Z12
M = snappy.Manifold("m202"); G = M.fundamental_group()
print("m202:", M, "cusps", M.num_cusps(), "H1", M.homology(), "vol %.6f" % M.volume(), "|Isom|", M.symmetry_group().order(), "amphicheiral", M.symmetry_group().is_amphicheiral(), "CS %.6f" % M.chern_simons())
print("pi_1:", G.generators(), G.relators(), "peripheral:", G.peripheral_curves(), "shapes:", [str(s)[:22] for s in M.cusp_info("shape")])
RELS = [L.word_from_snappy(r) for r in G.relators()]; CUSPS = [[L.word_from_snappy(w) for w in pc] for pc in G.peripheral_curves()]
# numeric traces from SnapPy for the target triple
Gh = M.high_precision().fundamental_group()
ta, tb, tab = (complex(str(Gh.SL2C(w).trace()).replace(" ", "")) if False else None for w in ("a", "b", "ab"))
import re
def tr_num(w):
    m = Gh.SL2C(w); return complex(m[0, 0]) + complex(m[1, 1]) if hasattr(m, "__getitem__") else None
try: ta, tb, tab = [complex(str(Gh.SL2C(w).trace()).replace("j", "j")) for w in ("a", "b", "ab")]
except Exception: ta, tb, tab = [complex(Gh.SL2C(w).trace()) for w in ("a", "b", "ab")]
print("SnapPy traces: tr a = %s  tr b = %s  tr ab = %s" % (ta, tb, tab))
# exact candidates: t_a, t_b in {omega, omega-bar}, t_ab in {+-sqrt3}; Fricke form A = [[ta,-1],[1,0]], B = [[0,u],[-1/u,tb]], u + 1/u = t_ab
SQRT3 = Z12 + Z12.inv()
cands = []
for t_a in (OMEGA, OMEGA * OMEGA):
    for t_b in (OMEGA, OMEGA * OMEGA):
        for s in (ONE, K(-1)):
            t_ab = SQRT3 * s
            # u + 1/u = t_ab  ->  u = zeta_12^k with 2cos(k pi/6) = +-sqrt3: k = 1, 11 (+sqrt3) or 5, 7 (-sqrt3)
            for k in (1, 5, 7, 11):
                u = ONE
                for _ in range(k): u = u * Z12
                if not (u + u.inv() == t_ab): continue
                for sa in (ONE, K(-1)):
                    for sb in (ONE, K(-1)):
                        A = L.mscale(L.mat([[t_a, -1], [1, 0]]), sa); B = L.mscale(L.mat([[0, u], [-u.inv(), t_b]]), sb)
                        rho = L.Rep({"a": A, "b": B})
                        if all(L.meq(rho(R), L.eye(2)) for R in RELS):
                            cands.append((str(t_a), str(t_b), str(t_ab), k, str(sa), str(sb), A, B))
print("exact SL(2) lifts satisfying the relator:", len(cands))
for c in cands[:8]: print("   tr a", c[0], "tr b", c[1], "tr ab", c[2], "u = zeta^%d" % c[3], "signs", c[4], c[5])
assert cands, "no exact lift found"
# pick the lift matching SnapPy's traces numerically (up to the sign lifts)
def close(x, y): return abs(x - y) < 1e-6
pick = None
for c in cands:
    A, B = c[6], c[7]; rho = L.Rep({"a": A, "b": B})
    if close(abs(L.tr(A).cx()), abs(ta)) and close(L.tr(A).cx().imag * ta.imag >= 0, True):
        pick = c; break
pick = pick or cands[0]; A, B = pick[6], pick[7]; rho = L.Rep({"a": A, "b": B})
print("chosen lift: tr a =", L.tr(A), " tr b =", L.tr(B), " tr ab =", L.tr(rho(L.word_from_snappy('ab'))))
for i, (m, l) in enumerate(CUSPS):
    print(f"cusp {i}: tr m = {L.tr(rho(m))}, tr l = {L.tr(rho(l))}, [m,l] = I: {L.meq(rho(m + l + L.inv_word(m) + L.inv_word(l)), L.eye(2))}")
# automorphism census by exact traces: words of length <= 5, (a', b') preserving the exact triple up to the SL2 sign lifts and killing the relator
def reduced(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase(): out.pop()
        else: out.append(ch)
    return "".join(out)
def inv_str(w): return w.swapcase()[::-1]
def subst(word, ia, ib):
    out = ""
    for ch in word:
        img = ia if ch.lower() == "a" else ib
        out += img if ch.islower() else inv_str(img)
    return reduced(out)
An, Bn = np.array(L.to_cx(A)), np.array(L.to_cx(B)); letters = {"a": An, "b": Bn, "A": np.linalg.inv(An), "B": np.linalg.inv(Bn)}
def ev(w):
    Mx = np.eye(2, dtype=complex)
    for ch in w: Mx = Mx @ letters[ch]
    return Mx
TA, TB, TAB = np.trace(An), np.trace(Bn), np.trace(An @ Bn)
words = [""]
for n in range(1, 6):
    for tup in itertools.product("aAbB", repeat=n):
        w = "".join(tup)
        if reduced(w) == w: words.append(w)
words = [w for w in words if w]
def okt(w, t): x = np.trace(ev(w)); return any(abs(x - y) < 1e-9 for y in (t, -t))
ca = [w for w in words if okt(w, TA)]; cb = [w for w in words if okt(w, TB)]
relstr = G.relators()[0]
def is_pm_I(Mx): return np.allclose(Mx, np.eye(2), atol=1e-9) or np.allclose(Mx, -np.eye(2), atol=1e-9)
found = []
for ia in ca:
    Ma = ev(ia)
    for ib in cb:
        Mb = ev(ib)
        if not any(abs(np.trace(Ma @ Mb) - y) < 1e-9 for y in (TAB, -TAB)): continue
        if not is_pm_I(ev(subst(relstr, ia, ib))): continue
        found.append((ia, ib))
def h1_action(ia, ib):
    e = lambda w, g: sum(1 if ch == g else -1 if ch == g.upper() else 0 for ch in w)
    return ((e(ia, "a"), e(ib, "a")), (e(ia, "b"), e(ib, "b")))     # columns = images of a, b in H1 = Z^2
classes = {}
for ia, ib in found: classes.setdefault(h1_action(ia, ib), []).append((ia, ib))
print(f"automorphism census: {len(found)} word pairs (length <= 5), {len(classes)} distinct H1 actions")
for k, v in sorted(classes.items(), key=lambda kv: -len(kv[1])): print("   H1 action", k, " reps", v[:2], " count", len(v))
json.dump(dict(pairs=len(found), classes=len(classes), h1_actions=[list(map(list, k)) for k in classes],
               lift=dict(tr_a=str(L.tr(A)), tr_b=str(L.tr(B)), u_power=pick[3], A=[[str(x) for x in r] for r in A], B=[[str(x) for x in r] for r in B]),
               rels=RELS, cusps=CUSPS), open("m202_setup.json", "w"), default=str)
