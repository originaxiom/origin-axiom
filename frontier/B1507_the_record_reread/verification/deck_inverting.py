"""B1507 -- the deck-inverting isometry of s961 (B1391's named target, OPEN_LEADS 'the next target toward three'), with SnapPy.

s961 -> m004 is the only cyclic 3-fold cover (B1371, B1506).  Its deck Z/3 is H_1(m004)/3, so a lift of an isometry f of m004
conjugates the deck generator tau to tau^(f_*), where f_* = +-1 is f's action on H_1(m004) = Z<meridian>.  Checked here:
  (1) the eight isometries of m004 (D4) on the cusp's (meridian, longitude): four negate the meridian, two of them orientation-
      preserving;
  (2) Isom(s961): order 24 = 8 x 3 (every isometry is a lift), nonabelian, centre Z/2, abelianization (Z/2)^2 (B335's record);
  (3) from SnapPy's multiplication table: exactly two elements of order 3, both acting on the cusp homology trivially (the deck,
      a translation of the cusp), forming a normal subgroup; the elements that conjugate tau to tau^2, with their orientation and
      their action on the cusp's meridian.
Not computed here (an open outcome, to be sealed first): whether a deck-inverting isometry maps B1506's background orbits to
themselves, which is what would make each orbit carry S3's '2 + 1' (B1391)."""
import warnings
warnings.filterwarnings("ignore")
import snappy


def m004_isometries():
    M = snappy.Manifold('m004')
    G = M.symmetry_group()
    rows = []
    for iso in G.isometries():
        cm = iso.cusp_maps()[0]
        rows.append(dict(cusp_map=[list(map(int, r)) for r in cm], det=int(cm.det()), meridian=int(cm[0][0])))
    return M, G, rows


def s961_group():
    M = snappy.Manifold('m004')
    covers = [C for C in M.covers(3) if C.cover_info()['type'] == 'cyclic']
    C = covers[0]
    S = C.symmetry_group()
    n = S.order()
    isos = S.isometries()
    cms = [iso.cusp_maps()[0] for iso in isos]
    mult = [[S.multiply_elements(i, j) for j in range(n)] for i in range(n)]
    e = next(i for i in range(n) if all(mult[i][j] == j for j in range(n)))
    inv = [next(j for j in range(n) if mult[i][j] == e) for i in range(n)]

    def order(i):
        k, x = 1, i
        while x != e:
            x = mult[x][i]; k += 1
        return k
    orders = [order(i) for i in range(n)]
    three = [i for i in range(n) if orders[i] == 3]
    normal = all(mult[mult[g][t]][inv[g]] in three for g in range(n) for t in three)
    tau = three[0]
    inverting = [g for g in range(n) if mult[mult[g][tau]][inv[g]] == inv[tau]]
    return dict(
        identify=[str(x) for x in C.identify()], homology=str(C.homology()), cusps=C.num_cusps(),
        vol_ratio=round(float(C.volume() / M.volume()), 10), order=n, abelian=S.is_abelian(), dihedral=S.is_dihedral(),
        centre=str(S.center()), abelianization=str(S.abelianization()), amphicheiral=S.is_amphicheiral(),
        order_3=len(three), order_3_cusp_maps=[[list(map(int, r)) for r in cms[i]] for i in three], deck_normal=normal,
        inverting=len(inverting),
        inverting_orientation_preserving=sum(1 for g in inverting if int(cms[g].det()) == 1),
        inverting_meridian_signs=sorted({int(cms[g][0][0]) for g in inverting}),
        centralising=n - len(inverting))


if __name__ == "__main__":
    M, G, rows = m004_isometries()
    print(f"m004: Isom = {G} of order {G.order()}, amphicheiral {G.is_amphicheiral()}, invertible knot {G.is_invertible_knot()}")
    for r in rows:
        print(f"   cusp map {r['cusp_map']}  det {r['det']:+d}  meridian -> {r['meridian']:+d} meridian")
    neg = [r for r in rows if r['meridian'] == -1]
    print(f"   negate the meridian: {len(neg)} of {len(rows)}, orientation-preserving among them: {sum(r['det'] == 1 for r in neg)}")
    d = s961_group()
    for k, v in d.items():
        print(f"s961: {k} = {v}")
