#!/usr/bin/env python3
"""B939 -- THE KLEIN ASSEMBLY: the sharp pair computed.

The assembly test's one computable-on-this-bench pair: W_frame (the solo
ledger LIII / FS4 frame Klein, {identity, pair-flip, all-flip, product} on
the four B854 charges) vs the wall pair's 2-torsion (B928:
{1, sigma_chi-, sigma_-1, sigma_chi+}, whose 27-shadow is {I, D2, D, D2D}).
Both live on the banked B854 build.  This cell computes whether they
generate the same subgroup of Aut(e6) -- and what they share.

Conventions copied from banked instruments (cited, then re-verified here):
  - the build:            frontier/B854_centralizer_exact/e6_centralizer.py
  - gmap machinery:       frontier/B928_d2_decode/d2_decode.py  [2]
  - chi characters:       B907 verdict.json (CHI_P = (1,-1,1,-1,1,1)),
                          B907 sweep_results.json (the inner compact-flip
                          character CHI_C = (1,-1,-1,1,-1,1)),
                          B907 results_complete.json (the outer all-flip
                          character CHI_ALL = (1,1,-1,-1,-1,1))
  - rep27 diagonals:      d2_decode.py rep_diagonal_of_inner (copied)

HOUSE RULES ENFORCED: exact arithmetic (Fractions / sympy exact) for every
verdict-bearing claim; e6_centralizer.py exec'd in an isolated namespace
with chdir to scratch and __file__ set; no Rayleigh readouts (no numerics
at all in this cell); no measured number touched; failures abort loudly.

Output: results.json next to this file.  Runtime: a few minutes
(dominated by the fresh B854 build exec).
"""
import io
import os
import json
import time
import tempfile
import contextlib
import itertools
from fractions import Fraction as Fr
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
SCRATCH = os.environ.get("SESSION_SCRATCH") or tempfile.mkdtemp(prefix="b939_")
os.makedirs(SCRATCH, exist_ok=True)
T00 = time.time()
RES = {"cell": "B939 Klein assembly (sharp pair)", "checks": {}}


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


def REC(name, value, detail=""):
    RES["checks"][name] = {"value": value, "detail": str(detail)}
    log(f"  [DATA] {name} = {value} {detail}")


# ================================================================ [0] build
log("[0] B854 build (isolated exec, chdir scratch, __file__ set) ...")
cwd = os.getcwd()
g6 = {"__file__": os.path.join(SCRATCH, "e6_centralizer.py"),
      "__name__": "b854_build"}
src = open(os.path.join(REPO, "frontier", "B854_centralizer_exact",
                        "e6_centralizer.py")).read()
try:
    os.chdir(SCRATCH)
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, "b854", "exec"), g6)
finally:
    os.chdir(cwd)

ROOTS = [tuple(r) for r in g6["ROOTS"]]
IDX = {r: i for i, r in enumerate(ROOTS)}
CMAT = [list(row) for row in g6["C"]]
ns = list(g6["ns"])                       # [8, 14, 16, 22]
INV = {n: [Fr(c) for c in g6["INV"][n]] for n in ns}
BB = g6["BB"]                             # 78x78 bracket table (Fractions)
eps_fn = g6["eps"]
Ipoly = {n: [int(c) for c in g6["Ipoly"][n]] for n in ns}
CHK("build_78dim_72roots_ns", len(ROOTS) == 72 and sorted(ns) == [8, 14, 16, 22])

BBnz = [[[(k, Bv[k]) for k in range(78) if Bv[k]] for Bv in row] for row in BB]

# ================================================================ [1] machinery
log("[1] gmap machinery (d2_decode conventions) + tau cocycle solve ...")
FLIP = {0: 5, 5: 0, 1: 1, 2: 4, 4: 2, 3: 3}


def flipw(w):
    return tuple(w[FLIP[i]] for i in range(6))


# F2 cocycle solve for the tau lift (B907 route, re-run -- as in d2_decode [2])
rows, rhs = [], []
for a_ in ROOTS:
    for b_ in ROOTS:
        s_ = tuple(a_[i] + b_[i] for i in range(6))
        if s_ in IDX:
            row = [0] * 72
            row[IDX[a_]] ^= 1
            row[IDX[b_]] ^= 1
            row[IDX[s_]] ^= 1
            cc = eps_fn(a_, b_) * eps_fn(flipw(a_), flipw(b_))
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


IDMAP = [(k, 1) for k in range(78)]


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


def apply_gmap(g, vec):
    img = [Fr(0)] * 78
    for k in range(78):
        if vec[k]:
            j, c = g[k]
            img[j] += c * vec[k]
    return img


def pattern_of_gmap(g):
    """+-diagonal action on the four charges; None entries where broken."""
    out = {}
    for n in ns:
        vec = INV[n]
        img = apply_gmap(g, vec)
        ev = None
        okay = True
        for k in range(78):
            if vec[k] == 0 and img[k] == 0:
                continue
            if vec[k] == 0:
                okay = False
                break
            rt = img[k] / vec[k]
            if rt not in (1, -1):
                okay = False
                break
            if ev is None:
                ev = int(rt)
            elif int(rt) != ev:
                okay = False
                break
        out[n] = ev if okay else None
    return out


def rank_of(vecs):
    """exact rank over Q of a list of 78-dim Fraction vectors."""
    m = [list(v) for v in vecs]
    rank = 0
    col = 0
    nrow = len(m)
    while rank < nrow and col < 78:
        piv = next((i for i in range(rank, nrow) if m[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        m[rank], m[piv] = m[piv], m[rank]
        pv = m[rank][col]
        m[rank] = [x / pv for x in m[rank]]
        for i in range(nrow):
            if i != rank and m[i][col] != 0:
                c = m[i][col]
                m[i] = [x - c * y for x, y in zip(m[i], m[rank])]
        rank += 1
        col += 1
    return rank


CHK("frame_rank_4", rank_of([INV[n] for n in ns]) == 4)

# the characters (banked addresses, cited in the header)
CHI_P = (1, -1, 1, -1, 1, 1)              # B907 verdict: the wall character
CHI_M = tuple(-x for x in CHI_P)
ALL_MINUS = (-1,) * 6
CHI_C = (1, -1, -1, 1, -1, 1)             # B907 inner sweep: compact-flip
CHI_ALL = (1, 1, -1, -1, -1, 1)           # B907 completeness: outer all-flip
ALL_ONES = (1,) * 6

g_schip = inner_gmap(CHI_P)
g_schim = inner_gmap(CHI_M)
g_sm1 = inner_gmap(ALL_MINUS)
g_sc = inner_gmap(CHI_C)
g_phip = outer_gmap(CHI_P)
g_phim = outer_gmap(CHI_M)
g_phall = outer_gmap(CHI_ALL)
g_tau = outer_gmap(ALL_ONES)

# ================================================================ [2] K4
log("[2] the wall Klein K4 = {1, sigma_chi+, sigma_chi-, sigma_-1} ...")
CHK("K4_members_are_automorphisms",
    all(is_automorphism_gmap(g) for g in (g_schip, g_schim, g_sm1)))
CHK("K4_members_are_involutions",
    all(gmap_compose(g, g) == IDMAP for g in (g_schip, g_schim, g_sm1)))
CHK("K4_klein_closure_chip_o_chim_equals_allminus",
    gmap_compose(g_schip, g_schim) == g_sm1
    and gmap_compose(g_schip, g_sm1) == g_schim,
    "{1, s_chi+, s_chi-, s_-1} is a Klein four-group in Inn(e6)")

pat_sm1 = pattern_of_gmap(g_sm1)
pat_chip = pattern_of_gmap(g_schip)
pat_chim = pattern_of_gmap(g_schim)
CHK("sigma_allminus_frame_action_TRIVIAL",
    pat_sm1 == {8: 1, 14: 1, 16: 1, 22: 1},
    "sigma_-1 fixes all four charges (matches banked B907 inner sweep row)")
CHK("sigma_chi_pm_frame_action_BROKEN",
    all(v is None for v in pat_chip.values())
    and all(v is None for v in pat_chim.values()),
    "sigma_chi+- do NOT act +-diagonally on any charge "
    "(matches banked B907 inner sweep rows: eps None)")

# sharper: sigma_chi+ does not even preserve the frame SPAN or either pencil
FRAME = [INV[n] for n in ns]
img_frame = [apply_gmap(g_schip, v) for v in FRAME]
rk_joint = rank_of(FRAME + img_frame)
REC("rank_frame_plus_sigma_chip_image", rk_joint,
    "4 would mean span-preserving; 8 = maximal breakage")
CHK("sigma_chip_does_NOT_preserve_frame_span", rk_joint > 4)
for (nm, pair) in (("noncompact_pencil", (8, 16)),
                   ("compact_pencil", (14, 22))):
    P = [INV[pair[0]], INV[pair[1]]]
    rp = rank_of(P + [apply_gmap(g_schip, v) for v in P])
    REC(f"rank_{nm}_plus_sigma_chip_image", rp, "2 = plane preserved")
    CHK(f"sigma_chip_does_NOT_preserve_{nm}", rp > 2)

# ================================================================ [3] C8
log("[3] the frame-realizing group C8 = <phi+, sigma_c, sigma_-1> ...")
CHK("C8_generators_are_automorphisms",
    all(is_automorphism_gmap(g) for g in (g_phip, g_sc)))
CHK("C8_generators_are_involutions",
    gmap_compose(g_phip, g_phip) == IDMAP
    and gmap_compose(g_sc, g_sc) == IDMAP)
CHK("C8_generators_commute_pairwise",
    gmap_compose(g_phip, g_sc) == gmap_compose(g_sc, g_phip)
    and gmap_compose(g_phip, g_sm1) == gmap_compose(g_sm1, g_phip)
    and gmap_compose(g_sc, g_sm1) == gmap_compose(g_sm1, g_sc))
CHK("phi_minus_equals_phi_plus_o_sigma_allminus",
    gmap_compose(g_phip, g_sm1) == g_phim,
    "the two wall conjugations differ by the frame-trivial leg")
CHK("outer_allflip_equals_phi_plus_o_sigma_c",
    gmap_compose(g_phip, g_sc) == g_phall,
    "the banked B907 outer all-flip member (1,1,-1,-1,-1,1) IS phi+ o sigma_c")


def closure(gens):
    seen = {tuple(IDMAP): IDMAP}
    frontier = [IDMAP]
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                gh = gmap_compose(g, h)
                t = tuple(gh)
                if t not in seen:
                    seen[t] = gh
                    nxt.append(gh)
        frontier = nxt
    return list(seen.values())


C8 = closure([g_phip, g_sc, g_sm1])
CHK("C8_order_8_elementary_abelian", len(C8) == 8,
    "<phi+, sigma_c, sigma_-1> = (Z2)^3 -- the banked 8 C-compatible census "
    "members (B907 completeness C3 table), now verified as a GROUP")
pats = [pattern_of_gmap(g) for g in C8]
patset = sorted({tuple(p[n] for n in ns) for p in pats})
CHK("C8_frame_pattern_image_is_the_KLEIN",
    patset == [(-1, -1, -1, -1), (-1, 1, -1, 1),
               (1, -1, 1, -1), (1, 1, 1, 1)],
    "P(C8) = W_frame = {identity, compact-flip, noncompact-flip, all-flip} "
    "= the solo LIII / FS4 Klein, REALIZED")
kernel = [g for g, p in zip(C8, pats)
          if tuple(p[n] for n in ns) == (1, 1, 1, 1)]
CHK("C8_pattern_kernel_is_1_sigma_allminus",
    len(kernel) == 2 and any(g == g_sm1 for g in kernel),
    "ker(P) = {1, sigma_-1}: the frame-invisible leg")
# V_wall = the wall-conjugation Klein, inside C8
CHK("V_wall_klein_inside_C8",
    gmap_compose(g_phip, g_phim) == g_sm1
    and all(tuple(g) in {tuple(x) for x in C8}
            for g in (g_phip, g_phim, g_sm1)),
    "{1, phi+, phi-, sigma_-1} is a Klein subgroup of C8; frame image = "
    "{identity, noncompact-flip} (a Z2 only)")

# ================================================================ [4] verdict
log("[4] THE SHARP PAIR: K4 vs W_frame realizations ...")
K4 = [IDMAP, g_schip, g_schim, g_sm1]
K4set = {tuple(g) for g in K4}
C8set = {tuple(g) for g in C8}
inter = K4set & C8set
CHK("K4_cap_C8_is_exactly_1_sigma_allminus",
    inter == {tuple(IDMAP), tuple(g_sm1)},
    "the two Kleins share EXACTLY one nonidentity element: sigma_-1 "
    "(= the wall twist D on the 27; frame-trivial)")
JOINT = closure([g_schip, g_sm1, g_sc, g_phip])
CHK("joint_group_is_Z2_to_the_4", len(JOINT) == 16,
    "<K4 u C8> = (Z2)^4: 16 commuting monomial involutions")
jpats = Counter()
for g in JOINT:
    p = pattern_of_gmap(g)
    t = tuple(p[n] for n in ns)
    jpats[t if all(v is not None for v in t) else "BROKEN"] += 1
REC("joint_group_pattern_census", {str(k): v for k, v in jpats.items()},
    "each Klein pattern x2 carriers + 8 frame-breaking elements")
CHK("joint_census_shape",
    jpats["BROKEN"] == 8 and all(
        jpats[t] == 2 for t in [(1, 1, 1, 1), (1, -1, 1, -1),
                                (-1, 1, -1, 1), (-1, -1, -1, -1)]))

RES["verdict_sharp_pair"] = (
    "DISTINCT SUBGROUPS OF Aut(e6), overlapping in exactly {1, sigma_-1}. "
    "K4 (the wall 2-torsion, inner, Cartan-fixing) does NOT act on the "
    "frame: two of its legs break every charge line and neither pencil "
    "plane survives. W_frame is realized by the OTHER Klein-carrying group "
    "C8 = <phi+, sigma_c, sigma_-1> (the C-compatible census subgroup), "
    "with P(C8) = W_frame and ker P = {1, sigma_-1}. The shared leg "
    "sigma_-1 is the frame-invisible one -- the B912/B928 wall twist D.")
log(RES["verdict_sharp_pair"])
dump()

# ================================================================ [5] holonomy
log("[5] the shared leg IS the holonomy quaternion: sigma_-1 = Ad(i) ...")
# (a) chi_allminus(r) = (-1)^{ht r} for all 72 roots
ch_m1 = chi_of(ALL_MINUS)
CHK("chi_allminus_equals_height_parity_all_72_roots",
    all(ch_m1(r) == (-1) ** (sum(r) % 2) for r in ROOTS))
# (b) the principal h has alpha_j(h) = 2 for every simple root
hpr = [Fr(c) for c in g6["h"]]
simple = []
for i in range(6):
    u = [0] * 6
    u[i] = 1
    simple.append(tuple(u))
ok = True
for srt in simple:
    ev = g6["evec"](srt)
    out = g6["br"](hpr, [Fr(c) for c in ev])
    ok = ok and (out == [Fr(2) * Fr(c) for c in ev])
CHK("principal_h_is_2rho_check_alpha_j_of_h_equals_2", ok,
    "so Ad(exp(i*pi*h/2)) e_alpha = (-1)^{ht alpha} e_alpha = sigma_-1")
# (c) exp(i*pi*h_sl2/2) = diag(i,-i) is the 2T quaternion 'i' of the build
import sympy as sp
Iq = sp.I
target = sp.Matrix([[Iq, 0], [0, -Iq]])
G24 = g6["G"]
CHK("diag_i_minus_i_is_in_the_2T_list",
    any((M - target).applyfunc(sp.expand) == sp.zeros(2, 2) for M in G24),
    "sigma_-1 = Ad of the holonomy quaternion i (via the principal SL2); "
    "consistency: as a 2T element it MUST fix all four charges -- and its "
    "frame pattern is indeed trivial (stage [2])")

# ================================================================ [6] 2O bridge
log("[6] the octahedral bridge: s in 2O \\ 2T realizes the compact flip ...")
z8 = (1 + Iq) / sp.sqrt(2)                # the quaternion (1+i)/sqrt2
CHK("s_not_in_2T",
    not any((M - sp.Matrix([[z8, 0], [0, sp.conjugate(z8)]])
             ).applyfunc(sp.radsimp) == sp.zeros(2, 2) for M in G24))
# s normalizes 2T: s M s^-1 = [[M00, i*M01], [-i*M10, M11]] exactly
G24keys = set()
for M in G24:
    G24keys.add(tuple(sp.expand(x) for x in
                      (M[0, 0], M[0, 1], M[1, 0], M[1, 1])))
ok = True
for M in G24:
    conj = (sp.expand(M[0, 0]), sp.expand(Iq * M[0, 1]),
            sp.expand(-Iq * M[1, 0]), sp.expand(M[1, 1]))
    if conj not in G24keys:
        ok = False
CHK("s_normalizes_2T_exactly", ok, "s in 2O, the octahedral extension")
# s action on the four invariant forms: coefficient of x^{n-j} y^j scales
# by z8^{n-2j}; the sign per block:
sgn = {}
for n in ns:
    powers = {(n - 2 * j) % 8 for j, c in enumerate(Ipoly[n]) if c}
    vals = {sp.expand(z8 ** k) for k in powers}
    CHK(f"form_x{n}_transforms_by_a_single_sign",
        vals == {sp.Integer(1)} or vals == {sp.Integer(-1)},
        f"support powers mod 8: {sorted(powers)}")
    sgn[n] = 1 if vals == {sp.Integer(1)} else -1
CHK("octahedral_element_realizes_the_COMPACT_FLIP",
    [sgn[n] for n in ns] == [1, -1, 1, -1],
    "Ad(s)|frame = (+,-,+,-): s flips exactly the t-carrying (compact) "
    "charges -- the hemisphere split IS t-parity, realized inside the "
    "principal SL2's normalizer of the holonomy")

# ================================================================ [7] tau
log("[7] tau and the pencil planes ...")
CHK("tau_is_automorphism_involution",
    is_automorphism_gmap(g_tau) and gmap_compose(g_tau, g_tau) == IDMAP)
pat_tau = pattern_of_gmap(g_tau)
CHK("tau_frame_action_BROKEN",
    all(v is None for v in pat_tau.values()),
    "the bare theta-lift does NOT act +-diagonally on the frame "
    "(matches banked B907 outer sweep chi=1 row); only its chi-signed "
    "dressings phi+-, phi_all do")
img_frame_tau = [apply_gmap(g_tau, v) for v in FRAME]
REC("rank_frame_plus_tau_image", rank_of(FRAME + img_frame_tau),
    "4 = span preserved, 8 = fully broken")

# ================================================================ [8] shadows
log("[8] the 27-shadows tie the table to B928's D-set ...")
REPJ = json.load(open(os.path.join(REPO, "frontier", "B883_the_27",
                                   "rep27.json")))
REP = [[[int(x) for x in row] for row in REPJ["rep"][str(k)]]
       for k in range(78)]
B912 = json.load(open(os.path.join(REPO, "frontier", "B912_norm_cell",
                                   "results.json")))
Dd_banked = [int(x) for x in B912["D_diag"]]
B916 = json.load(open(os.path.join(REPO, "frontier", "B916_lambda_bridge",
                                   "results.json")))
D2_banked = [int(x) for x in B916["H_prime_diag_vs_H_plus"]["D2"]]


def rep_diagonal_of_inner(signs):
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


T_m1 = rep_diagonal_of_inner(ALL_MINUS)
T_chim = rep_diagonal_of_inner(CHI_M)
T_c = rep_diagonal_of_inner(CHI_C)
CHK("shadow_sigma_allminus_is_banked_D_12_flips",
    T_m1 is not None and (T_m1 == Dd_banked
                          or [-x for x in T_m1] == Dd_banked)
    and min(T_m1.count(-1), T_m1.count(1)) == 12)
CHK("shadow_sigma_chim_is_banked_D2_11_flips",
    T_chim is not None and (T_chim == D2_banked
                            or [-x for x in T_chim] == D2_banked)
    and min(T_chim.count(-1), T_chim.count(1)) == 11)
CHK("shadow_sigma_c_is_Dc_12_flips",
    T_c is not None and min(T_c.count(-1), T_c.count(1)) == 12,
    "the compact-flip's 27-shadow: the census D_c (B928 flip counts "
    "0,12,12,12 for {I, D, D_c, D_c D})")
REC("shadow_summary",
    {"sigma_-1 -> D (wall twist)": 12,
     "sigma_chi- -> D2 (the ELEVEN)": 11,
     "sigma_c -> D_c": 12},
    "K4's frame-invisible legs are 27-visible; W_frame's carriers cast "
    "the census D-set")

RES["verdict"] = "COMPLETE"
dump()
log("DONE. results.json written.")
