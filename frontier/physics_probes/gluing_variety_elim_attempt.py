"""Phase 2 gold-standard: A-polynomial by symbolic elimination of the gluing variety, via
SEQUENTIAL RESULTANTS (eliminate shapes one at a time). Calibrate on figure-eight -> Cooper-Long,
then apply to m136. SnapPy gluing_equations(rect); edge rows imposed; cusp rows give hM,hL."""
import warnings; warnings.filterwarnings("ignore")
import sympy as sp
import snappy


def equations(name):
    Mfd = snappy.Manifold(name); n = Mfd.num_tetrahedra()
    ge = Mfd.gluing_equations(form="rect")
    z = sp.symbols(f"z0:{n}"); hM, hL = sp.symbols("hM hL")

    def parts(row):
        A, B, c = row; num, den = sp.Integer(1), sp.Integer(1)
        for i in range(n):
            for e, base in ((A[i], z[i]), (B[i], 1 - z[i])):
                if e > 0: num *= base**e
                elif e < 0: den *= base**(-e)
        return sp.expand(num), sp.expand(den), c

    eqs = []
    edges = ge[:-2]
    for row in edges[:-1]:                 # drop one redundant edge row (rank n-1, not n)
        num, den, c = parts(row); eqs.append(sp.expand(num - sp.Integer(-1)**int(c) * den))
    for row, h in ((ge[-2], hM), (ge[-1], hL)):
        num, den, c = parts(row); eqs.append(sp.expand(h * den - sp.Integer(-1)**int(c) * num))
    return eqs, list(z), hM, hL


def elim_resultants(name):
    eqs, z, hM, hL = equations(name)
    polys = eqs
    for zi in z:                          # eliminate shapes one at a time
        with_zi = [p for p in polys if zi in p.free_symbols]
        without = [p for p in polys if zi not in p.free_symbols]
        if len(with_zi) < 2:
            polys = without + with_zi; continue
        # pivot = lowest-degree-in-zi; take resultant with the rest
        with_zi.sort(key=lambda p: sp.degree(p, zi))
        piv = with_zi[0]; newp = []
        for p in with_zi[1:]:
            r = sp.resultant(piv, p, zi)
            if r != 0: newp.append(sp.expand(r))
        polys = without + newp
    # remaining polynomials in hM,hL only: take their gcd-content / the nontrivial factor
    polys = [sp.factor(p) for p in polys if p != 0 and (hM in p.free_symbols or hL in p.free_symbols)]
    return polys, hM, hL


def cooper_long(M, L): return M**4*L**2 + (-M**8 + M**6 + 2*M**4 + M**2 - 1)*L + M**4
def tracemap_m2(M, L): return M**2*L**2 - (M**4 - 4*M**2 + 1)*L + M**2
M, L = sp.symbols("M L")


def is_monomial_ratio(q):
    q = sp.cancel(q)
    if q == 0: return False
    nm, dn = sp.fraction(q)
    try:
        return len(sp.Poly(nm, M, L).monoms()) == 1 and len(sp.Poly(dn, M, L).monoms()) == 1
    except Exception:
        return False


def match(Aglue, targ, hM, hL, name):
    for am in (1, 2):
        for al in (1, 2):
            sub = sp.expand(Aglue.subs({hM: M**am, hL: L**al}))
            for fac, _ in sp.factor_list(sub)[1]:
                if not ({M, L} <= fac.free_symbols): continue
                if is_monomial_ratio(fac / targ(M, L)):
                    print(f"  [{name}] MATCH: A_glue factor == target up to unit "
                          f"{sp.cancel(fac/targ(M,L))}  (hM=M^{am}, hL=L^{al})")
                    return True
    return False


for name, targ, tname in [("4_1", cooper_long, "Cooper-Long"), ("m136", tracemap_m2, "m=2 eliminant")]:
    print(f"=== {name} (target: {tname}) ===")
    polys, hM, hL = elim_resultants(name)
    facs = []
    for p in polys:
        for fac, _ in sp.factor_list(p)[1]:
            if hM in fac.free_symbols and hL in fac.free_symbols and fac not in facs:
                facs.append(fac)
    print(f"  eliminant factors in (hM,hL): {len(facs)}")
    for fac in facs:
        print("    ", fac)
    found = any(match(fac, targ, hM, hL, name) for fac in facs)
    if not found: print("  (no monomial-unit match found among factors)")
    print()
