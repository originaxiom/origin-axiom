#!/usr/bin/env python3
"""The web seat's peer check of queue card Q0021 (fam3-v1-high-03): a second computation in other code, by other means.

The card verifies two cards of another seat. This script recomputes the parts of it whose definitions the card states
in full: the finite group G_T of rho_T and its scalars, the 64 sign dictionaries and their counts, the E_8
admissibility congruence and the exclusion of whole units, and the index vectors of the 16 and the 27 with the K2
vanishing sets. It works in exact integer arithmetic (monomial matrices with 24th-root exponents; weights in halves),
standard library only. It imports nothing of the producer's and reads no file of theirs.

THE DEFINITIONS USED (the card's definitions field). zeta = exp(2 pi i/24). rho_u(t) = [[i,0,0],[0,0,1],[0,1,0]],
rho_u(s) = [[0,0,-i],[0,-i,0],[-i,0,0]], chi_eta(t) = zeta, chi_eta(s) = exp(-i pi/4) = zeta^21, rho_T = chi_eta^21
rho_u, G_T = <rho_T(t), rho_T(s)>, Z = its scalars. Fields f = (Q, u^c, d^c, L, e^c, nu^c), s in {+-1}^6,
w_SU3 = (2,1,1,0,0,0), w_SU2 = (3,0,0,1,0,0), w_grav = (6,3,3,2,1,1), n_G = 9 sum w_G s_f mod 24, "G-free" when
n_G = 0; m_K = -9 (2 s_Q + s_u + s_d) mod 24 and 6 K_W = m_K mod 24; free on Z in F_c when the phase
zeta_4^(3 sum w_G s_f) is 1 for G = SU3, SU2, grav (this seat's reading of "F_c Z-phase"); F_S cubic
A = sum w_grav s_f, cubic-free when A = 0; I-31 is all s_f = +1. "Without nu^c" drops nu^c's term. E_8 admissibility:
c = 9 + 3(r + m) = 0 mod 24; the allowed twists r in {0, 4, 8, 12, 16, 20} are taken from the card. K2: n_G =
w_G c mod 24 with w_G(rep) = (1/2) sum over the rep's weights of <w, alpha_G>^2 and w_grav(rep) = dim; this script
takes the weights of the 16 (spinor, (+-1/2)^5 with an even number of minus signs) and of the 27 = 16 + 10 + 1 of
SO(10) in E_6, with alpha_SU3 = e1 - e2 and alpha_SU2 = e4 - e5 inside SU(5) (coordinates 1-3 and 4-5): that is,
from the weights of SO(10), not from the 240 roots of E_8 as the card does.

THE CONDITION, written before any of this was run. The card holds where this seat checks it if and only if all of:
  F1. |G_T| = 96, its scalar subgroup is exactly mu_4 = {1, i, -1, -i}, and det rho_T(g) = chi_eta(g)^9 for g = t, s.
  F2. Over the 64 dictionaries: 16 are SU3-free; none is SU2-free, the SU2 values being exactly {6, 12, 18}; of the 16
      SU3-free, 4 are gravity-free, and 0 when nu^c's term is dropped; for I-31, n_SU3 = 12 and K_W = 2 mod 4; I-31 is
      free on Z in F_c, and 8 of the 64 are; I-31's cubic is A = 16, and 4 of the 64 are cubic-free.
  F3. For every r and m mod 24, c = 0 mod 24 if and only if m = 5 - r mod 8; and no whole unit m = 24n is admissible at
      any allowed twist.
  F4. w(27) = (6, 6, 27) and w(16) = (4, 4, 16); among c = 0, 3, ..., 21 mod 24, K2 vanishes on the 27 only at c = 0 and
      on the 16 exactly at c in {0, 6, 12, 18}.
  Any one failing is a fault in the card as this seat reads it, or in this seat's reading; the note says which.

NOT CHECKED HERE: rho_H and its equivalence to rho_T; the uniform-scalar realization by the SM gauge group and by
E_6 U(1)_psi; the Riemann-Roch dimensions chi_k, the list of allowed twists, C8 = 3n against W134, and the 17/24
datum (they need rho(S), rho(T) and the B1641 pieces, which the card names but does not define); the K2 vectors from
E_8's 240 roots as such; the card's planted controls and float count.

    python3 relays/chat1_2026-11-28_peer/q0021_check.py            # the check; exits 0, prints the verdict
    python3 relays/chat1_2026-11-28_peer/q0021_check.py --control  # nu^c's gravity weight made 2 on purpose; exits 1
"""
import itertools
import sys
from fractions import Fraction

CONTROL = "--control" in sys.argv


def say(text):
    print("DECISIVE: " + text)


# ---------------------------------------------------------------- monomial matrices: column j -> zeta^e[j] e_{p[j]}
def mono_mul(A, B):
    (p, e), (q, f) = A, B
    return (tuple(p[q[j]] for j in range(3)), tuple((f[j] + e[q[j]]) % 24 for j in range(3)))


def scal(M, k):
    p, e = M
    return (p, tuple((x + k) % 24 for x in e))


def det_exp(M):
    p, e = M
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])
    return (sum(e) + (12 if inv % 2 else 0)) % 24


def f1():
    ut = ((0, 2, 1), (6, 0, 0))                  # [[i,0,0],[0,0,1],[0,1,0]]
    us = ((2, 1, 0), (18, 18, 18))               # [[0,0,-i],[0,-i,0],[-i,0,0]]
    chi_t, chi_s = 1, 21
    Tt, Ts = scal(ut, 21 * chi_t), scal(us, 21 * chi_s)
    one = ((0, 1, 2), (0, 0, 0))
    G, frontier = {one}, [one]
    while frontier:
        new = []
        for g in frontier:
            for x in (Tt, Ts):
                h = mono_mul(g, x)
                if h not in G:
                    G.add(h)
                    new.append(h)
        frontier = new
    scalars = sorted(g[1][0] for g in G if g[0] == (0, 1, 2) and len(set(g[1])) == 1)
    dets = (det_exp(Tt) == (9 * chi_t) % 24, det_exp(Ts) == (9 * chi_s) % 24)
    ok = len(G) == 96 and scalars == [0, 6, 12, 18] and all(dets)
    say("F1 |G_T| = %d; scalar exponents (of zeta_24) %s; det = chi_eta^9 at t, s: %s; as the card says: %s"
        % (len(G), scalars, dets, ok))
    return ok


def f2():
    w3, w2 = (2, 1, 1, 0, 0, 0), (3, 0, 0, 1, 0, 0)
    wg = (6, 3, 3, 2, 1, 2 if CONTROL else 1)    # wrong on purpose in the control
    dot = lambda w, s: sum(a * b for a, b in zip(w, s))
    S = list(itertools.product((1, -1), repeat=6))
    su3 = [s for s in S if (9 * dot(w3, s)) % 24 == 0]
    su2_vals = sorted({(9 * dot(w2, s)) % 24 for s in S})
    su2_free = [s for s in S if (9 * dot(w2, s)) % 24 == 0]
    grav = [s for s in su3 if (9 * dot(wg, s)) % 24 == 0]
    grav_no_nu = [s for s in su3 if (9 * dot(wg[:5], s[:5])) % 24 == 0]
    i31 = (1,) * 6
    n3 = (9 * dot(w3, i31)) % 24
    mK = (-9 * (2 * i31[0] + i31[1] + i31[2])) % 24
    KW = [k for k in range(4) if (6 * k) % 24 == mK]        # K_W mod 4 solving 6 K_W = m_K mod 24
    zfree = lambda s: all((3 * dot(w, s)) % 4 == 0 for w in (w3, w2, wg))
    n_zfree = sum(1 for s in S if zfree(s))
    A = dot(wg, i31)
    n_cubic = sum(1 for s in S if dot(wg, s) == 0)
    ok = len(su3) == 16 and not su2_free and su2_vals == [6, 12, 18] and len(grav) == 4 and not grav_no_nu and \
        n3 == 12 and KW == [2] and zfree(i31) and n_zfree == 8 and A == 16 and n_cubic == 4
    say("F2 SU3-free %d/64; SU2-free %d (values %s); gravity-free %d/16, %d without nu^c; I-31: n_SU3 = %d, "
        "K_W mod 4 in %s, free on Z: %s; Z-free %d/64; I-31 cubic A = %d; cubic-free %d/64; as the card says: %s"
        % (len(su3), len(su2_free), su2_vals, len(grav), len(grav_no_nu), n3, KW, zfree(i31), n_zfree, A, n_cubic,
           ok))
    return ok


def f3():
    equiv = all(((9 + 3 * (r + m)) % 24 == 0) == ((m - (5 - r)) % 8 == 0) for r in range(24) for m in range(24))
    whole = [(r, n) for r in (0, 4, 8, 12, 16, 20) for n in range(-5, 6) if (9 + 3 * (r + 24 * n)) % 24 == 0]
    ok = equiv and not whole
    say("F3 c = 0 mod 24 iff m = 5 - r mod 8: %s; admissible whole units at the allowed twists: %s; as the card "
        "says: %s" % (equiv, whole, ok))
    return ok


def f4():
    half = Fraction(1, 2)
    spin16 = [w for w in itertools.product((half, -half), repeat=5) if sum(1 for x in w if x < 0) % 2 == 0]
    vec10 = []
    for i in range(5):
        for sgn in (1, -1):
            v = [Fraction(0)] * 5
            v[i] = Fraction(sgn)
            vec10.append(tuple(v))
    one = [tuple([Fraction(0)] * 5)]
    a3 = (1, -1, 0, 0, 0)
    a2 = (0, 0, 0, 1, -1)
    ip = lambda w, a: sum(x * y for x, y in zip(w, a))

    def wvec(rep):
        return (int(half * sum(ip(w, a3) ** 2 for w in rep)), int(half * sum(ip(w, a2) ** 2 for w in rep)), len(rep))

    w16, w27 = wvec(spin16), wvec(spin16 + vec10 + one)
    cs = range(0, 24, 3)
    van27 = [c for c in cs if all((w * c) % 24 == 0 for w in w27)]
    van16 = [c for c in cs if all((w * c) % 24 == 0 for w in w16)]
    ok = w27 == (6, 6, 27) and w16 == (4, 4, 16) and van27 == [0] and van16 == [0, 6, 12, 18]
    say("F4 w(27) = %s, w(16) = %s; K2 vanishes on the 27 at c = %s and on the 16 at c = %s; as the card says: %s"
        % (w27, w16, van27, van16, ok))
    return ok


def main():
    verdict = all([f1(), f2(), f3(), f4()])
    if CONTROL:
        print("CONTROL: the checks %s the error made on purpose" % ("caught" if not verdict else "MISSED"))
        return 1 if not verdict else 0
    say("VERDICT: the card holds where this seat checks it (F1-F4): %s" % verdict)
    return 0


if __name__ == "__main__":
    sys.exit(main())
