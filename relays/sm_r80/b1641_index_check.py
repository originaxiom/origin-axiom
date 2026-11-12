#!/usr/bin/env python3
"""SM-R80: B1641's index recomputed from its statement, in exact arithmetic, by this seat's own code.

The statement (B1641's sealed script, verification/w46_on_main.py, its W3 line): index(Lambda+, n) = -chi_{3/2+12n}(rho_T)
+ the sum over the pieces of Lambda+ of chi_{1+12n}, where chi_k(rho) = dim M_k(rho) - dim S_{2-k}(rho*) is the Euler
characteristic of vector-valued forms.  rho_T is the representation on the three thetas as B1634 writes it:
rho(S) = e^{-23 pi i/4} P13, rho(T) = e^{7 pi i/4} diag(i, 1, 1) P23.  A unit m_j on a line lowers that line's exponent
by m_j (B1796).  chi is computed by Borcherds' formula (Reflection groups of Lorentzian lattices, section 7):
chi_k = d + d k/12 - alpha(e^{pi i k/2} rho(S)) - alpha((e^{pi i k/3} rho(S) rho(T))^{-1}) - sum_j (a_j - m_j),
alpha(A) the sum of the eigenvalues' turns in [0, 1), a_j the turns of rho(T).  Every matrix here is monomial with
root-of-unity entries, so eigenvalue turns are exact rationals: a cycle of length l whose entries multiply to
e^{2 pi i theta} has eigenvalues with turns (theta + j)/l, j = 0 .. l-1.  Nothing is taken from main's code.
Validated first on known spaces: the trivial representation (dim M_k of the full modular group, k = 0 .. 28) and the
characters of eta^r (r = 1 .. 23, weight r/2: the space is C eta^r and the dual cusp space is 0, so chi = 1).
Planted: the index with the sign of its defining term reversed must disagree with B1641's sealed table.
Usage (from a clone that has the commit): b1641_index_check.py OUT.json"""
import json
import subprocess
import sys
from fractions import Fraction as Fr

REV = "c40446392"


class Mono:
    """a monomial matrix: column j goes to row perm[j] with entry e^{2 pi i turn[j]}"""
    def __init__(self, perm, turn):
        self.perm, self.turn = list(perm), [Fr(t) % 1 for t in turn]

    def __matmul__(self, o):      # (self o)[:, j] = self[:, o.perm[j]] * entry
        return Mono([self.perm[o.perm[j]] for j in range(len(o.perm))],
                    [o.turn[j] + self.turn[o.perm[j]] for j in range(len(o.perm))])

    def scale(self, t):
        return Mono(self.perm, [x + t for x in self.turn])

    def inv(self):
        n = len(self.perm); p = [0] * n; t = [0] * n
        for j in range(n):
            p[self.perm[j]] = j; t[self.perm[j]] = -self.turn[j]
        return Mono(p, t)

    def eig_turns(self):
        seen, out = set(), []
        for s in range(len(self.perm)):
            if s in seen:
                continue
            cyc, j = [], s
            while j not in seen:
                seen.add(j); cyc.append(j); j = self.perm[j]
            th = sum(self.turn[c] for c in cyc) % 1
            out += [((th + i) / len(cyc)) % 1 for i in range(len(cyc))]
        return sorted(out)


alpha = lambda A: sum(A.eig_turns(), Fr(0))


def chi(k, S, T, m=None):
    k = Fr(k); d = len(S.perm)
    a = T.eig_turns()
    m = m or [0] * d
    return d + d * k / 12 - alpha(S.scale(k / 4)) - alpha((S @ T).scale(k / 6).inv()) - sum(x - y for x, y in zip(a, m))


out = {"commit": REV}
# validation 1: the trivial representation
classical = {0: 1, 2: 0, 4: 1, 6: 1, 8: 1, 10: 1, 12: 2, 14: 1, 16: 2, 18: 2, 20: 2, 22: 2, 24: 3, 26: 2, 28: 3}
one = Mono([0], [0])
out["validation_trivial"] = {k: str(chi(k, one, one)) for k in classical}
v1 = all(chi(k, one, one) == classical[k] for k in classical if k != 2)
# weight 2: M_2 = 0 and S_0 = 0 for the trivial representation... chi_2 = dim M_2 - dim S_0 = 0 - 0 = 0
v1 = v1 and chi(2, one, one) == 0
# validation 2: eta^r, r = 1 .. 23, with eta^r(-1/tau) = tau^{r/2} e^{-pi i r/4} eta^r(tau), eta^r(tau + 1) = e^{2 pi i r/24} eta^r
eta = {r: str(chi(Fr(r, 2), Mono([0], [Fr(-r, 8)]), Mono([0], [Fr(r, 24)]))) for r in range(1, 24)}
out["validation_eta_powers"] = eta
v2 = all(v == "1" for v in eta.values())
# rho_T as B1634 writes it
P13, P23 = [2, 1, 0], [0, 2, 1]
rS = Mono(P13, [Fr(-23, 8)] * 3)
rT = Mono([0, 1, 2], [Fr(1, 4), 0, 0]) @ Mono(P23, [0, 0, 0])
rT = rT.scale(Fr(7, 8))
a = rT.eig_turns()
out["rho_T_exponents"] = [str(x) for x in a]
res = {"chi_3/2": str(chi(Fr(3, 2), rS, rT)),
       "chi_3/2+12n": {n: str(chi(Fr(3, 2) + 12 * n, rS, rT)) for n in (-1, 0, 1)},
       "chi_3/2 with a unit on one line": [str(chi(Fr(3, 2), rS, rT, m)) for m in ([1, 0, 0], [0, 1, 0], [0, 0, 1])],
       "chi_3/2 with the uniform unit, and at weight 27/2": [str(chi(Fr(3, 2), rS, rT, [1, 1, 1])), str(chi(Fr(27, 2), rS, rT))]}
out["rho_T"] = res
index = lambda n, sign=-1: sign * chi(Fr(3, 2) + 12 * n, rS, rT)       # empty Lambda+: no piece term
out["index_empty_Lambda_plus"] = {n: str(index(n)) for n in (-1, 0, 1)}
out["index_empty_Lambda_plus_unit_on_one_line"] = str(-chi(Fr(3, 2), rS, rT, [1, 0, 0]))
sealed = json.loads(subprocess.run(["git", "show", REV + ":frontier/B1641_w46_on_main_and_the_two_objects/verification/w46_on_main.json"],
                                   capture_output=True, text=True, check=True).stdout)["W3"]
table = {ident: {n: v["table"]["0,n=%d" % n][0] for n in (-1, 0, 1)} for ident, v in sealed.items()}
out["sealed_table_empty_Lambda_plus"] = table
agree = all(abs(float(index(n)) - t[n]) < 1e-9 for t in table.values() for n in (-1, 0, 1))
planted = all(abs(float(index(n, sign=+1)) - t[n]) < 1e-9 for t in table.values() for n in (-1, 0, 1))
out["checks"] = {
    "validation: trivial representation, classical dimensions": v1,
    "validation: eta^r, r = 1..23, chi = 1": v2,
    "rho_T's exponents are 1/8, 3/8, 7/8": a == [Fr(1, 8), Fr(3, 8), Fr(7, 8)],
    "chi_3/2(rho_T) = 0": chi(Fr(3, 2), rS, rT) == 0,
    "chi_{3/2+12n}(rho_T) = 3n": all(chi(Fr(3, 2) + 12 * n, rS, rT) == 3 * n for n in (-1, 0, 1, 2)),
    "a unit on any one line raises chi by 1": all(chi(Fr(3, 2), rS, rT, m) == 1 for m in ([1, 0, 0], [0, 1, 0], [0, 0, 1])),
    "the uniform unit is the weight twelve higher": chi(Fr(3, 2), rS, rT, [1, 1, 1]) == chi(Fr(27, 2), rS, rT) == 3,
    "the index at an empty Lambda+ is +3, 0, -3 at n = -1, 0, 1": [index(n) for n in (-1, 0, 1)] == [3, 0, -3],
    "the index with a unit on one line is -1": -chi(Fr(3, 2), rS, rT, [1, 0, 0]) == -1,
    "this recomputation agrees with B1641's sealed table": agree,
    "PLANTED: the defining term's sign reversed disagrees with the sealed table": not planted,
}
out["all_hold"] = all(out["checks"].values())
json.dump(out, open(sys.argv[1], "w"), indent=1)
print(json.dumps(out["checks"], indent=1)); print(json.dumps(res)); print(out["index_empty_Lambda_plus"])
