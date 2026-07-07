#!/usr/bin/env python3
"""B455 (Ethogram E3) — integrate the curve: finite deformations along the E6 moduli.

Engine (per prereg): the adjoint realization. rho0 = Ad(principal(rho_geo)) as 78x78,
built from B351's exact brackets (ad matrices) + the principal-sl2 chain basis; H^1
directions per Sym-block from the Fox/relator linearization (the B445 formulation);
Newton continuation rho(a)=expm(ad_u) R0, rho(b)=expm(ad_v) S0 on the relator residual.

Run: python3 integrate.py  > run_log.txt      (gates -> m=1 run gate -> the five directions)
"""
import math
import os
import sys
import time

import numpy as np
from scipy.linalg import expm, logm, lstsq

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "B351_exact_e6_chevalley"))
import exact_e6 as E6

import snappy

EXPONENTS = [1, 4, 5, 7, 8, 11]
RELATOR = "abbbaBAAB"
TMAX, DT0 = 1.0, 0.1
CEILING_S = 3600


# ---------------- the chain basis (B352's construction, re-derived) ----------------
def chains():
    e, h, f = E6.principal_sl2()
    kern = E6._nullspace(E6._ad_matrix(e))
    by_m = {}
    for v in kern:
        p = next(iter(v))
        w = int(E6.brk(h, v).get(p, 0) / v[p])
        by_m[w // 2] = v
    assert sorted(by_m) == EXPONENTS
    out = {}
    for m, v in by_m.items():
        c = [v]
        for _ in range(2 * m):
            c.append(E6.brk(f, c[-1]))
        assert not E6.brk(f, c[-1])
        out[m] = c
    return out


CH = chains()
# S: columns = chain vectors (root coords) -> the block basis; order blocks by EXPONENTS
COLS = [(m, k) for m in EXPONENTS for k in range(2 * m + 1)]
S = np.zeros((78, 78))
for j, (m, k) in enumerate(COLS):
    col = np.zeros(78)
    for i, c in CH[m][k].items():
        col[i] = float(c)
    S[:, j] = col / np.linalg.norm(col)          # normalized: raw chains are factorially skewed
Sinv = np.linalg.inv(S)
assert np.linalg.cond(S) < 1e6, np.linalg.cond(S)

# ad matrices for the sl2 triple (exact -> float)
E_, H_, F_ = E6.principal_sl2()
adE = np.array([[float(c) for c in row] for row in E6._ad_matrix(E_)])
adH = np.array([[float(c) for c in row] for row in E6._ad_matrix(H_)])
adF = np.array([[float(c) for c in row] for row in E6._ad_matrix(F_)])

# ad matrix for an arbitrary root-coord vector (complex)
AD_BASIS = None


def build_ad_basis():
    global AD_BASIS
    AD_BASIS = np.zeros((78, 78, 78))
    for j in range(78):
        M = E6._ad_matrix({j: 1})
        for r in range(78):
            row = M[r]
            for cidx in range(78):
                if row[cidx]:
                    AD_BASIS[j, r, cidx] = float(row[cidx])


def ad_of(vec):
    """ad of a complex root-coord vector via the precomputed basis ads."""
    return np.tensordot(vec, AD_BASIS, axes=(0, 0))


# ---------------- rho0 from SnapPy holonomy ----------------
def holonomy(name):
    M = snappy.ManifoldHP(name)
    G = M.fundamental_group()
    def cl(x):
        return complex(str(x.real()).replace(' ', '')) + 1j * float(str(x.imag()).replace(' ', ''))
    mats = {}
    for g in G.generators():
        A = G.SL2C(g)
        mats[g] = np.array([[complex(float(A[i, j].real()), float(A[i, j].imag()))
                             for j in range(2)] for i in range(2)])
    return mats, G.relators()[0]


def sl2_to_e6_ad(M2):
    """Ad(principal(M2)) as 78x78 (root coords): expm(ad(xi_E6)), xi = logm(M2)."""
    xi = logm(M2)
    # xi = alpha e + beta h + gamma f in sl2 basis e=[[0,1],[0,0]], h=diag(1,-1), f=[[0,0],[1,0]]
    alpha, gamma = xi[0, 1], xi[1, 0]
    beta = xi[0, 0]
    adxi = alpha * adE + beta * adH + gamma * adF
    return expm(adxi)


def sym_power(M, n):
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    dim = n + 1
    out = np.zeros((dim, dim), dtype=complex)
    for k in range(dim):
        p1 = np.array([math.comb(n - k, i) * a ** (n - k - i) * c ** i for i in range(n - k + 1)])
        p2 = np.array([math.comb(k, j) * b ** (k - j) * d ** j for j in range(k + 1)])
        col = np.convolve(p1, p2)
        out[:, k] = col
    return out


# ---------------- H^1 directions per block (Fox/relator linearization) ----------------
def rep_of(letter, mats):
    g = letter.lower()
    R = mats[g]
    return np.linalg.inv(R) if letter.isupper() else R


def h1_direction_vec(mats, relator, m):
    """The correct (vector-valued) block cocycle: z: {a,b} -> C^{2m+1};
    relator condition: sum_k Ad-prefix_k z(letter_k) = 0, with z(g^-1) = -Sym(rho(g^-1)) z(g)."""
    reps = {g: sym_power(mats[g], 2 * m) for g in mats}
    dim = 2 * m + 1
    rows = np.zeros((dim, 2 * dim), dtype=complex)
    pref = np.eye(dim, dtype=complex)
    for letter in relator:
        g = letter.lower()
        Rg = reps[g] if letter.islower() else np.linalg.inv(reps[g])
        blockcol = 0 if g == 'a' else 1
        if letter.islower():
            coeff = pref
        else:
            coeff = -pref @ Rg
        rows[:, blockcol * dim:(blockcol + 1) * dim] += coeff
        pref = pref @ Rg
    # Z^1 = kernel of rows (dim x 2dim); B^1 = {(R_a - I)w, (R_b - I)w}
    U, sv, Vh = np.linalg.svd(rows)
    null = Vh.conj().T[:, dim:]                       # 2dim - rank >= dim+? kernel dim = 2dim - rank
    rank = int(np.sum(sv > 1e-8 * sv[0]))
    null = Vh.conj().T[:, rank:]
    B = np.zeros((2 * dim, dim), dtype=complex)
    B[:dim, :] = reps['a'] - np.eye(dim)
    B[dim:, :] = reps['b'] - np.eye(dim)
    QB, _ = np.linalg.qr(B)
    # H^1 rep: null vector minus its B^1 projection, largest residual
    best, bestn = None, 0
    for j in range(null.shape[1]):
        v = null[:, j]
        w = v - QB @ (QB.conj().T @ v)
        if np.linalg.norm(w) > bestn:
            bestn, best = np.linalg.norm(w), w
    z = best / np.linalg.norm(best)
    return z[:dim], z[dim:]                            # (z_a, z_b) block-vectors


def block_vec_to_root(zvec, m):
    """embed a Sym^{2m}-block vector into 78-dim root coords via the chain basis."""
    out = np.zeros(78, dtype=complex)
    j0 = COLS.index((m, 0))
    for k in range(2 * m + 1):
        out += zvec[k] * S[:, j0 + k]
    return out


# ---------------- the continuation ----------------
def relator_matrix(Ra, Rb, relator):
    Ma = {'a': Ra, 'b': Rb, 'A': np.linalg.inv(Ra), 'B': np.linalg.inv(Rb)}
    M = np.eye(78, dtype=complex)
    for letter in relator:
        M = M @ Ma[letter]
    return M


def residual(u, v, R0, S0, relator):
    Ra = expm(ad_of(u)) @ R0
    Rb = expm(ad_of(v)) @ S0
    return (relator_matrix(Ra, Rb, relator) - np.eye(78)).flatten(), Ra, Rb


def newton(u, v, R0, S0, relator, tol=1e-10, itmax=12):
    n = 78
    for it in range(itmax):
        r, Ra, Rb = residual(u, v, R0, S0, relator)
        rn = np.linalg.norm(r) / max(np.linalg.norm(Ra), 1.0)
        if rn < tol:
            return u, v, rn, True
        # finite-difference Jacobian (156 complex params)
        J = np.zeros((len(r), 156), dtype=complex)
        h = 1e-7
        for j in range(78):
            du = np.zeros(78, dtype=complex)
            du[j] = h
            J[:, j] = (residual(u + du, v, R0, S0, relator)[0] - r) / h
            J[:, 78 + j] = (residual(u, v + du, R0, S0, relator)[0] - r) / h
        step, *_ = lstsq(J, -r, lapack_driver='gelsy')
        u = u + step[:78]
        v = v + step[78:]
    r, _, _ = residual(u, v, R0, S0, relator)
    return u, v, np.linalg.norm(r), False


def continue_direction(m, mats, relator, R0, S0, label, tmax=TMAX):
    za, zb = h1_direction_vec(mats, relator, m)
    ra, rb = block_vec_to_root(za, m), block_vec_to_root(zb, m)
    t, dt = 0.0, DT0
    u = np.zeros(78, dtype=complex)
    v = np.zeros(78, dtype=complex)
    halvings = 0
    history = []
    t0 = time.time()
    while t < tmax - 1e-12:
        tt = min(t + dt, tmax)
        useed = u + (tt - t) * ra
        vseed = v + (tt - t) * rb
        un, vn, rn, ok = newton(useed, vseed, R0, S0, relator)
        if ok:
            t, u, v = tt, un, vn
            dt = min(dt * 1.3, DT0)
            Ra = expm(ad_of(u)) @ R0
            offblock = offblock_norm(Ra)
            history.append((t, float(np.trace(Ra).real), float(np.trace(Ra).imag), offblock, rn))
            print(f"   [{label} m={m}] t={t:.3f} tr={np.trace(Ra):.6f} offblock={offblock:.3e} res={rn:.1e}",
                  flush=True)
        else:
            dt /= 2
            halvings += 1
            if halvings > 4:
                print(f"   [{label} m={m}] WALL at t*={t:.4f} (4 halvings, res {rn:.1e})", flush=True)
                return dict(direction=m, verdict="WALL", t_star=t, history=history)
        if time.time() - t0 > CEILING_S / 6:
            print(f"   [{label} m={m}] ceiling hit at t={t:.3f}", flush=True)
            return dict(direction=m, verdict="CEILING", t_star=t, history=history)
    return dict(direction=m, verdict="COMPONENT-FOUND", t_star=t, history=history)


def offblock_norm(R):
    """departure from block-diagonal (the sl2-factored locus) in the chain basis."""
    Rb = Sinv @ R @ S
    total = 0.0
    j = 0
    for m in EXPONENTS:
        d = 2 * m + 1
        blk = Rb[j:j + d, j:j + d].copy()
        Rb[j:j + d, j:j + d] = 0
        j += d
    return float(np.linalg.norm(Rb) / np.linalg.norm(R))


def main():
    print("== E3 engine build ==", flush=True)
    build_ad_basis()
    mats, relator = holonomy('4_1')
    print(f"relator: {relator}", flush=True)
    R0 = sl2_to_e6_ad(mats['a'])
    S0 = sl2_to_e6_ad(mats['b'])
    # GATE i: block-diagonal + matches Sym blocks
    ob = offblock_norm(R0)
    Rb = Sinv @ R0 @ S
    j0 = COLS.index((1, 0))
    blk = Rb[j0:j0 + 3, j0:j0 + 3]
    sym2 = sym_power(mats['a'], 2)
    # compare up to the chain-basis normalization: traces must agree
    g1 = abs(np.trace(blk) - np.trace(sym2)) < 1e-6
    print(f"GATE i: offblock(R0)={ob:.2e} (must ~0); Sym^2 trace match: {g1}", flush=True)
    # GATE ii: relator residual at rho0
    r0 = np.linalg.norm(relator_matrix(R0, S0, relator) - np.eye(78))
    print(f"GATE ii: relator residual at rho0 = {r0:.2e} (relative {r0/np.linalg.norm(R0):.2e})", flush=True)
    ok_gates = ob < 1e-10 and g1 and (r0 / np.linalg.norm(R0)) < 1e-10
    if not ok_gates:
        print("ENGINE GATES FAILED - no runs.", flush=True)
        return
    # RUN GATE: m=1 (geometric) must stay block-diagonal along the continuation
    print("== run gate: m=1 (the A-polynomial direction) ==", flush=True)
    g = continue_direction(1, mats, relator, R0, S0, "4_1", tmax=0.4)
    maxoff = max(h[3] for h in g['history']) if g['history'] else 1.0
    gate_pass = g['verdict'] in ("COMPONENT-FOUND", "WALL") and maxoff < 1e-6 and len(g['history']) >= 2
    print(f"run gate: verdict={g['verdict']} max offblock={maxoff:.2e} -> {'PASS' if gate_pass else 'FAIL'}",
          flush=True)
    if not gate_pass:
        print("RUN GATE FAILED - stopping per prereg.", flush=True)
        return
    # THE PROBE: the five non-geometric directions
    results = [g]
    for m in [4, 5, 7, 8, 11]:
        print(f"== direction m={m} ==", flush=True)
        results.append(continue_direction(m, mats, relator, R0, S0, "4_1"))
    # CONTROL: 5_2, gate + two directions
    print("== control: 5_2 ==", flush=True)
    mats2, rel2 = holonomy('5_2')
    R02 = sl2_to_e6_ad(mats2['a'])
    S02 = sl2_to_e6_ad(mats2['b'])
    r02 = np.linalg.norm(relator_matrix(R02, S02, rel2) - np.eye(78))
    print(f"5_2 gates: relator residual {r02:.2e}", flush=True)
    for m in [1, 4, 8]:
        results.append(continue_direction(m, mats2, rel2, R02, S02, "5_2",
                                          tmax=0.4 if m == 1 else TMAX))
    import json
    json.dump([{k: (v if k != 'history' else v[-3:]) for k, v in r.items()} for r in results],
              open('landings.json', 'w'), indent=1, default=str)
    print("[landings.json written]", flush=True)


if __name__ == '__main__':
    main()
