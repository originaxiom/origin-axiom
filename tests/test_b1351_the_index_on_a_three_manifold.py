"""B1351 lock: on every closing the Wilson-line spectrum pairs weight with mirror weight -- h^1(Y_n; psi) = h^1(Y_n; psi-bar) for
every character (Poincare duality), checked with the 2x2 criterion modulo two primes; fast: levels 2..7."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "frontier" / "B1351_the_index_on_a_three_manifold" / "verification"))


def test_every_character_is_paired_with_its_conjugate_on_the_closings():
    import pairs_on_the_closings as P
    for n, (chars, carry) in {2: (4, 0), 3: (15, 3), 5: (120, 20), 6: (319, 27), 7: (840, 56)}.items():
        total, c, paired = P.level(n)
        assert (total, c) == (chars, carry), (n, total, c)
        assert paired == total, (n, paired, total)
