"""B366 -- the invariant-spin-sector lemmas (exact)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B366_invariant_spin_sector'))
from invariant_spin import puncture_lemma, spin_lemma, forcing_shape


def test_puncture_lemma():
    assert puncture_lemma()          # the origin is the unique SL(2,Z)-invariant 2-torsion point


def test_spin_lemma():
    assert spin_lemma()              # odd [1/2,1/2] uniquely invariant; evens one orbit


def test_forcing_shape():
    assert forcing_shape()           # the invariant sector lives in the a=1/2 (seam-bearing) class
