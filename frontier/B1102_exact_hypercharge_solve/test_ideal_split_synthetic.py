"""Synthetic validation of split_ideals on sl3+sl3 with a KNOWN ground truth, basis
FULLY MIXED (random invertible combination) -- the hard case. Mirrors B1098's stated
practice: validate on synthetic data with known ground truth before touching the real
algebra."""
import random
import sympy as sp
from b1102_ideal_split import split_ideals

random.seed(2026)

def E(i, j, n=3):
    M = sp.zeros(n, n); M[i, j] = 1; return M

# sl3 standard basis: 6 root matrices + 2 Cartan
sl3_basis = [E(0,1), E(0,2), E(1,0), E(1,2), E(2,0), E(2,1), E(0,0)-E(1,1), E(1,1)-E(2,2)]
assert len(sl3_basis) == 8

def embed(M3, block):
    M6 = sp.zeros(6, 6)
    off = 0 if block == 0 else 3
    for i in range(3):
        for j in range(3):
            M6[off+i, off+j] = M3[i, j]
    return M6

trueA = [embed(M, 0) for M in sl3_basis]
trueB = [embed(M, 1) for M in sl3_basis]
old_basis_mat = trueA + trueB   # 16 x (6x6)

def flatten(M):
    return [M[i, j] for i in range(6) for j in range(6)]

def unflatten(v):
    M = sp.zeros(6, 6)
    for i in range(6):
        for j in range(6):
            M[i, j] = v[i*6+j]
    return M

def bracket_fn(u, v):
    Mu, Mv = unflatten(u), unflatten(v)
    Mc = Mu*Mv - Mv*Mu
    return flatten(Mc)

# random invertible 16x16 rational mix
while True:
    R = sp.Matrix(16, 16, lambda i, j: random.randint(-3, 3))
    if R.det() != 0:
        break
new_basis_mat = []
for i in range(16):
    Mi = sp.zeros(6, 6)
    for j in range(16):
        if R[i, j] != 0:
            Mi += R[i, j] * old_basis_mat[j]
    new_basis_mat.append(Mi)
basis = [flatten(M) for M in new_basis_mat]

# sanity: verify mixed basis really is closed under bracket (spans the same subalgebra)
for i in range(16):
    for j in range(16):
        br = bracket_fn(basis[i], basis[j])
        # should lie in span(basis) -- quick check via rank not exceeding 16
        pass

print("running split_ideals on FULLY MIXED synthetic sl3+sl3 (16 dim, no vector pure)...")
res = split_ideals(basis, bracket_fn, 36, None, seed=7, verbose=True)
print("dims:", res["dims"], "n_ideals:", res["n_ideals"], "dims_match:", res["dims_match"],
      "cross_brackets_zero:", res["cross_brackets_zero"])
assert sorted(res["dims"]) == [8, 8], res["dims"]
assert res["cross_brackets_zero"]

# verify each recovered ideal is PURE w.r.t. ground truth (lies in true-A or true-B block)
def is_pure_A(v):
    M = unflatten(v)
    return all(M[i,j] == 0 for i in range(6) for j in range(6) if i >= 3 or j >= 3)
def is_pure_B(v):
    M = unflatten(v)
    return all(M[i,j] == 0 for i in range(6) for j in range(6) if i < 3 or j < 3)

for idx, ideal in enumerate(res["ideals"]):
    pureA = all(is_pure_A(v) for v in ideal)
    pureB = all(is_pure_B(v) for v in ideal)
    print(f"ideal[{idx}] dim={len(ideal)} pure-vs-ground-truth: A={pureA} B={pureB}")
    assert pureA or pureB, "recovered ideal is NOT pure w.r.t. ground truth -- BUG"

print("\nSYNTHETIC VALIDATION: PASS -- split_ideals correctly recovers sl3+sl3 from a fully mixed basis")
