"""B1258 -- 2T CANNOT SELECT THE EMBEDDING, and neither can the SO(10) grading.

B1257 named a canonical selector (Brieskorn-Slodowy picks the subregular orbit uniquely,
and it is the embedding giving three chiral generations).  Earning I-25 needs the OBJECT
to confirm it.  This arc runs the two natural object-internal tests.  BOTH COME BACK BLIND,
one of them by a theorem -- so the discriminator is not where anyone would look first.

TEST 1 -- the 27|2T branching (B327's gate).  BLIND, and provably so.
  chi_27 on 2T's seven classes is IDENTICAL for the two candidates: (27,27,3,0,0,0,0).
  So is chi_78.  The mechanism:
    (a) lambda = 1  : chi_Sym^n = n+1, so the sum is the DIMENSION -- 27 for both.
    (b) lambda = -1 : chi = (n+1)(-1)^n, and ALL indices are EVEN in both -- again the dimension.
    (c) lambda of order m in {3,4,6} (2T's remaining classes): chi_Sym^n depends ONLY on
        n mod m, and the index multisets AGREE mod 3, mod 4 and mod 6:
            principal  n = {16,8,0}      subregular n = {12,8,4}
            mod 3: [0,1,2] = [0,1,2]   mod 4: [0,0,0] = [0,0,0]   mod 6: [0,2,4] = [0,2,4]
  Hence the equality of characters is FORCED, not accidental.  NOTE the scope correction:
  B327's branching gate, used to sharpen the hierarchy CRUX, is blind to this distinction.

TEST 2 -- compatibility with the SO(10) grading D2.  BLIND for a different reason.
  Neither candidate makes the 16 (D2 = +1) a union of complete sl2 strings -- and neither
  makes the 10+1 one either.  Consistent with B1255's [C18, D2|W18] != 0: the object's
  gradings and its sl2 structure are transverse, not aligned.

CONSEQUENCE.  I-25 stays UNEARNED and the search space for its discriminator is narrowed by
two: not the finite-group branching (theorem), not the SO(10) compatibility (computation).

CONTROLS (MB12, both directions):
  - the character test is NOT vacuous: a 27-decomposition whose indices differ mod 12
    (n = {10,9,5}) gives a DIFFERENT character, exhibited;
  - the periodicity claim is verified per modulus rather than asserted, and the naive
    "period 12 for all n" version is exhibited as FALSE (it fails at lambda = 1, where
    chi = n+1 grows) -- this arc's own first statement of the mechanism, corrected;
  - dimensions reconstruct to 27 and 78 in every decomposition used.
"""
import collections, itertools, json, os
import sympy as sp

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
I = sp.I
CLASSES = [("1", 1, sp.Integer(1), 1), ("-1", 1, sp.Integer(-1), 2), ("ord4", 6, I, 4),
           ("ord6", 4, sp.exp(I*sp.pi/3), 6), ("ord3", 4, sp.exp(2*I*sp.pi/3), 3),
           ("ord3'", 4, sp.exp(-2*I*sp.pi/3), 3), ("ord6'", 4, sp.exp(-I*sp.pi/3), 6)]
CARTAN = sp.Matrix([[2,0,-1,0,0,0],[0,2,0,-1,0,0],[-1,0,2,-1,0,0],
                    [0,-1,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,2]])
PRIN, SUB = (2,2,2,2,2,2), (2,2,2,0,2,2)
W13 = [1, 0, -1, 0, 1, -1]


def chi_n(n, lam):
    return sp.nsimplify(sp.simplify(sum(lam**(n-2*k) for k in range(n+1))))


def chi_sum(ns, lam):
    return sp.nsimplify(sp.simplify(sum(sum(lam**(n-2*k) for k in range(n+1)) for n in ns)))


def _setup():
    R = json.load(open(os.path.join(REPO, "frontier", "B883_the_27", "rep27.json")))
    rep = [[[int(v) for v in row] for row in R["rep"][str(k)]] for k in range(78)]
    WT = [tuple(rep[i][a][a] for i in range(6)) for a in range(27)]
    roots = [v for v in itertools.product(range(-3,4), repeat=6)
             if (sp.Matrix(6,1,list(v)).T*CARTAN*sp.Matrix(6,1,list(v)))[0,0] == 2]
    return WT, CARTAN.inv(), roots


def strings(vals):
    m = collections.Counter(vals); out = []
    while sum(m.values()):
        top = max(k for k in m if m[k] > 0)
        if top < 0: return None
        out.append(top)
        for v in range(top, -top-1, -2):
            m[v] -= 1
            if m[v] < 0: return None
    return sorted(out, reverse=True)


def selftest():
    print("B1258 -- 2T is blind, and so is the SO(10) grading (selftest)")
    WT, Cinv, roots = _setup()

    def hv(c, weights):
        coef = Cinv * sp.Matrix(6,1,list(c))
        return [int(sum(w[i]*coef[i] for i in range(6))) for w in weights]

    p27, s27 = strings(hv(PRIN, WT)), strings(hv(SUB, WT))
    assert [k+1 for k in p27] == [17,9,1] and [k+1 for k in s27] == [13,9,5]
    # roots pair with h DIRECTLY (alpha = sum n_j alpha_j  =>  <alpha,h> = sum n_j c_j);
    # the inverse Cartan is only for weights given by Dynkin labels.
    def hroot(c):
        return [sum(r[j]*c[j] for j in range(6)) for r in roots] + [0]*6
    p78 = strings(hroot(PRIN))
    s78 = strings(hroot(SUB))
    assert sum(k+1 for k in p78) == 78 and sum(k+1 for k in s78) == 78
    print(f"  [dec ] 27: principal {[k+1 for k in p27]}  subregular {[k+1 for k in s27]}")
    print(f"  [dec ] 78: principal {[k+1 for k in p78]}  subregular {[k+1 for k in s78]}")

    # TEST 1 -- the characters
    for nm, a, b in (("27", p27, s27), ("78", p78, s78)):
        ra = [chi_sum(a, lam) for _,_,lam,_ in CLASSES]
        rb = [chi_sum(b, lam) for _,_,lam,_ in CLASSES]
        same = all(sp.simplify(x-y) == 0 for x, y in zip(ra, rb))
        print(f"  [T1  ] chi_{nm} on 2T's 7 classes: {ra}   identical? {same}")
        assert same

    # the mechanism, per modulus
    P, S = [k for k in p27], [k for k in s27]
    assert all(n % 2 == 0 for n in P + S), "lambda=-1 arm needs all indices even"
    for m, lam in ((3, sp.exp(2*I*sp.pi/3)), (4, I), (6, sp.exp(I*sp.pi/3))):
        per = all(sp.simplify(chi_n(n, lam) - chi_n(n+m, lam)) == 0 for n in range(10))
        agree = sorted(n % m for n in P) == sorted(n % m for n in S)
        print(f"  [mech] order {m}: chi periodic mod {m}? {per};  index multisets agree mod {m}? {agree}")
        assert per and agree

    # CONTROL A -- the naive "period 12 everywhere" claim is FALSE (this arc's own first version)
    naive = all(sp.simplify(chi_n(n, sp.Integer(1)) - chi_n(n+12, sp.Integer(1))) == 0 for n in range(3))
    print(f"  [ctl ] naive 'chi periodic mod 12 on EVERY class' -- false at lambda=1: {not naive}")
    assert not naive

    # CONTROL B -- the test is not vacuous
    A = [10, 9, 5]
    assert sum(n+1 for n in A) == 27
    ra = [chi_sum(A, lam) for _,_,lam,_ in CLASSES]
    rb = [chi_sum(P, lam) for _,_,lam,_ in CLASSES]
    print(f"  [ctl ] indices differing mod 12 (n={A}) give a DIFFERENT character: "
          f"{any(sp.simplify(x-y) != 0 for x, y in zip(ra, rb))}")
    assert any(sp.simplify(x-y) != 0 for x, y in zip(ra, rb))

    # TEST 2 -- SO(10) compatibility
    sgn = [(-1)**(sum(a*b for a, b in zip(W13, WT[t])) + 1) for t in range(27)]
    assert sum(1 for s in sgn if s == -1) == 11
    for nm, c in (("principal", PRIN), ("subregular", SUB)):
        h = hv(c, WT)
        plus  = [h[i] for i in range(27) if sgn[i] == 1]
        minus = [h[i] for i in range(27) if sgn[i] == -1]
        print(f"  [T2  ] {nm}: the 16 a union of complete sl2 strings? {strings(plus) is not None};"
              f"  the 10+1? {strings(minus) is not None}")
        assert strings(plus) is None and strings(minus) is None

    print("\n  => BOTH object-internal tests are BLIND. I-25's discriminator is neither the")
    print("     finite-group branching (by theorem) nor the SO(10) compatibility (by computation).")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
