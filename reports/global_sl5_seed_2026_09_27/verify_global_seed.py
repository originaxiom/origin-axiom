"""Exact Q(zeta5) cohomology by restriction of scalars and FLINT rational ranks."""
import json
from functools import lru_cache
from itertools import combinations

from flint import fmpq_mat

from verify_topology import cover, data

DEGREE = 4


def zero(r, c):
    return fmpq_mat(r, c)


def eye(n):
    a = zero(n, n)
    for i in range(n):
        a[i, i] = 1
    return a


def hs(*matrices):
    r = matrices[0].nrows()
    out, offset = zero(r, sum(a.ncols() for a in matrices)), 0
    for a in matrices:
        assert a.nrows() == r
        for i in range(r):
            for j in range(a.ncols()):
                out[i, offset+j] = a[i, j]
        offset += a.ncols()
    return out


def vs(*matrices):
    return hs(*(a.transpose() for a in matrices)).transpose()


def blockdiag(*matrices):
    out = zero(sum(a.nrows() for a in matrices), sum(a.ncols() for a in matrices))
    row = column = 0
    for a in matrices:
        for i in range(a.nrows()):
            for j in range(a.ncols()):
                out[row+i, column+j] = a[i, j]
        row += a.nrows()
        column += a.ncols()
    return out


def kron(a, b):
    out = zero(a.nrows()*b.nrows(), a.ncols()*b.ncols())
    for i in range(a.nrows()):
        for j in range(a.ncols()):
            for k in range(b.nrows()):
                for l in range(b.ncols()):
                    out[i*b.nrows()+k, j*b.ncols()+l] = a[i, j]*b[k, l]
    return out


def submatrix(a, r0, r1, c0, c1):
    return fmpq_mat([[a[i, j] for j in range(c0, c1)] for i in range(r0, r1)])


def null_columns(a):
    reduced, rank = a.rref()
    pivots = [next(j for j in range(a.ncols()) if reduced[i, j]) for i in range(rank)]
    free = [j for j in range(a.ncols()) if j not in pivots]
    out = zero(a.ncols(), len(free))
    for col, fc in enumerate(free):
        out[fc, col] = 1
        for row, pc in enumerate(pivots):
            out[pc, col] = -reduced[row, fc]
    assert a*out == zero(a.nrows(), len(free))
    return out


def zeta5():
    return fmpq_mat([[0, 0, 0, -1], [1, 0, 0, -1], [0, 1, 0, -1], [0, 0, 1, -1]])


def field_matrix(coordinates):
    out, power, z = zero(4, 4), eye(4), zeta5()
    for c in coordinates:
        out += c*power
        power = power*z
    return out


def wedge_over_field(a):
    assert a.nrows() == a.ncols() and a.nrows() % DEGREE == 0
    n = a.nrows() // DEGREE
    blocks = [[submatrix(a, DEGREE*i, DEGREE*(i+1), DEGREE*j, DEGREE*(j+1))
               for j in range(n)] for i in range(n)]
    pairs = list(combinations(range(n), 2))
    return vs(*(hs(*(blocks[i][k]*blocks[j][l]-blocks[i][l]*blocks[j][k]
                     for k, l in pairs)) for i, j in pairs))


class Rep:
    def __init__(self, matrices):
        self.mats = matrices
        self.invs = [a.inv() for a in matrices]
        self.d = matrices[0].nrows()
        assert all(a.nrows() == a.ncols() == self.d for a in matrices)

    def word(self, w):
        out = eye(self.d)
        for x in w:
            out *= self.mats[x-1] if x > 0 else self.invs[-x-1]
        return out

    def fox(self, w, g):
        prefix, out = eye(self.d), zero(self.d, self.d)
        for x in w:
            if x > 0:
                if x == g:
                    out += prefix
                prefix *= self.mats[x-1]
            else:
                prefix *= self.invs[-x-1]
                if -x == g:
                    out -= prefix
        return out

    def dual(self):
        # Q-dual is isomorphic to restriction of the K-dual via trace pairing.
        return Rep([a.transpose() for a in self.invs])


def cohom(rep, n):
    rels, mu, lam = cover(n)
    d, ng = rep.d, len(rep.mats)
    assert ng == n+1 and d % DEGREE == 0
    identity = eye(d)
    assert all(rep.word(r) == identity for r in rels)
    d0 = vs(*(a-identity for a in rep.mats))
    d1 = vs(*(hs(*(rep.fox(r, g) for g in range(1, ng+1))) for r in rels))
    assert d1*d0 == zero(d1.nrows(), d0.ncols())
    cocycles = null_columns(d1)
    boundary = vs(rep.word(mu)-identity, rep.word(lam)-identity)
    boundary_d1 = hs(-(rep.word(lam)-identity), rep.word(mu)-identity)
    restriction = vs(*(hs(*(rep.fox(w, g) for g in range(1, ng+1))) for w in (mu, lam)))
    assert restriction*d0 == boundary
    assert boundary_d1*boundary == zero(d, d)
    assert boundary_d1*restriction*cocycles == zero(d, cocycles.ncols())
    r0, rb = d0.rank(), boundary.rank()
    r1 = hs(restriction*cocycles, boundary).rank()-rb
    raw = (d-r0, cocycles.ncols()-r0, d-rb, 2*d-boundary_d1.rank()-rb, r1)
    assert all(x % DEGREE == 0 for x in raw)
    return tuple(x//DEGREE for x in raw)


def indexed(rep, n):
    a, b = cohom(rep, n), cohom(rep.dual(), n)
    index = a[1]-a[4]-b[1]+b[4]
    assert a[4]+b[4] == a[3] == b[3]
    assert index == a[0]-b[0]+b[2]-a[4]
    return {"I": index, "V": a, "dual": b}


def plus(a, b, multiple=1):
    return tuple(x+multiple*y for x, y in zip(a, b))


def scalar_rep(q):
    z = zeta5()
    return Rep([z**((q*k) % 5) for k in data()["chi_exponents_mod5"]])


@lru_cache(None)
def native_doublet():
    chi = scalar_rep(1)
    squared = scalar_rep(2)
    rels, _, _ = cover(2)
    equations = vs(*(hs(*(squared.fox(r, g) for g in range(1, 4))) for r in rels))
    z = null_columns(equations)
    coboundary = vs(*(a-eye(4) for a in squared.mats))
    assert z.ncols()-coboundary.rank() == 4
    chosen = None
    for j in range(z.ncols()):
        candidate = submatrix(z, 0, 12, j, j+1)
        if hs(coboundary, candidate).rank() > coboundary.rank():
            chosen = candidate
            break
    assert chosen is not None
    coc = [field_matrix([chosen[4*i+j, 0] for j in range(4)]) for i in range(3)]
    scale = next(c for c in coc if c != zero(4, 4)).inv()
    coc = [c*scale for c in coc]
    rho = Rep([vs(hs(a, c*a.inv()), hs(zero(4, 4), a.inv())) for a, c in zip(chi.mats, coc)])
    assert all(rho.word(r) == eye(8) for r in rels)
    return rho


def twist(rep, q):
    return Rep([a*kron(eye(rep.d//4), scalar) for a, scalar in zip(rep.mats, scalar_rep(q).mats)])


def pullback(rep):
    return Rep([rep.word(w) for w in data()["M6_generators_in_M2"]])


def parent(q):
    p = fmpq_mat(data()["regular_C3"])
    rho = native_doublet()
    return twist(Rep([blockdiag(a, kron(p**k, eye(4)))
                      for a, k in zip(rho.mats, data()["M2_to_C3"])]), q)


def transfer_pair(rep):
    omega = fmpq_mat([[0, -1], [1, -1]])
    return Rep([kron(omega**k, a) for a, k in zip(rep.mats, data()["M2_to_C3"])])


@lru_cache(None)
def one_twist(q):
    e = parent(q)
    wedge = Rep([wedge_over_field(a) for a in e.mats])
    rho1, rho2 = indexed(pullback(twist(native_doublet(), q)), 6), indexed(pullback(twist(native_doublet(), 2*q)), 6)
    line1, line2 = indexed(pullback(scalar_rep(q)), 6), indexed(pullback(scalar_rep(2*q)), 6)
    assert line1["I"] == line2["I"] == 0
    out = {}
    for name, rep, rho_data, line_data, copies, lines in [
        ("E", e, rho1, line1, 1, 3), ("wedge2E", wedge, rho2, line2, 3, 4)
    ]:
        down, up, pair = indexed(rep, 2), indexed(pullback(rep), 6), indexed(transfer_pair(rep), 2)
        for side in ("V", "dual"):
            assert up[side] == tuple(copies*x+lines*y for x, y in zip(rho_data[side], line_data[side]))
            assert up[side] == plus(down[side], pair[side])
            assert all(x % 2 == 0 for x in pair[side])
        assert up["I"] == copies*rho_data["I"]
        assert pair["I"] % 2 == 0 and up["I"] == down["I"]+pair["I"]
        out[name] = {"down": down, "up": up, "paired_nontrivial_deck": pair,
                     "deck_indices": [down["I"], pair["I"]//2, pair["I"]//2]}
    assert out["E"]["deck_indices"][1:] == [0, 0]
    assert len(set(out["wedge2E"]["deck_indices"])) == 1
    return out


def mixed_control():
    p = fmpq_mat(data()["regular_C3"])
    rho = native_doublet()
    mixed = Rep([kron(p**k, a) for a, k in zip(rho.mats, data()["M2_to_C3"])])
    result = indexed(mixed, 2)
    assert result["V"] == result["dual"] == (0, 1, 1, 2, 1)
    result["restriction_profile"] = {"V": circle_restrictions(mixed, 2),
                                     "dual": circle_restrictions(mixed.dual(), 2)}
    return result


def circle_restrictions(rep, n):
    rels, mu, lam = cover(n)
    ng = len(rep.mats)
    d1 = vs(*(hs(*(rep.fox(r, g) for g in range(1, ng+1))) for r in rels))
    cocycles = null_columns(d1)
    a = cohom(rep, n)
    result = {"H1": a[1], "torus_rank": a[4], "torus_kernel": a[1]-a[4]}
    for name, word in (("meridian", mu), ("longitude", lam)):
        boundary = rep.word(word)-eye(rep.d)
        restriction = hs(*(rep.fox(word, g) for g in range(1, ng+1)))
        raw = hs(restriction*cocycles, boundary).rank()-boundary.rank()
        assert raw % DEGREE == 0
        rank = raw//DEGREE
        result[name+"_rank"] = rank
        result[name+"_kernel"] = a[1]-rank
        assert 0 <= rank <= a[1] and result[name+"_kernel"] >= result["torus_kernel"]
    return result


def main():
    import flint
    assert zeta5()**5 == eye(4) and zeta5() != eye(4)
    control = indexed(native_doublet(), 2)
    assert control["V"] == control["dual"] == (0, 1, 1, 2, 1)
    print("Native doublet and mixed control:", json.dumps({"doublet": control, "mixed": mixed_control()}), flush=True)
    rows = {}
    for q in data()["central_twists_mod5"]:
        rows[str(q)] = one_twist(q)
        print("TWIST", q, json.dumps(rows[str(q)]), flush=True)
    summary = {q: [r["E"]["up"]["I"], r["wedge2E"]["up"]["I"]] for q, r in rows.items()}
    print(json.dumps({"field": "Q(zeta5), exact rational restriction of scalars",
                      "flint_version": flint.__version__, "upstairs_index_pairs": summary,
                      "irreducible_candidate_constructed": False, "physical_chirality_derived": False}, indent=2))
    print("PASS: actual global coupled seed, direct restriction, transfer and split controls")


if __name__ == "__main__":
    main()
