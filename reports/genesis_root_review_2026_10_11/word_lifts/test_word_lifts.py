"""Independent integer-letter controls for the sealed word checker."""
import itertools
import unittest
import verify as v

ENC = {"a": 1, "b": 2, "A": -1, "B": -2}
DEC = {i: x for x, i in ENC.items()}


def reference_reduce(word):
    # Repeated adjacent cancellation, not the producer's stack algorithm.
    out = list(word)
    while True:
        for i in range(len(out) - 1):
            if out[i] == -out[i + 1]:
                out = out[:i] + out[i + 2:]
                break
        else:
            return out


def reference_apply(f, word):
    images = {ENC[x]: [ENC[c] for c in w] for x, w in f.items()}
    expanded = []
    for c in word:
        seq = images[abs(ENC[c])]
        expanded.extend(seq if ENC[c] > 0 else [-i for i in seq[::-1]])
    return "".join(DEC[i] for i in reference_reduce(expanded))


class WordLiftTests(unittest.TestCase):
    def test_reduction_against_second_algorithm(self):
        for n in range(6):
            for letters in itertools.product("abAB", repeat=n):
                word = "".join(letters)
                expected = "".join(DEC[i] for i in reference_reduce([ENC[x] for x in word]))
                self.assertEqual(v.red(word), expected)

    def test_substitution_against_second_algorithm(self):
        for f in (v.L0, v.L1, v.R0, v.R1, *v.INVERSES):
            for n in range(5):
                for letters in itertools.product("abAB", repeat=n):
                    word = "".join(letters)
                    self.assertEqual(v.apply(f, word), reference_apply(f, word))

    def test_composition_order_is_discriminating(self):
        self.assertEqual(v.compose(v.L0, v.R0), {"a": "aab", "b": "ab"})
        self.assertNotEqual(v.compose(v.L0, v.R0), v.compose(v.R0, v.L0))

    def test_pair_conjugation_independent_on_generators(self):
        for l, r, q in v.PAIR_TABLE:
            for base, target in ((v.L0, l), (v.R0, r)):
                for x in "ab":
                    pulled = reference_apply(v.inner(v.inv(q)), x)
                    updated = reference_apply(base, pulled)
                    self.assertEqual(reference_apply(v.inner(q), updated), target[x])

    def test_delta_power_independent(self):
        for x in "ab":
            word = x
            for _ in range(4):
                for f in (v.L0, v.INVERSES[2], v.L0):
                    word = reference_apply(f, word)
            self.assertEqual(word, reference_apply(v.inner(v.C), x))

    def test_signed_exponents_are_not_positive_words(self):
        mutant = v.compose(v.inner("a"), v.L0)
        self.assertEqual(v.h1(mutant), v.h1(v.L0))
        self.assertNotIn(mutant, v.positive_candidates(v.h1(v.L0)))
        self.assertNotEqual(v.apply(mutant, v.C), v.C)

    def test_cyclic_word_has_no_period(self):
        self.assertEqual(len(v.C), 4)
        self.assertEqual(v.red(v.C * 2), v.C * 2)
        for period in (1, 2):
            self.assertNotEqual(v.C[:period] * (4 // period), v.C)

    def test_false_identities_are_rejected(self):
        self.assertNotEqual(v.compose(v.L1, v.INVERSES[0]), v.ID)
        self.assertNotEqual(v.compose(v.R1, v.INVERSES[2]), v.ID)
        self.assertNotEqual(v.power({"a": "ab", "b": "a"}, 2), v.compose(v.L0, v.R0))
        self.assertNotEqual(v.transport(v.R0, "b"), v.R1)

    def test_complete_sealed_packet(self):
        out = v.verify()
        self.assertEqual(out["status"], "PASS")
        self.assertFalse(out["physical_claim"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
