"""B649 stage 2a — exact entry identification in L = Q(s, i) (prereg 4dc3eacd)."""
import warnings

warnings.filterwarnings("ignore")
import mpmath as mp  # noqa: E402
import snappy  # noqa: E402

mp.mp.dps = 360

# RUN 2 (in-trail revision; run 1 preserved as *_run1_FAILED.txt): the
# 64-digit source left ~40 digits of pslq fitting freedom at coeff 1e8
# and the EXACT det gate caught spurious identifications. Source now =
# the polished PSL rep at 1200 bits (~360 digits), signs fixed per
# generator against the 64-digit SL2 lift; acceptance 1e-250.
from snappy.snap.polished_reps import polished_holonomy

Mlow = snappy.Manifold("m136").high_precision()
Glow = Mlow.fundamental_group(simplify_presentation=True)
M0 = snappy.Manifold("m136")
GP = polished_holonomy(M0, bits_prec=1200, lift_to_SL2=False)
G = Glow                                  # words/relators from the same presentation


def _clean(x):
    return str(x).replace(" E", "e").replace("E", "e").strip()


def _p2mp(mat):
    return [[mp.mpc(_clean(mat[i][j].real()), _clean(mat[i][j].imag()))
             for j in range(2)] for i in range(2)]


def _low(word):
    m = None
    for ch in word:
        x = Glow.SL2C(ch)
        m = x if m is None else m * x
    return [[mp.mpc(_clean(m[i, j].real()), _clean(m[i, j].imag()))
             for j in range(2)] for i in range(2)]


def mat_of(gen):
    """polished matrix, sign-fixed against the 64-digit SL2 lift."""
    P = _p2mp(GP(gen))
    S = _low(gen)
    dplus = max(abs(P[i][j] - S[i][j]) for i in range(2) for j in range(2))
    dminus = max(abs(-P[i][j] - S[i][j]) for i in range(2) for j in range(2))
    if dminus < dplus:
        P = [[-P[i][j] for j in range(2)] for i in range(2)]
    return P


A = mat_of("a")
B = mat_of("b")
C = mat_of("c")

# s: the real root ~ +3.1075 of s^4 - 8 s^2 - 16
s_num = mp.sqrt(4 + 4 * mp.sqrt(2))* mp.mpf(1)
s_num = mp.sqrt(4 + 4 * mp.sqrt(2))
BASIS = [s_num ** j for j in range(4)]


def ident_real(x):
    """identify real x in Q(s): pslq on [x, 1, s, s^2, s^3]."""
    if abs(x) < mp.mpf(10) ** -300:
        return [__import__("fractions").Fraction(0)] * 4
    rel = mp.pslq([x] + BASIS, maxcoeff=10 ** 10, maxsteps=10 ** 6)
    if rel is None or rel[0] == 0:
        return None
    from fractions import Fraction as Fr
    c0 = rel[0]
    coeffs = [Fr(-rel[k + 1], c0) for k in range(4)]
    recon = sum(Fr(c.numerator, c.denominator) * 1 for c in [0]) if False \
        else sum(mp.mpf(c.numerator) / c.denominator * BASIS[k]
                 for k, c in enumerate(coeffs))
    if abs(recon - x) > mp.mpf(10) ** -250:
        return None
    return coeffs


def ident_entry(z):
    re = ident_real(mp.re(z))
    im = ident_real(mp.im(z))
    return (re, im)


def try_all(mats, tag):
    out = {}
    ok = True
    for nm, Mx in mats.items():
        for i in range(2):
            for j in range(2):
                r = ident_entry(Mx[i][j])
                out[(nm, i, j)] = r
                if r[0] is None or r[1] is None:
                    ok = False
    print(f"  [{tag}] all 12 entries identified: {ok}", flush=True)
    return ok, out


print("== S2a-G1 direct attempt ==", flush=True)
ok, table = try_all({"a": A, "b": B, "c": C}, "direct")

if not ok:
    print("\n== normalization: meridian to upper-triangular parabolic ==",
          flush=True)
    # meridian word CCB (stage 1); find its fixed point, conjugate to inf;
    # then fix the second normalization by sending b's fixed point to 0.
    MU = mat_of("CCB")
    # parabolic fixed point p: (MU00 - MU11 +- 0)/ (2 MU10) for parabolic
    p = (MU[0][0] - MU[1][1]) / (2 * MU[1][0])
    # T sends p -> inf: T = [[1, -p],[0,1]] * [[0,-1],[1,0]] variant;
    # use T = [[0, -1], [1, -p]] (Mobius z -> -1/(z - p))
    T = [[mp.mpf(0), mp.mpf(-1)], [mp.mpf(1), -p]]
    def minv2(Mx):
        d = Mx[0][0] * Mx[1][1] - Mx[0][1] * Mx[1][0]
        return [[Mx[1][1] / d, -Mx[0][1] / d], [-Mx[1][0] / d, Mx[0][0] / d]]
    def mm2(X, Y):
        return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)]
                for i in range(2)]
    Ti = minv2(T)
    An = mm2(mm2(T, A), Ti)
    Bn = mm2(mm2(T, B), Ti)
    Cn = mm2(mm2(T, C), Ti)
    # scale freedom: conjugate by diag(d, 1/d) to make MU_n = [[1,1],[0,1]]:
    MUn = mm2(mm2(T, MU), Ti)
    u = MUn[0][1] / MUn[0][0] if abs(MUn[0][0]) > 0 else MUn[0][1]
    d = mp.sqrt(u)
    D = [[1 / d, mp.mpf(0)], [mp.mpf(0), d]]
    Di = [[d, mp.mpf(0)], [mp.mpf(0), 1 / d]]
    An = mm2(mm2(D, An), Di)
    Bn = mm2(mm2(D, Bn), Di)
    Cn = mm2(mm2(D, Cn), Di)
    ok, table = try_all({"a": An, "b": Bn, "c": Cn}, "normalized")

if ok:
    print("\n== S2a-G2/G3: exact verification in L ==", flush=True)
    from fractions import Fraction as Fr

    MOD = [Fr(16), Fr(0), Fr(8), Fr(0)]  # s^4 = 16 + 8 s^2 (run-2 sign fix)

    def pmulred(p, q):
        out = [Fr(0)] * 7
        for i, a_ in enumerate(p):
            if a_ == 0:
                continue
            for j, b_ in enumerate(q):
                out[i + j] += a_ * b_
        for k in range(6, 3, -1):
            c = out[k]
            if c != 0:
                out[k] = Fr(0)
                for t, m in enumerate(MOD):
                    out[k - 4 + t] += c * m
        return out[:4]

    class L:
        """elements of Q(s,i): (re, im) each a 4-vector over Q in powers of s."""
        __slots__ = ("re", "im")
        def __init__(self, re=None, im=None):
            self.re = re or [Fr(0)] * 4
            self.im = im or [Fr(0)] * 4
        def __add__(self, o):
            return L([a + b for a, b in zip(self.re, o.re)],
                     [a + b for a, b in zip(self.im, o.im)])
        def __sub__(self, o):
            return L([a - b for a, b in zip(self.re, o.re)],
                     [a - b for a, b in zip(self.im, o.im)])
        def __mul__(self, o):
            rr = pmulred(self.re, o.re)
            ii = pmulred(self.im, o.im)
            ri = pmulred(self.re, o.im)
            ir = pmulred(self.im, o.re)
            return L([a - b for a, b in zip(rr, ii)],
                     [a + b for a, b in zip(ri, ir)])
        def is_zero(self):
            return all(c == 0 for c in self.re) and \
                all(c == 0 for c in self.im)
        def __repr__(self):
            return f"L({self.re},{self.im})"

    def Lc(q):
        e = L()
        e.re = [Fr(q), Fr(0), Fr(0), Fr(0)]
        return e

    def to_L(cell):
        re, im = table[cell]
        return L([Fr(c) for c in re], [Fr(c) for c in im])

    def matL(nm):
        return [[to_L((nm, i, j)) for j in range(2)] for i in range(2)]

    aL, bL, cL = matL("a"), matL("b"), matL("c")

    def mmL(X, Y):
        return [[X[i][0] * Y[0][j] + X[i][1] * Y[1][j] for j in range(2)]
                for i in range(2)]

    def detL(Mx):
        return Mx[0][0] * Mx[1][1] - Mx[0][1] * Mx[1][0]

    def invL_proj(Mx):
        """projective inverse: adjugate (differs from inverse by det —
        harmless projectively; dets tracked separately)."""
        return [[Mx[1][1], Lc(0) - Mx[0][1]],
                [Lc(0) - Mx[1][0], Mx[0][0]]]

    # RUN-2 FINDING (in-trail): the polished PSL matrices are
    # UNNORMALIZED projective representatives — det(g) is a nontrivial
    # element of L (the exact det gate caught this in run 1 and the
    # 250-digit re-identification confirmed the entries ARE in L).
    # Gates go PROJECTIVE-EXACT: relators = scalar*I in L; trace
    # identities via tr^2/det (scale-free); the 27-lift for stage 2b
    # uses even Sym powers / det^m, which stays in L with NO roots.
    lets = {"a": aL, "b": bL, "c": cL,
            "A": invL_proj(aL), "B": invL_proj(bL), "C": invL_proj(cL)}
    for nm in ("a", "b", "c"):
        print(f"  det({nm}) = {detL(lets[nm])}", flush=True)

    def wordL(w):
        m = None
        for ch in w:
            m = lets[ch] if m is None else mmL(m, lets[ch])
        return m

    print("\n== S2a-G2' (projective-exact): relators = scalar * I ==",
          flush=True)
    for rel in G.relators():
        R = wordL(rel)
        off = R[0][1].is_zero() and R[1][0].is_zero()
        diag = (R[0][0] - R[1][1]).is_zero()
        print(f"  relator {rel}: scalar matrix exactly: {off and diag}"
              f" (lambda = {R[0][0] if off and diag else 'n/a'})",
              flush=True)

    print("\n== S2a-G3' (projective-exact): tr^2/det identities ==",
          flush=True)
    # targets^2 in L: mu: 4; lam: 4; b: 4; ac: (-s2-s2 i)^2 = 4i*? compute
    # (sqrt2 + sqrt2 i)^2 = 2 + 2*2i/2... do it exactly: sqrt2 = (s^2-4)/4.
    def sqrt2L():
        e = L()
        e.re = [Fr(-1), Fr(0), Fr(1, 4), Fr(0)]
        return e
    iL = L(); iL.im = [Fr(1), Fr(0), Fr(0), Fr(0)]
    t_ac_target = Lc(0) - sqrt2L() - sqrt2L() * iL
    t_abc_target = Lc(0) - Lc(2) * sqrt2L() * iL
    targets = {"CCB": Lc(2) * Lc(2), "caCA": Lc(2) * Lc(2),
               "b": Lc(2) * Lc(2),
               "ac": t_ac_target * t_ac_target,
               "abc": t_abc_target * t_abc_target}
    for w, tgt in targets.items():
        Wm = wordL(w)
        t = Wm[0][0] + Wm[1][1]
        lhs = t * t
        rhs = tgt * detL(Wm)
        ok2 = (lhs - rhs).is_zero()
        print(f"  tr({w})^2 = target^2 * det: {ok2}", flush=True)

    import json
    dump = {f"{nm}{i}{j}": [[str(x) for x in table[(nm, i, j)][0]],
                            [str(x) for x in table[(nm, i, j)][1]]]
            for nm in ("a", "b", "c") for i in range(2) for j in range(2)}
    with open(__file__.replace("b649_stage2a.py", "entries_L.json"),
              "w") as fh:
        json.dump(dump, fh, indent=1)
    print("  exact entries dumped to entries_L.json", flush=True)

print("\nB649 stage 2a DONE", flush=True)
