import sympy as sp
from collections import deque, Counter
import itertools

# E6 Cartan matrix, same as B299 (symmetric, simply-laced)
C = sp.Matrix([[2, -1, 0, 0, 0, 0], [-1, 2, -1, 0, 0, 0], [0, -1, 2, -1, 0, -1],
               [0, 0, -1, 2, -1, 0], [0, 0, 0, -1, 2, 0], [0, 0, -1, 0, 0, 2]])
assert C == C.T, "Cartan matrix must be symmetric (simply-laced normalization)"

THETA = sp.Matrix([[0, -1, 1, 0, 0, 0], [1, -1, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0],
                   [0, 0, 1, 0, -1, 0], [0, 0, 0, 1, -1, 0], [0, 0, 0, 0, 0, 1]])
PHI = sp.Matrix([[1, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, -2], [0, 0, 1, 0, 0, -3],
                 [0, 0, 1, -1, 1, -2], [0, 0, 1, -1, 0, -1], [0, 0, 1, 0, 0, -2]])

# --- 1. Generate the full E6 root system by reflection-closure from the 6 simple roots ---
def reflect(v, i):
    # s_i(v) = v - (Cv)_i * e_i   (C symmetric, simply-laced => (v,alpha_i)=(Cv)_i)
    Cv_i = sum(C[i, j] * v[j] for j in range(6))
    v2 = list(v)
    v2[i] -= Cv_i
    return tuple(v2)

simple = [tuple(1 if k == i else 0 for k in range(6)) for i in range(6)]
roots = set(simple)
q = deque(simple)
while q:
    v = q.popleft()
    for i in range(6):
        w = reflect(v, i)
        if w not in roots:
            roots.add(w)
            q.append(w)

print("Total roots generated:", len(roots))
assert len(roots) == 72, f"expected 72 roots, got {len(roots)}"

def is_pos(v):
    s = [x for x in v if x != 0]
    return all(x > 0 for x in s)  # E6 simply-laced: coeffs all same sign

pos_roots = [v for v in roots if is_pos(v)]
print("Positive roots:", len(pos_roots))
assert len(pos_roots) == 36

def height(v):
    return sum(v)

heights = Counter(height(v) for v in pos_roots)
print("Height histogram:", dict(sorted(heights.items())))

surv3 = [v for v in pos_roots if height(v) % 3 == 0]
print("height%3==0 positive roots:", len(surv3))
assert len(surv3) == 9

def form(v, w):
    return sum(v[i] * C[i, j] * w[j] for i in range(6) for j in range(6))

# connected components via nonzero pairing (as B305 did)
import networkx as nx
G = nx.Graph()
G.add_nodes_from(range(9))
for i in range(9):
    for j in range(i + 1, 9):
        if form(surv3[i], surv3[j]) != 0:
            G.add_edge(i, j)
comps = list(nx.connected_components(G))
comp_sizes = sorted(len(c) for c in comps)
print("Components of the 9 height%3==0 roots:", comp_sizes)
assert comp_sizes == [3, 3, 3], "expected A2 x A2 x A2"

blocks = [sorted(c) for c in comps]  # 3 blocks of root-indices into surv3
print("Blocks (indices into surv3):", blocks)

# --- 2. Check theta, phi preserve the FULL 72-root system, and derive their action on the 9 special roots ---
def act_root(M, v):
    # candidate action on root-coefficient-vectors: v -> M*v (since M^T C M = C tested for weight-basis identity)
    vv = sp.Matrix(v)
    r = M * vv
    return tuple(int(x) for x in r)

for name, M in [("theta", THETA), ("phi", PHI)]:
    bad = [v for v in roots if act_root(M, v) not in roots]
    print(f"{name}: preserves full 72-root system:", len(bad) == 0, "(", len(bad), "violations )")

# also check M^T C M == C (bilinear form preserved) -- this licenses acting directly on root vectors
for name, M in [("theta", THETA), ("phi", PHI)]:
    print(f"{name}: M^T C M == C :", (M.T * C * M) == C)

# --- 3. action on the 9 special roots -> permutation of the 3 blocks ---
print("\nNOTE: theta/phi are generic INNER (Weyl-group) elements, not diagram automorphisms")
print("(neither maps the 6 simple roots to signed simple roots) -- so the naive v->Mv action")
print("does NOT in general preserve the POSITIVE root system. Testing directly:")
surv3_idx = {v: i for i, v in enumerate(surv3)}
for name, M in [("theta", THETA), ("phi", PHI)]:
    ok = True
    img = {}
    for i, v in enumerate(surv3):
        w = act_root(M, v)
        if w not in surv3_idx:
            ok = False
    print(f"{name}: naive root action v->Mv preserves the 9 positive special roots as a set:", ok)
print("(this diagnostic is NOT required for the actual claim below, which uses the intrinsic")
print(" weight-space block assignment + the already-validated Dynkin/dual action on the 27)")

# --- 4. Now the 27 weights & their orbits under theta, phi (reuse B299 logic) ---
E6_CARTAN = C
def weights_27():
    seen = {(1, 0, 0, 0, 0, 0)}
    q = deque(seen)
    while q:
        mu = q.popleft()
        for i in range(6):
            if mu[i] == 1:
                nu = tuple(mu[j] - E6_CARTAN[i, j] for j in range(6))
                if nu not in seen:
                    seen.add(nu); q.append(nu)
    return list(seen)

W27 = weights_27()
assert len(W27) == 27
Wset = set(W27)

def action_on_dynkin(M):
    A = E6_CARTAN * M * E6_CARTAN.inv()
    return sp.Matrix(6, 6, lambda i, j: int(A[i, j]))

def act_weight(A, mu):
    return tuple(sum(A[i, j] * mu[j] for j in range(6)) for i in range(6))

# --- 5. block-id of a weight: which of the 3 A2 blocks is it TRIVIAL under? ---
# pairing (mu, alpha) for alpha = sum v_j alpha_j (simply-laced, Dynkin-normalized) = sum_j v_j * mu_j
def pairing(mu, v):
    return sum(v[j] * mu[j] for j in range(6))

def weight_block(mu):
    trivial_blocks = []
    for bi, b in enumerate(blocks):
        if all(pairing(mu, surv3[i]) == 0 for i in b):
            trivial_blocks.append(bi)
    return trivial_blocks

block_assignment = {}
bad_weights = []
for mu in W27:
    tb = weight_block(mu)
    if len(tb) != 1:
        bad_weights.append((mu, tb))
    else:
        block_assignment[mu] = tb[0]

print("\nWeights with ambiguous/non-unique trivial-block (expect 0):", len(bad_weights))
if bad_weights[:5]:
    print("  examples:", bad_weights[:5])

print("Block-id distribution over the 27:", Counter(block_assignment.values()) if len(bad_weights)==0 else "N/A (ambiguous cases exist)")

# --- 6. orbit structure + block-id pattern per orbit, for theta and phi ---
def orbits(M):
    A = action_on_dynkin(M)
    seen = set(); orbs = []
    for mu in W27:
        if mu in seen: continue
        orb = [mu]; cur = act_weight(A, mu)
        while cur != mu:
            orb.append(cur); cur = act_weight(A, cur)
        seen.update(orb); orbs.append(orb)
    return orbs

if len(bad_weights) == 0:
    for name, M in [("theta", THETA), ("phi", PHI)]:
        orbs = orbits(M)
        sizes = Counter(len(o) for o in orbs)
        print(f"\n{name}: {len(orbs)} orbits, sizes {dict(sizes)}")
        per_orbit_blocks = []
        all_match = True
        for o in orbs:
            bl = sorted(block_assignment[mu] for mu in o)
            per_orbit_blocks.append(bl)
            if bl != [0, 1, 2]:
                all_match = False
        print(f"{name}: every orbit hits all 3 blocks exactly once (multiset == [0,1,2]):", all_match)
        print(f"{name}: sample orbit block-multisets:", per_orbit_blocks[:3], "...")
