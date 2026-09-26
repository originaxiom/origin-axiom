#!/usr/bin/env python3
"""B1380 -- THE PUNCTURE IS THE WORD'S.  Is the chain's puncture (P019's A5b; B749's fork F6; B1003's second FRAGILE axiom)
an independent choice, or is it already implied by the carrier axiom as P019 states it (A5: "the description is realized
as an action on a carrier: the rank-2 free group F2 with sigma's abelianization acting as a mapping class")?

Conventions: F2 = F(a, b), words are lists of nonzero ints (1 = a, 2 = b, negative = inverse); sigma is the Fibonacci
substitution a -> ab, b -> a (P019 T4), extended to F2; [a, b] = a b a^-1 b^-1; the abelianization matrix has the images'
letter counts as columns.

Sections (each asserts; the run log is puncture_run.txt):
  S1 sigma and sigma^2 are automorphisms of F2 (explicit inverses)
  S2 the fiber-level orientation dichotomy: an automorphism of F2 sends [a,b] to a conjugate of [a,b]^det (Nielsen),
     checked on sigma, sigma^2 and 300 seeded products of elementary Nielsen moves (instrument control)
  S3 no closed surface has fundamental group F2 (orientable: H1 rank; non-orientable: 2-torsion in H1)
  S4 the four compact surfaces with pi1 = F2 (chi = -1) and their peripheral classes in H1
  S5 realizability: sigma (any power) is induced by a homeomorphism of exactly one of the four -- the once-punctured
     torus (a boundary class nonzero in H1 would give sigma^ab^j an eigenvalue 1); controls: the criterion does not fire
     on automorphisms that ARE realized on the thrice-punctured sphere and the punctured Klein bottle
  S6 the description against its shadow: the Fibonacci word's n+1 factors of length n have exactly 2 abelianized
     (letter-count) images, for every n <= 60; positive words inject into F2 and not into Z^2
  S7 SnapPy: b++LR = m004 (sigma^2 on the once-punctured torus), b-+L = m000 = Gieseking (sigma itself, orientation
     reversing; its orientation cover is m004), m004(0,1) = the closed torus bundle (flat tetrahedra: Sol; H1 = Z)
Usage: python3 puncture.py"""
import sys, os, math, itertools, random, warnings
warnings.filterwarnings("ignore")
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

HERE = os.path.dirname(os.path.abspath(__file__))
A, B = 1, 2
COMM = [A, B, -A, -B]


def red(w):
    out = []
    for x in w:
        if out and out[-1] == -x:
            out.pop()
        else:
            out.append(x)
    return out


def inv(w):
    return [-x for x in reversed(w)]


def apply(phi, w):
    out = []
    for x in w:
        out += phi[x] if x > 0 else inv(phi[-x])
    return red(out)


def compose(phi, psi):                       # (phi o psi)(g) = phi(psi(g))
    return {g: apply(phi, psi[g]) for g in psi}


def cyc_red(w):
    w = red(w)
    while len(w) > 1 and w[0] == -w[-1]:
        w = w[1:-1]
    return w


def conjugate(u, v):                          # conjugate in a free group iff cyclic reductions are rotations
    u, v = cyc_red(u), cyc_red(v)
    return len(u) == len(v) and (not u or any(u[i:] + u[:i] == v for i in range(len(u))))


def ab(w):
    return (sum((x == A) - (x == -A) for x in w), sum((x == B) - (x == -B) for x in w))


def matrix(phi):
    ca, cb = ab(phi[A]), ab(phi[B])
    return sp.Matrix([[ca[0], cb[0]], [ca[1], cb[1]]])


SIGMA = {A: [A, B], B: [A]}
SIGMA_INV = {A: [B], B: [-B, A]}
SIGMA2 = compose(SIGMA, SIGMA)
ELEMENTARY = [{A: [A, B], B: [B]}, {A: [B, A], B: [B]}, {A: [A], B: [B, A]}, {A: [A], B: [A, B]},
              {A: [B], B: [A]}, {A: [-A], B: [B]}, {A: [A], B: [-B]}]


def s1_automorphisms():
    ok = all(apply(SIGMA, SIGMA_INV[g]) == [g] and apply(SIGMA_INV, SIGMA[g]) == [g] for g in (A, B))
    M1, M2 = matrix(SIGMA), matrix(SIGMA2)
    assert ok and M1 == sp.Matrix([[1, 1], [1, 0]]) and M2 == sp.Matrix([[2, 1], [1, 1]]) and M2 == M1 ** 2
    assert SIGMA2 == {A: [A, B, A], B: [A, B]}
    return ok, M1, M2


def s2_orientation(samples=300, seed=1380):
    img1, img2 = apply(SIGMA, COMM), apply(SIGMA2, COMM)
    s1 = (conjugate(img1, inv(COMM)), conjugate(img1, COMM))
    s2 = (conjugate(img2, COMM), conjugate(img2, inv(COMM)))
    assert s1 == (True, False) and s2 == (True, False)
    rng = random.Random(seed); good = 0; dets = {1: 0, -1: 0}
    for _ in range(samples):
        phi = {A: [A], B: [B]}
        for _ in range(rng.randint(1, 12)):
            phi = compose(phi, rng.choice(ELEMENTARY))
        d = matrix(phi).det(); dets[int(d)] += 1
        good += conjugate(apply(phi, COMM), COMM if d == 1 else inv(COMM))
    assert good == samples and dets[1] > 0 and dets[-1] > 0
    return s1, s2, good, dets


def s3_closed_surfaces(kmax=6):
    rows = []
    for g in range(0, 4):                          # orientable: H1 = Z^2g, torsion-free; F2 would need 2g = 2
        rows.append(("S_%d" % g, "Z^%d" % (2 * g), "abelian Z^2 (ab = ba), not free" if g == 1 else
                     ("trivial" if g == 0 else "H1 rank %d != 2" % (2 * g))))
    for k in range(1, kmax + 1):                    # non-orientable N_k: relator x1^2...xk^2 -> H1 = Z^(k-1) + Z/2
        snf = smith_normal_form(sp.Matrix([[2] * k]), domain=sp.ZZ)
        diag = [snf[0, 0]]
        rows.append(("N_%d" % k, "Z^%d + Z/%d" % (k - 1, abs(diag[0])), "2-torsion in H1: not free"))
        assert abs(diag[0]) == 2
    return rows


SURFACES = {                                        # (name, (genus, orientable), n boundary, peripheral words in F(x,y))
    "S(1,1) once-punctured torus": ((1, True), 1, [[A, B, -A, -B]]),
    "S(0,3) thrice-punctured sphere": ((0, True), 3, [[A], [B], inv([A, B])]),
    "N(1,2) twice-punctured projective plane": ((1, False), 2, [[B], inv([A, A, B])]),
    "N(2,1) once-punctured Klein bottle": ((2, False), 1, [inv([A, A, B, B])]),
}


def s4_the_four():
    found = []
    for g in range(0, 3):
        for n in range(1, 5):
            if 2 - 2 * g - n == -1:
                found.append(("orientable", g, n))
    for k in range(1, 4):
        for n in range(1, 5):
            if 2 - k - n == -1:
                found.append(("non-orientable", k, n))
    assert found == [("orientable", 0, 3), ("orientable", 1, 1), ("non-orientable", 1, 2), ("non-orientable", 2, 1)]
    classes = {name: [ab(w) for w in per] for name, (_, _, per) in SURFACES.items()}
    return found, classes


def fires(M, v, n):                                  # can some power M^j (j | 2 n!) fix the nonzero class v up to sign?
    v = sp.Matrix(v); N = 2 * math.factorial(n)
    return any((M ** j) * v == v or (M ** j) * v == -v for j in range(1, N + 1) if N % j == 0)


def s5_realizability():
    M1, M2 = matrix(SIGMA), matrix(SIGMA2)
    no_root = all((M1 ** j - sp.eye(2)).det() != 0 and (M1 ** j + sp.eye(2)).det() != 0 for j in range(1, 49))
    assert no_root
    verdict = {}
    for name, (_, n, per) in SURFACES.items():
        nonzero = [ab(w) for w in per if ab(w) != (0, 0)]
        blocked = bool(nonzero) and not any(fires(M, v, n) for M in (M1, M2) for v in nonzero)
        verdict[name] = "sigma NOT realizable (peripheral class %s nonzero in H1)" % (nonzero[0],) if blocked else \
            "sigma realizable: [a,b] -> conjugate of [a,b]^(+-1) (Nielsen; Dehn-Nielsen-Baer)"
    assert [k for k, v in verdict.items() if v.startswith("sigma realizable")] == ["S(1,1) once-punctured torus"]
    # controls: the criterion must NOT fire on automorphisms that are realized there
    swap = {A: [B], B: [A]}                           # on S(0,3): c1 <-> c2 (then (c1c2)^-1 -> (c2c1)^-1, conjugate)
    assert conjugate(apply(swap, inv([A, B])), inv([A, B]))
    ctrl_s03 = any(fires(matrix(swap), v, 3) for v in [(1, 0), (0, 1), (-1, -1)])
    kb_swap = {A: [B], B: [A]}                        # on N(2,1): x1 <-> x2 fixes x1^2 x2^2 up to conjugacy
    assert conjugate(apply(kb_swap, inv([A, A, B, B])), inv([A, A, B, B]))
    ctrl_n21 = fires(matrix(kb_swap), (-2, -2), 1)
    assert ctrl_s03 and ctrl_n21
    return no_root, verdict, (ctrl_s03, ctrl_n21)


def fibonacci_word(n_min=6000):
    w = [A]
    while len(w) < n_min:
        w = apply(SIGMA, w)
    return w


def s6_word_against_shadow(nmax=60):
    f = fibonacci_word()
    rows = []
    for n in range(1, nmax + 1):
        facs = {tuple(f[i:i + n]) for i in range(len(f) - n)}
        parikh = {ab(list(u)) for u in facs}
        rows.append((n, len(facs), len(parikh)))
    assert all(p == n + 1 and q == 2 for n, p, q in rows)
    words = [list(t) for m in range(1, 13) for t in itertools.product((A, B), repeat=m)]
    inject_F2 = len({tuple(red(w)) for w in words}) == len(words)
    inject_Z2 = len({ab(w) for w in words}) == len(words)
    assert inject_F2 and not inject_Z2 and ab([A, B]) == ab([B, A])
    freq = sum(1 for x in f if x == A) / len(f)
    return rows, inject_F2, inject_Z2, len(words), len({ab(w) for w in words}), freq


def s7_snappy():
    import snappy
    m004, m000 = snappy.Manifold("m004"), snappy.Manifold("m000")
    b2, b1 = snappy.Manifold("b++LR"), snappy.Manifold("b-+L")
    out = {
        "b++LR = m004": b2.is_isometric_to(m004), "b-+L = m000": b1.is_isometric_to(m000),
        "m000 orientable": m000.is_orientable(), "cover(m000) = m004": m000.orientation_cover().is_isometric_to(m004),
        "vol m000, m004": (round(float(m000.volume()), 10), round(float(m004.volume()), 10)),
    }
    C = snappy.Manifold("m004(0,1)")
    out["m004(0,1)"] = (C.solution_type(), str(C.homology()), round(float(C.volume()), 10))
    b1s = {}
    for p in range(-3, 4):
        for q in range(0, 4):
            if (p, q) != (0, 0) and math.gcd(p, q) == 1 and (q > 0 or p > 0):
                D = snappy.Manifold("m004"); D.dehn_fill((p, q))
                b1s[(p, q)] = D.homology().betti_number()
    out["b1 = 1 fillings"] = sorted(k for k, v in b1s.items() if v == 1)
    assert out["b++LR = m004"] and out["b-+L = m000"] and not out["m000 orientable"] and out["cover(m000) = m004"]
    assert out["m004(0,1)"][0] != "all tetrahedra positively oriented" and out["m004(0,1)"][1] == "Z"
    assert out["b1 = 1 fillings"] == [(0, 1)]
    return out


if __name__ == "__main__":
    print("S1  sigma, sigma^2 automorphisms of F2:", s1_automorphisms())
    s1, s2, good, dets = s2_orientation()
    print("S2  sigma([a,b]) ~ ([a,b]^-1, [a,b]):", s1, "| sigma^2([a,b]) ~ ([a,b], [a,b]^-1):", s2)
    print("    Nielsen control: %d/300 seeded automorphisms send [a,b] to a conjugate of [a,b]^det; det counts %s"
          % (good, dets))
    print("S3  closed surfaces never have pi1 = F2:")
    for r in s3_closed_surfaces():
        print("     ", r)
    found, classes = s4_the_four()
    print("S4  compact surfaces with chi = -1 and boundary (pi1 = F2):", found)
    for k, v in classes.items():
        print("      %-42s peripheral classes in H1: %s" % (k, v))
    no_root, verdict, ctrl = s5_realizability()
    print("S5  sigma^ab has no root-of-unity eigenvalue (det(M^j -+ I) != 0, j <= 48):", no_root)
    for k, v in verdict.items():
        print("      %-42s %s" % (k, v))
    print("    controls (criterion does not fire on realized maps): S(0,3) swap %s, N(2,1) swap %s" % ctrl)
    rows, i2, iz, nw, nz, freq = s6_word_against_shadow()
    print("S6  Fibonacci word: (n, #factors, #letter-count images) for n = 1..5, 30, 60:",
          [r for r in rows if r[0] in (1, 2, 3, 4, 5, 30, 60)])
    print("    all n <= 60: factors = n+1, images = 2:", all(p == n + 1 and q == 2 for n, p, q in rows))
    print("    positive words of length 1..12: %d; distinct in F2: %s; distinct in Z^2: %s (%d images); freq(a) = %.6f"
          " (1/phi = %.6f)" % (nw, i2, iz, nz, freq, 2 / (1 + 5 ** 0.5)))
    print("S7  SnapPy:", s7_snappy())
    print("DONE")
