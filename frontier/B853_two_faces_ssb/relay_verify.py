#!/usr/bin/env python3
"""B853 -- the incoming Frob relay, verified before acceptance.

A review seat relayed three facts claiming to overturn B849's T1 and correct its Cell 4. This
session has already found several unpropagated errors in that seat's output (17-vs-43 eigenvalues,
the Riley polynomial), so nothing is accepted on statement. Each fact is recomputed.

Mathematics scope. Nothing reaches CLAIMS.md.
"""
import json
import os
from math import gcd

import sympy as sp
from sympy import isprime

HERE = os.path.dirname(os.path.abspath(__file__))
D_CUSP = -48          # m004's cusp order (B737, banked)
D_FIELD = -3          # the trace field Q(sqrt-3), maximal order


def reduced_forms(D):
    """Primitive reduced positive-definite forms of discriminant D < 0."""
    out = []
    for a in range(1, 300):
        if a * a > abs(D):
            break
        for b in range(-a, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or abs(b) > a:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue                              # reduction tie-breaks
            if gcd(gcd(a, b), c) != 1:
                continue                              # primitive only
            out.append((a, b, c))
    return out


def class_number(D):
    return len(reduced_forms(D))


def cm_point(a, b, D):
    return sp.simplify((-b + sp.sqrt(D)) / (2 * a))


def conjugation_fixes(tau):
    """c acts on the upper half plane by tau -> -conj(tau). Purely imaginary tau are fixed."""
    return bool(sp.simplify(-sp.conjugate(tau) - tau) == 0)


def conductor(D, dK=D_FIELD):
    f2 = D // dK
    f = sp.sqrt(f2)
    return int(f) if f == int(f) else None


def primes_represented(a, b, c, N=200, coprime_to=12, box=15):
    out = set()
    for x in range(-box, box + 1):
        for y in range(-box, box + 1):
            v = a * x * x + b * x * y + c * y * y
            if 0 < v <= N and isprime(v) and gcd(v, coprime_to) == 1:
                out.add(v)
    return sorted(out)


def main():
    res = {}

    # ---- FACT 1: the forms, their CM points, and complex conjugation ----
    forms = reduced_forms(D_CUSP)
    f1 = dict(forms=forms, h=len(forms), points=[], all_fixed_by_c=True,
              all_b_zero=all(b == 0 for (_a, b, _c) in forms))
    for (a, b, c) in forms:
        tau = cm_point(a, b, D_CUSP)
        fixed = conjugation_fixes(tau)
        f1["all_fixed_by_c"] &= fixed
        f1["points"].append(dict(form=[a, b, c], tau=str(tau),
                                 purely_imaginary=bool(sp.simplify(sp.re(tau)) == 0),
                                 fixed_by_conjugation=fixed))
    res["fact1"] = f1

    # ---- FACT 2: is Frob_2 even defined on Cl(O_f)? ----
    f = conductor(D_CUSP)
    two_coprime = gcd(2, f) == 1
    principal = next(x for x in forms if x[0] == 1)
    other = [x for x in forms if x[0] != 1]
    gens = primes_represented(*other[0]) if other else []
    princ_primes = primes_represented(*principal)
    res["fact2"] = dict(
        conductor=f,
        two_divides_conductor=(f % 2 == 0),
        frob2_is_defined_on_Cl_Of=two_coprime,
        two_is_inert_in_K=((D_FIELD % 8) == 5),
        note=("The Artin map Cl(O_f) = Gal(H_O/K) is defined on ideals COPRIME TO f. "
              "2 | f = 4, so (2) is not in that group. Inertness of 2 is true and does not "
              "repair the obstruction."),
        nontrivial_class_primes=gens[:6],
        principal_class_primes=princ_primes[:6],
        smallest_legitimate_generator=(f"Frob_{gens[0]}" if gens else None))

    # ---- FACT 3: the two class numbers, and that they differ ----
    res["fact3"] = dict(
        h_cusp_order_disc_minus48=class_number(D_CUSP),
        h_maximal_order_disc_minus3=class_number(D_FIELD),
        conductor_of_cusp_order=f,
        object_specific=(class_number(D_CUSP) != class_number(D_FIELD)))

    # ---- what this does and does not do to B849 ----
    res["assessment"] = dict(
        T1_overturned=False,
        T1_note=("A class GROUP is a candidate for the symmetry that BREAKS; an ORDER PARAMETER "
                 "is the quantity that MEASURES the breaking (zero in the symmetric phase, "
                 "nonzero in the broken one). h(-48) = 2 supplies the former, not the latter. "
                 "B849's computation stands: CS(m004) = 0 and every orientation-odd invariant "
                 "is 2-torsion."),
        cell4_conclusion_stands=True,
        cell4_mechanism_superseded=True,
        cell4_note=("B849 Cell 4 said c is not in Gal(K^ab/K) -- true, and B851 confirmed it "
                    "verbatim from the primary source. The relay shows c acts trivially on both "
                    "classes for a SHARPER reason (both CM points purely imaginary), and supplies "
                    "the POSITIVE half B849 never did: what DOES generate the Z/2."),
        four_for_four_refined=True,
        refinement=("The MECHANISM is field-level -- shown three ways (phi_m004 = phi_orbifold; "
                    "B850's generic III_1; B852's Farey model). But WHAT THE MECHANISM BREAKS "
                    "may be object-specific: h = 2 at m004's conductor-4 cusp against h = 1 at "
                    "m003's maximal order. Same field, same scattering, different class group. "
                    "cc's 'keeps not being about this object' was a claim about the mechanism "
                    "and was over-generalised to the whole phenomenon."),
        open_question=("Does the programme's system see O_K or the conductor-4 order O_4? "
                       "This is B851's relocated conditional, now sharpened: not merely whether "
                       "the system is BC/CMR-type, but OVER WHICH ORDER."))

    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, sort_keys=True)

    print("=" * 78)
    print("B853 -- the incoming Frob relay, verified")
    print("=" * 78)
    print(f"\nFACT 1  forms of disc {D_CUSP}: {f1['forms']}  -> h = {f1['h']}")
    for p in f1["points"]:
        print(f"        {tuple(p['form'])}: tau = {p['tau']:<16} purely imaginary="
              f"{p['purely_imaginary']}  c fixes={p['fixed_by_conjugation']}")
    print(f"        VERDICT: CONFIRMED -- all b = 0 ({f1['all_b_zero']}), "
          f"c fixes both ({f1['all_fixed_by_c']})")

    f2 = res["fact2"]
    print(f"\nFACT 2  conductor f = {f2['conductor']};  2 | f = {f2['two_divides_conductor']}")
    print(f"        Frob_2 defined on Cl(O_f)? {f2['frob2_is_defined_on_Cl_Of']}   "
          f"(2 inert in K: {f2['two_is_inert_in_K']}, which does not help)")
    print(f"        nontrivial class represents primes {f2['nontrivial_class_primes']}")
    print(f"        principal class represents primes {f2['principal_class_primes']}")
    print(f"        VERDICT: STRUCTURE RIGHT, PRIME WRONG -> "
          f"{f2['smallest_legitimate_generator']}, not Frob_2")

    f3 = res["fact3"]
    print(f"\nFACT 3  h(disc -48, conductor {f3['conductor_of_cusp_order']}) = "
          f"{f3['h_cusp_order_disc_minus48']};  h(disc -3, maximal) = "
          f"{f3['h_maximal_order_disc_minus3']}")
    print(f"        VERDICT: CONFIRMED -- class groups differ = {f3['object_specific']}")

    a = res["assessment"]
    print(f"\nASSESSMENT")
    print(f"  T1 overturned?            {a['T1_overturned']}  (class group != order parameter)")
    print(f"  Cell 4 conclusion stands? {a['cell4_conclusion_stands']}")
    print(f"  Cell 4 mechanism superseded? {a['cell4_mechanism_superseded']}")
    print(f"  'four for four' refined?  {a['four_for_four_refined']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# ---------------------------------------------------------------------------
# The two-faces computation (section 2 of FINDINGS)
# ---------------------------------------------------------------------------
def two_faces():
    """Which face does each object live on, and what is its parity under each Galois action?"""
    t, k = sp.symbols("tau kappa", positive=True)
    V = k * (t**3 / 3 - t**2 / 2 - t)
    phi = (1 + sp.sqrt(5)) / 2
    anti = sp.simplify(-1 / phi)

    def gal5(e):
        return sp.simplify(e.subs(sp.sqrt(5), -sp.sqrt(5)))

    def gal3(e):
        return sp.simplify(e.subs(sp.sqrt(-3), -sp.sqrt(-3)))

    m = sp.sqrt(5) / 3
    Vp = sp.simplify(V.subs(t, phi) / k)
    Va = sp.simplify(V.subs(t, anti) / k)
    return dict(
        m=str(m),
        m_odd_under_sqrt5_galois=bool(sp.simplify(gal5(m) + m) == 0),
        m_fixed_under_sqrt_minus3_galois=bool(sp.simplify(gal3(m) - m) == 0),
        critical_points=[str(sp.nsimplify(phi)), str(sp.nsimplify(anti))],
        critical_points_swapped_by_gal5=bool(sp.simplify(gal5(phi) - anti) == 0),
        critical_values=[str(Vp), str(Va)],
        critical_values_are_galois_conjugates=bool(sp.simplify(gal5(Vp) - Va) == 0),
        V_phi_below_V_zero=bool(Vp < 0),
        barrier_at_anti=bool(Va > 0),
        barrier_height_above_minimum=float(Va - Vp),
        # the point: the whole order-parameter story is FIXED by the sqrt(-3) involution
        order_parameter_story_is_invisible_to_the_broken_symmetry=bool(
            sp.simplify(gal3(m) - m) == 0 and sp.simplify(gal3(Vp) - Vp) == 0))


def twenty_seven_top_block():
    """VERIFY (not assume) that the 27's top principal-SL(2) block is V_16.

    h = 2*rho^vee has alpha_i(h) = 2, so for mu = sum c_j alpha_j the principal weight is
    2*sum(c_j). omega_1 in the ROOT basis is the first row of the inverse Cartan matrix.
    Control: the adjoint's highest root has height 11 (= h - 1), giving V_22.
    """
    C = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                   [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])
    Ci = C.inv()
    top27 = 2 * sum(Ci.row(0))
    theta = [1, 2, 2, 3, 2, 1]                       # highest root of E6, Bourbaki
    return dict(principal_weight_of_omega1=int(top27),
                top_block_of_27_is_V16=(int(top27) == 16),
                highest_root_height=sum(theta),
                adjoint_top_block=2 * sum(theta),
                control_adjoint_is_V22=(2 * sum(theta) == 22))


def multiplicative_independence():
    """2+sqrt3 and 4+sqrt15: independent. NORMS DO NOT SEPARATE THEM -- both are 1."""
    u3 = 2 + sp.sqrt(3)
    u15 = 4 + sp.sqrt(15)
    return dict(norm_u3=int(sp.simplify(u3 * (2 - sp.sqrt(3)))),
                norm_u15=int(sp.simplify(u15 * (4 - sp.sqrt(15)))),
                norms_separate_them=False,
                argument=("Q(sqrt3) cap Q(sqrt15) = Q, so (2+sqrt3)^a = (4+sqrt15)^b would be "
                          "RATIONAL; but 2+sqrt3 is an irrational unit of infinite order, so a = 0, "
                          "and symmetrically b = 0. Hence multiplicatively independent and "
                          "Gelfond-Schneider applies to the length ratio."))
