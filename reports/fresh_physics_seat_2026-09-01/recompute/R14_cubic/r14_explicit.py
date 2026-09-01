#!/usr/bin/env python3
"""R14 blind recomputation, part 2 (explicit, exact, own frame).

Own construction (trinification frame), no arc code consulted:
  27 variables: A (3x3, color 3, SU(3)_L 3bar), B (3x3, SU(3)_L 3, SU(3)_R 3bar),
                C (3x3, SU(3)_R 3, color 3bar).
  Candidate cubic  I = det A + det B + det C - tr(A B C).

  (a) Exact stabilizer algebra of I inside gl(27): the invariance system block-
      decomposes by (A,B,C)-multidegree into diagonal / cyclic / anticyclic
      block ansaetze; exact sparse nullspaces give dims 24 + 27 + 27 = 78 = e6.
  (b) Exact uniqueness in this frame: weight-zero cubic monomial space (under the
      6 Cartans) -> impose all 78 generators -> exact nullspace dim, and the
      nullvector's support/coefficients.
  (c) Planted-positive control: same pipeline under sl3^3 only (24 gens) -> dim must be >1.
  (d) SM-graded support table: 11 pieces [6,3 | 2,2,2,1,1,1 | 3,3,3], 286 unordered
      piece-triples; count cells hit by the cubic, and cells allowed by charges alone.
All arithmetic exact (int/Fraction).
"""
from fractions import Fraction
from itertools import combinations_with_replacement, permutations

N = 27
# variable indexing
def vA(i, j): return 3 * i + j          # A_ij  : i color, j L
def vB(j, k): return 9 + 3 * j + k      # B_jk  : j L, k R
def vC(k, i): return 18 + 3 * k + i     # C_ki  : k R, i color

# ---------- polynomials as dict{sorted tuple of var indices: int} ----------
def padd(P, Q, c=1):
    for m, v in Q.items():
        P[m] = P.get(m, 0) + c * v
        if P[m] == 0:
            del P[m]
    return P

def build_cubic():
    I = {}
    # det A, det B, det C
    for (f, sgnblk) in ((vA, 1), (vB, 1), (vC, 1)):
        for perm in permutations(range(3)):
            s = 1
            # permutation sign
            p = list(perm); sg = 1
            for a in range(3):
                for b in range(a + 1, 3):
                    if p[a] > p[b]:
                        sg = -sg
            mono = tuple(sorted(f(r, perm[r]) for r in range(3)))
            padd(I, {mono: sg * sgnblk})
    # - tr(ABC) = - A_ij B_jk C_ki
    for i in range(3):
        for j in range(3):
            for k in range(3):
                mono = tuple(sorted((vA(i, j), vB(j, k), vC(k, i))))
                padd(I, {mono: -1})
    return I

I = build_cubic()
coeffs = sorted(set(I.values()))
print("[cubic] monomials:", len(I), " coefficient set:", coeffs,
      " squarefree:", all(len(set(m)) == 3 for m in I))

# ---------- action of a linear map M (dict (a,b)->coeff meaning dx_a += M_ab x_b) on a cubic ----------
def act(M, P):
    """(M.P)(x) = sum_a dP/dx_a * (M x)_a ; M sparse dict {(a,b): c}."""
    out = {}
    for mono, cv in P.items():
        # dP/dx_a for each position in mono
        for pos in range(3):
            a = mono[pos]
            rest = mono[:pos] + mono[pos + 1:]
            # multiplicity handling: derivative of x_a^r gives r * x_a^{r-1}; since we
            # iterate positions, each copy contributes once -> correct total factor.
            for (aa, b), c in M.items():
                if aa == a:
                    newm = tuple(sorted(rest + (b,)))
                    out[newm] = out.get(newm, 0) + cv * c
    return {m: v for m, v in out.items() if v != 0}

# ---------- exact sparse nullspace (rows: dict col->Fraction) ----------
def nullspace(rows, ncols):
    piv = {}   # col -> reduced row (dict)
    for r in rows:
        r = {c: Fraction(v) for c, v in r.items() if v != 0}
        while r:
            c = min(r)
            if c in piv:
                f = r[c]
                pr = piv[c]
                for cc, vv in pr.items():
                    r[cc] = r.get(cc, Fraction(0)) - f * vv
                    if r[cc] == 0:
                        del r[cc]
            else:
                inv = r[c]
                piv[c] = {cc: vv / inv for cc, vv in r.items()}
                break
    # back-substitute to RREF
    cols = sorted(piv)
    for c in reversed(cols):
        pr = piv[c]
        for c2 in cols:
            if c2 < c and c in piv[c2]:
                f = piv[c2][c]
                for cc, vv in pr.items():
                    piv[c2][cc] = piv[c2].get(cc, Fraction(0)) - f * vv
                    if piv[c2][cc] == 0:
                        del piv[c2][cc]
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for c in cols:
            if fc in piv[c]:
                v[c] = -piv[c][fc]
        basis.append(v)
    return basis

# ---------- (a) stabilizer: three block ansaetze ----------
def block_system(blocks):
    """blocks: list of (target_block, source_block) pairs, each in {'A','B','C'};
       unknowns: entries of the 9x9 maps between blocks. Returns nullspace basis
       as sparse M dicts."""
    rng = {'A': list(range(0, 9)), 'B': list(range(9, 18)), 'C': list(range(18, 27))}
    unknowns = []   # (tgt_var, src_var)
    for (t, s) in blocks:
        for a in rng[t]:
            for b in rng[s]:
                unknowns.append((a, b))
    uidx = {u: q for q, u in enumerate(unknowns)}
    # equations: coefficients of sum_u m_u * x_srcb * dI/dx_tgta
    eqs = {}   # monomial -> dict uidx -> coeff
    for (a, b) in unknowns:
        contrib = act({(a, b): 1}, I)
        for mono, v in contrib.items():
            eqs.setdefault(mono, {})[uidx[(a, b)]] = v
    ns = nullspace(list(eqs.values()), len(unknowns))
    out = []
    for v in ns:
        M = {}
        for q, val in enumerate(v):
            if val != 0:
                M[unknowns[q]] = val
        out.append(M)
    return out

diag_ns = block_system([('A', 'A'), ('B', 'B'), ('C', 'C')])
cyc_ns = block_system([('A', 'B'), ('B', 'C'), ('C', 'A')])
acyc_ns = block_system([('A', 'C'), ('B', 'A'), ('C', 'B')])
print("[stab] diagonal-block nullspace dim:", len(diag_ns))
print("[stab] cyclic-block   nullspace dim:", len(cyc_ns))
print("[stab] anticyc-block  nullspace dim:", len(acyc_ns))
dim_stab = len(diag_ns) + len(cyc_ns) + len(acyc_ns)
print("[stab] TOTAL dim of stabilizer algebra of I in gl(27):", dim_stab, "(e6 = 78)")
gens78 = diag_ns + cyc_ns + acyc_ns
# exact verification: every generator annihilates I
assert all(act(M, I) == {} for M in gens78)
print("[stab] all", dim_stab, "generators annihilate I exactly: True")

# sanity: no other blocks can contribute (multidegree argument) — verify the four
# remaining mixed pairings give trivial nullspace contributions beyond the above?
# The A<-A etc. are covered; mixed types like ('A','B') with ('B','A') would mix
# degree sectors; check one such combined ansatz gives nothing new:
extra = block_system([('A', 'B'), ('B', 'A')])
print("[stab-control] ansatz dA<-B, dB<-A alone: nullspace dim:", len(extra), "(expect 0)")

# ---------- sl3^3 generators explicitly (for planted control + Cartan) ----------
def sl3_basis():
    bas = []
    for i in range(3):
        for j in range(3):
            if i != j:
                bas.append({(i, j): Fraction(1)})
    bas.append({(0, 0): Fraction(1), (1, 1): Fraction(-1)})
    bas.append({(1, 1): Fraction(1), (2, 2): Fraction(-1)})
    return bas

def emb_color(P):   # dA = P A, dC = -C P
    M = {}
    for (p, q), c in P.items():
        for j in range(3):
            M[(vA(p, j), vA(q, j))] = M.get((vA(p, j), vA(q, j)), 0) + c
        for k in range(3):
            M[(vC(k, q), vC(k, p))] = M.get((vC(k, q), vC(k, p)), 0) - c
    return M

def emb_L(P):       # dB = P B, dA = -A P
    M = {}
    for (p, q), c in P.items():
        for k in range(3):
            M[(vB(p, k), vB(q, k))] = M.get((vB(p, k), vB(q, k)), 0) + c
        for i in range(3):
            M[(vA(i, q), vA(i, p))] = M.get((vA(i, q), vA(i, p)), 0) - c
    return M

def emb_R(P):       # dC = P C, dB = -B P
    M = {}
    for (p, q), c in P.items():
        for i in range(3):
            M[(vC(p, i), vC(q, i))] = M.get((vC(p, i), vC(q, i)), 0) + c
        for j in range(3):
            M[(vB(j, q), vB(j, p))] = M.get((vB(j, q), vB(j, p)), 0) - c
    return M

sl3cube = [emb(P) for emb in (emb_color, emb_L, emb_R) for P in sl3_basis()]
assert all(act(M, I) == {} for M in sl3cube)
print("[sl3^3] 24 generators annihilate I exactly: True")

# Cartan charges of the 27 variables (6 diagonal generators)
H = []
for emb in (emb_color, emb_L, emb_R):
    H.append(emb({(0, 0): Fraction(1), (1, 1): Fraction(-1)}))
    H.append(emb({(1, 1): Fraction(1), (2, 2): Fraction(-1)}))
wt = []
for a in range(N):
    wt.append(tuple(M.get((a, a), Fraction(0)) for M in H))

# ---------- weight-zero cubic monomial space ----------
zero_monos = []
for t in combinations_with_replacement(range(N), 3):
    s = tuple(wt[t[0]][q] + wt[t[1]][q] + wt[t[2]][q] for q in range(6))
    if all(x == 0 for x in s):
        zero_monos.append(t)
print("[frame] weight-zero cubic monomials:", len(zero_monos),
      " squarefree:", all(len(set(m)) == 3 for m in zero_monos))

def invariance_nullspace(gens, monos):
    midx = {m: q for q, m in enumerate(monos)}
    rows = {}
    for gi, M in enumerate(gens):
        for q, m in enumerate(monos):
            for outm, v in act(M, {m: 1}).items():
                rows.setdefault((gi, outm), {})[q] = v
    return nullspace(list(rows.values()), len(monos))

ns_full = invariance_nullspace(gens78, zero_monos)
print("[unique] nullspace dim of invariance system (78 gens, weight-zero cubics):", len(ns_full))
if len(ns_full) == 1:
    v = ns_full[0]
    # normalize: make entries integer, primitive
    from math import gcd
    den = 1
    for x in v:
        den = den * x.denominator // gcd(den, x.denominator)
    iv = [int(x * den) for x in v]
    g = 0
    for x in iv:
        g = gcd(g, abs(x))
    iv = [x // g for x in iv]
    nz = [x for x in iv if x != 0]
    print("[unique] support:", len(nz), "/", len(iv),
          " coefficient values:", sorted(set(nz)))
    # cross-check equals I up to sign
    recon = {}
    for q, m in enumerate(zero_monos):
        if iv[q]:
            recon[m] = iv[q]
    sgn = None
    same = True
    for m, c in recon.items():
        if m not in I:
            same = False; break
        r = Fraction(I[m], c)
        if sgn is None:
            sgn = r
        elif r != sgn:
            same = False; break
    print("[unique] reconstructed nullvector equals det+det+det-tr cubic up to overall scale:",
          same and len(recon) == len(I), " scale:", sgn)

# ---------- planted-positive control: sl3^3 only ----------
ns_ctrl = invariance_nullspace(sl3cube, zero_monos)
print("[control] nullspace dim under sl3^3 only (24 gens):", len(ns_ctrl), "(must be > 1)")

# ---------- SM-graded cells ----------
# pieces: from A: Q = columns j=0,1 (6);  T_A = column j=2 (3)
#         from B: doublets d_k = rows j=0,1, column k (2 each); singlets s_k = row j=2 (1 each)
#         from C: antitriplets t_k = row k (3 each)
piece = {}
names = {}
for i in range(3):
    for j in range(3):
        piece[vA(i, j)] = 'Q' if j < 2 else 'D'
for j in range(3):
    for k in range(3):
        piece[vB(j, k)] = ('d%d' % k) if j < 2 else ('s%d' % k)
for k in range(3):
    for i in range(3):
        piece[vC(k, i)] = 't%d' % k
plist = sorted(set(piece.values()))
psize = {p: sum(1 for a in range(N) if piece[a] == p) for p in plist}
print("[cells] pieces:", {p: psize[p] for p in plist}, " count:", len(plist))
ncells = len(list(combinations_with_replacement(plist, 3)))
print("[cells] total unordered piece-triples:", ncells)

support_cells = {}
for m, c in I.items():
    cell = tuple(sorted(piece[a] for a in m))
    support_cells.setdefault(cell, []).append((m, c))
print("[cells] cells hit by the cubic (coupled):", len(support_cells),
      " -> zeros:", ncells - len(support_cells))
for cell in sorted(support_cells):
    sizes = tuple(sorted(psize[p] for p in cell))
    print("    cell", cell, " sizes", sizes, " #monomials:", len(support_cells[cell]))

# charge-allowed cells: does the cell contain ANY zero-weight triple at all?
from collections import defaultdict
byp = defaultdict(list)
for a in range(N):
    byp[piece[a]].append(a)
allowed = []
for cell in combinations_with_replacement(plist, 3):
    found = False
    # iterate distinct index triples consistent with the multiset
    import itertools
    for combo in itertools.product(*[byp[p] for p in cell]):
        if len(set(combo)) < 3:
            continue
        if tuple(sorted(piece[a] for a in combo)) != tuple(sorted(cell)):
            continue
        s = tuple(sum(wt[a][q] for a in combo) for q in range(6))
        if all(x == 0 for x in s):
            found = True
            break
    if found:
        allowed.append(cell)
print("[cells] cells allowed by the 6 Cartan charges alone:", len(allowed))
print("[cells] charge-allowed == coupled support:",
      sorted(allowed) == sorted(support_cells))
