#!/usr/bin/env python3
"""B871 -- G5, the keystone: "registerable" formalized as a B599 pairing datum.

The cascade's gate (B861: the generation stays chiral as a stripped multiset) was the
last imported DEFINITION. This arc pays it: a chirality-REGISTERING measurement is a
B599 pairing datum

    bra        = chi_R, the generation's (formal) character,
    probe      = f_rho = chi_rho - chi_rhobar   (theta-odd, dial-neutral),
    contraction = the invariant orthonormality pairing,
    evaluation A(R, rho) = mult_rho(R) - mult_rhobar(R)  (an integer).

Theorem (verified on every cascade menu row):
  (a) REGISTERS: A(Rbar, rho) = -A(R, rho) -- the evaluation is odd under the
      theta-class swap; a nonzero A hears which side it is on.
  (b) B599 PARITY: the even (self-conjugate-paired) part of R contributes 0 to every
      A -- registering is a strictly odd-sector hearing; the minimal registering
      configuration pairs odd against odd (n = 2, the B593 shape).
  (c) KEYSTONE EQUIVALENCE: (exists rho with A != 0) <=> the stripped multiset is
      chiral <=> B861's gate. "Registerable" = "a B599-legal measurement of chirality
      exists."
  (d) BLINDNESS WITNESS: where the gate fails, the blindness is an intertwiner
      (Schur pairing); the cascade's banked witness J6 = epsilon on Lambda^2(4)
      (B860) is reverified here exactly over Z.

Characters are FORMAL: irreps are basis vectors of a free Z-module, conjugation is a
permutation, the pairing is Kronecker. Nothing is numerically integrated; every A is
an exact integer. Mathematics scope; nothing to CLAIMS.md; Gate 5 untouched.
"""
import importlib.util
import json
import os
from collections import Counter
from itertools import permutations

HERE = os.path.dirname(os.path.abspath(__file__))
_B861 = os.path.join(HERE, "..", "B861_fused_cascade", "fused_cascade.py")
_spec = importlib.util.spec_from_file_location("b861", _B861)
b861 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b861)
CONJ, STEPS, chiral = b861.CONJ, b861.STEPS, b861.chiral


def conj_item(item):
    return tuple(CONJ[x] for x in item)


# ---------------------------------------------------------- the pairing datum
def evaluation(R, rho):
    """A(R, rho) = <chi_R, chi_rho - chi_rhobar> under the Kronecker pairing."""
    c = Counter(R)
    return c[rho] - c[conj_item(rho)]


def even_odd_split(R):
    """chi_R = even + odd in the free Z-module: even = the self-conjugate-paired
    portion, odd = the antisymmetric remainder. Returns (even, odd) as Counters
    with integer (possibly half-integer avoided: use paired construction)."""
    c, e, o = Counter(R), Counter(), Counter()
    for item in set(c) | {conj_item(i) for i in c}:
        m, mbar = c[item], c[conj_item(item)]
        paired = min(m, mbar)
        e[item] = paired          # even part: matched rho/rhobar pairs
        o[item] = m - paired      # odd remainder (nonneg on one side of each pair)
    return e, o


def eval_counter(c, rho):
    return c[rho] - c[conj_item(rho)]


# ---------------------------------------------------------- J6 = epsilon (B860)
def su4_generators():
    """Basis of sl(4): elementary E_ij (i != j) and Cartan H_i, as 4x4 int arrays."""
    def M():
        return [[0] * 4 for _ in range(4)]
    gens = []
    for i in range(4):
        for j in range(4):
            if i != j:
                m = M(); m[i][j] = 1; gens.append(m)
    for i in range(3):
        m = M(); m[i][i] = 1; m[i + 1][i + 1] = -1; gens.append(m)
    return gens


def lambda2_action(X):
    """Induced action of X on Lambda^2(C^4), basis e_i^e_j (i<j), exact ints."""
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    idx = {p: k for k, p in enumerate(pairs)}
    A = [[0] * 6 for _ in range(6)]
    for (i, j), k in idx.items():
        # X.(ei^ej) = (X ei)^ej + ei^(X ej)
        for a in range(4):
            if X[a][i]:
                p, s = ((a, j), 1) if a < j else ((j, a), -1)
                if a != j:
                    A[idx[p]][k] += s * X[a][i]
            if X[a][j]:
                p, s = ((i, a), 1) if i < a else ((a, i), -1)
                if a != i:
                    A[idx[p]][k] += s * X[a][j]
    return A


def epsilon_form():
    """J[(ij),(kl)] = sign of (i,j,k,l) as a permutation of (0,1,2,3), else 0."""
    pairs = [(i, j) for i in range(4) for j in range(i + 1, 4)]
    J = [[0] * 6 for _ in range(6)]
    for a, (i, j) in enumerate(pairs):
        for b, (k, l) in enumerate(pairs):
            if {i, j, k, l} == {0, 1, 2, 3}:
                perm = (i, j, k, l)
                sgn = 1
                for x in range(4):
                    for y in range(x + 1, 4):
                        if perm[x] > perm[y]:
                            sgn = -sgn
                J[a][b] = sgn
    return J


def j6_intertwines():
    """J rho(X) + rho(X)^T J = 0 for every sl(4) generator: 6 = Lambda^2(4) is
    self-dual VIA epsilon -- the blindness witness on the failing step-3 row."""
    J = epsilon_form()
    for X in su4_generators():
        A = lambda2_action(X)
        for r in range(6):
            for c in range(6):
                s = sum(J[r][k] * A[k][c] for k in range(6)) \
                    + sum(A[k][r] * J[k][c] for k in range(6))
                if s != 0:
                    return False
    return True


# ---------------------------------------------------------------------- main
def main():
    res = {"datum": "bra chi_R | probe f_rho = chi_rho - chi_rhobar (theta-odd, "
                    "dial-neutral) | invariant Kronecker contraction",
           "rows": []}
    for key, menu in STEPS:
        for name, dim, gen in menu:
            R = list(gen)
            probes = sorted(set(R) | {conj_item(i) for i in R})
            evals = {str(p): evaluation(R, p) for p in probes}
            best = max(abs(v) for v in evals.values())
            e, o = even_odd_split(R)
            even_blind = all(eval_counter(e, p) == 0 for p in probes)
            odd_carries = all(eval_counter(o, p) == evaluation(R, p) for p in probes)
            Rbar = [conj_item(i) for i in R]
            odd_under_swap = all(evaluation(Rbar, p) == -evaluation(R, p)
                                 for p in probes)
            res["rows"].append(dict(
                step=key, option=name, gate_chiral=chiral(R),
                register_exists=best > 0, max_abs_eval=best,
                registers_swap=odd_under_swap, even_part_blind=even_blind,
                odd_part_carries_all=odd_carries))
    res["keystone_equivalence"] = all(r["register_exists"] == r["gate_chiral"]
                                      for r in res["rows"])
    res["swap_oddness_all_rows"] = all(r["registers_swap"] for r in res["rows"])
    res["b599_parity_all_rows"] = all(r["even_part_blind"] and
                                      r["odd_part_carries_all"]
                                      for r in res["rows"])
    res["j6_epsilon_intertwines"] = j6_intertwines()
    res["can_fail"] = any(not r["register_exists"] for r in res["rows"])
    res["can_pass"] = any(r["register_exists"] for r in res["rows"])

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True)

    print("=" * 74)
    print("B871 -- G5: registering as a B599 pairing datum")
    print("=" * 74)
    for r in res["rows"]:
        print(f"  {r['step']:11} {r['option']:14} gate {str(r['gate_chiral']):5} "
              f"datum-exists {str(r['register_exists']):5} maxA {r['max_abs_eval']}")
    print(f"\n  keystone equivalence (all rows) : {res['keystone_equivalence']}")
    print(f"  evaluation odd under the swap   : {res['swap_oddness_all_rows']}")
    print(f"  B599 parity (even blind)        : {res['b599_parity_all_rows']}")
    print(f"  J6 = epsilon intertwines (B860) : {res['j6_epsilon_intertwines']}")
    print(f"  criterion can fail / can pass   : {res['can_fail']} / {res['can_pass']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
