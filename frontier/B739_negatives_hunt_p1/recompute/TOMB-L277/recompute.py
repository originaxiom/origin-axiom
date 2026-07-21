"""B739 Stage-B recompute — TOMB-L277 (TOMBSTONES.md K-O, speculations/TOMBSTONES.md:L277).

BANKED KILL (kill_form: base-rate): the golden "trace leak" tr rho_{SU(2)_3}(A) = -1/phi is
NOT a distinguished signal, because in the finite image (order 2880) the asserted counts are
1350/2880 ~ 47% nonzero-trace and 384/2880 ~ 13% golden-magnitude (|phi^{+-1}|) trace — the
seed sits in a POPULATED class. fact_basis was ASSERTED: no script or committed artifact for
the 2880 trace enumeration exists anywhere in the repo (B210's dual_mckay.py computes only
the image ORDER 2880). This script re-derives the discriminating fact from scratch.

DISCRIMINATING FACT (the fact that, if true, kills the claim):
  in the image of the SU(2)_3 modular representation (order 2880),
  (a) the number of elements with nonzero trace is 1350 (~47%), and
  (b) the number of elements with golden-magnitude trace |tr| in {phi, 1/phi} is 384 (~13%),
  with the seed's trace exactly -1/phi, so the seed's trace class is populated, not a
  singleton — "distinguished by nonvanishing golden trace" fails.

DECLARED CONVENTIONS (E1) — taken from the arc's own declarations where they exist
(frontier/B210_dual_mckay_hyperbolic/dual_mckay.py, wrt_image_order_su2_3), re-declared
explicitly where the tombstone left them implicit:
  C1. SU(2)_3 modular data (B210's convention, k=3, n=k+2=5, rank 4, q = e^{2 pi i/5}):
        S_{ab} = sqrt(2/5) sin(pi (a+1)(b+1)/5),  a,b = 0..3
        T = diag exp(2 pi i (h_a - c/24)),  h_a = a(a+2)/(4n),  c = 3k/(k+2) = 9/5.
  C2. rho: SL(2,Z) -> U(4) by s |-> S, t |-> T where s = [[0,-1],[1,0]], t = [[1,1],[0,1]].
      Well-definedness is VERIFIED below: S^2 = I exactly (sympy) and (ST)^3 = I to 1e-50
      (60-digit evalf), i.e. the SL(2,Z) presentation relations s^4 = 1, (st)^3 = s^2 hold
      (the rep in this normalization factors through PSL(2,Z); traces of words are therefore
      well-defined class functions).
  C3. The seed A = RL = [[2,1],[1,1]] (the golden cat map), with R = t, L = s t^{-1} s^{-1}
      (standard: s t s^{-1} = L^{-1}). Trace is conjugation-invariant, so the choice of word
      decomposition is immaterial.
  C4. "Finite image" = the multiplicative closure <S, T> (B210's object, banked order 2880).
  C5. "Nonzero trace" = |tr| > tol; "golden-magnitude" = min(||tr|-phi|, ||tr|-1/phi|) < tol,
      with tol = 1e-6 — STRICTLY |phi^{+-1}| per the tombstone's wording (the image also
      contains |tr| = 2/phi = sqrt5-1 and 2 phi = sqrt5+1 clusters; those are NOT counted).
      Robustness of the tolerance is demonstrated by the printed cluster table (min gap
      between distinct |tr| clusters >> tol, max within-cluster residual << tol).
  C6. Enumeration: deterministic BFS over left-multiplication by (S, T), numpy complex128,
      dedup key = entries rounded to 5 decimals (B210's own key convention).
  C7. Class level: conjugacy classes computed as orbits under conjugation by the generators;
      trace constancy on each class is asserted, and the element-level golden count is
      cross-checked against the sum of golden-class sizes.

Deterministic: no wall-clock, no randomness, no network. Environment: python3 + numpy + sympy.
Gate 5: pure representation theory / group theory; no SM quantities anywhere.
"""
import numpy as np
import sympy as sp

# ---------------------------------------------------------------- exact layer (sympy)
n = 5
Ssym = sp.Matrix(4, 4, lambda i, j: sp.sqrt(sp.Rational(2, n)) * sp.sin(sp.pi * (i + 1) * (j + 1) / n))
hsym = [sp.Rational(a * (a + 2), 4 * n) for a in range(4)]
csym = sp.Rational(9, 5)
Tsym = sp.diag(*[sp.exp(2 * sp.pi * sp.I * (hsym[a] - csym / 24)) for a in range(4)])
Tsym_inv = sp.diag(*[1 / Tsym[a, a] for a in range(4)])

# relation s^2-check: S^2 == I exactly (hence S^-1 = S, S^4 = I)
assert sp.simplify(Ssym * Ssym - sp.eye(4)) == sp.zeros(4, 4), "S^2 != I"
print("EXACT: S^2 = I (sympy)  -> S^{-1} = S, S^4 = I")

# relation (ST)^3 == I: 60-digit residual (full symbolic simplify is slow; residual is decisive)
rel = (Ssym * Tsym) ** 3 - sp.eye(4)
res_rel = max(abs(complex(rel[i, j].evalf(60))) for i in range(4) for j in range(4))
assert res_rel < 1e-50, f"(ST)^3 != I, residual {res_rel}"
print(f"VERIFIED: max |(ST)^3 - I| entry = {res_rel:.3e} (60-digit evalf) -> SL(2,Z) relations hold")

# the seed trace, EXACT: rho(RL) = T S T^{-1} S^{-1} = T S T^{-1} S
seed_sym = Tsym * Ssym * Tsym_inv * Ssym
tr_seed_exact = sp.simplify(sp.expand_complex(sp.expand(sp.trace(seed_sym))))
target = (1 - sp.sqrt(5)) / 2  # = -1/phi
assert sp.simplify(tr_seed_exact - target) == 0, f"seed trace != -1/phi: {tr_seed_exact}"
print(f"EXACT: tr rho(RL) = {tr_seed_exact} = (1-sqrt5)/2 = -1/phi  (sympy, exact)")

# ---------------------------------------------------------------- numeric layer (numpy)
k = 3
a = np.arange(4)
S = np.sqrt(2 / n) * np.sin(np.pi * np.outer(a + 1, a + 1) / n)
h = a * (a + 2) / (4 * n)
c = 3 * k / (k + 2)
T = np.diag(np.exp(2j * np.pi * (h - c / 24)))
I4 = np.eye(4)
Tinv = np.conj(T)          # T unitary diagonal
Sinv = S                   # S^2 = I (exact, above)
assert np.allclose(S @ S.conj().T, I4) and np.allclose(T @ T.conj().T, I4), "generators not unitary"

def key(M):
    return tuple(np.round(M.flatten(), 5))   # B210's dedup convention (C6)

# BFS closure of <S,T>
seen = {key(I4): 0}
elems = [I4]
frontier = [I4]
while frontier:
    nf = []
    for M in frontier:
        for g in (S, T):
            P = M @ g
            kk = key(P)
            if kk not in seen:
                seen[kk] = len(elems)
                elems.append(P)
                nf.append(P)
    frontier = nf
order = len(elems)
print(f"\nIMAGE ORDER |<S,T>| = {order}   (banked: 2880)  {'MATCH' if order == 2880 else 'MISMATCH'}")

# closure sanity: products of every element with each generator stay inside
assert all(key(elems[i] @ g) in seen for i in range(order) for g in (S, T)), "not closed"
print("VERIFIED: closure under right-multiplication by both generators (group confirmed)")

# ---------------------------------------------------------------- the trace census
phi = (1 + np.sqrt(5)) / 2
tol = 1e-6
traces = np.array([np.trace(M) for M in elems])
abst = np.abs(traces)

# cluster table: distinct |tr| values with multiplicities + separation diagnostics
clusters = {}
for v in abst:
    ck = round(float(v), 6)
    clusters.setdefault(ck, []).append(float(v))
ckeys = sorted(clusters)
print("\n|tr| cluster table (value : multiplicity):")
for ck in ckeys:
    print(f"  {ck:>9.6f} : {len(clusters[ck]):>4}")
gaps = [ckeys[i + 1] - ckeys[i] for i in range(len(ckeys) - 1)]
spread = max(max(vs) - min(vs) for vs in clusters.values())
print(f"cluster separation: min inter-cluster gap = {min(gaps):.6f}, "
      f"max within-cluster spread = {spread:.2e}  (tol = {tol:.0e} sits safely between)")

n_zero = int(np.sum(abst <= tol))
n_nonzero = int(np.sum(abst > tol))
n_golden = int(np.sum((np.abs(abst - phi) < tol) | (np.abs(abst - 1 / phi) < tol)))
print(f"\nTHE DISCRIMINATING COUNTS (banked: 1350/2880 nonzero ~47%; 384/2880 golden-magnitude ~13%):")
print(f"  nonzero trace      : {n_nonzero}/{order} = {100*n_nonzero/order:.2f}%   "
      f"{'MATCH' if n_nonzero == 1350 else 'MISMATCH'}")
print(f"  zero trace         : {n_zero}/{order} = {100*n_zero/order:.2f}%")
print(f"  golden |phi^(+-1)| : {n_golden}/{order} = {100*n_golden/order:.2f}%   "
      f"{'MATCH' if n_golden == 384 else 'MISMATCH'}")

# the seed inside the image
seed = T @ S @ Tinv @ Sinv
kseed = key(seed)
assert kseed in seen, "seed not in enumerated image"
tr_seed = np.trace(seed)
print(f"\nseed rho(RL): trace = {tr_seed.real:+.12f}{tr_seed.imag:+.2e}j   (-1/phi = {-1/phi:.12f})")
n_same_value = int(np.sum(np.abs(traces - (-1 / phi)) < tol))
print(f"elements with trace EXACTLY -1/phi (the seed's value): {n_same_value}  -> value class populated")

# ---------------------------------------------------------------- class level (C7)
Sidx_inv, Tidx_inv = S.conj().T, T.conj().T   # unitary: inverse = conjugate transpose
class_of = {}
classes = []
for i in range(order):
    if i in class_of:
        continue
    cid = len(classes)
    orbit = [i]
    class_of[i] = cid
    fr = [i]
    while fr:
        nf = []
        for j in fr:
            M = elems[j]
            for g, gi in ((S, Sidx_inv), (T, Tidx_inv)):
                cidx = seen[key(g @ M @ gi)]
                if cidx not in class_of:
                    class_of[cidx] = cid
                    orbit.append(cidx)
                    nf.append(cidx)
        fr = nf
    classes.append(orbit)
assert sum(len(o) for o in classes) == order, "class partition broken"
# trace constant on each class
for o in classes:
    ts = traces[o]
    assert np.max(np.abs(ts - ts[0])) < 1e-9, "trace not constant on a conjugacy class"
n_classes = len(classes)
golden_cls = [o for o in classes
              if abs(abs(traces[o[0]]) - phi) < tol or abs(abs(traces[o[0]]) - 1 / phi) < tol]
assert sum(len(o) for o in golden_cls) == n_golden, "class-level vs element-level golden count mismatch"
seed_cid = class_of[seen[kseed]]
seed_cls_size = len(classes[seed_cid])
same_val_cls = {class_of[i] for i in range(order) if abs(traces[i] - (-1 / phi)) < tol}
print(f"\nCLASS LEVEL: {n_classes} conjugacy classes; {len(golden_cls)} classes carry "
      f"golden-magnitude trace (sum of sizes = {n_golden}, cross-check MATCH)")
print(f"  the seed's conjugacy class: id {seed_cid}, size {seed_cls_size} "
      f"(a singleton would need size 1 AND a unique trace)")
print(f"  conjugacy classes sharing the seed's exact trace -1/phi: {len(same_val_cls)}")

# ---------------------------------------------------------------- per-element side-claims
L = S @ Tinv @ Sinv          # rho(L) = S T^{-1} S^{-1}
for name, M in (("RRL", T @ T @ L), ("RLL", T @ L @ L)):
    t = np.trace(M)
    print(f"side-claim tr rho({name}) = {t.real:+.2e}{t.imag:+.2e}j   "
          f"(tombstone: exactly 0) {'MATCH' if abs(t) < tol else 'MISMATCH'}")

# ---------------------------------------------------------------- verdict summary
print("\nSUMMARY vs the banked kill (TOMBSTONES K-O):")
print(f"  image order        : recomputed {order}    banked 2880")
print(f"  nonzero trace      : recomputed {n_nonzero} ({100*n_nonzero/order:.1f}%)  banked 1350 (~47%)")
print(f"  golden magnitude   : recomputed {n_golden} ({100*n_golden/order:.1f}%)   banked 384 (~13%)")
print(f"  seed trace         : recomputed -1/phi (EXACT, sympy)      banked -1/phi")
print(f"  seed class populated: {n_same_value} elements / {len(same_val_cls)} classes share the exact value; "
      f"{len(golden_cls)} classes are golden-magnitude")
ok = (order == 2880 and n_nonzero == 1350 and n_golden == 384 and n_same_value > 1)
print(f"KILL {'RECONFIRMED' if ok else 'NOT REPRODUCED'}: nonvanishing golden trace is a populated, "
      f"base-rate-heavy property; it does not single out the seed.")
