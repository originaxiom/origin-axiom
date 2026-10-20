"""B1679 -- the common point for every n, verified on main (the SM seat's W109 proof and W108 census). Live: main's
independent numerical search over SL(2,C)^n for characters fixed by the moves (seeded, small): at n = 2 under the record's
R and L the zeros are the quaternion point (0, 0, 0) and the trivial point (the bite: the search does find a non-trivial
common point where one exists); at n = 3 under the six R_ij every zero is trivial. Fricke's identity, the proof's step 2,
checked on random SL(2,C) pairs. Stored: the seat's checks (C1-C5), its W108 census, and main's full search."""
import importlib.util, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1679_the_common_point_for_every_n_verified"


def _ms():
    spec = importlib.util.spec_from_file_location("ms", A / "verification" / "main_check" / "main_search.py")
    src = (A / "verification" / "main_check" / "main_search.py").read_text().split("n3 = search(")[0]   # definitions only
    ns = {}; exec(compile(src, "main_search_defs", "exec"), ns); return ns


def test_the_search_finds_the_quaternion_point_and_only_the_trivial_point_at_three():
    ns = _ms(); ns["rng"] = np.random.default_rng(1679)
    n2 = {tuple(np.round(h, 4)) for h in ns["search"](2, [(0, 1, "R"), (1, 0, "L")], 30)}
    assert any(all(abs(x) < 1e-4 for x in h) for h in n2) and any(all(abs(x - 2) < 1e-4 for x in h) for h in n2)
    assert all(all(abs(x) < 1e-4 for x in h) or all(abs(x - 2) < 1e-4 for x in h) for h in n2)
    n3 = ns["search"](3, [(i, j, "R") for i in range(3) for j in range(3) if i != j], 30)
    assert n3 and all(np.allclose(h, 2, atol=1e-4) for h in n3)


def test_fricke_step_two():
    rng = np.random.default_rng(2)
    for _ in range(50):
        x = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); x /= np.sqrt(np.linalg.det(x))
        y = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2)); y /= np.sqrt(np.linalg.det(y))
        assert abs(np.trace(x @ y) + np.trace(x @ np.linalg.inv(y)) - np.trace(x) * np.trace(y)) < 1e-9


def test_stored_runs():
    r = A / "verification" / "received"
    w109 = (r / "the_record_count_for_every_n_run.txt").read_text()
    assert "cells: {'C1': True, 'C2': True, 'C3': True, 'C4': True, 'C5 solvability': True, 'C5 orders': True}" in w109
    assert "Groebner basis ['x1 - 2', 'x2 - 2', 'x3 - 2', 'y12 - 2', 'y13 - 2', 'y23 - 2', 'z - 2']" in w109
    m = (A / "verification" / "main_check" / "main_search_run.txt").read_text()
    assert "n = 3, the six R_ij: 119 zeros" in m
