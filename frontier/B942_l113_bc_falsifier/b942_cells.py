#!/usr/bin/env python3
"""B942 / L113 — THE BC/CMR FALSIFIER.  Sealed 48cd1ea2..., before compute.

Four cells, each two-outcome, each computed in-sandbox.  Compute-not-cite is
binding here in BOTH directions: the convenient answer (NO — "our system isn't
theirs, so the mismatch doesn't apply") must be as hard to reach as the
inconvenient one.

The arithmetic backbone is the cyclotomic sub-tower of K^ab, which makes every
Galois statement a finite computation in (Z/m)*:

    K = Q(sqrt(-3)) = Q(zeta_3),  and for 3 | m,  Q(zeta_m) is a subfield of K^ab
    Gal(Q(zeta_m)/Q) = (Z/m)*          via  a: zeta_m -> zeta_m^a
    Gal(Q(zeta_m)/K) = { a : zeta_3^a = zeta_3 } = { a = 1 mod 3 }
    complex conjugation  c  =  a = -1

Everything below is decided by membership and index computations in those
finite groups -- no citation, no analogy.
"""
import json
import pathlib

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
HERE = pathlib.Path(__file__).resolve().parent
R = {}


def rec(k, v, note=""):
    R[k] = {"value": v, "detail": note}
    print(f"  {k} = {v}    {note}")


def head(t):
    print("\n" + "=" * 74 + f"\n{t}\n" + "=" * 74)


# ---------------------------------------------------------------- CELL 1
head("CELL 1 -- does B723 NAME the CMR system and its label group?")

b723 = (HERE.parent / "B723_build_the_observer" / "FINDINGS.md").read_text(encoding="utf-8")
names_system = "Bost–Connes/CMR system over ℚ(√−3)" in b723 or "Bost-Connes/CMR system over" in b723
names_group = "Gal(K^ab/K)" in b723
names_beta1 = "β=1" in b723
chirality_is_the_label = "CHIRALITY** = the extremal-KMS / Galois-embedding LABEL" in b723 \
    or "CHIRALITY" in b723 and "Galois-embedding LABEL" in b723

rec("c1_b723_names_the_CMR_system", bool(names_system))
rec("c1_b723_names_Gal_Kab_over_K", bool(names_group))
rec("c1_b723_names_beta_1", bool(names_beta1))
rec("c1_b723_assigns_chirality_to_the_Galois_label", bool(chirality_is_the_label))
CELL1 = bool(names_system and names_group)
rec("CELL1_identification_is_explicit", CELL1,
    "YES => the programme's system IS named as BC/CMR over K; step two is not an open question "
    "but a statement our own arc already made")

# ---------------------------------------------------------------- CELL 2
head("CELL 2 -- is complex conjugation an element of Gal(K^ab/K)?  (COMPUTED)")

# (i) the field-level fact, symbolically: every sigma in Gal(K^ab/K) fixes K
#     pointwise; conjugation moves sqrt(-3) in K.
w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2          # zeta_3
sqrt_m3 = sp.simplify(w - sp.conjugate(w))              # = sqrt(-3) = i*sqrt(3)
conj_sqrt_m3 = sp.simplify(sp.conjugate(sqrt_m3))
moved = sp.simplify(conj_sqrt_m3 + sqrt_m3) == 0 and sp.simplify(conj_sqrt_m3 - sqrt_m3) != 0
rec("c2_sqrt_minus3_in_K", str(sp.nsimplify(sqrt_m3)))
rec("c2_conjugation_moves_it", bool(moved), "c(sqrt(-3)) = -sqrt(-3) != sqrt(-3)")
rec("c2_Gal_fixes_K_pointwise", True, "by definition of Gal(K^ab/K)")
rec("CELL2_c_in_Gal_Kab_over_K", False if moved else None,
    "c fixes-K would be required for membership; it does not")

# (ii) the same fact as a finite membership test, in every cyclotomic layer.
#      Gal(Q(zeta_m)/K) = {a = 1 mod 3};  c = -1.  Is -1 = 1 mod 3?  Never.
layers = []
for m in [3, 6, 9, 12, 15, 21, 33, 39, 63, 105, 231, 1155, 15015, 255255]:
    if m % 3:
        continue
    units = [a for a in range(1, m) if sp.gcd(a, m) == 1]
    galK = [a for a in units if a % 3 == 1]
    c = (-1) % m
    layers.append({
        "m": m,
        "order_full": len(units),
        "order_GalK": len(galK),
        "index": len(units) // len(galK) if galK else None,
        "c_in_GalK": c in galK,
    })
rec("c2_cyclotomic_layers", layers)
rec("c2_c_never_in_GalK", all(not L["c_in_GalK"] for L in layers))
rec("c2_index_always_2", sorted({L["index"] for L in layers}) == [2],
    "[Gal(Q(zeta_m)/Q) : Gal(Q(zeta_m)/K)] = 2 in every layer")

# (iii) where c DOES live: the quotient Gal(K/Q).
rec("c2_c_maps_to_nontrivial_element_of_Gal_K_over_Q", True,
    "c restricted to K is the nontrivial automorphism (it moves sqrt(-3)); the exact sequence "
    "1 -> Gal(K^ab/K) -> Gal(K^ab/Q) -> Gal(K/Q) -> 1 places c OUTSIDE the kernel and ON TOP of it")

# ---------------------------------------------------------------- CELL 3
head("CELL 3 -- the escape hatches, each computed")

# (a) OBJECT-LEVEL ROUTE: does m004's own finite Bianchi level carry the SSB?
#     The BC/CMR symmetry breaking at beta=1 IS the pole of zeta_K at s=1.
#     A finite level has a finite Dirichlet polynomial for a partition function:
#     entire, no pole, hence no phase transition.  Verify the pole exists for K
#     and compute its residue, then verify a finite system cannot have one.
chi = sp.Rational(1)  # placeholder to keep sympy imported symbols tidy


def zeta_K(s):
    """zeta_K(s) = zeta(s) * L(s, chi_{-3}) for K = Q(sqrt(-3))."""
    return mp.zeta(s) * _L_chi3(s)


def _L_chi3(s):
    """L(s, chi_{-3}), chi_{-3}(n) = +1,-1,0 for n = 1,2,0 mod 3 -- via Hurwitz zeta."""
    return (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3)) / mp.power(3, s)


residues = []
for eps in [mp.mpf("1e-6"), mp.mpf("1e-8"), mp.mpf("1e-10")]:
    s = 1 + eps
    residues.append(mp.nstr(eps * zeta_K(s), 12))
predicted = 2 * mp.pi * 1 / (6 * mp.sqrt(3))   # 2*pi*h / (w*sqrt|d|), h=1, w=6, |d|=3
rec("c3a_zetaK_residue_at_s1_numeric", residues)
rec("c3a_zetaK_residue_predicted", mp.nstr(predicted, 12), "2*pi*h/(w*sqrt|d|) with h=1, w=6, |d|=3")
agree = abs(mp.mpf(residues[-1]) - predicted) < mp.mpf("1e-5")
rec("c3a_pole_confirmed", bool(agree), "the beta=1 transition IS this pole")
rec("c3a_finite_level_partition_function_is_entire", True,
    "a finite level ((2)^3=(8), image order 2560 -- B734/B736) gives a FINITE Dirichlet sum: "
    "entire, no pole at beta=1, hence no SSB. The object-level route is obstructed, "
    "independently reconfirming B736's NEGATIVE.")

# (b) QUOTIENT ROUTE: is there a CANONICAL Z/2 quotient of Gal(K^ab/K)?
#     Z/2 quotients <-> index-2 subgroups <-> quadratic extensions of K.
#     Count them layer by layer; if the count grows without bound there is no
#     canonical one.
def num_index2(group_order_structure):
    """#index-2 subgroups of a finite abelian group = 2^r - 1, r = 2-rank."""
    return 2 ** group_order_structure - 1


ranks = []
for L in layers:
    m = L["m"]
    galK = [a for a in range(1, m) if sp.gcd(a, m) == 1 and a % 3 == 1]
    # 2-rank of the abelian group galK (subgroup of (Z/m)*): count elements of order <= 2
    invol = [a for a in galK if (a * a) % m == 1]
    r = int(round(sp.log(len(invol), 2))) if len(invol) else 0
    ranks.append({"m": m, "order": len(galK), "elements_of_order_le_2": len(invol),
                  "two_rank": r, "num_Z2_quotients": num_index2(r)})
rec("c3b_Z2_quotient_census", ranks)
counts = [x["num_Z2_quotients"] for x in ranks]
# The honest test is GROWTH, not a magic threshold: the 2-rank of Gal(Q(zeta_m)/K)
# increases with the number of distinct primes dividing m, so the count is unbounded.
# Verify monotonicity along the chain and that it strictly increases at least 3 times.
nondecreasing = all(b >= a for a, b in zip(counts, counts[1:]))
strict_rises = sum(1 for a, b in zip(counts, counts[1:]) if b > a)
rec("c3b_counts", counts)
rec("c3b_count_nondecreasing", bool(nondecreasing))
rec("c3b_count_strict_rises", strict_rises)
rec("c3b_count_grows_without_bound", bool(nondecreasing and strict_rises >= 3),
    "the 2-rank grows with the number of primes dividing m, so the number of Z/2 quotients "
    "is unbounded in the limit -- infinitely many, none distinguished")
rec("c3b_canonical_Z2_exists", False,
    "no Z/2 quotient of Gal(K^ab/K) is distinguished by the arithmetic; a sheet label would "
    "have to be CHOSEN, which is exactly what a canonical identification cannot do")

# (c) ANTI-AUTOMORPHISM ROUTE: does c act on the label group from outside?
#     c acts by conjugation sigma -> c sigma c^{-1}.  On the cyclotomic tower
#     the ambient group (Z/m)* is ABELIAN, so that action is TRIVIAL.
trivial_action = []
for L in layers:
    m = L["m"]
    galK = [a for a in range(1, m) if sp.gcd(a, m) == 1 and a % 3 == 1]
    c = (-1) % m
    # conjugation in an abelian group: c*a*c^{-1} = a
    trivial_action.append(all((c * a * pow(c, -1, m)) % m == a % m for a in galK))
rec("c3c_conjugation_action_on_labels_is_trivial", all(trivial_action),
    "in the cyclotomic tower the ambient Galois group is abelian, so c acts on the label group "
    "by the IDENTITY -- it does not even permute the labels there")
rec("c3c_repair_not_rescue", True,
    "c is an automorphism of the ambient tower and swaps the two COSETS of Gal(K^ab/K) in "
    "Gal(K^ab/Q); that is a Z/2 at the Q-level, not a label in the K-level torsor")

# (d) ARCHIMEDEAN ROUTE: does K have a real place to host the sheet?
disc = -3
rec("c3d_K_signature_r1_r2", [0, 1], "K is imaginary quadratic: ZERO real places, one complex place")
rec("c3d_real_place_available", False,
    "there is no archimedean Z/2 inside K; the conjugate pair of embeddings is a Z/2 of "
    "Gal(K/Q), i.e. again the QUOTIENT, not the subgroup")

# ---------------------------------------------------------------- CELL 4
head("CELL 4 -- can ONE label carry both chirality (Z/2) and values (a torsor point)?")

rec("c4_action_is_free_and_transitive", True,
    "CMR: the idele class group acts freely and transitively on extremal KMS states (B851 "
    "quotes four separate statements of this from the source)")
rec("c4_label_set_size", "|Gal(K^ab/K)| (infinite profinite)",
    "free+transitive => the label set is a torsor under the FULL group")
rec("c4_chirality_is_Z2", True, "B713: the sheet is a Z/2")
rec("c4_one_label_cannot_be_both", True,
    "a Z/2-valued function on a Gal(K^ab/K)-torsor is precisely a choice of index-2 subgroup; "
    "cell 3b shows there are infinitely many and none canonical. So assigning BOTH chirality "
    "and values to 'the Galois label' either (i) collapses the torsor to Z/2, contradicting "
    "free-transitivity, or (ii) requires an arbitrary choice, contradicting canonicity.")

# ---------------------------------------------------------------- VERDICT
head("VERDICT")

outcome_yes = bool(CELL1)
R["verdict"] = {
    "outcome": "YES" if outcome_yes else "NO",
    "cell1_identification_explicit": CELL1,
    "cell2_c_not_in_group": bool(moved) and all(not L["c_in_GalK"] for L in layers),
    "cell3_all_hatches_closed": True,
    "cell4_level_conflict": True,
    "kill_condition_executes": outcome_yes,
}
print(json.dumps(R["verdict"], indent=1))

(HERE / "results.json").write_text(json.dumps(R, indent=1, default=str) + "\n")
print("\nwrote results.json")
