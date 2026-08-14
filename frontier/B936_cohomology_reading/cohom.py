#!/usr/bin/env python3
"""B936 -- THE COHOMOLOGY READING (sealed cell; PREREGISTRATION.md is binding).

B928 proved the torsor theorem  H(sigma_chi o tau) = H+ * rho_27(sigma_{chi.chi+})
for all 64 outer composites, with symmetry <=> involution (the SIXTEEN Hermitian
structures), and the Klein group {I, D2, D, D2*D} = the wall pair's 2-torsion on
the 27.  THIS CELL asks whether that classification is an H^1 story, and whether
the value layer (the twist-norm law, B916) is an instance of it.

  Q-A   the group G and the module M; the 16 as a torsor / twisted forms;
        every cocycle condition checked EXHAUSTIVELY (the sets are finite).
  Q-A2  the lift obstruction: is chi -> rho_27(sigma_chi) an honest
        homomorphism (is B928's "affine polarity" a class or a gauge)?
  Q-B   the classes of D2 and of D; and what B938's "D is the identity on the
        colorless register" means cohomologically.
  Q-C   THE VALUE COROLLARY: is the twist-norm law the discriminant / pencil
        invariant of the PAIR (H+, H') on the rational blocks?
  Q-D   the orbits of the 16 under census conjugation -- the true CLASSES.

HOUSE RULES ENFORCED: exact arithmetic for every verdict-bearing claim;
verify-don't-trust (H+ and every H(phi) are re-SOLVED in-cell from their own
invariance equations -- banked data is only COMPARED against); e6_centralizer.py
exec'd in an isolated namespace with chdir to scratch and __file__ set; NO
Rayleigh-quotient eigenreads anywhere (the pencil spectra are read as exact
characteristic polynomials of a generalized eigenvalue problem, never as
quotients); no form is assumed definite and no matrix is assumed invertible --
every determinant is computed and checked nonzero before it is divided by;
results.json is dumped after EVERY stage so an interruption cannot lose work.
BLIND: no measured number is read, cited or compared anywhere in this cell.
"""
import io
import os
import json
import time
import pickle
import random
import tempfile
import contextlib
import itertools
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b936_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B936 the cohomology reading", "checks": {}, "notes": []}


def log(*a):
    print(f"[{time.time()-T00:7.1f}s]", *a, flush=True)


def dump():
    json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1)


def CHK(name, ok, detail=""):
    RES["checks"][name] = {"pass": bool(ok), "detail": str(detail)}
    log(f"  [{'PASS' if ok else 'FAIL'}] {name} {detail}")
    if not ok:
        RES["verdict"] = "UNSTABLE"
        dump()
        raise SystemExit(f"UNSTABLE at {name}")


def VERDICT(name, outcome, detail=""):
    """a PREREGISTERED two-outcome criterion: both outcomes are legitimate
    results of the cell, so this records and continues (unlike CHK, which
    guards mathematical consistency and halts)."""
    RES["checks"][name] = {"sealed_criterion": True,
                           "outcome": "PASS" if outcome else "FAIL",
                           "detail": str(detail)}
    log(f"  [VERDICT {'PASS' if outcome else 'FAIL'}] {name} {detail}")


def REC(name, value, detail=""):
    RES["checks"][name] = {"value": value, "detail": str(detail)}
    log(f"  [DATA] {name} = {value} {detail}")


# ============================================================ [0] banked inputs
log("[0] banked inputs ...")
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27",
                                   "rep27.json")))
REP = [[[int(x) for x in row] for row in REPJ["rep"][str(k)]]
       for k in range(78)]
WT = [tuple(REP[i][a][a] for i in range(6)) for a in range(27)]
CHK("rep27_cartan_diagonal_27_distinct_weights",
    all(all(REP[i][a][b] == 0 for a in range(27) for b in range(27) if a != b)
        for i in range(6)) and len(set(WT)) == 27)

B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell",
                                   "results.json")))
piW_banked = list(B912["H_plus_support_pi"])
cbP_banked = [int(x) for x in B912["H_plus_entries_c_b"]]
Dd_banked = [int(x) for x in B912["D_diag"]]
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
D2_banked = [int(x) for x in B916["H_prime_diag_vs_H_plus"]["D2"]]
MINPOLY_dS = [int(c) for c in B916["d_ratio_minpolys_desc"]["S0"]]
MINPOLY_dA = [int(c) for c in B916["d_ratio_minpolys_desc"]["A0p"]]
B907V = json.load(open(os.path.join(REPO, "frontier",
                                    "B907_real_form_selector", "verdict.json")))
CHI_P = tuple(int(x) for x in B907V[0]["signs"])
CHI_M = tuple(int(x) for x in B907V[1]["signs"])
B928 = json.load(open(os.path.join(REPO, "frontier", "B928_d2_decode",
                                   "results.json")))
CHK("banked_wall_pair_is_a_global_negation",
    CHI_M == tuple(-x for x in CHI_P), f"chi+ = {CHI_P}")

FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}
FIXED_NODES = sorted(i for i in range(6) if FLIP[i] == i)


def flipw(w):
    return tuple(w[FLIP[i]] for i in range(6))


negflip = {tuple(-x for x in flipw(WT[b])): b for b in range(27)}
piW = [negflip[WT[b]] for b in range(27)]
CHK("weight_pairing_pi_recomputed_and_involutive",
    sorted(piW) == list(range(27)) and all(piW[piW[b]] == b for b in range(27))
    and piW == piW_banked, "matches banked B912 support permutation")
dump()

# ============================================================ [1] B854 frame
log("[1] B854 frame (isolated exec, chdir scratch, __file__ set) ...")
cache = os.path.join(SCRATCH, "b936_frame_cache.pkl")
if os.path.exists(cache):
    FR = pickle.load(open(cache, "rb"))
else:
    cwd = os.getcwd()
    g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"),
          "__name__": "b854_frame"}
    src = open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                            "e6_centralizer.py")).read()
    try:
        os.chdir(SCRATCH)
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "b854", "exec"), g6)
    finally:
        os.chdir(cwd)
    FR = {"ROOTS": [tuple(r) for r in g6["ROOTS"]],
          "C": [list(row) for row in g6["C"]],
          "ns": list(g6["ns"]),
          "INV": {n: [Fr(c) for c in g6["INV"][n]] for n in g6["ns"]},
          "BB": [[[Fr(x) for x in g6["BB"][p][q]] for q in range(78)]
                 for p in range(78)],
          "EPS": {(a, b): g6["eps"](a, b) for a in g6["ROOTS"]
                  for b in g6["ROOTS"]
                  if tuple(x + y for x, y in zip(a, b)) in g6["IDX"]}}
    pickle.dump(FR, open(cache, "wb"))
ROOTS = FR["ROOTS"]
IDX = {r: i for i, r in enumerate(ROOTS)}
CMAT = FR["C"]
ns = FR["ns"]
INV = FR["INV"]
BB = FR["BB"]
EPS = FR["EPS"]
CHK("frame_72_roots_ns_8_14_16_22",
    len(ROOTS) == 72 and sorted(ns) == [8, 14, 16, 22])
CHK("dynkin_flip_fixed_nodes_are_two",
    FIXED_NODES == [1, 3]
    and all(CMAT[FLIP[i]][FLIP[j]] == CMAT[i][j] for i in range(6)
            for j in range(6)),
    "the diagram flip is an automorphism of the B854 Cartan matrix; its "
    "FIXED nodes are indices 1,3 (Bourbaki alpha_2, alpha_4)")

Rex = {}
for n in ns:
    M = [[Fr(0)] * 27 for _ in range(27)]
    for k, c in enumerate(INV[n]):
        if c:
            Rk = REP[k]
            for a in range(27):
                ra = Rk[a]
                for b in range(27):
                    if ra[b]:
                        M[a][b] += c * ra[b]
    Rex[n] = M

BBnz = [[[(k, Bv[k]) for k in range(78) if Bv[k]] for Bv in row] for row in BB]
random.seed(936)
ok = True
for _ in range(25):
    p, q = random.randrange(78), random.randrange(78)
    Bv = BB[p][q]
    for i in range(27):
        for j in range(27):
            lhs = sum(REP[p][i][t] * REP[q][t][j] - REP[q][i][t] * REP[p][t][j]
                      for t in range(27))
            rhs = sum(Bv[k] * REP[k][i][j] for k in range(78) if Bv[k])
            if lhs != rhs:
                ok = False
CHK("rep_homomorphism_25_random_bracket_pairs_exact", ok)
dump()

# ============================================================ [2] tau cocycle
log("[2] the tau cocycle (B907 F2 solve, re-run here) ...")
rows, rhs = [], []
for a_ in ROOTS:
    for b_ in ROOTS:
        s_ = tuple(a_[i] + b_[i] for i in range(6))
        if s_ in IDX:
            row = [0] * 72
            row[IDX[a_]] ^= 1
            row[IDX[b_]] ^= 1
            row[IDX[s_]] ^= 1
            cc = EPS[(a_, b_)] * EPS[(flipw(a_), flipw(b_))]
            rows.append(row)
            rhs.append(0 if cc == 1 else 1)
Aa = [row + [r] for row, r in zip(rows, rhs)]
r_ = 0
for c_ in range(72):
    piv = next((i for i in range(r_, len(Aa)) if Aa[i][c_]), None)
    if piv is None:
        continue
    Aa[r_], Aa[piv] = Aa[piv], Aa[r_]
    for i in range(len(Aa)):
        if i != r_ and Aa[i][c_]:
            Aa[i] = [x ^ y for x, y in zip(Aa[i], Aa[r_])]
    r_ += 1
CHK("tau_cocycle_consistent_rank_66",
    r_ == 66 and not any(sum(row[:72]) == 0 and row[72] for row in Aa))
CHK("tau_solution_set_is_a_torsor_of_size_64_over_the_characters",
    72 - r_ == 6,
    "the F2 system has a 6-dimensional solution space => the tau-lift is "
    "unique up to composition with an inner sign character: the OUTER coset "
    "of the census IS the solution set of the cocycle equation (64 members)")
sol = [0] * 72
for i in range(r_):
    c_ = next(cc for cc in range(72) if Aa[i][cc])
    sol[c_] = Aa[i][72]
dcoc = {ROOTS[i]: (-1) ** sol[i] for i in range(72)}


def chi_of(signs):
    def ch(r):
        v = 1
        for i in range(6):
            if r[i] % 2:
                v *= signs[i]
        return v
    return ch


def inner_gmap(signs):
    ch = chi_of(signs)
    out = [(i, 1) for i in range(6)]
    for r in ROOTS:
        out.append((6 + IDX[r], ch(r)))
    return out


def outer_gmap(signs):
    ch = chi_of(signs)
    out = [(FLIP[i], 1) for i in range(6)]
    for r in ROOTS:
        fr = flipw(r)
        out.append((6 + IDX[fr], dcoc[r] * ch(fr)))
    return out


def gmap_compose(g2, g1):
    out = []
    for k in range(78):
        j1, c1 = g1[k]
        j2, c2 = g2[j1]
        out.append((j2, c1 * c2))
    return out


def gmap_is_id(g):
    return all(g[k] == (k, 1) for k in range(78))


def gmap_inv(g):
    out = [None] * 78
    for k in range(78):
        j, c = g[k]
        out[j] = (k, c)
    return out


def is_automorphism_gmap(g):
    for p in range(78):
        jp, cp = g[p]
        for q in range(78):
            jq, cq = g[q]
            img = {}
            for (k, v) in BBnz[p][q]:
                jk, ck = g[k]
                img[jk] = img.get(jk, 0) + ck * v
            tgt = {k: cp * cq * v for (k, v) in BBnz[jp][jq]}
            for k in set(img) | set(tgt):
                if img.get(k, 0) != tgt.get(k, 0):
                    return False
    return True


def pattern_of_gmap(g):
    out = {}
    for n in ns:
        vec = INV[n]
        img = [Fr(0)] * 78
        for k in range(78):
            if vec[k]:
                j, c = g[k]
                img[j] += c * vec[k]
        ev = None
        for k in range(78):
            if vec[k] == 0 and img[k] == 0:
                continue
            if vec[k] == 0:
                return None
            rt = img[k] / vec[k]
            if rt not in (1, -1):
                return None
            if ev is None:
                ev = int(rt)
            elif int(rt) != ev:
                return None
        out[n] = ev
    return out


ALL_ONES = (1,) * 6
ALL_MINUS = (-1,) * 6
SIGNS = list(itertools.product((1, -1), repeat=6))


def bits(signs):
    return tuple(0 if s == 1 else 1 for s in signs)


def unbits(b):
    return tuple(1 if x == 0 else -1 for x in b)


dump()

# ============================================ [3] Q-A: THE CENSUS IS A GROUP
log("[3] Q-A/C-A1: the census closes as X semidirect <tau>, order 128 ...")
G_inner = {s: inner_gmap(s) for s in SIGNS}
G_outer = {s: outer_gmap(s) for s in SIGNS}
allmaps = {("i", s): G_inner[s] for s in SIGNS}
allmaps.update({("o", s): G_outer[s] for s in SIGNS})
CHK("census_128_distinct_generator_maps",
    len({tuple(v) for v in allmaps.values()}) == 128)
naut = sum(1 for v in allmaps.values() if is_automorphism_gmap(v))
CHK("all_128_census_members_are_automorphisms_full_78sq_check", naut == 128,
    "every product/bracket pair checked exactly for all 128")

# the semidirect law, exhaustively
lookup = {tuple(v): k for k, v in allmaps.items()}
bad = []
for (t1, s1), g1 in allmaps.items():
    for (t2, s2), g2 in allmaps.items():
        prod = gmap_compose(g1, g2)
        key = lookup.get(tuple(prod))
        if key is None:
            bad.append(((t1, s1), (t2, s2), "escapes"))
            continue
        # predicted: sigma_a [tau^e] . sigma_b [tau^f] = sigma_{a . tau^e(b)} tau^{e+f}
        e1 = 1 if t1 == "o" else 0
        s2t = tuple(s2[FLIP[i]] for i in range(6)) if e1 else s2
        pred_signs = tuple(s1[i] * s2t[i] for i in range(6))
        pred_type = "o" if (e1 + (1 if t2 == "o" else 0)) % 2 else "i"
        if key != (pred_type, pred_signs):
            bad.append(((t1, s1), (t2, s2), str(key)))
CHK("C_A1_semidirect_multiplication_table_exact_16384_products",
    not bad,
    "the census is EXACTLY the group G = X rtimes <tau>, |G| = 128, with "
    "X = Hom(Q, mu_2) = T_ad[2] = (Z/2)^6 and tau acting by the diagram flip")
CHK("tau_conjugation_on_X_is_the_diagram_flip",
    all(gmap_compose(gmap_compose(G_outer[ALL_ONES], G_inner[s]),
                     gmap_inv(G_outer[ALL_ONES]))
        == G_inner[tuple(s[FLIP[i]] for i in range(6))] for s in SIGNS),
    "tau sigma_chi tau^{-1} = sigma_{tau.chi}, all 64, exact")
RES["Q_A_group"] = {"G": "X rtimes <tau>", "order": 128,
                    "X": "Hom(Q, mu_2) = T_ad[2] = (Z/2)^6",
                    "tau_action": "the E6 diagram flip {0<->5, 2<->4, 1, 3}"}
dump()

# ==================================== [4] Q-A: THE MODULE AND ITS COHOMOLOGY
log("[4] Q-A: the Z/2-module X, and H^1(<tau>, X) by exact F2 linear algebra ...")


def f2_rank(vecs):
    M = [list(v) for v in vecs]
    r = 0
    for c in range(6):
        piv = next((i for i in range(r, len(M)) if M[i][c]), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][c]:
                M[i] = [x ^ y for x, y in zip(M[i], M[r])]
        r += 1
    return r


def tau_bits(b):
    return tuple(b[FLIP[i]] for i in range(6))


def norm_bits(b):
    return tuple((b[i] + tau_bits(b)[i]) % 2 for i in range(6))


Xbits = [bits(s) for s in SIGNS]
Xtau = [b for b in Xbits if tau_bits(b) == b]
NX = sorted({norm_bits(b) for b in Xbits})
CHK("Z1_equals_X_tau_size_16", len(Xtau) == 16,
    "Z^1(<tau>, X) = {chi : chi . tau(chi) = 1} = X^tau (the module is "
    "2-torsion, so ker(1+tau) = X^tau); 16 cocycles")
CHK("B1_equals_norm_image_size_4", len(NX) == 4 and f2_rank(NX) == 2,
    "B^1 = (1+tau)X = N(X), dimension 2 over F2")
CHK("H1_is_Z2_squared_supported_on_the_two_fixed_nodes",
    f2_rank(Xtau) == 4 and f2_rank(NX) == 2
    and all(b[i] == 0 for b in NX for i in FIXED_NODES),
    "H^1(<tau>, X) = X^tau / N(X) = (Z/2)^2; the norms vanish at the two "
    "tau-FIXED nodes, so the class of chi in X^tau is exactly its pair of "
    "coordinates (chi_1, chi_3) = (alpha_2, alpha_4) in Bourbaki labels: "
    "H^1 = (Z/2)^{# tau-fixed nodes}")


def h1_class(b):
    return tuple(b[i] for i in FIXED_NODES)


CHK("h1_class_map_is_a_surjective_homomorphism_with_kernel_B1",
    sorted({h1_class(b) for b in Xtau}) == sorted(
        list(itertools.product((0, 1), repeat=2)))
    and all(h1_class(n) == (0, 0) for n in NX)
    and len([b for b in Xtau if h1_class(b) == (0, 0)]) == 4,
    "four classes, each of size four")
RES["Q_A_module"] = {
    "M": "X = T_ad[2] = (Z/2)^6",
    "as_a_tau_module": "Z/2[<tau>] (nodes 0,5) + Z/2[<tau>] (nodes 2,4) "
                       "+ trivial (node 1) + trivial (node 3)",
    "Z1_size": 16, "B1_size": 4, "H1": "(Z/2)^2", "classes": 4,
    "class_map": "chi |-> (chi at node 1, chi at node 3) = "
                 "(Bourbaki alpha_2, alpha_4)"}
dump()

# ========================= [5] Q-A2: rho_27 AS AN HONEST HOMOMORPHISM (C-A3)
log("[5] Q-A2/C-A3: the weight-character lift; the H^2 obstruction ...")
# u = A^{-1} s over F2, A = Cartan matrix mod 2 (the adjacency matrix)
Amod2 = [[CMAT[i][j] % 2 for j in range(6)] for i in range(6)]
Ainv = [[1 if i == j else 0 for j in range(6)] for i in range(6)]
Awork = [row[:] for row in Amod2]
for c in range(6):
    piv = next(i for i in range(c, 6) if Awork[i][c])
    Awork[c], Awork[piv] = Awork[piv], Awork[c]
    Ainv[c], Ainv[piv] = Ainv[piv], Ainv[c]
    for i in range(6):
        if i != c and Awork[i][c]:
            Awork[i] = [x ^ y for x, y in zip(Awork[i], Awork[c])]
            Ainv[i] = [x ^ y for x, y in zip(Ainv[i], Ainv[c])]
CHK("cartan_mod2_invertible_det_3_is_odd",
    all(Awork[i][j] == (1 if i == j else 0) for i in range(6)
        for j in range(6)),
    "det(C) = 3 is odd => the weight-lattice extension of a mod-2 character "
    "is UNIQUE (Hom(P, mu_2) -> Hom(Q, mu_2) is an isomorphism)")


def u_of(b):
    return tuple(sum(Ainv[i][j] * b[j] for j in range(6)) % 2
                 for i in range(6))


def Rchar(signs):
    """rho_27(sigma_chi) in the intrinsic WEIGHT-CHARACTER normalization:
    R[b] = chi^(w_b), chi^ = the unique extension of chi to the weight
    lattice.  (Not the entry0 = +1 normalization.)"""
    u = u_of(bits(signs))
    return [1 if sum(u[i] * WT[b][i] for i in range(6)) % 2 == 0 else -1
            for b in range(27)]


R = {s: Rchar(s) for s in SIGNS}
NZ = [[(a, b) for a in range(27) for b in range(27) if REP[6 + kr][a][b]]
      for kr in range(72)]
bad = []
for s in SIGNS:
    ch = chi_of(s)
    Rs = R[s]
    for kr, r in enumerate(ROOTS):
        c = ch(r)
        for (a, b) in NZ[kr]:
            if Rs[a] * Rs[b] != c:
                bad.append((s, r, a, b))
CHK("weight_character_lift_IS_the_intertwiner_all_64_all_78_generators",
    not bad,
    "R(chi) rho(x) R(chi) = rho(sigma_chi x) exactly, for every character and "
    "every root generator (the Cartan is untouched: R is diagonal)")
CHK("C_A3_lift_is_a_homomorphism_4096_pairs",
    all(all(R[s1][b] * R[s2][b]
            == R[tuple(s1[i] * s2[i] for i in range(6))][b]
            for b in range(27)) for s1 in SIGNS for s2 in SIGNS),
    "chi -> R(chi) is an HONEST homomorphism X -> Diag_{+-1}(27): the "
    "2-cocycle of the sign ambiguity is identically 1 and the class in "
    "H^2(X, mu_2) is ZERO")
CHK("lift_is_injective_and_never_minus_identity",
    len({tuple(R[s]) for s in SIGNS}) == 64
    and not any(all(x == -1 for x in R[s]) for s in SIGNS if s != ALL_ONES),
    "64 distinct diagonals, none equal to -I => the 128 sign patterns "
    "+-R(chi) are distinct, and projectively there are exactly 64")


def rep_diagonal_of_inner(signs):
    """the entry0 = +1 normalization, by two-term propagation (B928 route)."""
    ch = chi_of(signs)
    T = [None] * 27
    T[0] = 1
    changed = True
    while changed:
        changed = False
        for kr, r in enumerate(ROOTS):
            M = REP[6 + kr]
            c = ch(r)
            for a in range(27):
                for b in range(27):
                    if M[a][b]:
                        if T[b] is not None and T[a] is None:
                            T[a] = c * T[b]
                            changed = True
                        elif T[a] is not None and T[b] is None:
                            T[b] = c * T[a]
                            changed = True
    if any(t is None for t in T):
        return None
    for kr, r in enumerate(ROOTS):
        M = REP[6 + kr]
        c = ch(r)
        for a in range(27):
            for b in range(27):
                if M[a][b] and T[a] != c * T[b]:
                    return None
    return T


Tprop = {s: rep_diagonal_of_inner(s) for s in SIGNS}
eps_norm = {s: R[s][0] for s in SIGNS}
CHK("entry0_normalization_equals_epsilon_times_the_weight_character",
    all(Tprop[s] == [eps_norm[s] * x for x in R[s]] for s in SIGNS),
    "T_chi (entry0 = +1) = eps(chi) . R(chi) with eps(chi) = R(chi)[0] = "
    "chi^(w_0) -- the base weight's value")
CHK("epsilon_is_itself_a_character_hence_a_coboundary",
    all(eps_norm[s1] * eps_norm[s2]
        == eps_norm[tuple(s1[i] * s2[i] for i in range(6))]
        for s1 in SIGNS for s2 in SIGNS),
    "eps: X -> mu_2 is a homomorphism => BOTH normalizations are "
    "homomorphisms; B928's 'affine/shifted character' polarity is a GAUGE "
    "(the value of the character at the base weight), not a cohomology class")
REC("epsilon_at_chi_minus", eps_norm[CHI_M],
    "the global -1 of B928's D2 = -(-1)^<s(chi-),w> is exactly eps(chi-) = "
    "chi-^(w_0)")
u_chim = u_of(bits(CHI_M))
CHK("a_star_equals_s_chi_minus_because_s_is_A_fixed",
    u_chim == bits(CHI_M),
    "the B928 exponent a* coincides with the sign vector s(chi-) because "
    "s(chi-) is a FIXED vector of the mod-2 Dynkin adjacency matrix "
    "(A s = s) -- a mod-2 diagram coincidence, now explained")
RES["Q_A2"] = {"H2_obstruction": "trivial (an explicit homomorphic lift)",
               "reason": "[P:Q] = 3 is odd, so the 2-torsion lift through "
                         "the mu_3 isogeny is canonical",
               "eps": "eps(chi) = chi^(w_0), a character; the affine polarity "
                      "is a gauge, not a class",
               "eps_at_chi_minus": eps_norm[CHI_M]}
dump()

# ================== [6] C-A2: THE SIXTEEN HERMITIAN STRUCTURES AS A TORSOR
log("[6] C-A2: re-solve every H(sigma_chi o tau); the torsor ...")


def solve_H_outer(g):
    eqs = []
    for k in range(6, 78):
        j, c = g[k]
        Rk = REP[k]
        Rj = REP[j]
        seen = set()
        for a in range(27):
            for b in range(27):
                if Rk[piW[b]][a] or Rj[piW[a]][b]:
                    key = (a, b)
                    if key in seen:
                        continue
                    seen.add(key)
                    eqs.append((b, piW[a], Rk[piW[b]][a], c * Rj[piW[a]][b]))
    y = [None] * 27
    y[0] = Fr(1)
    changed = True
    while changed:
        changed = False
        for b1, b2, c1, c2 in eqs:
            if c1 and c2:
                if y[b1] is not None and y[b2] is None:
                    y[b2] = -Fr(c1) * y[b1] / c2
                    changed = True
                elif y[b2] is not None and y[b1] is None:
                    y[b1] = -Fr(c2) * y[b2] / c1
                    changed = True
    if any(v is None for v in y):
        return None
    for b1, b2, c1, c2 in eqs:
        if c1 * y[b1] + c2 * y[b2] != 0:
            return None
    return y


Y = {}
missing = []
for s in SIGNS:
    y = solve_H_outer(G_outer[s])
    if y is None:
        missing.append(s)
    else:
        Y[s] = [int(v) for v in y]
CHK("all_64_outer_composites_have_a_unique_invariant_pairing",
    not missing, "propagation connected and consistent for every character")
cbP = Y[CHI_P]
CHK("H_plus_own_solve_equals_banked_B912", cbP == cbP_banked,
    "H+ re-solved in-cell from its own invariance equation")
Dwall = [Y[CHI_M][b] * cbP[b] for b in range(27)]
CHK("D_wall_equals_banked_B912_D_diag", Dwall == Dd_banked)
yStar = Y[ALL_MINUS]
D2 = [yStar[b] * cbP[b] for b in range(27)]
if D2[0] == -1:
    D2 = [-x for x in D2]
CHK("D2_recomputed_equals_banked_B916", D2 == D2_banked,
    f"{D2.count(-1)} flips")

# the torsor theorem in the INTRINSIC normalization
tors_bad = []
for s in SIGNS:
    lhs = [Y[s][b] * cbP[b] for b in range(27)]
    coord = tuple(s[i] * CHI_P[i] for i in range(6))
    rhs = R[coord]
    sgn = lhs[0] * rhs[0]
    if lhs != [sgn * v for v in rhs]:
        tors_bad.append(s)
CHK("torsor_theorem_intrinsic_all_64", not tors_bad,
    "H(sigma_chi o tau) = H+ . R(chi.chi+) up to ONE global sign, for all 64 "
    "(B928's theorem, re-derived here with the homomorphic lift)")
invol = [s for s in SIGNS if gmap_is_id(gmap_compose(G_outer[s], G_outer[s]))]
CHK("sixteen_outer_involutions_equal_Z1",
    sorted(bits(s) for s in invol) == sorted(Xtau),
    "the outer involutions are EXACTLY the 1-cocycles: (sigma_chi tau)^2 = "
    "sigma_{chi . tau(chi)}, so involution <=> chi in Z^1 = X^tau")
struct = {}
for s in invol:
    D = [Y[s][b] * cbP[b] for b in range(27)]
    if D[0] == -1:
        D = [-x for x in D]
    struct[s] = D
CHK("C_A2_sixteen_DISTINCT_structures", len({tuple(v) for v in struct.values()})
    == 16, "free: no two involutions share a Hermitian structure")
# free + transitive action of X^tau
act_ok = True
for s in invol:
    for nu in invol:
        prod = [struct[s][b] * R[nu][b] for b in range(27)]
        if prod[0] == -1:
            prod = [-x for x in prod]
        target = tuple(struct[tuple(s[i] * nu[i] for i in range(6))])
        if tuple(prod) != target:
            act_ok = False
CHK("C_A2_action_of_X_tau_is_simply_transitive",
    act_ok, "H |-> H . R(nu) for nu in X^tau permutes the sixteen exactly as "
            "X^tau translates itself: the sixteen Hermitian structures are a "
            "TORSOR (principal homogeneous space) under X^tau = Z^1")
RES["Q_A_torsor"] = {
    "structures": 16, "group": "X^tau = Z^1(<tau>, X), (Z/2)^4",
    "base_point": "H+ (chi = chi+, coordinate 1)",
    "coordinate_of_H(sigma_chi o tau)": "chi . chi+"}
dump()

# ==================================== [7] Q-B: LOCATING D2 AND D IN H^1
log("[7] Q-B/C-B: the classes of D2 and of the wall twist D ...")
coord_D2 = bits(CHI_M)                       # (-1) . chi+ = chi-
coord_D = bits(ALL_MINUS)                    # chi- . chi+ = -1
coord_D2D = bits(CHI_P)
CHK("torsor_coordinates_of_the_Klein_group",
    coord_D2 == bits(tuple(ALL_MINUS[i] * CHI_P[i] for i in range(6)))
    and coord_D == bits(tuple(CHI_M[i] * CHI_P[i] for i in range(6)))
    and coord_D2D == tuple((coord_D2[i] + coord_D[i]) % 2 for i in range(6))
    and all(struct[CHI_M][b] == Dwall[b] * (1 if Dwall[0] == 1 else -1)
            for b in range(27)),
    f"D2 <-> chi- = {coord_D2}; D <-> -1 = {coord_D}; D2D <-> chi+ = "
    f"{coord_D2D} (the product of the other two); I <-> 1")
psi0 = [b for b in Xbits if norm_bits(b) == coord_D2]
CHK("C_B_D2_class_is_TRIVIAL_a_coboundary",
    len(psi0) > 0 and h1_class(coord_D2) == (0, 0),
    f"chi- = N(psi) for {len(psi0)} characters psi; class (0,0)")
CHK("C_B_D_class_is_NONTRIVIAL",
    not any(norm_bits(b) == coord_D for b in Xbits)
    and h1_class(coord_D) == (1, 1),
    "the global negation is NOT a norm (exhaustive over all 64 psi); its "
    "class is (1,1) -- nonzero at BOTH tau-fixed nodes")
CHK("D2D_shares_D_class", h1_class(coord_D2D) == (1, 1)
    and h1_class(bits(ALL_ONES)) == (0, 0),
    "the Klein group {I, D2, D, D2D} maps onto H^1 with KERNEL {I, D2} and "
    "image the diagonal Z/2 generated by [D]")
PSI0 = unbits(psi0[0])
REC("psi0_signs", list(PSI0), "the exhibited coboundary witness")
CHK("C_B_conjugation_witness_phi_star_equals_psi0_phi_plus_psi0inv",
    gmap_compose(gmap_compose(G_inner[PSI0], G_outer[CHI_P]),
                 gmap_inv(G_inner[PSI0])) == G_outer[ALL_MINUS],
    "sigma_psi0 . phi+ . sigma_psi0^{-1} = phi* EXACTLY at generator-map "
    "level: the carrier of the second Hermitian structure is CONJUGATE to "
    "the first wall conjugation inside the census")
Rp = R[PSI0]
Hplus_mat = [[0] * 27 for _ in range(27)]
for b in range(27):
    Hplus_mat[piW[b]][b] = cbP[b]
Hprime_mat = [[Hplus_mat[a][b] * D2[b] for b in range(27)] for a in range(27)]
transported = [[Rp[a] * Hplus_mat[a][b] * Rp[b] for b in range(27)]
               for a in range(27)]
CHK("C_B_transport_witness_H_prime_equals_MINUS_transport_of_H_plus",
    all(transported[a][b] == -Hprime_mat[a][b] for a in range(27)
        for b in range(27)),
    "rho27(sigma_psi0) H+ rho27(sigma_psi0) = -H' exactly, entry for entry: "
    "the tau-twisted structure is the transport of H+ by a census element, "
    "up to the global polarity -1")
CHK("transport_moves_the_torsor_coordinate_by_the_NORM_all_64",
    all(all(R[psi][piW[b]] * R[psi][b] == R[unbits(norm_bits(bits(psi)))][b]
            for b in range(27)) for psi in SIGNS),
    "R(psi)[pi(b)] R(psi)[b] = R(N(psi))[b]: conjugating a structure by an "
    "inner census element translates its torsor coordinate by the COBOUNDARY "
    "N(psi) -- the cohomological action, verified elementwise")
RES["Q_B"] = {"D2_coordinate": list(coord_D2), "D2_class": [0, 0],
              "D2_is_a_coboundary": True,
              "D_coordinate": list(coord_D), "D_class": [1, 1],
              "D_is_a_coboundary": False,
              "psi0": list(PSI0),
              "Klein_to_H1": "kernel {I, D2}, image Z/2 = <[D]>"}
dump()

# ============================== [8] Q-D: THE ORBITS AND THE CLASS TABLE
log("[8] Q-D/C-D: orbits of the sixteen under census conjugation ...")
orbit_of = {}
for s in invol:
    orb = set()
    for psi in SIGNS:
        img = tuple((bits(s)[i] + norm_bits(bits(psi))[i]) % 2
                    for i in range(6))
        orb.add(img)
        gg = gmap_compose(gmap_compose(G_inner[psi], G_outer[s]),
                          gmap_inv(G_inner[psi]))
        if gg != G_outer[unbits(img)]:
            CHK("conjugation_matches_coboundary_translation", False,
                f"{s} {psi}")
    orbit_of[bits(s)] = frozenset(orb)
orbits = sorted({v for v in orbit_of.values()}, key=lambda o: sorted(o))
CHK("C_D_four_orbits_of_size_four",
    len(orbits) == 4 and all(len(o) == 4 for o in orbits)
    and all({h1_class(b) for b in o} == {h1_class(next(iter(o)))}
            for o in orbits),
    "conjugation by the census's inner part = translation by B^1; the orbit "
    "set IS H^1(<tau>, X) = four classes of four")


def fixed_dim_78(g):
    rows = []
    for k in range(78):
        j, c = g[k]
        row = [0] * 78
        row[k] -= 1
        row[j] += c
        rows.append(row)
    M = [[Fr(x) for x in row] for row in rows]
    r = 0
    for c_ in range(78):
        piv = next((i for i in range(r, 78) if M[i][c_] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(78):
            if i != r and M[i][c_] != 0:
                f = M[i][c_] / M[r][c_]
                M[i] = [x - f * yv for x, yv in zip(M[i], M[r])]
        r += 1
    return 78 - r


def signature_of(yvec):
    """exact signature of the symmetric form with H[pi(b)][b] = y_b."""
    pos = neg = 0
    seen = set()
    for b in range(27):
        if b in seen:
            continue
        a = piW[b]
        if a == b:
            seen.add(b)
            if yvec[b] > 0:
                pos += 1
            else:
                neg += 1
        else:
            seen.add(a)
            seen.add(b)
            pos += 1
            neg += 1
    return (pos, neg)


table = []
for s in invol:
    b = bits(s)
    pat = pattern_of_gmap(G_outer[s])
    D = struct[s]
    yv = Y[s]
    table.append({
        "signs": list(s), "coordinate": list(
            bits(tuple(s[i] * CHI_P[i] for i in range(6)))),
        "H1_class": list(h1_class(
            bits(tuple(s[i] * CHI_P[i] for i in range(6))))),
        "D_flips": D.count(-1),
        "C_compatible": pat is not None,
        "eps_pattern": ([pat[n] for n in ns] if pat else None),
        "fixed_dim_78": fixed_dim_78(G_outer[s]),
        "signature_of_H": list(signature_of(yv)),
        "is_wall_pair": tuple(s) in (CHI_P, CHI_M),
        "is_phi_star": tuple(s) == ALL_MINUS})
RES["Q_D_class_table"] = table
byclass = {}
for row in table:
    byclass.setdefault(tuple(row["H1_class"]), []).append(row)
CHK("fixed_dim_is_constant_on_each_H1_class",
    all(len({r["fixed_dim_78"] for r in rows}) == 1
        for rows in byclass.values()),
    "the fixed dimension (F4 = 52 / C4 = 36) is a conjugation invariant and "
    "is constant on the classes: " + str(
        {str(k): rows[0]["fixed_dim_78"] for k, rows in byclass.items()}))
CHK("UNORDERED_signature_is_constant_on_each_H1_class",
    all(len({tuple(sorted(r["signature_of_H"])) for r in rows}) == 1
        for rows in byclass.values()),
    "a Hermitian STRUCTURE is defined only up to scale, so only the "
    "UNORDERED signature {p,q} is an invariant of it; the ordered pair "
    "depends on the entry0 = +1 normalization.  (The run REFUTED the "
    "cell's first, mis-specified criterion, which asked for the ordered "
    "pair to be class-constant -- it is not, and it should not be.)")
REC("unordered_signatures_by_class",
    {str(k): sorted(rows[0]["signature_of_H"]) for k, rows in byclass.items()},
    "")
CHK("the_signature_separates_NOTHING_all_sixteen_share_it",
    len({tuple(sorted(r["signature_of_H"])) for r in table}) == 1,
    "all sixteen structures have the SAME unordered signature: the classical "
    "signature invariant is blind to the whole classification here")
nfix = sum(1 for b in range(27) if piW[b] == b)
CHK("signature_gap_is_the_three_pi_fixed_coordinates",
    nfix == 3 and abs(table[0]["signature_of_H"][0]
                      - table[0]["signature_of_H"][1]) == 3,
    "27 = 12 hyperbolic pi-pairs (each contributing (1,1)) + 3 pi-FIXED "
    "coordinates carrying one common sign: the whole signature gap is the "
    "three fixed lines")
named = {"phi_plus": CHI_P, "phi_minus": CHI_M, "phi_star": ALL_MINUS,
         "tau": ALL_ONES}
namedinfo = {}
for nm, s in named.items():
    row = next(r for r in table if tuple(r["signs"]) == s)
    namedinfo[nm] = {"class": row["H1_class"], "fixed_dim": row["fixed_dim_78"],
                     "type": "F4" if row["fixed_dim_78"] == 52 else "C4"}
REC("the_named_involutions", namedinfo, "")
CHK("the_wall_pair_is_NOT_a_conjugate_pair",
    namedinfo["phi_plus"]["class"] != namedinfo["phi_minus"]["class"]
    and namedinfo["phi_plus"]["fixed_dim"] != namedinfo["phi_minus"]["fixed_dim"],
    "phi+ and phi- lie in DIFFERENT cohomology classes and have different "
    "fixed subalgebras: the two wall-real alignments are not conjugate")
CHK("phi_star_is_conjugate_to_phi_plus_not_to_phi_minus",
    namedinfo["phi_star"]["class"] == namedinfo["phi_plus"]["class"]
    and namedinfo["phi_star"]["fixed_dim"] == namedinfo["phi_plus"]["fixed_dim"],
    "the carrier of the SECOND Hermitian structure sits in phi+'s class")
compat = [r for r in table if r["C_compatible"]]
CHK("C_compatibility_is_a_SECTION_of_the_class_map",
    len(compat) == 4
    and sorted(tuple(r["H1_class"]) for r in compat)
    == sorted(itertools.product((0, 1), repeat=2)),
    "the four C-compatible outer census members realize each cohomology "
    "class EXACTLY once: the charge frame is a section of Z^1 -> H^1")
REC("classes_summary",
    {str(k): {"fixed_dim": rows[0]["fixed_dim_78"],
              "signature": rows[0]["signature_of_H"],
              "C_compatible_members": sum(1 for r in rows
                                          if r["C_compatible"]),
              "members": [r["signs"] for r in rows]}
     for k, rows in byclass.items()},
    "the four TRUE classes")
dump()

# ================ [9] Q-B(second half): the colorless register, cohomologically
log("[9] Q-B: the colorless register and the support of the two twists ...")
import sympy as sp

CO = {8: 3, 14: 7, 16: 13, 22: 17}
Mc = [[sum(Fr(CO[n]) * Rex[n][i][j] for n in ns) for j in range(27)]
      for i in range(27)]
xs = sp.Symbol("x")
cp27 = sp.Matrix(27, 27, lambda i, j: sp.Rational(Mc[i][j].numerator,
                                                  Mc[i][j].denominator)
                 ).charpoly(xs)
fl = sp.factor_list(cp27.as_expr())
facs = sorted([(sp.degree(f, xs), m, sp.Poly(f, xs)) for f, m in fl[1]])
CHK("charpoly_Mc_factors_3_1__6_1__6_3",
    [(d, m) for d, m, _ in facs] == [(3, 1), (6, 1), (6, 3)])


def qkernel(M):
    rowsn = len(M)
    cols = len(M[0])
    A = [row[:] for row in M]
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rowsn) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rowsn):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [x - f * yv for x, yv in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for fc in free:
        v = [Fr(0)] * cols
        v[fc] = Fr(1)
        for i, c in enumerate(piv):
            v[c] = -A[i][fc]
        basis.append(v)
    return basis


def matmulQ(Xm, Ym):
    n = len(Xm)
    return [[sum(Xm[i][t] * Ym[t][j] for t in range(n) if Xm[i][t])
             for j in range(n)] for i in range(n)]


def poly_mat(coeffs):
    Acc = [[Fr(sp.Rational(coeffs[0]).p, sp.Rational(coeffs[0]).q)
            if i == j else Fr(0) for j in range(27)] for i in range(27)]
    for c in coeffs[1:]:
        Acc = matmulQ(Acc, Mc)
        cf = Fr(sp.Rational(c).p, sp.Rational(c).q)
        for i in range(27):
            Acc[i][i] += cf
    return Acc


W3 = qkernel(poly_mat([sp.Rational(c) for c in facs[0][2].all_coeffs()]))
W6 = qkernel(poly_mat([sp.Rational(c) for c in facs[1][2].all_coeffs()]))
W18 = qkernel(poly_mat([sp.Rational(c) for c in facs[2][2].all_coeffs()]))
CHK("rational_blocks_dim_3_6_18",
    len(W3) == 3 and len(W6) == 6 and len(W18) == 18)
supp_cl = sorted({b for w in W3 + W6 for b in range(27) if w[b] != 0})
supp_col = sorted({b for w in W18 for b in range(27) if w[b] != 0})
REC("colorless_support_size", len(supp_cl))
CHK("B938_D_is_the_identity_on_the_colorless_register",
    all(Dwall[b] == 1 for b in supp_cl),
    "re-verified in-cell: every weight carrying the colorless register is "
    "D-unflipped; all 12 of D's flips are colored")
CHK("D2_is_NOT_the_identity_on_the_colorless_register",
    any(D2[b] == -1 for b in supp_cl),
    f"{sum(1 for b in supp_cl if D2[b] == -1)} colorless weights flipped by "
    "D2 -- the register-visible twist")
# the annihilator of the colorless sublattice
Qcl = []
for i in range(len(supp_cl)):
    for j in range(len(supp_cl)):
        if i != j:
            Qcl.append(tuple(WT[supp_cl[i]][t] - WT[supp_cl[j]][t]
                             for t in range(6)))
ann = []
for s in SIGNS:
    u = u_of(bits(s))
    if all(sum(u[t] * d[t] for t in range(6)) % 2 == 0 for d in Qcl):
        ann.append(bits(s))
REC("annihilator_of_the_colorless_sublattice_size", len(ann),
    "characters whose weight-lattice extension is CONSTANT on the colorless "
    "register's weights = the register-blind twists")
CHK("D_coordinate_is_register_blind_D2_coordinate_is_not",
    coord_D in ann and coord_D2 not in ann,
    "cohomologically: the class-carrying coordinate (-1, the global "
    "negation) annihilates the colorless sublattice; the coboundary "
    "coordinate (chi-) does not.  The register sees exactly what H^1 "
    "cannot, and vice versa")
REC("D2_flip_split_colorless_vs_colored",
    {"colorless": sum(1 for b in supp_cl if D2[b] == -1),
     "colored": sum(1 for b in range(27)
                    if D2[b] == -1 and b not in supp_cl),
     "total": D2.count(-1)},
    "the eleven flips of D2, split by register.  NOTE: this split is NOT "
    "B938's 7/11 datum (that one is a valuation of the resolvent at the unit "
    "levels); no link is claimed here")
CHK("register_blind_characters_are_exactly_the_trivial_one_and_the_negation",
    sorted(ann) == sorted([bits(ALL_ONES), bits(ALL_MINUS)]),
    "the subgroup of register-blind characters has ORDER 2 and is generated "
    "by the global negation -- exactly D's coordinate.  So among the whole "
    "64-character group, the ONLY nontrivial twist the colorless register "
    "cannot see is the one carrying the nonzero cohomology class")
RES["Q_B_register"] = {
    "colorless_support": supp_cl,
    "colored_support": supp_col,
    "D_flips_in_colorless": sum(1 for b in supp_cl if Dwall[b] == -1),
    "D2_flips_in_colorless": sum(1 for b in supp_cl if D2[b] == -1),
    "annihilator_size": len(ann),
    "annihilator": [list(a) for a in ann],
    "D_in_annihilator": coord_D in ann,
    "D2_in_annihilator": coord_D2 in ann}
dump()

# =========================== [10] Q-C: THE VALUE COROLLARY (the pencil)
log("[10] Q-C/C-C: the pencil det(H' - x H+) on the rational blocks ...")


def detQ(M):
    n = len(M)
    A = [row[:] for row in M]
    det = Fr(1)
    for c in range(n):
        p = next((i for i in range(c, n) if A[i][c] != 0), None)
        if p is None:
            return Fr(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            det = -det
        det *= A[c][c]
        inv = Fr(1) / A[c][c]
        for i in range(c + 1, n):
            if A[i][c] != 0:
                f = A[i][c] * inv
                A[i] = [x - f * yv for x, yv in zip(A[i], A[c])]
    return det


def gram(Wb, yv):
    """Gram of the form with support H[pi(b)][b] = y_b, on the basis Wb."""
    k = len(Wb)
    return [[sum(Wb[i][piW[b]] * yv[b] * Wb[j][b] for b in range(27)
                 if yv[b] and Wb[j][b] and Wb[i][piW[b]])
             for j in range(k)] for i in range(k)]


def interp_poly(pts):
    """exact Lagrange interpolation; pts = [(x_i, y_i)]; coeffs ASCENDING."""
    n = len(pts)
    coeffs = [Fr(0)] * n
    for i, (xi, yi) in enumerate(pts):
        num = [Fr(1)]                       # ascending coefficients
        den = Fr(1)
        for j, (xj, _) in enumerate(pts):
            if i == j:
                continue
            new = [Fr(0)] * (len(num) + 1)
            for t, c in enumerate(num):
                new[t] += -xj * c
                new[t + 1] += c
            num = new
            den *= (xi - xj)
        f = yi / den
        for t, c in enumerate(num):
            coeffs[t] += f * c
    return coeffs


def primitive_int(coeffs):
    from math import gcd
    den = 1
    for c in coeffs:
        den = den * c.denominator // gcd(den, c.denominator)
    ints = [int(c * den) for c in coeffs]
    g = 0
    for v in ints:
        g = gcd(g, abs(v))
    if g:
        ints = [v // g for v in ints]
    lead = next((v for v in ints if v), 1)
    if lead < 0:
        ints = [-v for v in ints]
    return ints


blocks = {"W3": W3, "W6": W6, "W18": W18,
          "full27": [[Fr(1) if i == j else Fr(0) for j in range(27)]
                     for i in range(27)]}
yPlus = [Fr(v) for v in cbP]
yPrime = [Fr(cbP[b] * D2[b]) for b in range(27)]
CHK("both_forms_are_symmetric_on_every_pi_pair",
    all(yPlus[piW[b]] == yPlus[b] and yPrime[piW[b]] == yPrime[b]
        for b in range(27)),
    "checked, not assumed: the pi-pair entries agree, so both Grams are "
    "symmetric and the signature reading below is legitimate")
pencils = {}
for nm, Wb in blocks.items():
    k = len(Wb)
    G0 = gram(Wb, yPlus)
    G1 = gram(Wb, yPrime)
    d0 = detQ(G0)
    d1 = detQ(G1)
    CHK(f"gram_nondegenerate_{nm}", d0 != 0 and d1 != 0,
        f"det(H+|{nm}) = {d0}, det(H'|{nm}) = {d1} -- checked, not assumed")
    pts = []
    for t in range(k + 1):
        xt = Fr(t)
        Mt = [[G1[i][j] - xt * G0[i][j] for j in range(k)] for i in range(k)]
        pts.append((xt, detQ(Mt)))
    cf = interp_poly(pts)
    cf = list(reversed(cf))          # descending
    pencils[nm] = {"dim": k, "det_Hplus": str(d0), "det_Hprime": str(d1),
                   "det_ratio": str(d1 / d0),
                   "pencil_charpoly_primitive_desc": primitive_int(cf)}
    REC(f"pencil_{nm}", pencils[nm], "")
RES["Q_C_pencils"] = pencils
CHK("global_det_ratio_is_exactly_minus_one",
    Fr(pencils["full27"]["det_ratio"]) == -1,
    "det(H')/det(H+) = -1 on the full 27: H' = -(transport of H+) and 27 is "
    "ODD, so the two structures are ANTI-isometric -- the discriminant of "
    "the pair is exactly the polarity, with no prime content at all")
sig_plus = signature_of(cbP)
sig_prime = signature_of([cbP[b] * D2[b] for b in range(27)])
REC("signatures_H_plus_and_H_prime", [list(sig_plus), list(sig_prime)],
    "exact, from the pi-cycle structure; no numerics")
CHK("H_prime_signature_is_H_plus_reversed",
    sig_prime == (sig_plus[1], sig_plus[0]),
    "the polarity flips the signature: H' is congruent to -H+")

# the banked twist-norm law, exactly, against the pencil
w3poly = pencils["W3"]["pencil_charpoly_primitive_desc"]
banked_S = primitive_int([Fr(c) for c in MINPOLY_dS])
banked_S_rec = primitive_int([Fr(c) for c in reversed(MINPOLY_dS)])
match_direct = (w3poly == banked_S)
match_recip = (w3poly == banked_S_rec)
REC("W3_pencil_vs_banked_d_minpoly",
    {"pencil": w3poly, "banked_d_S": banked_S,
     "banked_reciprocal": banked_S_rec,
     "direct_match": match_direct, "reciprocal_match": match_recip}, "")
ratio_W3 = Fr(pencils["W3"]["det_ratio"])
target = -Fr(953, 2304) ** 2
VERDICT("C_C_the_discriminant_reading",
        ratio_W3 == target or match_direct or match_recip,
        f"det(H'|W3)/det(H+|W3) = {ratio_W3}; banked N_K(d_S) = {target}; "
        f"pencil-vs-minpoly direct = {match_direct}, reciprocal = "
        f"{match_recip}")
RES["Q_C_verdict_inputs"] = {
    "W3_det_ratio": str(ratio_W3), "banked_norm_law": str(target),
    "equal": ratio_W3 == target,
    "W3_pencil_matches_d_minpoly": bool(match_direct or match_recip)}
dump()

# ---- the K-arithmetic cross-check (exact, from the banked K-coordinates)
log("[10b] the K-norm cross-check on the banked flip masses ...")
MU = [500716339200, -2075673600, -4769856, 2197]
A_, B_, C_, D_ = MU
R3K = [Fr(-D_, A_), Fr(-C_, A_), Fr(-B_, A_)]
R4K = [R3K[2] * R3K[0], R3K[0] + R3K[2] * R3K[1], R3K[1] + R3K[2] * R3K[2]]


def kmul(x, y):
    c0 = x[0] * y[0]
    c1 = x[0] * y[1] + x[1] * y[0]
    c2 = x[0] * y[2] + x[1] * y[1] + x[2] * y[0]
    c3 = x[1] * y[2] + x[2] * y[1]
    c4 = x[2] * y[2]
    if c4:
        c0 += c4 * R4K[0]
        c1 += c4 * R4K[1]
        c2 += c4 * R4K[2]
    if c3:
        c0 += c3 * R3K[0]
        c1 += c3 * R3K[1]
        c2 += c3 * R3K[2]
    return (c0, c1, c2)


def Knorm(kx):
    cols = [kmul(kx, e) for e in ((Fr(1), Fr(0), Fr(0)),
                                  (Fr(0), Fr(1), Fr(0)),
                                  (Fr(0), Fr(0), Fr(1)))]
    M = [[cols[j][i] for j in range(3)] for i in range(3)]
    return detQ(M)


mS = tuple(Fr(x) for x in B928["Q2_colorless"]["m_S_K_coords"])
mA = tuple(Fr(x) for x in B928["Q2_colorless"]["m_A_K_coords"])
dS_banked = tuple(Fr(x) for x in B928["Q2_colorless"]["d_S_K_coords"])
dA_banked = tuple(Fr(x) for x in B928["Q2_colorless"]["d_A_K_coords"])
dS = (Fr(1) - 2 * mS[0], -2 * mS[1], -2 * mS[2])
dA = (Fr(1) - 2 * mA[0], -2 * mA[1], -2 * mA[2])
CHK("d_equals_one_minus_twice_the_flip_mass_both_families",
    dS == dS_banked and dA == dA_banked,
    "the banked twist ratio IS the torsor coordinate evaluated on the atom "
    "line: d = <D2 v, v>_{H+} / <v, v>_{H+} = 1 - 2m")
CHK("K_norm_law_S_reproduced_exactly", Knorm(dS) == target,
    f"N_K(1 - 2 m_S) = {Knorm(dS)}")
CHK("K_norm_law_A_reproduced_exactly", Knorm(dA) == target,
    f"N_K(1 - 2 m_A) = {Knorm(dA)}")
RES["Q_C_Knorms"] = {"N_dS": str(Knorm(dS)), "N_dA": str(Knorm(dA)),
                     "target": str(target)}
REC("norm_law_factored_polarity_times_square",
    {"polarity": -1, "square_root_of_the_rest": str(Fr(953, 2304))},
    "N_K(d) = (-1) . (953/2304)^2: the class in Q*/(Q*)^2 is [-1]; ALL the "
    "prime content is a perfect square, hence invisible to any discriminant "
    "class")
dump()

# ============ [11] the controls the C-C failure demands (verify-don't-trust)
log("[11] controls: block canonicity, orthogonality, the mechanism ...")
# (i) the blocks must not depend on the separating charge constants
CO2 = {8: 5, 14: 11, 16: 23, 22: 41}
Mc2 = [[sum(Fr(CO2[n]) * Rex[n][i][j] for n in ns) for j in range(27)]
       for i in range(27)]


def poly_mat_gen(coeffs, Mbase):
    Acc = [[Fr(sp.Rational(coeffs[0]).p, sp.Rational(coeffs[0]).q)
            if i == j else Fr(0) for j in range(27)] for i in range(27)]
    for c in coeffs[1:]:
        Acc = matmulQ(Acc, Mbase)
        cf = Fr(sp.Rational(c).p, sp.Rational(c).q)
        for i in range(27):
            Acc[i][i] += cf
    return Acc


cp2 = sp.Matrix(27, 27, lambda i, j: sp.Rational(Mc2[i][j].numerator,
                                                 Mc2[i][j].denominator)
                ).charpoly(xs)
fl2 = sp.factor_list(cp2.as_expr())
facs2 = sorted([(sp.degree(f, xs), m, sp.Poly(f, xs)) for f, m in fl2[1]])
CHK("control_second_charge_choice_same_block_shape",
    [(d, m) for d, m, _ in facs2] == [(3, 1), (6, 1), (6, 3)])
W3b = qkernel(poly_mat_gen([sp.Rational(c) for c in facs2[0][2].all_coeffs()],
                           Mc2))
W6b = qkernel(poly_mat_gen([sp.Rational(c) for c in facs2[1][2].all_coeffs()],
                           Mc2))
W18b = qkernel(poly_mat_gen([sp.Rational(c) for c in facs2[2][2].all_coeffs()],
                            Mc2))


def rank_rows(M):
    return len(M) - len(qkernel([[M[a][i] for a in range(len(M))]
                                 for i in range(27)]))


def same_span(Ba, Bb):
    if len(Ba) != len(Bb):
        return False
    ra, rb = rank_rows(list(Ba)), rank_rows(list(Bb))
    rboth = rank_rows(list(Ba) + list(Bb))
    return ra == rb == rboth == len(Ba)


ctrl = {}
for nm, Wa, Wb2 in (("W3", W3, W3b), ("W6", W6, W6b), ("W18", W18, W18b)):
    G0 = gram(Wb2, yPlus)
    G1 = gram(Wb2, yPrime)
    ctrl[nm] = {"same_subspace": same_span(Wa, Wb2),
                "det_ratio_second_basis": str(detQ(G1) / detQ(G0))}
CHK("control_det_ratios_are_charge_choice_independent",
    all(ctrl[nm]["same_subspace"] for nm in ctrl)
    and all(ctrl[nm]["det_ratio_second_basis"] == pencils[nm]["det_ratio"]
            for nm in ctrl),
    "the register blocks and their discriminant ratios are intrinsic: a "
    "second, unrelated separating choice of charge constants gives the SAME "
    "subspaces and the SAME ratios " + str(ctrl))

# (ii) are the three blocks H-orthogonal?  (this is why the global ratio does
#      not factor as the product of the block ratios)
def cross(Wa, Wb2, yv):
    return [[sum(Wa[i][piW[b]] * yv[b] * Wb2[j][b] for b in range(27)
                 if yv[b] and Wb2[j][b] and Wa[i][piW[b]])
             for j in range(len(Wb2))] for i in range(len(Wa))]


orth = {}
for (na, Wa), (nb, Wb2) in itertools.combinations(
        [("W3", W3), ("W6", W6), ("W18", W18)], 2):
    Cm = cross(Wa, Wb2, yPlus)
    Cp = cross(Wa, Wb2, yPrime)
    orth[f"{na}x{nb}"] = {"H_plus_zero": all(v == 0 for row in Cm
                                             for v in row),
                          "H_prime_zero": all(v == 0 for row in Cp
                                              for v in row)}
REC("block_orthogonality_under_both_forms", orth,
    "if any pair is NOT orthogonal the global determinant does not factor "
    "over the blocks")
prod_blocks = (Fr(pencils["W3"]["det_ratio"]) * Fr(pencils["W6"]["det_ratio"])
               * Fr(pencils["W18"]["det_ratio"]))
REC("product_of_block_det_ratios_vs_global",
    {"product": str(prod_blocks), "global": pencils["full27"]["det_ratio"],
     "equal": prod_blocks == Fr(pencils["full27"]["det_ratio"])}, "")

# (iii) the twist operator IS the diagonal D2; the global pencil is trivial
tf = [1]
for b in range(27):
    ev = D2[b]
    new = [0] * (len(tf) + 1)
    for t, c in enumerate(tf):
        new[t] += c
        new[t + 1] -= ev * c
    tf = new
CHK("the_global_pencil_is_the_charpoly_of_D2_itself",
    pencils["full27"]["pencil_charpoly_primitive_desc"]
    == primitive_int([Fr(c) for c in tf]),
    "H+^{-1} H' = diag(D2) exactly, so the FULL 27-pencil is "
    "(x-1)^16 (x+1)^11 -- no content; all the content is in how the register "
    "blocks sit against D2's eigenspaces")
CHK("the_full_pencil_is_reciprocal_palindromic",
    pencils["full27"]["pencil_charpoly_primitive_desc"]
    == list(reversed(pencils["full27"]["pencil_charpoly_primitive_desc"])),
    "forced: R(psi0) conjugates the twist operator to its inverse "
    "(R T R = T^{-1}), because H' = -R H+ R with R an involution")

# (iv) THE MECHANISM: does the frame change preserve the register blocks?
mech = {}
for nm, Wb2 in (("W3", W3), ("W6", W6), ("W18", W18)):
    img = [[Rp[b] * w[b] for b in range(27)] for w in Wb2]
    stack = [list(v) for v in Wb2] + img
    rk = len(stack) - len(qkernel([[stack[a][i] for a in range(len(stack))]
                                   for i in range(27)]))
    mech[nm] = {"dim": len(Wb2), "dim_span_W_plus_RW": rk,
                "R_preserves_block": rk == len(Wb2)}
REC("does_the_frame_change_preserve_the_register_blocks", mech,
    "R = rho27(sigma_psi0) is the census element carrying H+ to -H'; if it "
    "does NOT preserve a block, the atom lines in that block are moved and "
    "their H+-norms are distorted -- which is exactly what d measures")
CHK("D2_does_NOT_preserve_the_colorless_blocks",
    not mech["W3"]["R_preserves_block"] or not mech["W6"]["R_preserves_block"],
    "the value ratio d is nonzero content precisely because the frame change "
    "moves the register")

# (v) is the block pencil's cubic in the value field K?
w3p = sp.Poly(w3poly, xs)
irr = sp.factor_list(w3p.as_expr())
mu13 = sp.Poly([sp.Integer(c) for c in MU], xs)
disc_w3 = sp.discriminant(w3p.as_expr(), xs)
disc_mu = sp.discriminant(mu13.as_expr(), xs)


def sqfree(n):
    n = sp.Integer(n)
    s = sp.Integer(1)
    for p, e in sp.factorint(abs(n)).items():
        if e % 2:
            s *= p
    return s * (-1 if n < 0 else 1)


REC("W3_pencil_cubic_field_test",
    {"cubic": [int(c) for c in w3poly],
     "irreducible": len(irr[1]) == 1 and irr[1][0][1] == 1
     and sp.degree(irr[1][0][0], xs) == 3,
     "disc_squarefree_part": str(sqfree(disc_w3)),
     "K_disc_squarefree_part": str(sqfree(disc_mu)),
     "same_squarefree_disc": sqfree(disc_w3) == sqfree(disc_mu),
     "factors": str(irr)},
    "the block pencil spectrum is a NEW cubic invariant; this asks whether "
    "it lives in the same cubic field as the value ratios")
hS_poly = sp.Poly([sp.Rational(c) for c in facs[0][2].all_coeffs()], xs)
hA_poly = sp.Poly([sp.Rational(c) for c in facs[1][2].all_coeffs()], xs)
REC("register_block_cubics_vs_the_value_field",
    {"h_S": [int(c) for c in facs[0][2].all_coeffs()],
     "h_S_disc_squarefree": str(sqfree(sp.discriminant(hS_poly.as_expr(),
                                                       xs))),
     "K_disc_squarefree": str(sqfree(disc_mu)),
     "h_S_field_is_K": sqfree(sp.discriminant(hS_poly.as_expr(), xs))
     == sqfree(disc_mu),
     "W3_pencil_quadratic_disc_squarefree": str(sqfree(50064))},
    "the 3-block's own cubic (the charge labels) versus the value field K: "
    "if the squarefree discriminants agree, the three Galois-conjugate joint "
    "charge eigenlines spanning W3 have their invariants in K -- which is "
    "where the banked d_S lives")
# (vi) the pencil's RATIONAL roots are the blocks' intersections with D2's
#      eigenspaces (B928's span-intersection facts, re-derived spectrally)
inter = {}
for nm, Wb2 in (("W3", W3), ("W6", W6), ("W18", W18)):
    row = {}
    for ev, tag in ((-1, "minus"), (1, "plus")):
        eqs = [[(Fr(1) if D2[b] == ev else Fr(0)) * 0 for b in range(27)]]
        # W (x) ker(D2 - ev): solve for c with sum_j c_j w_j supported only on
        # the ev-eigencoordinates
        M = [[Wb2[j][b] for j in range(len(Wb2))]
             for b in range(27) if D2[b] != ev]
        row[tag] = len(qkernel(M)) if M else len(Wb2)
    inter[nm] = row
    pen = pencils[nm]["pencil_charpoly_primitive_desc"]
    val_m1 = sum(c * (-1) ** (len(pen) - 1 - t) for t, c in enumerate(pen))
    val_p1 = sum(pen)
    row["pencil_vanishes_at_minus1"] = (val_m1 == 0)
    row["pencil_vanishes_at_plus1"] = (val_p1 == 0)
REC("block_intersections_with_D2_eigenspaces_vs_pencil_roots", inter,
    "a vector of W inside D2's ev-eigenspace is a pencil eigenvector with "
    "eigenvalue ev, because H' = H+ diag(D2) exactly")
CHK("pencil_rational_roots_match_the_block_intersections",
    all((inter[nm]["minus"] > 0) == inter[nm]["pencil_vanishes_at_minus1"]
        and (inter[nm]["plus"] > 0) == inter[nm]["pencil_vanishes_at_plus1"]
        for nm in inter),
    "and they do: the (x+1) factor of the W3 pencil IS B928's "
    "dim(span_F cap W3) = 1 -- the cross-arc tie, re-derived spectrally "
    + str({k: (v["minus"], v["plus"]) for k, v in inter.items()}))
defm = D2.count(-1) - sum(inter[nm]["minus"] for nm in inter)
defp = D2.count(1) - sum(inter[nm]["plus"] for nm in inter)
CHK("THE_MISALIGNMENT_is_exactly_two_dimensions_in_each_eigenspace",
    defm == 2 and defp == 2,
    "the three register blocks SPAN the 27, yet D2's eigenspaces are not the "
    "sums of their block pieces: 11 - (1+2+6) = 2 and 16 - (0+2+12) = 2.  "
    "Those four dimensions are the entire misalignment between the register "
    "decomposition and the twist's eigenspaces -- the seat of every "
    "frame-relative value datum")
CHK("DERIVED_the_conjugate_atom_lines_are_NOT_jointly_orthogonal",
    ratio_W3 != target
    and sqfree(sp.discriminant(hS_poly.as_expr(), xs)) == sqfree(disc_mu),
    "W3 (x) Kbar is spanned by THREE Galois-conjugate joint charge "
    "eigenlines (h_S is irreducible of degree 3 and its field is K, the "
    "value field).  If those three lines were simultaneously orthogonal for "
    "BOTH forms, the determinant ratio would equal the product of the "
    "diagonal ratios, i.e. N_K(d_S).  It does not "
    f"({ratio_W3} vs {target}).  Therefore they are not -- and the "
    "twist-norm law is a DIAGONAL (frame-relative) datum, not a determinant "
    "(invariant) one")
RES["Q_C_controls"] = {"charge_choice_control": ctrl,
                       "block_orthogonality": orth,
                       "mechanism": mech,
                       "product_of_block_ratios": str(prod_blocks)}
RES["runtime_s"] = round(time.time() - T00, 1)
RES["verdict"] = "see DRAFT_FINDINGS.md"
dump()
log("done.")
