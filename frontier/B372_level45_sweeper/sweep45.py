"""B372 — the level-45 sweep, executed as pre-registered.

Stage 1 (HARD GATE): the identical pipeline at N=15 must reproduce the banked flagship
tr(Par·P0 Q4) and a second banked cell exactly. Stage 2: N=45 — full singles (m=1,2) and the
full (1,2) pair table, every nonzero cell identified exactly in the declared 12-dim basis
{1,c1,c2} (x) {1,sqrt5,sqrt-3,sqrt-15}, with held-out-embedding verification per prime and
CRT/rational reconstruction across primes.
"""
import json
import os
import sys
from fractions import Fraction as Fr
from math import gcd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fp_engine import (Level, basis_elements, primes_1_mod, primitive_root,
                       rational_reconstruct, _solve_mod)

HERE = os.path.dirname(os.path.abspath(__file__))


def gamma_and_reps(N):
    m = 4 * N
    if N == 15:
        G = [1, 19, 31, 49]
    else:
        G = [1, 19, 91, 109]
    seen, reps, held = {}, [], []
    nb = 4 if N == 15 else 12
    for k in range(1, m):
        if gcd(k, m) != 1:
            continue
        key = min(k * g % m for g in G)
        if key not in seen:
            seen[key] = k
            if len(reps) < nb:
                reps.append(k)
        elif len(held) < 2 and k not in reps:
            held.append(k)
        if len(reps) == nb and len(held) == 2:
            break
    return G, reps, held


def full_tables(N, p, zk, m1=1, m2=2):
    """One pipeline pass: singles for m1, m2 and the full pair DFT table, mod p."""
    L = Level(N, p, zk)
    W1, W2 = L.W(m1), L.W(m2)
    o1, pow1 = L.order_powers(W1)
    o2, pow2 = L.order_powers(W2)
    C = L.pair_cell_table(pow1, pow2)
    pair = {(a, b): L.dft_cell(C, o1, o2, a, b) for a in range(o1) for b in range(o2)}
    s1 = {a: L.single_cell(pow1, a) for a in range(o1)}
    s2 = {b: L.single_cell(pow2, b) for b in range(o2)}
    return o1, o2, pair, s1, s2


def run_level(N, primes, m1=1, m2=2):
    G, reps, held = gamma_and_reps(N)
    nb = len(reps)
    per_prime = []
    for p in primes:
        g = primitive_root(p)
        z0 = pow(g, (p - 1) // (4 * N), p)
        inv4 = pow(len(G), p - 2, p)
        data = {}                     # k -> Gamma-averaged tables
        Bs = {}
        for k in reps + held:
            acc_pair, acc_s1, acc_s2 = None, None, None
            for gam in G:
                kk = (k * gam) % (4 * N)
                o1, o2, pair, s1, s2 = full_tables(N, p, pow(z0, kk, p), m1, m2)
                if acc_pair is None:
                    acc_pair = dict(pair)
                    acc_s1, acc_s2 = dict(s1), dict(s2)
                else:
                    for key in acc_pair:
                        acc_pair[key] = (acc_pair[key] + pair[key]) % p
                    for key in acc_s1:
                        acc_s1[key] = (acc_s1[key] + s1[key]) % p
                    for key in acc_s2:
                        acc_s2[key] = (acc_s2[key] + s2[key]) % p
            data[k] = ({key: v * inv4 % p for key, v in acc_pair.items()},
                       {key: v * inv4 % p for key, v in acc_s1.items()},
                       {key: v * inv4 % p for key, v in acc_s2.items()})
            Bs[k] = basis_elements(N, p, pow(z0, k, p))
        per_prime.append((p, data, Bs))

    def identify(get):
        """get(tables) -> value mod p; solve across reps, verify held-outs, CRT."""
        sols, M = [], 1
        for p, data, Bs in per_prime:
            A = [Bs[k] for k in reps]
            y = [get(data[k]) for k in reps]
            x = _solve_mod(A, y, p)
            for k in held:
                if sum(xi * bi for xi, bi in zip(x, Bs[k])) % p != get(data[k]):
                    return None
            sols.append((p, x))
            M *= p
        out = []
        for i in range(nb):
            r = 0
            for p, x in sols:
                Mi = M // p
                r = (r + x[i] * Mi * pow(Mi, p - 2, p)) % M
            f = rational_reconstruct(r, M)
            if f is None:
                return None
            out.append(f)
        return out

    o1, o2 = (20, 12) if N == 15 else (60, 12)
    result = {"pair": {}, "singles1": {}, "singles2": {}, "failures": []}
    for a in range(o1):
        for b in range(o2):
            v = identify(lambda t, a=a, b=b: t[0][(a, b)])
            if v is None:
                result["failures"].append(f"pair({a},{b})")
            elif any(x != 0 for x in v):
                result["pair"][f"{a},{b}"] = [str(x) for x in v]
    for a in range(o1):
        v = identify(lambda t, a=a: t[1][a])
        if v is None:
            result["failures"].append(f"s1({a})")
        elif any(x != 0 for x in v):
            result["singles1"][str(a)] = [str(x) for x in v]
    for b in range(o2):
        v = identify(lambda t, b=b: t[2][b])
        if v is None:
            result["failures"].append(f"s2({b})")
        elif any(x != 0 for x in v):
            result["singles2"][str(b)] = [str(x) for x in v]
    return result


def main():
    primes = primes_1_mod(720, 3)
    # ---- stage 1: the hard gate at N=15 ----
    r15 = run_level(15, primes)
    banked = json.load(open(os.path.join(HERE, "..", "B367_value_map", "step0_tables.json")))["1,2"]
    gate = (r15["pair"].get("0,4") == banked["0,4"]
            and r15["pair"].get("0,8") == banked["0,8"]
            and not r15["failures"])
    print(f"GATE (N=15 reproduces banked flagship cells): {gate}", flush=True)
    if not gate:
        print("  got (0,4):", r15["pair"].get("0,4"), " banked:", banked["0,4"])
        print("  got (0,8):", r15["pair"].get("0,8"), " banked:", banked["0,8"])
        print("  failures:", r15["failures"][:5])
        raise SystemExit("gate failed — no level-45 number is read")
    # ---- stage 2: N=45 ----
    r45 = run_level(45, primes)
    with open(os.path.join(HERE, "sweep45.json"), "w") as fh:
        json.dump(r45, fh, indent=1)

    def comp_nonzero(vecs, idxs):
        return sum(1 for v in vecs.values() if any(Fr(v[i]) != 0 for i in idxs))

    imag_idx = [i for i in range(12) if i % 4 in (2, 3)]      # sqrt-3, sqrt-15 slots
    q1 = comp_nonzero(r45["singles1"], imag_idx) + comp_nonzero(r45["singles2"], imag_idx)
    q2 = comp_nonzero(r45["pair"], imag_idx)
    print(f"N=45: nonzero pair cells {len(r45['pair'])}, singles1 {len(r45['singles1'])}, "
          f"singles2 {len(r45['singles2'])}, failures {len(r45['failures'])}", flush=True)
    print(f"Q1 singles with imaginary components: {q1}  (null: 0 — the wall)")
    print(f"Q2 pair cells with imaginary components: {q2}  "
          f"(pre-registered null: 0 = the seam does NOT persist; alternative: >0 = it does)")


if __name__ == "__main__":
    main()
