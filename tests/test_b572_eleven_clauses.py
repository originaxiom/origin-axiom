"""B572 — the eleven-clause chain, adjudicated: the three locks.

  (1) V1 REFUTED: the 27's principal height multiset has mult 2 at heights +-1 and
      +-4 (the handoff's V3+V7+V17 predicts 3 and 1) — branching is V17+V9+V1;
      corrected tr_27(rho(ab)) = 647707.5 + 876344.096...i at tr_2 = (5+sqrt(-3))/2.
  (2) THE WELD: chi_27(z) = chi_27(1/z) exactly — 27 and 27bar have the SAME
      character on any SL(2)-factored rep (the holonomy cannot distinguish them;
      what sigma does is move the POINT, i.e. conj(tr_27) != tr_27).
  (3) THE SINE KERNEL: S_odd of E6 level 2 = -i * (2/sqrt7)[sin(2 pi s t/7)],
      identity ordering, and S_odd^2 = -I. (S-block only; T-phases E6-specific.)
See frontier/B572_eleven_clauses/FINDINGS.md.
"""
import importlib.util
import os
from collections import Counter

import numpy as np
import sympy as sp

_spec = importlib.util.spec_from_file_location(
    "c3mod", os.path.join(os.path.dirname(__file__), "..",
                          "frontier", "B570_allowed_plays", "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(c3)

C6 = sp.Matrix([[2, 0, -1, 0, 0, 0], [0, 2, 0, -1, 0, 0], [-1, 0, 2, -1, 0, 0],
                [0, -1, -1, 2, -1, 0], [0, 0, 0, -1, 2, -1], [0, 0, 0, 0, -1, 2]])


def test_v1_branching_refuted():
    G6 = C6.inv()
    seen = {tuple(G6[:, 0])}
    frontier = [G6[:, 0]]
    while frontier:
        new = []
        for v in frontier:
            for j in range(6):
                pj = sum(C6[i, j] * v[i] for i in range(6))
                u = sp.Matrix(v)
                u[j] = v[j] - pj
                tu = tuple(u)
                if tu not in seen:
                    seen.add(tu)
                    new.append(u)
        frontier = new
    rho6 = sum([G6[:, j] for j in range(6)], sp.zeros(6, 1))
    hc = Counter(sp.Rational((sp.Matrix(m).T * C6 * rho6)[0, 0]) for m in seen)
    assert hc[1] == hc[-1] == 2          # V3+V7+V17 would give 3
    assert hc[4] == hc[-4] == 2          # V3+V7+V17 would give 1
    assert hc[8] == hc[-8] == 1 and hc[0] == 3
    # corrected clause-8 value at the banked Galois point
    t = (5 + sp.sqrt(-3)) / 2
    z = sp.symbols('z')
    zv = sp.solve(z + 1 / z - t, z)[0]
    chi27 = sum(sum(zv**(k - 2 * j) for j in range(k + 1)) for k in (16, 8, 0))
    val = complex(sp.N(chi27, 20))
    assert abs(val.real - 647707.5) < 1e-6
    assert abs(val.imag - 876344.0964696) < 1e-4


def test_weld_27_equals_27bar_on_sl2():
    z = sp.symbols('z')
    chi = sum(sum(z**(k - 2 * j) for j in range(k + 1)) for k in (16, 8, 0))
    assert sp.simplify(chi - chi.subs(z, 1 / z)) == 0    # 27 = 27bar as characters here
    # while sigma moves the point: the value at the geometric point is non-real
    t = (5 + sp.sqrt(-3)) / 2
    zv = sp.solve(sp.symbols('w') + 1 / sp.symbols('w') - t, sp.symbols('w'))[0]
    val = complex(sp.N(chi.subs(z, zv), 20))
    assert abs(val.imag) > 1e5


def test_sine_kernel_identity():
    W, eps = c3.weyl_group()
    rho_w = c3.root_coords([1] * 6)
    sh = [c3.root_coords(p) + rho_w for p in c3.PRIM]
    S = np.zeros((9, 9), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), np.array(sh))
    for a in range(9):
        for b in range(a, 9):
            ips = Wl[:, a, :] @ (c3.C @ sh[b])
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / c3.KH))
    S /= np.sqrt((S @ S.conj().T)[0, 0].real)
    if S[0, 0].real < 0:
        S = -S
    odd = np.zeros((9, 3))
    for j, (a, b) in enumerate([(1, 2), (3, 4), (7, 8)]):
        odd[a, j], odd[b, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
    S_odd = odd.T @ S @ odd
    M = np.array([[np.sin(2 * np.pi * s * t / 7) for t in (1, 2, 3)]
                  for s in (1, 2, 3)]) * 2 / np.sqrt(7)
    assert np.allclose(M @ M, np.eye(3), atol=1e-12)          # the kernel is an involution
    assert np.linalg.norm(S_odd - (-1j) * M) < 1e-9           # the identity, natural ordering
    assert np.allclose(S_odd @ S_odd, -np.eye(3), atol=1e-9)  # = conjugation on the odd sector
