"""B1510 instrument: the two-sided deformation of rho0 = A (+) 1, A = mu rho_q (Ballas' projective holonomy of m004 with a central twist),
along both singlet directions c (in H^1(A), the 16's singlet) and c* (in H^1(A*), the 16*'s singlet).

Modes:
  --controls  run only on objects outside the sealed population (see PREREGISTRATION.md section 5):
              C0 valuation-rank unit tests; C1-C3 the exact one-sided families [[A, eps c],[0,1]], [[A,0],[eps c*^T A,1]] and the split
              family at the mu = -1 points (B1509's banked I = -1, +1, 0); C4 the GL(2) Heusener-Porti-Suarez control on m004
              (rho0 = diag(alpha, 1) at a simple root of the Alexander polynomial), solver in absolute mode.
  --sealed    the six exceptional points over GF(1009), GF(1033), GF(1129) (+ exact order-two cross-check): every quantity named in
              PREREGISTRATION.md section 6.
Nothing in --controls computes a sealed quantity (no adjoint cohomology at the six points, no two-sided term)."""
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(HERE))
import deform_lib as DL  # noqa: E402


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


IL = _load(ROOT / "frontier/B1374_the_class_index_in_the_sm_frame/verification/index_lib.py", "b1374_index_lib")
EI = _load(ROOT / "frontier/B1509_the_join_on_the_projective_vacuum/verification/extension_index.py", "b1509_extension_index")
WORD_R, WORD_MU, WORD_L = "mnMNmNMnmN", "m", "nMNmmNMn"
GENS = ("m", "n")
PRIMES = (1009, 1033, 1129)


# ------------------------------------------------------------------ helpers on cochains (dict g -> d x d)
def vec_cochain(U, d):
    return [U[g][i][j] for g in GENS for i in range(d) for j in range(d)]


def unvec_cochain(F, v, d):
    out, k = {}, 0
    for g in GENS:
        out[g] = [[v[k + i * d + j] for j in range(d)] for i in range(d)]
        k += d * d
    return out


def vec_mat(M): return [x for r in M for x in r]


def blockdiag(F, A, one):
    a = len(A)
    M = DL.zeros(F, a + 1, a + 1)
    for i in range(a):
        for j in range(a):
            M[i][j] = A[i][j]
    M[a][a] = one
    return M


def ad(F, X, U):
    return DL.mmul(F, DL.mmul(F, X, U), DL.inverse(F, X))


class Setup:
    """rho0 = diag(A, 1) on m, n with first-order cocycles c (upper right column) and c* (lower left row, as a column of A*)"""

    def __init__(self, F, Am, An, c, cs, label):
        self.F, self.label = F, label
        self.a = len(Am)
        self.d = self.a + 1
        self.A = {"m": Am, "n": An}
        self.rho0 = {g: blockdiag(F, self.A[g], F.one) for g in GENS}
        self.c, self.cs = c, cs

    def U_c(self, coef=None):
        F, a, d = self.F, self.a, self.d
        coef = F.one if coef is None else coef
        U = {}
        for g in GENS:
            M = DL.zeros(F, d, d)
            for i in range(a):
                M[i][a] = F.mul(coef, self.c[g][i])
            U[g] = M
        return U

    def U_cs(self, coef=None):
        F, a, d = self.F, self.a, self.d
        coef = F.one if coef is None else coef
        U = {}
        for g in GENS:
            M = DL.zeros(F, d, d)
            for j in range(a):
                M[a][j] = F.mul(coef, self.cs[g][j])
            U[g] = M
        return U

    def U_diag(self, top, bottom):
        """e(g) diag(top,..,top, bottom), e(m) = e(n) = 1: the twist-type cocycles"""
        F, a, d = self.F, self.a, self.d
        U = {}
        for g in GENS:
            M = DL.zeros(F, d, d)
            for i in range(a):
                M[i][i] = top
            M[a][a] = bottom
            U[g] = M
        return U

    def family(self, U, N):
        return DL.Family(self.F, self.rho0, U, N)


def separated(F, M0, a):
    """the line is separated at this element: the block of M0 minus 1 is invertible"""
    B = [[F.sub(M0[i][j], F.one if i == j else F.zero) for j in range(a)] for i in range(a)]
    return DL.rank(F, B) == a


def add_cochains(F, U, V):
    return {g: DL.madd(F, U[g], V[g]) for g in GENS}


def scale_cochain(F, c, U):
    return {g: DL.mscale(F, c, U[g]) for g in GENS}


def zero_cochain(F, d):
    return {g: DL.zeros(F, d, d) for g in GENS}


# ------------------------------------------------------------------ the Fox coboundary J and H^2 = coker J
def fox_J(S):
    """J as a (d^2) x (2 d^2) matrix: column = vec of the order-one relator coefficient for a unit first-order cochain"""
    F, d = S.F, S.d
    cols = []
    for g in GENS:
        for i in range(d):
            for j in range(d):
                U = zero_cochain(F, d)
                U[g][i][j] = F.one
                R = S.family({1: U}, 1).word(WORD_R)
                cols.append(vec_mat(R[1]))
    return DL.mT(cols)


def coboundaries(S):
    F, d = S.F, S.d
    out = []
    for i in range(d):
        for j in range(d):
            X = DL.zeros(F, d, d)
            X[i][j] = F.one
            U = {g: DL.msub(F, ad(F, S.rho0[g], X), X) for g in GENS}
            out.append(vec_cochain(U, d))
    return out


# ------------------------------------------------------------------ the formal solver
class Solver:
    """order-by-order formal deformation with first-order term U1 = s c + t c*.  The free cocycle choice f_(k-1) (a combination of
    `basis`, representatives of H^1 classes) is fixed at step k by the constraints that are affine in it:
      det^(k-1) = 0 [if use_det], lam_m^(k-1) = 0 [chiral], the class of P_k in H^2 = coker J,
      lam_l^(k) = 0 and lam_l^(k+1) = 0 [chiral; the latter read with U_k = the projected particular solution].
    The shifted constraint lam_l^(k+1) is PREREGISTRATION section 3, Theorem D: lam_l - 1 is divisible by st on the reducible locus,
    so the line's longitude condition at order k+1 is fixed by the order-(k-1) choice; the order-k choice moves it only through the
    polarisation of kappa_l, which vanishes where kappa_l does.  basis = list of (name, cochain)."""

    def __init__(self, S, N, basis, chiral, use_det=True, s=None, t=None):
        self.S, self.F, self.N, self.d, self.a = S, S.F, N, S.d, S.a
        self.basis, self.chiral, self.use_det = basis, chiral, use_det
        F, d = self.F, self.d
        s = F.one if s is None else s
        t = F.one if t is None else t
        self.U = {1: add_cochains(F, S.U_c(s), S.U_cs(t))}
        self.J = fox_J(S)
        dd = d * d
        self.Y = DL.nullspace(F, DL.mT(self.J), dd)                         # coker basis: y^T J = 0
        self.Y_kind = [self._kind(y) for y in self.Y]
        _, piv = DL.rref(F, [row + [F.one if i == j else F.zero for j in range(dd)] for i, row in enumerate(self.J)])
        self.comp = [p - 2 * dd for p in piv if p >= 2 * dd]                  # a complement of im J in C^2
        self.Jaug = [row + [F.one if i == c else F.zero for c in self.comp] for i, row in enumerate(self.J)]
        self.log = []

    def _kind(self, y):
        """the block of gl(d) = gl(a) + A + A* + F that a coker vector is supported on (J is block diagonal)"""
        a, d = self.a, self.d
        kinds = set()
        for idx, v in enumerate(y):
            if self.F.iszero(v):
                continue
            i, j = divmod(idx, d)
            kinds.add("block" if (i < a and j < a) else "A" if (i < a and j == a) else "A*" if (i == a and j < a) else "corner")
        return kinds.pop() if len(kinds) == 1 else "mixed"

    # constraint pieces ------------------------------------------------
    def _fam(self, upto):
        return self.S.family({k: v for k, v in self.U.items() if k <= upto}, upto)

    def relator(self, upto):
        return self._fam(upto).word(WORD_R)

    def obstruction(self, P):
        v = vec_mat(P)
        return [self._dot(y, v) for y in self.Y]

    def _dot(self, y, v):
        F = self.F
        s = F.zero
        for a, b in zip(y, v):
            if not F.iszero(a) and not F.iszero(b):
                s = F.add(s, F.mul(a, b))
        return s

    def lam(self, word, upto):
        fam = self._fam(upto)
        L = fam.X["m"] if word == "m" else fam.word(word)
        return DL.line_eigenvalue(self.F, L, upto, self.a)

    def logdet(self, upto):
        F, d = self.F, self.d
        V = [DL.zeros(F, d, d)] + [self.U[k]["m"] if k in self.U else DL.zeros(F, d, d) for k in range(1, upto + 1)]
        return DL.log_det(F, V, upto, d)

    def particular(self, k):
        """U_k solving J U_k = -P_k - w, w in the fixed complement of im J (w = 0 iff the class of P_k vanishes); free variables 0"""
        F, dd = self.F, self.d * self.d
        P = self.relator(k)[k]
        x = DL.solve(F, self.Jaug, [F.neg(v) for v in vec_mat(P)])
        return unvec_cochain(F, x[:2 * dd], self.d), any(not F.iszero(v) for v in x[2 * dd:])

    def lam_l_next(self, k):
        """lam_l at order k+1 with U_k = the projected particular solution (f_k = 0)"""
        Uk, _ = self.particular(k)
        self.U[k] = Uk
        try:
            return self.lam(WORD_L, k + 1)[k + 1]
        finally:
            del self.U[k]

    def constraints(self, k):
        out = []
        if self.use_det:
            out.append(self.logdet(k - 1)[k - 1])
        if self.chiral:
            out.append(self.lam("m", k - 1)[k - 1])
        out += self.obstruction(self.relator(k)[k])
        if self.chiral:
            out.append(self.lam(WORD_L, k)[k])
            if k + 1 <= self.N:
                out.append(self.lam_l_next(k))
        return out

    def constraint_kinds(self, k):
        """labels of constraints(k)'s components"""
        rows = (["det"] if self.use_det else []) + (["lam_m"] if self.chiral else []) + list(self.Y_kind)
        if self.chiral:
            rows += ["lam_l"] + (["lam_l_next"] if k + 1 <= self.N else [])
        return rows

    def final_constraints(self, k):
        out = []
        if self.use_det:
            out.append(self.logdet(k)[k])
        if self.chiral:
            out.append(self.lam("m", k)[k])
        return out

    def _solve_choice(self, order, fn, rows=None):
        """fix the free choice at `order` so that fn() vanishes; fn is affine in it (checked after the fact); rows labels fn's
        components for the per-block ranks in the log"""
        F = self.F
        base = fn()
        saved = self.U[order]
        cols = []
        for name, z in self.basis:
            self.U[order] = add_cochains(F, saved, z)
            cols.append([F.sub(x, y) for x, y in zip(fn(), base)])
            self.U[order] = saved
        M = DL.mT(cols) if cols else [[] for _ in base]
        if cols:
            f = DL.solve(F, M, [F.neg(x) for x in base])
        else:
            f = None if any(not F.iszero(x) for x in base) else []
        entry = {"constraints": len(base), "rank_of_linear_map": DL.rank(F, M) if cols else 0,
                 "base_nonzero": sum(1 for x in base if not F.iszero(x))}
        if rows is not None and cols:
            assert len(rows) == len(base)
            for kind in ("A", "A*", "block"):
                sub = [M[i] for i, r in enumerate(rows) if r == kind]
                entry[f"rank_on_{kind}_rows"] = DL.rank(F, sub) if sub else 0
                entry[f"base_{kind}_nonzero"] = sum(1 for i, r in enumerate(rows) if r == kind and not F.iszero(base[i]))
        if f is None:
            entry["solvable"] = False
            entry["base"] = [F.show(x) for x in base]
            entry["rank_augmented"] = DL.rank(F, [r + [x] for r, x in zip(M, base)]) if cols else None
            return entry
        entry["solvable"] = True
        entry["free_choice"] = {name: F.show(x) for (name, _), x in zip(self.basis, f) if not F.iszero(x)}
        for (name, z), x in zip(self.basis, f):
            if not F.iszero(x):
                self.U[order] = add_cochains(F, self.U[order], scale_cochain(F, x, z))
        entry["after_choice_all_zero"] = all(F.iszero(x) for x in fn())
        return entry

    def run(self):
        F, N = self.F, self.N
        P2 = self.relator(2)[2]
        ob2 = self.obstruction(P2)
        self.log.append({"order": 2, "obstruction_class_P2": [F.show(x) for x in ob2], "coker_blocks": self.Y_kind,
                         "obstruction_zero": all(F.iszero(x) for x in ob2)})
        if self.chiral:
            lam2 = self.lam(WORD_L, 2)[2]
            self.log[-1]["lam_l_2"] = F.show(lam2)
            if not F.iszero(lam2):
                return {"exists_to_order": 1, "stopped": "chiral: lam_l^(2) != 0", "log": self.log}
        if not all(F.iszero(x) for x in ob2):
            return {"exists_to_order": 1, "stopped": "order-two obstruction", "log": self.log}
        self.U[2], _ = self.particular(2)
        for k in range(3, N + 1):
            entry = {"order": k}
            entry.update(self._solve_choice(k - 1, lambda: self.constraints(k), self.constraint_kinds(k)))
            if not entry["solvable"] or not entry["after_choice_all_zero"]:
                self.log.append(entry)
                return {"exists_to_order": k - 1, "stopped": f"order {k} constraints not solvable", "log": self.log}
            Uk, obstructed = self.particular(k)
            if obstructed:
                entry["particular"] = False
                self.log.append(entry)
                return {"exists_to_order": k - 1, "stopped": f"order {k} particular solution obstructed", "log": self.log}
            self.U[k] = Uk
            self.log.append(entry)
        if self.final_constraints(N):
            entry = {"order": "final (det, lam_m at order N)"}
            entry.update(self._solve_choice(N, lambda: self.final_constraints(N)))
            self.log.append(entry)
            if not entry["solvable"] or not entry["after_choice_all_zero"]:
                return {"exists_to_order": N - 1, "stopped": "final det/lam_m not solvable", "log": self.log}
        return {"exists_to_order": N, "stopped": None, "log": self.log}

    def verify(self):
        """independent re-evaluation of the finished family: relator, det, line eigenvalues, the parity of the terms"""
        F, N, a = self.F, self.N, self.a
        fam = self._fam(N)
        R = fam.word(WORD_R)
        out = {"relator_identity_to_order_N": all(DL.iszeromat(F, R[k]) for k in range(1, N + 1)) and R[0] == DL.eye(F, self.d)}
        if self.use_det:
            out["det_one_to_order_N"] = all(F.iszero(x) for x in self.logdet(N)[1:])
        Lm, Ll = fam.X["m"], fam.word(WORD_L)
        lm = DL.line_eigenvalue(F, Lm, N, a)
        out["lam_m_series"] = [F.show(x) for x in lm]
        if separated(F, Ll[0], a):
            ll = DL.line_eigenvalue(F, Ll, N, a)
            out["lam_l_series"] = [F.show(x) for x in ll]
            out["line_stays_(1,1)"] = all(F.iszero(x) for x in lm[1:]) and all(F.iszero(x) for x in ll[1:])
        else:
            out["lam_l_series"] = "not separated: the block's longitude has eigenvalue 1"
            out["line_stays_(1,1)"] = None

        def odd_part_zero(U):
            return all(F.iszero(U[g][i][a]) and F.iszero(U[g][a][i]) for g in GENS for i in range(a))

        def even_part_zero(U):
            return all(F.iszero(U[g][i][j]) for g in GENS for i in range(a + 1) for j in range(a + 1)
                       if (i < a) == (j < a))
        out["parity_symmetric"] = all(odd_part_zero(self.U[k]) if k % 2 == 0 else even_part_zero(self.U[k])
                                      for k in range(1, N + 1) if k in self.U)
        return out


# ------------------------------------------------------------------ H^1 basis at rho0 (adjoint part computed: sealed mode only)
def h1_basis(S):
    """representatives of H^1(pi; gl(d)_rho0): c, c*, the twist T, the centre, and the adjoint sl(a) classes; with dimension data"""
    F, a, d = S.F, S.a, S.d
    J = fox_J(S)
    B = coboundaries(S)
    Z = DL.nullspace(F, J, 2 * d * d)
    rkB = DL.rank(F, B)
    T = S.U_diag(F.one, F.of(-a))
    C = S.U_diag(F.one, F.one)
    named = [("c", S.U_c()), ("c*", S.U_cs()), ("twist_T", T), ("centre", C)]
    span = list(B) + [vec_cochain(z, d) for _, z in named]
    # adjoint sl(a) classes: block-supported traceless cocycles, independent of B^1 and of the named classes
    adj = []
    idx = [(g, i, j) for g in GENS for i in range(a) for j in range(a)]
    cols = []
    for (g, i, j) in idx:
        U = zero_cochain(F, d)
        U[g][i][j] = F.one
        cols.append(vec_cochain(U, d))
    # constraints: J U = 0 and trace zero on each generator
    Jcols = DL.mmul(F, J, DL.mT(cols))                       # d^2 x |idx|
    trrows = []
    for g in GENS:
        trrows.append([F.one if (gg == g and i == j) else F.zero for (gg, i, j) in idx])
    sol = DL.nullspace(F, Jcols + trrows, len(idx))
    adj_cocycles = [DL.mmul(F, [v], cols)[0] for v in sol]               # as vectors of length 2 d^2
    for v in adj_cocycles:
        if DL.rank(F, span + [v]) > DL.rank(F, span):
            span.append(v)
            adj.append(v)
    basis = named + [(f"adj{n + 1}", unvec_cochain(F, v, d)) for n, v in enumerate(adj)]
    h1_total = len(Z) - rkB
    return basis, {"dim_Z1": len(Z), "dim_B1": rkB, "h1_gl": h1_total, "h1_sl_adjoint": len(adj),
                   "basis_spans_H1": len(named) + len(adj) == h1_total}


def adjoint_rigidity(S, basis):
    """rank of the restriction H^1(pi; sl(a)) -> H^1(T; sl(a)) and h^0(T; gl(a)) (the cusp pair's centraliser)"""
    F, a, d = S.F, S.a, S.d
    rho0m = S.rho0["m"]
    rhol = S.family({}, 1).word(WORD_L)[0]

    def res(U):
        famz = S.family({1: U}, 1)
        um = DL.mmul(F, famz.X["m"][1], DL.inverse(F, rho0m))
        ul = DL.mmul(F, famz.word(WORD_L)[1], DL.inverse(F, rhol))
        return vec_mat(um) + vec_mat(ul)

    BT = []
    for i in range(d):
        for j in range(d):
            X = DL.zeros(F, d, d)
            X[i][j] = F.one
            BT.append(vec_mat(DL.msub(F, ad(F, rho0m, X), X)) + vec_mat(DL.msub(F, ad(F, rhol, X), X)))
    adj = [z for name, z in basis if name.startswith("adj")]
    R = [res(z) for z in adj]
    rkBT = DL.rank(F, BT)
    r_res = DL.rank(F, BT + R) - rkBT
    # h^0(T; gl(a)): block-supported X commuting with rho0(m), rho0(l) on the A block
    cols = []
    idx = [(i, j) for i in range(a) for j in range(a)]
    rows = []
    for (i, j) in idx:
        X = DL.zeros(F, d, d)
        X[i][j] = F.one
        cols.append(vec_mat(DL.msub(F, ad(F, rho0m, X), X)) + vec_mat(DL.msub(F, ad(F, rhol, X), X)))
    h0T_gl = len(idx) - DL.rank(F, cols)
    return {"h1_adjoint": len(adj), "restriction_rank": r_res, "restriction_injective": r_res == len(adj), "h0_T_gl_a": h0T_gl,
            "cusp_pair_regular": h0T_gl == a}


def fixed_end_obstruction(solver, basis):
    """the second-order peripheral class modulo B^1(T) + res(H^1(pi)) (PREREGISTRATION section 3, Proposition F): its traceless
    gl(a)-block part (the triple product tau(a) = <c* a c> on H^1(sl(a))), and its line part at the longitude (= lam_l^(2))"""
    S, F, a, d = solver.S, solver.F, solver.a, solver.d
    fam = solver._fam(2)
    r0m, r0l = S.rho0["m"], fam.word(WORD_L)[0]
    Xm, Xl = fam.X["m"], fam.word(WORD_L)
    rows, rhs = [], []
    for (X0, A1) in ((r0m, Xm[1]), (r0l, Xl[1])):
        u1 = DL.mmul(F, A1, DL.inverse(F, X0))
        for i in range(d):
            for j in range(d):
                row = []
                for p in range(d):
                    for q in range(d):
                        W = DL.zeros(F, d, d)
                        W[p][q] = F.one
                        row.append(DL.msub(F, ad(F, X0, W), W)[i][j])
                rows.append(row)
                rhs.append(u1[i][j])
    w = DL.solve(F, rows, rhs)
    if w is None:
        return {"first_order_peripheral_coboundary": False}
    Wm = [[w[i * d + j] for j in range(d)] for i in range(d)]

    def gauged(X):
        """conjugation by I + eps W: orders one and two"""
        A1, A2, X0 = X[1], X[2], X[0]
        first = DL.madd(F, A1, DL.msub(F, DL.mmul(F, Wm, X0), DL.mmul(F, X0, Wm)))
        t = DL.madd(F, A2, DL.msub(F, DL.mmul(F, Wm, A1), DL.mmul(F, A1, Wm)))
        t = DL.madd(F, t, DL.msub(F, DL.mmul(F, X0, DL.mmul(F, Wm, Wm)), DL.mmul(F, Wm, DL.mmul(F, X0, Wm))))
        return first, DL.mmul(F, t, DL.inverse(F, X0))

    f_m, u2m = gauged(Xm)
    f_l, u2l = gauged(Xl)

    def res(U):
        famz = S.family({1: U}, 1)
        return (DL.mmul(F, famz.X["m"][1], DL.inverse(F, r0m)), DL.mmul(F, famz.word(WORD_L)[1], DL.inverse(F, r0l)))

    def traceless(M):
        tr = F.zero
        for i in range(a):
            tr = F.add(tr, M[i][i])
        sc = F.mul(tr, F.inv(F.of(a)))
        return [F.sub(M[i][j], sc if i == j else F.zero) for i in range(a) for j in range(a)]

    def proj(Mm, Ml, kind):
        if kind == "sl":
            return traceless(Mm) + traceless(Ml)
        return [x for r in Mm for x in r] + [x for r in Ml for x in r]          # "total": all of gl(d)

    out = {"first_order_peripheral_coboundary": True, "gauged_first_order_zero": DL.iszeromat(F, f_m) and DL.iszeromat(F, f_l)}
    cob = []
    for i in range(d):
        for j in range(d):
            X = DL.zeros(F, d, d)
            X[i][j] = F.one
            cob.append((DL.msub(F, ad(F, r0m, X), X), DL.msub(F, ad(F, r0l, X), X)))
    resb = [res(z) for _, z in basis]
    for kind in ("sl", "total"):
        span = [proj(x, y, kind) for x, y in cob] + [proj(x, y, kind) for x, y in resb]
        v = proj(u2m, u2l, kind)
        out[f"o_rel_{kind}"] = DL.rank(F, span + [v]) - DL.rank(F, span)
    trl = F.zero
    for i in range(a):
        trl = F.add(trl, u2l[i][i])
    out["line_at_longitude"] = F.show(u2l[a][a])
    out["block_trace_at_longitude"] = F.show(trl)
    return out


# ------------------------------------------------------------------ setups
def modp_setups(p):
    F0, pts = EI.modp_points(p)
    F = DL.FP(p)
    out = []
    for label, qq, mu in pts:
        mats = EI.modp_rep(F0, qq, mu)
        A = IL.Rep(F0, list(GENS), mats)
        c = EI.modp_cocycle(F0, A)
        cs = EI.modp_cocycle(F0, A.dual())
        mu_label = "-1" if mu == p - 1 else ("i" if mu == F0.root_of_unity(4) else "-i")
        S = Setup(F, mats["m"], mats["n"], {g: [r[0] for r in c[g]] for g in GENS}, {g: [r[0] for r in cs[g]] for g in GENS},
                  f"{label} (q={qq} mod {p}, mu={mu_label})")
        S.mu_label, S.p, S.q_modp = mu_label, p, qq
        out.append(S)
    return out


def exact_setups():
    import sympy as sp
    K = EI.K
    F = DL.FK(K)
    out = []
    for label, qq, mu, ml in EI.POINTS:
        m, n = EI.ballas(qq)
        A = EI.ERep({"m": EI.dm(mu * m), "n": EI.dm(mu * n)})
        c = EI.generator_cocycle(A)
        cs = EI.generator_cocycle(A.dual())
        conv = lambda M: [[M[i, j].element for j in range(M.shape[1])] for i in range(M.shape[0])]
        S = Setup(F, conv(A.M["m"]), conv(A.M["n"]), {g: [x[0] for x in conv(c[g])] for g in GENS},
                  {g: [x[0] for x in conv(cs[g])] for g in GENS}, f"{label}, mu={ml} (exact)")
        S.mu_label = ml
        out.append(S)
    return out


def index_row(F, fam, N):
    """main's index of the family over F((eps)) to order N, with the data Theorem C names"""
    r = DL.index_laurent(F, fam, WORD_R, WORD_MU, WORD_L, N + 1)
    V, Vs = r["V"], r["V*"]
    return {"I": r["I"], "a0": V["a0"], "b0": Vs["a0"], "a1": V["a1"], "b1": Vs["a1"], "t0": V["t0"], "s0": Vs["t0"],
            "r1": V["r1"], "q1": Vs["r1"], "n_V": V["n"], "n_Vstar": Vs["n"], "pivots_V": V["pivot_vals_Big"],
            "pivots_Vstar": Vs["pivot_vals_Big"], "prec_left": min(V["prec_left"], Vs["prec_left"])}


# ------------------------------------------------------------------ controls (outside the sealed population)
def control_valuation_rank():
    F = DL.FP(1009)
    e = lambda *cs: [F.of(x) for x in cs] + [0] * (8 - len(cs))
    cases = {
        "diag(eps, eps^2)": ([[e(0, 1), e(0)], [e(0), e(0, 0, 1)]], 2),
        "rank-one [[eps, eps^2], [1, eps]]": ([[e(0, 1), e(0, 0, 1)], [e(1), e(0, 1)]], 1),
        "zero": ([[e(0), e(0)], [e(0), e(0)]], 0),
        "[[1,1],[1,1+eps^3]]": ([[e(1), e(1)], [e(1), e(1, 0, 0, 1)]], 2),
    }
    return {name: DL.laurent_rank(F, M, 8)[0] == want for name, (M, want) in cases.items()}


def control_one_sided(N=6):
    """C1-C3 (the banked identity): B1509's I(W1), I(W2) at all six points (-1/+1 at mu = -1, 0/0 at +-i) and the split 0,
    reproduced over F((eps)) by the ranks-only index on the exact one-sided families"""
    rows = []
    for p in PRIMES:
        for S in modp_setups(p):
            F = S.F
            w1, w2 = (-1, +1) if S.mu_label == "-1" else (0, 0)
            for name, U1, want in (("W1 (line quotient)", S.U_c(), w1), ("W2 (line sub)", S.U_cs(), w2),
                                   ("split A+1", zero_cochain(F, S.d), 0)):
                fam = S.family({1: U1}, N)
                R = fam.word(WORD_R)
                exact = all(DL.iszeromat(F, R[k]) for k in range(1, N + 1))
                lm = DL.line_eigenvalue(F, fam.X["m"], N, S.a)
                ll = DL.line_eigenvalue(F, fam.word(WORD_L), N, S.a)
                idx = DL.index_laurent(F, fam, WORD_R, WORD_MU, WORD_L, N + 1)
                rows.append({"point": S.label, "family": name, "exact_rep_to_order": N if exact else None,
                             "line_(1,1)": all(F.iszero(x) for x in lm[1:] + ll[1:]), "I": idx["I"], "expected": want,
                             "prec_left": min(idx["V"]["prec_left"], idx["V*"]["prec_left"])})
    return rows


def gl2_setups(p):
    """GL(2) on m004: rho0 = diag(alpha, 1), alpha(m) = alpha(n) = t0, t0 a simple root of the Alexander polynomial t^2 - 3t + 1"""
    F0 = IL.GF(p)
    r5 = F0.sqrt(5)
    if r5 is None:
        return []
    F = DL.FP(p)
    out = []
    for sgn in (1, -1):
        t0 = (3 + sgn * r5) * F0.inv(2) % p
        A = IL.Rep(F0, list(GENS), {"m": [[t0]], "n": [[t0]]})
        c = EI.modp_cocycle(F0, A)
        cs = EI.modp_cocycle(F0, A.dual())
        S = Setup(F, [[t0]], [[t0]], {g: [r[0] for r in c[g]] for g in GENS}, {g: [r[0] for r in cs[g]] for g in GENS},
                  f"GL2 t0={t0} mod {p}")
        S.p, S.t0 = p, t0
        out.append(S)
    return out


def gl2_basis(S):
    F = S.F
    return [("c", S.U_c()), ("c*", S.U_cs()), ("twist_T", S.U_diag(F.one, F.of(-1))), ("centre", S.U_diag(F.one, F.one))]


def control_gl2(N=8):
    """C4: the absolute two-sided deformation of diag(alpha, 1) exists (Heusener-Porti-Suarez; Burde, de Rham) and its index over
    F((eps)) is 0 (Theorem C).  (A character is 1 on the longitude, so the line is not separated there: no chiral reading.)"""
    rows = []
    for p in PRIMES:
        setups = gl2_setups(p)
        if not setups:
            rows.append({"p": p, "skipped": "5 is not a square"})
            continue
        for S in setups:
            F = S.F
            sol = Solver(S, N, gl2_basis(S), chiral=False, use_det=False)
            res = sol.run()
            row = {"p": p, "t0": S.t0, "absolute_exists_to_order": res["exists_to_order"], "stopped": res["stopped"],
                   "orders": [{k: v for k, v in e.items() if k in ("order", "solvable", "rank_of_linear_map", "free_choice")}
                              for e in res["log"]]}
            if res["exists_to_order"] == N:
                ver = sol.verify()
                row["relator_identity"] = ver["relator_identity_to_order_N"]
                row["line_stays_(1,1)"] = ver["line_stays_(1,1)"]
                row["parity_symmetric"] = ver["parity_symmetric"]
                for n in (N - 2, N):
                    row[f"index_N{n}"] = index_row(F, sol._fam(n), n)
            rows.append(row)
    return rows


def control_chiral_one_sided(N=6):
    """C5: the chiral solver on the one-sided direction (s, t) = (1, 0) at the mu = -1 points, with the named classes only (no
    adjoint class is computed): it must return the exact family [[A, eps c], [0, 1]] (every choice zero, every U_k = 0 for k >= 2),
    the line at (1, 1) and B1509's index -1"""
    rows = []
    for p in PRIMES:
        for S in modp_setups(p):
            if S.mu_label != "-1":
                continue
            F = S.F
            named = [("c", S.U_c()), ("c*", S.U_cs()), ("twist_T", S.U_diag(F.one, F.of(-S.a))), ("centre", S.U_diag(F.one, F.one))]
            sol = Solver(S, N, named, chiral=True, use_det=True, s=F.one, t=F.zero)
            res = sol.run()
            ver = sol.verify() if res["exists_to_order"] == N else {}
            higher_zero = all(DL.iszeromat(F, sol.U[k][g]) for k in range(2, N + 1) if k in sol.U for g in GENS)
            idx = DL.index_laurent(F, sol._fam(N), WORD_R, WORD_MU, WORD_L, N + 1) if ver else {}
            rows.append({"point": S.label, "exists_to_order": res["exists_to_order"], "all_choices_zero":
                         all(not e.get("free_choice") for e in res["log"] if "free_choice" in e), "U_k_zero_for_k>=2": higher_zero,
                         "relator_identity": ver.get("relator_identity_to_order_N"), "line_stays_(1,1)": ver.get("line_stays_(1,1)"),
                         "I": idx.get("I")})
    return rows


def gl3_setups(p):
    """GL(3) on m004: rho0 = (t rho_geo) + 1, rho_geo m004's geometric representation into SL(2) (m = [[1,1],[0,1]],
    n = [[1,0],[z,1]], z found mod p), t a root of the hyperbolic torsion polynomial t^2 - 4t + 1 (where h^1(t rho_geo) = 1)"""
    F0 = IL.GF(p)
    F = DL.FP(p)
    out = []
    z = next(z for z in range(1, p) if IL.Rep(F0, list(GENS), {"m": [[1, 1], [0, 1]], "n": [[1, 0], [z, 1]]}).check_relators([WORD_R]))
    r3 = F0.sqrt(3)
    for t in ((2 + r3) % p, (2 - r3) % p):
        mats = {"m": F0.scale(t, [[1, 1], [0, 1]]), "n": F0.scale(t, [[1, 0], [z, 1]])}
        A = IL.Rep(F0, list(GENS), mats)
        c = EI.modp_cocycle(F0, A)
        cs = EI.modp_cocycle(F0, A.dual())
        S = Setup(F, mats["m"], mats["n"], {g: [r[0] for r in c[g]] for g in GENS}, {g: [r[0] for r in cs[g]] for g in GENS},
                  f"GL3 z={z} t={t} mod {p}")
        S.p, S.t = p, t
        out.append(S)
    return out


def control_gl3(N=8):
    """C6: the adjoint machinery on a rank-three case outside the sealed population (Heusener-Porti's setting at a simple root):
    the H^1 basis with its adjoint class, boundary rigidity, the fixed-end class, the absolute branch (GL mode) and its index"""
    rows = []
    for p in PRIMES:
        for S in gl3_setups(p):
            F = S.F
            basis, h1 = h1_basis(S)
            row = {"p": p, "t": S.t, "H1": h1, "rigidity": adjoint_rigidity(S, basis)}
            sol = Solver(S, N, basis, chiral=False, use_det=False)
            res = sol.run()
            row["absolute_exists_to_order"] = res["exists_to_order"]
            row["stopped"] = res["stopped"]
            row["order2_obstruction_zero"] = res["log"][0]["obstruction_zero"]
            row["orders"] = [{k: v for k, v in e.items() if k in ("order", "rank_of_linear_map", "rank_on_A_rows", "rank_on_A*_rows",
                                                                     "base_A_nonzero", "base_A*_nonzero", "free_choice")}
                             for e in res["log"]]
            if res["exists_to_order"] >= 2:
                row["fixed_end_order2"] = fixed_end_obstruction(sol, basis)
            row["kappa_l_hat"] = F.show(sol.lam(WORD_L, 2)[2])
            if res["exists_to_order"] == N:
                ver = sol.verify()
                row["verify"] = {k: ver[k] for k in ("relator_identity_to_order_N", "parity_symmetric", "line_stays_(1,1)")}
                row["index"] = {n: index_row(F, sol._fam(n), n) for n in (N - 2, N)}
            rows.append(row)
    return rows


def controls():
    return {"C0_valuation_rank": control_valuation_rank(), "C1_C3_one_sided_and_split": control_one_sided(),
            "C4_gl2_heusener_porti_suarez": control_gl2(), "C5_chiral_solver_on_the_one_sided_family": control_chiral_one_sided(),
            "C6_gl3_adjoint_machinery": control_gl3()}


# ------------------------------------------------------------------ the sealed run
def sealed_point(S, N_list=(8, 10)):
    F = S.F
    basis, h1 = h1_basis(S)
    out = {"point": S.label, "mu": S.mu_label, "H1": h1, "rigidity": adjoint_rigidity(S, basis)}
    Nmax = max(N_list)
    # the absolute two-sided branch (det = 1; the line is free to move)
    sol_abs = Solver(S, Nmax, basis, chiral=False, use_det=True)
    res_abs = sol_abs.run()
    out["order2_obstruction_zero"] = res_abs["log"][0]["obstruction_zero"]
    out["absolute"] = {"exists_to_order": res_abs["exists_to_order"], "stopped": res_abs["stopped"], "log": res_abs["log"]}
    if res_abs["exists_to_order"] >= 2:
        out["fixed_end_order2"] = fixed_end_obstruction(sol_abs, basis)
    lam2 = sol_abs.lam(WORD_L, 2)[2]
    out["kappa_l_hat"] = F.show(lam2)
    out["kappa_l_zero"] = F.iszero(lam2)
    if res_abs["exists_to_order"] == Nmax:
        out["absolute"]["verify"] = sol_abs.verify()
        out["absolute"]["index"] = {N: index_row(F, sol_abs._fam(N), N) for N in N_list}
    # the chiral two-sided branch (the trivial line keeps (1, 1)); only where kappa_l_hat = 0 (Theorem B)
    if out["kappa_l_zero"]:
        sol_ch = Solver(S, Nmax, basis, chiral=True, use_det=True)
        res_ch = sol_ch.run()
        out["chiral"] = {"exists_to_order": res_ch["exists_to_order"], "stopped": res_ch["stopped"], "log": res_ch["log"]}
        if res_ch["exists_to_order"] == Nmax:
            out["chiral"]["verify"] = sol_ch.verify()
            out["chiral"]["index"] = {N: index_row(F, sol_ch._fam(N), N) for N in N_list}
    else:
        out["chiral"] = {"exists_to_order": 1, "stopped": "kappa_l_hat != 0 (Theorem B): the line's longitude eigenvalue moves at order two"}
    return out


def sealed_exact_order2():
    rows = []
    for S in exact_setups():
        F = S.F
        sol = Solver(S, 2, [], chiral=False, use_det=False)
        P2 = sol.relator(2)[2]
        ob = sol.obstruction(P2)
        lam = sol.lam(WORD_L, 2)
        rows.append({"point": S.label, "mu": S.mu_label, "order2_obstruction_zero": all(F.iszero(x) for x in ob),
                     "kappa_l_hat": F.show(lam[2]), "kappa_l_zero": F.iszero(lam[2])})
    return rows


def sealed():
    """the banked identity first (B1509's indices through this pipeline's F((eps)) index), then every sealed quantity"""
    banked = control_one_sided()
    ok = all(r["I"] == r["expected"] and r["exact_rep_to_order"] == 6 for r in banked) and len(banked) == 54
    out = {"banked_identity_B1509_reproduced": ok, "banked_identity_rows": len(banked)}
    if not ok:
        out["stopped"] = "the banked identity failed: no sealed quantity read"
        return out
    out["exact_order2"] = sealed_exact_order2()
    out["modp"] = [sealed_point(S) for p in PRIMES for S in modp_setups(p)]
    return out


if __name__ == "__main__":
    if "--controls" in sys.argv:
        res = controls()
        txt = json.dumps(res, indent=1, sort_keys=True, default=str)
        print(txt)
        if "--record" in sys.argv:
            (HERE / "controls_run.txt").write_text(txt + "\n", encoding="utf-8")
    elif "--sealed" in sys.argv:
        res = sealed()
        txt = json.dumps(res, indent=1, sort_keys=True, default=str)
        print(txt)
        if "--record" in sys.argv:
            (HERE / "two_sided_run.txt").write_text(txt + "\n", encoding="utf-8")
    else:
        print(__doc__)
