#!/usr/bin/env python3
"""B499 -- CL-3D (Gate D): the non-Hermitian spectral data package at the object's kappa.

PREREG: docs/CLOSURE_CAMPAIGN_2026-07.md (CL-3D) + local README.md. Outcome enum (committed):
DATA-BANKED (+ a precisely posed conjecture) / SURPRISE (structure contradicting the DG picture
-> H1 discipline, owner present before voicing).

QUESTION (Gate D, docs/OPEN_PROBLEMS.md). The metallic trace map at real kappa>2 is the Fibonacci
Hamiltonian (Cantor spectrum, Damanik-Gorodetski horseshoe; K007/K010). The object's actual
kappa = sqrt(3) e^{+-i pi/6} is COMPLEX (kappa - 2 = e^{+-2 i pi/3}, a primitive cube root of
unity; K020 sec.5) -- the Schrodinger cocycle is non-self-adjoint (coupling lam = e^{+-i pi/3},
a primitive 6th root of unity, since kappa = 2 + lam^2). Is there a DG-type spectral theorem
there? This probe produces the conjecture-shaped data a non-self-adjoint spectral theorist needs,
each item with error control and a Hermitian control (MB6: run the control).

METHOD (all banked, reused verbatim where possible):
  - trace-map escape rate gamma (B186 estimator, validated on DG ground truth; B451 asymptotic
    correction noted -- the anchor below locks the B186 EARLY-WINDOW value 0.51 that B451
    confirmed reproduces with this estimator);
  - MST max-gap / diameter (B163/B165 -- the banked total-disconnectedness diagnostic);
  - eigenvalue-cloud box dimension (B186 C2 -- finite-depth effective values, weakly separating
    at this depth for real kappa; recorded honestly);
  - pseudospectra sigma_min(z - H) via complex Schur + inverse iteration on the triangular
    factor (validated against direct SVD on a subsample), eigenvector condition numbers,
    OBC-vs-PBC spectral movement (non-normality / spectral-pooling monitors).

STRUCTURE
  S0 [exact, sympy]  the level set named: invariant conservation, seed-on-surface identity,
      kappa - 2 = zeta_3 (Phi_3(kappa-2) = 0, Eisenstein), the Galois Z/2 swapping the +- pair
      (K020/B285), fixed points of T + the B124 void Jacobian {phi^2, -1, phi^-2}, and the
      structural operator identities (H complex symmetric; H(conj lam) = conj H(lam)).
  S1 [num, CONTROLS -- prereg: any failure => INVALID, stop]  the Hermitian anchors: gamma
      reproduces B186's banked 0.51 at lam=3; V=1 Fibonacci level set (kappa=3) shows the DG
      Cantor signatures (gamma>0, persistent MST gap >> band); kappa=2 periodic limit behaves
      as K010's dictionary says (gamma~0, non-escaping real set = the band [-2,2] by measure,
      MST gap -> 0); eigenvalues sit deep in the non-escaping set (escape-time control).
  S2 [num]  the object's level set kappa = sqrt(3) e^{i pi/6}:
      (a) complexified trace-map escape structure: E-plane escape-time map (2D escape rate),
          real section (empty), symmetric x=y slice (both z-branches), the diagonal line
          through the two fixed points, the conjugate level (exact mirror);
      (b) pseudospectra of the non-self-adjoint approximants (233, 610; eigenvalues to 1597):
          sigma_min portraits, eps-decade areas, amplification dist/sigma_min vs the Hermitian
          control, cond(V) growth, OBC/PBC movement;
      (c) dimension/scaling: MST persistence across 610/987/1597, cloud box-dims,
          escape-based box-count slopes (resolution-honest brackets);
      (d) symmetry: the +- conjugate pair is exact (Galois/amphichiral, K020), NO intra-kappa
          PT-type reality (checked, not assumed), H^T = H exact.
  S3 verdict + the DATA-SUPPORTED CONJECTURES (never claims) -> b499_nonhermitian_dg.json.

BOUNDS: single process, deterministic seeds, ~3 min; grids/sizes logged in PARAMS below.
FIREWALL: spectral / dynamical mathematics only (K010 boundary); no scale, no Lambda;
nothing promotes; NOTHING to CLAIMS.md.
"""
import json
import os
import time

import numpy as np
import sympy as sp

np.seterr(over="ignore", invalid="ignore")
T0 = time.time()

PARAMS = {
    "lam_object": "exp(i pi/3)  (kappa = 2 + lam^2 = sqrt(3) e^{i pi/6})",
    "escape": {"R": 20.0, "Kmax_line": 30, "Kmax_2d": 60, "line_pts": 400,
               "fit_window": "1e-3 < f < 0.5 (B186 verbatim)"},
    "eplane_window": [-2.6, 3.2, -0.4, 1.4],
    "eplane_grid": [800, 300],
    "finegrid": [1920, 720],
    "slice_window": [-2.0, 2.0, -2.0, 2.0],
    "slice_grid": [500, 500],
    "depths_golden": {"d11": 233, "d13": 610, "d14": 987, "d15": 1597},
    "pseudospectra": {"sizes": [233, 610], "grid_233": [96, 44], "grid_610": [64, 30],
                      "invit_iters": 10, "svd_validation_pts": 150,
                      "eps_decades": [-1.0, -1.5, -2.0, -2.5, -3.0, -4.0, -5.0]},
    "seed": 0,
}

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

OUT = {"probe": "B499", "prereg": "CL-3D (docs/CLOSURE_CAMPAIGN_2026-07.md)", "params": PARAMS}

# =====================================================================
# S0 [exact]: the level set named (sympy; no floats in any claim here)
# =====================================================================
print("== S0 [exact]: the object's level set, named ==")
x, y, z, lamS, ES = sp.symbols("x y z lam E")
Tsym = (2*x*y - z, x, y)
Isym = lambda a, b, c: a**2 + b**2 + c**2 - 2*a*b*c - 1
chk("trace map T=(2xy-z,x,y) conserves I=x^2+y^2+z^2-2xyz-1 (B165 D0)",
    sp.expand(Isym(*Tsym) - Isym(x, y, z)) == 0)
seed_line = ((ES - lamS)/2, ES/2, sp.Integer(1))
chk("Schrodinger seed ((E-lam)/2, E/2, 1) lies on I=(lam/2)^2 for ALL E (B186 C0; kappa=2+lam^2)",
    sp.simplify(Isym(*seed_line) - (lamS/2)**2) == 0)

kappa = sp.sqrt(3)*sp.exp(sp.I*sp.pi/6)
zeta3 = sp.exp(2*sp.I*sp.pi/3)
lam_exact = sp.exp(sp.I*sp.pi/3)
EC = sp.expand_complex
chk("kappa - 2 = zeta_3 = e^{2 i pi/3} (K020 sec.5: kappa-2 = omega^2), |kappa-2| = 1",
    EC(kappa - 2 - zeta3) == 0 and EC(sp.Abs(kappa - 2) - 1) == 0)
chk("Phi_3(kappa-2) = (kappa-2)^2 + (kappa-2) + 1 = 0 -- the Eisenstein cyclotomic; the "
    "Q(sqrt-3) Galois Z/2 (sqrt-3 -> -sqrt-3, B285) swaps kappa <-> conj(kappa)",
    EC((kappa-2)**2 + (kappa-2) + 1) == 0
    and EC(sp.conjugate(kappa) - 2 - zeta3**2) == 0)
chk("the coupling lam = e^{i pi/3} (primitive 6th root of unity, |lam|=1) has lam^2 = kappa-2",
    EC(lam_exact**2 - (kappa - 2)) == 0)
# fixed points of T and the level surfaces they pin
J = sp.Matrix([[2*y, 2*x, -1], [1, 0, 0], [0, 1, 0]])
ev_void = sp.Matrix(J.subs([(x, 1), (y, 1)])).eigenvals()
phi = (1 + sp.sqrt(5))/2
chk("fixed points of T: (0,0,0) [I=-1, kappa=-2, the figure-eight point B67] and (1,1,1) "
    "[I=0, kappa=2, the void]; void Jacobian spectrum {phi^2, -1, phi^-2} (B124)",
    Isym(0, 0, 0) == -1 and Isym(1, 1, 1) == 0
    and all(any(sp.simplify(e - v) == 0 for e in ev_void) for v in [phi**2, -1, phi**-2]))
OUT["exact"] = {"kappa": "sqrt(3) e^{i pi/6}", "kappa_minus_2": "zeta_3 (primitive cube root of 1)",
                "coupling": "e^{i pi/3} (primitive 6th root of 1)",
                "conjugate_pair_is_galois_orbit": True, "void_jacobian": "{phi^2, -1, 1/phi^2}"}

# =====================================================================
# shared numerics (banked machinery: B186 survival/escape_rate + box_dim,
# B163/B165 MST, verbatim up to variable names)
# =====================================================================
LAM = complex(np.exp(1j*np.pi/3))

def Tmap(p):
    xx, yy, zz = p; return np.array([2*xx*yy - zz, xx, yy])

def survival(lmb, Egrid, Kmax=30, R=20.0):                      # B186 verbatim
    P = np.array([[(Ev - lmb)/2, Ev/2, 1.0] for Ev in Egrid], dtype=complex)
    alive = np.ones(len(P), bool); f = []
    for _ in range(Kmax):
        nrm = np.linalg.norm(P, axis=1); alive &= np.isfinite(nrm) & (nrm < R)
        f.append(alive.mean())
        P[~alive] = 0.0
        P = np.array([Tmap(p) for p in P])
    return np.array(f)

def escape_rate(f):                                             # B186 verbatim
    K = np.arange(len(f)); m = (f > 1e-3) & (f < 0.5)
    if m.sum() < 3: return 0.0
    return float(-np.polyfit(K[m], np.log(f[m]), 1)[0])

def metallic_word(n, m=1):
    sub = "a"*m + "b"; s = {-1: "b", 0: "a"}
    for k in range(1, n+1): s[k] = "".join(sub if c == "a" else "a" for c in s[k-1])
    return s[n]

def H_mat(word, lmb, periodic=True):
    L = len(word); V = np.array([lmb if c == "a" else 0.0 for c in word], dtype=complex)
    H = np.zeros((L, L), dtype=complex); np.fill_diagonal(H, V); i = np.arange(L-1)
    H[i, i+1] = 1; H[i+1, i] = 1
    if periodic: H[0, L-1] = 1; H[L-1, 0] = 1
    return H

def box_dim(ev, scales=2.0**np.arange(-2, -8, -1)):             # B186 verbatim
    P = np.c_[ev.real, ev.imag]; rng = np.ptp(P, axis=0); rng[rng == 0] = 1
    P = (P - P.min(0))/rng
    Ns = [len({(int(a//s), int(b//s)) for a, b in P}) for s in scales]
    return float(np.polyfit(np.log(1/scales), np.log(np.array(Ns, float)), 1)[0])

def mst_max_gap_over_diam(ev):                                  # B163/B165 verbatim
    P = np.c_[ev.real, ev.imag]; n = len(P)
    intree = np.zeros(n, bool); mind = np.full(n, np.inf); mind[0] = 0.0; edges = np.empty(n)
    for t_ in range(n):
        u = int(np.argmin(np.where(intree, np.inf, mind))); edges[t_] = mind[u]; intree[u] = True
        d = np.sqrt(((P - P[u])**2).sum(1)); upd = (~intree) & (d < mind); mind[upd] = d[upd]
    diam = np.hypot(ev.real.max()-ev.real.min(), ev.imag.max()-ev.imag.min())
    return float(edges[1:].max())/float(diam)

def iterate_kt(x, y, z, Kmax=60, R=20.0):
    """Vectorized escape-time of trace-map seeds (freeze-on-escape; L1 trap |x|+|y|+|z|<R)."""
    alive = np.ones(x.shape, bool); kt = np.full(x.shape, Kmax, dtype=int)
    for k in range(Kmax):
        nrm = np.abs(x) + np.abs(y) + np.abs(z)
        esc = alive & ~(np.isfinite(nrm) & (nrm < R))
        kt[esc] = k; alive &= ~esc
        x = np.where(alive, x, 0); y = np.where(alive, y, 0); z = np.where(alive, z, 0)
        x, y, z = 2*x*y - z, x, y
    return alive, kt

def kt_of_E(E, lmb, Kmax=60, R=20.0):
    return iterate_kt((E - lmb)/2, E/2*np.ones_like(E), np.ones_like(E), Kmax, R)

def gamma_from_kt(kt, Kmax):
    f = np.array([(kt >= K).mean() for K in range(Kmax + 1)])
    K = np.arange(Kmax + 1); m = (f > 1e-3) & (f < 0.5)
    if m.sum() < 3: return 0.0
    return float(-np.polyfit(K[m], np.log(f[m]), 1)[0])

def hausdorff(A, B):
    PA = np.c_[A.real, A.imag]; PB = np.c_[B.real, B.imag]
    d = np.sqrt(((PA[:, None, :] - PB[None, :, :])**2).sum(-1))
    return float(max(d.min(1).max(), d.min(0).max()))

# =====================================================================
# S1 [num]: CONTROLS (prereg: any failure => INVALID)
# =====================================================================
print("\n== S1 [num]: Hermitian controls (any failure => INVALID) ==")
reg = np.linspace(-4, 4, 400) + 0j
g_b186 = escape_rate(survival(3.0, reg))
g_v1   = escape_rate(survival(1.0, reg))
g_band = escape_rate(survival(0.0, reg))
chk("C1 banked-anchor reproduction: gamma(lam=3) = B186's early-window 0.51 (B451: asymptotic "
    "0.445; the ANCHOR locks the estimator)", abs(g_b186 - 0.51) < 0.05,
    x=f"gamma={g_b186:.4f} (banked 0.51)")
chk("C2 DG ground truth at the V=1 level set (kappa=3): exponential escape gamma>0; "
    "kappa=2 band calibrator gamma~0", g_v1 > 0.05 and g_band < 0.02,
    x=f"gamma(V=1)={g_v1:.4f}, gamma(band)={g_band:.4f}")

Ereal = np.linspace(-3, 4, 4001) + 0j
_, kt_band = kt_of_E(Ereal, 0.0 + 0j, Kmax=40)
frac_band = float((kt_band >= 40).mean())
chk("C3 K010 dictionary at kappa=2: non-escaping real set = the band [-2,2] "
    "(measure fraction of [-3,4] = 4/7)", abs(frac_band - 4/7) < 0.01,
    x=f"fraction={frac_band:.4f} vs 4/7={4/7:.4f}")

w11, w13, w14, w15 = (metallic_word(n) for n in (11, 13, 14, 15))
ev_c13 = np.linalg.eigvals(H_mat(w13, 1.0)); ev_b13 = np.linalg.eigvals(H_mat(w13, 0.0))
ev_c15 = np.linalg.eigvals(H_mat(w15, 1.0)); ev_b15 = np.linalg.eigvals(H_mat(w15, 0.0))
mst_c = [mst_max_gap_over_diam(ev_c13), mst_max_gap_over_diam(ev_c15)]
mst_b = [mst_max_gap_over_diam(ev_b13), mst_max_gap_over_diam(ev_b15)]
chk("C4 B165-method control: V=1 MST max-gap/diam persistent across 610->1597 and >> band -> 0",
    min(mst_c) > 0.10 and abs(mst_c[0] - mst_c[1]) < 0.03 and max(mst_b) < 0.02
    and min(mst_c) > 5*max(mst_b),
    x=f"V=1 gaps {[round(v,4) for v in mst_c]} vs band {[round(v,4) for v in mst_b]}")

d_c13, d_b13 = box_dim(ev_c13), box_dim(ev_b13)
chk("C5 box-dim (B186 C2, finite-depth effective): V=1 cloud < band at matched depth "
    "[HONEST CAVEAT: weakly separating at V=1 -- the strong controls are C2/C4]",
    d_c13 < d_b13 - 0.02, x=f"V=1 {d_c13:.3f} < band {d_b13:.3f}")

ev_c11 = np.linalg.eigvals(H_mat(w11, 1.0))
_, kt_ev_c = kt_of_E(ev_c11.astype(complex), 1.0 + 0j)
_, kt_gen_c = kt_of_E(Ereal, 1.0 + 0j)
med_ev_c, med_gen_c = float(np.median(kt_ev_c)), float(np.median(kt_gen_c))
chk("C6 spectrum = non-escaping set consistency (control): eigenvalue escape times >> generic "
    "(shadowing depth ~ log(1/spacing)/log(phi))", med_ev_c >= 12 and med_gen_c <= 9,
    x=f"median kt: eigenvalues {med_ev_c:.0f} vs generic line {med_gen_c:.0f}")

OUT["controls"] = {"gamma_lam3_anchor": round(g_b186, 4), "gamma_lam3_banked": 0.51,
                   "gamma_V1": round(g_v1, 4), "gamma_band": round(g_band, 4),
                   "band_nonescaping_fraction": round(frac_band, 4), "band_expected": round(4/7, 4),
                   "mst_V1_d13_d15": [round(v, 4) for v in mst_c],
                   "mst_band_d13_d15": [round(v, 4) for v in mst_b],
                   "boxdim_V1_d13": round(d_c13, 3), "boxdim_band_d13": round(d_b13, 3),
                   "kt_median_eigs_vs_generic_V1": [med_ev_c, med_gen_c]}
if not ok:
    print("\nCONTROLS FAILED => INVALID (prereg). Stopping.")
    import sys; sys.exit(1)

# =====================================================================
# S2a [num]: the object's level set -- complexified escape structure
# =====================================================================
print("\n== S2a [num]: escape structure on the object's level surface (kappa = sqrt3 e^{i pi/6}) ==")
re_g = np.linspace(-2.6, 3.2, 800); im_g = np.linspace(-0.4, 1.4, 300)
Egrid = re_g[None, :] + 1j*im_g[:, None]
alive2d, kt2d = kt_of_E(Egrid, LAM, Kmax=60)
g_obj2d = gamma_from_kt(kt2d, 60)
counts = [int((kt2d >= K).sum()) for K in range(0, 41, 4)]
chk("2D escape rate on the E-plane: exponential escape (the same horseshoe signature as the "
    "DG-proven control; band gives 0.000)", g_obj2d > 0.2,
    x=f"gamma_2D={g_obj2d:.4f}; survivors at K=0,4,...,40: {counts}")

_, kt_real = kt_of_E(np.linspace(-4, 4, 4001) + 0j, LAM, Kmax=40)
n_real = int((kt_real >= 40).sum())
chk("real section: EMPTY at resolution (the spectrum leaves the real axis; cloud has Im>0)",
    n_real == 0, x=f"survivors on 4001-pt real line at K=40: {n_real}")

ev_o11 = np.linalg.eigvals(H_mat(w11, LAM))
_, kt_ev_o = kt_of_E(ev_o11.copy(), LAM)
med_ev_o = float(np.median(kt_ev_o)); med_gen_o = float(np.median(kt2d))
chk("spectrum = non-escaping set consistency (object): eigenvalues sit deep "
    "(median kt ~ 16 = shadowing depth at spacing ~1e-3) vs generic ~5",
    med_ev_o >= 12 and med_gen_o <= 9,
    x=f"median kt: eigenvalues {med_ev_o:.0f} vs E-plane grid {med_gen_o:.0f}")

# symmetric x=y slice on the level surface: z^2 - 2x^2 z + (2x^2 - 1 - I0) = 0
I0 = (LAM/2)**2
re_s = np.linspace(-2, 2, 500); im_s = np.linspace(-2, 2, 500)
X = re_s[None, :] + 1j*im_s[:, None]
disc = np.sqrt((X**2)**2 - (2*X**2 - 1 - I0) + 0j)
slice_res = {}
for sgn, nm in [(+1, "z+"), (-1, "z-")]:
    Z = X**2 + sgn*disc
    _, kts = iterate_kt(X.copy(), X.copy(), Z, Kmax=40)
    gs = gamma_from_kt(kts, 40)
    slice_res[nm] = {"gamma": round(gs, 3), "survivors_K40": int((kts >= 40).sum())}
chk("symmetric x=y slice (both z-branches): exponential escape, no survivors at K=40 "
    "(thin/Cantor-like on the slice too)",
    all(v["gamma"] > 0.2 and v["survivors_K40"] == 0 for v in slice_res.values()),
    x=str(slice_res))

# the diagonal line x=y=z=w through both fixed points (each point on its OWN level)
W = re_s[None, :] + 1j*im_s[:, None]
aliveD, ktD = iterate_kt(W.copy(), W.copy(), W.copy(), Kmax=40)
roots_diag = np.roots([-2, 3, 0, -1 - I0])          # 3w^2 - 2w^3 - 1 = I0
_, kt_roots = iterate_kt(roots_diag.copy(), roots_diag.copy(), roots_diag.copy(), Kmax=60)
chk("diagonal line through the fixed points: bounded orbits exist on the line (near the "
    "elliptic fixed point (0,0,0), kappa~-2) BUT its 3 intersection points with the OBJECT's "
    "level all ESCAPE -- the diagonal meets this level only in the escaping set",
    aliveD.sum() > 0 and int(kt_roots.max()) < 20,
    x=f"line survivors {int(aliveD.sum())}/{aliveD.size}; intersection escape times {list(kt_roots)}")

# conjugate level = exact mirror (subsampled numerical check of the exact identity)
sub = Egrid[::7, ::11]
_, kt_conj = kt_of_E(np.conj(sub), np.conj(LAM), Kmax=60)
_, kt_here = kt_of_E(sub, LAM, Kmax=60)
chk("conjugate level kappa-bar: escape-time map is the exact mirror (Galois pair, one orbit)",
    np.array_equal(kt_conj, kt_here))

OUT["escape"] = {"gamma_2d_object": round(g_obj2d, 4), "survivor_counts_K0_40_step4": counts,
                 "real_section_survivors": n_real,
                 "kt_median_eigs_vs_generic": [med_ev_o, med_gen_o],
                 "slice_xy": slice_res,
                 "diagonal_line_survivors": int(aliveD.sum()),
                 "diagonal_cap_object_level_escape_times": [int(v) for v in kt_roots],
                 "conjugate_mirror_exact": True}

# =====================================================================
# S2b [num]: pseudospectra of the non-self-adjoint approximants
# =====================================================================
print("\n== S2b [num]: pseudospectra / non-normality vs the Hermitian control ==")
from scipy.linalg import schur, solve_triangular

def smin_field(H, Z, iters=10, seed=0):
    """sigma_min(z-H) on grid Z: complex Schur once, inverse iteration on the triangular factor."""
    Tt, _ = schur(H, output='complex')
    n = Tt.shape[0]; rng = np.random.default_rng(seed)
    out = np.empty(Z.size); Iden = np.eye(n, dtype=complex)
    for j, zz in enumerate(Z.ravel()):
        A = zz*Iden - Tt
        v = rng.standard_normal(n) + 1j*rng.standard_normal(n); v /= np.linalg.norm(v)
        s = 0.0
        for _ in range(iters):
            try:
                w_ = solve_triangular(A, v, lower=False, check_finite=False)
                u = solve_triangular(A, w_, lower=False, trans='C', check_finite=False)
            except Exception:
                s = 0.0; break
            nu = np.linalg.norm(u)
            if not np.isfinite(nu) or nu == 0: s = 0.0; break
            v = u/nu; s = 1/np.sqrt(nu)
        out[j] = s
    return out.reshape(Z.shape)

# object, n=233
H233 = H_mat(w11, LAM); ev233 = ev_o11
re_p = np.linspace(-2.6, 3.2, 96); im_p = np.linspace(-0.4, 1.4, 44)
Zp = re_p[None, :] + 1j*im_p[:, None]
S233 = smin_field(H233, Zp)
cell = (re_p[1]-re_p[0])*(im_p[1]-im_p[0])
# validation vs direct SVD on a subsample
rngv = np.random.default_rng(1)
idx = rngv.choice(Zp.size, 150, replace=False)
sv = np.array([np.linalg.svd(zz*np.eye(233) - H233, compute_uv=False)[-1]
               for zz in Zp.ravel()[idx]])
relerr = float(np.max(np.abs(S233.ravel()[idx] - sv)/sv))
chk("sigma_min estimator validated vs direct SVD (150-pt subsample, n=233)", relerr < 0.08,
    x=f"max rel err = {relerr:.4f}")

dist233 = np.abs(Zp.ravel()[:, None] - ev233[None, :]).min(1).reshape(Zp.shape)
amp233 = float(np.nanmax((dist233/np.maximum(S233, 1e-300))[dist233 > 1e-6]))
_, V233 = np.linalg.eig(H233); cond233 = float(np.linalg.cond(V233))
# Hermitian control, same machinery
H233c = H_mat(w11, 1.0); ev233c = np.linalg.eigvals(H233c)
re_pc = np.linspace(-2.8, 3.6, 96); im_pc = np.linspace(-0.9, 0.9, 44)
Zpc = re_pc[None, :] + 1j*im_pc[:, None]
S233c = smin_field(H233c, Zpc)
dist233c = np.abs(Zpc.ravel()[:, None] - ev233c[None, :]).min(1).reshape(Zpc.shape)
amp233c = float(np.nanmax((dist233c/np.maximum(S233c, 1e-300))[dist233c > 1e-6]))
chk("pseudospectral amplification max dist(z,Lambda)/sigma_min: Hermitian control ~ 1 (normal); "
    "object O(10), bounded by cond(V) (Bauer-Fike) -- non-normal but TAME, no pooling",
    amp233c < 1.2 and 1.05 < amp233 < 1.1*cond233,
    x=f"object {amp233:.2f} (cond(V)={cond233:.1f}) vs control {amp233c:.3f}")

# eps-decade areas (object n=233 and n=610; control n=233)
eps_list = [10.0**e for e in PARAMS["pseudospectra"]["eps_decades"]]
areas233 = [float((S233 < e).sum()*cell) for e in eps_list]
cellc = (re_pc[1]-re_pc[0])*(im_pc[1]-im_pc[0])
areas233c = [float((S233c < e).sum()*cellc) for e in eps_list]
H610 = H_mat(w13, LAM)
re_p6 = np.linspace(-2.6, 3.2, 64); im_p6 = np.linspace(-0.4, 1.4, 30)
Zp6 = re_p6[None, :] + 1j*im_p6[:, None]
S610 = smin_field(H610, Zp6)
cell6 = (re_p6[1]-re_p6[0])*(im_p6[1]-im_p6[0])
areas610 = [float((S610 < e).sum()*cell6) for e in eps_list]
ev610 = np.linalg.eigvals(H610)
dist610 = np.abs(Zp6.ravel()[:, None] - ev610[None, :]).min(1).reshape(Zp6.shape)
amp610 = float(np.nanmax((dist610/np.maximum(S610, 1e-300))[dist610 > 1e-6]))
_, V610 = np.linalg.eig(H610); cond610 = float(np.linalg.cond(V610))
# d_eff from the resolvable decades (eps in [1e-2, 1e-1]; below that: point regime)
le = np.log10(eps_list[:3]); la = np.log10(np.maximum(areas233[:3], 1e-12))
slope_eps = float(np.polyfit(le, la, 1)[0]); d_eff = 2 - slope_eps
print(f"   eps-areas (object n=233):  {[f'{a:.4f}' for a in areas233]}  at eps 1e-1..1e-5")
print(f"   eps-areas (object n=610):  {[f'{a:.4f}' for a in areas610]}")
print(f"   eps-areas (control n=233): {[f'{a:.4f}' for a in areas233c]}")
chk("eps-pseudospectral area scaling (resolvable decades eps in [1e-2,1e-1]): "
    "area ~ eps^s with d_eff = 2-s in [0.7, 1.5] -- a 1D-content set, NOT area-filling "
    "[HONEST CAVEAT: ~1.5 decades only; below eps~spacing the point regime takes over]",
    0.7 < d_eff < 1.5, x=f"slope={slope_eps:.3f}, d_eff={d_eff:.3f}")

# cond(V) growth + OBC/PBC movement
conds = {}
for n_ in (9, 10, 11, 12, 13):
    _, Vn = np.linalg.eig(H_mat(metallic_word(n_), LAM))
    conds[len(metallic_word(n_))] = float(np.linalg.cond(Vn))
sizes = np.array(sorted(conds)); cvals = np.array([conds[s] for s in sizes])
expo = float(np.polyfit(np.log(sizes), np.log(cvals), 1)[0])
chk("eigenvector condition numbers grow POLYNOMIALLY, cond(V) ~ n^alpha with alpha ~ 0.5 "
    "(NOT exponentially -- mild non-normality; Hermitian control has cond = 1 exactly)",
    0.2 < expo < 0.9 and cvals[-1] < 100,
    x=f"cond(V): {dict((int(k), round(v,1)) for k, v in conds.items())}, alpha={expo:.2f}")

evP = ev610; evO = np.linalg.eigvals(H_mat(w13, LAM, periodic=False))
diam_o = float(np.abs(evP[:, None] - evP[None, :]).max())
bc_obj = hausdorff(evP, evO)/diam_o
evPc = np.linalg.eigvals(H_mat(w13, 1.0, True)); evOc = np.linalg.eigvals(H_mat(w13, 1.0, False))
diam_c = float(evPc.real.max() - evPc.real.min())
bc_ctrl = hausdorff(evPc, evOc)/diam_c
chk("OBC vs PBC spectral movement (n=610): object ~ Hermitian control (NO Hatano-Nelson-type "
    "boundary catastrophe / spectral pooling)", bc_obj < 3*bc_ctrl and bc_obj < 0.1,
    x=f"object {bc_obj:.4f} vs control {bc_ctrl:.4f} (Hausdorff/diam)")

OUT["pseudospectra"] = {
    "smin_validation_max_relerr": round(relerr, 4),
    "amplification_max": {"object_233": round(amp233, 2), "object_610": round(amp610, 2),
                          "hermitian_control_233": round(amp233c, 3)},
    "condV": {str(int(k)): round(v, 2) for k, v in conds.items()},
    "condV_growth_exponent": round(expo, 3), "condV_610": round(cond610, 2),
    "eps_list": PARAMS["pseudospectra"]["eps_decades"],
    "eps_areas_object_233": [round(a, 4) for a in areas233],
    "eps_areas_object_610": [round(a, 4) for a in areas610],
    "eps_areas_control_233": [round(a, 4) for a in areas233c],
    "eps_area_slope": round(slope_eps, 3), "d_eff_from_eps_areas": round(d_eff, 3),
    "obc_pbc_hausdorff_over_diam": {"object": round(bc_obj, 4), "control": round(bc_ctrl, 4)}}

# =====================================================================
# S2c [num]: dimension / scaling of the non-escaping set
# =====================================================================
print("\n== S2c [num]: dimension & scaling (resolution-honest) ==")
ev_o13 = ev610
ev_o14 = np.linalg.eigvals(H_mat(w14, LAM))
ev_o15 = np.linalg.eigvals(H_mat(w15, LAM))
mst_o = [mst_max_gap_over_diam(e) for e in (ev_o13, ev_o14, ev_o15)]
chk("B165-method at the object's kappa: MST max-gap/diam PERSISTENT across 610/987/1597 and "
    ">> band -> totally-disconnected (Cantor-like) signature",
    min(mst_o) > 0.08 and max(mst_o) - min(mst_o) < 0.02 and min(mst_o) > 5*max(mst_b),
    x=f"object gaps {[round(v,4) for v in mst_o]} vs band {[round(v,4) for v in mst_b]}")

dims_cloud = [box_dim(e) for e in (ev_o13, ev_o14, ev_o15)]
print(f"   eigenvalue-cloud box-dims (610/987/1597): {[round(d,3) for d in dims_cloud]} "
      f"[finite-sample effective values]")

re_f = np.linspace(-2.6, 3.2, 1920); im_f = np.linspace(-0.4, 1.4, 720)
Ef = re_f[None, :] + 1j*im_f[:, None]
_, ktf = kt_of_E(Ef, LAM, Kmax=18)
slopes = {}
for K in (10, 12, 14, 16):
    mask = ktf >= K
    Ns = []
    for b in (2, 4, 8, 16, 32, 64):
        h, w_ = mask.shape
        M = mask[:h//b*b, :w_//b*b].reshape(h//b, b, w_//b, b).any(axis=(1, 3))
        Ns.append(int(M.sum()))
    sl = float(-np.polyfit(np.log([2, 4, 8, 16, 32, 64]), np.log(np.array(Ns, float)), 1)[0])
    slopes[K] = {"boxes": Ns, "slope": round(sl, 3)}
sl_seq = [slopes[K]["slope"] for K in (10, 12, 14, 16)]
chk("escape-based box-count of the K-survivor sets (1920x720 grid): slopes DECREASE "
    "monotonically toward ~1.0 as the survivor neighborhood tightens; survivor count decays "
    "exponentially -> ZERO-AREA set, box-dim bracket ~[1.0, 1.3] (upper estimates), NOT 2",
    all(sl_seq[i] > sl_seq[i+1] for i in range(3)) and 0.8 < sl_seq[-1] < 1.35,
    x=f"slopes K=10/12/14/16: {sl_seq}")

OUT["dimension"] = {"mst_object_d13_d14_d15": [round(v, 4) for v in mst_o],
                    "boxdim_cloud_object": [round(d, 3) for d in dims_cloud],
                    "escape_boxcount": {str(k): v for k, v in slopes.items()},
                    "bracket": "box-dim(non-escaping E-plane set) ~ 1.0-1.3 (resolution-limited "
                               "upper estimates); zero 2D Lebesgue measure (exponential escape)"}

# =====================================================================
# S2d [num+exact]: symmetry structure (check, don't assume)
# =====================================================================
print("\n== S2d: symmetry structure ==")
Hb = H_mat(w11, np.conj(LAM))
chk("conjugate pair EXACT: H(conj lam) = conj H(lam) entrywise => spec(kappa-bar) = conj "
    "spec(kappa) (the Galois/amphichiral Z/2 of K020/B285 acting on the spectrum)",
    np.array_equal(Hb, np.conj(H233)))
chk("H^T = H exact (the cocycle/operator is COMPLEX SYMMETRIC -- transpose-symmetric, "
    "not self-adjoint)", np.array_equal(H233, H233.T))
diam233 = float(np.abs(ev233[:, None] - ev233[None, :]).max())
pt_asym = hausdorff(ev233, np.conj(ev233))/diam233
chk("NO intra-kappa PT-type reality (checked, not assumed): the spectrum is NOT "
    "conjugation-symmetric (cloud lies in Im E > 0); the antiunitary symmetry acts only "
    "ACROSS the +- pair", pt_asym > 0.1 and float(ev233.imag.min()) > 0,
    x=f"Hausdorff(spec, conj spec)/diam = {pt_asym:.3f}; min Im = {ev233.imag.min():.3f}")
OUT["symmetry"] = {"conjugate_pair_exact": True, "complex_symmetric": True,
                   "pt_reality": False, "pt_asymmetry": round(pt_asym, 4),
                   "min_Im_spec_233": round(float(ev233.imag.min()), 4),
                   "max_Im_spec_233": round(float(ev233.imag.max()), 4)}

# =====================================================================
# S3: verdict + the DATA-SUPPORTED CONJECTURES (never claims)
# =====================================================================
no_pooling = (g_obj2d > 0.2 and sl_seq[-1] < 1.35 and amp233 < 1.1*cond233
              and bc_obj < 0.1 and min(mst_o) > 0.08)
verdict = "DATA-BANKED" if (ok and no_pooling) else "SURPRISE"
OUT["verdict"] = {
    "outcome": verdict,
    "enum": ["DATA-BANKED", "SURPRISE"],
    "no_pooling_no_positive_measure": bool(no_pooling),
    "conjecture_D1": (
        "DATA-SUPPORTED CONJECTURE (not a claim). Non-Hermitian Damanik-Gorodetski at the "
        "object's level: for kappa = sqrt(3) e^{+-i pi/6} (kappa-2 = zeta_3, coupling "
        "lam = e^{+-i pi/3}), the Fibonacci trace map T(x,y,z) = (2xy-z, x, y) restricted to "
        "the complex level surface I = (kappa-2)/4 is uniformly hyperbolic on its non-escaping "
        "set (a complex horseshoe in the Bedford-Smillie sense), the Schrodinger line "
        "((E-lam)/2, E/2, 1) meets its stable lamination in a compact, totally disconnected "
        "set Sigma of zero Lebesgue area in the E-plane with box dimension ~ 1, and Sigma is "
        "the spectrum of the non-self-adjoint metallic operator H = Delta + lam*chi_Fib "
        "(Hausdorff limit of the approximant spectra, boundary-condition independent)."),
    "conjecture_D2": (
        "DATA-SUPPORTED CONJECTURE (not a claim). Spectral-pseudospectral correspondence: the "
        "non-self-adjoint cocycle at the object's kappa is complex symmetric with only "
        "POLYNOMIALLY growing eigenvector condition numbers (cond(V) ~ n^0.5), so the "
        "eps-pseudospectra of the approximants converge to the eps-neighborhood of Sigma with "
        "amplification bounded polynomially in volume -- no spectral pooling, no "
        "Hatano-Nelson-type boundary sensitivity; DG-type spectral data survive "
        "non-self-adjointness at this kappa."),
}
print(f"\nVERDICT: {verdict}" + ("" if verdict == "DATA-BANKED" else "  << H1 DISCIPLINE: stop, owner present"))
print("Conjecture D1 (non-Hermitian DG at the object's kappa): complex horseshoe on the level")
print("surface; spectrum = zero-area, totally disconnected, box-dim ~1 Cantor-like set in C.")
print("Conjecture D2 (spectral-pseudospectral correspondence): complex-symmetric cocycle, cond(V)")
print("~ n^0.5, amplification bounded, no pooling, no boundary catastrophe.")

OUT["runtime_seconds"] = round(time.time() - T0, 1)
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "b499_nonhermitian_dg.json"), "w") as fh:
    json.dump(OUT, fh, indent=1)
print(f"\n[banked b499_nonhermitian_dg.json; runtime {OUT['runtime_seconds']}s]")
print("FIREWALL: mathematics only; nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
