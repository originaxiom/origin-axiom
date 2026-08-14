#!/usr/bin/env python3
"""B859 -- the SM handoff scrutinised: the cascade's gate was wrong, its conclusion survives.

The incoming SM-campaign handoff (solo seat, 2026-08-03) rests its Q5 CASCADE THEOREM on the
exclusion of SO(8)xU(1) at step 2 as "NOT conformal, c = 9/2". That is an h-dual error:
h^v(D4) = 6, not 7, so c(SO(8)_1 x U(1)) = 4 + 1 = 5 = c(SO(10)_1) and the option IS conformal
-- and at dim 29 it would BEAT SU(5)xU(1) under the handoff's own maximal-symmetry principle.

THE REPAIR, which is better than the original: gate on CHIRALITY instead of conformality.
-1 in the Weyl group <=> every rep self-conjugate <=> no chiral matter. For D_n, -1 in W iff
n even. SO(8) = D4: all reps real; and by Borel-de Siebenthal D4 contains no A4, so the branch
cannot reach SU(5) either. Two independent obstructions. Applied uniformly, the same gate also
retires part of the Michel import at step 1: the vector-like cosets (Sp(8)'s 42, SU(6)xSU(2)'s
(20,2)) die by the framework's own even/odd criterion.

Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))


def c(dim, hv, k=1):
    return Fr(k * dim, k + hv)


def minus1_in_W(family, n):
    """-1 in the Weyl group: A_n iff n==1; B/C always; D_n iff n even; E6 no; E7/E8/F4/G2 yes."""
    return {"A": n == 1, "B": True, "C": True, "D": n % 2 == 0,
            "E6": False, "E7": True, "E8": True, "F4": True, "G2": True}[family]


def main():
    res = {}

    # --- the h-dual error, pinned by the dim = rank(h+1) identity (simply-laced) ---
    hv = {}
    for lab, dim, rank in [("A1", 3, 1), ("A2", 8, 2), ("A3", 15, 3), ("A4", 24, 4),
                           ("A5", 35, 5), ("D4", 28, 4), ("D5", 45, 5), ("E6", 78, 6)]:
        hv[lab] = dim // rank - 1
    res["h_dual"] = hv
    res["handoff_used_D4"] = 7
    res["D4_correct"] = hv["D4"]
    res["so8u1_c"] = str(c(28, hv["D4"]) + 1)
    res["so10_c"] = str(c(45, hv["D5"]))
    res["so8u1_is_conformal"] = (c(28, hv["D4"]) + 1 == c(45, hv["D5"]))
    # free-fermion cross-check: SO(N)_1 = N Majorana fermions, c = N/2
    res["free_fermion_check"] = {"SO(8)_1": str(Fr(8, 2)), "SO(10)_1": str(Fr(10, 2))}

    # --- step 2, re-gated ---
    res["step2"] = [
        dict(option="SU(5)xU(1)", dim=25, c=str(c(24, 5) + 1), conformal=True,
             chiral=True, note="A4: -1 not in W; complex reps"),
        dict(option="Pati-Salam SU(4)xSU(2)^2", dim=21, c=str(c(15, 4) + 2 * c(3, 2)),
             conformal=True, chiral=True, note="A3 factor complex"),
        dict(option="SO(8)xU(1)", dim=29, c=str(c(28, 6) + 1), conformal=True,
             chiral=False,
             note="D4: -1 IN W, all reps real; AND Borel-de Siebenthal: no A4 in D4"),
    ]
    viable = [o for o in res["step2"] if o["chiral"]]
    res["step2_winner"] = max(viable, key=lambda o: o["dim"])["option"]
    res["step2_unique"] = (res["step2_winner"] == "SU(5)xU(1)")

    # --- step 1, same gate on the COSET (the rep carrying the would-be matter) ---
    res["step1"] = [
        dict(option="SO(10)xU(1)", dim=46, coset="16+16bar", coset_complex=True),
        dict(option="SU(6)xSU(2)", dim=38, coset="(20,2)", coset_complex=False,
             note="20 = Lambda^3(6) is SELF-DUAL; (20,2) self-conjugate: vector-like"),
        dict(option="SU(3)^3", dim=24, coset="(3,3,3)+conj", coset_complex=True),
        dict(option="Sp(8)", dim=36, coset="42", coset_complex=False,
             note="C4: -1 in W, all reps self-dual"),
        dict(option="SU(3)_9", dim=8, coset="(4,1)+(1,4)", coset_complex=True),
    ]
    v1 = [o for o in res["step1"] if o["coset_complex"]]
    res["step1_winner"] = max(v1, key=lambda o: o["dim"])["option"]
    res["step1_note"] = ("the vector-like cosets die by the framework's own even/odd "
                         "criterion, retiring part of the Michel import")

    # --- step 3: the gate is silent; the trit stands ---
    res["step3"] = [dict(option="SU(4)xU(1)", dim=16, chiral=True),
                    dict(option="SM", dim=12, chiral=True),
                    dict(option="SU(3)xU(1)^2", dim=10, chiral=True)]
    res["step3_gate_silent"] = True
    res["sm_nonextremal"] = True

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 74)
    print("B859 -- the cascade re-gated on chirality (-1 in W)")
    print("=" * 74)
    print(f"\n  h^v(D4): handoff used {res['handoff_used_D4']}, correct {res['D4_correct']}")
    print(f"  c(SO(8)xU(1)) = {res['so8u1_c']} = c(SO(10)_1) = {res['so10_c']}"
          f"  -> conformal: {res['so8u1_is_conformal']}")
    print(f"\n  step 1 winner (chiral coset + max dim): {res['step1_winner']}")
    print(f"  step 2 winner (chiral + max dim)      : {res['step2_winner']}"
          f"   unique: {res['step2_unique']}")
    print(f"  step 3: gate silent; SM in menu, non-extremal: {res['sm_nonextremal']}")
    print("\n  => the cascade's CONCLUSION survives with a framework-native gate;")
    print("     its stated conformality gate at step 2 was wrong (h-dual error).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
