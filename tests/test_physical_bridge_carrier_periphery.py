"""R79 mathematical controls, no transcript-string certification."""
import importlib.util
from pathlib import Path
import unittest

PATH = Path(__file__).resolve().parents[1] / "reports/physical_bridge_2026_09_05/carrier_periphery.py"
SPEC = importlib.util.spec_from_file_location("carrier_periphery_r79", PATH)
cp = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(cp)


class CarrierPeripheryTests(unittest.TestCase):
    def test_conjugacy_detector_is_two_sided(self):
        self.assertTrue(cp.conjugate(cp.C, cp.apply(cp.inner((1, 2, 1)), cp.C)))
        self.assertFalse(cp.conjugate(cp.C, cp.inverse(cp.C)))
        self.assertFalse(cp.conjugate(cp.C, (1, 2)))
        self.assertFalse(cp.conjugate(cp.C, cp.word_power(cp.C, 2)))
        self.assertTrue(cp.conjugate((), (1, -1)))

    def test_genuine_automorphisms_recover_signed_periphery(self):
        rows = cp.nielsen_sequences(4)
        self.assertEqual(len(rows), sum(4**j for j in range(5)))
        signs = set()
        for _, f, fi in rows:
            self.assertEqual(cp.compose(f, fi), cp.IDENTITY)
            self.assertEqual(cp.compose(fi, f), cp.IDENTITY)
            d = cp.determinant(cp.homology(f))
            signs.add(d)
            self.assertTrue(cp.conjugate(cp.apply(f, cp.C), cp.C if d == 1 else cp.inverse(cp.C)))
        self.assertEqual(signs, {-1, 1})

    def test_unimodular_endomorphism_is_not_an_automorphism_certificate(self):
        psi = ((1,), cp.reduce_word((2,) + cp.C))
        self.assertEqual(cp.homology(psi), cp.homology(cp.IDENTITY))
        self.assertFalse(cp.conjugate(cp.apply(psi, cp.C), cp.C))
        self.assertFalse(cp.conjugate(cp.apply(psi, cp.C), cp.inverse(cp.C)))

    def test_record_normalizations_are_actual_words(self):
        sigma2 = cp.compose(cp.SIGMA, cp.SIGMA)
        self.assertEqual(cp.compose(cp.inner((-1, -2, -1)), sigma2), cp.F0)
        self.assertEqual(cp.compose(cp.inner((-1,)), cp.B1303), cp.F0)
        self.assertEqual(cp.apply(cp.F0, cp.C), cp.C)
        self.assertNotEqual(sigma2, cp.F0)
        self.assertEqual(cp.homology(sigma2), cp.homology(cp.F0))

    def test_normalized_lifts_are_distinct_despite_same_homology(self):
        images = set()
        for k in range(-3, 4):
            f, fi = cp.framed(k), cp.framed_inverse(k)
            images.add(f)
            self.assertEqual(cp.apply(f, cp.C), cp.C)
            self.assertEqual(cp.homology(f), cp.homology(cp.F0))
            self.assertEqual(cp.compose(f, fi), cp.IDENTITY)
            self.assertEqual(cp.compose(fi, f), cp.IDENTITY)
        self.assertEqual(len(images), 7)

    def test_slope_is_transported_not_frozen_as_a_number(self):
        self.assertNotEqual(cp.shear(1, 3, 1), (1, 3))
        self.assertEqual(cp.shear(1, 3, 1), (4, 3))
        self.assertEqual(cp.shear(*cp.shear(1, 3, 1), -1), (1, 3))
        self.assertEqual(cp.shear(1, 0, 3), (1, 0))

    def test_nonabelian_flat_descent_control_and_transport(self):
        ts = cp.finite_transversals()
        self.assertTrue(ts)
        t, c = ts[0], cp.evaluate(cp.C)
        self.assertNotEqual(c, cp.I3)
        self.assertNotEqual(cp.mm(c, cp.mp(t, 3)), cp.I3)
        self.assertEqual(cp.mm(c, cp.mp(cp.mm(c, t), 3)), cp.I3)
        self.assertEqual(cp.mm(cp.mp(c, 4), cp.mp(t, 3)), cp.I3)

    def test_entire_preregistered_finite_protocol(self):
        result = cp.run_checks()
        self.assertEqual(result["nielsen_sequences_length_0_to_5"], sum(4**j for j in range(6)))
        self.assertEqual(result["slope_integer_controls"], 7*7*7)
        self.assertEqual(result["abelian_blind_controls"], 6**3*7)


if __name__ == "__main__":
    unittest.main()
