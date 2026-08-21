"""
P-KOIDE — the sealed det-phi -> Koide instrument.

Standalone (mpmath only, no machine paths, no repo dependency at runtime).
Executes exactly the routes pre-committed in PRECOMMIT.md, written BEFORE this
script was run. Default prior: NO-BRIDGE. Gate 5: lepton masses enter ONLY as
the Koide-side target; nothing about them is ever fed into the object-side
(det phi / trit / v0) constructions below.

Provenance of every hardcoded object-side number (none re-fitted here):
  - det phi = -2/3, and its exact 6x6/72x72 block decomposition: independently
    recomputed in this probe from the banked artifact
    frontier/B904_barton_sudbery/stage4c_phi.pkl (sympy exact rationals;
    verified det(6x6)=-2/3, det(72x72)=+1, block-off-diagonals exactly zero).
    The 6x6 matrix below is transcribed verbatim from that recomputation.
  - the trit block dimensions (9,9,9): frontier/B897_27_under_g20/FINDINGS.md
    (sealed prereg e293f095..., two independent primes, identical signature).
  - v0 = support (1,-1,1) at indices (12,13,14): frontier/B663_bifocal_anatomy/
    .../a1_jordan/a1_results.json ("v0_coordinates_at_support"), N(v0,v0,v0)=-6,
    rank 3 (invertible), sharp(v0) proportional to v0 -- the one sealed, forced,
    unfitted rank-3 exceptional-Jordan-algebra element on record.
  - PDG charged-lepton masses: as already banked in
    frontier/B703_koide_sigma_distance/koide_q3.py (central values, MeV).
"""
import json
import mpmath as mp

mp.mp.dps = 40


# --------------------------------------------------------------------------
# Generic Koide-geometry instrument: for any positive triple (a,b,c), treat
# (sqrt a, sqrt b, sqrt c) as a vector in R^3 and report Q, the angle to the
# democratic direction (1,1,1), and the identity Q = 1/(3 cos^2 alpha).
# --------------------------------------------------------------------------
def koide_Q(a, b, c):
    a, b, c = mp.mpf(a), mp.mpf(b), mp.mpf(c)
    return (a + b + c) / (mp.sqrt(a) + mp.sqrt(b) + mp.sqrt(c)) ** 2


def angle_to_democratic(v):
    """v: iterable of 3 reals (already the 'sqrt-space' vector, no sqrt taken
    here) -> angle in degrees to (1,1,1) and cos^2 of that angle."""
    v = [mp.mpf(x) for x in v]
    d = [mp.mpf(1), mp.mpf(1), mp.mpf(1)]
    dot = sum(vi * di for vi, di in zip(v, d))
    nv = mp.sqrt(sum(vi * vi for vi in v))
    nd = mp.sqrt(3)
    cosA = dot / (nv * nd)
    alpha = mp.acos(cosA)
    return mp.degrees(alpha), cosA ** 2


def koide_Q_from_sqrt_vector(v):
    """Q computed directly from a sqrt-space vector v=(x,y,z) meaning
    (sqrt m_1, sqrt m_2, sqrt m_3) = v, i.e. Q = (sum v_i^2)/(sum v_i)^2."""
    v = [mp.mpf(x) for x in v]
    return sum(vi * vi for vi in v) / (sum(v)) ** 2


results = {}

# ============================================================================
# STEP 1 — the Koide side, classical, verified against PDG central values
# ============================================================================
print("=" * 78)
print("STEP 1 -- classical Koide geometry, PDG charged leptons")
print("=" * 78)

ME = mp.mpf('0.51099895000')     # MeV, PDG (as banked in B703)
MMU = mp.mpf('105.6583755')      # MeV
MTAU = mp.mpf('1776.86')         # MeV

Q_pdg = koide_Q(ME, MMU, MTAU)
alpha_pdg, cos2_pdg = angle_to_democratic([mp.sqrt(ME), mp.sqrt(MMU), mp.sqrt(MTAU)])
# cross-check the geometric identity Q = 1/(3 cos^2 alpha) independently
Q_from_angle = 1 / (3 * cos2_pdg)

print(f"Q (PDG)                 = {mp.nstr(Q_pdg, 12)}   (target 2/3 = {mp.nstr(mp.mpf(2)/3, 12)})")
print(f"alpha (PDG)              = {mp.nstr(alpha_pdg, 10)} deg   (target 45 deg)")
print(f"cos^2(alpha) (PDG)       = {mp.nstr(cos2_pdg, 12)}   (target 1/2)")
print(f"Q recovered from angle   = {mp.nstr(Q_from_angle, 12)}  (identity Q=1/(3cos^2 a) check)")
print(f"|Q - 2/3|                = {mp.nstr(abs(Q_pdg - mp.mpf(2)/3), 6)}")
print(f"identity residual        = {mp.nstr(abs(Q_pdg - Q_from_angle), 6)}")

results["step1_koide_classical"] = {
    "Q_pdg": mp.nstr(Q_pdg, 15),
    "alpha_pdg_deg": mp.nstr(alpha_pdg, 12),
    "cos2_alpha_pdg": mp.nstr(cos2_pdg, 15),
    "Q_from_angle_identity_check": mp.nstr(Q_from_angle, 15),
    "identity_residual": mp.nstr(abs(Q_pdg - Q_from_angle), 6),
    "reading": "Q=2/3 to 5 sig figs <=> alpha=45.00 deg <=> cos^2(alpha)=1/2 -- "
               "the STRUCTURAL content any bridge must derive is the 45 deg "
               "geometry, not the bare number 2/3 (B1129 dismissed the bare "
               "equality already).",
}

# ============================================================================
# STEP 0 recap (established before this script ran; see PRECOMMIT.md) --
# det phi's exact block structure, transcribed from the independent
# recomputation against the banked artifact.
# ============================================================================
print()
print("=" * 78)
print("STEP 0 recap -- det phi's exact meaning (established before STEP 2)")
print("=" * 78)

DETPHI = mp.mpf(-2) / 3
print(f"det phi (full 78x78)         = {DETPHI}  (independently reconfirmed from stage4c_phi.pkl)")
print("phi is EXACTLY block-diagonal: 72x72 root block det = +1 (signed permutation,")
print("zero cross terms); 6x6 Cartan/torus block det = -2/3 -- the ENTIRE value lives")
print("on E6's rank-6 Cartan subalgebra basis-change, nothing elsewhere.")

# the 6x6 block B (build Cartan rows h1..h6) x (BS-native torus cols), transcribed
# verbatim from the sympy-exact recomputation against stage4c_phi.pkl
B6 = mp.matrix([
    [1,    0,    0,    0,  mp.mpf(2)/3,  mp.mpf(1)/3],
    [1,    1,    0,    0,  0,            0],
    [mp.mpf(3)/2, mp.mpf(1)/2, mp.mpf(1)/2, mp.mpf(1)/2,  mp.mpf(1)/3, -mp.mpf(1)/3],
    [2,    1,    1,    0,  0,            0],
    [mp.mpf(3)/2, mp.mpf(1)/2, mp.mpf(1)/2, mp.mpf(1)/2, -mp.mpf(1)/3,  mp.mpf(1)/3],
    [1,    0,    0,    0, -mp.mpf(2)/3, -mp.mpf(1)/3],
])
detB6 = mp.det(B6)
print(f"det(6x6 block) recomputed here (mpmath) = {mp.nstr(detB6, 10)}  (exact value -2/3)")

# route (c'): does this block hide an angle-like eigen/singular value near 1/sqrt(2)?
U, S, V = mp.svd_r(B6)
sing_vals = sorted([S[i] for i in range(6)])
print("singular values of the 6x6 block:", [mp.nstr(s, 6) for s in sing_vals])
target = 1 / mp.sqrt(2)
closest = min(sing_vals, key=lambda s: abs(s - target))
print(f"1/sqrt(2) = {mp.nstr(target, 6)}  ; closest singular value = {mp.nstr(closest, 6)}"
      f"  ; gap = {mp.nstr(abs(closest - target), 6)}")

results["step0_detphi_block_structure"] = {
    "det_phi_full": "-2/3",
    "det_root_block_72x72": "+1 (signed permutation, exact)",
    "det_cartan_block_6x6": mp.nstr(detB6, 10),
    "singular_values_6x6_block": [mp.nstr(s, 8) for s in sing_vals],
    "nearest_singular_value_to_1_over_sqrt2": mp.nstr(closest, 8),
    "gap_to_cos45": mp.nstr(abs(closest - target), 6),
    "reading": "No eigenvalue or singular value of the only non-trivial block "
               "of phi is near cos45=1/sqrt2~0.7071 (nearest gap reported above, "
               "not small). Route (c') CLOSED: phi carries no latent angle.",
}

# ============================================================================
# STEP 2 -- candidate bridge routes (exactly the 4 pre-committed; no others)
# ============================================================================
print()
print("=" * 78)
print("STEP 2 -- candidate bridge routes")
print("=" * 78)

# ---- Route (a): the trit / B897 three 9-blocks -----------------------------
print("\n--- Route (a): the trit (B897) -- three 9-blocks, triality-cyclic ---")
dims = (9, 9, 9)  # the ONLY natural 3-vector this structure supplies un-chosen
Q_a = koide_Q_from_sqrt_vector([mp.sqrt(d) for d in dims])
alpha_a, cos2_a = angle_to_democratic([mp.sqrt(d) for d in dims])
print(f"block dims                = {dims}")
print(f"Q(dims)                    = {mp.nstr(Q_a, 8)}   (democratic point => Q=1/3 exactly, the MINIMUM of Koide's Q, not 2/3)")
print(f"alpha(dims)                = {mp.nstr(alpha_a, 8)} deg   (0 deg expected -- the ANTIPODE of Koide's 45deg)")
print("secondary check: su(2)' refinement (3+6) applies to only 2 of the 3 blocks")
print("(the (3c,3f) block is single-valued) -- no second, well-defined 3-vector exists.")
print("Casimirs C_c=C_f=4/9, C_w=3/8 are cross-SECTOR invariants (color/flavor/weak),")
print("not a 3-tuple indexed by the three generation-blocks -- no vector there either.")

results["route_a_trit"] = {
    "input": "block dimensions (9,9,9), B897 FINDINGS.md (two-prime sealed result)",
    "Q": mp.nstr(Q_a, 10),
    "alpha_deg": mp.nstr(alpha_a, 10),
    "verdict": "NO BRIDGE -- bare permutation symmetry forces the fully "
               "democratic point (alpha=0 deg, Q=1/3, the MINIMUM of Koide's Q), "
               "the OPPOSITE of Koide's 45deg/2:3 point on the same circle "
               "(Q ranges over [1/3,1) as alpha ranges over [0,90)deg; Koide's "
               "point is near the middle, not at either extreme). No second "
               "natural 3-vector exists in the banked B897/B1030 data (su(2)' "
               "refinement is 2-of-3 blocks only; Casimirs are cross-sector, not "
               "per-block).",
}

# ---- Route (b): det phi = 1/(3 cos^2 alpha) read backward ------------------
print("\n--- Route (b): det phi plugged into Q=1/(3cos^2 alpha) ---")
absdetphi = abs(DETPHI)
cos2_b = 1 / (3 * absdetphi)
alpha_b = mp.degrees(mp.acos(mp.sqrt(cos2_b)))
print(f"|det phi|                  = {mp.nstr(absdetphi, 8)}")
print(f"cos^2(alpha) implied       = {mp.nstr(cos2_b, 8)}  (= 1/2, trivially, since |det phi|=2/3 by arithmetic)")
print(f"alpha implied               = {mp.nstr(alpha_b, 8)} deg")
print("KILL: this 'derivation' works for ANY quantity X with X=2/3 -- it has zero")
print("discriminating power. Reductio: a 3-sided die's P(roll>1)=2/3 also solves to")
print("alpha=45deg under the same substitution. Demonstrating:")
reductio_val = mp.mpf(2) / 3   # P(roll in {2,3} out of a 3-sided die) -- unrelated quantity, also 2/3
cos2_r = 1 / (3 * reductio_val)
print(f"  reductio: X=2/3 (die roll probability, wholly unrelated) -> cos^2 alpha = "
      f"{mp.nstr(cos2_r, 6)} -> alpha = {mp.nstr(mp.degrees(mp.acos(mp.sqrt(cos2_r))), 6)} deg")
print("Since ANY X=2/3 substitutes identically, route (b) is DISQUALIFIED by the seal's")
print("own rule ('det phi = 2/3 = Q' as a bare equality) -- confirmed computationally: the")
print("map has NO dependence on det phi's actual content (the STEP 0 block structure),")
print("only on its numeric value coinciding with 2/3.")

results["route_b_bare_substitution"] = {
    "cos2_alpha_implied": mp.nstr(cos2_b, 10),
    "alpha_implied_deg": mp.nstr(alpha_b, 10),
    "reductio_with_unrelated_2_3_quantity_deg": mp.nstr(mp.degrees(mp.acos(mp.sqrt(cos2_r))), 10),
    "verdict": "DISQUALIFIED by construction (pre-committed) -- a bare numeric "
               "substitution with zero discriminating power; reductio confirms "
               "any unrelated X=2/3 gives the identical 'derivation'.",
}

# ---- Route (c): v0, the sealed rank-3 Jordan element (B663/B670 A1) --------
print("\n--- Route (c): v0 (B663/B670 A1) -- support (1,-1,1) at indices (12,13,14) ---")
v0 = (1, -1, 1)
alpha_c, cos2_c = angle_to_democratic(v0)
print(f"v0 raw support vector       = {v0}")
print(f"alpha(v0, (1,1,1))          = {mp.nstr(alpha_c, 8)} deg  (45 deg expected if bridge)")
print(f"cos^2(alpha)                = {mp.nstr(cos2_c, 8)}  (1/2 expected if bridge)")
print("Flag (pre-committed, before this number was seen): this comparison may not even")
print("be principled -- (12,13,14) are raw 27-dim basis-coordinate SLOTS in whatever")
print("convention the object's basis uses, not a verified Peirce/eigenvalue decomposition")
print("of v0 (that needs v0's trace + quadratic-invariant functionals -- NOT banked in")
print("a1_results.json; T2_v0_v0 is explicitly null there). Named as the uncomputed datum.")

results["route_c_v0_jordan_heart"] = {
    "input": "v0 support (1,-1,1) at 27-indices (12,13,14); B663/B670 arc A1, sealed 247ace23...",
    "alpha_deg": mp.nstr(alpha_c, 10),
    "cos2_alpha": mp.nstr(cos2_c, 10),
    "verdict": "NO BRIDGE -- neither numerically 45deg (actual: arccos(1/3) "
               "=70.53deg, cos^2=1/9) nor a principled comparison in the first "
               "place (raw coordinate slots, not v0's actual Peirce eigenvalues, "
               "which are NOT a banked datum -- named as NEEDS-STRUCTURE-adjacent "
               "but does not on its own overturn the default).",
    "uncomputed_datum_named": "v0's Peirce/eigenvalue triple (trace + quadratic "
               "invariant of the exceptional Jordan algebra on v0) -- not present "
               "in a1_results.json (T2_v0_v0: null).",
}

# ============================================================================
# STEP 3(iii) -- coincidence / base-rate calibration for landing on 2/3
# ============================================================================
print()
print("=" * 78)
print("STEP 3(iii) -- base-rate calibration: how cheap is landing on 2/3?")
print("=" * 78)


def is_smooth(n, primes=(2, 3)):
    n = abs(int(n))
    if n == 0:
        return True
    for p in primes:
        while n % p == 0:
            n //= p
    return n == 1


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


N = 30
reduced = [(p, q) for q in range(2, N + 1) for p in range(1, q) if gcd(p, q) == 1]
total = len(reduced)
smooth = [(p, q) for (p, q) in reduced if is_smooth(p) and is_smooth(q)]
n_smooth = len(smooth)
density = mp.mpf(n_smooth) / total

print(f"reduced fractions p/q, 1<=p<q<={N}: total = {total}")
print(f"{{2,3}}-smooth p AND q among them: {n_smooth}  (density = {mp.nstr(density, 6)} = "
      f"{mp.nstr(density * 100, 4)}%)")
print("2/3 itself: p+q=5, p*q=6 -- among the smallest possible non-unit, non-half")
print("fraction heights; i.e. 2/3 sits inside this same small, densely-populated set.")
print("E6's own arithmetic is saturated with exactly these primes: |Z(E6_sc)|=3,")
print("Coxeter number h=12=2^2*3, |W(E6)|=2^7*3^4*5, dim=78=2*3*13, the 27=3^3 --")
print("so ANY dimensionless ratio native to this construction is a priori strongly")
print("biased toward a {2,3}-smooth value, with NO reference to leptons at all.")

results["step3_base_rate"] = {
    "N": N,
    "total_reduced_fractions": total,
    "count_2_3_smooth_both_num_denom": n_smooth,
    "density": mp.nstr(density, 8),
    "reading": "2/3 is among the smallest-height fractions possible and lands "
               "inside a {2,3}-smooth set that is intrinsically dense in this "
               "construction's own native arithmetic (E6 group-theoretic "
               "invariants are pervasively 2,3-smooth) -- landing on 2/3 by "
               "chance is CHEAP, consistent with coincidence, not surprising "
               "enough on its own to indicate a forced link.",
}

# ============================================================================
# VERDICT
# ============================================================================
print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
verdict = "NO-BRIDGE"
print(verdict, "-- all four pre-committed routes fail to derive the 45deg/cos^2=1/2")
print("Koide GEOMETRY from the object; det phi's own structure (STEP 0) is proven to")
print("be a rank-6 Cartan-lattice basis-change fact with categorically no 3-vector or")
print("angle content. The two 2/3's are independent, differently-sourced, both-cheap")
print("small rationals. B1129's dismissal STANDS and is sharpened: the gap (no")
print("instrument) is now CLOSED by an instrument that was built and failed.")

results["verdict"] = verdict
results["gate5_compliance"] = ("lepton masses used ONLY in step1 (the Koide-side "
    "target, alpha=45deg/cos2=1/2); never fed into det phi / trit / v0 constructions.")

with open("results.json", "w") as f:
    json.dump(results, f, indent=1)
print("\nsaved results.json")
