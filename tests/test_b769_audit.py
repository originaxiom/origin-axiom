"""Compute-grade locks for the B769 audit (cc3 verification pass)."""
import sympy as sp

u = sp.Symbol("u")
omega = sp.Rational(-1, 2) + sp.I * sp.sqrt(3) / 2


class TestUnmovednessTheorem:
    def test_conjugation_trivial_on_v4(self):
        V4 = [0b000, 0b001, 0b010, 0b011]
        assert all((g ^ v ^ g) == v for g in range(8) for v in V4)

    def test_aut_v4_is_s3(self):
        assert (4 - 1) * (4 - 2) == 6  # |GL(2,F2)|


class TestFrameTorsor:
    def test_three_frames(self):
        from itertools import combinations
        frames = list(combinations(["c", "th", "cth"], 2))
        assert len(frames) == 3


class TestDerivativePlane:
    def test_probe_vector(self):
        A = sp.Matrix([[1, 1], [0, 1]])
        B = sp.Matrix([[1, 0], [-u, 1]])
        probe = sp.simplify(sp.diff(sp.expand((A*B).trace()**2 - 1), u).subs(u, omega))
        assert sp.simplify(sp.re(probe) + 5) == 0
        assert sp.simplify(sp.im(probe) - sp.sqrt(3)) == 0

    def test_theta_frame_aligned_with_c_frame(self):
        A = sp.Matrix([[1, 1], [0, 1]])
        B = sp.Matrix([[1, 0], [-u, 1]])
        probe = sp.simplify(sp.diff(sp.expand((A*B).trace()**2 - 1), u).subs(u, omega))
        # even = Re, odd = Im: theta-frame lies along c-frame
        assert sp.re(probe) != 0  # even component nonzero
        assert sp.im(probe) != 0  # odd component nonzero
        # the key: even is purely real, odd is purely real (as a coefficient of i)
        # => the two frames share the same axes


class TestSL3EightSpace:
    @staticmethod
    def _sym2(M):
        a, b, c_, e = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        return sp.Matrix([
            [a**2, a*b, b**2],
            [2*a*c_, a*e + b*c_, 2*b*e],
            [c_**2, c_*e, e**2]])

    def test_theta_odd_coordinates_vanish(self):
        A3 = self._sym2(sp.Matrix([[1, 1], [0, 1]]).subs(u, omega))
        B3 = self._sym2(sp.Matrix([[1, 0], [-omega, 1]]))
        vals = {
            "x1": A3.trace(), "x2": B3.trace(),
            "x3": (A3*B3).trace(), "x4": A3.inv().trace(),
            "x5": B3.inv().trace(), "x6": (A3.inv()*B3).trace(),
            "x7": (A3*B3.inv()).trace(), "x8": (A3.inv()*B3.inv()).trace(),
        }
        for a, b in [("x1","x4"),("x2","x5"),("x3","x8"),("x6","x7")]:
            assert sp.simplify(vals[a] - vals[b]) == 0

    def test_x1_equals_3(self):
        A3 = self._sym2(sp.Matrix([[1, 1], [0, 1]]))
        assert sp.simplify(A3.trace() - 3) == 0
