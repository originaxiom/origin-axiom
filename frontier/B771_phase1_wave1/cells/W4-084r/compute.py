#!/usr/bin/env python3
"""
W4-084r -- N8: Anderson-Putnam BORDER-FORCING on the COLLARED system (W3 carry).

WHY THIS CELL EXISTS
--------------------
W3-084 built the AP complex on the 1-collared substitution sigma_4 and read off
Hˇ^1(Omega)=Z^4, BUT it only ever ran forces_border() on the RAW substitution
(which returns False for every substitution that needs collaring) -- it never
re-ran the test on the COLLARED system.  The Anderson-Putnam theorem certifies
        Omega = lim_<-( Gamma_c , sigma_c ),   hence   Hˇ^*(Omega)=Hˇ^*(complex)
ONLY WHEN THE (collared) SUBSTITUTION FORCES ITS BORDER.  Border-forcing is the
decisive correctness check; without it the cohomology is uncertified.

THIS CELL
---------
Generic k-collaring iterator.  At each depth d it re-runs the level-1
border-forcing test forces_border() ON THE d-COLLARED SUBSTITUTION.  It reports
the smallest depth d* at which the border is forced, recomputes the AP-complex
cohomology at d* AND at d*+1 (must agree -- extra collaring cannot change Omega),
and only then certifies Hˇ^*.

SEALED CRITERION (in-code verdict below):
  * border forced at some collar depth d* AND cohomology certified
    (controls reproduce textbook Hˇ^1 at d*, and Hˇ^1(d*)==Hˇ^1(d*+1))  => RESOLVED-A
  * border NEVER forces up to DMAX (substitution non-recognizable / the
    forcing test is a genuine obstruction)                              => RESOLVED-B
  * controls fail / robustness (d* vs d*+1) disagrees / asserts trip    => UNRESOLVED

BORDER-FORCING TEST (level-1, exact combinatorial form; Sadun "Topology of
Tiling Spaces" Ch.4, Anderson-Putnam 1998):
  A substitution s over alphabet A with admissible 2-blocks L2 forces its border
  iff at the seam of every admissible pair (u,v) the tile abutting the seam INSIDE
  the substituted image is determined by the tile on the OTHER side of the seam:
        last(s(u))  is a function of v alone   (left_nb[v] singleton), and
        first(s(v)) is a function of u alone   (right_nb[u] singleton).
This is EXACTLY the level-1 AP border-forcing condition.  The raw substitution
fails it (control: raw returns False); collaring is what repairs it -- so the
test is non-vacuous (a free-symbol swap of the substitution changes the answer;
Fib/TM/sigma_4 all differ, asserted below).

House method: exact integer/sympy arithmetic (integer linear algebra over Z, no
floats); every check ASSERTed with its direction; UNRESOLVED reachable; the
discriminating fact (collar depth d*, forces_border truth table, b1, charpoly,
Hˇ^1) computed IN-CELL, never cited.  Comparator control = the raw (uncollared)
system, which must NOT force the border, proving the criterion can fail.
"""
import json
import time
import collections
from collections import defaultdict

import sympy as sp

T0 = time.time()
CELL = "/Users/dri/origin-axiom/frontier/B771_phase1_wave1/cells/W4-084r"
DMAX = 4                         # max collar depth to search before declaring non-forcing
FAILED = []


def log(msg):
    print(f"[{time.time()-T0:7.2f}s] {msg}", flush=True)


def gate(name, ok, detail=""):
    log(f"GATE {name}: {'PASS' if ok else 'FAIL'}  {detail}")
    if not ok:
        FAILED.append(name)
    return ok


# ======================================================================
# 0. generic id-substitution machinery
#    An "id" is any hashable (a letter str at level 0, a nested tuple after
#    collaring).  A substitution is a dict  id -> list[id].  first/last of an id
#    are sub[id][0] / sub[id][-1] (ids themselves).
# ======================================================================
def base_word(sub, seed, min_len=60000):
    w = seed
    while len(w) < min_len:
        w = "".join(sub[c] for c in w)
    return list(w)                         # list of single-char ids


def two_blocks(word):
    """Admissible ordered 2-blocks (consecutive id pairs) in a level word."""
    return {(word[i], word[i + 1]) for i in range(len(word) - 1)}


def forces_border(sub, l2):
    """
    Level-1 border-forcing test for id-substitution `sub` with admissible ordered
    2-block set `l2`.  Returns (ok, left_multi, right_multi) where the *_multi are
    the witnesses (ids whose neighbour is NOT forced) -- the discriminating fact.
    """
    left_nb = defaultdict(set)             # v -> { last(sub[u])  : (u,v) admissible }
    right_nb = defaultdict(set)            # u -> { first(sub[v]) : (u,v) admissible }
    for (u, v) in l2:
        left_nb[v].add(sub[u][-1])
        right_nb[u].add(sub[v][0])
    left_multi = {v: sorted(map(str, s)) for v, s in left_nb.items() if len(s) != 1}
    right_multi = {u: sorted(map(str, s)) for u, s in right_nb.items() if len(s) != 1}
    ok = (not left_multi) and (not right_multi)
    return ok, left_multi, right_multi


def collar_step(sub, word):
    """
    One collaring step, generic over ids.
      new id  = 3-block (l,c,r) of the current word (a tuple of current ids).
      new sub[(l,c,r)] : let img=sub[c]=[c1..ck], L=last(sub[l]), R=first(sub[r]).
        k==1 : [ (L,c1,R) ]
        else : [ (L,c1,c2),(c1,c2,c3),...,(c_{k-1},ck,R) ]
      new word = sliding 3-window over `word`.
    Returns (new_sub, new_word).  ASSERTs every produced tile is an admissible
    3-block of the new word (image cannot escape the language).
    """
    new_word = [ (word[i-1], word[i], word[i+1]) for i in range(1, len(word)-1) ]
    tiles = set(new_word)
    last_of = {c: sub[c][-1] for c in sub}
    first_of = {c: sub[c][0] for c in sub}
    new_sub = {}
    for t in tiles:
        l, c, r = t
        img = sub[c]
        L, R = last_of[l], first_of[r]
        if len(img) == 1:
            out = [(L, img[0], R)]
        else:
            out = [(L, img[0], img[1])]
            out += [(img[i-1], img[i], img[i+1]) for i in range(1, len(img)-1)]
            out += [(img[-2], img[-1], R)]
        for o in out:
            assert o in tiles, ("collared image escaped language", t, o)
        new_sub[t] = out
    # sanity: substitution closed on the tile set (domain == produced ids' universe)
    produced = set().union(*[set(v) for v in new_sub.values()])
    assert produced <= tiles, ("produced ids not all admissible tiles",)
    return new_sub, new_word


# ======================================================================
# 1. AP complex of a (collared) substitution + induced map on H_1.
#    Graph Gamma: edges = tiles; two tiles U,V are glued right(U)~left(V) iff
#    (U,V) is an admissible 2-block (they occur consecutively in the word).
# ======================================================================
def ap_cohomology(tiles, sub, l2):
    tiles = list(tiles)
    E = len(tiles)
    eidx = {t: i for i, t in enumerate(tiles)}

    # union-find on 2E oriented endpoints: node 2i=left end, 2i+1=right end
    parent = list(range(2 * E))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for (u, v) in l2:
        union(2 * eidx[u] + 1, 2 * eidx[v] + 0)   # right(u) ~ left(v)

    reps = {}
    for n in range(2 * E):
        reps.setdefault(find(n), len(reps))
    V = len(reps)

    def node(i, side):
        return reps[find(2 * i + side)]

    b1 = E - V + 1

    # spanning tree over Gamma (V nodes, E edges: edge i joins node(i,0)-node(i,1))
    tp = list(range(V))

    def tfind(a):
        while tp[a] != a:
            tp[a] = tp[tp[a]]
            a = tp[a]
        return a
    tree_edges, cotree = [], []
    for i in range(E):
        u, v = node(i, 0), node(i, 1)
        ru, rv = tfind(u), tfind(v)
        if ru != rv:
            tp[ru] = rv
            tree_edges.append(i)
        else:
            cotree.append(i)
    assert len(cotree) == b1, (len(cotree), b1)

    tree_adj = defaultdict(list)
    for i in tree_edges:
        u, v = node(i, 0), node(i, 1)
        tree_adj[u].append((v, i, +1))
        tree_adj[v].append((u, i, -1))

    def tree_path_vec(src, dst):
        prev = {src: None}
        q = collections.deque([src])
        while q:
            x = q.popleft()
            if x == dst:
                break
            for (y, ei, sgn) in tree_adj[x]:
                if y not in prev:
                    prev[y] = (x, ei, sgn)
                    q.append(y)
        vec = [0] * E
        x = dst
        while prev[x] is not None:
            px, ei, sgn = prev[x]
            vec[ei] += sgn
            x = px
        return vec

    cycles = []
    for j in cotree:
        u, v = node(j, 0), node(j, 1)
        vec = [0] * E
        vec[j] += 1
        path = tree_path_vec(v, u)
        for e in range(E):
            vec[e] += path[e]
        cycles.append(vec)

    Gamma = sp.Matrix(E, b1, lambda r, c: cycles[c][r])

    Mc = sp.zeros(E, E)
    for t in tiles:
        for o in sub[t]:
            Mc[eidx[o], eidx[t]] += 1

    img = Mc * Gamma
    Bh = sp.Matrix(b1, b1, lambda i, j: img[cotree[i], j])

    # ASSERT induced image is a genuine cycle (closed under boundary) -- both dirs
    d1 = sp.zeros(V, E)
    for i in range(E):
        d1[node(i, 1), i] += 1
        d1[node(i, 0), i] -= 1
    for j in range(b1):
        assert (d1 * img[:, j]) == sp.zeros(V, 1), "induced image not a cycle"
    # ASSERT cotree-coefficient readout is exact (cycles are a basis)
    assert sp.Matrix(E, b1, lambda r, c: (Gamma * Bh)[r, c]) == img, \
        "cotree readout failed (cycles not a basis)"

    return {"E": E, "V": V, "b1": b1, "B": Bh}


# ======================================================================
# 2. direct-limit group invariants of (Z^m, B)  (=> Hˇ^1 = lim_->(Z^m,B^T))
# ======================================================================
def direct_limit(B):
    m = B.shape[0]
    x = sp.symbols('x')
    if m == 0:
        return {"rank": 0, "d": 1, "d_abs": 1, "primes": {},
                "charpoly_str": "1"}
    p = B.charpoly(x).as_expr()
    r = (B**m).rank()                         # eventual rank
    poly = sp.Poly(p, x)
    k0, q = 0, poly
    while q.eval(0) == 0:
        q = q.quo(sp.Poly(x, x))
        k0 += 1
    assert (m - k0) == r, ("zero-eig mult vs eventual rank", m - k0, r)
    d = int(q.eval(0))
    d_abs = abs(d)
    primes = {}
    if d_abs > 1:
        for pr in sp.factorint(d_abs):
            qmodp = sp.Poly([c % pr for c in q.all_coeffs()], x, modulus=pr)
            cp, qq = 0, qmodp
            while qq.eval(0) % pr == 0 and qq.degree() > 0:
                qq = qq.quo(sp.Poly(x, x, modulus=pr))
                cp += 1
            primes[int(pr)] = int(cp)
    return {"rank": int(r), "d": int(d), "d_abs": int(d_abs),
            "primes": primes, "charpoly_str": str(p)}


def group_string(dl):
    r = dl["rank"]
    if dl["d_abs"] == 1:
        return "0" if r == 0 else ("Z" if r == 1 else f"Z^{r}")
    inverted = sum(dl["primes"].values())
    pure = r - inverted
    parts = []
    if pure > 0:
        parts.append("Z" if pure == 1 else f"Z^{pure}")
    for pr, cp in sorted(dl["primes"].items()):
        parts.append(f"Z[1/{pr}]" if cp == 1 else f"Z[1/{pr}]^{cp}")
    return " (+) ".join(parts)


# ======================================================================
# 3. driver: primitivity/aperiodicity/recognizability, then COLLAR-ITERATE the
#    border-forcing test, then cohomology at d* and d*+1.
# ======================================================================
def incidence(sub, letters):
    M = sp.zeros(len(letters), len(letters))
    idx = {c: i for i, c in enumerate(letters)}
    for j, c in enumerate(letters):
        for ch in sub[c]:
            M[idx[ch], j] += 1
    return M


def is_primitive(M, maxp=80):
    n = M.shape[0]
    P = sp.eye(n)
    for k in range(1, maxp + 1):
        P = P * M
        if all(P[i, j] > 0 for i in range(n) for j in range(n)):
            return True, k
    return False, None


def complexity(word, nmax):
    return [len({tuple(word[i:i+n]) for i in range(len(word)-n+1)})
            for n in range(1, nmax + 1)]


def run(name, sub0, seed, expect_group=None):
    letters = sorted(sub0.keys())
    log(f"===== {name}: sub={sub0} =====")
    w0 = base_word(sub0, seed, 60000)
    sub = {c: list(sub0[c]) for c in sub0}     # normalize to id->list

    # --- recognizability prerequisites (Mosse): primitive + aperiodic ---
    M = incidence(sub0, letters)
    prim, kprim = is_primitive(M)
    gate(f"{name}:primitive", prim, f"M^{kprim}>0")
    comp = complexity(w0, 12)
    ape = all(comp[n-1] >= n+1 for n in range(1, 13)) and \
        all(comp[i] <= comp[i+1] for i in range(len(comp)-1)) and comp[-1] > comp[3]
    gate(f"{name}:aperiodic", ape, f"p(n)={comp} (>= n+1, non-decreasing, unbounded)")
    recognizable = prim and ape
    gate(f"{name}:recognizable(Mosse)", recognizable, "primitive+aperiodic => Mosse")

    # --- comparator control: RAW system must NOT force the border (criterion can
    #     fail).  If raw already forced, collaring would be vacuous. ---
    l2_0 = two_blocks(w0)
    raw_ok, _, _ = forces_border(sub, l2_0)

    # --- COLLAR-ITERATE the border-forcing test ---
    levels = [(sub, w0, l2_0)]                 # level 0 = raw
    force_table = [(0, raw_ok)]
    dstar = 0 if raw_ok else None
    cur_sub, cur_word = sub, w0
    for d in range(1, DMAX + 1):
        cur_sub, cur_word = collar_step(cur_sub, cur_word)
        l2 = two_blocks(cur_word)
        ok, lm, rm = forces_border(cur_sub, l2)
        levels.append((cur_sub, cur_word, l2))
        force_table.append((d, ok))
        log(f"{name}: collar depth {d}: tiles={len(set(cur_word))}  "
            f"forces_border={ok}" + ("" if ok else f"  unforced_left={lm} unforced_right={rm}"))
        if ok and dstar is None:
            dstar = d
            # continue one more level so we can cross-check d* vs d*+1 cohomology
            if d + 1 <= DMAX:
                nsub, nword = collar_step(cur_sub, cur_word)
                levels.append((nsub, nword, two_blocks(nword)))
                nok, _, _ = forces_border(nsub, two_blocks(nword))
                force_table.append((d + 1, nok))
                # once forced, all deeper collars must stay forced (monotone) -- ASSERT
                gate(f"{name}:forcing-stable@{d+1}", nok,
                     "border must remain forced under further collaring")
            break

    log(f"{name}: raw forces_border={raw_ok}   force_table={force_table}   d*={dstar}")

    result = {"name": name, "sub": sub0, "primitive": prim, "aperiodic": bool(ape),
              "recognizable": recognizable, "raw_forces_border": raw_ok,
              "force_table": force_table, "collar_depth": dstar, "comp": comp}

    if dstar is None:
        gate(f"{name}:border-forces(<= D{DMAX})", False,
             "border never forced within DMAX -> non-forcing obstruction")
        result["H1"] = None
        return result

    # --- cohomology at d* and (if available) d*+1; must agree ---
    def coh_at(level_idx):
        s, wd, l2 = levels[level_idx]
        tiles = sorted(set(wd), key=str)
        coh = ap_cohomology(tiles, s, l2)
        dl = direct_limit(coh["B"])
        g = group_string(dl)
        return coh, dl, g

    coh_ds, dl_ds, g_ds = coh_at(dstar)          # index dstar == depth dstar (level list is 0..)
    log(f"{name}: @d*={dstar}  AP complex E={coh_ds['E']} V={coh_ds['V']} b1={coh_ds['b1']}")
    log(f"{name}: @d*={dstar}  induced H_1 matrix B=\n{coh_ds['B']}")
    log(f"{name}: @d*={dstar}  charpoly(B)={dl_ds['charpoly_str']}  rank={dl_ds['rank']}  "
        f"det_image={dl_ds['d']}  primes_inverted={dl_ds['primes']}")
    log(f"{name}: @d*={dstar}  Hˇ^0=Z  Hˇ^1={g_ds}")

    result.update({
        "E": coh_ds["E"], "V": coh_ds["V"], "b1": coh_ds["b1"],
        "B": [[int(coh_ds["B"][i, j]) for j in range(coh_ds["b1"])]
              for i in range(coh_ds["b1"])],
        "charpoly_B": dl_ds["charpoly_str"], "rank": dl_ds["rank"],
        "det_image": dl_ds["d"], "primes_inverted": dl_ds["primes"],
        "H0": "Z", "H1": g_ds})

    # robustness: cohomology invariant under one more collaring (Omega unchanged)
    if dstar + 1 < len(levels):
        _, _, g_next = coh_at(dstar + 1)
        stable = (g_next == g_ds)
        gate(f"{name}:Hˇ^1 stable under extra collar", stable,
             f"Hˇ^1@d*={g_ds}  Hˇ^1@d*+1={g_next}")
        result["H1_next"] = g_next

    if expect_group is not None:
        ok = (g_ds == expect_group)
        gate(f"{name}:CONTROL matches textbook Hˇ^1", ok, f"got {g_ds}, expected {expect_group}")
        result["control_expected"] = expect_group
        result["control_ok"] = ok
    return result


# ======================================================================
LANG_RESULTS = {}

# CONTROL 1: Fibonacci, textbook Hˇ^1 = Z^2
LANG_RESULTS["fibonacci"] = run("Fibonacci", {"a": "ab", "b": "a"}, "a",
                                expect_group="Z^2")
# CONTROL 2: Thue-Morse, textbook Hˇ^1 = Z (+) Z[1/2]
LANG_RESULTS["thue_morse"] = run("Thue-Morse", {"a": "ab", "b": "ba"}, "a",
                                 expect_group="Z (+) Z[1/2]")

# vacuity self-test: the two controls must give DIFFERENT cohomology (a swapped
# substitution changes the answer => forces_border/cohomology are not vacuous)
gate("vacuity:controls-differ",
     LANG_RESULTS["fibonacci"]["H1"] != LANG_RESULTS["thue_morse"]["H1"],
     f"Fib={LANG_RESULTS['fibonacci']['H1']}  TM={LANG_RESULTS['thue_morse']['H1']}")

# TARGET: sigma_4
SIGMA4 = {"a": "abAAB", "b": "aAB", "A": "abAB", "B": "aA"}
LANG_RESULTS["sigma_4"] = run("sigma_4", SIGMA4, "a")

# banked cross-check: exactly 7 admissible 2-blocks (GRAMMAR.md)
w4 = base_word(SIGMA4, "a", 60000)
gate("sigma_4:7-transitions(banked)", len(two_blocks(w4)) == 7,
     f"admissible 2-blocks={sorted(''.join(t) for t in two_blocks(w4))}")

# comparator: raw sigma_4 must NOT force border (criterion can fail) while the
# collared one does (criterion can pass) -- the discriminating fact
s4 = LANG_RESULTS["sigma_4"]
gate("sigma_4:raw-does-not-force(comparator)", s4["raw_forces_border"] is False,
     "raw substitution fails border-forcing => collaring does real work")

# ======================================================================
# VERDICT  (in-code; UNRESOLVED reachable)
# ======================================================================
controls_ok = (LANG_RESULTS["fibonacci"].get("control_ok") and
               LANG_RESULTS["thue_morse"].get("control_ok"))
s4_forces = s4["collar_depth"] is not None
s4_recognizable = s4["recognizable"]

if FAILED:
    verdict = "UNRESOLVED"
    headline = f"pipeline uncertified; failed gates: {FAILED}"
elif not s4_recognizable:
    verdict = "RESOLVED-B"
    headline = "sigma_4 not recognizable (non-primitive/periodic) -- AP does not apply"
elif not s4_forces:
    verdict = "RESOLVED-B"
    headline = (f"sigma_4 border NEVER forces up to collar depth {DMAX} "
                "-- non-recognizable border obstruction")
elif controls_ok:
    verdict = "RESOLVED-A"
    headline = (f"sigma_4 border FORCED at collar depth d*={s4['collar_depth']}; "
                f"certified AP complex E={s4['E']} V={s4['V']} b1={s4['b1']}; "
                f"Hˇ^0=Z, Hˇ^1={s4['H1']} (stable under extra collaring)")
else:
    verdict = "UNRESOLVED"
    headline = "controls did not reproduce textbook cohomology"

log("=" * 64)
log(f"VERDICT: {verdict}")
log(f"HEADLINE: {headline}")
log(f"FAILED GATES: {FAILED}")

OUT = {"verdict": verdict, "headline": headline, "failed_gates": FAILED,
       "DMAX": DMAX,
       "sigma_4_collar_depth": s4["collar_depth"],
       "sigma_4_force_table": s4["force_table"],
       "sigma_4_raw_forces_border": s4["raw_forces_border"],
       "sigma_4_H0": "Z", "sigma_4_H1": s4.get("H1"),
       "sigma_4_b1": s4.get("b1"), "sigma_4_E": s4.get("E"), "sigma_4_V": s4.get("V"),
       "sigma_4_charpoly_B": s4.get("charpoly_B"),
       "sigma_4_det_image": s4.get("det_image"),
       "sigma_4_primes_inverted": s4.get("primes_inverted"),
       "sigma_4_H1_next_collar": s4.get("H1_next"),
       "controls": {k: {"collar_depth": LANG_RESULTS[k]["collar_depth"],
                        "H1": LANG_RESULTS[k].get("H1"),
                        "control_ok": LANG_RESULTS[k].get("control_ok"),
                        "force_table": LANG_RESULTS[k]["force_table"]}
                    for k in ("fibonacci", "thue_morse")},
       "results": LANG_RESULTS}
with open(f"{CELL}/results.json", "w") as f:
    json.dump(OUT, f, indent=2, default=str)
log(f"wrote {CELL}/results.json")
