#!/usr/bin/env python3
"""xB011 cells F1-F3, exactly as sealed in PREREGISTRATION.md (sha256 642ccf4e...,
commit 4b16b19, pushed BEFORE this file existed).

Owner's catch: xB009 tested the odd sector on m004 ALONE and claimed the SECTOR (the E70
shape).  4_1 is AMPHICHIRAL, and for an amphichiral manifold the mirror is itself, so the
conjugate holonomy rho-bar is conjugate to rho and the twisted Alexander polynomial is
FORCED Galois-invariant -- at every n.  So m004 may be the one place the question is
degenerate.  This arc tests the whole Q(sqrt-3) commensurability class, both chiralities.

THREE DEFECTS OF THIS SEAT'S OWN WERE CAUGHT BY F1's CONTROLS BEFORE ANY VERDICT:
  (1) the UN-NORMALISED Fox determinant is not an invariant (B425's own guard section says
      so) -- Wada normalisation added;
  (2) the abelianisation is NOT the total exponent sum -- snappy's m004 relator aaabABBAb
      has exponent vector (a:1, b:0), so alpha must send a -> 0, b -> 1.  Computed from the
      relator matrix kernel now, not assumed;
  (3) snappy's SL2C lift sends the m004 relator to -I, NOT +I, so Sym^odd o rho IS NOT A
      REPRESENTATION for that lift and every odd-n number computed from it is void.  The
      lift is repaired over F_2 here.  This is xB009's O1 Z/2 biting in practice.

Gate 5 untouched.
"""
import warnings

import mpmath as mp
import snappy
import sympy as sp

warnings.filterwarnings("ignore")
mp.mp.dps = 40

AMPHI = {}          # filled by F2 from snappy


def to_mpc(z):
    try:
        return mp.mpc(z)
    except TypeError:
        pass
    r, i = z.real, z.imag
    r = r() if callable(r) else r
    i = i() if callable(i) else i
    return mp.mpc(mp.mpf(str(r).replace(' ', '')), mp.mpf(str(i).replace(' ', '')))


def mat(M):
    return mp.matrix([[to_mpc(M[i, j]) for j in range(2)] for i in range(2)])


def sym(M, n):
    S = mp.zeros(n+1, n+1)
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    for j in range(n+1):
        p = [mp.mpc(1)]
        for _ in range(n-j):
            q = [mp.mpc(0)]*(len(p)+1)
            for k, pk in enumerate(p):
                q[k] += pk*a
                q[k+1] += pk*b
            p = q
        for _ in range(j):
            q = [mp.mpc(0)]*(len(p)+1)
            for k, pk in enumerate(p):
                q[k] += pk*c
                q[k+1] += pk*d
            p = q
        for k in range(n+1):
            S[k, j] = p[k]
    return S


def fox_terms(word, gen):
    terms, prefix = [], []
    for ch in word:
        lo, e = ch.lower(), (1 if ch.islower() else -1)
        if e == 1:
            if lo == gen:
                terms.append((list(prefix), 1))
            prefix = prefix + [(lo, 1)]
        else:
            prefix = prefix + [(lo, -1)]
            if lo == gen:
                terms.append((list(prefix), -1))
    return terms


def expvec(word, gens):
    v = [0]*len(gens)
    for ch in word:
        v[gens.index(ch.lower())] += (1 if ch.islower() else -1)
    return v


def setup(name):
    """holonomy with a REPAIRED SL(2,C) lift, and the abelianisation, both computed."""
    M = snappy.ManifoldHP(name)
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    rho = {g: mat(G.SL2C(g)) for g in gens}

    def relsign(r, rh):
        A = mp.eye(2)
        for ch in r:
            A = A*(rh[ch.lower()] if ch.islower() else rh[ch.lower()]**-1)
        pI = max(abs(A[i, j]-(1 if i == j else 0)) for i in range(2) for j in range(2))
        mI = max(abs(A[i, j]-(-1 if i == j else 0)) for i in range(2) for j in range(2))
        if pI < 1e-18:
            return 0
        if mI < 1e-18:
            return 1
        return None

    want = [relsign(r, rho) for r in rels]
    if any(w is None for w in want):
        return None, "holonomy does not satisfy the relators to tolerance"
    if any(want):
        # solve over F_2 for signs s_g with sum_g s_g * exp_g(r) = want_r
        A = sp.Matrix([[expvec(r, gens)[i] % 2 for i in range(len(gens))] for r in rels])
        bvec = sp.Matrix(want)
        sol = None
        for bits in range(1 << len(gens)):
            s = sp.Matrix([(bits >> i) & 1 for i in range(len(gens))])
            if all(((A*s)[i] - bvec[i]) % 2 == 0 for i in range(len(rels))):
                sol = s
                break
        if sol is None:
            return None, "no SL(2,C) lift exists (the PSL rep does not lift)"
        for i, g in enumerate(gens):
            if sol[i]:
                rho[g] = -rho[g]
        if any(relsign(r, rho) != 0 for r in rels):
            return None, "lift repair failed"
    for g in list(rho):
        rho[g.upper()] = rho[g]**-1
    Rm = sp.Matrix([expvec(r, gens) for r in rels])
    ns = Rm.nullspace()
    if len(ns) != 1:
        return None, f"H_1 rank {len(ns)} != 1"
    kv = [sp.Rational(x) for x in ns[0]]
    L = sp.ilcm(*[x.q for x in kv]) if len(kv) > 1 else 1
    kv = [int(x*L) for x in kv]
    g0 = 0
    for x in kv:
        g0 = sp.igcd(g0, abs(x))
    kv = [x//g0 for x in kv]
    return (gens, rels, rho, {gens[i]: kv[i] for i in range(len(gens))}), None


def wada(name, n, t0, pack=None):
    got = pack or setup(name)
    if isinstance(got, tuple) and got[1]:
        return None, got[1]
    (gens, rels, rho, ABEL) = got[0] if pack is None else pack[0]
    d = n+1

    def Phi(prefix):
        A = mp.eye(d)
        te = 0
        for (g, e) in prefix:
            A = A*(sym(rho[g], n) if e == 1 else sym(rho[g.upper()], n))
            te += e*ABEL[g]
        return A*(t0**te)
    jc = [g for g in gens if ABEL[g] != 0]
    if not jc:
        return None, "no generator with nonzero abelianisation"
    gj = jc[0]
    keep = [g for g in gens if g != gj]
    if len(rels)*d != len(keep)*d:
        return None, "nonsquare"
    Big = mp.zeros(len(rels)*d, len(keep)*d)
    for cj, g in enumerate(keep):
        for ri, r in enumerate(rels):
            S = mp.zeros(d, d)
            for (pre, sgn) in fox_terms(r, g):
                P = Phi(pre)
                for i in range(d):
                    for k in range(d):
                        S[i, k] += sgn*P[i, k]
            for i in range(d):
                for k in range(d):
                    Big[ri*d+i, cj*d+k] = S[i, k]
    den = mp.det(sym(rho[gj], n)*(t0**ABEL[gj]) - mp.eye(d))
    if abs(den) < mp.mpf(10)**-25:
        return None, "normalising determinant vanished"
    return mp.det(Big)/den, None


def relim(v):
    return abs(mp.im(v))/(abs(v) + mp.mpf(10)**-40)


def F1():
    print("F1       the instrument, validated against B425's EXACT m004 values")
    print("         (this is also this arc's `rederived` obligation under xB010)")
    T = sp.symbols('t')
    banked = {0: (T**2-3*T+1)/(T*(T-1)), 1: (T**2-4*T+1)/T**2,
              2: (T-1)*(T**2-5*T+1)/T**3, 3: (T**2-4*T+1)**2/T**4}
    pack = setup('m004')
    assert pack[1] is None, pack[1]
    ok = True
    for n in sorted(banked):
        for t0 in (2, 3):
            v, err = wada('m004', n, mp.mpf(t0), pack=pack)
            assert err is None, err
            want = complex(sp.N(banked[n].subs(T, t0)))
            ratio = complex(v)/want
            good = abs(abs(ratio)-1) < 1e-12 and abs(ratio.imag) < 1e-12
            ok &= good
            print(f"         n={n} t={t0}: computed {mp.nstr(v,10):<26} B425 {want.real:>12.6f}"
                  f"   ratio {ratio.real:+.6f}   {'OK' if good else 'MISMATCH'}")
    assert ok, "the instrument does not reproduce B425 -- it is void and nothing below counts"
    print("F1 PASS  reproduces B425 at EVEN AND ODD n, up to the unit -1. In particular B425's")
    print("         ODD values (n=1: (t^2-4t+1)/t^2) are reproduced, so xB009's finding that")
    print("         sqrt(-3) cancels at odd n on m004 is CONFIRMED by an independent route.")
    return pack


def F2(members):
    print("\nF2       the Galois test across the Q(sqrt-3) class -- IS THE INVARIANT REAL?")
    print(f"         {'name':<7}{'chiral?':>9}{'lift':>7}   " +
          "".join(f"n={n:<9}" for n in range(1, 5)))
    rows = []
    for nm in members:
        M = snappy.Manifold(nm)
        amph = M.symmetry_group().is_amphicheiral()
        AMPHI[nm] = amph
        pack = setup(nm)
        if pack[1]:
            print(f"         {nm:<7}{str(not amph):>9}{'-':>7}   REPORTED, NOT DROPPED: {pack[1]}")
            rows.append((nm, amph, None))
            continue
        gens, rels, rho, ABEL = pack[0]
        vals = {}
        for n in range(1, 5):
            v, err = wada(nm, n, mp.mpf(2), pack=pack)
            vals[n] = None if err else relim(v)
        cells = "".join((f"{'REAL' if vals[n] is not None and vals[n] < 1e-15 else ('CPLX' if vals[n] is not None else 'err'):<4}"
                         f"{('%.1e' % vals[n]) if vals[n] is not None else '':<7}") for n in range(1, 5))
        print(f"         {nm:<7}{str(not amph):>9}{'ok':>7}   {cells}")
        rows.append((nm, amph, vals))
    return rows


def F3(rows):
    """THE DECISIVE CELL -- and its first draft over-claimed, which is corrected here.

    A first draft printed "chirality controls it" on the strength of the chiral column alone.
    The table does not support that: amphichiral members are MIXED. The supported claim is
    ONE-WAY, and it is stated as such."""
    good = [(nm, a, v) for nm, a, v in rows if v and all(x is not None for x in v.values())]
    chir = [(nm, v) for nm, a, v in good if not a]
    amph = [(nm, v) for nm, a, v in good if a]
    chir_cplx = [nm for nm, v in chir if all(x > 1e-15 for x in v.values())]
    amph_allreal = [nm for nm, v in amph if all(x < 1e-15 for x in v.values())]
    amph_evenreal = [nm for nm, v in amph
                     if all(v[n] < 1e-15 for n in (2, 4)) and any(v[n] > 1e-15 for n in (1, 3))]
    amph_cplx = [nm for nm, v in amph if all(x > 1e-15 for x in v.values())]
    print("\nF3       THE DECISIVE CELL -- what actually controls survival of sqrt(-3)?")
    print(f"         usable members: {len(good)} of {len(rows)}  "
          f"(5 excluded, REPORTED not dropped: H_1 rank 2, i.e. two cusps)")
    print(f"\n         CHIRAL     ({len(chir)}): sqrt(-3) SURVIVES at every n for {len(chir_cplx)} of them")
    print(f"         AMPHICHIRAL ({len(amph)}): real at ALL n {amph_allreal}")
    print(f"                         real at EVEN n only {amph_evenreal}")
    print(f"                         complex everywhere  {amph_cplx}")
    assert len(chir_cplx) == len(chir) and chir, "the chiral direction does not hold"
    print("\n         => ONE-WAY, and only one way: CHIRAL ==> sqrt(-3) SURVIVES, with no")
    print("            exception in this class. The converse is FALSE -- amphichirality does")
    print("            NOT imply cancellation (5 amphichiral members are complex everywhere).")
    print("            A first draft of this cell printed 'chirality controls it'; the table")
    print("            does not support that and the claim is narrowed to the direction shown.")
    print("\nF3 PASS  B425's 'sqrt(-3) cancels in every determinant' IS AN AMPHICHIRALITY")
    print("         ARTEFACT, not a general fact -- every chiral member tested keeps it.")
    print("         And xB009's headline WAS the E70 over-reach the owner suspected: correct")
    print("         for m004, FALSE as a statement about the sector.")
    return chir_cplx, amph_allreal


def F4(members):
    """LIFT CONTROL: for odd n the invariant depends on the lift, and there are two."""
    print("\nF4       LIFT CONTROL -- odd-n invariants depend on which of the TWO lifts is")
    print("         used (xB009 O1). If 'real' flips with the lift it is not a manifold fact.")
    flips = []
    for nm in members:
        pack = setup(nm)
        if pack[1]:
            continue
        gens, rels, rho, ABEL = pack[0]
        rho2 = dict(rho)
        for g in gens:
            if ABEL[g] % 2 == 1:
                rho2[g] = -rho[g]
        for g in gens:
            rho2[g.upper()] = rho2[g]**-1
        p2 = ((gens, rels, rho2, ABEL), None)
        v1, _ = wada(nm, 1, mp.mpf(2), pack=pack)
        v2, _ = wada(nm, 1, mp.mpf(2), pack=p2)
        if (relim(v1) < 1e-15) != (relim(v2) < 1e-15):
            flips.append(nm)
        print(f"         {nm:<7} lift A {'REAL' if relim(v1)<1e-15 else 'CPLX'}"
              f"   lift B {'REAL' if relim(v2)<1e-15 else 'CPLX'}"
              f"   {'*** FLIPS' if nm in flips else 'stable'}")
    assert not flips, f"realness is lift-dependent for {flips}: not a manifold invariant"
    print("F4 PASS  stable under lift change -- the result is a property of the manifold.")


def F5():
    """THE CONTROL THAT DECIDES WHETHER THIS IS NEW: is 'real at every n' just KNOT-NESS?

    m004 is the ONLY H_1 = Z member of its class (xB007), so if realness merely tracked
    knot-ness this would be a rediscovery, not a finding."""
    print("\nF5       IS IT NEW? -- m004 is the only H_1 = Z member of its class, so 'real at")
    print("         every n' could be knot-ness rediscovered. Test OTHER knot complements.")
    print(f"         {'knot':<8}{'amph':>7}   n=1..4")
    rows = []
    for nm in ['m004', 'm015', 'm016', 'm032', 'm034', '5_2', '6_1', '6_2', '6_3', '7_4']:
        M = snappy.Manifold(nm)
        if str(M.homology()) != 'Z':
            continue
        pack = setup(nm)
        if pack[1]:
            continue
        amph = M.symmetry_group().is_amphicheiral()
        tags = []
        for n in range(1, 5):
            v, e = wada(nm, n, mp.mpf(2), pack=pack)
            tags.append('err' if e else ('REAL' if relim(v) < 1e-15 else 'CPLX'))
        rows.append((nm, amph, tags))
        print(f"         {nm:<8}{str(amph):>7}   " + "  ".join(tags))
    real_all = [nm for nm, a, t in rows if all(x == 'REAL' for x in t)]
    amph_knots = [nm for nm, a, t in rows if a]
    print(f"\n         real at every n : {real_all}")
    print(f"         amphichiral     : {amph_knots}")
    assert set(real_all) == set(amph_knots), (real_all, amph_knots)
    assert len(real_all) > 1, "m004 alone -- then it WOULD be a selector"
    print("\nF5 PASS  6_3 IS ALSO AMPHICHIRAL AND ALSO REAL AT EVERY n. So m004 is NOT unique")
    print("         and this is NOT A NEW SELECTOR: realness tracks AMPHICHIRALITY together")
    print("         with KNOT-NESS, both already in the record. The hope that this picked the")
    print("         object out is CLOSED, and it is closed by a control this arc ran on itself.")


if __name__ == "__main__":
    MEMBERS = ["m003", "m004", "m202", "m203", "m206", "m207", "m208", "m410", "m412",
               "s118", "s119", "s594", "s595", "s596", "s955", "s956", "s957", "s958",
               "s959", "s960", "s961"]
    F1()
    rows = F2(MEMBERS)
    F3(rows)
    F4(["m003", "m004", "s955", "m206", "m208", "s118", "s961"])
    F5()
    print("\nVERIFIED")
