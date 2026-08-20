"""B1102 Op1 (part a): split a reductive Lie algebra given as an explicit basis inside
an ambient space into its simple ideals, via primary decomposition of ad(generic
element) + bracket-connectivity merge of the resulting PURE blocks + bracket closure.

Algorithm (own code; the METHOD -- primary decomposition catching eigenvalue collisions
via a squarefreeness certificate -- is designed here fresh, not copied from B1098's
verifier, precisely because that verifier's own code isn't available to import, only
its FINDINGS description ("a primary-decomposition method... pre-validated on synthetic
sl3+sl3 data with known ground truth"); the same discipline is followed below: validate
on synthetic sl3+sl3 with a RANDOM basis mix (worst case: no vector pure) before trusting
the real 78-dim centralizer data.

Why primary decomposition (not naive pairwise-bracket union-find on the raw basis):
if the raw basis vectors are already "mixed" (nonzero components in more than one
ideal), naive union-find over raw-vector brackets over-merges immediately (mixed
vectors generically fail to commute with everything). Primary decomposition of
ad(generic x) first isolates PURE blocks (each block is an eigenspace / Q-irreducible
generalized eigenspace of ad(x); for x=x_A+x_B with x_A,x_B regular in their own
ideals, a NONZERO eigenvalue's block lies entirely in one ideal -- proved below in
the docstring of `split_ideals`) -- union-find is then applied to those PURE blocks,
where the connectivity argument (root graphs of simple Lie algebras are connected) is
valid.
"""
import random
from fractions import Fraction as F
import sympy as sp


def _is_zero_ambient(v):
    return all((x == 0) for x in v)


def split_ideals(basis, bracket_fn, ambient_dim, to_ambient, seed=1, max_tries=8, verbose=False):
    """basis: list of n ambient vectors (each a length-`ambient_dim` list of Fraction/
    sp.Rational) spanning a Lie subalgebra c of the ambient algebra, closed under
    bracket_fn (ambient bracket). Returns dict with 'ideals': list of lists of ambient
    basis vectors (each inner list a basis for one simple ideal, in ORIGINAL c-coords
    reconstructed as ambient vectors), plus certification fields.

    Method:
      1. intrinsic structure constants of c (express bracket_fn(basis[i],basis[j]) back
         in c-coordinates via exact linear solve).
      2. for a random rational x in c, T = intrinsic ad(x); factor char poly over Q;
         for each irreducible factor away from t^k (k = the eigenvalue-0 multiplicity),
         ker(p(T)) is a PURE block (proof: if v is a lambda-eigenvector of ad_c(x) with
         lambda != 0, and c = I_1 (+) ... (+) I_r (unknown a priori) with x = sum x_m,
         write v = sum v_m (v_m in I_m); ad_c(x)(v_m) = ad_{I_m}(x_m)(v_m) since ideals
         kill each other, so each v_m is itself a lambda-eigenvector of ad_{I_m}(x_m) or
         zero; a SQUAREFREE nonzero-part char poly (checked, not assumed) means each
         eigenvalue's line is 1-dim over the algebraic closure, so at most one v_m is
         nonzero -- the block (and its Galois orbit, i.e. the whole ker(p(T)) primary
         component, since Galois preserves each Q-rational ideal I_m) is PURE).
      3. union-find merge pure blocks using ambient bracket-nonzero connectivity (valid
         because root systems of simple algebras are connected graphs under this
         relation, and cross-ideal brackets are identically zero -- so blocks from
         different ideals NEVER connect, blocks from the same ideal ALWAYS eventually
         connect).
      4. bracket-closure each merged cluster (adds back the zero-eigenvalue/Cartan part)
         to recover the full ideal.
      5. exhaustive certification: dims sum to dim(c), pairwise brackets across ideals
         are ALL exactly zero (every basis-pair, not sampled).
    """
    n = len(basis)
    # 1. intrinsic structure constants: express bracket_fn(basis[i],basis[j]) in c-coords.
    # NOTE: sp.Rational(x) (NOT nsimplify -- nsimplify on an already-exact Rational goes
    # hunting for closed forms via PSLQ and can blow up into enormous nested-radical
    # garbage; caught by a timeout during this arc's own synthetic self-test).
    def _rat(x):
        return x if isinstance(x, (sp.Rational, sp.Integer)) else sp.Rational(x)
    Cmat = sp.Matrix([[_rat(x) for x in row] for row in basis]).T  # ambient_dim x n
    def to_ccoords(vec):
        rhs = sp.Matrix([_rat(x) for x in vec])
        sol, params = Cmat.gauss_jordan_solve(rhs)
        sol = sol.subs({p: 0 for p in params})
        return [_rat(sol[i]) for i in range(n)]

    F_INTR = {}  # (i,j) -> list of n coords
    for i in range(n):
        for j in range(n):
            br_ij = bracket_fn(basis[i], basis[j])
            F_INTR[(i, j)] = to_ccoords(br_ij) if not _is_zero_ambient(br_ij) else [sp.Integer(0)] * n

    def intrinsic_ad(coeffs):
        """n x n sympy matrix of ad(x) in c-coords, x = sum coeffs[i]*basis[i]."""
        M = sp.zeros(n, n)
        for i in range(n):
            ci = coeffs[i]
            if ci == 0:
                continue
            for j in range(n):
                fij = F_INTR[(i, j)]
                for k in range(n):
                    if fij[k]:
                        M[k, j] += ci * fij[k]
        return M

    rng = random.Random(seed)
    for attempt in range(max_tries):
        coeffs = [sp.Integer(rng.randint(-9, 9)) for _ in range(n)]
        if all(c == 0 for c in coeffs):
            continue
        T = intrinsic_ad(coeffs)
        lam = sp.Symbol("lam")
        cp = T.charpoly(lam).as_expr()
        factors = sp.factor_list(cp, lam)[1]  # [(poly, mult), ...]
        # eigenvalue-0 multiplicity / factor
        zero_mult = 0
        nonzero_factors = []
        for fac, mult in factors:
            if fac == lam:
                zero_mult += mult
            else:
                nonzero_factors.append((fac, mult))
        nonzero_sqfree = all(m == 1 for _, m in nonzero_factors)
        if verbose:
            print(f"  [attempt {attempt}] zero_mult={zero_mult}, nonzero factors degs="
                  f"{[sp.degree(f, lam) for f, m in nonzero_factors]}, squarefree={nonzero_sqfree}")
        if not nonzero_sqfree:
            continue  # bad luck / non-generic x; retry
        # 2. pure blocks = ker(p(T)) for each nonzero irreducible factor
        blocks = []  # each: list of n-dim c-coordinate vectors (sympy), a basis for ker(p(T))
        for fac, mult in nonzero_factors:
            pT = fac.as_poly(lam).eval({}) if False else None
            # build p(T) by Horner on the matrix
            coeffs_poly = sp.Poly(fac, lam).all_coeffs()  # leading first
            pT = sp.zeros(n, n)
            cur = sp.eye(n)
            # Horner: p(T) = (((a0*T + a1*I)*T + a2*I)*T + ...)
            acc = sp.zeros(n, n)
            for c_ in coeffs_poly:
                acc = acc * T + c_ * sp.eye(n)
            ker = acc.nullspace()
            assert len(ker) == sp.degree(fac, lam), (len(ker), sp.degree(fac, lam))
            blocks.append([[_rat(v[k]) for k in range(n)] for v in ker])
        total_nonzero_dim = sum(len(b) for b in blocks)
        assert total_nonzero_dim == n - zero_mult
        break
    else:
        raise RuntimeError("split_ideals: could not find a generic element after retries "
                            "(nonzero char-poly part never squarefree) -- escalate to fallback")

    # convert each block's c-coord vectors to ambient vectors for bracket testing
    def ccoords_to_ambient(cc):
        out = [F(0)] * ambient_dim if isinstance(basis[0][0], F) else [sp.Integer(0)] * ambient_dim
        for k in range(n):
            if cc[k] != 0:
                bk = basis[k]
                coef = cc[k]
                for idx in range(ambient_dim):
                    if isinstance(bk[idx], F):
                        out[idx] = out[idx] + F(coef.p, coef.q) * bk[idx] if coef != 0 else out[idx]
                    else:
                        out[idx] = out[idx] + coef * bk[idx]
        return out

    block_ambient = [[ccoords_to_ambient(v) for v in b] for b in blocks]

    # 3. union-find merge blocks via ambient bracket connectivity
    nb = len(blocks)
    parent = list(range(nb))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx != ry:
            parent[rx] = ry

    changed = True
    while changed:
        changed = False
        groups = {}
        for i in range(nb):
            groups.setdefault(find(i), []).append(i)
        keys = list(groups.keys())
        for a in range(len(keys)):
            for b in range(a + 1, len(keys)):
                ra, rb = keys[a], keys[b]
                if find(ra) == find(rb):
                    continue
                connected = False
                for bi in groups[ra]:
                    for bj in groups[rb]:
                        for u in block_ambient[bi]:
                            for w in block_ambient[bj]:
                                if not _is_zero_ambient(bracket_fn(u, w)):
                                    connected = True
                                    break
                            if connected:
                                break
                        if connected:
                            break
                    if connected:
                        break
                if connected:
                    union(ra, rb)
                    changed = True

    clusters = {}
    for i in range(nb):
        clusters.setdefault(find(i), []).append(i)
    cluster_list = list(clusters.values())

    # 4. bracket-closure each cluster: add [u,w] for u,w in the cluster's vectors, repeat
    ideals = []
    for cl in cluster_list:
        vecs = []
        for bi in cl:
            vecs.extend(block_ambient[bi])
        # closure via rank-extension (exact): keep adding brackets while rank grows
        def basis_matrix(vs):
            return sp.Matrix.hstack(*[sp.Matrix([sp.Rational(x) for x in v]) for v in vs]) if vs else sp.zeros(ambient_dim, 0)
        M = basis_matrix(vecs)
        frontier = list(vecs)
        grown = True
        while grown:
            grown = False
            new_vecs = []
            for i in range(len(frontier)):
                for j in range(len(vecs)):
                    br_ = bracket_fn(frontier[i], vecs[j])
                    if not _is_zero_ambient(br_):
                        testM = sp.Matrix.hstack(M, sp.Matrix([sp.Rational(x) for x in br_]))
                        if testM.rank() > M.rank():
                            M = testM
                            new_vecs.append(br_)
                            grown = True
            if new_vecs:
                vecs = vecs + new_vecs
                frontier = new_vecs
        # reduce to an actual basis (rref-independent columns)
        Mrr, piv = M.rref()
        ideal_basis = [list(M[:, p]) for p in piv]
        ideals.append(ideal_basis)

    # 5. certification
    dims = [len(I) for I in ideals]
    cross_zero = True
    for a in range(len(ideals)):
        for b in range(len(ideals)):
            if a == b:
                continue
            for u in ideals[a]:
                for w in ideals[b]:
                    if not _is_zero_ambient(bracket_fn(u, w)):
                        cross_zero = False
    total_dim = sum(dims)
    return {
        "ideals": ideals,
        "dims": dims,
        "n_ideals": len(ideals),
        "total_dim": total_dim,
        "expected_dim": n,
        "dims_match": total_dim == n,
        "cross_brackets_zero": cross_zero,
    }
