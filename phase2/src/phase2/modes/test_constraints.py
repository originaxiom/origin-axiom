from __future__ import annotations

import numpy as np

from phase2.modes.constraints import enforce_global_floor


# ============================================================
# Origin Axiom — Phase 2
# Tests for constraint enforcement
#
# These are lightweight and can be run with:
#   python -m phase2.modes.test_constraints
#
# (Optional) integrate with pytest later; Phase 2 keeps it simple.
# ============================================================


def _rng(seed: int = 12345) -> np.random.Generator:
    return np.random.default_rng(seed)


def test_no_change_when_above_floor() -> None:
    eps = 1e-6
    A = 3e-6 + 4e-6j  # |A| = 5e-6 > eps
    A2, act = enforce_global_floor(A, epsilon=eps, rng=_rng())
    assert A2 == A
    assert act.applied is False
    assert abs(act.delta_magnitude) < 1e-30


def test_rescale_when_below_floor_preserve_direction() -> None:
    eps = 1e-6
    A = 3e-7 + 4e-7j  # |A| = 5e-7 < eps
    A2, act = enforce_global_floor(A, epsilon=eps, rng=_rng())
    assert act.applied is True
    assert np.isclose(abs(A2), eps)

    # direction preserved => A2 is positive scalar multiple of A
    # compare normalized complex direction
    d1 = A / abs(A)
    d2 = A2 / abs(A2)
    assert np.isclose(d1.real, d2.real)
    assert np.isclose(d1.imag, d2.imag)


def test_zero_vector_uses_seeded_direction() -> None:
    eps = 1e-6
    A = 0.0 + 0.0j
    A2a, act_a = enforce_global_floor(A, epsilon=eps, rng=_rng(111))
    A2b, act_b = enforce_global_floor(A, epsilon=eps, rng=_rng(111))
    A2c, act_c = enforce_global_floor(A, epsilon=eps, rng=_rng(222))

    assert act_a.applied is True
    assert act_a.direction_source == "random_direction"
    assert np.isclose(abs(A2a), eps)

    # same seed => same output
    assert A2a == A2b

    # different seed => (almost surely) different output
    assert A2a != A2c


def test_invalid_epsilon_raises() -> None:
    try:
        enforce_global_floor(1.0 + 0.0j, epsilon=-1.0, rng=_rng())
        assert False, "Expected ValueError"
    except ValueError:
        pass


def main() -> None:
    test_no_change_when_above_floor()
    test_rescale_when_below_floor_preserve_direction()
    test_zero_vector_uses_seeded_direction()
    test_invalid_epsilon_raises()
    print("OK: constraints tests passed")


if __name__ == "__main__":
    main()