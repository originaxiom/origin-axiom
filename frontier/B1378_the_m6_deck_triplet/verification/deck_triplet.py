#!/usr/bin/env python3
"""B1378 -- THE M6 DECK TRIPLET.  On Y6 (the degree-6 cyclic cover of m004, in its Reidemeister-Schreier
presentation, rs_presentation.py), a single non-split B1374/B1375 background sits in a genuine order-3 orbit of
the native deck group; each of the three orbit members has six-sector Standard-Model-frame index (-1)^6, and their
rank-6 direct sum (a legitimate reducible module, by additivity of cohomology over a direct sum) has EXACT index
(-3)^6 -- six sector-by-six-sector, this is the first exact three-generation-SHAPED index this branch's tower has
produced from one internally generated three-cycle, rather than by hand-inserting three copies.

Provenance (own verification, not a copy): the construction (seed character/cocycle, the deck-orbit map on
characters, the six SM sectors) is reported by an external research seat's audit package (seat "0925",
2026-09-25, harvested this branch's scratchpad from an uploaded checkpoint archive; see FINDINGS.md Sec. 0 for the
exact source and what if anything was taken on trust).  Independently re-verified here over three prime fields and
exactly over Q(zeta_8), using this branch's OWN index_lib.py / exact_lib.py (B1374), not the source's script.  One
genuine error was found and corrected in the source's account of the deck orbit's automorphism (see
rs_presentation.py's TAU2 comment) -- it does not affect the index computation below, which never uses that map;
it is relevant only to Sec. 3's genuineness check (do the three members form a literal automorphism orbit).

Usage: python3 deck_triplet.py"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                                 "B1374_the_class_index_in_the_sm_frame", "verification"))
from index_lib import GF, Rep, module, index, reducible_rep, h1_and_cocycle
from exact_lib import Cyc, data
import rs_presentation as P

GENS = list(P.LETTERS)                                           # "abcdefg" = z, x0..x5
RELS = P.RELS_STR
MU, LAM = P.MU_STR, P.LAM_STR
N = 120
SECT = [("Q", 1, 3), ("u^c", -4, 3), ("e^c", 6, 3), ("d^c", 2, 1), ("L", -3, 1), ("nu^c", 0, -5)]
SEED_CHI = (0, 0, 15, 45, 0, 75, 105)
SEED_Y = (0, 0, 0, 0, 0, 0, 0)
SEED_G = (0, 30, 15, 15, 30, 75, 75)
PRIMES = (601, 1201, 1321)


def deck(c, k=1):
    """the deck group's action on a character (or a character-shaped exponent tuple), by k steps of the order-6
    generator TAU: pullback along conjugation by a (source construction, reproduced verbatim -- see Sec. 2 for the
    direct cross-check against evaluating the TAU word map on an abelian character)."""
    z0 = c[0]; xs = list(c[1:])
    for _ in range(k):
        xs = xs[1:] + [(z0 + xs[0]) % N]
    return (z0, *xs)


def cadd(a, b): return tuple((x + y) % N for x, y in zip(a, b))
def cmul(a, k): return tuple((k * x) % N for x in a)


def blockdiag(F, mats):
    dims = [len(A) for A in mats]; D = sum(dims); O = F.zeros(D, D); off = 0
    for A, d in zip(mats, dims):
        for i in range(d):
            for j in range(d): O[off + i][off + j] = A[i][j]
        off += d
    return O


def run_prime(p):
    F = GF(p); z = F.root_of_unity(N)
    orbit = [(deck(SEED_CHI, 2 * j), deck(SEED_Y, 2 * j), deck(SEED_G, 2 * j)) for j in range(3)]
    assert len(set(orbit)) == 3, "the three deck-orbit members must be distinct characters"
    members_idx = []; sector_reps = [[] for _ in SECT]
    for cc, yy, gg in orbit:
        chi = dict(zip(GENS, cc)); chi2 = {g: pow(z, 2 * chi[g], p) for g in GENS}
        h1, ct = h1_and_cocycle(F, GENS, RELS, MU, LAM, chi2)
        assert h1 == 1 and ct is not None, "the seed character must have a unique non-split extension class"
        chi_val = {g: pow(z, chi[g], p) for g in GENS}
        rho = reducible_rep(F, GENS, chi_val, ct)
        Rrho = Rep(F, GENS, rho); assert Rrho.check_relators(RELS)
        row = []
        for si, (lab, sy, sg) in enumerate(SECT):
            psi_exp = dict(zip(GENS, cadd(cmul(yy, sy), cmul(gg, sg))))
            psi_val = {g: pow(z, psi_exp[g], p) for g in GENS}
            V = Rep(F, GENS, module(F, GENS, rho, 1, psi_val)); assert V.check_relators(RELS)
            I, dV, dVd = index(V, RELS, MU, LAM); row.append(I); sector_reps[si].append(V)
        members_idx.append(row)
    assert all(r == [-1] * 6 for r in members_idx), (p, members_idx)
    sums = []
    for si, (lab, _, __) in enumerate(SECT):
        reps = sector_reps[si]
        big = Rep(F, GENS, {g: blockdiag(F, [R.M[g] for R in reps]) for g in GENS})
        I, dV, dVd = index(big, RELS, MU, LAM); assert I == -3, (p, lab, I)
        sums.append((lab, I, dV, dVd))
    return members_idx, sums


# ---------------------------------------------------------------- exact, over Q(zeta_8)
def inverse_general(K, A):
    """Gauss-Jordan inverse of an n x n matrix over K = Cyc(N) (exact_lib's inverse2 only handles 1x1/2x2; kept
    local to this arc rather than touching the shared exact_lib.py, so B1374/B1375's locks are untouched)."""
    n = len(A); M = [row[:] + [K.const(1) if i == j else K.const(0) for j in range(n)] for i, row in enumerate(A)]
    for col in range(n):
        piv = next(r for r in range(col, n) if not K.is_zero(M[r][col]))
        M[col], M[piv] = M[piv], M[col]
        iv = K.inv(M[col][col]); M[col] = [K.mul(iv, x) for x in M[col]]
        for r in range(n):
            if r != col and not K.is_zero(M[r][col]):
                f = M[r][col]; M[r] = [K.sub(x, K.mul(f, y)) for x, y in zip(M[r], M[col])]
    return [row[n:] for row in M]


class KRepN:
    """like exact_lib.KRep, but with a general n x n inverse (needed for the rank-6 block-diagonal sum)."""
    def __init__(self, K, gens, mats):
        self.K = K; self.gens = gens; self.d = len(mats[gens[0]]); self.M = dict(mats)
        for g in gens: self.M[g.upper()] = inverse_general(K, mats[g])
    def word(self, w):
        R = self.K.eye(self.d)
        for ch in w: R = self.K.mmul(R, self.M[ch])
        return R
    def fox(self, w):
        K = self.K; D = {g: K.zeros(self.d, self.d) for g in self.gens}; pre = K.eye(self.d)
        for ch in w:
            g = ch.lower()
            if ch.islower(): D[g] = K.madd(D[g], pre)
            else: D[g] = K.msub(D[g], K.mmul(pre, self.M[ch]))
            pre = K.mmul(pre, self.M[ch])
        return D
    def dual(self): return KRepN(self.K, self.gens, {g: self.K.T(inverse_general(self.K, self.M[g])) for g in self.gens})


def to8(t): return tuple((x // 15) % 8 for x in t)


def run_exact():
    K = Cyc(8)
    orbit = [(to8(deck(SEED_CHI, 2 * j)), to8(deck(SEED_Y, 2 * j)), to8(deck(SEED_G, 2 * j))) for j in range(3)]
    members_idx = []; sector_reps = [[] for _ in SECT]
    for cc, yy, gg in orbit:
        chi = dict(zip(GENS, cc)); chi2 = {g: K.zeta((2 * chi[g]) % 8) for g in GENS}
        rep1 = KRepN(K, GENS, {g: [[chi2[g]]] for g in GENS})
        d1 = K.vstack(*[K.hstack(*[rep1.fox(r)[g] for g in GENS]) for r in RELS])
        Z = K.nullspace(d1, len(GENS))
        bvec = [K.sub(chi2[g], K.const(1)) for g in GENS]; rb = 0 if all(K.is_zero(x) for x in bvec) else 1
        assert len(Z) - rb == 1
        ct = next(dict(zip(GENS, z)) for z in Z if rb == 0 or K.rank([bvec, z]) == 2)
        chiv = {g: K.zeta(chi[g] % 8) for g in GENS}
        rho = {g: [[chiv[g], K.mul(ct[g], K.inv(chiv[g]))], [K.const(0), K.inv(chiv[g])]] for g in GENS}
        Rrho = KRepN(K, GENS, rho); assert all(Rrho.word(r) == K.eye(2) for r in RELS)
        row = []
        for si, (lab, sy, sg) in enumerate(SECT):
            psi_exp = tuple((sy * a + sg * b) % 8 for a, b in zip(yy, gg))
            psiv = {g: K.zeta(psi_exp[i]) for i, g in enumerate(GENS)}
            Vmats = {g: K.mscale(psiv[g], rho[g]) for g in GENS}
            V = KRepN(K, GENS, Vmats); assert all(V.word(r) == K.eye(2) for r in RELS)
            a0, a1, t0, t1, r1 = data(V, RELS, MU, LAM)
            b0, b1, s0, s1, q1 = data(V.dual(), RELS, MU, LAM)
            I = (a1 - r1) - (b1 - q1); row.append(I); sector_reps[si].append(V)
        members_idx.append(row)
    assert all(r == [-1] * 6 for r in members_idx), members_idx
    sums = []
    for si, (lab, _, __) in enumerate(SECT):
        reps = sector_reps[si]
        big = KRepN(K, GENS, {g: blockdiag_K(K, [R.M[g] for R in reps]) for g in GENS})
        a0, a1, t0, t1, r1 = data(big, RELS, MU, LAM); b0, b1, s0, s1, q1 = data(big.dual(), RELS, MU, LAM)
        I = (a1 - r1) - (b1 - q1); assert I == -3, (lab, I); sums.append((lab, I, (a0, a1, t0, r1), (b0, b1, s0, q1)))
    return members_idx, sums


def blockdiag_K(K, mats):
    dims = [len(A) for A in mats]; D = sum(dims); O = [[K.const(0)] * D for _ in range(D)]; off = 0
    for A, d in zip(mats, dims):
        for i in range(d):
            for j in range(d): O[off + i][off + j] = A[i][j]
        off += d
    return O


# ---------------------------------------------------------------- Sec. 2: deck() is the abelian pullback by TAU
def _chi_of_word(chi_tuple, word):
    v = 0
    for L in word:
        g = abs(L); v += chi_tuple[g - 1] if L > 0 else -chi_tuple[g - 1]
    return v % N


TAU = {1: [1], 2: [3], 3: [4], 4: [5], 5: [6], 6: [7], 7: [1, 2, -1]}       # TAU (order 6), same derivation as TAU2


def cross_check_deck_is_tau_pullback():
    """deck(c, 1) should equal the direct pullback c(TAU(-)) whenever c(z) = 0 (conjugation-invariance of an
    abelian character kills the wraparound's extra a^6-conjugation term); confirmed on the three seeds (all have
    chi(z) = 0, which is why the source's deck() formula, which is NOT the general pullback formula off that locus,
    is nonetheless exactly correct for every character this arc uses)."""
    for name, c in [("SEED_CHI", SEED_CHI), ("SEED_Y", SEED_Y), ("SEED_G", SEED_G)]:
        assert c[0] == 0
        direct = tuple(_chi_of_word(c, TAU[g]) for g in range(1, 8))
        assert deck(c, 1) == direct, (name, deck(c, 1), direct)
    # off the z(=0)-locus the two formulas genuinely differ (deck() carries an inert "+z0" term) -- not a live bug
    # for this arc (every character used has chi(z) = 0), demonstrated so the agreement above is not vacuous:
    off_locus = (7, 11, 13, 17, 19, 23, 29)
    assert deck(off_locus, 1) != tuple(_chi_of_word(off_locus, TAU[g]) for g in range(1, 8))
    return True


# ---------------------------------------------------------------- Sec. 3: the genuineness argument
def genuineness_argument(p=601):
    """Is the three-member 'orbit' a genuine TAU-automorphism orbit, or just three unrelated characters that happen
    to give matching index?  A first attempt at a decisive, fully explicit check (substitute a hand-derived word
    map for TAU^2 into every relator and look for an invertible 2x2 intertwiner between successive members'
    representations) was made and ABANDONED: two different hand derivations of the word map (see rs_presentation.
    py's TAU2 comment) both give the correct order on H_1(Y6) but FAIL to reproduce the identity on all six
    relators at the full (non-abelian) representation level, and no further attempt to fix the word-level formula
    is made here -- an honest instrument limit, not swept under the rug.

    What is used instead is a clean, abstract, word-map-free argument, whose only inputs are already computed in
    Sec. 1 and Sec. 2 above: TAU^2 is a deck transformation of an honest covering space, hence a genuine
    automorphism phi of pi_1(Y6) (a topological fact, not something that needs a presentation-level check); Sec. 2
    confirms deck() computes chi -> chi . phi exactly on every character this arc uses; squaring commutes with
    precomposition trivially, ((chi^2) . phi = (chi . phi)^2 for any phi), so phi pulls back member j+1's character
    chi_{j+1}^2 to exactly member j's chi_j^2.  Since phi is an automorphism, pullback along it is an ISOMORPHISM
    H^1(pi; chi_{j+1}^2) -> H^1(pi; chi_j^2); Sec. 1 already establishes both sides are 1-dimensional (h^1 = 1 at
    every member, every prime) -- so the pulled-back cocycle is a NONZERO scalar multiple of member j's own ct_j,
    and rescaling a non-split extension's cocycle by a nonzero scalar is a change of basis (conjugation by
    diag(1, lambda)), i.e. an ISOMORPHISM of representations.  Hence phi's pullback of member j+1 IS member j, up
    to isomorphism -- a genuine orbit, established without trusting any word-level formula for TAU or TAU^2.

    This function verifies the two computational inputs the argument needs, standalone (so this section does not
    silently depend on Sec. 1/2 having been run first in the same process)."""
    F = GF(p); z = F.root_of_unity(N)
    orbit = [(deck(SEED_CHI, 2 * j), deck(SEED_Y, 2 * j), deck(SEED_G, 2 * j)) for j in range(3)]
    h1s = []
    for cc, yy, gg in orbit:
        chi = dict(zip(GENS, cc)); chi2 = {g: pow(z, 2 * chi[g], p) for g in GENS}
        h1, ct = h1_and_cocycle(F, GENS, RELS, MU, LAM, chi2)
        assert h1 == 1 and ct is not None
        h1s.append(h1)
    assert cross_check_deck_is_tau_pullback()
    return h1s


# ---------------------------------------------------------------- Sec. 4: semisimplification kills the index
def semisimplification_control(p=601):
    """The whole index is carried by the non-split extension class: setting the cocycle to 0 (the split, reducible-
    but-decomposable module chi (+) chi^-1, tensored by the same psi) gives index 0 on every sector, at the seed
    member.  A cheap, own-code re-check of the source's reported control."""
    F = GF(p); z = F.root_of_unity(N)
    chi = dict(zip(GENS, SEED_CHI)); chi_val = {g: pow(z, chi[g], p) for g in GENS}
    ct = {g: 0 for g in GENS}
    rho_split = reducible_rep(F, GENS, chi_val, ct)
    out = []
    for lab, sy, sg in SECT:
        psi_exp = dict(zip(GENS, cadd(cmul(SEED_Y, sy), cmul(SEED_G, sg))))
        psi_val = {g: pow(z, psi_exp[g], p) for g in GENS}
        V = Rep(F, GENS, module(F, GENS, rho_split, 1, psi_val)); assert V.check_relators(RELS)
        I, dV, dVd = index(V, RELS, MU, LAM); out.append(I)
    assert out == [0] * 6, out
    return out


if __name__ == "__main__":
    print("=== Sec. 1: three primes, six sectors, member and orbit-sum indices ===")
    for p in PRIMES:
        members_idx, sums = run_prime(p)
        print(f"p={p}: members {members_idx}  orbit-sum I per sector {[s[1] for s in sums]}")
    print("\n=== Sec. 1b: exact over Q(zeta_8) ===")
    members_idx, sums = run_exact()
    print(f"members {members_idx}")
    for lab, I, dV, dVd in sums: print(f"  sector {lab}: I = {I}, V dims (a0,a1,t0,r1) = {dV}, V* dims = {dVd}")
    print("\n=== Sec. 2: deck() is the abelian pullback by TAU on this arc's characters (chi(z) = 0) ===")
    print("cross-check passed:", cross_check_deck_is_tau_pullback())
    print("\n=== Sec. 3: the genuineness argument (word-map-free) ===")
    h1s = genuineness_argument()
    print(f"h^1(pi; chi_j^2) = {h1s} at all three members (all 1) -- genuineness argument's inputs verified")
    print("\n=== Sec. 4: semisimplification control ===")
    print("index with the cocycle set to 0 (all six sectors):", semisimplification_control())
    print("\nDONE")
