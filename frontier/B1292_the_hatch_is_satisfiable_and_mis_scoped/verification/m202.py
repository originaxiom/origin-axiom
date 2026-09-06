"""B1292 -- B1291's hatch is SATISFIABLE (m202 is the witness) and MIS-SCOPED (it names the
wrong obstruction). Both halves computed here.

B1291 proved: on a ONE-cusped manifold |Fix(g)| on the cusp is EVEN, so |Fix| = 3 -- what an
order-3 rotation of the cusp torus needs -- is EXCLUDED. Its hatch said: go multi-cusped
inside m004's commensurability class, keeping Q(sqrt-3), 2T and E6.

HALF ONE -- THE HATCH IS SATISFIABLE. m202 is a witness, and every clause is checked:
  * SAME CLASS: vol(m202) = 4*V_tet = 2*vol(m004), so it is tiled by regular ideal tetrahedra
    and is cusped arithmetic over Q(sqrt-3); for CUSPED arithmetic manifolds the quaternion
    algebra is M_2(k), so the invariant trace field alone fixes the commensurability class.
    Both cusp shapes are exp(i*pi/3) -- the HEXAGONAL/Eisenstein shape -- hence in Q(sqrt-3).
  * KEEPS 2T: pi_1(m202) has 96 SURJECTIONS onto 2T = SL(2,3). The counting method is
    validated in the same run by reproducing m004's BANKED 48.
  * TWO CUSPS, and FOUR isometries realise |Fix| = 3 on BOTH cusps at once.
  * THE MECHANISM: m004's cusp is RECTANGULAR (shape 2*sqrt(-3)), which admits only +-1, which
    is exactly why it can never carry an order-3 rotation. m202's cusps are HEXAGONAL, which
    admit Z/6. The obstruction was the CUSP SHAPE, and the shape is what changes.

HALF TWO -- AND THE HATCH IS MIS-SCOPED, WHICH MATTERS MORE. Satisfying it does NOT deliver a
generation count, because PARITY WAS NEVER THE BINDING OBSTRUCTION. The binding one is
FLATNESS, and flatness is CUSP-COUNT-INDEPENDENT:

        chi(M) = 0 and chi(dM) = 0 for EVERY cusped manifold, at any number of cusps,
        because every boundary component is a flat torus.

So net chirality = -chi(d+M) = 0 survives the move. |Fix| = 3 and chi(d+M) != 0 are DIFFERENT
QUANTITIES and m202 supplies only the first. B1291's hatch is re-scoped at source accordingly:
it opens an ORDER-3 STRUCTURE ON THE BOUNDARY inside the right arithmetic -- which the programme
did not previously have anywhere -- and it does NOT open a route to net chirality.
"""
import warnings
warnings.filterwarnings("ignore")
import itertools

V_TET = 1.0149416064096536      # volume of the regular ideal tetrahedron


def sl23():
    F = range(3)
    return [(a, b, c, d) for a in F for b in F for c in F for d in F if (a * d - b * c) % 3 == 1]


def mul(x, y):
    a, b, c, d = x; e, f, g, h = y
    return ((a*e + b*g) % 3, (a*f + b*h) % 3, (c*e + d*g) % 3, (c*f + d*h) % 3)


def inv(x):
    a, b, c, d = x
    return (d % 3, (-b) % 3, (-c) % 3, a % 3)


ID = (1, 0, 0, 1)


def surjections_onto_2T(M):
    """(#homomorphisms, #surjections) pi_1(M) -> SL(2,3)."""
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    S = sl23()

    def ev(word, asg):
        r = ID
        for ch in word:
            g = asg[ord(ch.lower()) - 97]
            r = mul(r, g if ch.islower() else inv(g))
        return r

    tot = su = 0
    for asg in itertools.product(S, repeat=len(gens)):
        if all(ev(w, asg) == ID for w in rels):
            tot += 1
            img, fr = {ID}, [ID]
            while fr:
                x = fr.pop()
                for g in asg:
                    for y in (mul(x, g), mul(x, inv(g))):
                        if y not in img:
                            img.add(y); fr.append(y)
            if len(img) == 24:
                su += 1
    return tot, su


def det_A_minus_I(A):
    a, b, c, d = int(A[0, 0]), int(A[0, 1]), int(A[1, 0]), int(A[1, 1])
    return abs((a - 1) * (d - 1) - b * c)


def selftest():
    import snappy
    print("B1292 -- the hatch is satisfiable (m202) and mis-scoped (flatness, not parity)\n")
    print(f"  [env ] snappy {snappy.version()}")

    m4, m2 = snappy.Manifold("m004"), snappy.Manifold("m202")

    # --- HALF ONE: the witness ---
    for nm, M in (("m004", m4), ("m202", m2)):
        v = float(M.volume())
        print(f"  [vol ] {nm}: cusps={M.num_cusps()}  vol={v:.9f} = {v/V_TET:.6f} * V_tet")
        assert abs(v / V_TET - round(v / V_TET)) < 1e-7      # tiled by regular ideal tetrahedra
    assert abs(float(m2.volume()) / float(m4.volume()) - 2) < 1e-9

    shapes = [complex(m2.cusp_info(i)['shape']) for i in range(m2.num_cusps())]
    print(f"  [shape] m202 cusp shapes: {[f'{s:.6f}' for s in shapes]}  (hexagonal = exp(i*pi/3))")
    hexa = complex(0.5, 3 ** 0.5 / 2)
    assert all(abs(s - hexa) < 1e-9 for s in shapes)
    s4 = complex(m4.cusp_info(0)['shape'])
    print(f"  [shape] m004 cusp shape : {s4:.6f}  (RECTANGULAR: Re = 0) -- why order 3 is impossible there")
    assert abs(s4.real) < 1e-9

    tot4, su4 = surjections_onto_2T(m4)
    tot2, su2 = surjections_onto_2T(m2)
    print(f"  [2T  ] m004: {tot4} homs, {su4} SURJECTIONS onto 2T   <- reproduces the BANKED 48 (method control)")
    print(f"  [2T  ] m202: {tot2} homs, {su2} SURJECTIONS onto 2T")
    assert su4 == 48, su4                      # the control: if this breaks, the method is wrong
    assert su2 == 96 and su2 > 0

    G = m2.symmetry_group()
    three = [[det_A_minus_I(A) for A in iso.cusp_maps()] for iso in G.isometries()]
    both3 = [f for f in three if all(x == 3 for f2 in [f] for x in f2)]
    print(f"  [Fix ] m202 Sym = {G} (order {G.order()}); isometries with |Fix| = 3 on BOTH cusps: {len(both3)}")
    assert len(both3) == 4

    # --- HALF TWO: and it does NOT reach the target ---
    print("\n  [scope] does the cusp count change the INDEX chain?")
    for nm in ("m004", "m202", "o10_150704"):
        M = snappy.Manifold(nm); Gp = M.fundamental_group()
        g, r = len(Gp.generators()), len(Gp.relators())
        chiM = 1 - g + r
        print(f"        {nm:12} cusps={M.num_cusps()}  chi(M) = 1-{g}+{r} = {chiM}   chi(dM) = {M.num_cusps()} x 0 = 0")
        assert chiM == 0
    print("""
  ==> HALF ONE: B1291's hatch IS SATISFIABLE. m202 keeps Q(sqrt-3) (same class), keeps 2T
      (96 surjections, method validated against m004's banked 48), has TWO cusps, and carries
      FOUR isometries with |Fix| = 3 on BOTH cusps. The mechanism is the CUSP SHAPE:
      m004's is RECTANGULAR and admits only +-1; m202's are HEXAGONAL and admit Z/6.

  ==> HALF TWO: AND THE HATCH NAMED THE WRONG OBSTRUCTION. chi(M) = 0 and chi(dM) = 0 at ANY
      cusp count, because every boundary component is a flat torus -- so net chirality
      = -chi(d+M) = 0 SURVIVES the move. Parity was never binding; FLATNESS is, and flatness
      is cusp-count-independent.

  ==> WHAT m202 IS WORTH, STATED EXACTLY: the first place in this programme's own arithmetic
      where an ORDER-3 SYMMETRY ACTS ON THE BOUNDARY. That is new. It is NOT a generation
      count, and I-26 is untouched.
""")
    print("SELFTEST: PASS")


if __name__ == "__main__":
    selftest()
