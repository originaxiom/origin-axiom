"""Listening card 13 (main, 2026-11-25; data-free): lambda*, exactly. W+ on the largest orbit over the common point mod 81 as an
integer matrix; its characteristic polynomial (FLINT, exact) factored over Z; the irreducible factor with a root at 1.915298;
its degree, coefficients and roots; and the factor's value at lambda*^2 (the +- pair's field). See ../CARD.md.
    python3 -B identify.py > identify_run.txt"""
import sys, pathlib, numpy as np, flint, time
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
src = (next((ROOT / "frontier").glob("B1996_*")) / "verification" / "tower_decay.py").read_text().split("t0 = time.time()")[0]
ns = {}; exec(src, ns); orbits = ns["orbits_over_common_point"]
t0 = time.time()
N, n, Lm, Rm, roots = orbits(3, 4)
r, c = np.unique(roots, return_counts=True); big = r[np.argmax(c)]; mem = np.nonzero(roots == big)[0]; m = len(mem)
loc = -np.ones(n, dtype=int); loc[mem] = np.arange(m)
W = [[0] * m for _ in range(m)]
for j, i in enumerate(mem):
    W[loc[Lm[i]]][j] += 1; W[loc[Rm[i]]][j] += 1
M = flint.fmpz_mat(W)
cp = M.charpoly()
print("I1: mod 81, largest orbit %d; characteristic polynomial of degree %d computed exactly  [%.0f s]" % (m, cp.degree(), time.time() - t0), flush=True)
content, facs = cp.factor()
print("I1: its factorisation over Z: %d distinct irreducible factors; degrees with multiplicities %s" % (len(facs), sorted(((f.degree(), e) for f, e in facs), reverse=True)[:20]), flush=True)
target = 1.915298164734
best = None
for f, e in facs:
    rts = np.roots([int(x) for x in reversed(f.coeffs())]) if f.degree() > 0 else []
    for z in rts:
        if abs(z - target) < 1e-6:
            best = (f, e, rts)
if best:
    f, e, rts = best
    print("I2: lambda* is a root of an irreducible factor of degree %d (multiplicity %d in the characteristic polynomial)" % (f.degree(), e))
    print("I2: its coefficients (constant term first): %s" % [int(x) for x in f.coeffs()])
    print("I2: its roots: %s" % sorted([complex(round(z.real, 9), round(z.imag, 9)) for z in rts], key=lambda z: (-abs(z), z.real)))
    even = all(int(c_) == 0 for k, c_ in enumerate(f.coeffs()) if k % 2 == 1)
    print("I2: the factor is a polynomial in lambda^2: %s" % even)
    if even:
        half = flint.fmpz_poly([int(c_) for k, c_ in enumerate(f.coeffs()) if k % 2 == 0])
        print("J2: lambda*^2 = %.12f is a root of the degree-%d polynomial (constant first): %s; irreducible: %s" % (target ** 2, half.degree(), [int(x) for x in half.coeffs()], len(half.factor()[1]) == 1 and half.factor()[1][0][1] == 1))
else:
    print("I2: no factor has a root within 1e-6 of 1.915298")
