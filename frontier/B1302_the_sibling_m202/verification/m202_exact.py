"""B1302 setup: an EXACT holonomy of m202 in SL(2, Z[omega]) (m202 is tetrahedral, so its group is conjugate into PSL(2, O_3)).
Search small-entry matrices with tr a = tr b = omega-bar (or omega: the other orientation lift) and tr ab = +-sqrt(-3), det 1, relator = +-I,
then fix the SL2 sign lifts.  Output: A, B over Q(zeta_12) with relator = +I, and both cusps' peripheral traces."""
import os, sys, json, itertools, warnings
warnings.filterwarnings("ignore")
import numpy as np, snappy
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "B1297_the_spectral_cover_index", "verification"))
import d2lib as L
from d2lib import K, OMEGA, ONE, ZERO
M = snappy.Manifold("m202"); G = M.fundamental_group(); rel = G.relators()[0]
RELS = [L.word_from_snappy(rel)]; CUSPS = [[L.word_from_snappy(w) for w in pc] for pc in G.peripheral_curves()]
w_cx = OMEGA.cx()
R = range(-2, 3)
elems = [(x, y) for x in R for y in R]                       # x + y*omega
def k(e): return K(e[0]) + K(e[1]) * OMEGA
def cxv(e): return e[0] + e[1] * w_cx
# candidate A: trace t, det 1: p + s = t, ps - qr = 1
def mats_with_trace(t):
    out = []
    tc = t.cx()
    for p in elems:
        s_c = tc - cxv(p)
        # s = t - p must be in the box
        sy = round(s_c.imag / w_cx.imag); sx = round(s_c.real - sy * w_cx.real)
        if abs(sx) > 2 or abs(sy) > 2: continue
        s = (sx, sy)
        if abs(cxv(s) - s_c) > 1e-9: continue
        target = cxv(p) * cxv(s) - 1                            # qr = ps - 1
        for q in elems:
            qc = cxv(q)
            if abs(qc) < 1e-12:
                if abs(target) < 1e-12:
                    for r in elems: out.append((p, q, r, s))
                continue
            rc = target / qc
            ry = round(rc.imag / w_cx.imag); rx = round(rc.real - ry * w_cx.real)
            if abs(rx) > 2 or abs(ry) > 2 or abs(cxv((rx, ry)) - rc) > 1e-9: continue
            out.append((p, q, (rx, ry), s))
    return out
found = []
for t_a in (OMEGA * OMEGA, OMEGA):
    As = mats_with_trace(t_a)
    An = [np.array([[cxv(p), cxv(q)], [cxv(r), cxv(s)]]) for p, q, r, s in As]
    target_tab = [np.sqrt(3) * 1j, -np.sqrt(3) * 1j]
    def ev(word, A, B):
        D = {"a": A, "b": B, "A": np.linalg.inv(A), "B": np.linalg.inv(B)}; Mx = np.eye(2, dtype=complex)
        for ch in word: Mx = Mx @ D[ch]
        return Mx
    for i, (Ai, Am) in enumerate(zip(As, An)):
        for Bi, Bm in zip(As, An):                              # same trace for b (tr a = tr b)
            tab = np.trace(Am @ Bm)
            if not any(abs(tab - y) < 1e-9 for y in target_tab): continue
            Rm = ev(rel, Am, Bm)
            if np.allclose(Rm, np.eye(2), atol=1e-9) or np.allclose(Rm, -np.eye(2), atol=1e-9):
                found.append((t_a, Ai, Bi, np.allclose(Rm, np.eye(2), atol=1e-9)))
                if len(found) >= 4: break
        if len(found) >= 4: break
    if found: break
print("exact SL(2, Z[omega]) pairs found (first few):", len(found))
assert found, "no small-entry exact pair; widen the box"
t_a, Ai, Bi, plus = found[0]
A = L.mat([[k(Ai[0]), k(Ai[1])], [k(Ai[2]), k(Ai[3])]]); B = L.mat([[k(Bi[0]), k(Bi[1])], [k(Bi[2]), k(Bi[3])]])
rho = L.Rep({"a": A, "b": B})
if not L.meq(rho(RELS[0]), L.eye(2)):
    # fix the sign lift: try (-A, B), (A, -B), (-A, -B)
    for sa, sb in ((-1, 1), (1, -1), (-1, -1)):
        A2, B2 = L.mscale(A, K(sa)), L.mscale(B, K(sb)); r2 = L.Rep({"a": A2, "b": B2})
        if L.meq(r2(RELS[0]), L.eye(2)): A, B, rho = A2, B2, r2; break
assert L.meq(rho(RELS[0]), L.eye(2)), "relator not +I in any sign lift"
print("A =", A, " B =", B)
print("tr a =", L.tr(A), " tr b =", L.tr(B), " tr ab =", L.tr(rho(L.word_from_snappy('ab'))), " det A, det B =", L.det2(A), L.det2(B))
for i, (m, l) in enumerate(CUSPS):
    print(f"cusp {i}: tr m = {L.tr(rho(m))}, tr l = {L.tr(rho(l))}, [m,l] = I: {L.meq(rho(m + l + L.inv_word(m) + L.inv_word(l)), L.eye(2))}")
json.dump(dict(A=[[str(x) for x in r] for r in A], B=[[str(x) for x in r] for r in B], rel=rel, cusps=G.peripheral_curves()), open("m202_exact.json", "w"))
print("m202 EXACT: OK")
