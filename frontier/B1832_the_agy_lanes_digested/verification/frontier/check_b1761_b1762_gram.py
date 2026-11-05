"""agy:B1761 Thm 3 / agy:B1762 sec 2.1, the two Gram identities, on MAIN's b1656_funcs (data-free; no measured number read).

Sigma^(s)_cd = Tr(Y_c^dag Y_d) / sum_a Tr(Y_a^dag Y_a),  Y_c = coupling(Q_c, weighted_M(u^(s))),  Q = (QI, QJ, QK) (= e_1, e_2, e_3
in agy's naming, index 0, 1, 2), u_s = sqrt(2 pi L + c_s) R_s.
 G1: Sigma^(up)_{0,(1,2)} = 0 (the QI channel Frobenius-orthogonal to QJ, QK) -- agy: on (2/5, 1/10).
 G2: Sigma^(lep) = P Sigma^(down) P, P = diag(-1, 1, 1) -- agy: on (2/5, 1/10).
Asked here: the algebraic source of each, the domain (all ten (2/5, k/10) lines, the (1/5, k/10) lines, controls), and the
stronger matrix statement behind G2 (singular values of Y_lep(H) = those of Y_down(PH) for EVERY Higgs H?), against
B1742's 'lepton = down only for a QI-free Higgs on the order-10 lines'.  Also agy:B1762's Sigma^(up) eigenvalues at its point."""
import json, math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from _main_frame import B, SECT, cm

Bf = B(); CM = cm()
QS = [Bf.QI, Bf.QJ, Bf.QK]; KEYS = list(Bf.UNITS)
P = np.diag([-1.0, 1.0, 1.0])
OUT = {}

# --- 1. the Gram form as a hermitian form in the channel weights u ----------------------------------------------
A = {(c, s): Bf.coupling(QS[c], Bf.EDUAL[s]) for c in range(3) for s in KEYS}
def G(c, d): return np.array([[np.trace(A[(c, s)].conj().T @ A[(d, t)]) for t in KEYS] for s in KEYS])
print("1. Tr(Y_c^dag Y_d) = sum_{s,t} conj(u_s) u_t G^{cd}_{st}; nonzero (s, t) entries of G^{cd}:")
struct = {}
for c, d in [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]:
    g = G(c, d); nz = [(KEYS[i], KEYS[j], complex(np.round(g[i, j], 12))) for i in range(4) for j in range(4) if abs(g[i, j]) > 1e-12]
    struct["%d%d" % (c, d)] = [(a, b, [v.real, v.imag]) for a, b, v in nz]
    print("   (c,d)=(%d,%d): %s" % (c, d, ["%s%s:%s" % (a, b, v) for a, b, v in nz]))
OUT["gram_form_structure"] = struct
# does flipping u_i reproduce P-conjugation, for random u?
rng = np.random.default_rng(11)
def gram(u):
    M = Bf.weighted_M(u); Y = [Bf.coupling(Q, M) for Q in QS]
    S = np.array([[np.trace(Y[c].conj().T @ Y[d]) for d in range(3)] for c in range(3)]); return S / np.trace(S).real
dev_flip = 0.0
for _ in range(20):
    u = {s: complex(*rng.normal(size=2)) for s in KEYS}; uf = dict(u); uf["i"] = -u["i"]
    dev_flip = max(dev_flip, np.abs(gram(uf) - P @ gram(u) @ P).max())
OUT["flip_u_i_equals_P_conjugation_max_dev"] = dev_flip
print("   flipping u_i -> -u_i equals Sigma -> P Sigma P for 20 random u: max dev %.1e" % dev_flip)

# --- 2. the identities on lines ---------------------------------------------------------------------------------
def sector_u(line, t, L, sec):
    w = float(line[0]) * t + float(line[1]); x, y = Bf.sector_twists(w, t, *SECT[sec]); R = Bf.residues(x, y, t); c = Bf.cA(x, y, t, R)
    return {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in KEYS}, R

lines = [(Fr(2, 5), Fr(k, 10)) for k in range(10)] + [(Fr(1, 5), Fr(k, 10)) for k in (1, 2, 3)] + [(Fr(1, 7), Fr(3, 7)), (Fr(3, 10), Fr(1, 10)), (Fr(0), Fr(1, 6)), (Fr(1, 3), Fr(1, 2))]
taus = [0.3145 + 3.0345j, -0.21 + 1.7j]
rows = []
for line in lines:
    for t in taus:
        L = CM.radii(t)[0]
        uu, Ru = sector_u(line, t, L, "up"); ud, Rd = sector_u(line, t, L, "down"); ue, Re = sector_u(line, t, L, "lep")
        Su, Sd, Se = gram(uu), gram(ud), gram(ue)
        g1 = float(np.hypot(abs(Su[0, 1]), abs(Su[0, 2]))); g2 = float(np.abs(Se - P @ Sd @ P).max()); g2plain = float(np.abs(Se - Sd).max())
        # the matrix statement behind G2: singular values for random Higgs directions
        sv_flip, sv_plain = 0.0, 0.0
        Md, Me = Bf.weighted_M(ud), Bf.weighted_M(ue)
        for _ in range(6):
            h = rng.normal(size=3) + 1j * rng.normal(size=3)
            sd = np.linalg.svd(Bf.coupling(sum(h[k] * QS[k] for k in range(3)), Md), compute_uv=False)
            sdP = np.linalg.svd(Bf.coupling(sum((P @ h)[k] * QS[k] for k in range(3)), Md), compute_uv=False)
            se = np.linalg.svd(Bf.coupling(sum(h[k] * QS[k] for k in range(3)), Me), compute_uv=False)
            sv_flip = max(sv_flip, np.abs(se - sdP).max() / se.max()); sv_plain = max(sv_plain, np.abs(se - sd).max() / se.max())
        # residue relation lep vs down (up to one common factor)
        ratios = {s: (Re[s] / Rd[s] if abs(Rd[s]) > 1e-13 else None) for s in KEYS}
        rows.append({"line": [str(line[0]), str(line[1])], "tau": [t.real, t.imag], "L": L, "G1_up_offblock": g1, "G2_lep_vs_PdownP": g2,
                     "lep_vs_down_plain": g2plain, "sv_lep(H)_vs_down(PH)": sv_flip, "sv_lep(H)_vs_down(H)": sv_plain,
                     "abs_R_i_up": abs(Ru["i"]), "R_lep/R_down": {s: (None if v is None else [v.real, v.imag]) for s, v in ratios.items()}})
print("2. line            tau            G1 up off-block  G2 |lep-PdP|  |lep-d|   sv lep(H)~down(PH)  sv lep(H)~down(H)  |R_i^up|")
for r in rows:
    print("   (%-4s,%-5s) %7.4f%+.4fi   %9.1e     %9.1e   %8.1e   %9.1e          %9.1e        %8.1e" % (r["line"][0], r["line"][1], r["tau"][0], r["tau"][1],
          r["G1_up_offblock"], r["G2_lep_vs_PdownP"], r["lep_vs_down_plain"], r["sv_lep(H)_vs_down(PH)"], r["sv_lep(H)_vs_down(H)"], r["abs_R_i_up"]))
OUT["lines"] = rows
print("   R_lep/R_down per channel on (2/5, 1/10) at tau0:", {s: (None if v is None else complex(*v)) for s, v in rows[2]["R_lep/R_down"].items()})
print("   R_lep/R_down per channel on (2/5, 2/10) at tau0:", {s: (None if v is None else complex(*v)) for s, v in rows[4]["R_lep/R_down"].items()})

# --- 3. agy:B1762's Sigma^(up) eigenvalues at its probe point (L_max) and B1759's 'raw matter vector' invariant ----
t = 0.3145 + 3.0345j; L = CM.radii(t)[0]
uu, Ru = sector_u((Fr(2, 5), Fr(1, 10)), t, L, "up"); Su = gram(uu)
ev = np.linalg.eigvalsh(Su[1:, 1:]); OUT["b1762"] = {"L_max": L, "Sigma_up_00": Su[0, 0].real, "block_eigs": ev.tolist(), "boost": float(ev.max() / Su[0, 0].real)}
print("3. (2/5,1/10) tau=0.3145+3.0345i, L_max=%.4f: Sigma^up_00 = %.4f; (QJ,QK)-block eigenvalues %s; boost = max/Sigma_00 = %.4f"
      % (L, Su[0, 0].real, np.round(ev, 4), ev.max() / Su[0, 0].real))
for tt in [0.3145 + 3.0345j, (1 + 1j * math.sqrt(84)) / 3, 0.3145 + 3.10j, 0.3145 + 2.95j]:
    Lm = CM.radii(tt)[0]; uu, _ = sector_u((Fr(2, 5), Fr(1, 10)), tt, Lm, "up"); v = np.array([uu["i"], uu["j"], uu["k"]])
    print("   weighted u_up=(u_i,u_j,u_k) at tau=%.4f%+.4fi (L_max %.3f): I = %.4f" % (tt.real, tt.imag, Lm, abs(v @ v) / np.vdot(v, v).real))
json.dump(OUT, open(pathlib.Path(__file__).with_suffix(".json"), "w"), indent=1, default=str)
print("exit 0")
