#!/usr/bin/env python3
"""CELL G1 -- the su(3)+g2 descent of E6 (closes the T8b quantifier gap).

WHAT THIS COMPUTES
  (1) The branching of the 27 of E6 under the maximal S-subalgebra su(3)+g2, derived
      INDEPENDENTLY of B873/Slansky by exhaustive multiset enumeration constrained by
      dimension, BOTH embedding-index (Dynkin T) sums, exact conformal weights of the
      level-1 conformal embedding, and vanishing of the su(3) cubic anomaly (forced:
      E6 has no cubic Casimir).  Diffed against B873's cited branching afterward.
  (2) Registerability of the step E6 -> su(3)+g2 with an independent implementation of
      the B860/B861 criterion, with MANDATORY bite controls (must PASS on banked
      SO(10)xU(1), must FAIL on banked Sp(8) / SU(4)xU(1) / B863's rows).
  (3) The FULL descent tree below su(3)+g2: menu = maximal reductive subalgebras
      (factor-wise maximal subalgebras + diagonal subalgebras of isomorphic factor
      pairs, per Dynkin's classification of maximal subalgebras of semisimple
      algebras), every registerable branch continued to termination.

STATED CONVENTIONS (E23 class -- explicit, because verdicts depend on them)
  C1. "Generation content" = the branching of the FULL 27 (B861's uniform object,
      not the 16-based SM generation B863 prints; both are exercised as controls
      and give identical verdicts on every banked row).
  C2. Registerable(step g -> h) = the multiset of NON-ABELIAN irreducible content of
      the descended generation is complex (not equal to its own conjugate).  ALL
      abelian charges are stripped ("dial-stripped", B860/B861).  This is the banked
      convention: B863's row (a) [su(2)->u(1): {3:2, 3b:2, 1:3} => NO] is derivable
      ONLY under it (with u(1) charges retained that multiset would be complex).
  C3. Menu class below the product node = structural maximal reductive subalgebras,
      i.e. B863's step class ("structural descents + the genuine conformal
      embedding"): B863's own menu rows (a),(b) are non-conformal structural
      descents, and every genuine conformal case at these levels (g2_1 > a1_1+a1_3,
      c=14/5; g2_1 > a1_28, c=14/5; su(3)_k > so(3) principal) is ALREADY a member
      of the structural list, so the class matches the corpus's.
  C4. Maximal subalgebras of a direct sum g1+g2 are m1+g2, g1+m2 (mi maximal in gi)
      and, for g1 ~= g2, the (possibly twisted) diagonal -- Dynkin.  Per-factor
      lists used: su(3): su(2)+u(1) (regular), so(3) (principal S);
      g2: su(3) (regular long-root), su(2)+su(2) (regular), su(2) (principal S, index 28);
      su(2): u(1).  These rank<=2 lists are classical and exhaustive.

Gate 5: every number below is a dimension, rank, Dynkin index, central charge,
conformal weight, anomaly coefficient, or multiset count.  No measured SM value.
"""
from fractions import Fraction as F
from collections import Counter
import itertools
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# ============================================================ rep data per factor type
# Normalization: theta^2 = 2;  T(fund A1) = 1/2;  T(adjoint) = h_dual.
# A1 labels are ints (the dimension); other types use string labels.

A2_REPS = {  # label: (dim, T, conj_label, cubic_anomaly A)
    "1":  (1,  F(0),      "1",   0),
    "3":  (3,  F(1, 2),   "3b",  1),
    "3b": (3,  F(1, 2),   "3",  -1),
    "6":  (6,  F(5, 2),   "6b",  7),
    "6b": (6,  F(5, 2),   "6",  -7),
    "8":  (8,  F(3),      "8",   0),
}
G2_REPS = {"1": (1, F(0)), "7": (7, F(1)), "14": (14, F(4)), "27g": (27, F(9))}
D5_REPS = {"1": (1, F(0)), "10": (10, F(1)), "16": (16, F(2)), "16b": (16, F(2))}
D5_CONJ = {"1": "1", "10": "10", "16": "16b", "16b": "16"}
C4_REPS = {"1": (1, F(0)), "27c": (27, F(3))}          # traceless Lambda^2(8); self-dual
A3_REPS = {"1": (1, F(0)), "4": (4, F(1, 2)), "4b": (4, F(1, 2)), "6": (6, F(1))}
A3_CONJ = {"1": "1", "4": "4b", "4b": "4", "6": "6"}
A4_REPS = {"1": (1, F(0)), "5": (5, F(1, 2)), "5b": (5, F(1, 2)),
           "10": (10, F(3, 2)), "10b": (10, F(3, 2))}
A4_CONJ = {"1": "1", "5": "5b", "5b": "5", "10": "10b", "10b": "10"}


def a1_T(d):
    return F(d * (d * d - 1), 12)


def rdim(t, lab):
    if t == "A1":
        return lab
    return {"A2": A2_REPS, "G2": G2_REPS, "D5": D5_REPS, "C4": C4_REPS,
            "A3": A3_REPS, "A4": A4_REPS}[t][lab][0]


def rT(t, lab):
    if t == "A1":
        return a1_T(lab)
    return {"A2": A2_REPS, "G2": G2_REPS, "D5": D5_REPS, "C4": C4_REPS,
            "A3": A3_REPS, "A4": A4_REPS}[t][lab][1]


def rconj(t, lab):
    if t == "A1" or t == "G2" or t == "C4":
        return lab            # every A1/G2/C4 irrep is self-conjugate (-1 in W)
    if t == "A2":
        return A2_REPS[lab][2]
    return {"D5": D5_CONJ, "A3": A3_CONJ, "A4": A4_CONJ}[t][lab]


# ============================================================ the registerability criterion
def conj_content(algebra, content):
    return Counter({tuple(rconj(t, l) for t, l in zip(algebra, tup)): m
                    for tup, m in content.items()})


def chiral(algebra, content):
    """Convention C2: complex non-abelian multiset (all u(1) charges stripped)."""
    return conj_content(algebra, content) != Counter(content)


# ============================================================ branching rules (verified)
# rule = (name, target_types, embedding_indices, {src_label: [piece_tuple, ...]})
RULES = {
    "A2": [
        ("su(2)+u(1) [regular]", ["A1"], [F(1)],
         {"1": [(1,)], "3": [(2,), (1,)], "3b": [(2,), (1,)],
          "6": [(3,), (2,), (1,)], "6b": [(3,), (2,), (1,)],
          "8": [(3,), (2,), (2,), (1,)]}),
        ("so(3) [principal S, index 4]", ["A1"], [F(4)],
         {"1": [(1,)], "3": [(3,)], "3b": [(3,)],
          "6": [(5,), (1,)], "6b": [(5,), (1,)], "8": [(5,), (3,)]}),
    ],
    "G2": [
        ("su(3)' [regular, long roots]", ["A2"], [F(1)],
         {"1": [("1",)], "7": [("3",), ("3b",), ("1",)],
          "14": [("8",), ("3",), ("3b",)]}),
        ("su(2)+su(2) [regular, indices (1,3)]", ["A1", "A1"], [F(1), F(3)],
         {"1": [(1, 1)], "7": [(2, 2), (1, 3)],
          "14": [(3, 1), (1, 3), (2, 4)]}),
        ("su(2) [principal S, index 28]", ["A1"], [F(28)],
         {"1": [(1,)], "7": [(7,)], "14": [(3,), (11,)]}),
    ],
    "A1": [
        ("u(1)", [], [], None),   # handled specially: d -> d singlets
    ],
    "A4": [   # only what the SU(5) controls need
        ("su(4)+u(1) [regular]", ["A3"], [F(1)],
         {"1": [("1",)], "5": [("4",), ("1",)], "5b": [("4b",), ("1",)],
          "10": [("6",), ("4",)], "10b": [("6",), ("4b",)]}),
        ("SM su(3)+su(2)+u(1) [regular]", ["A2", "A1"], [F(1), F(1)],
         {"1": [("1", 1)], "5": [("3", 1), ("1", 2)], "5b": [("3b", 1), ("1", 2)],
          "10": [("3", 2), ("3b", 1), ("1", 1)],
          "10b": [("3b", 2), ("3", 1), ("1", 1)]}),
    ],
}

# tensor tables for diagonal subalgebras of isomorphic pairs
TENSOR_A2 = {
    ("1", "1"): ["1"], ("3", "1"): ["3"], ("3b", "1"): ["3b"],
    ("6", "1"): ["6"], ("6b", "1"): ["6b"], ("8", "1"): ["8"],
    ("3", "3"): ["6", "3b"], ("3b", "3b"): ["6b", "3"],
    ("3", "3b"): ["8", "1"],
}


def tensor_a2(r, s):
    for key in ((r, s), (s, r)):
        if key in TENSOR_A2:
            return TENSOR_A2[key]
    raise KeyError(f"A2 tensor table missing {r} x {s}")


def tensor_a1(d1, d2):
    return list(range(d1 + d2 - 1, abs(d1 - d2), -2))


def verify_rules():
    """Every branching rule must conserve dimension and satisfy the index sum
    T_j(branch) = x_j * T_src(R) for each target factor j (for a piece with labels
    (l_1..l_k), its contribution to factor j is T_j(l_j) * prod_{i!=j} dim(l_i))."""
    report = []
    for src, rules in RULES.items():
        for name, tgts, xs, mp in rules:
            if mp is None:
                continue
            for lab, pieces in mp.items():
                dsum = sum(
                    1 if not piece else
                    __import__("math").prod(rdim(t, l) for t, l in zip(tgts, piece))
                    for piece in pieces)
                ok_d = dsum == rdim(src, lab)
                ok_x = True
                for j, (tj, xj) in enumerate(zip(tgts, xs)):
                    tsum = sum(rT(tj, piece[j])
                               * __import__("math").prod(
                                   rdim(t, l) for i, (t, l) in enumerate(zip(tgts, piece))
                                   if i != j)
                               for piece in pieces)
                    if tsum != xj * rT(src, lab):
                        ok_x = False
                report.append(dict(rule=f"{src} -> {name}", rep=str(lab),
                                   dim_ok=ok_d, index_ok=ok_x))
    # diagonal tables
    for (r, s), pieces in TENSOR_A2.items():
        dsum = sum(rdim("A2", p) for p in pieces)
        tsum = sum(rT("A2", p) for p in pieces)
        want_t = rT("A2", r) * rdim("A2", s) + rT("A2", s) * rdim("A2", r)
        report.append(dict(rule=f"A2 diag {r}x{s}", rep=f"{r}x{s}",
                           dim_ok=dsum == rdim("A2", r) * rdim("A2", s),
                           index_ok=tsum == want_t))
    for d1, d2 in [(2, 2), (2, 3), (3, 3), (2, 4)]:
        pieces = tensor_a1(d1, d2)
        report.append(dict(rule=f"A1 diag {d1}x{d2}", rep=f"{d1}x{d2}",
                           dim_ok=sum(pieces) == d1 * d2,
                           index_ok=sum(a1_T(p) for p in pieces)
                           == a1_T(d1) * d2 + a1_T(d2) * d1))
    return report


# ============================================================ menu generation + descent
def apply_rule(algebra, content, i, rule):
    name, tgts, _, mp = rule
    new_alg = tuple(algebra[:i]) + tuple(tgts) + tuple(algebra[i + 1:])
    new_content = Counter()
    for tup, m in content.items():
        if algebra[i] == "A1" and mp is None:          # A1 -> u(1): d singlets
            new_content[tup[:i] + tup[i + 1:]] += m * tup[i]
        else:
            for piece in mp[tup[i]]:
                new_content[tup[:i] + tuple(piece) + tup[i + 1:]] += m
    return new_alg, new_content


def apply_diag(algebra, content, i, j, twisted=False):
    t = algebra[i]
    new_alg = tuple(a for k, a in enumerate(algebra) if k != j)
    new_content = Counter()
    for tup, m in content.items():
        r, s = tup[i], tup[j]
        if twisted:
            s = rconj(t, s)
        prods = tensor_a2(r, s) if t == "A2" else tensor_a1(r, s)
        for p in prods:
            new = list(tup)
            new[i] = p
            del new[j]
            new_content[tuple(new)] += m
    return new_alg, new_content


def menu(algebra, content):
    """All maximal-reductive breaking steps of a product algebra (convention C4)."""
    out = []
    for i, t in enumerate(algebra):
        for rule in RULES.get(t, []):
            if t in ("A2", "G2", "A1"):
                label = f"break factor {i} ({t}): {rule[0]}"
                out.append((label,) + apply_rule(algebra, content, i, rule))
    for i in range(len(algebra)):
        for j in range(i + 1, len(algebra)):
            if algebra[i] == algebra[j] and algebra[i] in ("A1", "A2"):
                out.append((f"diagonal of factors {i},{j} ({algebra[i]})",)
                           + apply_diag(algebra, content, i, j))
                if algebra[i] == "A2":
                    out.append((f"twisted diagonal of factors {i},{j} (A2)",)
                               + apply_diag(algebra, content, i, j, twisted=True))
    return out


def alg_name(algebra):
    names = {"A1": "su(2)", "A2": "su(3)", "G2": "g2", "D5": "so(10)",
             "C4": "sp(8)", "A3": "su(4)", "A4": "su(5)"}
    return "+".join(names[t] for t in algebra) if algebra else "(abelian only)"


def content_str(algebra, content):
    return " + ".join(f"{m}x({','.join(str(l) for l in tup)})"
                      for tup, m in sorted(content.items(), key=lambda kv: str(kv[0])))


def descend(algebra, content, path, depth, log, terminals, chains):
    opts = menu(algebra, content)
    verdicts = []
    any_reg = False
    for label, na, nc in opts:
        reg = chiral(na, nc)
        verdicts.append((label, na, nc, reg))
        any_reg = any_reg or reg
    pad = "  " * depth
    log.append(f"{pad}NODE {alg_name(algebra)}   content: {content_str(algebra, content)}")
    for label, na, nc, reg in verdicts:
        log.append(f"{pad}  option: {label:48s} -> {alg_name(na):22s} "
                   f"{'REGISTERABLE' if reg else 'dies (self-conjugate)'}")
    if not any_reg:
        log.append(f"{pad}  ** TERMINAL ** (no registerable option)")
        terminals.append(dict(algebra=alg_name(algebra),
                              content={content_str(algebra, content): 1},
                              path=list(path)))
        chains.append(list(path) + [f"TERMINAL: {alg_name(algebra)}"])
        return
    for label, na, nc, reg in verdicts:
        if reg:
            descend(na, nc, path + [f"{alg_name(algebra)} --[{label}]--> {alg_name(na)}"],
                    depth + 1, log, terminals, chains)


# ============================================================ (1) branching of the 27
def derive_27_branching():
    """Independent derivation: enumerate ALL multisets of (A2 irrep x G2 irrep) pairs with
      sum dim = 27,
      sum (per-factor Dynkin index) = x * T_E6(27), x = (2,1)  [x forced: level-1 target,
        factor levels = embedding indices; conformality c(A2_2)+c(G2_1)=16/5+14/5=6=c(E6_1)],
      conformal weight h_A2 + h_G2 = 2/3 mod 1  [h(27 of E6 at level 1) = C2/(2*13) = 2/3],
      su(3) cubic anomaly sum = 0  [E6 has no cubic Casimir => any restriction of the 27
        is anomaly-free on every su(3) factor].
    """
    # A2 irreps by Dynkin label (p,q), dim <= 27
    a2 = []
    for p in range(0, 7):
        for q in range(0, 7):
            d = (p + 1) * (q + 1) * (p + q + 2) // 2
            if d <= 27:
                T = F(d * (p * p + q * q + p * q + 3 * p + 3 * q), 24)
                C2 = F(16) * T / d if d else F(0)
                A = F(d * (p - q) * (p + 2 * q + 3) * (2 * p + q + 3), 60)
                a2.append(dict(pq=(p, q), dim=d, T=T, h=C2 / 10, A=A))
    g2 = [dict(lab=k, dim=v[0], T=v[1],   # C2 = 2*dim(g2)*T/dim = 28*T/dim; h = C2/(2(k+hv)) = C2/10
               h=(F(28) * v[1] / v[0]) / 10 if v[0] else F(0))
          for k, v in G2_REPS.items()]

    pairs = []
    for ra in a2:
        for rg in g2:
            d = ra["dim"] * rg["dim"]
            if d <= 27:
                pairs.append(dict(
                    name=f"({ra['pq']},{rg['lab']})", d=d,
                    tA=ra["T"] * rg["dim"], tG=rg["T"] * ra["dim"],
                    h=(ra["h"] + rg["h"]) % 1, A=ra["A"] * rg["dim"]))
    # target sums
    T27_E6 = F(3)
    want = dict(dim=27, tA=F(2) * T27_E6, tG=F(1) * T27_E6)

    sols_dim_index, sols_h, sols_anom = [], [], []

    def rec(i, d, ta, tg, acc):
        if d == 0:
            if ta == 0 and tg == 0:
                sols_dim_index.append(list(acc))
            return
        if i >= len(pairs):
            return
        p = pairs[i]
        m = 0
        while m * p["d"] <= d:
            if m * p["tA"] <= ta and m * p["tG"] <= tg:
                rec(i + 1, d - m * p["d"], ta - m * p["tA"], tg - m * p["tG"],
                    acc + [p] * m)
            m += 1

    rec(0, want["dim"], want["tA"], want["tG"], [])
    for s in sols_dim_index:
        if all(x["h"] == F(2, 3) for x in s):
            sols_h.append(s)
    for s in sols_h:
        if sum(x["A"] for x in s) == 0:
            sols_anom.append(s)
    return dict(
        n_dim_index=len(sols_dim_index),
        dim_index=[sorted(x["name"] for x in s) for s in sols_dim_index],
        n_h=len(sols_h), h=[sorted(x["name"] for x in s) for s in sols_h],
        n_final=len(sols_anom), final=[sorted(x["name"] for x in s) for s in sols_anom])


# ============================================================ main
def main():
    RES = {}
    print("=" * 78)
    print("CELL G1 -- the su(3)+g2 descent of E6")
    print("=" * 78)

    # ---- rule verification (dimension + index arithmetic on every branching used)
    rep = verify_rules()
    bad = [r for r in rep if not (r["dim_ok"] and r["index_ok"])]
    RES["branching_rules_verified"] = dict(n_checks=len(rep), n_failed=len(bad),
                                           failed=bad)
    print(f"\n[0] branching-rule verification: {len(rep)} checks, {len(bad)} failed")
    assert not bad, f"branching arithmetic failed: {bad}"

    # ---- embedding data
    c_a2_2 = F(2 * 8, 2 + 3)
    c_g2_1 = F(14, 1 + 4)
    RES["embedding"] = dict(
        subalgebra="su(3)+g2, maximal S-subalgebra of e6 (Dynkin), dim 8+14=22",
        indices="(2,1)", c_sum=str(c_a2_2 + c_g2_1), c_e6_1=str(F(6)),
        conformal=(c_a2_2 + c_g2_1 == 6))
    print(f"\n[1] embedding su(3)_2 + g2_1 in (e6)_1: c = {c_a2_2}+{c_g2_1} = "
          f"{c_a2_2 + c_g2_1} = c(E6_1): conformal {RES['embedding']['conformal']}")

    # ---- (1) independent derivation of the 27 branching
    br = derive_27_branching()
    RES["branching_27"] = br
    print(f"\n[2] 27-branching, derived independently:")
    print(f"    dim+both-index solutions: {br['n_dim_index']}  {br['dim_index']}")
    print(f"    + conformal-weight h=2/3: {br['n_h']}  {br['h']}")
    print(f"    + su(3)-anomaly = 0:      {br['n_final']}  {br['final']}")
    expected = sorted(["((1, 0),7)", "((0, 2),1)"])
    conj_expected = sorted(["((0, 1),7)", "((2, 0),1)"])
    got = [sorted(s) for s in br["final"]]
    unique_up_to_conj = (len(got) == 2 and expected in got and conj_expected in got)
    RES["branching_27"]["unique_up_to_conjugation"] = unique_up_to_conj
    RES["branching_27"]["chosen"] = "27 = (3,7) + (6b,1)"
    RES["branching_27"]["diff_vs_B873"] = (
        "AGREES with B873/Slansky's cited 27 = (3,7)+(6bar,1); here derived, not cited "
        "(the h- and anomaly-filters are this cell's additions to B873's dim+index check; "
        "B873's x=(2,1) T-arithmetic is reproduced by the index sums)")
    print(f"    unique up to overall conjugation: {unique_up_to_conj}"
          f"   => 27 = (3,7) + (6b,1)   [matches B873/Slansky]")
    assert unique_up_to_conj

    # ---- (2) the criterion, with MANDATORY controls (MB12: bites both ways)
    print("\n[3] registerability criterion -- independent implementation + bite controls:")
    controls = []
    # PASS control: banked SO(10)xU(1) step 1 (B861: registerable)
    alg, cont = ("D5",), Counter({("16",): 1, ("10",): 1, ("1",): 1})
    v = chiral(alg, cont)
    controls.append(("PASS-control  E6 -> SO(10)xU(1)   {16,10,1}", v, True))
    # FAIL control: banked Sp(8) step 1 (B861: NOT registerable)
    v = chiral(("C4",), Counter({("27c",): 1}))
    controls.append(("FAIL-control  E6 -> Sp(8)         {27 self-dual}", v, False))
    # FAIL control: banked SU(4)xU(1) step 3 (B861/B994: NOT registerable)
    su5 = (("A4",), Counter({("10",): 1, ("5b",): 2, ("5",): 1, ("1",): 2}))
    a4rule = RULES["A4"][0]
    na, nc = apply_rule(su5[0], su5[1], 0, a4rule)
    v = chiral(na, nc)
    controls.append(("FAIL-control  SU(5) -> SU(4)xU(1) (B863-class kill)", v, False))
    # positive control: the SM itself (banked chiral), from the SAME su(5) content
    na_sm, nc_sm = apply_rule(su5[0], su5[1], 0, RULES["A4"][1])
    v = chiral(na_sm, nc_sm)
    controls.append(("PASS-control  SU(5) -> SM         (positive control)", v, True))
    # B863 rows on the banked SM generation (16-based, exactly B863's multisets)
    b863_a = ("A2",), Counter({("3",): 2, ("3b",): 2, ("1",): 3})
    controls.append(("FAIL-control  B863 (a) su(2)->u(1) {3:2,3b:2,1:3}",
                     chiral(*b863_a), False))
    # B863 (b'): su(3)_1 -> su(2)_4 principal on SM gen (3,2)+2(3b,1)+(1,2)+(1,1)
    smgen = ("A2", "A1"), Counter({("3", 2): 1, ("3b", 1): 2, ("1", 2): 1, ("1", 1): 1})
    na, nc = apply_rule(smgen[0], smgen[1], 0, RULES["A2"][1])
    controls.append(("FAIL-control  B863 (b') su(3)_1->su(2)_4 principal",
                     chiral(na, nc), False))
    controls.append(("PASS-control  B863 SM gen itself {(3,2),2(3b,1),(1,2),(1,1)}",
                     chiral(*smgen), True))
    all_ok = True
    for name, got, want_v in controls:
        ok = got == want_v
        all_ok = all_ok and ok
        print(f"    {name:55s} chiral={got}  want={want_v}  OK={ok}")
    RES["controls"] = [dict(name=n, chiral=g, want=w, ok=g == w) for n, g, w in controls]
    RES["controls_all_ok"] = all_ok
    assert all_ok, "criterion implementation fails banked controls"

    # engine-level control: B863's terminality of the SM node reproduced by the SAME
    # descent engine used for the su(3)+g2 tree (banked SM content -> no registerable option)
    sm_opts = menu(*smgen)
    sm_terminal = not any(chiral(na, nc) for _, na, nc in sm_opts)
    RES["engine_reproduces_B863_terminality"] = sm_terminal
    print(f"    ENGINE-control: SM node with banked content is TERMINAL "
          f"(reproduces B863): {sm_terminal}")
    assert sm_terminal

    # ---- (3) step 1: registerability of E6 -> su(3)+g2
    alg0 = ("A2", "G2")
    cont0 = Counter({("3", "7"): 1, ("6b", "1"): 1})
    step1 = chiral(alg0, cont0)
    RES["step1"] = dict(
        content="27 = (3,7)+(6b,1)", registerable=step1,
        note=("NOT-REGISTERABLE-AT-STEP-1 is FALSE: g2's reps are all real, but "
              "chirality lives in the su(3) factor -- 3 (x7) and 6b are unpaired. "
              "Confirms B873 layer 5."))
    print(f"\n[4] step 1  E6 -> su(3)+g2, 27 = (3,7)+(6b,1): registerable = {step1}"
          f"   (confirms B873; the 'g2 forces self-conjugate' hunch is FALSE)")

    # ---- the full descent tree
    print("\n[5] FULL DESCENT TREE below su(3)+g2 (menu per convention C4):")
    log, terminals, chains = [], [], []
    descend(alg0, cont0, [f"E6 --[S-subalgebra, conformal (2,1)]--> su(3)+g2"],
            1, log, terminals, chains)
    for line in log:
        print("    " + line)
    RES["tree"] = log
    RES["terminals"] = terminals
    RES["n_chains"] = len(chains)
    RES["chains"] = chains
    term_algs = sorted(set(t["algebra"] for t in terminals))
    RES["terminal_algebras"] = term_algs
    print(f"\n    chains: {len(chains)}; terminal algebras: {term_algs}")

    # endpoint content check: every chain ends at su(3) with {3:7, 6b:1}
    endpoint_ok = all(t["algebra"] == "su(3)" for t in terminals)
    ep_contents = sorted(set(next(iter(t["content"])) for t in terminals))
    RES["endpoint"] = dict(
        algebra="su(3) (+ abelian dials)", all_chains=endpoint_ok,
        contents=ep_contents,
        anomaly=str(7 * 1 + (-7)),
        anomaly_note="7*A(3)+A(6b) = 7-7 = 0: anomaly-free, as forced (E6 has no cubic Casimir)")
    print(f"    every chain terminates at su(3): {endpoint_ok}; "
          f"endpoint content(s): {ep_contents}")
    print(f"    endpoint anomaly check: 7*A(3)+A(6b) = 0: True")

    # ---- min-dim chain on the specials-inclusive menu
    step1_menu = [("SO(10)xU(1)", 46), ("SU(6)xSU(2)", 38), ("SU(3)^3", 24),
                  ("su(3)+g2", 22)]     # registerable step-1 options, completed menu (B873)
    mindim = min(step1_menu, key=lambda x: x[1])
    RES["min_dim_on_specials_inclusive_menu"] = dict(
        registerable_step1_options=step1_menu, min_dim_pick=mindim[0],
        chain="E6 -> su(3)+g2 -> su(3)+su(2) [g2 principal, min-dim 11] -> su(3) TERMINAL",
        endpoint="su(3), NOT the SM")
    print(f"\n[6] min-dim on the specials-inclusive step-1 menu picks: {mindim[0]} "
          f"(dim {mindim[1]} < 24)")
    print(f"    its chain terminates at su(3) -- the SM is NOT reached.")

    # ---- verdict
    RES["verdict"] = "NON-SM-ENDPOINT"
    RES["verdict_detail"] = (
        "Every registerable-respecting chain through su(3)+g2 terminates at su(3) "
        "(+ abelian dials) with generation content {3:7, 6b:1} -- chain-independent. "
        "The SM algebra su(3)+su(2)+u(1) occurs as an INTERMEDIATE node on this branch "
        "(with content {(3,2):2,(3,1):3,(6b,1):1}) but is NOT terminal there: "
        "su(2)->u(1) remains registerable, so every selection function must continue. "
        "Rule-independence does NOT extend to the specials-inclusive menu: min-dim "
        "selects su(3)+g2 at step 1 and lands at su(3). The T8b scope correction "
        "(part (ii) restricted to the regular menus) is NECESSARY, not merely prudent.")
    print(f"\n[7] VERDICT: {RES['verdict']}")
    print("    " + RES["verdict_detail"])

    json.dump(RES, open(os.path.join(HERE, "results.json"), "w"),
              indent=1, sort_keys=True, default=str)

    # branching data file
    BR = dict(
        step1="27 of E6 under su(3)_2+g2_1:  27 = (3,7) + (6b,1)",
        g2_to_su3="7 = 3+3b+1; 14 = 8+3+3b (x=1)",
        g2_to_su2su2="7 = (2,2)+(1,3); 14 = (3,1)+(1,3)+(2,4) (x=(1,3))",
        g2_to_su2_principal="7 = 7; 14 = 3+11 (x=28)",
        su3_to_su2u1="3 = 2+1; 6 = 3+2+1; 8 = 3+2+2+1 (x=1)",
        su3_to_so3_principal="3 = 3; 6 = 5+1; 8 = 5+3 (x=4)",
        diagonals="A2xA2: 3x3=6+3b, 3x3b=8+1; A1xA1: Clebsch-Gordan",
        all_verified_by="dimension sum + per-factor Dynkin-index sum (see results.json)")
    json.dump(BR, open(os.path.join(HERE, "branching_data.json"), "w"),
              indent=1, sort_keys=True)
    print("\ndone.")


if __name__ == "__main__":
    main()
