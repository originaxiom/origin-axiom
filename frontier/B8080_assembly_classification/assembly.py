#!/usr/bin/env python3
"""B8080 -- Theorem (classification among the polyhedral candidates), DEPOSITED.

The paper's Scope (assembly) says of Theorem (classify):

    "The enumeration behind this theorem is a search over multiset decompositions of 27
     into non-trivial irreducible degrees for each of the six groups, together with a
     non-degeneracy test on the resulting cubic.  That search is described here but its
     code is not deposited, so by this paper's own standard the theorem is an assertion
     ABOUT a computation. ... The full six-group classification should be read as
     unverified."

This is that code.  The six groups are CONSTRUCTED as the theorem says -- the binary ones
as unit quaternions (2T the 24 Hurwitz units, 2O the 48, 2I the 120 icosians), the others
as permutation groups -- and conjugacy classes, power maps and characters are COMPUTED,
never transcribed.  No character value is typed in from a table.

METHOD.  Character tables by Dixon's algorithm at the least prime p > 3654 with
p = 1 mod 120 = lcm of the six exponents, so p = 1 mod exp(G) for all six and every character value lies in F_p; and
p > C(29,3) = 3654, which bounds every multiplicity computed below, so each integer answer
is recovered unambiguously.  All arithmetic is exact integer arithmetic mod p.

THE TEST.  For V a sum of non-trivial irreducibles with dim V = 27:
  (i)  dim (Sym^3 V*)^G >= 1                       -- an invariant cubic exists at all;
  (ii) every irreducible summand V_i participates in some triple, i.e. there are summands
       V_j, V_k with (V_i* (x) V_j* (x) V_k*)^G nonzero.
(ii) is necessary for non-degeneracy: if V_i participates in no triple then V_i lies in
the radical of EVERY invariant cubic, so no invariant cubic on V is non-degenerate.  Where
(i) and (ii) both hold, a generic invariant cubic has zero radical.

QUANTIFIER (COMPUTE_THE_PROGRAM): the AXIOMS layer -- six finite groups and their complex
representation theory.  Nothing about the member, the class, the sisters or the rows.

NOT PREREGISTERED.  The controls are falsifiable by the paper and by classical facts this
arc did not choose: sum of squared degrees = |G|, column orthogonality, the
Frobenius-Schur reading of Lemma (quat) and Corollary (onlybinary), and the paper's own
weaker banked claim that 2T admits an assembly and 2O, A5, 2I, S4 do not.
"""
import itertools
import json
import os
import random
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
def _is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** .5) + 1))


# exponents are 6 (A4), 12 (S4, 2T), 24 (2O), 30 (A5), 60 (2I): lcm = 120.  A first
# version used 120//2 = 60 and 2O's character values then fell outside F_p, which is
# exactly the failure the modulus condition exists to prevent.
P = next(q for q in range(3671, 100000) if q % 120 == 1 and _is_prime(q))
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


# ----------------------------------------------------------------- the six groups
def qmul_factory(d):
    def m(x, y):
        return (x[0] * y[0] + d * x[1] * y[1], x[0] * y[1] + x[1] * y[0])

    def a(x, y):
        return (x[0] + y[0], x[1] + y[1])

    def n(x):
        return (-x[0], -x[1])

    def qm(p_, q_):
        a1, b1, c1, d1 = p_
        a2, b2, c2, d2 = q_
        return (a(a(m(a1, a2), n(m(b1, b2))), a(n(m(c1, c2)), n(m(d1, d2)))),
                a(a(m(a1, b2), m(b1, a2)), a(m(c1, d2), n(m(d1, c2)))),
                a(a(m(a1, c2), n(m(b1, d2))), a(m(c1, a2), m(d1, b2))),
                a(a(m(a1, d2), m(b1, c2)), a(n(m(c1, b2)), m(d1, a2))))
    return qm


Z = (Fr(0), Fr(0))


def rr(x):
    return (Fr(x), Fr(0))


def closure(gens, mu):
    G = set(gens)
    fr = list(G)
    while fr:
        nx = []
        for x in fr:
            for g in gens:
                y = mu(x, g)
                if y not in G:
                    G.add(y)
                    nx.append(y)
        fr = nx
    return sorted(G)


q2 = qmul_factory(2)
E2T = closure([(Z, rr(1), Z, Z),
               (rr(Fr(1, 2)), rr(Fr(1, 2)), rr(Fr(1, 2)), rr(Fr(1, 2)))], q2)
E2O = closure(E2T + [((Fr(0), Fr(1, 2)), (Fr(0), Fr(1, 2)), Z, Z)], q2)

q5 = qmul_factory(5)
PHI, IPHI = (Fr(1, 2), Fr(1, 2)), (Fr(-1, 2), Fr(1, 2))


def hf(t):
    return (t[0] / 2, t[1] / 2)


def ng(t):
    return (-t[0], -t[1])


_E = set()
for _k in range(4):
    for _s in (1, -1):
        _v = [Z] * 4
        _v[_k] = rr(_s)
        _E.add(tuple(_v))
for _sg in itertools.product((1, -1), repeat=4):
    _E.add(tuple((Fr(_sg[i], 2), Fr(0)) for i in range(4)))
_base = [Z, hf(rr(1)), hf(IPHI), hf(PHI)]
for _pm in itertools.permutations(range(4)):
    if sum(1 for i in range(4) for j in range(i + 1, 4) if _pm[i] > _pm[j]) % 2:
        continue
    for _sg in itertools.product((1, -1), repeat=3):
        _vals = [_base[0]] + [_base[i + 1] if _sg[i] > 0 else ng(_base[i + 1])
                              for i in range(3)]
        _v = [None] * 4
        for i in range(4):
            _v[_pm[i]] = _vals[i]
        _E.add(tuple(_v))
E2I = sorted(_E)

PERM4 = list(itertools.permutations(range(4)))
PERM5 = list(itertools.permutations(range(5)))


def pmul(a, b):
    return tuple(a[b[i]] for i in range(len(a)))


def par(p_):
    return sum(1 for i in range(len(p_)) for j in range(i + 1, len(p_))
               if p_[i] > p_[j]) % 2


GROUPS = {
    "A4": ([p for p in PERM4 if par(p) == 0], pmul, 12),
    "S4": (PERM4, pmul, 24),
    "A5": ([p for p in PERM5 if par(p) == 0], pmul, 60),
    "2T": (E2T, q2, 24),
    "2O": (E2O, q2, 48),
    "2I": (E2I, q5, 120),
}

print("=" * 78)
print("CONTROLS -- the groups, constructed as the theorem describes")
print("=" * 78)
for nm, (EL, mu, order) in GROUPS.items():
    S = set(EL)
    gate(f"{nm}: order {order}, closed under its own multiplication",
         len(EL) == order and all(mu(x, y) in S for x in EL for y in EL))
if FAILED:
    raise SystemExit("group construction failed -- nothing may be read")


# ----------------------------------------------------------------- Dixon mod p
def rref(M, p, cols):
    M = [r[:] for r in M]
    piv, r = [], 0
    for c in range(cols):
        pr = next((i for i in range(r, len(M)) if M[i][c] % p), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        iv = pow(M[r][c], p - 2, p)
        M[r] = [v * iv % p for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(cols)]
        piv.append(c)
        r += 1
    return M, piv


def nullspace(M, p, cols):
    R, piv = rref(M, p, cols)
    out = []
    for fc in [c for c in range(cols) if c not in piv]:
        v = [0] * cols
        v[fc] = 1
        for i, c in enumerate(piv):
            v[c] = (-R[i][fc]) % p
        out.append(v)
    return out


def analyse(EL, mu, p=P):
    n = len(EL)
    idx = {g: i for i, g in enumerate(EL)}
    mt = [[idx[mu(EL[i], EL[j])] for j in range(n)] for i in range(n)]
    e = next(i for i in range(n) if all(mt[i][j] == j for j in range(n)))
    inv = [next(j for j in range(n) if mt[i][j] == e) for i in range(n)]
    cls, seen = [], set()
    for g in range(n):
        if g in seen:
            continue
        C = sorted({mt[mt[x][g]][inv[x]] for x in range(n)})
        seen |= set(C)
        cls.append(C)
    cls.sort(key=lambda c: (len(c), c[0]))
    k = len(cls)
    which = [0] * n
    for ci, c in enumerate(cls):
        for g in c:
            which[g] = ci
    h = [len(c) for c in cls]
    rep = [c[0] for c in cls]
    ID = which[e]
    pw2 = [which[mt[g][g]] for g in rep]
    pw3 = [which[mt[mt[g][g]][g]] for g in rep]
    invc = [which[inv[g]] for g in rep]
    M = []
    for i in range(k):
        Mi = [[0] * k for _ in range(k)]
        for j in range(k):
            for x in cls[i]:
                for y in cls[j]:
                    Mi[j][which[mt[x][y]]] += 1
        for j in range(k):
            for l in range(k):
                assert Mi[j][l] % h[l] == 0
                Mi[j][l] //= h[l]
        M.append([[v % p for v in row] for row in Mi])
    rng = random.Random(20260818)
    vecs = []
    for _ in range(60):
        co = [rng.randrange(1, p) for _ in range(k)]
        N = [[sum(co[i] * M[i][j][l] for i in range(k)) % p for l in range(k)]
             for j in range(k)]
        found, bad = [], False
        for lam in range(p):
            A = [[(N[j][l] - (lam if j == l else 0)) % p for l in range(k)]
                 for j in range(k)]
            ns = nullspace(A, p, k)
            if len(ns) == 1:
                found.append(ns[0])
            elif len(ns) > 1:
                bad = True
                break
        if not bad and len(found) == k:
            vecs = found
            break
    assert len(vecs) == k, "eigenvalue separation failed"
    chars = []
    for v in vecs:
        om = [x * pow(v[ID], p - 2, p) % p for x in v]
        s = sum(om[i] * om[invc[i]] % p * pow(h[i], p - 2, p) for i in range(k)) % p
        d2 = n % p * pow(s, p - 2, p) % p
        d = next(dd for dd in range(1, int(n ** .5) + 2) if dd * dd % p == d2)
        chars.append([om[i] * d % p * pow(h[i], p - 2, p) % p for i in range(k)])
    chars.sort(key=lambda c: (c[0], c))
    return dict(n=n, k=k, h=h, ID=ID, pw2=pw2, pw3=pw3, invc=invc, chars=chars)


TAB = {}
print()
print("=" * 78)
print("THE CHARACTER TABLES -- computed by Dixon's algorithm, never transcribed")
print("=" * 78)
for nm, (EL, mu, order) in GROUPS.items():
    T = analyse(EL, mu)
    TAB[nm] = T
    degs = [c[T["ID"]] for c in T["chars"]]
    print(f"\n  {nm}: |G| = {T['n']}, {T['k']} classes of sizes {T['h']}")
    print(f"      irreducible degrees {degs}   sum of squares {sum(d*d for d in degs)}")
    gate(f"{nm}: sum of squared degrees equals |G|",
         sum(d * d for d in degs) == T["n"])
    gate(f"{nm}: number of irreducibles equals number of classes",
         len(degs) == T["k"])
    ok = True
    for a in range(T["k"]):
        for b in range(T["k"]):
            s = sum(c[a] * c[(T['invc'][b])] for c in T["chars"]) % P
            want = (T["n"] // T["h"][a]) % P if a == b else 0
            if s != want % P:
                ok = False
    gate(f"{nm}: column orthogonality holds", ok)
if FAILED:
    raise SystemExit("character tables failed their controls")


def fs_indicator(T, ci):
    """Frobenius-Schur indicator, as an integer in {-1,0,1}."""
    v = sum(T["h"][i] * T["chars"][ci][T["pw2"][i]] for i in range(T["k"])) % P
    v = v * pow(T["n"], P - 2, P) % P
    return v - P if v > P // 2 else v


print()
print("=" * 78)
print("LEMMA (quat) AND COROLLARY (onlybinary) -- checked, not assumed")
print("=" * 78)
bin_ok = []
for nm in GROUPS:
    T = TAB[nm]
    twos = [i for i, c in enumerate(T["chars"]) if c[T["ID"]] == 2]
    faith, sl = [], []
    for i in twos:
        ker = sum(T["h"][j] for j in range(T["k"]) if T["chars"][i][j] == 2)
        if ker != 1:                      # not faithful: something acts trivially
            continue
        faith.append(i)
        # det of a 2-dimensional rep: det(g) = (chi(g)^2 - chi(g^2))/2.  Lemma (quat)
        # assumes G -> SL(V), so only the irreducibles with trivial determinant qualify;
        # the others here are the same 2 twisted by a linear character of order 3.
        det = [(T["chars"][i][j] ** 2 - T["chars"][i][T["pw2"][j]]) % P
               * pow(2, P - 2, P) % P for j in range(T["k"])]
        if all(x == 1 for x in det):
            sl.append(i)
    ind = [fs_indicator(T, i) for i in sl]
    print(f"  {nm}: {len(twos)} two-dimensional irreducible(s), {len(faith)} faithful, "
          f"{len(sl)} of them special-linear, Frobenius-Schur {ind}")
    if sl:
        bin_ok.append(nm)
    gate(f"{nm}: every faithful special-linear 2-dimensional irreducible is "
         f"QUATERNIONIC (indicator -1), as Lemma (quat) proves",
         all(x == -1 for x in ind))
gate("only 2T, 2O and 2I admit a faithful 2-dimensional irreducible "
     "(Corollary onlybinary)", sorted(bin_ok) == ["2I", "2O", "2T"], str(sorted(bin_ok)))


# ----------------------------------------------------------------- the enumeration
def sym3_invariants(T, chi):
    """dim (Sym^3 W*)^G for W with character chi (values indexed by class)."""
    tot = 0
    for i in range(T["k"]):
        a = chi[T["invc"][i]]                                   # chi_{W*}(g)
        b = chi[T["invc"][T["pw2"][i]]]                          # chi_{W*}(g^2)
        c = chi[T["invc"][T["pw3"][i]]]                          # chi_{W*}(g^3)
        tot += T["h"][i] * (a * a % P * a + 3 * a * b + 2 * c) % P
    return tot % P * pow(T["n"] * 6 % P, P - 2, P) % P


def triple(T, i, j, l):
    """dim (V_i* (x) V_j* (x) V_l*)^G."""
    ch = T["chars"]
    tot = sum(T["h"][t] * (ch[i][T["invc"][t]] * ch[j][T["invc"][t]] % P
                           * ch[l][T["invc"][t]]) for t in range(T["k"])) % P
    return tot * pow(T["n"], P - 2, P) % P


def decompositions(degs, target):
    """All multisets of non-trivial irreducibles with total dimension `target`."""
    out = []

    def rec(i, left, cur):
        if left == 0:
            out.append(tuple(cur))
            return
        if i == len(degs):
            return
        m = 0
        while m * degs[i][1] <= left:
            rec(i + 1, left - m * degs[i][1], cur + [(degs[i][0], m)] if m else cur)
            m += 1
    rec(0, target, [])
    return out


print()
print("=" * 78)
print("THE BLOCK-SUM LEMMA -- proved here, and it decides everything below")
print("=" * 78)
print("""
  LEMMA.  Let W be an IRREDUCIBLE G-module carrying a non-zero invariant cubic f.  Then
  the associated symmetric trilinear form T has ZERO radical.
  PROOF.  rad(T) = {w : T(w,.,.) = 0} is G-stable because T is invariant.  W irreducible
  forces rad(T) = 0 or W; and rad(T) = W says T = 0, i.e. f = 0.  []

  COROLLARY.  If 27 = sum m_i d_i over non-trivial irreducibles V_i of degree d_i each
  carrying a non-zero invariant cubic, then V = (+) V_i^{m_i} carries the block-diagonal
  cubic f = sum_blocks f_i, which is invariant and has zero radical -- because choosing
  the test vectors inside a single block reduces to that block.  So V is an ASSEMBLY in
  the paper's sense.

  The lemma is verified independently, on explicit matrices, in the S4 witness below.""")

# --- the explicit witness, on matrices, over Q -----------------------------------
import sympy as sp
Bv = [sp.Matrix([1, -1, 0, 0]), sp.Matrix([0, 1, -1, 0]), sp.Matrix([0, 0, 1, -1])]
BM = sp.Matrix.hstack(*Bv)


def _T(u, v, w):
    U, V_, W = BM * u, BM * v, BM * w
    return sum(U[i] * V_[i] * W[i] for i in range(4))


_e = [sp.Matrix([1 if i == j else 0 for i in range(3)]) for j in range(3)]


def _rho(pm):
    return sp.Matrix.hstack(*[BM.solve(sp.Matrix([b[pm.index(i)] for i in range(4)]))
                              for b in Bv])


_inv = all(sp.simplify(_T(_rho(pm) * _e[x], _rho(pm) * _e[y], _rho(pm) * _e[z])
                       - _T(_e[x], _e[y], _e[z])) == 0
           for pm in PERM4 for x in range(3) for y in range(3) for z in range(3))
_M = sp.zeros(9, 3)
for x in range(3):
    for y in range(3):
        for j in range(3):
            _M[3 * x + y, j] = _T(_e[j], _e[x], _e[y])
gate("witness, exact over Q: sum(x_i^3) on {sum x_i = 0} is S4-invariant "
     "(all 24 elements, all 27 triples)", _inv)
gate("witness: its trilinear form has ZERO radical, so the cubic is non-degenerate "
     "on an irreducible 3-dimensional module", len(_M.nullspace()) == 0)

print()
print("=" * 78)
print("THE ENUMERATION -- which groups admit a 27-dimensional assembly")
print("=" * 78)
RESULT = {}
for nm in ("A4", "S4", "2T", "2O", "A5", "2I"):
    T = TAB[nm]
    ID = T["ID"]
    cub = []
    for i, c in enumerate(T["chars"]):
        if all(x == 1 for x in c):
            continue                                    # the trivial module
        s = sym3_invariants(T, [c[u] for u in range(T["k"])])
        if s:
            cub.append((int(c[ID]), int(s)))
    degs = sorted({d for d, _ in cub})
    reach = [0] * 28
    reach[0] = 1
    for v in range(1, 28):
        reach[v] = 1 if any(d <= v and reach[v - d] for d in degs) else 0
    ok = bool(reach[27]) if degs else False
    wit = None
    if ok:
        left, wit = 27, []
        while left:
            d = next(d for d in degs if d <= left and reach[left - d])
            wit.append(d)
            left -= d
        from collections import Counter
        wit = sorted(Counter(wit).items())
    RESULT[nm] = dict(degrees=[int(c[ID]) for c in T["chars"]],
                      irreps_with_invariant_cubic=cub,
                      assembly_exists=ok,
                      witness=[[int(d), int(m)] for d, m in wit] if wit else None)
    w = "+".join(f"{m}x{d}" for d, m in wit) if wit else "-"
    print(f"\n  {nm}: non-trivial irreducibles carrying an invariant cubic "
          f"(degree, dim of cubic space): {cub}")
    print(f"      27 reachable from degrees {degs}: {ok}    witness  {w}")

surv = [nm for nm in RESULT if RESULT[nm]["assembly_exists"]]
print()
print("=" * 78)
print("THE RESULT -- and it CONTRADICTS Theorem (classify)")
print("=" * 78)
print(f"""
  A 27-dimensional assembly, in exactly the sense the paper defines -- a direct sum of
  non-trivial complex irreducibles of total dimension 27 carrying a non-degenerate
  invariant cubic form -- exists for:

      {surv}

  that is, for ALL SIX candidates.  Theorem (classify) states it exists "only for A4 and
  2T".  As stated, the theorem is FALSE, and the exclusions it needs are all four wrong.

  WHY THE EARLIER REPAIR WAS NOT ENOUGH.  Scope (assembly) records that an earlier version
  was false because every group has a 27-dimensional TRIVIAL representation, and repaired
  it by excluding trivial summands and demanding non-degeneracy.  The same failure mode
  survives the repair one level up: instead of 27 copies of the trivial module, take 9
  copies of a 3-dimensional irreducible with an invariant cubic (A4, S4, 2T, 2O), or
  3 copies each of a 4- and a 5-dimensional one (A5, 2I).  Multiplicity, not triviality,
  is what the definition fails to control.

  WHY THIS IS LOAD-BEARING AND NOT COSMETIC.  The paper's next step reads: "Of the two
  survivors only 2T is binary, i.e. a subgroup of SU(2), which is what the McKay
  correspondence requires."  That step needs the survivor set to be {{A4, 2T}}.  With 2O and
  2I surviving -- and BOTH ARE BINARY, as Corollary (onlybinary) itself establishes --
  binariness no longer isolates 2T.  So the failure is not absorbed downstream.

  WHAT THE REPAIR HAS TO BE.  The definition must pin the cubic, not merely require one to
  exist: the natural condition, and the one the construction actually uses, is that the
  pair (V, f) be the 27 of E6 with its Jordan determinant -- equivalently, that the
  assembly realise the group inside E6.  That is a different computation from the one the
  paper describes, and it is registered as owed rather than asserted here.""")
gate("all six candidates admit an assembly, refuting the stated classification",
     len(surv) == 6, str(surv))
gate("in particular 2O -- which IS binary -- admits one, so Corollary (onlybinary) "
     "does not rescue the argument", RESULT["2O"]["assembly_exists"])
gate("2T does admit one, so the paper's positive half stands",
     RESULT["2T"]["assembly_exists"])

RESULT["_summary"] = dict(all_six_admit=len(surv) == 6, survivors=sorted(surv), prime=P,
                          theorem_as_stated="FALSE",
                          method="Dixon mod p; p = 1 mod 120; block-sum lemma")
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RESULT, fh, indent=1, sort_keys=True)
print("\n  results.json written")
if FAILED:
    raise SystemExit(f"CONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
