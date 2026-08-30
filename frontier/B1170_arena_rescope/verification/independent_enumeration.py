"""B1170 independent re-derivation (cc, own code path): the B8143 step-4 enumeration.
Fraction Gaussian elimination for the linear system + explicit homogeneous-cubic analysis.
No sympy.solve. Expect: 252 examined, 222 killed by [SU(3)]^3, survivors = {AbbCD, aBBCD}
with charges prop. to (1/6,-2/3,1/3,-1/2,1)."""
import itertools
from fractions import Fraction as F
import numpy as np

REP = {"A": (6, +2, 2, 3), "a": (6, -2, 2, 3), "B": (3, +1, 1, 0),
       "b": (3, -1, 1, 0), "C": (2, 0, 0, 1), "D": (1, 0, 0, 0)}  # st, a3, tri, dbl

def nullspace_frac(rows):
    """Exact nullspace basis of a matrix with Fraction entries (rows: list of 5-tuples)."""
    m = [list(map(F, r)) for r in rows]; ncol = 5; piv = []
    r = 0
    for c in range(ncol):
        p = next((i for i in range(r, len(m)) if m[i][c] != 0), None)
        if p is None: continue
        m[r], m[p] = m[p], m[r]
        m[r] = [x / m[r][c] for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c] != 0:
                m[i] = [a - m[i][c] * b for a, b in zip(m[i], m[r])]
        piv.append(c); r += 1
        if r == len(m): break
    free = [c for c in range(ncol) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncol; v[fc] = F(1)
        for ri, pc in enumerate(piv):
            v[pc] = -m[ri][fc]
        basis.append(v)
    return basis

def cubic_on(content, ys):
    return sum(F(REP[r][0]) * y**3 for r, y in zip(content, ys))

n_exam = n_su3 = 0; survivors = []
for c in itertools.combinations_with_replacement("AaBbCD", 5):
    n_exam += 1
    if sum(REP[r][1] for r in c) != 0: n_su3 += 1; continue          # [SU(3)]^3
    if sum(REP[r][3] for r in c) % 2 != 0: continue                   # Witten
    lin = [[REP[r][2] for r in c], [REP[r][3] for r in c], [REP[r][0] for r in c]]
    ns = nullspace_frac(lin)
    rays = []
    if len(ns) == 1:
        if cubic_on(c, ns[0]) == 0: rays.append(tuple(ns[0]))         # linears isolate; cubic must vanish
    elif len(ns) == 2:
        v1, v2 = ns
        # homogeneous cubic P(s,t) = cubic(s*v1 + t*v2): expand exactly
        coef = [F(0)] * 4  # s^3, s^2 t, s t^2, t^3
        for r, (a, b) in zip(c, zip(v1, v2)):
            st = F(REP[r][0])
            coef[0] += st * a**3; coef[1] += st * 3 * a**2 * b
            coef[2] += st * 3 * a * b**2; coef[3] += st * b**3
        if all(x == 0 for x in coef): continue                        # cubic vanishes identically -> 1-param family -> NOT rigid
        # roots of P(s,1)=0 (plus t=0 ray if coef[0]==0)
        if coef[0] == 0:
            rays.append(tuple(v1))
        cs = [float(coef[i]) for i in range(4)]
        for root in np.roots(cs[:1] + cs[1:]) if cs[0] != 0 else (np.roots(cs[1:]) if any(cs[1:]) else []):
            if abs(root.imag) > 1e-9: continue
            s = root.real
            ray = tuple(F(a) * 1 + 0 for a in v1)  # placeholder; build numerically then rationalize
            vec = [s * float(a) + float(b) for a, b in zip(v1, v2)]
            rays.append(("num", s, tuple(vec)))
    # else len(ns) >= 3: never rigid
    good = []
    for ray in rays:
        if ray and ray[0] == "num":
            _, s, vec = ray
            if any(abs(x) < 1e-9 for x in vec): continue              # sterile
            # rationalize: try s rational (rational-root theorem check) for exact verify
            from fractions import Fraction
            sr = Fraction(s).limit_denominator(10**6)
            v1_, v2_ = ns
            vec_exact = [sr * a + b for a, b in zip(v1_, v2_)]
            lin_ok = all(sum(F(REP[r][k]) * y for r, y in zip(c, vec_exact)) == 0 for k in (2, 3, 0))
            cub_ok = cubic_on(c, vec_exact) == 0
            if lin_ok and cub_ok and all(y != 0 for y in vec_exact):
                good.append(tuple(vec_exact))
            elif not any(abs(x) < 1e-9 for x in vec):
                good.append(("IRRATIONAL", tuple(round(x, 6) for x in vec)))  # count, flag
        elif ray:
            if all(y != 0 for y in ray): good.append(tuple(ray))
    if good:
        survivors.append(("".join(c), sum(REP[r][0] for r in c), good))

print(f"examined: {n_exam}   killed by [SU(3)]^3: {n_su3}")
print(f"survivors: {len(survivors)}")
for name, states, g in survivors:
    ex = g[0]
    if ex and ex[0] != "IRRATIONAL":
        norm = [y / ex[-1] for y in ex]  # normalize to Ye=1 (last slot D where present)
        print(f"  {name} ({states} states): charges/Ye -> {[str(x) for x in norm]}")
    else:
        print(f"  {name} ({states} states): {ex}")
assert n_exam == 252 and n_su3 == 222, "count mismatch with cc3"
names = {s[0] for s in survivors}
assert names == {"AbbCD", "aBBCD"}, f"survivor mismatch: {names}"
sm = [s for s in survivors if s[0] == "AbbCD"][0][2][0]
norm = [y / sm[-1] for y in sm]
assert sorted(norm) == sorted([F(1,6), F(-2,3), F(1,3), F(-1,2), F(1)]), f"charge mismatch: {norm}"  # multiset: the two b-slots are identical letters
print("\nINDEPENDENT RE-DERIVATION CONFIRMS: 252 examined, 222 su3-killed, exactly 2 survivors,")
print("AbbCD = the SM 15-plet with charges (1/6,-2/3,1/3,-1/2,1) up to scale + the conjugate. REPRODUCES")
