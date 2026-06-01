"""B49 -- SL(3) certificate-to-proof hardening.

This probe does not replace a written proof.  It turns the B48 integer
classification certificate into reusable proof obligations:

* universal splitting criterion;
* positive split families and isolated cases;
* square-gap propagation lemma;
* finite positive strip checks;
* negative strip and boundary checks.

The result is a proof architecture for PC12, not a promoted theorem.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
B48_PATH = ROOT / "frontier" / "B48_sl3_metallic_trace_maps" / "probe.py"


def load_b48():
    spec = importlib.util.spec_from_file_location("b48_sl3_metallic_probe", B48_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load B48 probe from {B48_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


b48 = load_b48()


def third_diff(fn, n: int) -> int:
    return fn(n + 3) - 3 * fn(n + 2) + 3 * fn(n + 1) - fn(n)


def seed_tuple(fn, n: int) -> tuple[int, int, int, int, int]:
    values = [fn(n + offset) for offset in range(5)]
    h0 = values[0]
    d1 = values[1] - values[0]
    d2 = values[2] - 2 * values[1] + values[0]
    d3 = values[3] - 3 * values[2] + 3 * values[1] - values[0]
    d3_next = values[4] - 3 * values[3] + 3 * values[2] - values[1]
    return h0, d1, d2, d3, d3_next


def seed_is_propagating(seed: tuple[int, int, int, int, int]) -> bool:
    h0, d1, d2, d3, d3_next = seed
    return h0 > 0 and d1 > 0 and d2 > 0 and 0 < d3 <= d3_next


def recurrence_holds(fn, n_start: int, q: int, samples: int = 8) -> bool:
    for n in range(n_start, n_start + samples):
        if third_diff(fn, n + 2) != q * third_diff(fn, n + 1) - third_diff(fn, n):
            return False
    return True


def positive_gap(c: int, k: int, m: int, *, upper: bool) -> int:
    trace, _, discriminant = b48.discriminant_data(c, m)
    lower_square_root = trace + 4 * m - k
    if upper:
        return (lower_square_root + 1) ** 2 - discriminant
    return discriminant - lower_square_root**2


def negative_gap(c: int, parity: str, k: int, n: int, *, upper: bool) -> int:
    if parity == "even":
        m = 2 * n
        trace, _, discriminant = b48.discriminant_data(c, m)
        lower_square_root = trace + 8 * n + k
    elif parity == "odd":
        m = 2 * n + 1
        trace, _, discriminant = b48.discriminant_data(c, m)
        lower_square_root = -trace - (8 * n + k)
    else:
        raise ValueError(f"unknown parity {parity!r}")

    if upper:
        return (lower_square_root + 1) ** 2 - discriminant
    return discriminant - lower_square_root**2


def check_universal_splitting_criterion() -> tuple[bool, str]:
    for c in range(-20, 21):
        for m in range(1, 41):
            trace, second_coeff, discriminant = b48.discriminant_data(c, m)
            observed = b48.actual_splits(c, m)
            if discriminant < 0:
                criterion = False
            else:
                root = b48.math.isqrt(discriminant)
                criterion = root * root == discriminant and (trace + root) % 2 == 0
                if criterion:
                    alpha = (trace + root) // 2
                    beta = (trace - root) // 2
                    criterion = alpha + beta == trace and alpha * beta == second_coeff + 2
            if observed != criterion:
                return False, f"criterion mismatch c={c}, m={m}"
    return True, "criterion checked on -20<=c<=20, 1<=m<=40"


def check_positive_families() -> tuple[bool, str]:
    for m in range(1, 80):
        if not b48.actual_splits(1, m):
            return False, f"c=1 failed at m={m}"
        if not b48.actual_splits(3, m):
            return False, f"c=3 failed at m={m}"
        if b48.actual_splits(0, m) != (m % 3 == 0):
            return False, f"c=0 residue failed at m={m}"
        if b48.actual_splits(2, m) != (m % 6 == 0):
            return False, f"c=2 residue failed at m={m}"
        if b48.actual_splits(-1, m) != (m % 2 == 0):
            return False, f"c=-1 parity failed at m={m}"

    expected_isolated = {(-11, 1), (-9, 1), (-3, 2), (-3, 3)}
    for c in (-11, -9, -3):
        for m in range(1, 20):
            if b48.actual_splits(c, m) != ((c, m) in expected_isolated):
                return False, f"isolated case mismatch c={c}, m={m}"

    return True, "positive families and isolated cases checked"


def check_square_gap_propagation_lemma() -> tuple[bool, str]:
    # Algebraic core: if q>=2 and 0<a<=b, then q*b-a >= b because
    # q*b-a-b = (q-2)*b + (b-a) >= 0.
    for q in range(2, 20):
        for a in range(1, 20):
            for b in range(a, 20):
                if q * b - a < b:
                    return False, f"propagation inequality failed q={q}, a={a}, b={b}"
    return True, "recurrence propagation inequality checked for representative integers"


def check_positive_finite_strip() -> tuple[bool, str]:
    strip = {
        4: (7, 6),
        5: (5, 5),
        6: (4, 5),
        7: (3, 3),
        8: (3, 5),
        9: (2, 2),
        10: (2, 2),
        11: (2, 2),
        12: (2, 2),
        13: (2, 2),
        14: (2, 5),
    }

    for c, (k, n_start) in strip.items():
        q = c - 1
        for upper in (False, True):
            fn = lambda m, c=c, k=k, upper=upper: positive_gap(c, k, m, upper=upper)
            seed = seed_tuple(fn, n_start)
            if not seed_is_propagating(seed):
                return False, f"positive strip seed failed c={c}, upper={upper}, seed={seed}"
            if not recurrence_holds(fn, n_start, q):
                return False, f"positive strip recurrence failed c={c}, upper={upper}"
        for m in range(1, n_start):
            if b48.actual_splits(c, m):
                return False, f"positive strip direct initial split c={c}, m={m}"

    return True, "4<=c<=14 square-gap seeds and recurrences checked"


def check_negative_strip() -> tuple[bool, str]:
    rows = {
        (-11, "even"): (0, 1),
        (-11, "odd"): (5, 1),
        (-10, "even"): (0, 1),
        (-10, "odd"): (5, 2),
        (-9, "even"): (1, 2),
        (-9, "odd"): (6, 1),
        (-8, "even"): (1, 2),
        (-8, "odd"): (6, 1),
        (-7, "even"): (1, 2),
        (-7, "odd"): (6, 1),
        (-6, "even"): (1, 2),
        (-6, "odd"): (6, 1),
        (-5, "even"): (1, 2),
        (-5, "odd"): (6, 2),
        (-4, "even"): (1, 2),
        (-4, "odd"): (6, 3),
        (-3, "even"): (2, 3),
        (-3, "odd"): (7, 2),
        (-2, "even"): (2, 4),
        (-2, "odd"): (7, 4),
    }
    allowed_initial_splits = {(-11, 1), (-9, 1), (-3, 2), (-3, 3)}

    for (c, parity), (k, n_start) in rows.items():
        p = -c
        q = p * p + 2 * p - 1
        for upper in (False, True):
            fn = lambda n, c=c, parity=parity, k=k, upper=upper: negative_gap(c, parity, k, n, upper=upper)
            seed = seed_tuple(fn, n_start)
            if not seed_is_propagating(seed):
                return False, f"negative seed failed c={c}, parity={parity}, upper={upper}, seed={seed}"
            if not recurrence_holds(fn, n_start, q):
                return False, f"negative recurrence failed c={c}, parity={parity}, upper={upper}"

        initial_ns = range(1, n_start)
        for n in initial_ns:
            m = 2 * n if parity == "even" else 2 * n + 1
            if b48.actual_splits(c, m) and (c, m) not in allowed_initial_splits:
                return False, f"unexpected initial split c={c}, m={m}"

    if not b48.actual_splits(-11, 1):
        return False, "boundary split c=-11,m=1 missing"

    return True, "-11<=c<=-2 parity square-gap seeds and recurrences checked"


def run_checks() -> list[tuple[str, bool, str]]:
    checks = [
        ("universal splitting criterion", check_universal_splitting_criterion),
        ("positive families", check_positive_families),
        ("square-gap propagation lemma", check_square_gap_propagation_lemma),
        ("positive finite strip", check_positive_finite_strip),
        ("negative strip and boundary", check_negative_strip),
    ]
    return [(name, *fn()) for name, fn in checks]


def main() -> int:
    print("B49 -- SL(3) CERTIFICATE-TO-PROOF HARDENING")
    print("Status: proof architecture only; PC12 remains NEEDS_VALIDATION")
    print()
    results = run_checks()
    for name, ok, detail in results:
        print(f"{name}: {'OK' if ok else 'FAIL'} -- {detail}")
    all_ok = all(ok for _, ok, _ in results)
    print()
    print(f"B49 PROOF-HARDENING CHECKS: {'OK' if all_ok else 'FAIL'}")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
