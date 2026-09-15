#!/usr/bin/env python3
"""THE EXTENDED REGULATOR PROBE -- the certificate memo 143 reported and DID NOT COMMIT.

B1217's evidence-contract charge, upheld: "cloud's EXTENDED run -- the V-NEG headline itself --
is NOT REPRODUCIBLE AS COMMITTED. The file at outside_bench/certificates/vol_basis_extended.py
contains the BASIS BUILDER (R48-3), not the extended probe; no committed certificate carries the
involves_regulator gate."  Correct.  vol_basis_extended.py builds the basis and stops; the 216-cell
grid that produced memo 143's headline (108 raw / 0 involves_regulator) existed only inside a turn.

This file IS that probe.  It re-derives B1137's machinery from the PINNED commit (never a moving
ref), extends the pruned basis with the object's own complex volume, and re-runs the full grid with
the involves_regulator gate recomputed from the coefficients.

Gate 5: the 18 sealed B743 targets are loaded VERBATIM and enter only as comparison targets for a
computed negative.  Vol(m004) is COMPUTED from the Bloch-Wigner dilogarithm, never quoted.
"""
import os, sys, json, math, time, argparse, subprocess, glob
from concurrent.futures import ProcessPoolExecutor, as_completed

PAPER_PIN = "89affd5bbd4b900397af2bf3b987ff8f05f5cb80"
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
CACHE = os.path.join("/tmp", f"oa_b1137_{PAPER_PIN[:12]}")
NEED = ["frontier/B1137_regulator_probe", "frontier/B743_rung1_widened"]

def materialize():
    """B1137's modules at the PINNED commit, at the directory depth targets.py expects."""
    if os.path.isdir(os.path.join(CACHE, "frontier", "B1137_regulator_probe")):
        return
    os.makedirs(CACHE, exist_ok=True)
    names = [n for n in subprocess.run(["git","-C",REPO,"ls-tree","-r","--name-only",PAPER_PIN],
             capture_output=True, text=True).stdout.splitlines()
             if any(n.startswith(p) for p in NEED)]
    tar = subprocess.run(["git","-C",REPO,"archive",PAPER_PIN,*names], capture_output=True)
    subprocess.run(["tar","-x","-C",CACHE], input=tar.stdout, check=True)

materialize()
sys.path.insert(0, os.path.join(CACHE, "frontier", "B1137_regulator_probe"))
from mpmath import mp, mpf, pslq, nstr, polylog, exp, pi, mpc
import basis as basismod, targets as targetsmod, verify as verifymod

H_LIST = [100, 1000, 10000, 1000000]
D_LIST = [1, 2, 3]
MAXSTEPS = 4000
N_DIM_APPROX = 32                      # 28-entry extended basis + 1 + D

def dps_for_H(H):
    return max(100, int(math.ceil(1.3 * N_DIM_APPROX * math.log10(H))) + 40)

def vol_m004(dps):
    """Vol(4_1) = 2 * D(exp(i pi/3)), D the Bloch-Wigner dilogarithm.  On |z|=1 the log|z| term
    vanishes, so D(z) = Im Li_2(z).  COMPUTED, not quoted."""
    mp.dps = dps + 25
    return 2 * polylog(2, exp(mpc(0, 1) * pi / 3)).imag

def build(dps, extended):
    b, forms, _R = basismod.build_pruned_basis(dps=dps)
    keys = list(forms['FULL'])
    if extended:
        mp.dps = dps + 25
        V = vol_m004(dps)
        b = dict(b)
        b['vol']            = V
        b['vol_pinorm']     = V / pi
        b['vol_over_zetaK2'] = V / mp.mpf(b['zetaK_2'])
        keys = keys + ['vol', 'vol_pinorm', 'vol_over_zetaK2']
    return b, keys

def run_cell(args):
    V_str, digits, name, D, H, extended = args
    dps = dps_for_H(H)
    b, keys = build(dps, extended)
    mp.dps = dps + 25
    V = mpf(nstr(mpf(V_str), max(int(digits), 1)))
    vec = [mpf(1)] + [V**k for k in range(1, D+1)] + [mp.mpf(b[k]) for k in keys]
    tol = mpf(10) ** (-(dps - 10))
    t0 = time.time()
    rel = pslq(vec, maxcoeff=int(H), maxsteps=MAXSTEPS, tol=tol)
    r = {'name': name, 'D': D, 'H': H, 'dps': dps, 'n_dim': len(vec),
         'n_basis': len(keys), 'extended': extended, 'time': round(time.time()-t0, 1),
         'found': False, 'involves_V': False, 'involves_regulator': False}
    if rel is None or all(c == 0 for c in rel):
        return r
    c = [int(x) for x in rel]
    r['found'] = True; r['coeffs'] = c
    r['involves_V'] = any(x != 0 for x in c[1:1+D])
    # the gate, recomputed from coefficients exactly as B1137's aggregate.py does
    r['involves_regulator'] = any(x != 0 for x in c[1+D:])
    return r

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mode', choices=['control','extended','both'], default='both')
    ap.add_argument('--out', default=None)
    a = ap.parse_args()
    tg, sha = targetsmod.load_targets()
    print(f"sealed targets: {len(tg)}  sha256 {sha}")
    assert sha == "e93efeaa132bf7c1a6e0a3a9d41a436ff03d2aea5f626a2b404a5ef8a317e101", "TARGET SEAL BROKEN"
    print(f"Vol(m004) computed from Li_2 = {nstr(vol_m004(60), 30)}")
    modes = {'both': [False, True], 'control': [False], 'extended': [True]}[a.mode]
    allrows = []
    for ext in modes:
        jobs = [(t['value'], t['digits'], t['name'], D, H, ext)
                for t in tg for D in D_LIST for H in H_LIST]
        tag = "EXTENDED (28-entry basis, +vol)" if ext else "CONTROL (25-entry basis)"
        print(f"\n=== {tag}: {len(jobs)} cells ===", flush=True)
        rows = []
        with ProcessPoolExecutor(max_workers=4) as ex:
            for i, r in enumerate(as_completed([ex.submit(run_cell, j) for j in jobs]), 1):
                rr = r.result(); rows.append(rr); allrows.append(rr)
                if i % 12 == 0:
                    print(f"  {i}/{len(jobs)}  raw={sum(x['found'] for x in rows)}"
                          f"  reg={sum(x['involves_regulator'] for x in rows)}", flush=True)
        raw = sum(x['found'] for x in rows)
        iv  = sum(x['involves_V'] for x in rows)
        ir  = sum(x['involves_regulator'] for x in rows)
        tn  = len({x['name'] for x in rows if x['involves_regulator']})
        print(f"RESULT {tag}: cells={len(rows)} raw={raw} involves_V={iv} "
              f"involves_regulator={ir} targets_with_regulator={tn}", flush=True)
    if a.out:
        json.dump(allrows, open(a.out, 'w'), indent=1)
    print("\nDONE")

if __name__ == '__main__':
    main()
