"""Locks for B764 -- C19's out-of-field test and the corrected law."""
import math

import sympy as sp

u = sp.symbols("u")


def _offblock(riley):
    A = sp.Matrix([[1, 1], [0, 1]])
    Bm = sp.Matrix([[1, 0], [-u, 1]])
    tr = (A * Bm).trace()
    d = sp.diff(sp.expand(tr**2 - 1), u)
    roots = [complex(r) for r in sp.Poly(riley, u).nroots(30)]
    geo = max((r for r in roots if abs(r.imag) > 1e-10), key=lambda r: r.imag)
    return abs(complex(d.subs(u, geo)).imag), geo


def test_m004_quadratic_identity_holds():
    off, geo = _offblock(u**2 + u + 1)
    assert abs(off - math.sqrt(3)) < 1e-9              # = sqrt|disc| for the quadratic


def test_5_2_breaks_the_disc_form_and_obeys_the_pair_law():
    off, geo = _offblock(u**3 + u**2 + 2 * u + 1)
    assert abs(off - math.sqrt(23)) > 1                # the disc form FAILS
    assert abs(off - 2 * geo.imag) < 1e-9              # the pair-separation law holds


def test_the_disc_factorization_at_5_2():
    f = sp.Poly(u**3 + u**2 + 2 * u + 1, u)
    roots = [r.evalf(50) for r in f.all_roots()]
    z = [r for r in roots if sp.im(r) > 0][0]
    zb = [r for r in roots if sp.im(r) < 0][0]
    rr = [r for r in roots if abs(sp.im(r)) < sp.Float("1e-45")][0]
    recon = sp.expand((z - zb) ** 2 * ((z - rr) * (zb - rr)) ** 2)
    assert abs(sp.re(recon) - (-23)) < sp.Float("1e-40")
    assert abs(sp.im(recon)) < sp.Float("1e-40")
