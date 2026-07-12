#!/usr/bin/env python3
"""Tail-aware canonical return-substitution engine for the B530 substitution.

A candidate induced substitution is accepted only if one of the exact identities

    h sigma^q(Theta(i)) = Theta(tau(i)) h
or
    sigma^q(Theta(i)) h = h Theta(tau(i))

holds for every return word i, with the same conjugating word h.

No terminal residue may be discarded.
"""

from __future__ import annotations

from collections import defaultdict
from functools import lru_cache
import itertools
import sympy as sp


SUB = {"a": "abAAB", "b": "aAB", "A": "abAB", "B": "aA"}
X = sp.symbols("x")


def grow(depth: int, seed: str = "a") -> str:
    word = seed
    for _ in range(depth):
        word = "".join(SUB[c] for c in word)
    return word


def factor_position_map(word: str, length: int) -> dict[str, list[int]]:
    result: dict[str, list[int]] = defaultdict(list)
    for i in range(len(word) - length + 1):
        result[word[i:i + length]].append(i)
    return dict(result)


def standard_return_words_from_positions(
    word: str,
    positions: list[int],
    trim: int = 2,
) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for k in range(trim, len(positions) - trim - 1):
        item = word[positions[k]:positions[k + 1]]
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def substitute_power(word: str, power: int) -> str:
    for _ in range(power):
        word = "".join(SUB[c] for c in word)
    return word


def common_suffix(words: list[str]) -> str:
    if not words:
        return ""
    bound = min(map(len, words))
    length = 0
    while length < bound and len({w[-1 - length] for w in words}) == 1:
        length += 1
    return words[0][-length:] if length else ""


def common_prefix(words: list[str]) -> str:
    if not words:
        return ""
    bound = min(map(len, words))
    length = 0
    while length < bound and len({w[length] for w in words}) == 1:
        length += 1
    return words[0][:length]


def minimal_parse(text: str, words: list[str]) -> tuple[int, ...] | None:
    best: list[tuple[int, ...] | None] = [None] * (len(text) + 1)
    best[len(text)] = ()

    for i in range(len(text) - 1, -1, -1):
        candidates: list[tuple[int, ...]] = []
        for index, word in enumerate(words):
            if text.startswith(word, i):
                tail = best[i + len(word)]
                if tail is not None:
                    candidates.append((index,) + tail)
        if candidates:
            best[i] = min(candidates)
    return best[0]


def exact_solutions(return_words: list[str], power: int) -> list[dict]:
    substituted = [substitute_power(word, power) for word in return_words]
    suffix = common_suffix(substituted)
    prefix = common_prefix(substituted)
    solutions: list[dict] = []

    for length in range(len(suffix) + 1):
        h = suffix[-length:] if length else ""
        codes: list[tuple[int, ...]] = []
        valid = True
        for image in substituted:
            full = h + image
            body = full[:-len(h)] if h else full
            parsed = minimal_parse(body, return_words)
            if parsed is None:
                valid = False
                break
            decoded = "".join(return_words[index] for index in parsed)
            if full != decoded + h:
                valid = False
                break
            codes.append(parsed)
        if valid:
            solutions.append({
                "side": "left",
                "power": power,
                "tail": h,
                "codes": tuple(codes),
            })

    for length in range(len(prefix) + 1):
        h = prefix[:length]
        codes: list[tuple[int, ...]] = []
        valid = True
        for image in substituted:
            full = image + h
            body = full[len(h):] if h else full
            parsed = minimal_parse(body, return_words)
            if parsed is None:
                valid = False
                break
            decoded = "".join(return_words[index] for index in parsed)
            if full != h + decoded:
                valid = False
                break
            codes.append(parsed)
        if valid:
            solutions.append({
                "side": "right",
                "power": power,
                "tail": h,
                "codes": tuple(codes),
            })

    return solutions


@lru_cache(maxsize=None)
def permutations(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.permutations(range(size)))


def relabel_codes(
    codes: tuple[tuple[int, ...], ...],
    permutation: tuple[int, ...],
) -> tuple[tuple[int, ...], ...]:
    size = len(codes)
    inverse = [0] * size
    for old, new in enumerate(permutation):
        inverse[new] = old

    result = []
    for new_domain in range(size):
        old_domain = inverse[new_domain]
        result.append(tuple(permutation[c] for c in codes[old_domain]))
    return tuple(result)


@lru_cache(maxsize=None)
def canonical_codes(
    codes: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    return min(relabel_codes(codes, p) for p in permutations(len(codes)))


def incidence(codes: tuple[tuple[int, ...], ...]) -> sp.Matrix:
    size = len(codes)
    return sp.Matrix([
        [
            sum(1 for symbol in codes[column] if symbol == row)
            for column in range(size)
        ]
        for row in range(size)
    ])


def codes_as_strings(codes: tuple[tuple[int, ...], ...]) -> list[str]:
    return ["".join(map(str, image)) for image in codes]


@lru_cache(maxsize=None)
def system_invariants(
    codes: tuple[tuple[int, ...], ...],
) -> tuple[sp.Matrix, sp.Expr, int, int]:
    matrix = incidence(codes)
    return (
        matrix,
        sp.factor(matrix.charpoly(X).as_expr()),
        int(matrix.det()),
        int(matrix.rank()),
    )


def canonical_induced_system(
    return_words: list[str],
    max_power: int = 2,
) -> dict | None:
    for power in range(1, max_power + 1):
        solutions = exact_solutions(return_words, power)
        if not solutions:
            continue

        ranked = []
        for solution in solutions:
            canonical = canonical_codes(solution["codes"])
            ranked.append((
                canonical,
                len(solution["tail"]),
                solution["side"],
                solution["tail"],
                solution,
            ))
        ranked.sort(key=lambda item: item[:4])
        canonical, _, _, _, selected = ranked[0]
        matrix, charpoly, determinant, rank = system_invariants(canonical)
        return {
            "power": power,
            "side": selected["side"],
            "tail": selected["tail"],
            "raw_codes": selected["codes"],
            "canonical_codes": canonical,
            "matrix": matrix,
            "charpoly": charpoly,
            "determinant": determinant,
            "rank": rank,
            "solution_count": len(solutions),
        }
    return None


def census(depth: int, max_length: int, max_power: int = 2) -> list[dict]:
    word = grow(depth)
    records: list[dict] = []

    for length in range(1, max_length + 1):
        positions_by_factor = factor_position_map(word, length)
        for factor, positions in positions_by_factor.items():
            return_words = standard_return_words_from_positions(word, positions)
            induced = canonical_induced_system(return_words, max_power=max_power)
            if induced is None:
                raise RuntimeError(
                    f"No exact induced system through power {max_power}: {factor!r}"
                )
            records.append({
                "n": length,
                "factor": factor,
                "return_words": tuple(return_words),
                "return_count": len(return_words),
                **induced,
            })
    return records


def original_matrix() -> sp.Matrix:
    original_codes = (
        (0, 1, 2, 2, 3),
        (0, 2, 3),
        (0, 1, 2, 3),
        (0, 2),
    )
    return incidence(original_codes)


def expected_polynomial(power: int, alphabet_size: int) -> sp.Expr:
    core = sp.factor((original_matrix() ** power).charpoly(X).as_expr())
    return sp.factor(X ** (alphabet_size - 4) * core)
