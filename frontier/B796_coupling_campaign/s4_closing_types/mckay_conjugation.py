r"""S4's falsifying test: is CONJUGATION the same F2 bit as TAU?

S4 typed the five closings and matched each to a source, with one link left as
a typing judgement rather than a theorem:

    conjugation (the observer torsor's first bit, B766)  <->  tau (E6's unique
    order-2 diagram automorphism, B963)

Both are order 2. If they are the same bit, the closing budget shuts as a
theorem. If not, the conjugation bit is NOT the chirality resource, a source is
missing, and S4's headline is false.

THE ROUTE IS McKAY. 2T = the binary tetrahedral group sits in SU(2); McKay
sends its irreps to the nodes of the AFFINE E6 diagram, with dimension = mark.
Complex conjugation of representations, V -> V*, permutes the irreps, hence
permutes the nodes. The question is whether that permutation IS tau.

METHOD, all computed here, nothing assumed:
  1. build 2T explicitly as 24 unit quaternions -> SU(2) matrices
  2. conjugacy classes, and the character of the defining rep V2
  3. all 7 irreps: 3 one-dim from the abelianisation Z/3, V2 and its two
     twists, and V3 from 2⊗2 = 3+1
  4. the McKay graph by decomposing V_i ⊗ V2 with character inner products
  5. CHECK it is affine E6 (7 nodes, marks 1,1,1,2,2,2,3, star of 3 arms)
  6. the conjugation permutation, from chi -> conj(chi)
  7. is it a graph automorphism? of order 2? with tau's cycle type --
     two transpositions, three fixed points, swapping two arms?

Gate 5-Q. Structure only.
"""
import itertools

import numpy as np

# ---------------------------------------------------------------- 1. build 2T
def quats():
    """The 24 unit Hurwitz quaternions = the binary tetrahedral group."""
    out = []
    for s in (1, -1):
        out += [(s, 0, 0, 0), (0, s, 0, 0), (0, 0, s, 0), (0, 0, 0, s)]
    for signs in itertools.product((1, -1), repeat=4):
        out.append(tuple(s * 0.5 for s in signs))
    return out


def q2m(q):
    """Unit quaternion -> SU(2) matrix."""
    a, b, c, d = q
    return np.array([[a + 1j * b, c + 1j * d],
                     [-c + 1j * d, a - 1j * b]], dtype=complex)


G = [q2m(q) for q in quats()]
assert len(G) == 24
# closure check
def find(m, L, tol=1e-9):
    for i, x in enumerate(L):
        if np.allclose(x, m, atol=tol):
            return i
    return -1

assert all(find(a @ b, G) >= 0 for a in G for b in G), '2T must be closed'

# ------------------------------------------------- 2. conjugacy classes
classes, seen = [], set()
for i, g in enumerate(G):
    if i in seen:
        continue
    cl = {find(x @ g @ np.linalg.inv(x), G) for x in G}
    classes.append(sorted(cl))
    seen |= cl
sizes = [len(c) for c in classes]
reps = [G[c[0]] for c in classes]
k = len(classes)
print(f'2T: order {len(G)}, conjugacy classes {k}, sizes {sizes}')
assert k == 7, 'binary tetrahedral has 7 classes'

# ------------------------------------------------- 3. the seven characters
chi2 = np.array([np.trace(r) for r in reps])          # defining rep V2

# the three 1-dim reps come from 2T -> 2T/Q8 = Z/3
# an element's image is determined by its order-3 part; read it off the trace
# of the 3-dim rep instead: build the abelianisation directly.
comm = set()
for a in G:
    for b in G:
        comm.add(find(a @ b @ np.linalg.inv(a) @ np.linalg.inv(b), G))
Q8 = sorted(comm)
assert len(Q8) == 8, f'commutator subgroup should be Q8, got {len(Q8)}'
cosets = []
for i, g in enumerate(G):
    tag = frozenset(find(g @ G[j], G) for j in Q8)
    if tag not in [c[0] for c in cosets]:
        cosets.append((tag, i))
assert len(cosets) == 3
w = np.exp(2j * np.pi / 3)
def coset_index(gi):
    tag = frozenset(find(G[gi] @ G[j], G) for j in Q8)
    return [c[0] for c in cosets].index(tag)

chi1 = [np.array([1.0 + 0j] * k),
        np.array([w ** coset_index(c[0]) for c in classes]),
        np.array([w ** (2 * coset_index(c[0])) for c in classes])]
# order the two nontrivial ones canonically
chi1a, chi1b = chi1[1], chi1[2]

chi2b, chi2c = chi2 * chi1a, chi2 * chi1b            # the two twists of V2
chi3 = chi2 * chi2 - chi1[0]                          # 2⊗2 = 3 + 1

CH = [chi1[0], chi1a, chi1b, chi2, chi2b, chi2c, chi3]
NAMES = ['1', 'w', 'w2', 'V2', 'V2w', 'V2w2', 'V3']
DIMS = [int(round(abs(c[0]).real)) for c in CH]
print(f'irrep dimensions (McKay marks): {DIMS}')


def inner(a, b):
    return sum(s * x * np.conj(y) for s, x, y in zip(sizes, a, b)) / len(G)


# orthonormality — the character table must be right before anything is built
M = np.array([[inner(a, b) for b in CH] for a in CH])
assert np.allclose(M, np.eye(7), atol=1e-8), 'characters must be orthonormal'
print('character table verified orthonormal (7x7)')

# ------------------------------------------------- 4. the McKay graph
A = np.zeros((7, 7), dtype=int)
for i, ci in enumerate(CH):
    prod = ci * chi2
    for j, cj in enumerate(CH):
        A[i, j] = int(round(inner(prod, cj).real))
print('\nMcKay adjacency (V_i tensor V2 decomposed):')
for i in range(7):
    print('   ', NAMES[i].rjust(4), A[i])

# ------------------------------------------------- 5. is it affine E6?
assert (A == A.T).all(), 'McKay graph must be symmetric'
deg = A.sum(1)
assert sorted(DIMS) == [1, 1, 1, 2, 2, 2, 3], 'marks must be affine E6'
centre = DIMS.index(3)
assert deg[centre] == 3, 'the mark-3 node is the trivalent centre'
assert sorted(deg) == [1, 1, 1, 2, 2, 2, 3], f'affine E6 degrees, got {sorted(deg)}'
print('\nAFFINE E6 CONFIRMED: 7 nodes, marks 1,1,1,2,2,2,3, trivalent centre')

# ------------------------------------------------- 6. conjugation on nodes
perm = []
for i, ci in enumerate(CH):
    conj = np.conj(ci)
    j = max(range(7), key=lambda t: inner(conj, CH[t]).real)
    perm.append(j)
print(f'\nconjugation V -> V* permutes nodes: {perm}')
print('   ', ' '.join(f'{NAMES[i]}->{NAMES[perm[i]]}' for i in range(7)))

# ------------------------------------------------- 7. is it tau?
is_auto = all(A[i, j] == A[perm[i], perm[j]] for i in range(7) for j in range(7))
order2 = all(perm[perm[i]] == i for i in range(7))
fixed = [NAMES[i] for i in range(7) if perm[i] == i]
swaps = sorted({tuple(sorted((NAMES[i], NAMES[perm[i]]))) for i in range(7)
                if perm[i] != i})
print(f'\n  graph automorphism : {is_auto}')
print(f'  order 2            : {order2}')
print(f'  fixed nodes        : {fixed}')
print(f'  transpositions     : {swaps}')

verdict = (is_auto and order2 and len(swaps) == 2 and len(fixed) == 3)
print('\n' + '=' * 62)
if verdict:
    print('VERDICT: CONJUGATION *IS* TAU.')
    print('  order-2 diagram automorphism, two transpositions, three fixed')
    print('  nodes -- exactly tau\'s cycle type (B963: swaps two node pairs).')
    print('  It swaps two arms of the affine E6 star and fixes the third')
    print('  plus the centre. S4\'s budget closes as a theorem.')
else:
    print('VERDICT: NOT TAU -- S4\'s headline is FALSIFIED.')
print('=' * 62)
