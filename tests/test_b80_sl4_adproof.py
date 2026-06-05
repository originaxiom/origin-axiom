"""B80 (Phase 2, V62) -- locking test for the SL(4) tower from first principles.

The FULL proof (reconstruct J(m) over Q[m] via CRT, factor char(J(m)) = the tower) is in
build_jm.main() (~2-3 min, 40 F_p engine calls + sympy). Here we lock the fast, decisive pieces:
  (1) the symbolic tower helpers are self-consistent (char_factor / sl4_tower);
  (2) at integer m the EXACT F_p engine's char(DT_0(m)) equals the SL(4) tower at that m -- the
      core certified fact, cheap (one engine call per m).
Plus the recorded full result: jacobian_m_crt.json has matches_tower=True and the B65-identical char poly.
"""
import importlib.util
import json
import pathlib

import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[1]
_spec = importlib.util.spec_from_file_location(
    "b80_adproof", _ROOT / "frontier" / "B80_sl4_adproof" / "build_jm.py")
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)


def test_symbolic_tower_factors():
    """char_factor / sl4_tower are self-consistent: the tower expands and char_factor signs are right."""
    m, t = B.m, B.t
    assert sp.expand(B.char_factor(2) - (t**2 - (m**2 + 2) * t + 1)) == 0
    assert sp.expand(B.char_factor(3) - (t**2 - (m**3 + 3 * m) * t - 1)) == 0
    assert sp.expand(B.char_factor(2, sign=-1) - (t**2 + (m**2 + 2) * t + 1)) == 0
    assert sp.Poly(B.sl4_tower(), t).degree() == 15


def test_fp_engine_charpoly_is_tower_at_integer_m():
    """The EXACT F_p fixed-line Jacobian: char(DT_0(p,m)) == sl4_tower(m) mod p, for m=2 and m=3."""
    p = B.DEFAULT_PRIMES[0]
    assert B.verify_at_m(p, 2), "char(DT_0(m=2)) must equal the SL(4) tower at m=2 (mod p)"
    assert B.verify_at_m(p, 3), "char(DT_0(m=3)) must equal the SL(4) tower at m=3 (mod p)"


def test_recorded_full_reconstruction_matches_tower():
    """The committed full-build artifact records matches_tower=True (the Q[m] symbolic factorization)."""
    art = json.loads((_ROOT / "frontier" / "B80_sl4_adproof" / "jacobian_m_crt.json").read_text())
    assert art["matches_tower"] is True
    # and the recorded char poly equals the tower symbolically
    assert sp.expand(sp.sympify(art["charpoly_factored"]) - B.sl4_tower()) == 0
