"""SEALED-DIGEST CHECK c3 (value-free; main's M_of / coupling).
Claims (agy Theorem 20 Part A; Theorem 18 Part C; relay l.218-222, 266-267, 285-294):
 (a) on the strip's order-10 lines (2/5, (2j+1)/10): R^e = lam (+,+,-,+) R^d on channels (1, j, i, k), lam = exp(2 pi i (2-j)/5);
     on its order-5 lines (2/5, j/5): the identity channel carries the opposite sign (u_1^e = -lam u_1^d);
 (b) with the scalar a0 != 0 read with the SAME sign in down and lepton (FR-COV's (-adj S, S, S)), the order-10 identity
     survives and the order-5 one breaks;
 (c) on an order-10 line a QI admixture moves D linearly (the third-generation lepton/down relation only at second order).
Main's record (S297, CHANGELOG): 'spectra coincide for every Higgs exactly on B1703's d = e points' -- its scan used a0 = 0.
This check extends it over a0 != 0 on all 40 d = e points and 40 beta-half-lifts (main's committed classification).
FIREWALL: no singular value, no ratio of singular values across sectors, no deviation magnitude of a cross-sector spectrum is
printed; only matrix-identity residuals, YES/NO coincidence of the full spectra (1e-10 of the heaviest), the double ratio D
(within-sector ratios, not firewalled) and first-order coupling coefficients inside the down sector."""
import json, math, pathlib, sys, time
from fractions import Fraction as F
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "frontier/B1827_the_framing_ledger/verification/recheck"))
from identities_and_order5 import M_of, S_of, B
from mirror_rule_probe import Z
rng = np.random.default_rng(4112026)
P355 = ROOT / "frontier/B1830_the_register_triaged/verification/recheck/p355"

def coincide(Ya, Yb):
    sa = np.sort(np.linalg.svd(Ya, compute_uv=False)); sb = np.sort(np.linalg.svd(Yb, compute_uv=False))
    return bool(np.abs(sa - sb).max() < 1e-10 * max(sa.max(), sb.max()))
def fitlam(A, Bm): return np.vdot(Bm.ravel(), A.ravel()) / np.vdot(Bm.ravel(), Bm.ravel()).real
def rel(A, Bm): return float(np.linalg.norm(A - Bm) / np.linalg.norm(A))
def Y(S, M): return B.coupling(S, M)

# ---- (a) residue sign patterns and lam on the ten strip lines, two tau
print("(a) residue relations on the strip lines (2/5, j/10), channels (1, i, j, k) relative to lam := R^e_j / R^d_j")
for tau in (0.3 + 2.6j, 0.7 + 3.1j):
    for j in range(10):
        p2 = j / 10; w = B.line_w(0.4, p2, tau)
        Rd = B.residues(*B.sector_twists(w, tau, 1, 2), tau); Re = B.residues(*B.sector_twists(w, tau, -3, 6), tau)
        lam = Re["j"] / Rd["j"]
        sg = {s: (Re[s] / (lam * Rd[s]) if abs(Rd[s]) > 1e-14 * max(abs(v) for v in Rd.values()) else None) for s in B.UNITS}
        pat = "".join("0" if v is None else ("+" if abs(v - 1) < 1e-9 else "-" if abs(v + 1) < 1e-9 else "?") for v in (sg["1"], sg["i"], sg["j"], sg["k"]))
        extra = ""
        if j % 2 == 1:
            jj = (j - 1) // 2; extra = " |lam - exp(2 pi i (2-j')/5)| = %.1e (j'=%d)" % (abs(lam - np.exp(2j * np.pi * (2 - jj) / 5)), jj)
        print("  tau=%s line (2/5, %d/10) order %d: pattern %s  |lam|-1 = %.1e%s" % (tau, j, 10 if j % 2 else 5 if j else 5, pat, abs(lam) - 1, extra))

# ---- (b) a0 != 0 on main's 80 identity points (classification from main's committed identity_v2_tauA.json)
A = json.loads((P355 / "identity_v2_tauA.json").read_text())["points"]
T = [p for p in A if p["r0"]["res_T"] < 1e-10]; Pp = [p for p in A if p["r0"]["res_P"] < 1e-10]
HL = [p for p in A if p["r0"]["dev_noQI"] < 1e-10 and p["r0"]["dev_any"] > 1e-6]
print("\n(b) classes from main's table: transposed d=e %d, plain d=e %d, beta-half-lifts %d (orders %s)" % (
    len(T), len(Pp), len(HL), sorted({p["order"] for p in HL})))
def pt(p): a, b = p["pt"].split(","); return (float(F(a)), float(F(b)))
tally = {}
t0 = time.time()
for tau in (0.3 + 2.6j, 0.7 + 3.1j):
    L = Z.radii(tau)[0]
    for cls, pts in (("T", T), ("P", Pp), ("HL", HL)):
        for p in pts:
            if cls == "P" and p in T: continue
            Md, _ = M_of(tau, pt(p), L, "down"); Me, _ = M_of(tau, pt(p), L, "lepton")
            key = (cls, p["order"])
            for _ in range(3):
                h = rng.normal(size=3) + 1j * rng.normal(size=3)
                if cls == "HL": h[0] = 0.0                                  # QI-free (Q3 order is (QI, QJ, QK))
                a0 = complex(*rng.normal(size=2))
                same = coincide(Y(S_of(a0, h), Me), Y(S_of(a0, h), Md))
                opp = coincide(Y(S_of(-a0, h), Me), Y(S_of(a0, h), Md))
                zero = coincide(Y(S_of(0, h), Me), Y(S_of(0, h), Md))
                r = None
                if cls == "T":
                    lam = fitlam(Me, Md.T); r = rel(Y(S_of(a0, h), Me), lam * Y(S_of(-a0, h), Md).T)
                d = tally.setdefault(key, dict(n=0, a0zero=0, same=0, opp=0, worstT=0.0))
                d["n"] += 1; d["a0zero"] += zero; d["same"] += same; d["opp"] += opp
                if r is not None: d["worstT"] = max(d["worstT"], r)
print("  class, order: draws | spectra coincide at a0=0 | a0!=0 same sign | a0!=0 opposite signs | worst residual of "
      "Y_e(a0,h) = lam Y_d(-a0,h)^T (T class)")
for k in sorted(tally, key=lambda k: (k[0], k[1])):
    d = tally[k]
    print("  %-2s order %2d: %3d | %3d | %3d | %3d | %s" % (k[0], k[1], d["n"], d["a0zero"], d["same"], d["opp"], ("%.1e" % d["worstT"]) if k[0] == "T" else "-"))
print("  (%.0f s)" % (time.time() - t0))

# ---- (c) QI admixture on the order-10 strip lines: D_raw linear in h_I; first-order couplings inside the down sector
print("\n(c) order-10 strip lines, a0 = 0: D_raw = (s2/s1)_e (s1/s2)_d ; doubling ratios (D(2e)-1)/(D(e)-1) ; "
      "first-order |u_k^+ Y_I v_k| / ||Y_I|| in the down sector at h_I = 0 (k = 1, 2, 3 light to heavy)")
for tau in (0.3 + 2.6j, 0.7 + 3.1j):
    L = Z.radii(tau)[0]
    for p2 in (0.1, 0.3):
        Md, _ = M_of(tau, (0.4, p2), L, "down"); Me, _ = M_of(tau, (0.4, p2), L, "lepton")
        h0 = np.array([0, 0.8 + 0.3j, -0.5 + 1.1j]); hi = 1 + 1j
        def Draw(eps):
            S = S_of(0, h0 + np.array([eps * hi, 0, 0]))
            se = np.sort(np.linalg.svd(Y(S, Me), compute_uv=False)); sd = np.sort(np.linalg.svd(Y(S, Md), compute_uv=False))
            return (se[1] / se[0]) * (sd[0] / sd[1])
        D0 = Draw(0.0); r1 = (Draw(2e-4) - 1) / (Draw(1e-4) - 1); r2 = (Draw(4e-4) - 1) / (Draw(2e-4) - 1)
        Yd = Y(S_of(0, h0), Md); U, s, Vh = np.linalg.svd(Yd); o = np.argsort(s); U = U[:, o]; V = Vh.conj().T[:, o]
        YI = Y(B.QI, Md); nI = np.linalg.norm(YI, 2)
        fo = [abs(U[:, k].conj() @ YI @ V[:, k]) / nI for k in range(3)]
        print("  tau=%s line (2/5, %.1f): D_raw(h_I=0) - 1 = %.1e ; doubling ratios %.4f %.4f ; first-order (k=1,2,3) = %.2e %.2e %.2e"
              % (tau, p2, D0 - 1, r1, r2, *fo))
