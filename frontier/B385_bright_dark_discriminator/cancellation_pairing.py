"""B385 -- the window-cancellation pairing: how do dark (1,3)'s 44 anti-cells cancel
under EVERY window, and does bright (3,4) lack that symmetry?

Sharpest structural test first: the sigma31 relabel (P61: t(31a,31b)=t(a,b); on the raw grid
sigma31 acts as (j,l) fixed with VALUE conjugation) and the translation/mirror orbits.
Concretely: compute the exact anti-PAIR-VECTOR (z,s) of each cell; test candidate involutions
iota on the grid for: anti(iota(cell)) == -anti(cell) (odd pairing => all windows with
iota-symmetric characters cancel... a full spectral null needs anti to be ODD under a
TRANSLATION-type symmetry: anti[j+dj, l+dl] = -anti[j,l] for some (dj,dl) -- then every DFT
character chi with chi(dj,dl) = +1 kills it, and characters with chi = -1 must be checked
separately => a full null forces anti[j+dj,l+dl] = -anti[j,l] AND the same for a second
independent translation, OR odd under one translation whose order-2 character classes are
all killed by a second relation. Scan all translations."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order, par_trace

def anti_table(m1, m2):
    W1 = build_theta_W(m1); W2 = build_theta_W(m2)
    o1, p1 = matrix_order(W1); o2, p2 = matrix_order(W2)
    T = {}
    for j in range(o1):
        for l in range(o2):
            sol = SC.solve_H(SC.H_avg(par_trace(p1[j], p2[l])))
            T[(j,l)] = (sol[2], sol[3]) if sol else (Fr(0), Fr(0))
    return T, o1, o2

def translation_scan(T, o1, o2):
    """all (dj,dl) with anti[j+dj,l+dl] == -anti[j,l] everywhere (odd), or == +anti (even)."""
    odd, even = [], []
    for dj in range(o1):
        for dl in range(o2):
            if dj == 0 and dl == 0: continue
            if all(T[((j+dj)%o1,(l+dl)%o2)] == (-T[(j,l)][0], -T[(j,l)][1]) for j in range(o1) for l in range(o2)):
                odd.append((dj,dl))
            elif all(T[((j+dj)%o1,(l+dl)%o2)] == T[(j,l)] for j in range(o1) for l in range(o2)):
                even.append((dj,dl))
    return odd, even

for (m1,m2,st) in ((1,3,"dark"), (3,4,"bright")):
    T,o1,o2 = anti_table(m1,m2)
    odd, even = translation_scan(T,o1,o2)
    nz = sum(1 for v in T.values() if v != (0,0))
    print(f"({m1},{m2}) {st}: anti-cells {nz}/{o1*o2}; ODD translations {odd}; even {even[:6]}{'...' if len(even)>6 else ''}")
