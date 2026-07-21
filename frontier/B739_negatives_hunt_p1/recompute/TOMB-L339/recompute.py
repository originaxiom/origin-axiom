#!/usr/bin/env python3
"""B739 Stage-B recompute -- TOMB-L339 (TOMBSTONES.md:339; B565 cell R5; the L38 Higgs-scale
do-or-die kill).

BANKED DISCRIMINATING FACT (to be re-derived, not cited):
  (1) the PVI time has C* weight 0 (dimensionless modulus, exact symbolic);
  (2) the only C*-fixed Hitchin-base point is h=0 (nilpotent);
  (3) base dilation is NOT isomonodromic (banked: drift 3e5 vs invariant 1.7e-10);
  (4) hbar-compensation is exact.
  => no intrinsic scale on the Hitchin/Higgs side (kill_form: no-landing-site).

The B565 dir contains NO committed reproducer for these numbers (RESULTS.md restates them
without a script), so this recompute re-derives the fact from the arc chain's own declared
conventions (B164/B169, the arcs cell R5 was preregistered on), with every undeclared
convention chosen and DECLARED here (E1):

DECLARED CONVENTIONS (E1):
  C1. C* action = the Hitchin dilation lam.(E,Phi) = (E, lam*Phi); "weight k" of a coordinate
      x means x -> lam^k x. The action does not move the base curve or its punctures.
  C2. Fuchsian/parabolic realization per B164/B169: rank-2 traceless residues A_1,A_2,A_3 at
      z = 0, 1, s on P^1, A_inf = -(A_1+A_2+A_3); residues seeded exactly as B169
      (numpy default_rng(1), same draw order); Schlesinger flow dA_i/ds = [A_3,A_i]/(s-t_i),
      RK4, h = 0.01, s: 2 -> 3 (B169's declared integrator and window).
  C3. PVI time = the cross-ratio modulus of the 4 singular points (Jimbo--Miwa normalization
      (0, t, 1, inf)).
  C4. Base dilation realized at the residue level A_i -> lam*A_i (= Phi -> lam*Phi on the
      Fuchsian side). The banked record does not declare its lam; chosen here: lam = e
      (the unit-time dilation flow, matching Schlesinger's unit window s:2->3), plus an
      infinitesimal control lam = 1.01 to show the breakage is not a large-lam artifact.
  C5. Monodromy: fundamental solution transported by RK4 along piecewise paths from basepoint
      z0 = -0.7 - 1.3j (below the real axis); per pole p: straight segment z0 -> p - i*r,
      CCW circle of radius r = 0.3, reversed segment (via matrix inverse). Drift metric =
      max abs change over {tr M_1, tr M_2, tr M_3, tr(M_2 M_1)} (loops whose isotopy class
      is manifestly untouched by the pole moving 2 -> 3 along the real axis with all
      attachments in the lower half-plane), plus B169's local-invariant metric
      {det A_i, tr A_inf, det A_inf}.
  C6. hbar enters as the connection d/dz - (1/hbar) A(z) (the non-abelian-Hodge hbar-
      connection); compensation means (lam*A, lam*hbar) is the SAME connection as (A, hbar).

Deterministic: fixed seed rng(1) (B169's), fixed step counts, no wall-clock, no network.
Gate 5: pure isomonodromy/character-variety mathematics; no SM quantities; nothing to CLAIMS.
"""
import numpy as np
import sympy as sp

ok = True
def chk(name, cond, extra=""):
    global ok
    ok = ok and bool(cond)
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {extra}" if extra else ""))

# =====================================================================================
# PART 1 [exact] -- the PVI time has C* weight 0
# =====================================================================================
print("== PART 1 [exact]: the PVI time has C* weight 0 (dimensionless modulus) ==")
# (a) Under the Hitchin C* action (C1), Phi -> lam*Phi moves NO point of the base curve:
#     the punctures (0, t, 1, inf) -- hence the PVI time t -- are untouched. Weight 0 holds
#     definitionally for the Hitchin action; the substantive symbolic content is (b):
# (b) the PVI time is the CROSS-RATIO of the 4 singular points, and the cross-ratio is
#     exactly invariant under any dilation z -> lam*z of the plane (the scale subgroup
#     of PGL(2)) -- so no rescaling of the geometry can be read off from t.
a, b, c, d, lam = sp.symbols('a b c d lam', nonzero=True)
def cross_ratio(t1, t2, t3, t4):
    return ((t1 - t3) * (t2 - t4)) / ((t2 - t3) * (t1 - t4))
cr_diff = sp.simplify(cross_ratio(lam*a, lam*b, lam*c, lam*d) - cross_ratio(a, b, c, d))
chk("cross-ratio(lam*t_i) - cross-ratio(t_i) == 0 exactly (symbolic)", cr_diff == 0,
    extra=f"residual = {cr_diff}")
# weight readout: t -> lam^0 * t
chk("PVI time t = cross-ratio => C* weight 0 exactly (t -> lam^0 t)", cr_diff == 0,
    extra="the flow 'time' is a dimensionless modulus, not a length")

# =====================================================================================
# PART 2 [exact] -- the weight table; the only C*-fixed base point is h=0 (nilpotent)
# =====================================================================================
print("\n== PART 2 [exact]: base weights all 2; only C*-fixed base point is h=0 (nilpotent) ==")
# Rank-2 (SL(2)) Hitchin base = the quadratic differential q = det Phi.  General identity:
m11, m12, m21 = sp.symbols('m11 m12 m21')
M = sp.Matrix([[m11, m12], [m21, -m11]])           # traceless 2x2 (sl_2 Higgs field fiber)
det_scale = sp.simplify((lam*M).det() - lam**2 * M.det())
chk("det(lam*Phi) == lam^2 * det(Phi) identically (any traceless 2x2 fiber)", det_scale == 0,
    extra="every Hitchin-base coordinate has C* weight exactly 2")
# Concretely on the (0,4) Fuchsian Higgs field of B164/B169: Phi(z) = A1/z + A2/(z-1) + A3/(z-s):
z, s_sym = sp.symbols('z s')
A_syms = [sp.Matrix(2, 2, sp.symbols(f'x{i}_11 x{i}_12 x{i}_21 x{i}_22')) for i in (1, 2, 3)]
A_syms = [sp.Matrix([[X[0, 0], X[0, 1]], [X[1, 0], -X[0, 0]]]) for X in A_syms]  # traceless
Phi = A_syms[0]/z + A_syms[1]/(z-1) + A_syms[2]/(z-s_sym)
q = sp.together(Phi.det())
num, den = sp.fraction(q)
numP = sp.Poly(sp.expand(num), z)
coeff_weights = []
for cf in numP.all_coeffs():
    # substitute every entry x -> lam*x and compare
    subs = {sym: lam*sym for X in A_syms for sym in X.free_symbols if sym != s_sym}
    scaled = sp.expand(cf.subs(subs, simultaneous=True))
    w_ok = sp.simplify(scaled - lam**2 * cf) == 0
    coeff_weights.append(w_ok)
chk(f"ALL {len(coeff_weights)} numerator coefficients of q(z)=det Phi have weight exactly 2",
    all(coeff_weights),
    extra="weight table: base coordinates -> 2, PVI time -> 0 (Part 1), hbar -> 1 (Part 4)")
# Only fixed point: lam^2 * q = q for all lam  <=>  q = 0.
c_sym = sp.symbols('c_sym')
fixed_solutions = sp.solve(sp.Eq(lam**2 * c_sym, c_sym), c_sym)   # over generic lam
chk("lam^2*c = c for generic lam forces c = 0 (the ONLY C*-fixed base point is q=0)",
    fixed_solutions == [0], extra=f"solve returns {fixed_solutions}")
# q=0 <=> h nilpotent: Cayley-Hamilton for traceless 2x2: M^2 = -det(M)*I.
CH = sp.simplify(M*M - (-M.det())*sp.eye(2))
chk("Cayley-Hamilton (traceless 2x2): Phi^2 = -det(Phi)*I, so det Phi=0 => Phi^2=0 (NILPOTENT)",
    CH == sp.zeros(2, 2),
    extra="the unique C*-fixed base point h=0 is the nilpotent cone -- no nonzero fixed structure can set a scale")

# =====================================================================================
# PART 3 [num] -- Schlesinger IS isomonodromic; base dilation is NOT
# =====================================================================================
print("\n== PART 3 [num]: Schlesinger flow preserves monodromy; base dilation does NOT ==")
rng = np.random.default_rng(1)                      # B169's declared seed and draw order
def rand_traceless():
    a_ = rng.normal()+1j*rng.normal(); b_ = rng.normal()+1j*rng.normal(); c_ = rng.normal()+1j*rng.normal()
    return np.array([[a_, b_], [c_, -a_]], dtype=complex)
t_poles = [0.0+0j, 1.0+0j]                          # t1=0, t2=1 fixed; t3=s moves; t4=inf
A0 = [rand_traceless(), rand_traceless(), rand_traceless()]

def comm(X, Y): return X@Y - Y@X
def schlesinger_rhs(A, s):
    A1, A2, A3 = A
    d1 = comm(A3, A1)/(s - t_poles[0]); d2 = comm(A3, A2)/(s - t_poles[1]); d3 = -(d1 + d2)
    return [d1, d2, d3]
def rk4_flow_step(A, s, h):
    k1 = schlesinger_rhs(A, s)
    k2 = schlesinger_rhs([A[i]+0.5*h*k1[i] for i in range(3)], s+0.5*h)
    k3 = schlesinger_rhs([A[i]+0.5*h*k2[i] for i in range(3)], s+0.5*h)
    k4 = schlesinger_rhs([A[i]+h*k3[i] for i in range(3)], s+h)
    return [A[i] + (h/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i]) for i in range(3)]

def local_invariants(A):                             # B169's exact invariant list
    Ainf = -(A[0]+A[1]+A[2])
    return [np.linalg.det(X) for X in A] + [np.trace(Ainf), np.linalg.det(Ainf)]

# ---- global monodromy by path-ordered RK4 transport (C5) ----
Z0 = -0.7 - 1.3j
RAD = 0.3
N_SEG, N_CIRC = 15000, 30000
def field(A, poles, zz):
    return A[0]/(zz-poles[0]) + A[1]/(zz-poles[1]) + A[2]/(zz-poles[2])
def transport(A, poles, path, N):
    """RK4 for dY/du = z'(u) A(z(u)) Y along path(u), u in [0,1]; returns the 2x2 transport."""
    Y = np.eye(2, dtype=complex)
    h = 1.0/N
    zfun, dzfun = path
    def rhs(u, Y_):
        return dzfun(u) * (field(A, poles, zfun(u)) @ Y_)
    u = 0.0
    for _ in range(N):
        k1 = rhs(u, Y)
        k2 = rhs(u+0.5*h, Y+0.5*h*k1)
        k3 = rhs(u+0.5*h, Y+0.5*h*k2)
        k4 = rhs(u+h, Y+h*k3)
        Y = Y + (h/6)*(k1+2*k2+2*k3+k4)
        u += h
    return Y
def loop_matrix(A, poles, p):
    """monodromy around pole p, based at Z0: segment down-attach + CCW circle."""
    a_pt = p - 1j*RAD
    seg = (lambda u: Z0 + u*(a_pt - Z0), lambda u: (a_pt - Z0))
    T_go = transport(A, poles, seg, N_SEG)
    th0 = -np.pi/2
    circ = (lambda u: p + RAD*np.exp(1j*(th0 + 2*np.pi*u)),
            lambda u: RAD*2j*np.pi*np.exp(1j*(th0 + 2*np.pi*u)))
    T_c = transport(A, poles, circ, N_CIRC)
    return np.linalg.inv(T_go) @ T_c @ T_go
def monodromy_traces(A, s):
    poles = [t_poles[0], t_poles[1], s]
    Ms = [loop_matrix(A, poles, p) for p in poles]
    dets = [abs(np.linalg.det(Mk) - 1) for Mk in Ms]     # integrator sanity: det M_k = 1 exactly
    tr = [np.trace(Ms[0]), np.trace(Ms[1]), np.trace(Ms[2]), np.trace(Ms[1] @ Ms[0])]
    return tr, max(dets)

print("   computing baseline monodromy at s=2 ...")
tr_base, detg0 = monodromy_traces(A0, 2.0+0j)
inv_base = local_invariants(A0)
print(f"   baseline traces (s=2): trM1={tr_base[0]:.6g}  trM2={tr_base[1]:.6g}  "
      f"trM3={tr_base[2]:.6g}  trM2M1={tr_base[3]:.6g}")
chk("integrator sanity: |det M_k - 1| small at baseline (traceless residues => det=1)",
    detg0 < 1e-7, extra=f"max |det M_k - 1| = {detg0:.2e}")

# ---- (a) the Schlesinger flow s: 2 -> 3 (B169 conventions) ----
A = [X.copy() for X in A0]
s = 2.0+0j; h = 0.01
for _ in range(100):
    A = rk4_flow_step(A, s, h); s += h
moved = max(float(np.max(np.abs(A[i]-A0[i]))) for i in range(3))
inv_end = local_invariants(A)
drift_local = max(abs(x-y) for x, y in zip(inv_base, inv_end))
print("   computing monodromy after Schlesinger flow (s=3) ...")
tr_schl, detg1 = monodromy_traces(A, 3.0+0j)
drift_schl = max(abs(x-y) for x, y in zip(tr_base, tr_schl))
rel_schl = drift_schl / max(abs(x) for x in tr_base)
chk("the residues genuinely MOVE along the flow (non-vacuity)", moved > 0.1,
    extra=f"max |A_i(3)-A_i(2)| = {moved:.3f}")
chk("Schlesinger preserves B169's local conjugacy invariants (det A_i, tr/det A_inf)",
    drift_local < 1e-6, extra=f"local-invariant drift = {drift_local:.2e}  (banked-class: 1.7e-10; B169: 4.25e-10)")
chk("Schlesinger preserves the GLOBAL monodromy traces (isomonodromic)",
    rel_schl < 1e-5, extra=f"trace drift = {drift_schl:.2e} abs, {rel_schl:.2e} rel")

# ---- (b) base dilation A -> lam*A (the C* action, C4): lam = e ----
LAM = float(np.e)
A_dil = [LAM*X for X in A0]
print(f"   computing monodromy after base dilation lam = e = {LAM:.6f} ...")
tr_dil, _ = monodromy_traces(A_dil, 2.0+0j)
drift_dil = max(abs(x-y) for x, y in zip(tr_base, tr_dil))
inv_dil = local_invariants(A_dil)
drift_dil_local = max(abs(x-y) for x, y in zip(inv_base, inv_dil))
chk("base dilation is NOT isomonodromic: monodromy traces change grossly",
    drift_dil > 1e3 * max(drift_schl, 1e-300),
    extra=f"dilation trace drift = {drift_dil:.3e}  vs Schlesinger {drift_schl:.2e}  "
          f"(ratio {drift_dil/max(drift_schl,1e-300):.2e})")
chk("dilation also breaks the local exponents (det A_i -> e^2 det A_i)",
    drift_dil_local > 1.0, extra=f"local-invariant change = {drift_dil_local:.3e}")

# ---- (c) infinitesimal control: lam = 1.01 (breakage is not a large-lam artifact) ----
LAM_SMALL = 1.01
A_dil2 = [LAM_SMALL*X for X in A0]
print(f"   computing monodromy after base dilation lam = {LAM_SMALL} (control) ...")
tr_dil2, _ = monodromy_traces(A_dil2, 2.0+0j)
drift_dil2 = max(abs(x-y) for x, y in zip(tr_base, tr_dil2))
chk("even a 1% dilation breaks isomonodromy far above integrator noise (control)",
    drift_dil2 > 1e3 * max(drift_schl, 1e-300),
    extra=f"lam=1.01 trace drift = {drift_dil2:.3e}  (>> Schlesinger {drift_schl:.2e})")

# =====================================================================================
# PART 4 [exact] -- hbar-compensation is exact
# =====================================================================================
print("\n== PART 4 [exact]: hbar-compensation exact -- the dilation is absorbed by the EXTERNAL hbar ==")
hb = sp.symbols('hbar', nonzero=True)
comp = sp.simplify((lam*M)/(lam*hb) - M/hb)          # the hbar-connection d - (1/hbar) Phi
chk("(lam*Phi)/(lam*hbar) == Phi/hbar identically => the connection (hence ALL monodromy) is unchanged",
    comp == sp.zeros(2, 2),
    extra="the C* dilation acts on the quantization parameter hbar (weight 1), not on any internal scale")
# floating-point echo of the same identity on the actual residues:
comp_num = max(float(np.max(np.abs((LAM*A0[i])/LAM - A0[i]))) for i in range(3))
chk("numerical echo: (e*A_i)/e - A_i = 0 to machine precision", comp_num < 1e-14,
    extra=f"max residual = {comp_num:.2e}")

# =====================================================================================
# VERDICT
# =====================================================================================
print("\n== VERDICT (recomputed, not cited) ==")
print("  weight table: PVI time -> weight 0 (exact); ALL Hitchin-base coordinates -> weight 2")
print("  (exact); hbar -> weight 1 (external). Only C*-fixed base point: q=0, i.e. h nilpotent")
print("  (Cayley-Hamilton, exact). Base dilation is NOT isomonodromic (it grossly changes the")
print("  monodromy while Schlesinger preserves it), and is EXACTLY absorbed by hbar -> lam*hbar.")
print("  Every landing site for an intrinsic dimensionful scale on the Hitchin/Higgs side is")
print("  closed: weight-0 data is dimensionless, weight-2 data has no nonzero C*-fixed value,")
print("  and the one weight-1 parameter (hbar) is external. The banked kill is UPHELD.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
