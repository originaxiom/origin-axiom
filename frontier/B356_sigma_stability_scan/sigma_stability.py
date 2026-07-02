"""B356 -- the sigma-stability quick pair (campaign W1.2; H104 + the det-lemma; post-B329).

B329 closed the canonical 2T->E6 routes at Level 4 (both natural embeddings give n1=n2). This probe:
  (a) banks the one-line DET-LEMMA (twisted 2-dims have det != 1 => every SL(2,C)-factoring route
      forces the quaternionic 2) and the MOD-3-BLINDNESS note (2T's three 2-dims are Brauer-equal
      at p=3) -- pinning the "arithmetic route" questions B327 left;
  (b) states the FACTOR-ROUTE identities: every SU(2)-factoring, single-SU(3)-factor, or diagonal
      trinification embedding is sigma-stable for EVERY finite group (self-dual restriction);
  (c) runs the H104 chirality scan over {A4, S4, 2T, 2O, A5, 2I} at the character level: which
      groups admit ANY faithful 27-dim assembly with an invariant cubic (Sym^3 V)^G != 0 whose
      character is COMPLEX (non-self-dual) -- the necessary conditions for a chiral G -> E6.

METHOD (self-verifying, no transcribed tables): each group is built CONCRETELY (unit quaternions
for the binaries, permutations for A4/S4/A5) in float arithmetic (group combinatorics: closure,
classes, power maps -- exact as combinatorics, floats only label elements). Character tables are
DERIVED by decomposing tensor powers of a faithful seed character, then SNAPPED to exact algebraic
values (sympy nsimplify over {sqrt5, sqrt2, I, sqrt3}) and GATED exactly: row orthonormality,
sum(dim^2) = |G|, Frobenius-Schur indicators in {1,-1,0}. A failed gate raises (MB12: the checks
can fail). The scan itself runs in floats off the exact table (values <= 27^3, k <= 9 classes;
integer gates at 1e-6). Firewalled; nothing to CLAIMS; no physics claim.
"""
import cmath
import itertools
import math

import sympy as sp

PHI = (1 + 5 ** 0.5) / 2


# ---------------------------------------------------------------- concrete groups -----------------
def _qmul(a, b):
    return (a[0]*b[0]-a[1]*b[1]-a[2]*b[2]-a[3]*b[3],
            a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
            a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],
            a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0])


def _key(x):
    return tuple(round(v, 9) for v in x)


def elements(name):
    if name in ("A4", "S4", "A5"):
        n = 4 if name in ("A4", "S4") else 5
        perms = list(itertools.permutations(range(n)))
        if name in ("A4", "A5"):
            def sign(p):
                s = 1
                for i in range(len(p)):
                    for j in range(i+1, len(p)):
                        if p[i] > p[j]:
                            s = -s
                return s
            perms = [p for p in perms if sign(p) == 1]
        mul = lambda a, b: tuple(a[b[i]] for i in range(len(a)))
        inv = lambda p: tuple(sorted(range(len(p)), key=lambda i: p[i]))
        one = tuple(range(n))
        return perms, mul, inv, one
    gens = {
        "2T": [(0.5, 0.5, 0.5, 0.5), (0.0, 1.0, 0.0, 0.0)],
        "2O": [(0.5, 0.5, 0.5, 0.5), (2**-0.5, 2**-0.5, 0.0, 0.0)],
        "2I": [(0.5, 0.5, 0.5, 0.5), (PHI/2, (PHI-1)/2, 0.5, 0.0)],
    }[name]
    one = (1.0, 0.0, 0.0, 0.0)
    seen = {_key(one): one}
    frontier = [one]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                p = _qmul(g, h)
                if _key(p) not in seen:
                    seen[_key(p)] = p
                    nxt.append(p)
        frontier = nxt
    G = list(seen.values())
    mul = _qmul
    inv = lambda a: (a[0], -a[1], -a[2], -a[3])
    return G, mul, inv, one


def group_data(name):
    G, mul, inv, one = elements(name)
    idx = {_key(g) if name in ("2T", "2O", "2I") else g: i for i, g in enumerate(G)}
    key = (lambda g: _key(g)) if name in ("2T", "2O", "2I") else (lambda g: g)
    n = len(G)
    unassigned = set(range(n))
    classes, class_of = [], [None]*n
    while unassigned:
        i = min(unassigned)
        orbit = set()
        for h in G:
            c = mul(mul(h, G[i]), inv(h))
            orbit.add(idx[key(c)])
        for j in orbit:
            class_of[j] = len(classes)
            unassigned.discard(j)
        classes.append(sorted(orbit))

    def pmap(kpow):
        out = []
        for cl in classes:
            p = one
            for _ in range(kpow):
                p = mul(p, G[cl[0]])
            out.append(class_of[idx[key(p)]])
        return out
    return dict(name=name, G=G, idx=idx, key=key, classes=classes, class_of=class_of,
                one_class=class_of[idx[key(one)]], p2=pmap(2), p3=pmap(3), n=n,
                mul=mul, inv=inv)


# ------------------------------------------------- derived + snapped character tables -------------
def _one_dims(gd):
    """The 1-dim characters, concretely: G/[G,G] is cyclic (<=3) for all six groups; label cosets
    by a generator's power and read off exp(2 pi i jk/q)."""
    G, mul, inv = gd["G"], gd["mul"], gd["inv"]
    idx, key, classes = gd["idx"], gd["key"], gd["classes"]
    n = len(G)
    comms = {key(mul(mul(a, b), mul(inv(a), inv(b)))) for a in G for b in G}
    D = _set_closure(comms, gd)                                   # [G,G] as a set of keys
    q = n // len(D)
    if q == 1:
        return []
    # coset labels: k(g) = min power of a generating coset
    def coset(gk):
        return frozenset(key(mul(G[idx[gk]], G[idx[d]])) for d in list(D)[:1]) if False else None
    # simpler: label each element by which coset it is in, via BFS on coset reps
    label = {}
    for d in D:
        label[d] = 0
    g0 = next(key(g) for g in G if key(g) not in D)               # a generator of the cyclic quotient
    cur = {d: 0 for d in D}
    rep = g0
    kpow = 1
    while len(cur) < n:
        for d in D:
            cur[key(mul(G[idx[rep]], G[idx[d]]))] = kpow
        rep = key(mul(G[idx[rep]], G[idx[g0]]))
        kpow += 1
    out = []
    for j in range(1, q):
        chi = []
        for cl in classes:
            kk = cur[key(G[cl[0]])]
            chi.append(cmath.exp(2j*cmath.pi*j*kk/q))
        out.append(chi)
    return out


def _set_closure(seed_keys, gd):
    G, mul, idx, key = gd["G"], gd["mul"], gd["idx"], gd["key"]
    seen = set(seed_keys)
    frontier = list(seed_keys)
    while frontier:
        nxt = []
        for a in frontier:
            for b in list(seen):
                p = key(mul(G[idx[a]], G[idx[b]]))
                if p not in seen:
                    seen.add(p)
                    nxt.append(p)
        frontier = nxt
    return seen


def character_table(gd):
    name, G, classes, n = gd["name"], gd["G"], gd["classes"], gd["n"]
    k = len(classes)
    sizes = [len(c) for c in classes]

    def inner(f, h):
        return sum(sizes[c]*f[c]*h[c].conjugate() for c in range(k))/n

    if name in ("2T", "2O", "2I"):
        seed = [complex(2*G[cl[0]][0]) for cl in classes]                 # tr(SU(2) matrix) = 2a
    else:
        deg = len(G[0])
        seed = [complex(sum(1 for i in range(deg) if G[cl[0]][i] == i)) for cl in classes]
    seeds2 = []
    if name == "A5":
        # the Galois pair 3/3' cannot be separated by RATIONAL class functions (perm characters);
        # inject the icosahedral character chi_3 = [3,-1,0,phi,1-phi] by element order (the
        # phi <-> 1-phi assignment ambiguity is the Galois swap = a table automorphism; every
        # downstream verdict is swap-invariant, and the exact orthogonality gate validates it).
        mul, one = gd["mul"], gd["G"][gd["classes"][gd["one_class"]][0]]
        phi_seen = False
        chi3 = []
        for cl in classes:
            g = G[cl[0]]
            p, o = g, 1
            while p != one:
                p, o = mul(p, g), o + 1
            if o == 1:
                chi3.append(complex(3))
            elif o == 2:
                chi3.append(complex(-1))
            elif o == 3:
                chi3.append(complex(0))
            else:
                chi3.append(complex(PHI if not phi_seen else 1 - PHI))
                phi_seen = True
        seeds2.append(chi3)
    irreps = [[complex(1)]*k] + _one_dims(gd)

    def peel(f):
        r = list(f)
        for chi in irreps:
            m = inner(r, chi)
            mi = round(m.real)
            if mi:
                r = [r[c] - mi*chi[c] for c in range(k)]
        return r

    def try_add(r):
        if abs(inner(r, r).real - 1) < 1e-6:
            if r[gd["one_class"]].real < 0:
                r = [-x for x in r]
            if all(max(abs(r[c]-chi[c]) for c in range(k)) > 1e-6 for chi in irreps):
                irreps.append(r)
                return True
        return False

    for _ in range(30):
        if sum(round(chi[gd["one_class"]].real)**2 for chi in irreps) == n:
            break
        cands = []
        power = list(seed)
        for _ in range(6):
            cands.append(list(power))
            power = [power[c]*seed[c] for c in range(k)]
        cands.extend(seeds2)
        for a in irreps:
            for b in irreps:
                cands.append([a[c]*b[c] for c in range(k)])
            cands.append([a[c]*seed[c] for c in range(k)])
            for s2 in seeds2:
                cands.append([a[c]*s2[c] for c in range(k)])
        for f in cands:
            try_add(peel(f))
    dims = [round(chi[gd["one_class"]].real) for chi in irreps]
    assert sum(d*d for d in dims) == n, (name, dims, "table derivation incomplete")

    # ---- snap to exact values (deterministic candidate lattice) and GATE exactly ----
    s5, s2, s3 = sp.sqrt(5), sp.sqrt(2), sp.sqrt(3)
    cands_exact = {}
    for a in range(-12, 13):
        cands_exact[a/2.0] = sp.Rational(a, 2)
        for b in range(-8, 9):
            if b:
                cands_exact[(a + b*5**0.5)/2.0] = (a + b*s5)/2
        if a:
            cands_exact[a*2**0.5/2.0] = a*s2/2
            cands_exact[a*3**0.5/2.0] = a*s3/2

    def _snap(x):
        best = min(cands_exact, key=lambda c: abs(c - x))
        assert abs(best - x) < 1e-6, ("snap failed", x)
        return cands_exact[best]

    exact = []
    for chi in irreps:
        exact.append([_snap(v.real) + sp.I*_snap(v.imag) for v in chi])

    def einner(f, h):
        return sp.simplify(sum(sizes[c]*f[c]*sp.conjugate(h[c]) for c in range(k))/n)

    for i in range(len(exact)):                                  # exact orthonormality gate
        for j in range(i, len(exact)):
            v = einner(exact[i], exact[j])
            assert sp.simplify(v - (1 if i == j else 0)) == 0, (name, i, j, v)
    fs = []
    for chi in exact:                                            # exact Frobenius-Schur gate
        v = sp.simplify(sum(sizes[c]*chi[gd["p2"][c]] for c in range(k))/n)
        assert v in (1, -1, 0), (name, v)
        fs.append(int(v))
    return dict(sizes=sizes, irreps=exact, dims=dims, fs=fs, einner=einner)


# --------------------------------------------------------------- the deliverables -----------------
def det_lemma(gd, ct):
    """det-character of each 2-dim irrep: delta(c) = (chi(c)^2 - chi(c^2))/2. SL(2)-admissible iff
    delta == 1: twisted 2-dims are NOT SL(2)-reps, so every SL(2,C)-factoring route (holonomy,
    quaternion units) forces a quaternionic/self-dual 2."""
    out = {}
    k = len(ct["sizes"])
    for i, chi in enumerate(ct["irreps"]):
        if ct["dims"][i] != 2:
            continue
        det = [sp.simplify((chi[c]**2 - chi[gd["p2"][c]])/2) for c in range(k)]
        out[i] = dict(fs=ct["fs"][i], sl2_admissible=all(sp.simplify(d - 1) == 0 for d in det))
    return out


def mod3_blindness_2T():
    """2T's 2' = 2 (x) chi_omega and 2'' = 2 (x) chi_omega^2: their characters differ from chi_2 by
    factors omega^k, and omega^k - 1 = -(omega^k-1)... divisible by (1-omega) in Z[omega] =>
    identical Brauer characters at the prime over 3. Verified as exact divisibility."""
    w = sp.Rational(-1, 2) + sp.sqrt(3)*sp.I/2                    # omega, radical form
    q1 = sp.simplify((w - 1)/(1 - w))            # = -1
    q2 = sp.simplify((w**2 - 1)/(1 - w))         # = -(1+w)
    return sp.simplify(q1 + 1) == 0 and sp.simplify(sp.expand(q2 + 1 + w)) == 0


def h104_scan(name, gd=None, ct=None, max_report=4):
    """Enumerate all faithful 27-dim assemblies with (Sym^3 V)^G != 0; count complex ones.
    For all-real-character groups the enumeration is SKIPPED: complex = 0 is a THEOREM
    (every assembly is self-dual when every irreducible character is real)."""
    gd = gd or group_data(name)
    ct = ct or character_table(gd)
    k = len(ct["sizes"])
    n, sizes, dims = gd["n"], ct["sizes"], ct["dims"]
    # float copies for the scan
    chis = [[complex(v) for v in chi] for chi in ct["irreps"]]
    kernels = [{c for c in range(k) if abs(chis[i][c] - dims[i]) < 1e-9} for i in range(len(chis))]
    conj_of = []
    for i in range(len(chis)):
        cc = [v.conjugate() for v in chis[i]]
        conj_of.append(next(j for j in range(len(chis))
                            if max(abs(cc[c]-chis[j][c]) for c in range(k)) < 1e-9))
    if all(conj_of[i] == i for i in range(len(chis))):
        return dict(group=name, order=n, dims=sorted(dims), all_chars_real=True,
                    assemblies=None, complex_assemblies=0, examples=[],
                    note="all characters real => every assembly self-dual (theorem); enumeration skipped")
    one_c = gd["one_class"]
    order = sorted(range(len(chis)), key=lambda i: -dims[i])
    res = dict(total=0, cx=0, ex=[])

    def sym3_ok(chiV):
        tot = 0
        for c in range(k):
            tot += sizes[c]*(chiV[c]**3 + 3*chiV[c]*chiV[gd["p2"][c]] + 2*chiV[gd["p3"][c]])/6
        m = tot/n
        assert abs(m.imag) < 1e-6 and abs(m.real - round(m.real)) < 1e-6, m
        return round(m.real) >= 1

    def rec(pos, remaining, mult):
        if remaining == 0:
            used = [i for i in range(len(chis)) if mult[i] > 0]
            ker = set(range(k))
            for i in used:
                ker &= kernels[i]
            if ker != {one_c}:
                return
            chiV = [sum(mult[i]*chis[i][c] for i in used) for c in range(k)]
            if not sym3_ok(chiV):
                return
            res["total"] += 1
            if any(mult[i] != mult[conj_of[i]] for i in range(len(chis))):
                res["cx"] += 1
                if len(res["ex"]) < max_report:
                    res["ex"].append(tuple(mult))
            return
        if pos == len(order):
            return
        i = order[pos]
        for m in range(remaining // dims[i], -1, -1):
            mult[i] = m
            rec(pos + 1, remaining - m*dims[i], mult)
        mult[i] = 0

    rec(0, 27, [0]*len(chis))
    return dict(group=name, order=n, dims=sorted(dims),
                all_chars_real=all(conj_of[i] == i for i in range(len(chis))),
                assemblies=res["total"], complex_assemblies=res["cx"], examples=res["ex"])


def run_group(name):
    gd = group_data(name)
    ct = character_table(gd)
    return dict(det=det_lemma(gd, ct), scan=h104_scan(name, gd, ct), fs=ct["fs"], dims=ct["dims"])


if __name__ == "__main__":
    print("mod-3 blindness (2T):", mod3_blindness_2T())
    for g in ("A4", "S4", "2T", "2O", "A5", "2I"):
        r = run_group(g)
        sc = r["scan"]
        print(f"== {g} (|G|={sc['order']}, dims {sc['dims']}) ==")
        for i, d in r["det"].items():
            print(f"   2-dim #{i}: FS={d['fs']}  SL(2)-admissible={d['sl2_admissible']}")
        print(f"   all chars real: {sc['all_chars_real']} | 27-assemblies: {sc['assemblies']} "
              f"| COMPLEX: {sc['complex_assemblies']} | ex: {sc['examples'][:2]}")
