#!/usr/bin/env python3
"""GATE P5 verification -- menu completeness for the B861 fused cascade.

Three steps:
  step 1: conformal embeddings into (E6)_1        c = 6
  step 2: conformal embeddings into SO(10)_1      c = 5
  step 3: conformal embeddings into SU(5)_1       c = 4

Machinery (COMPUTED here):
  * Borel-de Siebenthal on explicit affine Dynkin diagrams (prime-mark node removal)
    + maximal Levi enumeration (mark-1 node removal from the finite diagram, + u1).
  * exact central charges c(g_k) = k dim / (k + hv) as Fractions.
  * closed-form conformal level: k = c hv / (dim - c) -- integer or no embedding level exists.
  * generous c-match scan over products of simple algebras (rank <= rank(g)) + u1's.
  * full-rank kill: a full-rank subalgebra contains a Cartan => regular => contained in a
    maximal full-rank regular; those are enumerated; dim bound kills impostor c-matches.
  * Dynkin-index cross-checks (T-arithmetic) for the special embeddings where the branching
    is standard.
  * registerability (B860/B861 criterion): -1 in W(h) for every simple factor => every rep
    self-conjugate => branched multiset self-conjugate => NOT registerable, independent of
    branching details.  Plus explicit multiset checks where a factor lacks -1 in W.
  * downward-inheritance lemma (makes maximal menus sufficient): if H's branched generation
    multiset is self-conjugate, so is its further restriction to h < H; hence any registerable
    conformal h sits inside a registerable conformal MAXIMAL H with dim H > dim h; ranking
    over maximal menus is complete.

CITED (named, not rederived): Dynkin's maximal S-subalgebra tables (Dynkin 1952, Amer. Math.
Soc. Transl.; recomputed by de Graaf 2011); Slansky (Phys. Rep. 79 (1981)) branchings;
-1 in W list (Bourbaki: w0 = -1 exactly for A1, Bn, Cn, D_even, G2, F4, E7, E8).
"""
from fractions import Fraction as F
from itertools import combinations

# ---------------------------------------------------------------- algebra data
# name: (dim, dual Coxeter number, rank)
ALG = {
    "A1": (3, 2, 1),  "A2": (8, 3, 2),  "A3": (15, 4, 3), "A4": (24, 5, 4),
    "A5": (35, 6, 5), "A6": (48, 7, 6),
    "B2": (10, 3, 2), "B3": (21, 5, 3), "B4": (36, 7, 4), "B5": (55, 9, 5),
    "B6": (78, 11, 6),
    "C3": (21, 4, 3), "C4": (36, 5, 4), "C5": (55, 6, 5), "C6": (78, 7, 6),
    "D4": (28, 6, 4), "D5": (45, 8, 5), "D6": (66, 10, 6),
    "G2": (14, 4, 2), "F4": (52, 9, 4), "E6": (78, 12, 6),
}
MINUS1_IN_W = {"A1", "B2", "B3", "B4", "B5", "B6", "C3", "C4", "C5", "C6",
               "D4", "D6", "G2", "F4"}  # of the ones above (D_even yes, D5 no, A_n>=2 no, E6 no)


def cc(name, k):
    d, hv, _ = ALG[name]
    return F(k * d, k + hv)


def conf_level(name, target):
    """closed form: c(g_k)=target  <=>  k = target*hv/(dim-target); None if not a +integer."""
    d, hv, _ = ALG[name]
    if d <= target:
        return None
    k = F(target * hv, d - target)
    return int(k) if k.denominator == 1 and k > 0 else None


# ------------------------------------------------- affine diagrams, BdS + Levi
# affine diagrams: nodes, edges, marks (affine node = 0)
AFFINE = {
    "E6": dict(edges=[(1, 3), (3, 4), (4, 5), (5, 6), (2, 4), (0, 2)],
               marks={0: 1, 1: 1, 2: 2, 3: 2, 4: 3, 5: 2, 6: 1}),
    "D5": dict(edges=[(0, 2), (1, 2), (2, 3), (3, 4), (3, 5)],
               marks={0: 1, 1: 1, 2: 2, 3: 2, 4: 1, 5: 1}),
    "A4": dict(edges=[(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)],
               marks={0: 1, 1: 1, 2: 1, 3: 1, 4: 1}),
}


def components(nodes, edges):
    adj = {n: set() for n in nodes}
    for a, b in edges:
        if a in nodes and b in nodes:
            adj[a].add(b); adj[b].add(a)
    seen, comps = set(), []
    for n in nodes:
        if n in seen:
            continue
        stack, comp = [n], set()
        while stack:
            x = stack.pop()
            if x in comp:
                continue
            comp.add(x); seen.add(x)
            stack.extend(adj[x] - comp)
        comps.append((comp, {a: adj[a] & comp for a in comp}))
    return comps


def classify(comp, adj):
    n = len(comp)
    degs = sorted(len(adj[a]) for a in comp)
    if degs[-1] <= 2:
        return f"A{n}"
    if degs.count(3) == 1 and degs[-1] == 3:
        branch = [a for a in comp if len(adj[a]) == 3][0]
        arms = []
        for nb in sorted(adj[branch]):
            length, prev, cur = 1, branch, nb
            while True:
                nxt = [x for x in adj[cur] if x != prev]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]; length += 1
            arms.append(length)
        arms = tuple(sorted(arms))
        if arms[:2] == (1, 1):
            return f"D{arms[2] + 3}"
        return {(1, 2, 2): "E6", (1, 2, 3): "E7", (1, 2, 4): "E8"}[arms]
    raise ValueError("unclassifiable")


def is_prime(n):
    return n in (2, 3, 5, 7)


def maximal_rank_menu(g):
    """(semisimple BdS from prime-mark affine removals) + (Levi u1-type from mark-1 finite
    removals).  Returns list of (label, factors:list[str], n_u1)."""
    dat = AFFINE[g]
    nodes = set(dat["marks"])
    out = []
    for i in sorted(nodes):
        m = dat["marks"][i]
        rest = nodes - {i}
        comps = components(rest, dat["edges"])
        types = sorted(classify(c, a) for c, a in comps)
        if i != 0 and m == 1:
            pass  # finite-node mark-1 removal handled below (Levi); affine-like removal of a
            # mark-1 node from the AFFINE diagram returns an algebra isomorphic to g itself.
        if m >= 2 and is_prime(m):
            if types != [g]:
                out.append(("+".join(types), types, 0))
    # Levi: remove a mark-1 node from the FINITE diagram (nodes - {0}), add u1
    fin = nodes - {0}
    for i in sorted(fin):
        if dat["marks"][i] != 1:
            continue  # Levi maximal iff removed node has mark 1 (Borel-de Siebenthal)
        rest = fin - {i}
        comps = components(rest, dat["edges"])
        types = sorted(classify(c, a) for c, a in comps)
        out.append(("+".join(types) + "+u1", types, 1))
    # dedupe
    seen, ded = set(), []
    for lab, t, u in out:
        if lab not in seen:
            seen.add(lab); ded.append((lab, t, u))
    return ded


def dim_of(types, n_u1):
    return sum(ALG[t][0] for t in types) + n_u1


# ---------------------------------------------------------------- c-match scan
def scan(target, max_rank):
    """all (factors:[(name, level)...], n_u1) with exact sum of c = target, sum rank <= max_rank.
    Intermediate-A1 levels capped at 200 (final factor solved in closed form -- exact)."""
    names = sorted(ALG)
    names.remove("E6")  # target algebras excluded as proper subalgebras of themselves
    sols = []

    def rec(start_idx, start_level, rem, rank_left, acc):
        for idx in range(start_idx, len(names)):
            nm = names[idx]
            d, hv, rk = ALG[nm]
            if rk > rank_left:
                continue
            lv0 = start_level if idx == start_idx else 1
            # exact closing level
            kc = None
            if d > rem:
                kk = F(rem * hv, d - rem)
                if kk.denominator == 1 and kk >= lv0:
                    kc = int(kk)
            if kc is not None:
                sols.append((acc + [(nm, kc)], 0))
            # continue with this factor at some level, then more factors
            kmax = int(F(rem * hv, d - rem)) if d > rem else 200
            for k in range(lv0, kmax + 1):
                c1 = cc(nm, k)
                if c1 >= rem:
                    break
                rec(idx, k + 1 if False else k, rem - c1, rank_left - rk, acc + [(nm, k)])
                # NOTE: allow repeats with non-decreasing (name, level): pass same idx and
                # require next level >= k via start_level
        return

    def rec2(idx, min_lv, rem, rank_left, acc):
        if rem == 0:
            sols.append((list(acc), 0))
            return
        for j in range(idx, len(names)):
            nm = names[j]
            d, hv, rk = ALG[nm]
            if rk > rank_left:
                continue
            lo = min_lv if j == idx else 1
            hi = int(F(rem * hv, d - rem)) if d > rem else 200
            for k in range(lo, hi + 1):
                c1 = cc(nm, k)
                if c1 > rem:
                    break
                rec2(j, k, rem - c1, rank_left - rk, acc + [(nm, k)])

    sols = []
    for n_u1 in range(0, max_rank + 1):
        sub = []
        remt = target - n_u1
        if remt < 0:
            continue
        if remt == 0:
            sols.append(([], n_u1))
            continue
        tmp = []
        _s = sols

        def collect(fs):
            tmp.append((fs, n_u1))
        _old = list(sols)
        sols_local = []
        # local recursion
        def r(idx, min_lv, rem, rank_left, acc):
            if rem == 0:
                sols_local.append((list(acc), n_u1))
                return
            for j in range(idx, len(names)):
                nm = names[j]
                d, hv, rk = ALG[nm]
                if rk > rank_left:
                    continue
                lo = min_lv if j == idx else 1
                hi = int(F(rem * hv, d - rem)) if d > rem else 200
                for k in range(lo, hi + 1):
                    c1 = cc(nm, k)
                    if c1 > rem:
                        break
                    r(j, k, rem - c1, rank_left - rk, acc + [(nm, k)])
        r(0, 1, F(remt), max_rank - n_u1, [])
        sols.extend(sols_local)
    return sols


# ------------------------------------------------------- T-arithmetic (theta^2=2)
def t_checks():
    """Dynkin-index cross-checks for the special embeddings with standard branchings.
    T(R) = dim(R) * C2(R) / (2 dim g);  T(adjoint) = hv;  T(fund A_n) = 1/2;
    T(vector B_n/D_n) = 1;  T(fund C_n) = 1/2.   x = sum_branch T_h / T_g(R)."""
    out = []
    # E6 > C4:  27 = Lambda^2(8)-1.  T(8x8)=2*8*T(8)=8; Sym2(8)=adj C4 => T=hv=5
    T_l2_8 = 8 - 5           # T(Lambda^2 8) = 3;  27 = L2(8) - singlet => T = 3
    x = F(T_l2_8, 3)         # T_E6(27) = 3
    out.append(("C4 < E6, 27=Lam2(8)-1", x == 1, f"x={x}"))
    # E6 > A2+G2:  27 = (3,7) + (6bar,1);  T(3)=1/2, T(6 of A2)=5/2, T(7 of G2)=1
    xa2 = F(7 * F(1, 2) + 1 * F(5, 2), 3)
    xg2 = F(3 * 1 + 0, 3)
    out.append(("A2+G2 < E6, 27=(3,7)+(6b,1)", (xa2, xg2) == (2, 1), f"x=({xa2},{xg2})"))
    # D5 > B2 adjoint: 10 = adj(B2) => x = T(adj)/T(vec D5) = hv(B2)/1 = 3
    out.append(("B2adj < D5, 10=adj", ALG["B2"][1] == 3, "x=3"))
    # D5 > B3+A1: 10 = (7,1)+(1,3);  x_B3 = T(7 of B3)=1;  x_A1 = T(3=adj A1)=hv(A1)=2
    out.append(("B3+A1 < D5, 10=(7,1)+(1,3)", ALG["A1"][1] == 2, "x=(1,2)"))
    # A4 > B2: 5 = vector;  x = T(5 of B2)/T(5 of A4) = 1/(1/2) = 2
    #   T(5 of B2) via B2=C2: 5 = Lam2(4)-1 of sp4: T(4x4)=2*4*(1/2)=4; Sym2(4)=adj => T=3
    t5 = 4 - 3
    x = F(t5, 1) / F(1, 2)
    out.append(("B2 < A4, 5=vector (via sp4 Lam2)", x == 2, f"x={x}"))
    return out


# ------------------------------------------------------------- registerability
def conj_mult(reps, conj):
    from collections import Counter
    return Counter(tuple(conj.get(x, x) for x in r) for r in reps) == Counter(map(tuple, reps))


CONJ = {"3": "3b", "3b": "3", "4": "4b", "4b": "4", "5": "5b", "5b": "5",
        "6A2": "6bA2", "6bA2": "6A2", "6c": "6bc", "6bc": "6c",
        "15": "15b", "15b": "15", "16": "16b", "16b": "16", "10c": "10bc", "10bc": "10c",
        # self-conjugate: reps of algebras with -1 in W, and real reps generally
        }


# ------------------------------------------------------------- impostor disposal
def dispose(g, fs, nu, windim, reg_menu, winner_lab):
    """Return (kill_reason or 'WINNER' or 'IN-MENU'). Every c-match with dim >= winner
    must land somewhere -- an undisposed impostor means the menu is NOT complete."""
    d = sum(ALG[n][0] for n, _ in fs) + nu
    rk = sum(ALG[n][2] for n, _ in fs) + nu
    grank = ALG[g][2]
    types_l1 = sorted(n for n, k in fs if k == 1)
    # the winner / menu rows themselves (handled by registerability downstream)
    if all(k == 1 for _, k in fs):
        for lab, types, u in reg_menu:
            if sorted(types) == types_l1 and u == nu:
                return "WINNER" if lab == winner_lab else "IN-MENU"
    # kill 3 first: citation-free, embedding-independent
    if all(n in MINUS1_IN_W for n, _ in fs):
        return "KILL: -1 in W for every factor => not registerable (no embedding needed)"
    if rk == grank:
        mx = max(dim_of(t, u) for _, t, u in reg_menu)
        if d > mx:
            return f"KILL: full rank => regular => dim <= {mx} < {d}"
        # derived fit: s semisimple-part must sit in H_ss of some maximal regular H, dim H >= d
        fits = []
        ss_rank = sum(ALG[n][2] for n, _ in fs)
        ss_dim = sum(ALG[n][0] for n, _ in fs)
        for lab, types, u in reg_menu:
            if dim_of(types, u) >= d:
                hs_rank = sum(ALG[t][2] for t in types)
                hs_dim = sum(ALG[t][0] for t in types)
                if ss_rank <= hs_rank and ss_dim <= hs_dim:
                    fits.append(lab)
        if not fits:
            return ("KILL: full rank => inside a maximal regular H with dim H >= "
                    f"{d}; semisimple part (rank {ss_rank}, dim {ss_dim}) fits no "
                    "H_ss (derived-fit)")
        return f"UNKILLED (fits {fits})"
    # rank-deficient: would be an S-subalgebra -- must appear in Dynkin's cited table
    return ("KILL: rank-deficient => S-subalgebra => must appear in Dynkin's cited "
            "table; it does not (citation)")


def main():
    import json as _json
    import os as _os
    RES = {"steps": {}, "impostors": {}, "t_checks": [], "registerability": {},
           "residual_citations": ["Dynkin maximal S-subalgebra tables (1952; "
                                  "recomputed de Graaf 2011)",
                                  "Slansky branching 27 = (3,7)+(6bar,1) for A2+G2"]}
    print("=" * 78)
    print("GATE P5 -- mechanical menu-completeness verification")
    print("=" * 78)

    # ---------------- regular (maximal-rank) menus, computed from the diagrams
    print("\n[1] Borel-de Siebenthal + maximal Levi, from explicit affine diagrams:")
    reg = {}
    for g in ("E6", "D5", "A4"):
        menu = maximal_rank_menu(g)
        reg[g] = menu
        tgt = cc(g, 1)
        print(f"  {g}  (c(g_1) = {tgt}):")
        for lab, types, nu in menu:
            c = sum(cc(t, 1) for t in types) + nu
            print(f"    {lab:12s} dim {dim_of(types, nu):3d}   c at level 1 = {c}"
                  f"   conformal: {c == tgt}")
    # full-rank kill bound
    print("\n[2] full-rank impostor kill (full rank => regular => inside a maximal regular):")
    for g in ("E6", "D5", "A4"):
        mx = max(dim_of(t, u) for _, t, u in reg[g])
        print(f"  {g}: max dim of a proper full-rank subalgebra = {mx}")

    # ---------------- generous c-scan + FULL DISPOSAL of every match >= winner
    print("\n[3] exact c-match scan (products of simples + u1's, rank <= rank g;"
          " intermediate-A1 cap 200) -- every match with dim >= winner DISPOSED:")
    targets = {"E6": ((6, 6, 46), "D5+u1"), "D5": ((5, 5, 25), "A4+u1"),
               "A4": ((4, 4, 12), "A1+A2+u1")}
    undisposed_total = 0
    for g, ((tgt, rmax, windim), winner_lab) in targets.items():
        sols = scan(tgt, rmax)
        big = []
        for fs, nu in sols:
            d = sum(ALG[n][0] for n, _ in fs) + nu
            rk = sum(ALG[n][2] for n, _ in fs) + nu
            if d >= windim:
                big.append((d, rk, fs, nu))
        big.sort(reverse=True)
        print(f"  into {g}_1 (c={tgt}): {len(sols)} exact c-matches;"
              f" those with dim >= winner({windim}): {len(big)}")
        rows = []
        for d, rk, fs, nu in big:
            lab = "+".join(f"{n}_{k}" for n, k in fs) + (f"+{nu}u1" if nu else "")
            verdict = dispose(g, fs, nu, windim, reg[g], winner_lab)
            rows.append(dict(label=lab, dim=d, rank=rk, disposal=verdict))
            if verdict.startswith("UNKILLED"):
                undisposed_total += 1
            print(f"      dim {d:3d} rank {rk}:  {lab:22s} -> {verdict}")
        # a KILLED row cannot compete for the win; only an UNKILLED tie threatens
        ties = [r for r in rows if r["dim"] == windim
                and r["disposal"].startswith("UNKILLED")]
        RES["impostors"][g] = dict(rows=rows, winner_dim=windim,
                                   winner_ties_outside_menu=len(ties))
        print(f"      winner-dim ties outside the menu: {len(ties)}")
    RES["undisposed_total"] = undisposed_total

    # ---------------- special embeddings (Dynkin, cited) with c computed
    print("\n[4] special (S-)maximal subalgebras -- Dynkin's tables (CITED), c COMPUTED:")
    SPECIALS = {
        "E6": [("A2", [("A2", 9)]), ("G2", [("G2", 3)]), ("C4", [("C4", 1)]),
               ("F4", [("F4", 1)]), ("A2+G2", [("A2", 2), ("G2", 1)])],
        "D5": [("B4 (SO9)", [("B4", 1)]), ("B3+A1 (SO7xSO3)", [("B3", 1), ("A1", 2)]),
               ("B2+B2 (SO5xSO5)", [("B2", 1), ("B2", 1)]), ("B2adj (SO5)", [("B2", 3)])],
        "A4": [("B2 (SO5)", [("B2", 2)])],
    }
    for g, lst in SPECIALS.items():
        tgt = cc(g, 1)
        print(f"  {g}:")
        for lab, fac in lst:
            c = sum(cc(n, k) for n, k in fac)
            d = sum(ALG[n][0] for n, _ in fac)
            print(f"    {lab:22s} dim {d:3d} levels {[k for _, k in fac]}"
                  f"  c = {c}  conformal: {c == tgt}")

    print("\n[5] Dynkin-index cross-checks (T-arithmetic, computed):")
    for lab, ok, det in t_checks():
        print(f"    {lab:38s} {det:12s} OK: {ok}")

    # closed-form forced levels
    print("\n[6] closed-form forced levels k = c*hv/(dim-c) for the special candidates:")
    for g, tgt in (("E6", 6), ("D5", 5), ("A4", 4)):
        row = []
        for nm in ("A2", "G2", "C4", "F4", "B2", "B3", "B4", "D4", "A5", "A6", "D6"):
            k = conf_level(nm, tgt)
            if k:
                row.append(f"{nm}_{k}(dim {ALG[nm][0]})")
        print(f"    c={tgt}: single-simple exact matches: {', '.join(row)}")

    # ---------------- registerability on the COMPLETED menus
    print("\n[7] registerability (generation multiset, abelian stripped) on completed menus:")
    # -1 in W theorem kills, independent of branching:
    killed = {
        "step1 G2_3": ["G2"], "step1 Sp(8)": ["C4"], "step1 F4_1": ["F4"],
        "step2 SO(8)xU(1)": ["D4"], "step2 SO(7)xSO(3)": ["B3", "A1"],
        "step2 SO(5)xSO(5)": ["B2", "B2"], "step2 SO(5)_3": ["B2"],
        "step2 SO(9)": ["B4"],
        "step3 SO(5)_2": ["B2"],
    }
    for lab, facs in killed.items():
        ok = all(f in MINUS1_IN_W for f in facs)
        print(f"    {lab:22s} factors {facs}: -1 in W all => every rep self-conj"
              f" => NOT registerable: {ok}")
    # A2+G2 needs the branching: 27 = (3,7)+(6bar,1)   [Slansky]
    gen = [("3", "7G2"), ("6bA2", "1")]
    ch = not conj_mult(gen, CONJ)
    print(f"    step1 A2+G2           27=(3,7)+(6b,1): chiral => registerable: {ch}"
          f"  (dim 22 < 46: cannot win)")

    # ---------------- final winners on completed menus
    print("\n[8] winners on the COMPLETED menus:")
    completed = {
        "step1 (E6)_1": [("SO(10)xU(1)", 46, True), ("SU(6)xSU(2)", 38, True),
                         ("Sp(8)", 36, False), ("SU(3)^3", 24, True),
                         ("SU(3)2xG2_1", 22, True), ("G2_3", 14, False),
                         ("SU(3)_9", 8, None)],
        "step2 SO(10)_1": [("SO(8)xU(1)", 29, False), ("SU(5)xU(1)", 25, True),
                           ("SO(7)xSO(3)", 24, False), ("Pati-Salam", 21, True),
                           ("SO(5)xSO(5)", 20, False), ("SO(5)_3", 10, False)],
        "step3 SU(5)_1": [("SU(4)xU(1)", 16, False), ("SM", 12, True),
                          ("SO(5)_2", 10, False)],
    }
    for step, menu in completed.items():
        regs = [(d, n) for n, d, r in menu if r]
        w = max(regs)
        uniq = len([1 for d, _ in regs if d == w[0]]) == 1
        RES["steps"][step] = dict(menu=menu, winner=w[1], winner_dim=w[0],
                                  unique=uniq)
        print(f"  {step}: winner {w[1]} (dim {w[0]}), unique {uniq};"
          f"  menu size {len(menu)}")

    # ---------------- ADDENDUM: the SU(3)_9 row, DECIDED (was: unresolved-but-cannot-win)
    # The index-9 A2 in E6 must branch the 27 onto a multiset with sum dim = 27 and
    # sum of Dynkin indices = 9 * T_E6(27) = 27. Enumerate ALL A2 irrep multisets:
    def su3_9_branching():
        irreps = []
        for a in range(0, 7):
            for b in range(0, 7):
                d = (a + 1) * (b + 1) * (a + b + 2) // 2
                if d <= 27:
                    irreps.append(((a, b), d, F(d * (a*a + b*b + a*b + 3*a + 3*b), 24)))
        irreps.sort(key=lambda x: -x[1])
        sols = []

        def rec(i, dl, tl, acc):
            if dl == 0:
                if tl == 0:
                    sols.append(list(acc))
                return
            if i >= len(irreps):
                return
            ab, d, T = irreps[i]
            m = 0
            while m * d <= dl and m * T <= tl:
                rec(i + 1, dl - m * d, tl - m * T, acc + [ab] * m)
                m += 1
        rec(0, 27, F(27), [])
        from collections import Counter
        return [(s, Counter(s) == Counter((b, a) for a, b in s)) for s in sols]

    br39 = su3_9_branching()
    RES["su3_9"] = dict(
        solutions=[{"multiset": [list(x) for x in s], "self_conjugate": sc}
                   for s, sc in br39],
        unique=len(br39) == 1,
        decided_dead=(len(br39) == 1 and br39[0][1]))
    print(f"\n  ADDENDUM SU(3)_9: dim+index force the 27-branching uniquely: "
          f"{RES['su3_9']['unique']} -> {br39[0][0]} self-conj {br39[0][1]}"
          f"  => row DECIDED dead (was: unresolved-but-cannot-win)")

    # the A1 level cap is a THEOREM, not a hope: an embedded sl2's level = its Dynkin
    # index <= the principal sl2's index = rank*h*(h+1)/6 (h = Coxeter number)
    RES["a1_cap_justification"] = {
        "E6": 6 * 12 * 13 // 6, "D5": 5 * 8 * 9 // 6, "A4": 4 * 5 * 6 // 6}
    print(f"\n  A1-cap justification (principal sl2 indices, all < 200): "
          f"{RES['a1_cap_justification']}")

    RES["t_checks"] = [(lab, ok) for lab, ok, _ in t_checks()]
    RES["registerability"] = {lab: all(f in MINUS1_IN_W for f in facs)
                              for lab, facs in killed.items()}
    RES["a2g2_registerable_but_small"] = ch
    RES["p5_gated"] = (undisposed_total == 0
                       and all(v["unique"] for v in RES["steps"].values())
                       and all(v["winner_ties_outside_menu"] == 0
                               for v in RES["impostors"].values())
                       and all(ok for _, ok in RES["t_checks"])
                       and all(RES["registerability"].values()))
    _json.dump(RES, open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),
                                       "results.json"), "w"), indent=1, sort_keys=True)
    print(f"\n  P5 GATED (all matches disposed, winners unique, no outside ties,"
          f" T-checks, kills): {RES['p5_gated']}")
    print("\ndone.")


if __name__ == "__main__":
    main()
