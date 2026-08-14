"""B1043 -- THE TRIPLE ASSEMBLY (sealed 575ad81b pre-compute).

The algebraic triple: triangle graph-of-groups, presentation
  < a, b1, b2, b3, t | REL(a,b1), REL(a,b2), REL(a,b3),
                       L1*L2^-1, L2*L3^-1, t a t^-1 a^-1, t L3 t^-1 L1^-1 >
identity gluing (rho(b_i) = B27 for all i), rho(t) = I (declared in the seal).
Reuses B632 cell 2's banked machinery by exec (the B1039 pattern; helpers inlined
per the namespace-drift hazard). Exact K arithmetic; sum(..., K0) throughout.

W0 the double gate (must reproduce h1 = 5 with anatomy 2+3) -> W1 h1(triple;27)
-> W2 anatomy per the sealed connecting formula -> W3 F3 (>=6) + DECOY D (>=12)
-> W4 the 3-cell check (the arity pairing's target).
"""
import io, os, time, contextlib

HERE = os.path.dirname(os.path.abspath(__file__))
CELL2 = os.path.join(HERE, "..", "B632_cubic_route", "cell2_texture.py")

ns = {"__name__": "b632_cell2", "__file__": CELL2}
t0 = time.time()
print("exec B632 cell2 (the full banked machinery)...", flush=True)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    exec(compile(open(CELL2).read(), CELL2, "exec"), ns)
print(f"cell2 loaded in {time.time()-t0:.1f}s", flush=True)

K, K0, K1 = ns["K"], ns["K0"], ns["K1"]
A27, B27, A27i, B27i = ns["A27"], ns["B27"], ns["A27i"], ns["B27i"]
rref = ns["ns"]["rref"]
REL = ns["REL"]
LONG = "abABaaBAbA"
DIM = 27


def meye(k):
    return [[K1 if i == j else K0 for j in range(k)] for i in range(k)]

def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def mmul(A, B):
    m, k, c = len(A), len(B), len(B[0])
    out = [[K0] * c for _ in range(m)]
    for i in range(m):
        Ai = A[i]
        for t_ in range(k):
            a = Ai[t_]
            if a.is_zero():
                continue
            Bt = B[t_]; oi = out[i]
            for j in range(c):
                if not Bt[j].is_zero():
                    oi[j] = oi[j] + a * Bt[j]
    return out

I27 = meye(DIM)


def rank_of(M):
    R, piv = rref([row[:] for row in M])
    return len(piv)


def nullity(M, ncols):
    return ncols - rank_of(M)


# ---- words as token lists: (genname, +1/-1); string words use a/A, b/B templates
def word_tokens(template, bname):
    toks = []
    for ch in template:
        if ch == "a":
            toks.append(("a", 1))
        elif ch == "A":
            toks.append(("a", -1))
        elif ch == "b":
            toks.append((bname, 1))
        elif ch == "B":
            toks.append((bname, -1))
        else:
            raise ValueError(ch)
    return toks

def inv_word(toks):
    return [(g, -s) for (g, s) in reversed(toks)]


def rho_of(gmats, toks):
    M = I27
    for (g, s) in toks:
        M = mmul(M, gmats[g][0] if s == 1 else gmats[g][1])
    return M


def fox_blocks(gmats, gens, toks):
    """Fox derivative blocks: d(word)/d(gen) evaluated in rho, per generator."""
    blocks = {g: [[K0] * DIM for _ in range(DIM)] for g in gens}
    prefix = I27
    for (g, s) in toks:
        if s == 1:
            blocks[g] = madd(blocks[g], prefix)
            prefix = mmul(prefix, gmats[g][0])
        else:
            prefix = mmul(prefix, gmats[g][1])
            blocks[g] = msub(blocks[g], prefix)
    return blocks


def h1(gmats, gens, relators):
    """dim H^1 = (g*27 - rank C) - (27 - h0), C the cocycle-constraint matrix."""
    rows = []
    for rel in relators:
        blocks = fox_blocks(gmats, gens, rel)
        for i in range(DIM):
            row = []
            for g in gens:
                row.extend(blocks[g][i])
            rows.append(row)
    rankC = rank_of(rows)
    dimZ1 = len(gens) * DIM - rankC
    stack = []
    for g in gens:
        stack.extend(msub(gmats[g][0], I27))
    h0 = nullity(stack, DIM)
    dimB1 = DIM - h0
    return dimZ1 - dimB1, h0


# ---- shared invariant dimensions
h0_M_stack = msub(A27, I27) + msub(B27, I27)
h0_M = nullity(h0_M_stack, DIM)
L27 = rho_of({"a": (A27, A27i), "b": (B27, B27i)}, word_tokens(LONG, "b"))
L27i = rho_of({"a": (A27, A27i), "b": (B27, B27i)}, inv_word(word_tokens(LONG, "b")))
h0_T_stack = msub(A27, I27) + msub(L27, I27)
h0_T = nullity(h0_T_stack, DIM)
print(f"[V1-pre] h0(M;27) = {h0_M}   h0(T^2;27) = {h0_T}", flush=True)

# ---- W0: THE DOUBLE GATE (path amalgam; must reproduce banked h1 = 5, anatomy 2+3)
gm2 = {"a": (A27, A27i), "b1": (B27, B27i), "b2": (B27, B27i)}
gens2 = ["a", "b1", "b2"]
rel2 = [
    word_tokens(REL, "b1"),
    word_tokens(REL, "b2"),
    word_tokens(LONG, "b1") + inv_word(word_tokens(LONG, "b2")),
]
t1 = time.time()
h1_dbl, h0_dbl = h1(gm2, gens2, rel2)
print(f"[W0] h1(double;27) = {h1_dbl} (banked: 5; h0 = {h0_dbl})  [{time.time()-t1:.0f}s]", flush=True)
assert h1_dbl == 5, "ENTRY GATE FAILED -- HALT (machinery fault, not a result)"

# the sealed formula PROPERLY: connecting = dim coker(⊕_v H0(M_v) -> ⊕_e H0(T_e)),
# via the actual MV difference maps. h0(M;27) = 1 (computed above -- the 27 carries
# an invariant line under the solo group; the h0(M)=0 shortcut was WRONG and the
# entry gate caught it). Edge map for identity gluings: restrictions differ.
def mv_connecting(n_vertices, edge_pairs):
    """rank of ⊕H0(M_v) -> ⊕H0(T_e), (v_i) |-> (v_i - v_j)_e; each H0(M) is the
    SAME invariant line inside the same 27 (identity gluing), so the map is
    determined by the difference pattern on the line's coefficient."""
    # coefficient matrix over Q: rows = edges, cols = vertices, +1/-1 pattern,
    # tensored with the (1-dim) invariant line -- rank = rank of the pattern
    # times 1 (the line is 1-dim, and its restriction to H0(T) is injective:
    # the invariant vector is nonzero in H0(T) since invariance under the whole
    # group implies invariance under the peripheral subgroup).
    import itertools
    rowsQ = []
    for (i, j) in edge_pairs:
        r = [0] * n_vertices
        r[i], r[j] = 1, -1
        rowsQ.append(r)
    # rank over Q by Gaussian elimination on small ints
    m = [r[:] for r in rowsQ]
    rank = 0
    for col in range(n_vertices):
        piv = next((k for k in range(rank, len(m)) if m[k][col] != 0), None)
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        for k in range(len(m)):
            if k != rank and m[k][col] != 0:
                f = m[k][col] / m[rank][col]
                m[k] = [a - f * b for a, b in zip(m[k], m[rank])]
        rank += 1
    return rank * h0_M  # the pattern rank times the invariant line's dimension

rank_dbl = mv_connecting(2, [(0, 1)])
conn_dbl = 1 * h0_T - rank_dbl
print(f"[W0] double: coker(H0-MV) = 1 seam x h0(T) - rank = {1*h0_T} - {rank_dbl} = {conn_dbl}, "
      f"bulk = {h1_dbl - conn_dbl} (banked: 2 + 3) -- GATE {'PASS' if (conn_dbl==2 and h1_dbl-conn_dbl==3) else 'FAIL'}", flush=True)
assert conn_dbl == 2 and h1_dbl - conn_dbl == 3

# ---- W1: THE TRIPLE
gm3 = {"a": (A27, A27i), "b1": (B27, B27i), "b2": (B27, B27i),
       "b3": (B27, B27i), "t": (I27, I27)}
gens3 = ["a", "b1", "b2", "b3", "t"]
L1, L2, L3 = (word_tokens(LONG, b) for b in ("b1", "b2", "b3"))
rel3 = [
    word_tokens(REL, "b1"),
    word_tokens(REL, "b2"),
    word_tokens(REL, "b3"),
    L1 + inv_word(L2),
    L2 + inv_word(L3),
    [("t", 1), ("a", 1), ("t", -1), ("a", -1)],
    [("t", 1)] + L3 + [("t", -1)] + inv_word(L1),
]
t2 = time.time()
h1_tri, h0_tri = h1(gm3, gens3, rel3)
print(f"[W1] h1(triple;27) = {h1_tri}  (h0 = {h0_tri})  [{time.time()-t2:.0f}s]", flush=True)

# ---- W2: anatomy per the sealed connecting formula (the ACTUAL MV map)
rank_tri = mv_connecting(3, [(0, 1), (1, 2), (2, 0)])
conn_tri = 3 * h0_T - rank_tri
bulk_tri = h1_tri - conn_tri
print(f"[W2] triple: coker(H0-MV) = 3 seams x h0(T) - rank = {3*h0_T} - {rank_tri} = {conn_tri}", flush=True)
print(f"[W2] bulk = h1 - connecting = {bulk_tri}", flush=True)
print(f"[W2] the cycle's fingerprint (typed): the vertex-difference pattern on the", flush=True)
print(f"     triangle has rank 2 (its kernel is the diagonal), so the cyclic closure", flush=True)
print(f"     contributes h0(M) = {h0_M} EXTRA connecting class(es) beyond the linear", flush=True)
print(f"     3x(per-seam) count -- creation is SUPERLINEAR in the cyclic assembly", flush=True)
print(f"     iff conn > 3 x {conn_dbl} = {3*conn_dbl}: {'YES' if conn_tri > 3*conn_dbl else 'NO'}", flush=True)

# ---- W3: THE FORBID + THE DECOY (both sealed)
f3_pass = conn_tri >= 6
decoy_pass = conn_tri >= 12
print(f"[W3] F3 (>= 6, pinned pre-arc): connecting = {conn_tri} -> {'PASS' if f3_pass else 'FAIL'}", flush=True)
print(f"[W3] DECOY D (>= 12, deliberately unbanked): -> {'PASS' if decoy_pass else 'FAIL'}", flush=True)
if f3_pass and not decoy_pass:
    print("[W3] discrimination reading (sealed): F3-pass + D-fail => the comparison", flush=True)
    print("     DISCRIMINATES; F3's outcome is INFORMATIVE. R44-12 discharged.", flush=True)
elif f3_pass and decoy_pass:
    print("[W3] BOTH PASS => suspect; vacuity investigation opens before any F3 credit.", flush=True)
else:
    print("[W3] F3 FAILS -> the frame loses its monotone-creation verb (the amendment's", flush=True)
    print("     own consequence).", flush=True)

# ---- W4: THE ARITY QUESTION -- the 3-slot pairing's target on THIS assembly
n_3cells = 0  # the presentation 2-complex has cells of dim <= 2 by construction
print(f"[W4] 3-cells in the assembly's presentation complex: {n_3cells}", flush=True)
print("[W4] HALT-VOID (the sealed halting discipline): the genuine three-slot cup", flush=True)
print("     H1 x H1 x H1 -> H3 has NO TARGET on a 2-complex -- the algebraic triple", flush=True)
print("     carries the arity-matched CLASSES but not the arity-matched PAIRING", flush=True)
print("     dimension. The 2-slot saturated form B_C is exactly what the arity", flush=True)
print("     observation excludes as the test. THE NAMED DOOR: an H3-bearing 3-body", flush=True)
print("     assembly -- the closed mirror-double OF the 3-fold cyclic cover", flush=True)
print("     (a genuine 3-manifold containing three commuting copies) -- is the", flush=True)
print("     arity test's true home; a future cell.", flush=True)

print("==== B1043 compute done ====", flush=True)
