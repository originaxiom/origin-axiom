#!/usr/bin/env python3
"""Portable exact checks for the R030 proper-specialization cover theorem.

The payload contains integral Q(zeta_12) chart generators and modular Bezout
coefficients on all 36 toric charts.  This certificate reduces the integral
generators itself and checks each GF(1009) identity literally.  The accompanying memo supplies the
standard proper-image argument promoting empty special fiber to empty generic
base locus.  No modular multiplier is called a characteristic-zero multiplier.
"""

from __future__ import annotations

import gzip
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
PRIME = 1009
PHI_SUBSET = [1, 3, 5, 9]
GENERATOR_ORDER = ["f", "Phi_1", "Phi_3", "Phi_5", "Phi_9"]
EXPECTED_KEYS = {
    "schema", "prime", "zeta12_mod_prime", "field_polynomial_ascending",
    "generator_order", "phi_subset", "charts",
}
CHART_KEYS = {
    "chart", "rays", "integral_generators", "bezout_coefficients_mod_prime",
}
# Filled after the scratch producer emits the deterministic all-chart payload
# and it is independently compared with the exact R028 chart convention.
EXPECTED_GZIP_HASH = "2efb53af4467fedaef5177f348e2c278311c88f736e4ddb03b843c16271b081e"
EXPECTED_GENERATOR_HASH = "f2840a7bd67416337bb68457840598b5ba4712052303b2b9322feac22b57e9dc"
ZERO_EXP = (0, 0, 0, 0)
UNIT_HEXAGON = (
    (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1),
)
DUAL_POINTS_2D = (
    (-1, -1), (-1, 0), (0, -1), (0, 0), (0, 1), (1, 0), (1, 1),
)
FAN_RAYS = tuple(ray + (0, 0) for ray in UNIT_HEXAGON) + tuple(
    (0, 0) + ray for ray in UNIT_HEXAGON
)
POLYTOPE_POINTS = tuple(
    left + right for left in DUAL_POINTS_2D for right in DUAL_POINTS_2D
)
A_M = (
    (0, 0, 1, -1),
    (0, 0, 1, 0),
    (1, 0, 0, 0),
    (0, 1, 0, 0),
)
RAY_PERMUTATION = (6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 0)
# Exact power-basis serialization of the banked height-308 map vector
# coords_308 -> to_field_vector(coords_308).  The reconstruction below checks
# every payload generator against these data rather than trusting a payload
# hash to identify the audited problem.
PHI308_COORDS = (
    (2, 0, -1, 0), (0, -1, 0, 1), (1, -2, -1, 0), (0, 0, 0, -2),
    (0, 0, 0, 2), (1, 0, -1, 1), (1, -1, 0, 0), (2, 2, 0, 0),
    (0, 0, 0, 0), (0, 2, 0, 0), (0, 0, 0, 0), (0, -2, 0, 0),
    (0, 0, 0, 0), (-2, -2, 0, 0), (-1, 0, 0, 1), (-1, 1, 1, -1),
    (0, 1, 0, -2), (0, 0, 0, 2), (-1, 2, 0, 0), (0, 2, 0, -1),
    (-1, 0, 1, 0), (0, -1, 0, 1), (0, -1, 0, 1), (-1, 0, 1, 0),
    (0, 0, 0, 0), (0, 0, 0, -1), (1, 0, 0, 0), (0, -1, 0, 1),
    (0, 0, 0, -1), (0, 1, 0, 0), (0, 0, 0, -1), (0, 0, 0, 0),
    (0, 0, 0, -1), (0, 0, -1, 0), (-1, 0, 1, 0),
)
NORM_COEFFICIENTS = (
    1, 1, 4, 1, 4, 1, 1, 4, 1, 1, 1, 1, 1, 4, 1, 4, 1, 1, 1, 4,
    1, 1, 1, 1, 0, 1, 1, 1, 1, 4, 1, 1, 1, 4, 1, 4, 1, 1, 1, 1,
    1, 4, 1, 1, 4, 1, 4, 1, 1,
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return value == divisor
        divisor += 1
    return True


def p_add(left: dict[tuple[int, ...], int],
          right: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
    result = dict(left)
    for exponent, coefficient in right.items():
        updated = (result.get(exponent, 0) + coefficient) % PRIME
        if updated:
            result[exponent] = updated
        else:
            result.pop(exponent, None)
    return result


def p_mul(left: dict[tuple[int, ...], int],
          right: dict[tuple[int, ...], int]) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(a + b for a, b in zip(left_exp, right_exp))
            updated = (result.get(exponent, 0)
                       + left_coefficient * right_coefficient) % PRIME
            if updated:
                result[exponent] = updated
            else:
                result.pop(exponent, None)
    return result


def decode_exponent(raw) -> tuple[int, ...]:
    require(isinstance(raw, list) and len(raw) == 4, "bad exponent length")
    require(all(isinstance(value, int) and not isinstance(value, bool)
                and value >= 0 for value in raw), "bad exponent")
    return tuple(raw)


def decode_integral_polynomial(raw, root: int) -> dict[tuple[int, ...], int]:
    require(isinstance(raw, list), "integral polynomial must be a list")
    answer: dict[tuple[int, ...], int] = {}
    previous = None
    for term in raw:
        require(isinstance(term, list) and len(term) == 2, "bad integral term")
        exponent = decode_exponent(term[0])
        require(previous is None or previous < exponent, "unsorted integral terms")
        previous = exponent
        coordinates = term[1]
        require(isinstance(coordinates, list) and len(coordinates) == 4,
                "bad field-coordinate length")
        require(all(isinstance(value, int) and not isinstance(value, bool)
                    for value in coordinates), "nonintegral field coordinate")
        require(any(coordinates), "zero integral coefficient must be omitted")
        coefficient = sum(value * pow(root, power, PRIME)
                          for power, value in enumerate(coordinates)) % PRIME
        if coefficient:
            answer[exponent] = coefficient
    return answer


def decode_modular_polynomial(raw) -> dict[tuple[int, ...], int]:
    require(isinstance(raw, list), "modular polynomial must be a list")
    answer: dict[tuple[int, ...], int] = {}
    previous = None
    for term in raw:
        require(isinstance(term, list) and len(term) == 2, "bad modular term")
        exponent = decode_exponent(term[0])
        require(previous is None or previous < exponent, "unsorted modular terms")
        previous = exponent
        coefficient = term[1]
        require(isinstance(coefficient, int) and not isinstance(coefficient, bool)
                and 0 < coefficient < PRIME, "noncanonical modular coefficient")
        answer[exponent] = coefficient
    return answer


def generator_hash(charts: list[dict]) -> str:
    generators = [chart["integral_generators"] for chart in charts]
    raw = json.dumps(generators, sort_keys=True,
                     separators=(",", ":")).encode("ascii")
    return hashlib.sha256(raw).hexdigest()


def dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return sum(a * b for a, b in zip(left, right))


def matvec(matrix: tuple[tuple[int, ...], ...], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(dot(row, vector) for row in matrix)


def matmul(left: tuple[tuple[int, ...], ...],
           right: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, ...], ...]:
    columns = tuple(zip(*right))
    return tuple(tuple(dot(row, column) for column in columns) for row in left)


def component_variables() -> tuple[dict[tuple[int, ...], int], ...]:
    first_ray = FAN_RAYS[0]
    first_points = tuple(point for point in POLYTOPE_POINTS
                         if dot(point, first_ray) >= 0)
    require(len(first_points) == len(PHI308_COORDS) == 35,
            "first-component coordinate count")
    variables = {point: index for index, point in enumerate(first_points)}
    answer = [dict() for _ in range(12)]
    power = tuple(tuple(int(row == column) for column in range(4))
                  for row in range(4))
    component = 0
    for _ in range(12):
        for point, variable in variables.items():
            answer[component][matvec(power, point)] = variable
        power = matmul(A_M, power)
        component = RAY_PERMUTATION[component]
    require(component == 0 and all(len(value) == 35 for value in answer),
            "component-variable orbit")
    return tuple(answer)


COMPONENT_VARIABLES = component_variables()


def add_exact_term(terms: dict[tuple[int, ...], tuple[int, ...]],
                   exponent: tuple[int, ...], coefficient: tuple[int, ...]) -> None:
    previous = terms.get(exponent, (0, 0, 0, 0))
    updated = tuple(a + b for a, b in zip(previous, coefficient))
    if any(updated):
        terms[exponent] = updated
    else:
        terms.pop(exponent, None)


def chart_exponent(point: tuple[int, ...], rays: tuple[tuple[int, ...], ...],
                   removed_component: int | None = None) -> tuple[int, ...]:
    removed_ray = FAN_RAYS[removed_component] if removed_component is not None else None
    exponent = tuple(dot(point, ray) + 1 - int(ray == removed_ray) for ray in rays)
    require(min(exponent) >= 0, "negative chart exponent")
    return exponent


def encode_exact_terms(terms: dict[tuple[int, ...], tuple[int, ...]]) -> list:
    return [[list(exponent), list(coefficient)]
            for exponent, coefficient in sorted(terms.items())]


def reconstruct_integral_generators(chart: int) -> list:
    rays = tuple(tuple(ray) for ray in expected_rays(chart))
    hypersurface: dict[tuple[int, ...], tuple[int, ...]] = {}
    for point, coefficient in zip(POLYTOPE_POINTS, NORM_COEFFICIENTS):
        add_exact_term(hypersurface, chart_exponent(point, rays),
                       (coefficient, 0, 0, 0))
    generators = [encode_exact_terms(hypersurface)]
    for component in PHI_SUBSET:
        terms: dict[tuple[int, ...], tuple[int, ...]] = {}
        for point, variable in COMPONENT_VARIABLES[component].items():
            add_exact_term(terms, chart_exponent(point, rays, component),
                           PHI308_COORDS[variable])
        generators.append(encode_exact_terms(terms))
    return generators


def expected_rays(chart: int) -> list[list[int]]:
    left_start, right_start = divmod(chart, 6)
    left = [UNIT_HEXAGON[left_start] + (0, 0),
            UNIT_HEXAGON[(left_start + 1) % 6] + (0, 0)]
    right = [(0, 0) + UNIT_HEXAGON[right_start],
             (0, 0) + UNIT_HEXAGON[(right_start + 1) % 6]]
    return [list(ray) for ray in sorted(left + right)]


def chart_action(chart: tuple[int, int]) -> tuple[int, int]:
    left, right = chart
    return ((right + 1) % 6, left)


def chart_orbits() -> tuple[tuple[int, ...], ...]:
    unseen = {(left, right) for left in range(6) for right in range(6)}
    orbits = []
    while unseen:
        seed = min(unseen, key=lambda item: 6 * item[0] + item[1])
        orbit = []
        cursor = seed
        while cursor not in orbit:
            orbit.append(cursor)
            cursor = chart_action(cursor)
        require(cursor == seed, "chart action did not close")
        unseen.difference_update(orbit)
        orbits.append(tuple(6 * left + right for left, right in orbit))
    return tuple(orbits)


def verify_chart(raw_chart: dict, root: int) -> int:
    require(isinstance(raw_chart, dict) and set(raw_chart) == CHART_KEYS,
            "chart schema keys differ")
    chart = raw_chart["chart"]
    require(isinstance(chart, int) and not isinstance(chart, bool)
            and 0 <= chart < 36, "chart")
    require(raw_chart["rays"] == expected_rays(chart), "ordered chart rays")
    raw_generators = raw_chart["integral_generators"]
    raw_coefficients = raw_chart["bezout_coefficients_mod_prime"]
    require(isinstance(raw_generators, list) and len(raw_generators) == 5,
            "generator count")
    require(isinstance(raw_coefficients, list) and len(raw_coefficients) == 5,
            "multiplier count")
    require(raw_generators == reconstruct_integral_generators(chart),
            "integral generator provenance mismatch")
    generators = [decode_integral_polynomial(value, root)
                  for value in raw_generators]
    coefficients = [decode_modular_polynomial(value)
                    for value in raw_coefficients]
    total: dict[tuple[int, ...], int] = {}
    for coefficient, generator in zip(coefficients, generators):
        total = p_add(total, p_mul(coefficient, generator))
    require(total == {ZERO_EXP: 1}, "modular Bezout identity is not one")

    planted = list(coefficients)
    planted[0] = p_add(planted[0], {ZERO_EXP: 1})
    planted_total: dict[tuple[int, ...], int] = {}
    for coefficient, generator in zip(planted, generators):
        planted_total = p_add(planted_total, p_mul(coefficient, generator))
    require(planted_total != {ZERO_EXP: 1}, "planted multiplier error survived")
    print(f"PASS chart {chart:02d} integral generators reduce to a literal GF(1009) unit identity")
    print(f"DATA chart {chart:02d} multiplier_terms={[len(value) for value in coefficients]}")
    return chart


def verify_payload(path: Path) -> None:
    compressed = path.read_bytes()
    with gzip.open(path, "rt", encoding="ascii") as handle:
        payload = json.load(handle)
    require(isinstance(payload, dict) and set(payload) == EXPECTED_KEYS,
            "payload schema keys differ")
    require(payload["schema"] == "oa-r030-proper-specialization-v2", "schema")
    require(payload["prime"] == PRIME and is_prime(PRIME), "prime")
    require(payload["field_polynomial_ascending"] == [1, 0, -1, 0, 1],
            "field polynomial")
    require(payload["generator_order"] == GENERATOR_ORDER, "generator order")
    require(payload["phi_subset"] == PHI_SUBSET, "Phi subset")
    require(hashlib.sha256(compressed).hexdigest() == EXPECTED_GZIP_HASH,
            "gzip payload hash")
    charts = payload["charts"]
    require(isinstance(charts, list) and len(charts) == 36, "chart count")
    require(generator_hash(charts) == EXPECTED_GENERATOR_HASH,
            "integral generator hash")

    root = payload["zeta12_mod_prime"]
    require(isinstance(root, int) and not isinstance(root, bool)
            and 0 < root < PRIME, "zeta residue")
    require((pow(root, 4, PRIME) - pow(root, 2, PRIME) + 1) % PRIME == 0,
            "cyclotomic relation")
    require(pow(root, 12, PRIME) == 1 and
            all(pow(root, divisor, PRIME) != 1 for divisor in (1, 2, 3, 4, 6)),
            "zeta residue does not have exact order 12")

    verified = tuple(sorted(verify_chart(chart, root) for chart in charts))
    require(verified == tuple(range(36)), "chart census")
    print("PASS all 36 integral generator payloads reconstruct from the source-locked height-308 vector and toric frames")
    print(f"DATA all36 gzip_sha256={hashlib.sha256(compressed).hexdigest()}")
    print("CONTROL planted multiplier perturbation rejected on all 36 charts")


def main() -> None:
    orbits = chart_orbits()
    require(tuple(sorted(len(value) for value in orbits)) == (12, 12, 12),
            "chart orbit lengths")
    require(tuple(min(value) for value in orbits) == (0, 1, 2),
            "chart representatives")
    path = HERE / "r030_mod1009_cover_all36.json.gz"
    require(path.is_file(), "missing all-chart payload")
    verify_payload(path)
    print("PASS exact C12 chart action has three length-12 orbits represented by 0,1,2")
    print("RESULT GF(1009) selected four-Phi base locus is empty on all 36 toric charts")
    print("THEOREM proper-image specialization promotes it to an empty Q(zeta_12) generic base locus")
    print("SCOPE coverage only: no characteristic-zero Bezout multipliers, residue row, Yukawa value or Serre-tail map")


if __name__ == "__main__":
    main()
