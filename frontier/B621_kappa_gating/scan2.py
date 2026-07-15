"""kappa-gating scan v2: test the SUMMED (signed) reflection-coset Gauss
sum  R(word,kap) = sum_{(pm,wi) in REFL x {+-1}} sg(wi) * tr(rho_Weil . P)
-- the actual reflection-coset contribution to Z -- rather than individual
terms, to strip the ambient/generic sqrt(3) leakage (from the A2 lattice's
own e^{2pi i/3} content) that contaminates a non-squarefree base like 12.
Also compute the identity+rotation ('other') coset sum as a control.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import time
import numpy as np
from scan import weil_ops, rho_weil, WEYL, REFL, fit_sqrt

WORDS = {"RL": 3, "RRL": 4, "RRRL": 5}

def coset_sums(word, T, S, perms):
    M = rho_weil(word, T, S)
    refl_sum = 0j
    other_sum = 0j
    for (pm, wi), (P, sg) in perms.items():
        v = np.trace(M @ P)
        if wi in REFL:
            refl_sum += sg * v
        else:
            other_sum += sg * v
    return refl_sum, other_sum

if __name__ == "__main__":
    kmin = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    kmax = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    rows = []
    for kap in range(kmin, kmax + 1):
        t0 = time.time()
        T, S, perms, n = weil_ops(kap)
        line = [f"kap={kap:2d}"]
        for word, tr_ in WORDS.items():
            base = tr_ ** 2 - 4
            rsum, osum = coset_sums(word, T, S, perms)
            rfit = fit_sqrt(rsum.real, base) or fit_sqrt(rsum.imag, base)
            ofit = fit_sqrt(osum.real, base) or fit_sqrt(osum.imag, base)
            rbear = bool(rfit and rfit[1] != 0)
            obear = bool(ofit and ofit[1] != 0)
            rows.append((word, kap, rbear, obear, rsum, osum))
            line.append(f"{word}: refl={'BEAR' if rbear else 'sil '}"
                         f"({rsum.real:+.4f}{rsum.imag:+.4f}j) "
                         f"other={'BEAR' if obear else 'sil '}")
        print("  ".join(line) + f"  [{time.time()-t0:.2f}s]", flush=True)

    print("\n--- summary (reflection-coset sum bearing set) ---")
    for word, tr_ in WORDS.items():
        base = tr_ ** 2 - 4
        bk = [k for (w, k, rb, ob, rs, os_) in rows if w == word and rb]
        print(f"{word} (t={tr_}, base={base}): REFL bearing kappa = {bk}")
    print("\n--- summary (other-coset sum bearing set, control) ---")
    for word, tr_ in WORDS.items():
        base = tr_ ** 2 - 4
        bk = [k for (w, k, rb, ob, rs, os_) in rows if w == word and ob]
        print(f"{word} (t={tr_}, base={base}): OTHER bearing kappa = {bk}")
