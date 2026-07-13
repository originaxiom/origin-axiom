"""Locks for the second literature sweep's in-session verified facts.

  lk2(11,809) = 1: the object's two leading charge primes are NONTRIVIALLY LINKED
  in Spec Z (Morishita dictionary: linking = Legendre symbols; 809 = 1 mod 4).
  Arboreal alignment: the Galois gauge tower matches FULL Aut(binary tree) at
  depths 1-2 (2, 8=D4) and the order-32 census at depth 3 is index 4 -- the PCF
  collapse signature; the 2^{2n+1} conjecture = full at depths 1-2, collapse after.
See docs/LITERATURE_SWEEP2_2026-07-13.md.
"""
import sympy as sp


def test_charge_primes_are_linked_in_spec_z():
    assert 809 % 4 == 1                                   # clean quadratic reciprocity
    assert sp.legendre_symbol(809, 11) == -1
    assert sp.legendre_symbol(-11, 809) == -1             # symmetric symbol with the twist
    # both = -1  =>  lk2(11,809) = 1: nontrivially linked (Morishita, arXiv:0904.3399 eq 2.1)


def test_arboreal_tower_alignment():
    """|G_depth| vs |Aut(T_depth)| = 2^(2^k - 1): full at k=1,2; index 4 at k=3."""
    ours = {1: 2, 2: 8, 3: 32}                            # Z/2, D4 (banked), order-32 (census)
    conj = {k: 2 ** (2 * (k - 1) + 1) for k in (1, 2, 3)} # |G_n| = 2^{2n+1}, n = k-1
    assert ours == conj                                    # the conjecture matches all data
    full = {k: 2 ** (2 ** k - 1) for k in (1, 2, 3)}
    assert ours[1] == full[1] and ours[2] == full[2]       # full tree group at depths 1-2
    assert full[3] // ours[3] == 4                         # the depth-3 collapse: index 4 (PCF)
