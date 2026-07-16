#!/usr/bin/env python3
"""
D3 track (ii) -- SEALED prereg d3_child/PREREG_D3.md (sha256 75d69af3...).
Twisted-bundle family Z(T^n A1) at E6 levels k=1..8, n=-6..6.

Repo <seat-workdir>/origin-axiom is READ-ONLY and is NOT touched by this
script (all sources below live under seat-work/). PYTHONDONTWRITEBYTECODE=1 is
set by the caller shell before invocation.

-------------------------------------------------------------------------------
IDENTITY -- symbolic derivation (verify BEFORE relying on it):

  Let T = diag(t_a) (t_a = zeta_{12K}^{T_expo[a]}) and let S be the (symmetric,
  unitary) modular S-matrix. Define rho := T^2 S T (banked convention, engine.py
  docstring + mp_odd_blocks: `rho = T * T * S * T`).

  Since T is diagonal, diagonal powers commute by exponent addition:
      T^n * rho = T^n * (T^2 S T) = T^(n+2) S T                      ... (1)
  Cyclicity of trace, Tr(ABC) = Tr(CAB), with A=T^(n+2), B=S, C=T:
      Tr(T^n rho) = Tr(T^(n+2) S T) = Tr(T * T^(n+2) * S) = Tr(T^(n+3) S)   ... (2)
  T^(n+3) is diagonal, so only the diagonal of S survives the trace:
      Tr(T^(n+3) S) = sum_a (T^(n+3))_aa S_aa = sum_a t_a^(n+3) S_aa       ... (3)

  => Tr(T^n rho) = sum_a t_a^(n+3) S_aa.   QED -- matches the prereg's cheap
  identity verbatim. Note only diag(S) and the t_a ever enter; no off-diagonal
  S entries are needed.

  This is ALSO checked numerically below (not just argued symbolically): a
  prototyping run (not part of the banked log) built k=1,2,3 fresh with the
  engine's own dense S,T,rho (S_float/T_float/run_gates) and confirmed
  Tr(T^n rho) computed densely agrees with the sum_a t_a^(n+3) S_aa shortcut
  to float64 precision (~1e-15) at n in {-6,-3,-1,0,1,2,5,6}; and for k=4..8 a
  full dense S was rebuilt from the *entire* counts tensor (not just the
  diagonal+row0 the shortcut uses) and Tr(T^n rho) again matched the shortcut
  to ~1e-15. This script re-derives those same per-level match numbers below
  (see CROSS-CHECK section) so the evidence is in this run's own log, at
  dps=40 as specified.

-------------------------------------------------------------------------------
S NORMALIZATION (engine.py / prereg, verbatim):
  U[a,b]   = sum_e counts[a,b,e] * zeta_{M6}^e         (M6 = 6K)
  S        = U / sqrt( (U U^dagger)[0,0].real )
  sign fix: S = -S if S[0,0].real < 0.

  (U U^dagger)[0,0] = sum_b U[0,b] * conj(U[0,b]) depends only on row U[0,:].
  S_aa = sign * U[a,a] / norm depends only on U[a,a].
  => only diag(U) and row U[0,:] are ever read from `counts`.

-------------------------------------------------------------------------------
Sources:
  k=1..3 : rebuilt fresh, engine.Level(k, W, eps) -- L.counts, L.T_expo.
  k=4..7 : <seat-workdir>/seat-work/level_ladder_campaign/outputs/level{k}_blocks.npz
  k=8    : <seat-workdir>/seat-work/proof_queue/q1_level8/outputs/level8_blocks.npz
  (keys: counts (N,N,M6) int64, T_expo (N,) int64)

GATE: n=0 must reproduce banked Z(A1), k=1..8 = {1,1,1,0,1,1,2,1}, to 1e-8
(real; imag < 1e-8). Hard stop on failure.
"""
import json
import math
import sys
import time
from fractions import Fraction

import numpy as np
import mpmath as mp

ENGINE_SCRIPTS = "<seat-workdir>/seat-work/level_ladder_campaign/scripts"
sys.path.insert(0, ENGINE_SCRIPTS)
from engine import Level, weyl_group  # noqa: E402

WORKDIR = "<seat-workdir>/seat-work/loops_queue/d3_child"
NPZ_PATHS = {
    4: "<seat-workdir>/seat-work/level_ladder_campaign/outputs/level4_blocks.npz",
    5: "<seat-workdir>/seat-work/level_ladder_campaign/outputs/level5_blocks.npz",
    6: "<seat-workdir>/seat-work/level_ladder_campaign/outputs/level6_blocks.npz",
    7: "<seat-workdir>/seat-work/level_ladder_campaign/outputs/level7_blocks.npz",
    8: "<seat-workdir>/seat-work/proof_queue/q1_level8/outputs/level8_blocks.npz",
}

BANKED_Z_A1 = {1: 1, 2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 7: 2, 8: 1}   # n=0 gate target
ORD_T_GIVEN = {1: 12, 2: 84, 3: 180, 4: 48, 5: 204, 6: 108, 7: 228, 8: 60}
N_RANGE = list(range(-6, 7))
DPS = 40


def lcm(a, b):
    return a * b // math.gcd(a, b)


def order_of_T(T_expo, twelveK):
    """ord(T) = lcm_a( twelveK / gcd(twelveK, T_expo[a]) ), skipping T_expo[a]=0 (order 1)."""
    ordT = 1
    for e in T_expo:
        e = int(e) % twelveK
        if e == 0:
            continue
        m = twelveK // math.gcd(twelveK, e)
        ordT = lcm(ordT, m)
    return ordT


def U_entry_mp(row, zpow):
    """mpmath sum_e row[e] * zpow[e], row a 1-D int64 array, zpow precomputed zeta_M6 powers."""
    return mp.fsum((int(c) * zpow[j] for j, c in enumerate(row) if c))


def compute_level(k, log):
    t0 = time.time()
    if k <= 3:
        W, eps = weyl_group()
        L = Level(k, W, eps)
        counts, T_expo = L.counts, L.T_expo
        source = f"fresh engine build (Level({k}, W, eps))"
    else:
        d = np.load(NPZ_PATHS[k])
        counts, T_expo = d["counts"], d["T_expo"]
        source = NPZ_PATHS[k]

    N, M6 = counts.shape[0], counts.shape[2]
    K = M6 // 6
    assert M6 == 6 * K, f"M6={M6} not divisible by 6 at k={k}"
    twelveK = 12 * K
    assert T_expo.shape[0] == N

    mp.mp.dps = DPS
    zpow = [mp.e ** (2j * mp.pi * j / M6) for j in range(M6)]

    U_diag = [U_entry_mp(counts[a, a, :], zpow) for a in range(N)]
    U_row0 = [U_entry_mp(counts[0, b, :], zpow) for b in range(N)]
    assert abs(U_row0[0] - U_diag[0]) < mp.mpf("1e-30"), "U[0,0] mismatch diag vs row0 extraction"

    norm2 = mp.fsum([(U_row0[b] * mp.conj(U_row0[b])).real for b in range(N)])
    norm = mp.sqrt(norm2)
    sign = 1 if mp.re(U_diag[0] / norm) > 0 else -1
    S_diag = [sign * U_diag[a] / norm for a in range(N)]

    t_a = [mp.e ** (2j * mp.pi * int(e) / twelveK) for e in T_expo]

    Z = {}
    for n in N_RANGE:
        val = sum((t_a[a] ** (n + 3)) * S_diag[a] for a in range(N))
        Z[n] = (float(mp.re(val)), float(mp.im(val)))

    ordT_computed = order_of_T(T_expo, twelveK)

    # ---- CROSS-CHECK: independent float64 dense reconstruction from the SAME counts,
    # using the FULL U matrix (not just diag+row0), confirming the shortcut identity.
    z64 = np.exp(2j * np.pi * np.arange(M6) / M6)
    Ufull = counts @ z64
    norm64 = np.sqrt((Ufull @ Ufull.conj().T)[0, 0].real)
    Sfull = Ufull / norm64
    if Sfull[0, 0].real < 0:
        Sfull = -Sfull
    Tdiag64 = np.exp(2j * np.pi * T_expo / twelveK)
    rho64 = (Tdiag64 ** 2)[:, None] * Sfull * Tdiag64[None, :]
    dense_diag_dev = float(np.max(np.abs(np.array([complex(s) for s in S_diag]) - np.diag(Sfull))))
    cross_ns = (-6, -3, 0, 1, 6)
    cross = {}
    for n in cross_ns:
        shortcut64 = sum((Tdiag64[a] ** (n + 3)) * complex(S_diag[a]) for a in range(N))
        dense64 = np.trace(np.diag(Tdiag64 ** n) @ rho64)
        cross[n] = (complex(shortcut64), complex(dense64), abs(shortcut64 - dense64))

    dt = time.time() - t0
    log.append(f"\n===== k={k}  (source: {source}) =====")
    log.append(f"  N={N}  M6={M6}  K={K}  12K={twelveK}  [build+compute {dt:.2f}s]")
    log.append(f"  ord(T): computed={ordT_computed}  given={ORD_T_GIVEN[k]}  match={ordT_computed == ORD_T_GIVEN[k]}")
    log.append(f"  cross-check: max|S_diag(mpmath shortcut) - diag(full dense float64 S)| = {dense_diag_dev:.3e}")
    for n in cross_ns:
        sc, de, diff = cross[n]
        log.append(f"    n={n:+d}: shortcut(dps40->c128)={sc:.10f}  dense(full-U,float64)={de:.10f}  diff={diff:.2e}")
    re0, im0 = Z[0]
    gate_ok = abs(re0 - BANKED_Z_A1[k]) < 1e-8 and abs(im0) < 1e-8
    log.append(f"  GATE n=0: Z={re0:+.12f}{im0:+.2e}i  banked={BANKED_Z_A1[k]}  PASS={gate_ok}")
    assert gate_ok, f"GATE FAILURE at k={k}: Z(n=0)={Z[0]} vs banked {BANKED_Z_A1[k]}"

    return Z, ordT_computed, N


def main():
    log = []
    log.append("D3 track (ii) run -- twisted-bundle family Z(T^n A1), E6 levels k=1..8, n=-6..6")
    log.append("prereg: d3_child/PREREG_D3.md sha256 75d69af324b7598efbaf459a737e4c681244ce2816f98d4e9358420399aac484")
    log.append(f"mpmath dps = {DPS}")
    log.append("identity: Tr(T^n rho) = sum_a t_a^(n+3) S_aa  [rho = T^2 S T; derivation + numeric cross-check in module docstring]")

    table = {}
    ordT_all = {}
    for k in range(1, 9):
        Z, ordT, N = compute_level(k, log)
        table[k] = Z
        ordT_all[k] = ordT

    log.append("\n===== GATE SUMMARY =====")
    log.append("All 8 levels PASS n=0 vs banked ladder {1,1,1,0,1,1,2,1} (real match <1e-8, imag <1e-8).")

    log.append("\n===== FULL TABLE (re, im), n=-6..6 =====")
    header = "k\\n  " + "  ".join(f"{n:+3d}" for n in N_RANGE)
    log.append(header)
    for k in range(1, 9):
        row = "  ".join(f"{table[k][n][0]:+.4f}" for n in N_RANGE)
        log.append(f"k={k}  " + row)
        imrow = "  ".join(f"{table[k][n][1]:+.2e}" for n in N_RANGE)
        log.append(f"     im: " + imrow)

    # ---- periodicity statement ----
    log.append("\n===== (a) TRIVIAL PERIODICITY n mod ord(T_k) =====")
    for k in range(1, 9):
        log.append(f"  k={k}: ord(T_k)={ORD_T_GIVEN[k]} (computed {ordT_all[k]}, match={ordT_all[k]==ORD_T_GIVEN[k]});"
                    f" Z(n) is periodic in n with period {ORD_T_GIVEN[k]} by construction"
                    f" (t_a^(n+3) depends on n only through n mod ord(t_a) | ord(T_k)).")
        if ORD_T_GIVEN[k] <= 12:
            log.append(f"    -> within n=-6..6 (span 12) this FORCES Z(-6)=Z(6) at k={k}"
                        f" (since -6 == 6 mod {ORD_T_GIVEN[k]}).")
        else:
            log.append(f"    -> ord(T_k)={ORD_T_GIVEN[k]} > 12, so NO two distinct n in -6..6 are forced"
                        f" to coincide by this periodicity alone.")
    # verify the k=1 forced coincidence numerically
    diff16 = complex(*table[1][-6]) - complex(*table[1][6])
    log.append(f"  numeric check k=1: Z(-6)-Z(6) = {diff16:.2e} (expect ~0, forced by ord(T_1)=12)")

    # ---- mod-5 analysis ----
    log.append("\n===== (b) MOD-5 SUBSTRUCTURE TEST =====")
    log.append("Grouping n=-6..6 by n mod 5 (Python convention): "
                "class0={-5,0,5} class1={-4,1,6} class2={-3,2} class3={-2,3} class4={-6,-1,4}")
    classes = {c: [n for n in N_RANGE if n % 5 == c] for c in range(5)}
    ZERO_TOL = 1e-6
    for k in range(1, 9):
        log.append(f"\n  -- k={k} (ord(T_k)={ORD_T_GIVEN[k]}, 5|ord(T_k) = {ORD_T_GIVEN[k] % 5 == 0}) --")
        supp_by_class = {}
        for c, ns in classes.items():
            entries = []
            for n in ns:
                re, im = table[k][n]
                is_zero = abs(re) < ZERO_TOL and abs(im) < ZERO_TOL
                entries.append((n, re, im, is_zero))
            supp_pattern = tuple(e[3] for e in entries)
            supp_by_class[c] = supp_pattern
            vals_str = ", ".join(f"n={n}:{'0' if z else f'{re:+.4f}'}" for n, re, im, z in entries)
            log.append(f"    class n%5={c} {ns}: {vals_str}")
        uniform_support = all(len(set(p)) == 1 for p in supp_by_class.values())
        # check whether nonzero values within a class are numerically equal to each other
        equal_within_class = True
        for c, ns in classes.items():
            vals = [complex(*table[k][n]) for n in ns]
            nz = [v for v in vals if abs(v) >= ZERO_TOL]
            if len(nz) >= 2:
                spread = max(abs(v - nz[0]) for v in nz)
                if spread > 1e-6:
                    equal_within_class = False
        log.append(f"    each class internally zero/nonzero-uniform: {uniform_support}")
        log.append(f"    nonzero values EQUAL within each class (extra structure candidate): {equal_within_class}")
        verdict = "NO-EXTRA-STRUCTURE" if not equal_within_class else "CANDIDATE-STRUCTURE-SEE-VALUES"
        log.append(f"    verdict k={k}: {verdict}")

    return table, log


if __name__ == "__main__":
    table, log = main()
    for line in log:
        print(line)

    # ---- bank outputs ----
    out_table = {str(k): {str(n): list(table[k][n]) for n in N_RANGE} for k in range(1, 9)}
    with open(f"{WORKDIR}/d3ii_table.json", "w") as f:
        json.dump(out_table, f, indent=1)
    with open(f"{WORKDIR}/d3ii_run.log", "w") as f:
        f.write("\n".join(log) + "\n")
    print("\nBANKED: d3ii_table.json, d3ii_run.log")
