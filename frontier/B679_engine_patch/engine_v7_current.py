"""
V7 conduit engine -- H9 / (G2)_1 conduit computation cell.
Origin Axiom project.

Conventions MIRRORED VERBATIM from
  <path> :
  - S = unnormalized Kac-Peterson Weyl alternating sum, normalized by
    S / sqrt((S S^dagger)_00), overall phase fixed so S_00 is a positive real
    (engine.py's own fix is the special case "if S00.real<0: S=-S", which
    suffices there because E6 has |Delta_+|=36 (i^36=1, a pure sign
    ambiguity); for A1 (|Delta_+|=1) and A2 (|Delta_+|=3) the residual
    ambiguity is a genuine phase i^{|Delta_+|}, not just a sign, so the fix
    implemented here is the literal generalization: rotate by the full
    residual phase so S_00 > 0 exactly. Cross-checked against i^{|Delta_+|}
    below and against the closed-form SU(2)_3 formula, which is manifestly
    real, as the validation gate.)
  - T_a = exp(2 pi i (h_a - c/24)), diagonal.
  - rho(A1) := T^2 S T, cross-gated against T S T^-1 S^-1 (the "two-word lock").
  - theta = conjugation; odd basis (e_a - e_b)/sqrt(2) over theta-pairs, in
    first-appearance order.
  - PRIM enumeration = lexicographic nested loops over Dynkin labels.

Algebra data for A_{n-1} (su(n), simply laced) realized concretely as the
standard permutation representation on the sum-zero hyperplane of R^n:
  simple roots e_i - e_{i+1}, Weyl group S_n by coordinate permutation,
  fundamental weights / Dynkin labels <-> partial-sum ("partition") vectors.
This sidesteps any row/column transpose ambiguity in an abstract
Cartan-matrix reflection-matrix construction: S_n permutation actions are
unambiguous, and the construction is checked against the h_j = j(j+1)/K
formula and the S_jl = sqrt(2/(k+2)) sin(pi(2j+1)(2l+1)/(k+2)) closed form
for SU(2)_3 before being trusted for SU(3)_2.
"""
import itertools
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 60


# ---------------------------------------------------------------------------
# A_{n-1} weight geometry (exact, Fraction arithmetic)
# ---------------------------------------------------------------------------

def An_weight_vector(dynkin_labels):
    """Dynkin labels (length n-1) -> weight vector in R^n (sum-zero hyperplane),
    via the standard partial-sum ("partition") realization of A_{n-1} weights."""
    n = len(dynkin_labels) + 1
    l = [sum(dynkin_labels[i:]) for i in range(len(dynkin_labels))] + [0]
    mean = Fraction(sum(l), n)
    return tuple(Fraction(x) - mean for x in l)


def An_rho_vector(n):
    return An_weight_vector(tuple([1] * (n - 1)))


def vdot(u, v):
    return sum(a * b for a, b in zip(u, v))


def vadd(u, v, s=1):
    return tuple(a + s * b for a, b in zip(u, v))


def An_primaries(n, k):
    """Dominant integral level-k weights of A_{n-1}, lexicographic nested loop
    over Dynkin labels (mirrors engine.py's enumerate_level_weights)."""
    r = n - 1
    prims = []
    ranges = [range(k + 1) for _ in range(r)]
    for labels in itertools.product(*ranges):
        if sum(labels) <= k:
            prims.append(labels)
    return prims


def An_weyl_group_signed(n):
    """S_n acting on R^n by coordinate permutation; eps = permutation sign."""
    elems = []
    for perm in itertools.permutations(range(n)):
        seen = [False] * n
        sign = 1
        for i in range(n):
            if not seen[i]:
                j, cyclen = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = perm[j]
                    cyclen += 1
                if cyclen % 2 == 0:
                    sign *= -1
        elems.append((perm, sign))
    return elems


def apply_perm(perm, v):
    return tuple(v[perm[i]] for i in range(len(v)))


def An_num_pos_roots(n):
    """|Delta_+| for A_{n-1} = n(n-1)/2."""
    return n * (n - 1) // 2


# ---------------------------------------------------------------------------
# exact-rational -> high precision complex exponential
# ---------------------------------------------------------------------------

def cexp_2pi_i_frac(fr: Fraction) -> mp.mpc:
    """exp(2 pi i * fr) at current mpmath precision, fr an exact Fraction."""
    num, den = fr.numerator, fr.denominator
    angle = 2 * mp.pi * mp.mpf(num) / mp.mpf(den)
    return mp.mpc(mp.cos(angle), mp.sin(angle))


# ---------------------------------------------------------------------------
# Kac-Peterson modular data for A_{n-1} level k
# ---------------------------------------------------------------------------

class An_Level:
    dimg = {2: 3, 3: 8}       # dim(su(n)) for n=2,3
    hvee = {2: 2, 3: 3}       # dual Coxeter number = n

    def __init__(self, n, k, primaries=None, name=""):
        self.n = n
        self.k = k
        self.K = k + self.hvee[n]
        self.name = name or f"A{n-1}_k{k}"
        self.PRIM = primaries if primaries is not None else An_primaries(n, k)
        self.N = len(self.PRIM)
        self.rho = An_rho_vector(n)
        self.lam_plus_rho = [vadd(An_weight_vector(lab), self.rho) for lab in self.PRIM]
        self.W = An_weyl_group_signed(n)
        self.nDeltaPlus = An_num_pos_roots(n)

        # exact rational conformal weights and central charge
        self.h = []
        for lab in self.PRIM:
            v = An_weight_vector(lab)
            num = vdot(v, vadd(v, self.rho, 2))     # (lambda, lambda+2rho)
            self.h.append(num / Fraction(2 * self.K))
        self.c = Fraction(self.k * self.dimg[n], self.K)

    # ---------- S matrix ----------
    def S_unnorm(self):
        """Unnormalized Weyl alternating sum U_ab (mpmath, high precision)."""
        N = self.N
        U = [[mp.mpc(0, 0) for _ in range(N)] for _ in range(N)]
        for a in range(N):
            for b in range(a, N):
                total = mp.mpc(0, 0)
                for perm, eps in self.W:
                    wv = apply_perm(perm, self.lam_plus_rho[a])
                    ip = vdot(wv, self.lam_plus_rho[b])           # exact Fraction
                    exponent = Fraction(-ip) / self.K
                    term = cexp_2pi_i_frac(exponent)
                    total += eps * term
                U[a][b] = total
                U[b][a] = total
        return U

    def S_matrix(self, verbose=False):
        """Normalize: S = U/sqrt(row0 norm), then full phase-fix S_00 -> positive real."""
        U = self.S_unnorm()
        N = self.N
        row0_norm2 = mp.mpf(0)
        for b in range(N):
            row0_norm2 += (U[0][b] * mp.conj(U[0][b])).real
        norm = mp.sqrt(row0_norm2)
        S = [[U[a][b] / norm for b in range(N)] for a in range(N)]
        s00 = S[0][0]
        phase = s00 / abs(s00)
        expected_phase = mp.mpc(0, 1) ** self.nDeltaPlus  # i^{|Delta_+|}
        if verbose:
            print(f"  [{self.name}] pre-fix S00 = {s00}, phase = {phase}, "
                  f"i^|Delta+|(|Delta+|={self.nDeltaPlus}) = {complex(expected_phase)}")
        S = [[S[a][b] / phase for b in range(N)] for a in range(N)]
        self._prefix_phase = phase
        self._expected_phase = expected_phase
        return S

    def T_matrix(self):
        return [cexp_2pi_i_frac(hh - self.c / 24) for hh in self.h]

    # ---------- helpers on mpmath matrices ----------
    @staticmethod
    def to_mpmatrix(Slist):
        n = len(Slist)
        M = mp.matrix(n, n)
        for i in range(n):
            for j in range(n):
                M[i, j] = Slist[i][j]
        return M

    @staticmethod
    def diag_mpmatrix(dlist):
        n = len(dlist)
        M = mp.zeros(n, n)
        for i in range(n):
            M[i, i] = dlist[i]
        return M

    def build(self, verbose=False):
        Slist = self.S_matrix(verbose=verbose)
        Tlist = self.T_matrix()
        S = self.to_mpmatrix(Slist)
        T = self.diag_mpmatrix(Tlist)
        return S, T

    # ---------- theta = conjugation ----------
    def conjugate_label(self, lab):
        return tuple(reversed(lab)) if self.n == 3 else lab  # (p,q)->(q,p) for A2; A1 self-conj always (real reps)

    def theta_split(self):
        fixed_idx = []
        pairs = []
        used = set()
        for i, p in enumerate(self.PRIM):
            cp = self.conjugate_label(p)
            if cp == p:
                fixed_idx.append(i)
            elif i not in used:
                j = self.PRIM.index(cp)
                pairs.append((i, j))
                used.add(i)
                used.add(j)
        return fixed_idx, pairs


def rho_A1_matrix(S, T):
    """rho(A1) := T^2 S T, cross-gated against T S T^-1 S^-1."""
    w1 = T * T * S * T
    w2 = T * S * (T ** -1) * (S ** -1)
    dev = max(abs(w1[i, j] - w2[i, j]) for i in range(w1.rows) for j in range(w1.cols))
    return w1, w2, dev


def gate_report(S, T, label=""):
    """Standard modular-data gates, mpmath high precision."""
    N = S.rows
    I = mp.eye(N)
    rep = {}
    rep['unitary'] = max(abs((S * S.conjugate().transpose() - I)[i, j])
                          for i in range(N) for j in range(N))
    rep['symmetric'] = max(abs((S - S.transpose())[i, j]) for i in range(N) for j in range(N))
    C2 = S * S
    STcubed = (S * T) ** 3
    rep['(ST)^3=S^2'] = max(abs((STcubed - C2)[i, j]) for i in range(N) for j in range(N))
    rep['S^4=I'] = max(abs(((S * S) ** 2 - I)[i, j]) for i in range(N) for j in range(N))
    rho, w2, dev = rho_A1_matrix(S, T)
    rep['two_word'] = dev
    rep['rho_unitary'] = max(abs((rho * rho.conjugate().transpose() - I)[i, j])
                              for i in range(N) for j in range(N))
    if label:
        print(f"--- gates: {label} ---")
        for k, v in rep.items():
            print(f"  {k}: {float(v):.3e}")
    return rep, rho


def verlinde_N(S):
    """N_{ab}^c = sum_m S_am S_bm conj(S_cm)/S_0m -- returns nested list, complex mpc."""
    N = S.rows
    d0 = [S[0, m] for m in range(N)]
    Nv = [[[None] * N for _ in range(N)] for _ in range(N)]
    for a in range(N):
        for b in range(N):
            for c in range(N):
                tot = mp.mpc(0, 0)
                for m in range(N):
                    tot += S[a, m] * S[b, m] * mp.conj(S[c, m]) / d0[m]
                Nv[a][b][c] = tot
    return Nv
