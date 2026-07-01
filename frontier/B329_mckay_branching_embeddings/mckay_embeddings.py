"""B329 -- 27|_2T for BOTH natural embeddings: is Level 3 reachable? (Chat-1 handoff follow-on).

Attacks the residual of B327: does the arithmetic 2T -> E6 give n1 != n2 (light generations SPLIT,
"Level 3", computable hierarchy) or n1 = n2 (degenerate, "Level 4", commensurator gate)? We compute
27|_2T explicitly for the two natural/arithmetic embeddings, from a brute-force 2T character table.

RESULT (both verified):
  (a) PRINCIPAL (quaternionic 2T c SU(2) c E6): 27|_2T = 3.1 + 3.1' + 3.1'' + 6.3  -> n1 = n2 (=3).
      Factors through 2T/{+-1}=A4 (no spinors 2,2',2''); real character; -I acts trivially.
  (b) TRINIFICATION (complex 2T c SU(3) c E6 via 1'+2'): 27|_2T = 9.1 + 3.1' + 3.1'' + 3.2' + 3.2''
      -> n1 = n2 (=0).  Real character.
  => BOTH natural embeddings give n1 = n2 -> Level 4. Level 3 needs a non-self-conjugate 27|_2T,
     i.e. a chiral (non-sigma-stable) embedding, which neither candidate provides.

Non-vacuity witness: the SU(3) "3" alone restricts to 2T as 1'+2', which has a COMPLEX character
(-1 +- sqrt(3) i at the two order-3 classes). It is the E6 27's BALANCED 3/3bar trinification
pairing that restores reality -- so n1=n2 is a real obstruction, not a triviality.

Firewalled: decides which LEVEL the hierarchy lives at, not any mass value. Nothing to CLAIMS.
Standalone: needs only sympy.
"""
import sympy as sp
import itertools

OMEGA = sp.Rational(-1, 2) + sp.sqrt(3) / 2 * sp.I           # e^{2 pi i / 3}


# ---------- 2T = 24 Hurwitz unit quaternions; conjugacy classes ----------
def _qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def _qinv(a): return (a[0], -a[1], -a[2], -a[3])
def _order(g):
    p, one = g, (1, 0, 0, 0)
    for k in range(1, 13):
        if p == one: return k
        p = _qmul(p, g)


def two_T():
    h = sp.Rational(1, 2)
    elts = set()
    for p in itertools.permutations(range(4)):
        for s in (1, -1):
            v = [0, 0, 0, 0]; v[p[0]] = s; elts.add(tuple(v))
    for s in itertools.product((h, -h), repeat=4):
        elts.add(tuple(s))
    elts = list(elts); assert len(elts) == 24
    seen, classes = set(), []
    for g in elts:
        if g in seen: continue
        cl = set(_qmul(_qmul(t, g), _qinv(t)) for t in elts)
        classes.append(sorted(cl)); seen |= cl
    classes.sort(key=lambda c: (_order(c[0]), c[0][0]))
    return elts, classes


def character_table():
    """Return (reps, sizes, irreps) with irreps a dict name->character function on a quaternion."""
    elts, classes = two_T()
    reps = [c[0] for c in classes]; sizes = [len(c) for c in classes]
    Q8 = set(g for g in elts if all(c in (0, 1, -1) for c in g))
    def cr(g): return frozenset(_qmul(g, q) for q in Q8)
    g0 = next(g for g in elts if _order(g) == 3)
    cos_pow = {cr((1, 0, 0, 0)): 0}; gp = g0
    for k in (1, 2):
        cos_pow[cr(gp)] = k; gp = _qmul(gp, g0)
    chi_1p = lambda g: OMEGA ** cos_pow[cr(g)]
    chi_1pp = lambda g: sp.conjugate(OMEGA) ** cos_pow[cr(g)]
    chi_2 = lambda g: 2 * g[0]
    irreps = {'1': lambda g: sp.Integer(1), "1'": chi_1p, "1''": chi_1pp,
              '2': chi_2, "2'": lambda g: chi_2(g) * chi_1p(g),
              "2''": lambda g: chi_2(g) * chi_1pp(g), '3': lambda g: 4 * g[0]**2 - 1}
    return reps, sizes, irreps


def _decompose(chi_vals, reps, sizes, irreps):
    return {name: sp.simplify(sum(sizes[i] * chi_vals[i] * sp.conjugate(chi(reps[i]))
                                  for i in range(7)) / 24) for name, chi in irreps.items()}


def branch_principal():
    """27 = spin8 + spin4 + spin0 (principal SL(2), B327) restricted to 2T."""
    reps, sizes, irreps = character_table()
    chi27 = [sp.simplify(sum(sp.chebyshevu(2 * j, reps[i][0]) for j in (8, 4, 0)))
             for i in range(7)]
    dec = _decompose(chi27, reps, sizes, irreps)
    return {k: v for k, v in dec.items() if v != 0}, dec


def branch_trinification():
    """2T -> SU(3) via (1'+2'); 27 = (3,3b,1)+(1,3,3b)+(3b,1,3) restricted to 2T c SU(3)_A."""
    reps, sizes, irreps = character_table()
    c1p, c2p, c1pp, c2pp = irreps["1'"], irreps["2'"], irreps["1''"], irreps["2''"]
    chi27 = [sp.simplify(3 * (c1p(reps[i]) + c2p(reps[i])) + 9
                         + 3 * (c1pp(reps[i]) + c2pp(reps[i]))) for i in range(7)]
    dec = _decompose(chi27, reps, sizes, irreps)
    return {k: v for k, v in dec.items() if v != 0}, dec


def su3_three_is_complex():
    """Non-vacuity witness: the SU(3) '3'|_2T = 1'+2' has a complex (non-self-conjugate) character."""
    reps, sizes, irreps = character_table()
    c1p, c2p = irreps["1'"], irreps["2'"]
    vals = [sp.simplify(c1p(r) + c2p(r)) for r in reps]
    return vals, any(sp.simplify(v - sp.conjugate(v)) != 0 for v in vals)


def n1_n2(dec):
    return dec["1'"] - dec["2'"], dec["1''"] - dec["2''"]


if __name__ == "__main__":
    reps, sizes, irreps = character_table()
    ortho = all(sp.simplify(sum(sizes[i] * irreps[a](reps[i]) * sp.conjugate(irreps[b](reps[i]))
                                for i in range(7)) / 24) == (1 if a == b else 0)
                for a in irreps for b in irreps)
    print("2T character table orthonormal:", ortho, " sum dim^2 =",
          sum(int(irreps[k](reps[0]))**2 for k in irreps))
    pa, da = branch_principal(); nb = n1_n2(da)
    print("\n(a) principal      27|_2T =", pa, "  n1,n2 =", nb, " n1==n2:", sp.simplify(nb[0]-nb[1]) == 0)
    pb, db = branch_trinification(); nc = n1_n2(db)
    print("(b) trinification  27|_2T =", pb, "  n1,n2 =", nc, " n1==n2:", sp.simplify(nc[0]-nc[1]) == 0)
    vals, cplx = su3_three_is_complex()
    print("\nnon-vacuity: SU(3) 3|_2T char =", vals, " -> complex:", cplx)
    print("\n=> both natural embeddings give n1=n2 -> Level 4; Level 3 needs a chiral embedding.")
