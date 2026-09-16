#!/usr/bin/env python3
"""xB001 cell 1 - INDEPENDENT re-derivation of B1136's shape-field family and separator table.

Own code: own quadratic-shape-field test (2x3 rational nullspace on Re/Im of a*z^2+b*z+c=0),
own property table. Does NOT read B1136's json. Prints the family, the separator table, and
- the join this seat adds - the cusp-trivial character group H_1(M)/<peripheral> per member.
"""
import snappy, mpmath as mp
from fractions import Fraction

mp.mp.dps = 40

def quad_of(z, maxden=10**6):
    """integers (a,b,c), gcd 1, a>0, with a z^2 + b z + c = 0; None if z is not quadratic."""
    z = mp.mpc(z)
    # rows: Re and Im of (z^2, z, 1)
    r = [(z**2).real, z.real, mp.mpf(1)]
    i = [(z**2).imag, z.imag, mp.mpf(0)]
    # nullspace of the 2x3 real matrix by 2x2 cofactors
    a =  r[1]*i[2] - r[2]*i[1]
    b = -(r[0]*i[2] - r[2]*i[0])
    c =  r[0]*i[1] - r[1]*i[0]
    v = [a, b, c]
    m = max(abs(x) for x in v)
    if m == 0:
        return None
    v = [x/m for x in v]
    fr = [Fraction(float(x)).limit_denominator(maxden) for x in v]
    den = 1
    for f in fr:
        den = den*f.denominator//__import__('math').gcd(den, f.denominator)
    ints = [int(f*den) for f in fr]
    g = 0
    for x in ints:
        g = __import__('math').gcd(g, abs(x))
    if g == 0:
        return None
    ints = [x//g for x in ints]
    if ints[0] < 0:
        ints = [-x for x in ints]
    A, B, C = ints
    if A == 0:
        return None
    # verify; snappy's default shapes carry ~1e-16, so the bar is set to 1e-11 and the
    # coefficients are additionally bounded so a spurious high-height fit cannot pass.
    if max(abs(A), abs(B), abs(C)) > 10**4:
        return None
    if abs(A*z**2 + B*z + C) > mp.mpf(10)**-11:
        return None
    return (A, B, C)

def squarefree(n):
    s, d = 1, 2
    m = abs(n)
    while d*d <= m:
        e = 0
        while m % d == 0:
            m //= d; e += 1
        if e % 2: s *= d
        d += 1
    s *= m
    return s if n > 0 else -s

def shape_field_disc(M):
    """squarefree discriminant shared by all tetrahedron shapes, or None if not all quadratic/equal."""
    discs = set()
    for z in M.tetrahedra_shapes('rect'):
        q = quad_of(complex(z))
        if q is None:
            return None
        A, B, C = q
        discs.add(squarefree(B*B - 4*A*C))
    return discs.pop() if len(discs) == 1 else None

def cusp_trivial_group(M):
    """invariant factors of H_1(M)/<image of peripheral subgroup>."""
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form
    G = M.fundamental_group()
    n = G.num_generators()
    def vec(w):
        v = [0]*n
        for ch in w:
            i = ord(ch.lower()) - ord('a')
            v[i] += 1 if ch.islower() else -1
        return v
    rows = [vec(r) for r in G.relators()]
    for cusp in G.peripheral_curves():
        for w in cusp:
            rows.append(vec(w))
    if not rows:
        return [0]*n
    S = smith_normal_form(Matrix(rows), domain=ZZ)
    d = [int(S[i, i]) for i in range(min(S.rows, S.cols))]
    free = n - len([x for x in d if x != 0])
    return sorted([abs(x) for x in d if abs(x) not in (0, 1)]) + [0]*free

def _cs_zero(M):
    try:
        return abs(float(M.chern_simons())) < 1e-9
    except Exception:
        return None


def main():
    fam = []
    for M in snappy.OrientableCuspedCensus():
        if M.num_tetrahedra() > 6:
            break
        if shape_field_disc(M) == -3:
            fam.append(M.name())
    print("shape-field family (all tetrahedron shapes in Q(sqrt-3)), <= 6 tetrahedra:")
    print(f"  {len(fam)} members: {fam}")
    B1136_FOURTEEN = ["m003","m004","m202","m203","m206","m207","m208","m410","m412",
                      "s118","s119","s594","s595","s596"]
    missed = [n for n in fam if n not in B1136_FOURTEEN]
    assert len(fam) == 21, f"expected 21 at <= 6 tetrahedra, got {len(fam)}"
    assert missed == ["s955","s956","s957","s958","s959","s960","s961"], missed
    print(f"  B1136 banked 14; its scan breaks at census index > 1200 and these {len(missed)}")
    print(f"  sit at indices 1256-1262, past the cutoff: {missed}")

    props = {}
    for nm in fam:
        M = snappy.Manifold(nm); G = M.symmetry_group()
        h1 = str(M.homology())
        props[nm] = dict(
            h1_is_Z = (h1 == "Z"),
            volume  = round(float(M.volume()), 10),
            tets    = M.num_tetrahedra(),
            cusps   = M.num_cusps(),
            torsion_free = ("/" not in h1),
            amphichiral  = bool(G.is_amphicheiral()),
            cs_zero = _cs_zero(M),
            h1 = h1,
            cusp_trivial = [x for x in cusp_trivial_group(M) if x != 0],
        )
    keys = ["h1_is_Z","volume","tets","cusps","torsion_free","amphichiral","cs_zero"]
    print("\nSEPARATOR TABLE (does the property hold for m004 and NO other family member?)")
    seps = []
    for k in keys:
        v4 = props["m004"][k]
        others = [n for n in fam if n != "m004" and props[n][k] == v4]
        sep = (len(others) == 0)
        if sep: seps.append(k)
        print(f"  {k:<14} m004={str(v4):<18} shared with {len(others):>2}  separates: {sep}")
    print(f"\nSEPARATORS = {seps}")
    assert seps == ["h1_is_Z"], f"expected exactly ['h1_is_Z'], got {seps}"
    print("EXACTLY ONE SEPARATOR: h1_is_Z  (m004 is a knot complement in S^3)")

    print("\nTHE JOIN (this seat): cusp-trivial character group H_1/<peripheral> per member")
    for nm in fam:
        p = props[nm]
        print(f"  {nm:<7} H1={p['h1']:<16} cusp-trivial={p['cusp_trivial'] if p['cusp_trivial'] else 'trivial'}")
    assert props["m004"]["cusp_trivial"] == [], "m004 must have trivial cusp-trivial group"
    print("\n  m004's cusp-trivial group is TRIVIAL - forced by H_1 = Z (the meridian generates).")
    import json, pathlib
    out = dict(family=fam, family_size=len(fam), separators=seps,
               b1136_family_size=14, b1136_missed=missed,
               cusp_trivial={n: props[n]["cusp_trivial"] for n in fam},
               h1={n: props[n]["h1"] for n in fam})
    pathlib.Path(__file__).with_name("xb002_results.json").write_text(json.dumps(out, indent=1))
    print("VERIFIED")

if __name__ == "__main__":
    main()
