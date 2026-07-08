#!/usr/bin/env python3
"""B478 — the +j asymmetry identified: is the two-world defect exactly a clock
translation? Claim to test: Par.D(m,c).Par = D(m,c) . Z^{cm} where Z = diag(zeta^j),
i.e. the chirality defect of the metallic letter m is a lattice translation by cm."""
import numpy as np, sys
N = 15
z = np.exp(2j*np.pi/N)
Par = np.zeros((N,N),complex)
for j in range(N): Par[(-j)%N, j] = 1
Z = np.diag([z**j for j in range(N)])
ok = True
for c in (1, 14, 2, 4):
    for m in (1, 2, 3):
        D = np.diag([z**((c*m*(j*(j-1)//2)) % N) for j in range(N)])
        lhs = Par @ D @ Par
        rhs = D @ np.linalg.matrix_power(Z, (c*m) % N)
        err = np.max(np.abs(lhs - rhs))
        ok &= err < 1e-12
        print(f"c={c:2d} m={m}: ||Par D Par - D Z^(cm)|| = {err:.2e}")
print("THE +j DEFECT IS EXACTLY THE CLOCK TRANSLATION Z^(cm):", "VERIFIED" if ok else "FAILS")
sys.exit(0 if ok else 1)
