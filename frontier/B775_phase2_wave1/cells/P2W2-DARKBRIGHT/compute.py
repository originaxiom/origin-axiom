"""P2W2-DARKBRIGHT (OI-044) -- the D3(a) bright/dark classification criterion.

QUESTION (Review 3, still-open item): produce the EXPLICIT criterion on a seed pair
(m1,m2) that decides bright vs dark, where
    dark  <=>  the s-matrix (the sqrt(-15) coefficient of the H-projected DFT of the
               level-15 partial-trace table tr(Par * W_{m1}^j * W_{m2}^l)) vanishes
               identically;  bright <=> some s-cell is nonzero.
Banked classification (B367/B385/B390):
    BRIGHT = {(1,2),(2,3),(2,4),(3,4),(1,7),(3,7),(2,7)}
    DARK   = {(1,3),(1,4),(3,5),(1,5),(4,5)}    out-of-sample (B390): (2,5) DARK.
    acceptance riddle: (1,3) DARK  vs  (3,4) BRIGHT.

WHAT THIS CELL ESTABLISHES (all in-cell, exact, re-runnable):
  Part A.  Reproduce the bright/dark verdict for (1,3),(1,4),(3,4) directly from the
           theta construction -- the discriminating facts IN CELL, not cited.  This is
           B390's verified effective test (the s-channel via the local q=3*q=5
           convolution); confirmed 12/12+OOS by re-running B390 (see NOTE below).
  Part B.  Map the closed-form landscape and TWO complementary no-go facts:
           (B1) UNMARKED wall: (1,3)-dark and (3,4)-bright generate SL(2,Z/15) subgroups
                with a BYTE-IDENTICAL unmarked bundle (|G|, orders, trace-15/3/5 and
                det(g-I) multisets, CRT images, -I).  => no class/character function of
                the *group* separates them  (this is B385's kill, re-derived in-cell).
           (B2) MARKED wall: the canonical marked SL(2) coordinate -- the commutator /
                Fricke trace  kappa = tr[g1,g2] = x1^2+x2^2+z^2 - x1 x2 z - 2 -- takes
                the IDENTICAL value kappa(1,4)=kappa(3,4) = -142, yet (1,4) is DARK and
                (3,4) is BRIGHT.  => the commutator coordinate cannot separate either.
           (B3) NO single closed-form congruence/QR/threshold on the seed traces
                (kappa, z=tr g1g2, w=tr g1g2^-1, mod 3/5/15, QR classes) yields a 12/12
                rule; the best seed-level rule tops out at 11/12 (defeated by the riddle).
  Part C.  Verdict.  An explicit VERIFIED *effective* characterization exists (B390:
           locality to a fixed rank-2 sqrt(-15) form, 12/12+OOS), but the intended
           closed-form arithmetic criterion on (m1,m2) does NOT exist at any natural
           seed/group/marked-trace level (B1-B3), and B385 localizes the genuine
           separator to the non-abelian v_word (Heisenberg-accumulation) layer, which
           is unreduced.  Chord discipline (B774): the s-channel factorizes through a
           character-level object, so it is not itself the theta-odd criterion.
           Terminal: UNRESOLVED, WALLED against the natural closed forms.
"""
import json, os, sys
from fractions import Fraction as Fr
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
FRONT = os.path.join(HERE, "..", "..", "..")
for d in ("B358_seam_certification", "B367_value_map", "B386_crt_closed_form"):
    sys.path.insert(0, os.path.join(FRONT, d))
import cyclo_engine as E                                    # noqa: E402
import seam_certification as SC                             # noqa: E402
from step0_exact_matrices import build_theta_W, matrix_order  # noqa: E402
from tensor_gate import local_partrace_table               # noqa: E402

BRIGHT = {(1, 2), (2, 3), (2, 4), (3, 4), (1, 7), (3, 7), (2, 7)}
DARK = {(1, 3), (1, 4), (3, 5), (1, 5), (4, 5)}
ALLPAIRS = sorted(BRIGHT | DARK)

# =====================================================================================
# Part A -- reproduce the s-channel bright/dark verdict in-cell for (1,3),(1,4),(3,4).
# =====================================================================================
def s_bright(m1, m2):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1, _ = matrix_order(W1); o2, _ = matrix_order(W2)
    T3 = local_partrace_table(3, 2, m1, m2, o1, o2)
    T5 = local_partrace_table(5, 2, m1, m2, o1, o2)
    z1, z2 = 60 // o1, 60 // o2
    n_cells = 0; svals = []
    for a in range(o1):
        for b in range(o2):
            t = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1 * j * a) % 60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(za, E.zeta((-z2 * l * b) % 60)),
                                       E.mul(T3[(j, l)], T5[(j, l)])))
            sol = SC.solve_H(SC.H_avg(E.scal(Fr(1, o1 * o2), t)))
            if sol and sol[3] != 0:
                n_cells += 1; svals.append(sol[3])
    return dict(ords=[o1, o2], s_bright=(n_cells > 0), n_s_cells=n_cells,
                sum_s_sq=str(sum((v * v for v in svals), Fr(0))))

print("== Part A: bright/dark verdict reproduced in-cell (theta s-channel) ==")
partA = {}
for (m1, m2) in [(1, 3), (1, 4), (3, 4)]:
    r = s_bright(m1, m2)
    banked = "bright" if (m1, m2) in BRIGHT else "dark"
    pred = "bright" if r["s_bright"] else "dark"
    r["banked"] = banked; r["predicted"] = pred; r["match"] = (pred == banked)
    partA[f"{m1},{m2}"] = r
    print(f"  ({m1},{m2}) banked={banked:6s} predicted={pred:6s} "
          f"s_cells={r['n_s_cells']:2d} sum_s^2={r['sum_s_sq']}  "
          f"{'OK' if r['match'] else 'MISMATCH'}")
A_ok = all(v["match"] for v in partA.values())
print(f"  Part A: 3/3 verdicts reproduced = {A_ok}  "
      f"(full 12/12+OOS via B390 tensor machinery, re-run this session)")

# =====================================================================================
# Part B -- the closed-form landscape + the two walls.
# gamma_m = [[1+m^2, m],[m, 1]] mod 15 (P64 leg; det 1).
# =====================================================================================
N15 = 15
def gm(m): return ((1 + m * m) % N15, m % N15, m % N15, 1 % N15)
def mmul15(A, B):
    a, b, c, d = A; e, f, g, h = B
    return ((a*e + b*g) % N15, (a*f + b*h) % N15, (c*e + d*g) % N15, (c*f + d*h) % N15)
I15 = (1, 0, 0, 1); mI15 = (N15 - 1, 0, 0, N15 - 1)
def gen_group(g1, g2):
    seen = {I15}; frontier = [I15]; gens = [g1, g2]
    while frontier:
        nf = []
        for x in frontier:
            for g in gens:
                y = mmul15(x, g)
                if y not in seen: seen.add(y); nf.append(y)
        frontier = nf
    return seen
def elt_order(g):
    x = g; k = 1
    while x != I15:
        x = mmul15(x, g); k += 1
        if k > 720: raise RuntimeError("order overflow")
    return k
def trace(g): return (g[0] + g[3]) % N15
def reduce_mod(g, p): return tuple(v % p for v in g)

def unmarked_bundle(m1, m2):
    """Invariants of the GROUP <g1,g2> only (no marking)."""
    G = gen_group(gm(m1), gm(m2))
    def detgmI(g):
        a, b, c, d = g
        return ((a - 1) * (d - 1) - b * c) % N15
    return dict(
        absG=len(G),
        absG3=len({reduce_mod(g, 3) for g in G}),
        absG5=len({reduce_mod(g, 5) for g in G}),
        minusI_in_G=(mI15 in G),
        order_multiset=dict(sorted(Counter(elt_order(g) for g in G).items())),
        trace15_multiset=dict(sorted(Counter(trace(g) for g in G).items())),
        trace3_multiset=dict(sorted(Counter(sum(reduce_mod(g, 3)[i] for i in (0, 3)) % 3
                                             for g in G).items())),
        trace5_multiset=dict(sorted(Counter(sum(reduce_mod(g, 5)[i] for i in (0, 3)) % 5
                                             for g in G).items())),
        detgmI_class_multiset=dict(sorted(Counter(detgmI(g) for g in G).items())),
    )

# ---- B1: UNMARKED wall ----
print("\n== Part B1: UNMARKED group-invariant wall  (1,3)-dark  vs  (3,4)-bright ==")
u13 = unmarked_bundle(1, 3); u34 = unmarked_bundle(3, 4)
unmarked_identical = (u13 == u34)
print(f"  |G(1,3)|={u13['absG']} (mod3={u13['absG3']},mod5={u13['absG5']}); "
      f"|G(3,4)|={u34['absG']} (mod3={u34['absG3']},mod5={u34['absG5']})")
print(f"  order multiset match : {u13['order_multiset']==u34['order_multiset']}")
print(f"  trace15 multiset match: {u13['trace15_multiset']==u34['trace15_multiset']}")
print(f"  det(g-I) multiset match: {u13['detgmI_class_multiset']==u34['detgmI_class_multiset']}")
print(f"  UNMARKED BUNDLE IDENTICAL: {unmarked_identical}   -> no group invariant separates")

# ---- marked SL(2) trace coordinates ----
def trg(m): return 2 + m * m                       # tr gamma_m           (over Z)
def trz(a, b): return 2 + (a + b) ** 2 + (a * b) ** 2   # tr g1 g2         (over Z)
def trw(a, b): return 2 + (a - b) ** 2             # tr g1 g2^-1          (over Z)
def kappa(a, b):
    x, y, z = trg(a), trg(b), trz(a, b)
    return x * x + y * y + z * z - x * y * z - 2   # Fricke commutator trace

# ---- B2: MARKED (commutator) wall ----
print("\n== Part B2: MARKED commutator/Fricke wall  (1,4)-dark  vs  (3,4)-bright ==")
k14, k34 = kappa(1, 4), kappa(3, 4)
kappa_wall = (k14 == k34)
print(f"  kappa(1,4)={k14}  (DARK) ;  kappa(3,4)={k34}  (BRIGHT)")
print(f"  commutator trace IDENTICAL across opposite verdict: {kappa_wall}"
      f"   -> the canonical marked coordinate cannot separate")

# ---- B3: no single closed-form congruence gives 12/12 ----
print("\n== Part B3: does ANY single seed-trace congruence/QR separate 12/12? ==")
def qr(n, p):
    n %= p
    return 0 if n == 0 else (1 if pow(n, (p - 1) // 2, p) == 1 else -1)
inv = {}
for (a, b) in ALLPAIRS:
    k, z, w = kappa(a, b), trz(a, b), trw(a, b)
    inv[(a, b)] = {
        "kappa%3": k % 3, "kappa%5": k % 5, "kappa%15": k % 15,
        "kappa_qr3": qr(k, 3), "kappa_qr5": qr(k, 5),
        "z%3": z % 3, "z%5": z % 5, "z%15": z % 15, "z_qr5": qr(z, 5), "z_qr3": qr(z, 3),
        "w%3": w % 3, "w%5": w % 5, "w%15": w % 15, "w_qr5": qr(w, 5), "w_qr3": qr(w, 3),
        "z%5==0": 1 if z % 5 == 0 else 0,
    }
separators = []
for name in next(iter(inv.values())):
    bvals = {inv[p][name] for p in ALLPAIRS if p in BRIGHT}
    dvals = {inv[p][name] for p in ALLPAIRS if p in DARK}
    if bvals.isdisjoint(dvals):
        separators.append(name)
print(f"  single-invariant value-set separators (disjoint bright/dark): {separators or 'NONE'}")
# best 'has an (ell,ell) seed' rule (the banked 11/12), for the record
def seed_type(m, p):
    disc = (m * m * (m * m + 4)) % p
    if disc == 0: return "par"
    return "hyp" if pow(disc, (p - 1) // 2, p) == 1 else "ell"
seed_types = {m: (seed_type(m, 3), seed_type(m, 5))
              for m in sorted({m for pr in ALLPAIRS for m in pr})}
conf = sum((any(seed_types[m] == ("ell", "ell") for m in pr) == (pr in BRIGHT))
           for pr in ALLPAIRS)
print(f"  best banked seed rule 'has (ell,ell) seed' = {conf}/12 (fails only the riddle)")
print(f"  seed types (t@3,t@5): {seed_types}")

# =====================================================================================
# Part C -- VERDICT BLOCK
# =====================================================================================
print("\n== Part C: verdict ==")
effective_test_verified = A_ok and (partA["1,3"]["predicted"] == "dark"
                                    and partA["3,4"]["predicted"] == "bright")
unmarked_walled = unmarked_identical            # B1
marked_walled = kappa_wall                      # B2
no_single_separator = (len(separators) == 0)    # B3
no_seed_12 = (conf < 12)

closed_form_walled = unmarked_walled and marked_walled and no_single_separator and no_seed_12

if effective_test_verified and closed_form_walled:
    verdict = "UNRESOLVED"
    terminal = ("WALLED: no closed-form seed/group/marked-trace criterion; "
                "verified EFFECTIVE test (B390 s-channel locality, 12/12+OOS) standing; "
                "genuine separator is the non-abelian v_word layer (B385), unreduced")
    headline = ("D3(a) has an explicit VERIFIED effective test (bright <=> the sqrt(-15) "
                "coefficient of the local q=3*q=5 convolution is nonzero -- a fixed rank-2 "
                "form, 12/12 + out-of-sample), but NO closed-form arithmetic criterion on "
                "(m1,m2): the unmarked SL(2,Z/15) group bundle is identical for "
                "(1,3)-dark and (3,4)-bright, the canonical marked commutator trace is "
                "identical for (1,4)-dark and (3,4)-bright (kappa=-142), and no single "
                "seed-trace congruence beats 11/12; the genuine separator lives in the "
                "non-abelian v_word (Heisenberg) layer and is unreduced to closed form.")
elif effective_test_verified and not closed_form_walled and no_single_separator is False:
    verdict = "RESOLVED-A"
    terminal = "a closed-form seed invariant separates 12/12"
    headline = f"seed separators found: {separators}"
else:
    verdict = "UNRESOLVED"
    terminal = "inconclusive / reproduction incomplete"
    headline = "see partial results"

discriminating_fact = (
    "TWO in-cell no-go facts against a closed-form seed criterion: "
    "(B1) (1,3)-DARK and (3,4)-BRIGHT have a byte-identical UNMARKED SL(2,Z/15) group "
    "bundle (|G|=%d, mod3=%d, mod5=%d; identical order/trace-15/3/5 and det(g-I) "
    "multisets); (B2) (1,4)-DARK and (3,4)-BRIGHT share the identical canonical MARKED "
    "coordinate kappa=tr[g1,g2]=-142.  s-channel (reproduced in-cell): (1,3)=0 cells "
    "DARK, (1,4)=%d cells DARK, (3,4)=%d cells BRIGHT.  No single seed-trace congruence "
    "beats %d/12."
    % (u13["absG"], u13["absG3"], u13["absG5"],
       partA["1,4"]["n_s_cells"], partA["3,4"]["n_s_cells"], conf)
)

results = {
    "cell": "P2W2-DARKBRIGHT", "OI": "OI-044",
    "definition": "dark <=> s-matrix (sqrt(-15) coeff of H-proj DFT pair-trace) == 0",
    "verdict": verdict, "terminal_state": terminal, "headline": headline,
    "discriminating_fact": discriminating_fact,
    "partA_riddle_verdicts": partA,
    "partA_all3_reproduced": A_ok,
    "partB1_unmarked_bundle_13": u13,
    "partB1_unmarked_bundle_34": u34,
    "partB1_unmarked_identical": unmarked_identical,
    "partB2_kappa_14": k14, "partB2_kappa_34": k34,
    "partB2_commutator_wall": kappa_wall,
    "partB3_single_separators": separators,
    "partB3_best_seed_rule_score": f"{conf}/12",
    "seed_types": {str(k): list(v) for k, v in seed_types.items()},
    "effective_test": ("B390: bright <=> sqrt(-15) coeff of the local q=3*q=5 convolution "
                       "is nonzero (rank-2 pairing); verified 12/12 + out-of-sample (2,5); "
                       "re-run this session (tensor gate PASS, G1+G2 12/12)."),
    "chord_discipline_note": (
        "B774: the s-channel is theta-odd but factorizes through a rank-2 bilinear form "
        "on abelian local spectra (B390) -- a character-level object.  B385 verified that "
        "group and character/word-statistic invariants do NOT separate; the only layer "
        "that sees the riddle is the non-abelian v_word (Heisenberg-accumulated word "
        "shift).  So the s-channel test is an effective characterization, not the closed "
        "theta-odd criterion; presenting it as 'the criterion' would be a relabeled trace "
        "invariant (the flagged failure mode)."),
    "base_rate_caveat": (
        "With enough ad-hoc Boolean features one can always fit 12 labeled points; the "
        "honest statement is that no NATURAL single seed-trace congruence/QR separates, "
        "and two identical-invariant/opposite-verdict pairs prove the two canonical "
        "candidate levels (unmarked group; commutator trace) cannot."),
    "gate_5Q": dict(structural_only=True, no_SM_values=True, no_consciousness=True,
                    nothing_to_CLAIMS=True, one_number_pin_untouched=True),
}
print(f"  VERDICT: {verdict}")
print(f"  TERMINAL: {terminal}")
print(f"  {headline}")

with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(results, fh, indent=1, default=str)
print("\nresults.json written. DONE")
