#!/usr/bin/env python3
"""THE THREE-GENERATION READING (B1302 addendum): on Y_12's 768 one-triplet lines the configuration <N_g2> ALONE (no
flavon VEV, no nu^c VEV) pairs the two surviving triplets (N_g2 D_g0 Dbar_g1) and the other generations' Higgs doublets
(N_g2 H_u,g0 H_d,g1, N_g2 H_u,g1 H_d,g0) and leaves everything else massless: three generations of Q, u^c, d^c, L, e^c,
nu^c, one Higgs pair H_u,g2, H_d,g2, no exotic colour triplet -- the MSSM's field content with right-handed neutrinos,
vector-like (every field with its mirror), at tree level.  Its Yukawa couplings through the light Higgs pair carry the
family tensor |eps_{i j g2}|: the mass matrices after electroweak breaking couple generations g0 and g1 off-diagonally
and leave generation g2 massless (rank 2).  Computed with B1302's mass-matrix machinery on the six solved patterns."""
import sys, pathlib, random, collections
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import one_triplet_vacua as V

def main():
    rng = random.Random(3)
    fmt = lambda f: (f[0] if not f[0].startswith('m:') else f[0][2:] + "'") + str(f[1] + 1)
    results = {}
    for (g0, g1, g2) in ((0, 2, 1), (0, 1, 2), (2, 0, 1), (2, 1, 0), (1, 0, 2), (1, 2, 0)):
        s = {lab: (1, 1, 1) for lab in V.LABELS}
        s['D'] = tuple(1 if g == g0 else 0 for g in range(3)); s['Dbar'] = tuple(1 if g == g1 else 0 for g in range(3)); s['S'] = tuple(1 if g == g2 else 0 for g in range(3))
        cfg = (g2, None, None)
        lp, zr, zc = V.light_pairs(s, cfg, rng, names=True)
        results[(g0, g1, g2)] = (lp, zr, zc)
    (lp, zr, zc) = results[(0, 2, 1)]
    print("=== the one-triplet line (D in generation 1, Dbar in 3, N in 2) with <N_2> alone ===")
    print(f"  light pairs per sector: {lp}")
    print(f"  exactly massless, colour-triplet sector: rows {[fmt(f) for f in zr['T']]}, cols {[fmt(f) for f in zc['T']]}  (the three d^c pairs; no D, no Dbar)")
    print(f"  exactly massless, doublet sector: rows {[fmt(f) for f in zr['H']]}, cols {[fmt(f) for f in zc['H']]}  (the three lepton doublets and ONE Higgs pair, H_u2 H_d2)")
    print(f"  the flavon-only sectors Q, u^c, e^c: {lp['Q']}, {lp['u^c']}, {lp['e^c']} light pairs each (all three generations)")
    same = all(v[0] == lp for v in results.values())
    print(f"  the same counts for all six generation assignments: {same}")
    # the Yukawa structure through the light Higgs pair: |eps_{i j g2}| with the light Higgs of generation g2
    g2 = 1
    up = [[1 if len({i, j, g2}) == 3 else 0 for j in range(3)] for i in range(3)]
    print(f"  up-type Yukawa matrix Q_i u^c_j H_u,{g2 + 1} (family tensor |eps_{{i j {g2 + 1}}}|): {up}  -> rank 2, generation {g2 + 1} massless, generations {[g + 1 for g in range(3) if g != g2]} paired off-diagonally")
    ok = (lp == {'T': 3, 'H': 5, 'Q': 3, 'u^c': 3, 'e^c': 3} and same
          and sorted(fmt(f) for f in zr['T']) == ["d^c'1", "d^c'2", "d^c'3"]
          and sorted(fmt(f) for f in zr['H']) == sorted(["H_u2", "L'1", "L'2", "L'3", "H_d'2"]))
    return dict(lp=lp, ok=ok)

if __name__ == "__main__":
    out = main()
    print("\nSELFTEST:", "PASS" if out['ok'] else "FAIL")
    sys.exit(0 if out['ok'] else 1)
