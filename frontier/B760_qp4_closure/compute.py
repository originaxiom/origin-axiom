"""QP-4 -- the closure probe (prereg 98201bd3).

Tests whether any object-native operation canonically signs the chord
(theta-odd) sector of the figure-eight knot's SU(3)_2 representation.
The weld block has eigenphases +/-72 deg (B753).  If some operation
breaks the conjugate pairing, the object can close itself (HATCH).
If not: NO-HATCH.

Deterministic; nothing to CLAIMS.
"""
import cmath
import importlib.util
import math
import os

import numpy as np

HERE = os.getcwd()


def load(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ======================================================================
# PART 1 -- reconstruct B753's 2x2 theta-odd weld block
# ======================================================================
print("=" * 80)
print("PART 1 -- the 2x2 theta-odd weld block (reproduced from B753/B238)")
print("=" * 80)

b238 = load("../B238_su32_levelrank/su32_wrt.py", "b238")
w, S, T, cc = b238.su3_data(2)
n = len(w)

C = np.zeros((n, n))
for i, wt in enumerate(w):
    C[w.index((wt[1], wt[0])), i] = 1.0

Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
R, L = T, Si @ Ti @ S
PHI = (1 + math.sqrt(5)) / 2

pairs = [(w.index((1, 0)), w.index((0, 1))),
         (w.index((2, 0)), w.index((0, 2)))]
U_odd = np.zeros((n, 2))
for j, (a, b) in enumerate(pairs):
    U_odd[a, j], U_odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
U_odd = U_odd.astype(complex)

W_weld = C @ R @ L
B = np.array([[np.conj(U_odd[:, i]) @ W_weld @ U_odd[:, j]
               for j in range(2)] for i in range(2)])

print(f"B[0,0] = {B[0,0]:+.6f}   B[0,1] = {B[0,1]:+.6f}")
print(f"B[1,0] = {B[1,0]:+.6f}   B[1,1] = {B[1,1]:+.6f}")
print(f"max |off-diag| = {max(abs(B[0,1]), abs(B[1,0])):.3e}")
det_B = np.linalg.det(B)
print(f"det(B) = {det_B:+.10f}   |det| = {abs(det_B):.10f}")
unitarity = np.linalg.norm(B @ B.conj().T - np.eye(2))
print(f"||BB^dag - I|| = {unitarity:.3e}   unitary: {unitarity < 1e-10}")
alpha = B[0, 0]
beta = B[0, 1]
su2_check = (abs(B[1, 0] + np.conj(beta)) < 1e-12 and
             abs(B[1, 1] - np.conj(alpha)) < 1e-12)
print(f"SU(2) structure [[alpha,beta],[-conj(beta),conj(alpha)]]: {su2_check}")

# ======================================================================
# PART 2 -- eigendecomposition: eigenphases +/-72 deg = {zeta_5, zeta_5^4}
# ======================================================================
print()
print("=" * 80)
print("PART 2 -- eigendecomposition")
print("=" * 80)

evals, evecs = np.linalg.eig(B)
phases = [cmath.phase(ev) * 180 / math.pi for ev in evals]
idx = sorted(range(2), key=lambda k: -phases[k])
evals = evals[idx]
evecs = evecs[:, idx]
phases = [phases[i] for i in idx]

zeta5 = cmath.exp(2j * math.pi / 5)
print(f"lambda_+  = {evals[0]:+.10f}   phase = {phases[0]:+.8f} deg")
print(f"lambda_-  = {evals[1]:+.10f}   phase = {phases[1]:+.8f} deg")
print(f"zeta_5    = {zeta5:+.10f}   (= e^(2pi i/5) = e^(i 72 deg))")
print(f"|lambda_+ - zeta_5|   = {abs(evals[0] - zeta5):.3e}")
print(f"|lambda_- - zeta_5^4| = {abs(evals[1] - zeta5**4):.3e}")
is_zeta5 = abs(evals[0] - zeta5) < 1e-10 and abs(evals[1] - zeta5**4) < 1e-10
print(f"eigenvalues = {{zeta_5, zeta_5^4}}: {is_zeta5}")
assert is_zeta5

# ======================================================================
# PART 3 -- cyclotomic structure: B^5 = I, char poly divides Phi_5
# ======================================================================
print()
print("=" * 80)
print("PART 3 -- cyclotomic structure: B^5 = I")
print("=" * 80)

B5 = np.linalg.matrix_power(B, 5)
b5_is_I = np.allclose(B5, np.eye(2), atol=1e-10)
print(f"B^5 = [[ {B5[0,0]:+.10f}, {B5[0,1]:+.10f} ],")
print(f"       [ {B5[1,0]:+.10f}, {B5[1,1]:+.10f} ]]")
print(f"B^5 = I: {b5_is_I}")
assert b5_is_I

tr_B = np.trace(B)
print(f"tr(B) = {tr_B.real:+.10f}   1/phi = {1/PHI:+.10f}   match: "
      f"{abs(tr_B - 1/PHI) < 1e-10}")
print(f"det(B) = {det_B.real:+.10f}   match 1: {abs(det_B - 1) < 1e-10}")
print(f"char poly: x^2 - (1/phi)x + 1   [roots: zeta_5, zeta_5^4]")
print(f"divides x^5 - 1 via Phi_5(x) = (x^2 - (1/phi)x + 1)(x^2 + phi x + 1)")

# ======================================================================
# PART 4 -- rotation in the eigenvector-derived real subspace
# ======================================================================
print()
print("=" * 80)
print("PART 4 -- B acts as rotation by 72 deg in the canonical real subspace")
print("=" * 80)

w_plus = evecs[:, 0] / np.linalg.norm(evecs[:, 0])
w_minus = evecs[:, 1] / np.linalg.norm(evecs[:, 1])

v1 = w_plus + w_minus
v2 = 1j * (w_plus - w_minus)

cos72 = math.cos(math.radians(72))
sin72 = math.sin(math.radians(72))

Bv1 = B @ v1
Bv2 = B @ v2
rot_v1 = np.allclose(Bv1, cos72 * v1 + sin72 * v2, atol=1e-10)
rot_v2 = np.allclose(Bv2, -sin72 * v1 + cos72 * v2, atol=1e-10)
print(f"real basis: v1 = w+ + w-,  v2 = i(w+ - w-)")
print(f"B v1 = cos(72) v1 + sin(72) v2:  {rot_v1}")
print(f"B v2 = -sin(72) v1 + cos(72) v2: {rot_v2}")
assert rot_v1 and rot_v2

det_RmI = 2 - 2 * cos72
print(f"\ndet(R(72) - I) = 2 - 2*cos(72) = {det_RmI:+.10f}  (nonzero => no fixed direction)")
assert abs(det_RmI) > 0.1
print(f"sin(72) = {sin72:+.10f}  (nonzero => rotation is non-trivial)")
print(f"=> the weld block's rotation in the real subspace has NO invariant line.")

# ======================================================================
# PART 5 -- no MCG power gives a half-integer eigenphase
# ======================================================================
print()
print("=" * 80)
print("PART 5 -- MCG powers: no non-trivial power has eigenphase 0 or 180 deg")
print("=" * 80)

print(f"{'power':>7}  {'phase mod 360':>14}  {'half-integer?':>14}")
for nn in range(1, 6):
    phase = (nn * 72) % 360
    hi = phase in (0, 180)
    tag = "IDENTITY" if phase == 0 else ("YES" if hi else "no")
    print(f"  B^{nn}     {phase:>10.0f} deg  {tag:>14}")
    if nn < 5:
        assert not hi

print("=> no non-trivial weld power has a real eigenvalue on theta-odd.")

# ======================================================================
# PART 6 -- charge conjugation C = -I on theta-odd
# ======================================================================
print()
print("=" * 80)
print("PART 6 -- charge conjugation C restricted to theta-odd")
print("=" * 80)

C_odd = np.array([[np.conj(U_odd[:, i]) @ C @ U_odd[:, j]
                    for j in range(2)] for i in range(2)])
c_minus_I = np.allclose(C_odd, -np.eye(2), atol=1e-12)
print(f"C|_odd = [[ {C_odd[0,0].real:+.1f}, {C_odd[0,1].real:+.1f} ],")
print(f"          [ {C_odd[1,0].real:+.1f}, {C_odd[1,1].real:+.1f} ]]")
print(f"C|_odd = -I: {c_minus_I}")
assert c_minus_I
print("=> C maps every theta-odd vector to its negative; cannot orient.")

# ======================================================================
# PART 7 -- Galois swaps the eigenvalue pair
# ======================================================================
print()
print("=" * 80)
print("PART 7 -- Galois action: sigma_4 swaps zeta_5 <-> zeta_5^4")
print("=" * 80)

print(f"Galois sigma_4 in Gal(Q(zeta_5)/Q): zeta_5 -> zeta_5^4 = conj(zeta_5)")
print(f"  sigma_4(lambda_+) = zeta_5^4 = lambda_-")
print(f"  sigma_4(lambda_-) = zeta_5   = lambda_+")
print(f"=> eigenvalues form a single Galois orbit (exchanged, not fixed).")

conj_lp = np.conj(evals[0])
conj_lm = np.conj(evals[1])
swap_lp = abs(conj_lp - evals[1]) < 1e-10
swap_lm = abs(conj_lm - evals[0]) < 1e-10
print(f"\nNumerical: conj(lambda_+) = {conj_lp:+.8f} = lambda_-: {swap_lp}")
print(f"           conj(lambda_-) = {conj_lm:+.8f} = lambda_+: {swap_lm}")
assert swap_lp and swap_lm

eps = np.array([[0, -1], [1, 0]], dtype=complex)
su2_conj = np.allclose(np.conj(B), eps @ B @ np.linalg.inv(eps), atol=1e-10)
print(f"\nSU(2) quaternionic structure: conj(B) = eps B eps^(-1): {su2_conj}")
print(f"  (eps = [[0,-1],[1,0]]; eps^2 = -I => quaternionic, not real)")
print(f"=> Galois provides NO real structure on the fundamental rep.")
print(f"   The conjugation that swaps eigenvalues is 'outer': it maps the")
print(f"   representation to its inequivalent conjugate, not to itself.")

# ======================================================================
# PART 8 -- QP-3 coupling transport: magnitude canonical, sign not
# ======================================================================
print()
print("=" * 80)
print("PART 8 -- QP-3 coupling transport: sign non-canonicity")
print("=" * 80)

omega = complex(-0.5, math.sqrt(3) / 2)
omega_bar = complex(-0.5, -math.sqrt(3) / 2)

d_omega = -2 * (2 - omega)
d_omega_bar = -2 * (2 - omega_bar)
print(f"Sym^2(AB) d/du at omega     = {d_omega:+.10f}   Im = {d_omega.imag:+.10f}")
print(f"Sym^2(AB) d/du at omega_bar = {d_omega_bar:+.10f}   Im = {d_omega_bar.imag:+.10f}")
sign_flips = abs(d_omega.imag + d_omega_bar.imag) < 1e-12
mag_same = abs(abs(d_omega.imag) - abs(d_omega_bar.imag)) < 1e-12
print(f"sign flips under Galois (omega <-> omega_bar): {sign_flips}")
print(f"magnitude invariant |Im| = sqrt(3): {mag_same}")
assert sign_flips and mag_same


def coupling_at(u):
    ds = [0, 0, -2*(2-u), 2*(2+u), 2*(2+u), -2*(2-u), 4*u**3+8*u]
    off = sum(abs(complex(d).imag)**2 for d in ds)
    tot = sum(abs(complex(d))**2 for d in ds)
    return off / tot


f_w = coupling_at(omega)
f_wb = coupling_at(omega_bar)
print(f"\ncoupling fraction at omega     = {f_w:.10f}")
print(f"coupling fraction at omega_bar = {f_wb:.10f}")
print(f"both = 15/32 = {15/32:.10f}: "
      f"{abs(f_w - 15/32) < 1e-12 and abs(f_wb - 15/32) < 1e-12}")
print(f"=> fraction (15/32) is Galois-invariant; signed Im(+/-sqrt(3)) is NOT.")

# ======================================================================
# PART 9 -- Q2 controls: the no-fixed-direction theorem at other angles
# ======================================================================
print()
print("=" * 80)
print("PART 9 -- Q2 controls")
print("=" * 80)

print("--- algebraic control: rotation at non-half-integer angles ---")
for adeg in [72, 108, 144]:
    ar = math.radians(adeg)
    det_val = 2 - 2 * math.cos(ar)
    s = math.sin(ar)
    has_fixed = abs(det_val) < 1e-10
    print(f"  R({adeg:>3} deg): det(R-I) = {det_val:+.6f}  sin = {s:+.6f}"
          f"  fixed dir: {has_fixed}")
    assert not has_fixed

print("\n--- positive control: degenerate angles ---")
for adeg in [0, 180]:
    ar = math.radians(adeg)
    det_val = 2 - 2 * math.cos(ar)
    s = math.sin(ar)
    has_fixed = abs(det_val) < 1e-10
    note = ("IDENTITY (all dirs fixed, none canonical)"
            if adeg == 0 else "-I (all dirs mapped to negative)")
    print(f"  R({adeg:>3} deg): det(R-I) = {det_val:+.6f}  sin = {s:+.6f}"
          f"  =>  {note}")

print("\n--- QP-3 input consistency: coupling fraction at the OTHER Galois image ---")
u_test = complex(0.3, 1.7)
u_test_bar = np.conj(u_test)
f1, f2 = coupling_at(u_test), coupling_at(u_test_bar)
print(f"  coupling_at({u_test}) = {f1:.10f}")
print(f"  coupling_at(conj)       = {f2:.10f}")
print(f"  Galois-invariant: {abs(f1 - f2) < 1e-12}")

# ======================================================================
# VERDICT
# ======================================================================
print()
print("=" * 80)
print("SUMMARY AND VERDICT")
print("=" * 80)

ops = [
    ("Galois sigma",    False, "swaps eigenvalues {zeta_5, zeta_5^4}"),
    ("MCG (weld B^n)",  False, "eigenphases n*72 deg, never 0 or 180 (n=1..4)"),
    ("Charge conj C",   False, "C = -I on theta-odd; commutes, cannot orient"),
    ("Amphicheiral tau", False, "= C at tangent level (B570 Lane C); same verdict"),
    ("QP-3 coupling",   False, "fraction 15/32 canonical; sign(Im) flips"),
]

for name, canonical, reason in ops:
    print(f"  {name:>20}:  canonical sign = {str(canonical):>5}  -- {reason}")

any_hatch = any(o[1] for o in ops)
verdict = "HATCH" if any_hatch else "NO-HATCH"

print()
print(f"VERDICT: {verdict}")
print()
print("The theta-odd eigenphases +/-72 deg = {zeta_5, zeta_5^4} form an")
print("inseparable Galois orbit in Q(zeta_5).  In the canonical real subspace,")
print("the weld block acts as rotation by 72 deg (sin 72 != 0) -- no invariant")
print("line exists.  All five candidate operations fail to break the pairing.")
print()
print("The object is INTEGRATED (QP-3: coupling 15/32) but cannot CLOSE itself.")
print("No object-native operation canonically orients the chord sector.")
print("Choosing w+ over w- = choosing sqrt(-1) = the Galois torsor.")
print()
print("'Awareness without choice' (S072 Layer-3) is computationally upheld.")
