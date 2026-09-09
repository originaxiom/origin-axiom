"""C6 -- fc R65: of B1264's 170 labellings c in {0,1,2}^6 (h_c = sum c_i omega_i^vee integral on the 27 and splitting it 9+9+9), the Kac class of
exp(2 pi i h_c / 3) by the dimension of its fixed subalgebra: 6 + #{roots alpha : <alpha, h_c> = 0 mod 3}. Own code from the E6 Cartan matrix only
(Bourbaki: chain 1-3-4-5-6, node 2 on 4). Expected (the seat): 80 labellings at dim 24 (A2^3) and 90 at dim 30 (D4 x T^2); colourings 40/45."""
import itertools, json
E = [(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)]; A = [[2 if i == j else 0 for j in range(6)] for i in range(6)]
for i, j in E: A[i-1][j-1] = A[j-1][i-1] = -1
def refl(lam, i):                       # s_i on weight (Dynkin-label) coordinates: lam - lam_i * alpha_i, alpha_i = row i of A
    return tuple(lam[k] - lam[i] * A[i][k] for k in range(6))
def orbit(start):
    seen = {start}; frontier = [start]
    while frontier:
        nxt = []
        for lam in frontier:
            for i in range(6):
                mu = refl(lam, i)
                if mu not in seen: seen.add(mu); nxt.append(mu)
        frontier = nxt
    return seen
roots = set()
for i in range(6): roots |= orbit(tuple(A[i]))
W27 = orbit((1, 0, 0, 0, 0, 0))
print("roots:", len(roots), " weights of the 27:", len(W27))
assert len(roots) == 72 and len(W27) == 27
# the centre: coweight classes z with <lambda, z> constant (non-zero) mod 3 on the 27 and 0 mod 3 on every root; a labelling and its central shifts
# c + z, c + 2z define the SAME automorphism of e6 and the same 9+9+9 partition (colours cyclically permuted) -- B1264 counts labellings modulo that
import itertools as it
centre = [d for d in it.product(range(3), repeat=6) if any(d) and len({sum(di * li for di, li in zip(d, lam)) % 3 for lam in W27}) == 1
          and all(sum(di * ai for di, ai in zip(d, a)) % 3 == 0 for a in roots)]
print("central shift vectors mod 3:", centre, " (expect two: z and 2z)")
assert len(centre) == 2
z = centre[0]
def shift(c, k): return tuple((ci + k * zi) % 3 for ci, zi in zip(c, z))
lab = []; dims = {}; seen = set()
for c in it.product(range(3), repeat=6):
    grades = [sum(ci * li for ci, li in zip(c, lam)) % 3 for lam in W27]
    if sorted(grades.count(g) for g in range(3)) != [9, 9, 9]: continue
    orb = {shift(c, k) for k in range(3)}; key = min(orb)
    if key in seen: continue
    seen.add(key)
    fixed = {6 + sum(1 for a in roots if sum(ci * ai for ci, ai in zip(cc, a)) % 3 == 0) for cc in orb}
    assert len(fixed) == 1, "the fixed dimension is not constant on a central orbit"
    fixed = next(iter(fixed)); lab.append((key, fixed)); dims[fixed] = dims.get(fixed, 0) + 1
print("labellings with a 9+9+9 grading, modulo the centre:", len(lab), " (B1264: 170)"); print("fixed-subalgebra dimensions:", dims, " (seat: {24: 80, 30: 90})")
col = {}
for c, d in lab:
    neg = tuple((-x) % 3 for x in c); negkey = min({shift(neg, k) for k in range(3)}); key = min(c, negkey); col.setdefault(key, set()).add(d)
coldims = {}
for k, ds in col.items():
    assert len(ds) == 1; d = next(iter(ds)); coldims[d] = coldims.get(d, 0) + 1
print("colourings (c ~ -c, modulo the centre):", len(col), " by dimension:", coldims, " (seat: 40 at 24, 45 at 30)")
ok = len(lab) == 170 and dims == {24: 80, 30: 90} and coldims == {24: 40, 30: 45}
json.dump(dict(labellings=len(lab), dims=dims, colourings=len(col), coldims=coldims, centre=centre, ok=ok), open("c_kac_classes.json", "w"), indent=1)
print("C6:", "PASS" if ok else "FAIL")
