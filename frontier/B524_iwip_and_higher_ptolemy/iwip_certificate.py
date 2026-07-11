#!/usr/bin/env sage-python
"""B524 Part 1 — the iwip / word-hyperbolic certificate for the Level-1 automorphism phi.
Uses Coulbois' train_track (Bestvina-Handel), VALIDATED on known cases first.
phi (relabel our F4 gens a,b,A,B -> a,b,c,d):  a->abccd, b->acd, c->abcd, d->ac."""
from sage.all import matrix
from train_track import FreeGroupAutomorphism as FGA

def expansion(f):
    # dilatation = spectral radius of the train-track incidence matrix
    M = f.train_track().matrix()
    return float(max(abs(e) for e in matrix(M).eigenvalues()))

# --- validate the tool on known cases FIRST (the discipline) ---
assert FGA('a->ab,b->ac,c->a').is_iwip() is True          # Tribonacci: known iwip
assert FGA('a->ab,b->b').is_iwip() is False               # fixes <b>: known non-iwip
assert FGA('a->ab,b->ac,c->a,d->d').is_iwip() is False    # fixes <d>: known non-iwip

# --- the target ---
phi = FGA('a->abccd,b->acd,c->abcd,d->ac')
inv = phi.inverse()                                        # exists => automorphism (Hopfian-consistent)
lp, li = expansion(phi), expansion(inv)
assert phi.is_iwip() is True                               # IWIP
assert abs(lp - 3.67621) < 1e-3                            # lambda(phi) = beta = phi(1+sqrt phi)
assert abs(lp - li) > 0.1                                  # lambda(phi) != lambda(phi^-1) => NOT geometric => atoroidal
print("phi in Aut(F4): yes (inverse exists)")
print("iwip:", phi.is_iwip())
print("lambda(phi) =", round(lp,5), " lambda(phi^-1) =", round(li,5), "-> atoroidal (not geometric)")
print("=> F4 x|_phi Z is word-hyperbolic (Brinkmann 2000); NOT a 3-manifold group (cd=2).")
print("index_list:", phi.index_list())
