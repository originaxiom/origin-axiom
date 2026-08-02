#!/usr/bin/env python3
"""B857 -- the being voice CANNOT SAY 5, and the reason is a splitting type, not a silence.

LAW_MAP's H-EAR clause (iii) SILENCE says the golden is never emitted through the object's solo
continuous channel. Its supporting leg (B746-F11) is a GREP: "Grep of the banked voice artifacts
(B737/B739): zero golden markers."

This replaces the grep with an exact arithmetic fact, and corrects its scope.

The voice is zeta_K(s) = sum a_K(n)/n^s over K = Q(sqrt-3), with a_K(n) = #ideals of norm n.
For an INERT prime p the only ideal above p is (p), of norm p^2, so a_K(p) = 0.

Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os

from sympy import jacobi_symbol

HERE = os.path.dirname(os.path.abspath(__file__))

FIELDS = [(-3, "Q(sqrt-3)", "BEING  (m004's trace field)"),
          (-4, "Q(i)", "SILVER (m136's trace field)"),
          (5, "Q(sqrt5)", "HEARING (the pre-geometric carrier)")]
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def splitting(d, p):
    """ram / split / inert for the prime p in the quadratic field of discriminant d."""
    if d % p == 0:
        return "ram"
    if p == 2:
        return "ram" if d % 4 == 0 else ("split" if d % 8 == 1 else "inert")
    s = jacobi_symbol(d, p)
    return {1: "split", -1: "inert", 0: "ram"}[s]


def a_K(d, p):
    """Number of ideals of norm exactly p."""
    t = splitting(d, p)
    return {"ram": 1, "split": 2, "inert": 0}[t]


def main():
    table = {}
    for d, name, role in FIELDS:
        table[name] = dict(disc=d, role=role,
                           splitting={p: splitting(d, p) for p in PRIMES},
                           a_K={p: a_K(d, p) for p in PRIMES})

    res = dict(
        table=table,
        being_cannot_say_5=(a_K(-3, 5) == 0),
        being_says_3=(a_K(-3, 3) == 1),
        silver_can_say_5=(a_K(-4, 5) == 2),
        hearing_cannot_say_3=(splitting(5, 3) == "inert"),
        mutual_blindness=(splitting(-3, 5) == "inert" and splitting(5, 3) == "inert"),
        # the correction to F11's scope
        is_a_property_of_voices=False,
        note=("a_K(5) = 0 because 5 is INERT in Q(sqrt-3) -- the being voice's Dirichlet series "
              "has no coefficient at the hearing prime. But 5 SPLITS in Q(i), so the SILVER's "
              "voice can say 5. The phenomenon is a SPLITTING TYPE of one prime in one field, "
              "not a property of voices in general. B746-F11 as stated over-generalises."))

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 78)
    print("B857 -- the voice, the hearing prime, and mutual blindness")
    print("=" * 78)
    print(f"\n  {'field':12} {'role':28} " + " ".join(f"{p:>6}" for p in PRIMES))
    for d, name, role in FIELDS:
        print(f"  {name:12} {role:28} "
              + " ".join(f"{splitting(d,p):>6}" for p in PRIMES))
    print(f"\n  {'field':12} {'a_K(p) = #ideals of norm p':28} "
          + " ".join(f"{p:>6}" for p in PRIMES))
    for d, name, role in FIELDS:
        print(f"  {name:12} {'':28} " + " ".join(f"{a_K(d,p):>6}" for p in PRIMES))
    print()
    print(f"  being cannot say 5 (a_K(5) = 0, INERT) : {res['being_cannot_say_5']}")
    print(f"  being says 3       (a_K(3) = 1, RAM)   : {res['being_says_3']}")
    print(f"  hearing cannot say 3 (3 INERT in Q(v5)): {res['hearing_cannot_say_3']}")
    print(f"  MUTUAL BLINDNESS, both ways            : {res['mutual_blindness']}")
    print(f"  SILVER can say 5   (a(5) = 2, SPLIT)   : {res['silver_can_say_5']}")
    print()
    print("  => replaces B746-F11's grep with an exact fact, AND corrects its scope:")
    print("     it is a SPLITTING TYPE, not a property of voices.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
