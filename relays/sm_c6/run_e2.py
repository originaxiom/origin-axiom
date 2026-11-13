#!/usr/bin/env python3
"""SM-C6 E2 (second half): the F2-rank of the three named bits (c the mirror, X the exchange, O the pieces' order) on
the record's slope-built observables.  Card: relays/cards/SM_C6_E2_the-rank-of-the-three-bits.md (pushed first).
    python3 run_e2.py MAIN_CHECKOUT [out.json]"""
import sys, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
sys.argv = [sys.argv[0], sys.argv[1]] + sys.argv[2:]
sys.path.insert(0, str(HERE))
import run_e1 as E
from fractions import Fraction as Fr

LEVELS = [(eps, w, k) for eps in (1, -1) for (w, ks) in (("LR", range(1, 6)), ("LLR", range(1, 5)), ("LLLR", range(1, 4)))
          for k in ks]


def swap(w):
    return w.translate(str.maketrans("LR", "RL"))


def slope_keys(S):
    return [v for kk, v in S.items() if kk != (0, 0, 0)]


def same_up_to_shift(A, B, F, negate=False):
    """is the multiset B equal to {(-)a + n : a in A} for one integer n?"""
    if len(A) != len(B): return False
    A2 = [(F.const(0) - a) if negate else a for a in A]
    sa = A2[0].F.const(0); sb = A2[0].F.const(0)
    for a in A2: sa = sa + a
    for b in B: sb = sb + b
    diff = sb - sa
    if any(diff.c[1:]): return False
    n = Fr(diff.c[0]) / len(A)
    if n.denominator != 1: return False
    key = lambda v: str(v.c)
    return sorted(key(a + F.const(n)) for a in A2) == sorted(key(b) for b in B)


def main():
    out_path = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "e2_results.json"
    rows = []
    for eps, w, k in LEVELS:
        N, S, _ = E.level(eps, w, k)
        F = next(iter(v for kk, v in S.items() if kk != (0, 0, 0))).F if len(S) > 1 else None
        if F is None: continue
        mw = swap(w)
        Nm, Sm, _ = E.level(eps, mw, k)
        A, Bm = slope_keys(S), slope_keys(Sm)
        c_on_slopes = not (Nm == N and same_up_to_shift(A, Bm, F))          # c acts on (i) unless the multiset is kept
        c_is_negation = Nm == N and same_up_to_shift(A, Bm, F, negate=True)
        # P1: the reverse in place of the mirror
        Nr, Sr, _ = E.level(eps, w[::-1], k)
        p1_trivial = Nr == N and same_up_to_shift(A, slope_keys(Sr), F)
        B0 = E.based(S, N)
        c_on_counts = E.census(B0) != E.census(E.based(Sm, Nm))
        neg = lambda x: tuple((-a) % N for a in x)
        sub = lambda x, y: tuple((a - b) % N for a, b in zip(x, y))
        X_acts = O_acts = P2_acts = False; O_swaps = True
        for (l, a), (n, ns) in B0.items():
            bx = B0[(neg(l), neg(a))]                                         # X: conjugate
            if bx != (n, ns): X_acts = True
            beta = sub(a, l)
            bo = B0.get((neg(l), beta))                                       # O: V(l^-1, beta)
            if bo is not None:
                if bo != (ns, n): O_swaps = False
                if bo != (n, ns): O_acts = True
            bp = B0.get((neg(l), a))                                          # P2: l inverted, alpha kept
            if bp is not None and bp != (n, ns): P2_acts = True
        rows.append({"state": ("+" if eps > 0 else "-") + w, "mirror": ("+" if eps > 0 else "-") + mw, "level": k, "N": N,
                     "c_acts_on_slopes": c_on_slopes, "c_is_negation_up_to_shift": c_is_negation,
                     "c_acts_on_census": c_on_counts, "X_acts_on_counts": X_acts, "O_acts_on_counts": O_acts,
                     "O_swaps_n_and_nstar": O_swaps, "P1_reverse_trivial_on_slopes": p1_trivial, "P2_acts": P2_acts})
        print(rows[-1], flush=True)
    any_ = lambda key: any(r[key] for r in rows)
    acts = {"c": any_("c_acts_on_slopes") or any_("c_acts_on_census"), "X": any_("X_acts_on_counts"), "O": any_("O_acts_on_counts")}
    # c and O are distinct actions if one acts where the other does not (c on slopes, O on counts)
    rank = (1 if acts["c"] else 0) + (1 if acts["O"] else 0) + (1 if acts["X"] else 0)
    summary = {"levels": len(rows), "acts": acts, "rank_joint": rank,
               "c_on_counts_anywhere": any_("c_acts_on_census"), "c_negation_everywhere_chiral":
               all(r["c_is_negation_up_to_shift"] for r in rows),
               "O_swaps_everywhere": all(r["O_swaps_n_and_nstar"] for r in rows),
               "P1_reverse_trivial_on_every_level": all(r["P1_reverse_trivial_on_slopes"] for r in rows),
               "P2_acts_on_some_level": any_("P2_acts")}
    json.dump({"summary": summary, "rows": rows}, open(out_path, "w"), indent=1)
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()
