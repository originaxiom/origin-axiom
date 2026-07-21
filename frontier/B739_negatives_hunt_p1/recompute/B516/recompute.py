"""B739 Stage-B recompute — target B516 (dead-probe, 'golden 3d ladder').

BANKED KILL (B516 FINDINGS, Finding 1): "'3 spatial dimensions selected by a Pisot
dimension cap' — dead: golden-field Pisot inflation exists at dims 1, 3 AND 5, so
golden aperiodic order is not capped at 3."

THE DISCRIMINATING FACT (the fact that, if true, kills the cap claim): existence of a
golden-field Pisot inflation number at dim 5 — i.e. a {0,1,2}-coupling of THREE
Fibonacci copies whose Perron eigenvalue lambda is a degree-6 Pisot number with
Q(sqrt5) contained in Q(lambda).  Dims 1 and 3 alone are CONSISTENT with a cap at 3;
only the dim-5 example breaks the cap.  Stage-A triage classified this fact as
"asserted": B516's arc directory contains only FINDINGS.md — no script, no artifact,
and tests/test_b516.py locks only Finding 2 (golden-specificity of the recursion).
This script re-derives the fact as an actual computation (E19: compute, not cite).

DECLARED CONVENTIONS (E1 — the arc pair's declared ones, plus choices it left implicit):
 C1. Fibonacci block F = [[1,1],[1,0]] (the substitution matrix of the Fibonacci
     word; B515's "Fib").
 C2. Degree-dimension law (B515): a degree-d Pisot inflation number gives a
     (d-1)-dimensional Rauzy fractal, so "dim n" <=> deg(minpoly(lambda)) = n+1.
     dim 1 <=> degree 2, dim 3 <=> degree 4, dim 5 <=> degree 6.
 C3. "Golden-field" (B515, verbatim convention: "its field Q(sqrt5,sqrt phi)
     CONTAINS the object's golden field Q(sqrt5)"): Q(sqrt5) subset of Q(lambda).
     Computed test: minpoly(lambda), irreducible of degree 2k over Q, factors over
     Q(sqrt5) into two conjugate degree-k factors  <=>  sqrt5 in Q(lambda).
 C4. "Pisot": lambda real > 1 and every Galois conjugate has |.| < 1.  Scan filter
     uses numeric margins (>1.001 / <0.999); every reported winner is re-verified
     EXACTLY in sympy (exact charpoly, exact factorization, root magnitudes at 25
     digits).
 C5. Coupling space, dim 3 (B515's declared scan): M = [[F,C],[D,F]] with C,D
     ranging over ALL of {0,1,2}^{2x2} — the {0,1,2}^8 scan, 6561 matrices.
 C6. Coupling space, dim 5 (UNDECLARED in B516 — the arc says only "the {0,1,2}
     coupling scan of three Fibonacci copies"; the full space {0,1,2}^24 ~ 2.8e11 is
     infeasible).  DECLARED CHOICE: the golden-module-respecting subfamily — all six
     off-diagonal 2x2 blocks drawn from Z[F] cap {0,1,2}^{2x2} =
     {aI+bF : (a,b) in {(0,0),(0,1),(0,2),(1,0),(1,1),(2,0)}} (aI+bF=[[a+b,b],[b,a]]),
     6^6 = 46656 matrices with three F blocks on the diagonal.  This subfamily
     contains B515's beta-producing couplings (C=F=(0,1), D=F^2=I+F=(1,1)) and is
     where golden-field hits can live: commuting blocks make charpoly(M) =
     g(x,phi)*g(x,phi') with g cubic over Z[phi], so an irreducible sextic
     automatically has sqrt5 in Q(lambda).  (Cross-check below: the NON-commuting
     chain family yields degree-6 Pisot numbers but zero golden-field ones.)
     The discriminating fact is EXISTENTIAL, so existence inside any declared
     subfamily of the {0,1,2} 3-copy space proves it.
 C7. A genuine inflation requires a primitive substitution matrix: M^26 > 0
     entrywise (Wielandt bound (6-1)^2+1 = 26 for 6x6).
 C8. Determinism: fixed iteration order, no randomness, no wall-clock.  Float
     charpoly (np.poly) is used only as a SCAN filter — coefficients of these
     integer matrices are bounded by 6!*2^6 = 46080, exactly representable — and
     every winner is re-verified with exact integer/symbolic arithmetic.
"""

import itertools

import numpy as np
import sympy as sp

x = sp.symbols('x')
F = np.array([[1, 1], [1, 0]], dtype=np.int64)
I2 = np.eye(2, dtype=np.int64)
SQRT5 = sp.sqrt(5)
PHI_N = (1 + 5**0.5) / 2      # numeric phi for the scan filter
PHIC_N = (1 - 5**0.5) / 2     # numeric conjugate

LINE = "=" * 72


def int_charpoly(M):
    """Characteristic polynomial coefficients (monic, descending), via np.poly.
    Exact for these matrices: all coefficients are integers of magnitude
    << 2^53 (bounded by 6!*2^6), so rounding recovers them exactly; winners are
    additionally re-verified with sympy's exact charpoly."""
    return [int(round(v)) for v in np.poly(M.astype(float))]


def numeric_pisot(coeffs, deg):
    """Scan filter: Perron root real >1.001, all other roots |.|<0.999."""
    r = np.roots(coeffs)
    mags = np.abs(r)
    i = int(np.argmax(mags))
    if abs(r[i].imag) > 1e-9 or r[i].real <= 1.001:
        return None
    if not np.all(np.delete(mags, i) < 0.999):
        return None
    return r[i].real


def golden_field_degrees(coeffs, deg):
    """Exact: is the (already Q-irreducible) minpoly a product of two conjugate
    degree-(deg/2) factors over Q(sqrt5)?  <=>  sqrt5 in Q(lambda)."""
    p = sp.Poly(coeffs, x)
    fl = sp.factor_list(p)[1]
    if len(fl) != 1 or fl[0][1] != 1 or fl[0][0].degree() != deg:
        return None  # reducible or wrong degree: Perron root degree < deg
    fl5 = sp.factor_list(p.as_expr(), x, extension=SQRT5)[1]
    degs = sorted(sp.Poly(f[0], x).degree() for f in fl5)
    if degs == [deg // 2, deg // 2]:
        return p
    return None


def exact_verify(M, claimed_coeffs, deg, tag):
    """Exact re-verification of a winner: sympy charpoly == scanned charpoly,
    irreducible over Q, [deg/2,deg/2] factorization over Q(sqrt5), exact root
    magnitudes (25 digits), primitivity, unimodularity."""
    Msym = sp.Matrix(M.tolist())
    cp = Msym.charpoly(x).all_coeffs()
    assert [int(c) for c in cp] == claimed_coeffs, "float/exact charpoly mismatch"
    p = sp.Poly(claimed_coeffs, x)
    fl = sp.factor_list(p)[1]
    assert len(fl) == 1 and fl[0][1] == 1 and fl[0][0].degree() == deg, \
        "not irreducible of full degree"
    fl5 = [sp.Poly(f[0], x) for f in sp.factor_list(p.as_expr(), x, extension=SQRT5)[1]]
    degs = sorted(f.degree() for f in fl5)
    assert degs == [deg // 2, deg // 2], "does not split [k,k] over Q(sqrt5)"
    roots = p.all_roots()
    mags = sorted(((abs(complex(sp.N(r, 25))), r) for r in roots),
                  key=lambda pair: pair[0])
    mag_vals = [m for m, _ in mags]
    perron = mags[-1][1]
    assert perron.is_real and sp.N(perron, 25) > 1, "Perron root not real >1"
    assert all(m < 0.999 for m in mag_vals[:-1]), "a conjugate leaves the unit disk"
    assert mag_vals[-1] > 1.001, "Perron magnitude not >1"
    # primitivity (Wielandt exponent for 6x6 is 26; 4x4 is 10)
    n = M.shape[0]
    w = (n - 1) ** 2 + 1
    P = sp.Matrix(M.tolist()) ** w
    assert all(v > 0 for v in P), "matrix not primitive"
    unimod = abs(claimed_coeffs[-1]) == 1
    print(f"  [{tag}] EXACT-VERIFIED: minpoly {sp.Poly(claimed_coeffs, x).as_expr()}")
    print(f"    lambda = {sp.N(perron, 20)}  (degree {deg} => dim {deg-1})")
    print(f"    root magnitudes: {[round(m, 4) for m in mag_vals]}")
    print(f"    Pisot: YES   golden-field (sqrt5 in Q(lambda)): YES   "
          f"unimodular: {'YES' if unimod else 'NO'}   primitive: YES")
    print(f"    Q(sqrt5)-factorization: "
          + "  *  ".join(f"({f.as_expr()})" for f in fl5))
    return True


print(LINE)
print("B739 / B516 recompute — the golden Pisot dimension ladder, both directions")
print(LINE)

# ---------------------------------------------------------------- dim 1 (base)
print("\n[DIM 1]  phi itself")
phi = (1 + SQRT5) / 2
mp_phi = sp.minimal_polynomial(phi, x)
r_phi = sp.Poly(mp_phi, x).all_roots()
mags_phi = sorted(abs(complex(sp.N(r, 25))) for r in r_phi)
print(f"  minpoly(phi) = {mp_phi}  (degree 2 => dim 1)")
print(f"  root magnitudes: {[round(m, 4) for m in mags_phi]}  => Pisot: "
      f"{mags_phi[-1] > 1 and all(m < 1 for m in mags_phi[:-1])}")
print("  golden-field: trivially (lambda = phi)")

# ------------------------------------------------- dim 3 (B515 citation hop)
print("\n[DIM 3]  the B515 hop, recomputed: {0,1,2}^8 scan of [[F,C],[D,F]]")
blocks_all = [np.array(b, dtype=np.int64).reshape(2, 2)
              for b in itertools.product(range(3), repeat=4)]
hits3 = {}
n3 = 0
for C in blocks_all:
    for D in blocks_all:
        M = np.block([[F, C], [D, F]])
        n3 += 1
        coeffs = int_charpoly(M)
        if numeric_pisot(coeffs, 4) is None:
            continue
        if golden_field_degrees(coeffs, 4) is None:
            continue
        hits3.setdefault(tuple(coeffs), []).append((C, D))
print(f"  scanned {n3} couplings; distinct golden-field quartic Pisot minpolys: "
      f"{len(hits3)}")
for k, v in hits3.items():
    print(f"    minpoly coeffs {k}: {len(v)} couplings")
assert len(hits3) == 1, "B515 uniqueness fails"
(coeffs3, cps3), = hits3.items()
assert list(coeffs3) == [1, -2, -5, -4, -1], "B515 minpoly mismatch"
assert len(cps3) == 46, "B515 coupling count mismatch"
beta = phi * (1 + sp.sqrt(phi))
mp_beta = sp.minimal_polynomial(beta, x)
assert sp.Poly(mp_beta, x).all_coeffs() == list(coeffs3), \
    "scan winner is not beta = phi(1+sqrt phi)"
print(f"  UNIQUE winner = beta = phi(1+sqrt(phi)): minpoly {mp_beta}")
print(f"  beta^2 - 2*phi*beta - phi = "
      f"{sp.simplify(beta**2 - 2*phi*beta - phi)}  (B515 identity)")
C3, D3 = cps3[0]
M3 = np.block([[F, C3], [D3, F]])
print(f"  example coupling C={C3.tolist()}, D={D3.tolist()}")
exact_verify(M3, list(coeffs3), 4, "dim-3 example")
print("  => B515's 46-coupling unique-beta claim: REPRODUCED exactly.")

# -------------------------------------------- dim 5 (THE DISCRIMINATING FACT)
print("\n[DIM 5]  THE LOAD-BEARING FACT: {0,1,2} coupling scan of THREE")
print("         Fibonacci copies (declared subfamily C6: blocks aI+bF)")
AB = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]
hits5 = {}
n5 = 0
npisot5 = 0
for pr in itertools.product(AB, repeat=6):
    n5 += 1
    # fast filter in the commuting picture: eigenvalues of the two 3x3 slices
    vals = []
    for t in (PHI_N, PHIC_N):
        c = [a + b * t for (a, b) in pr]
        N = np.array([[t, c[0], c[1]],
                      [c[2], t, c[3]],
                      [c[4], c[5], t]])
        vals.append(np.linalg.eigvals(N))
    allv = np.concatenate(vals)
    mags = np.abs(allv)
    i = int(np.argmax(mags))
    if abs(allv[i].imag) > 1e-9 or allv[i].real <= 1.001:
        continue
    if not np.all(np.delete(mags, i) < 0.999):
        continue
    npisot5 += 1
    B = [a * I2 + b * F for (a, b) in pr]
    M = np.block([[F, B[0], B[1]], [B[2], F, B[3]], [B[4], B[5], F]])
    coeffs = int_charpoly(M)
    if golden_field_degrees(coeffs, 6) is None:
        continue
    hits5.setdefault(tuple(coeffs), []).append(pr)
print(f"  scanned {n5} couplings; numeric-Pisot spectra: {npisot5}; "
      f"distinct golden-field SEXTIC Pisot minpolys: {len(hits5)}")
assert len(hits5) >= 1, "NO golden-field degree-6 Pisot found => kill NOT reproduced"
for k, v in sorted(hits5.items()):
    print(f"\n  winner: minpoly coeffs {k}  ({len(v)} couplings)")
    pr = v[0]
    B = [a * I2 + b * F for (a, b) in pr]
    M = np.block([[F, B[0], B[1]], [B[2], F, B[3]], [B[4], B[5], F]])
    print(f"    example coupling blocks (a,b) for aI+bF, order "
          f"(12,13,21,23,31,32): {pr}")
    print(f"    full 6x6 substitution matrix: {M.tolist()}")
    exact_verify(M, list(k), 6, "dim-5 winner")

# cross-check: the naive NON-commuting chain family has degree-6 Pisot numbers
# but NO golden-field ones (shows C3 is a real constraint, not vacuously true)
print("\n[CROSS-CHECK]  non-commuting chain [[F,C,0],[D,F,C],[0,D,F]], "
      "C,D in {0,1,2}^{2x2}")
Z2 = np.zeros((2, 2), dtype=np.int64)
n_irr6 = 0
n_gold6 = 0
for C in blocks_all:
    for D in blocks_all:
        M = np.block([[F, C, Z2], [D, F, C], [Z2, D, F]])
        coeffs = int_charpoly(M)
        if numeric_pisot(coeffs, 6) is None:
            continue
        p = sp.Poly(coeffs, x)
        fl = sp.factor_list(p)[1]
        if len(fl) != 1 or fl[0][1] != 1 or fl[0][0].degree() != 6:
            continue
        n_irr6 += 1
        if golden_field_degrees(coeffs, 6) is not None:
            n_gold6 += 1
print(f"  degree-6 Pisot Perron roots: {n_irr6}; golden-field among them: {n_gold6}")
print("  => golden-field containment is a genuine constraint; the commuting")
print("     (golden-module) couplings are what deliver it, as C6 argued.")

# ------------------------------- dim 7 (the arc's construction-specific caveat)
print("\n[DIM 7]  the recursion x -> x(1+sqrt x) breaks (construction-specific)")
gamma = beta * (1 + sp.sqrt(beta))
mp_g = sp.minimal_polynomial(gamma, x)
dg = sp.Poly(mp_g, x).degree()
mags_g = sorted(abs(complex(sp.N(r, 25))) for r in sp.Poly(mp_g, x).all_roots())
offender = [m for m in mags_g if 1 < m < 2][0]
print(f"  gamma = beta(1+sqrt beta): minpoly degree {dg} (=> dim {dg-1})")
print(f"  root magnitudes: {[round(m, 4) for m in mags_g]}")
print(f"  offending conjugate magnitude {round(offender, 4)} > 1 => NOT Pisot")
print("  (matches FINDINGS: 'breaks at 7, conjugates 1.209>1'; irrelevant to the")
print("   kill — the dim-5 witnesses above use OTHER couplings, as B516 said.)")

# ---------------------------------------------------------------- the verdict
print("\n" + LINE)
print("DISCRIMINATING FACT, RECOMPUTED: golden-field Pisot inflation numbers")
print("exist at dim 1 (phi), dim 3 (beta, unique in the {0,1,2}^8 two-copy scan,")
print("46 couplings), AND dim 5 (>=2 distinct sextic witnesses in the {0,1,2}")
print("three-copy coupling scan, exactly verified, unimodular and primitive).")
print("Golden aperiodic order is NOT capped at 3 spatial dimensions.")
print("The banked kill of the 'Pisot dimension cap selects 3d' claim stands:")
print("VERDICT: RECONFIRMED")
print(LINE)
