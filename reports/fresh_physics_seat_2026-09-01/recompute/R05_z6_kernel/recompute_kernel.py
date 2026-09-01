#!/usr/bin/env python3
"""R05 blind recomputation: kernel of Z(SU(3)) x Z(SU(2)) x U(1)_Y on SM content.

Written BEFORE opening any of the arc's verification scripts (global_form.py,
kernel_27.py, B1221/verification/, tests/). Spec taken only from the FINDINGS.md
of B862 / B1080 / B1221.

Conventions (mine, stated explicitly):
  - Element g = (a, b, t): a in Z3 (acts as omega^a on color 3, omega^{-a} on 3bar,
    trivially on 1 and 8), b in Z2 (acts as (-1)^b on isospin 2, trivially on 1 and 3),
    t in Q/Z representing the U(1)_Y phase e^{2*pi*i*t} on a field of integer
    hypercharge y = 6Y, acting as e^{2*pi*i*y*t}.
  - Trivial action on field (c, d, y):  c*a/3 + d*b/2 + y*t == 0 (mod 1),
    where c in {0, +1, -1} is color triality (3 -> +1, 3bar -> -1, 1/8 -> 0)
    and d in {0, 1} is isospin duality (2 -> 1, 1/3 -> 0).
  - All arithmetic exact (sympy Rational).

Two ambient choices computed for every content:
  (A) U(1) continuous (the honest circle). Kernel may be infinite when all y = 0.
  (B) U(1) restricted to 12th roots of unity, t = k/12 -- a finite-ambient variant
      kept because the banked control value 72 for adjoint-only content cannot be
      finite in ambient (A); diff against their convention afterwards.
"""
from fractions import Fraction
from itertools import product

# ---- field data: (colour, isospin, y=6Y, label) ; colour in {1,3,-3,8}, isospin in {1,2,3}
def F(c, d, y, lab):
    cmap = {1: 0, 3: 1, -3: -1, 8: 0}
    dmap = {1: 0, 2: 1, 3: 0}
    return (cmap[c], dmap[d], y, lab)

# SM 15-plet, banked hypercharges y = 6Y in (1, -4, 2, -3, 6)
SM15 = [
    F(3, 2, 1, "Q"),
    F(-3, 1, -4, "u^c"),
    F(-3, 1, 2, "d^c"),
    F(1, 2, -3, "L"),
    F(1, 1, 6, "e^c"),
]
NU = [F(1, 1, 0, "nu^c")]
SIXTEEN = SM15 + NU
TEN_OF_27 = [  # the 10 of SO(10) inside the 27: two doublets + colour triplet pair
    F(1, 2, 3, "H_u"),
    F(1, 2, -3, "H_d"),
    F(3, 1, -2, "T"),
    F(-3, 1, 2, "Tbar"),
]
SINGLET = [F(1, 1, 0, "s")]
TWENTYSEVEN = SIXTEEN + TEN_OF_27 + SINGLET

ADJOINT_ONLY = [F(8, 1, 0, "g"), F(1, 3, 0, "W"), F(1, 1, 0, "B")]
# "integer-charge content only": the fields with integer electric charges = the leptons
INTEGER_CHARGE = [F(1, 2, -3, "L"), F(1, 1, 6, "e^c"), F(1, 1, 0, "nu^c")]
NO_Q = [f for f in SM15 if f[3] != "Q"]


def kernel_continuous(content):
    """Exact kernel in Z3 x Z2 x U(1). Returns ('infinite', pairs) if a U(1) factor
    survives, else sorted list of (a, b, Fraction t)."""
    elems = []
    inf_pairs = []
    for a, b in product(range(3), range(2)):
        # constraints: y*t == -(c*a/3 + d*b/2) mod 1
        zero_ok = True
        tsets = None
        has_y = False
        for c, d, y, _ in content:
            off = Fraction(c * a, 3) + Fraction(d * b, 2)
            if y == 0:
                if off % 1 != 0:
                    zero_ok = False
                    break
            else:
                has_y = True
                r = (-off) % 1
                sols = {((r + j) / y) % 1 for j in range(abs(y))}
                tsets = sols if tsets is None else (tsets & sols)
                if not tsets:
                    break
        if not zero_ok:
            continue
        if not has_y:
            inf_pairs.append((a, b))
        elif tsets:
            elems += [(a, b, t) for t in sorted(tsets)]
    if inf_pairs:
        return ("infinite", inf_pairs, elems)
    return sorted(elems)


def kernel_mu12(content):
    """Kernel in the finite ambient Z3 x Z2 x mu_12 (t = k/12)."""
    out = []
    for a, b, k in product(range(3), range(2), range(12)):
        t = Fraction(k, 12)
        if all((Fraction(c * a, 3) + Fraction(d * b, 2) + y * t) % 1 == 0
               for c, d, y, _ in content):
            out.append((a, b, t))
    return sorted(out)


def group_structure(elems):
    """Check closure under the product in Z3 x Z2 x Q/Z, find element orders,
    report whether cyclic and list generators."""
    s = set(elems)
    for (a1, b1, t1), (a2, b2, t2) in product(elems, repeat=2):
        p = ((a1 + a2) % 3, (b1 + b2) % 2, (t1 + t2) % 1)
        if p not in s:
            return None
    n = len(elems)
    gens = []
    for g in elems:
        x, o = g, 1
        while x != (0, 0, Fraction(0)):
            x = ((x[0] + g[0]) % 3, (x[1] + g[1]) % 2, (x[2] + g[2]) % 1)
            o += 1
        if o == n:
            gens.append(g)
    return {"order": n, "cyclic": bool(gens), "generators": gens}


def show(name, content):
    print(f"--- {name} ---")
    ker = kernel_continuous(content)
    if isinstance(ker, tuple):
        _, pairs, extra = ker
        print(f"  continuous-U(1): INFINITE  (full U(1) circle survives for (a,b) in {pairs})")
    else:
        st = group_structure(ker)
        print(f"  continuous-U(1): |ker| = {len(ker)}, closed = {st is not None}, "
              f"cyclic = {st['cyclic'] if st else '?'}")
        print(f"    elements: {[(a, b, str(t)) for a, b, t in ker]}")
        if st and st["generators"]:
            print(f"    generators: {[(a, b, str(t)) for a, b, t in st['generators']]}")
    k12 = kernel_mu12(content)
    print(f"  mu_12 ambient:   |ker| = {len(k12)}")
    return ker, k12


results = {}
for name, content in [
    ("SM 15-plet (banked y = 1,-4,2,-3,6)", SM15),
    ("16 = 15-plet + nu^c", SIXTEEN),
    ("10 of the 27", TEN_OF_27),
    ("27 = 16 + 10 + 1", TWENTYSEVEN),
    ("adjoint-only (8,1,0)+(1,3,0)+(1,1,0)", ADJOINT_ONLY),
    ("integer-charge only (L, e^c, nu^c)", INTEGER_CHARGE),
    ("15-plet minus Q", NO_Q),
]:
    results[name] = show(name, content)

# --- generator check: (omega * 1_3, -1_2, zeta_6) = (a=1, b=1, t=1/6)
g = (1, 1, Fraction(1, 6))
ker15 = results["SM 15-plet (banked y = 1,-4,2,-3,6)"][0]
print("\nBanked generator (omega, -1, zeta_6) = (1,1,1/6) in kernel of 15-plet:",
      g in set(ker15))
st = group_structure(ker15)
print("15-plet kernel: order", st["order"], "cyclic", st["cyclic"],
      "; (1,1,1/6) generates:", g in st["generators"])

# --- planted-deviation controls: the instrument must be able to NOT find Z6 ---
print("\n=== planted controls (exclusion sanity) ===")
# 1. change e^c hypercharge 6 -> 5: kernel should not be Z6
plant1 = [f for f in SM15 if f[3] != "e^c"] + [F(1, 1, 5, "e^c'")]
k = kernel_continuous(plant1)
print("15-plet with y(e^c)=5:", "infinite" if isinstance(k, tuple) else f"|ker|={len(k)}")
# 2. drop u^c and d^c and e^c: only Q and L -> kernel should differ from Z6
plant2 = [F(3, 2, 1, "Q"), F(1, 2, -3, "L")]
k = kernel_continuous(plant2)
print("Q + L only:", "infinite" if isinstance(k, tuple) else f"|ker|={len(k)}")
# 3. vector-like exotic (3,1,1): breaks the Z6
plant3 = SM15 + [F(3, 1, 1, "X")]
k = kernel_continuous(plant3)
print("15-plet + exotic (3,1,y=1):", "infinite" if isinstance(k, tuple) else f"|ker|={len(k)}",
      [(a, b, str(t)) for a, b, t in k] if not isinstance(k, tuple) else "")
