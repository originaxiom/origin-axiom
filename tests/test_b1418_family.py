"""B1418 locks: (1) the instrument reproduces R27's m010 witness (I = +1, semisimplification 0) -- the banked identity;
(2) the characteristic-zero positive on the class member s958: at its cusp-trivial order-3 character chi, the reducible
non-split module Sym^3(rho_chi) (x) chi has I = +1 with semisimplification 0 (SnapPy's default presentation)."""
import os, sys, itertools, subprocess
import pytest
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V = os.path.join(ROOT, "frontier", "B1418_the_family_as_the_object", "verification")
sys.path.insert(0, V)

def test_m010_control():
    r = subprocess.run([sys.executable, os.path.join(V, "c2_reducible_index.py")], capture_output=True, text=True, timeout=900)
    assert r.returncode == 0 and "CONTROL PASS" in r.stdout and "BANKED IDENTITY reproduced" in r.stdout, r.stdout[-800:]

def test_s958_positive():
    snappy = pytest.importorskip("snappy")
    from c2_reducible_index import NF, presentation, char_on_word, nonsplit_cocycle, run_module
    K = NF([1, 0, -1, 0, 1]); z = K.alpha(); z3 = K.pw(z, 4)
    M, gens, rels, mu, lam = presentation("s958")
    found = []
    for vals in itertools.product([K.const(1), z3, K.pw(z3, 2)], repeat=len(gens)):
        chi = dict(zip(gens, vals))
        if all(K.is_zero(K.sub(char_on_word(K, r, chi), K.const(1))) for r in rels) and not all(K.is_zero(K.sub(chi[g], K.const(1))) for g in gens):
            chi2 = {g: K.mul(chi[g], chi[g]) for g in gens}; c, h1 = nonsplit_cocycle(K, gens, rels, chi2)
            if c is None: continue
            assert K.is_zero(K.sub(char_on_word(K, mu, chi), K.const(1))) and K.is_zero(K.sub(char_on_word(K, lam, chi), K.const(1)))   # cusp-trivial
            r = run_module(K, "s958", gens, rels, mu, lam, chi, c, 3, chi, "lock")
            found.append((r["I"], r["I_ss"]))
    assert found and all(I == 1 and Iss == 0 for I, Iss in found), found
