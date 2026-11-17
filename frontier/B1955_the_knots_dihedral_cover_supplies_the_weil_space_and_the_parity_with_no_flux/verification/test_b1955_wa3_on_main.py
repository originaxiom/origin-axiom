"""B1955's lock: the stored output of wa3_on_main.py (the parts that need SnapPy), and the exact algebra live."""
import itertools, json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
D = json.loads((HERE / "wa3_on_main.json").read_text())
z = np.exp(2j * np.pi / 5); psi = lambda x: z ** (x % 5)
P = np.array([[1.0 if (x + y) % 5 == 0 else 0.0 for y in range(5)] for x in range(5)])


def weil(c):
    T = np.diag([psi(c * x * x) for x in range(5)])
    for k in (1, 2, 3, 4):
        Fk = np.array([[psi(k * x * y) for y in range(5)] for x in range(5)]) / np.sqrt(5)
        for s in (1, -1, 1j, -1j):
            S = s * Fk
            if np.abs(np.linalg.matrix_power(S @ T, 3) - S @ S).max() < 1e-12 and np.abs(np.linalg.matrix_power(S, 4) - np.eye(5)).max() < 1e-12: return T, S


def group(T, S):
    key = lambda A: tuple(np.round(A.flatten(), 8)); G = {key(np.eye(5)): np.eye(5, dtype=complex)}; fr = list(G.values())
    while fr:
        nx = []
        for A in fr:
            for g in (T, S):
                N = A @ g
                if key(N) not in G: G[key(N)] = N; nx.append(N)
        fr = nx
    return list(G.values())


def test_the_cover_from_the_stored_run():
    assert D["A_dihedral_primes"] == [5] and D["A_onto_D25"] == 0 and 50 not in D["A_image_sizes_mod_25"]
    b = D["B"]
    assert b["longitude_trivial"] is True and b["meridian_fixed_sheets"] == 1 and b["meridian_order"] == 2
    assert b["cusp_degrees"] == [1, 2, 2] and b["deck_group_over_m004"] == 1 and b["deck_group_over_the_double_cover"] == 5
    assert D["C"]["three_cusped"][1] == "Z + Z + Z" and abs(float(D["C"]["three_cusped"][0]) - 5) < 1e-6
    assert D["C"]["degree_2"] == [[1, "Z/5 + Z"]]


def test_both_weil_classes_have_determinant_one_so_the_top_wedge_is_invariant():
    for c in (1, 2):
        T, S = weil(c); G = group(T, S)
        assert len(G) == 120 and max(abs(np.linalg.det(A) - 1) for A in G) < 1e-10
        assert np.abs(S @ S - P).max() < 1e-12
        ev = np.linalg.eigvals(T)
        assert max(abs(np.prod(ev[list(i)]) ** 5 - 1) for k in range(6) for i in itertools.combinations(range(5), k)) < 1e-10
    assert D["D"]["1"]["LR_distance_to_scalar_P"] > 0.5 and D["D"]["2"]["LR_distance_to_scalar_P"] > 0.5


def test_the_frame_does_not_see_the_class():
    tr = lambda c, n: np.trace(np.linalg.matrix_power(weil(c)[0], n))
    sig = lambda a, b: (tr(a, 2) * np.conj(tr(b, 2)) / (tr(a, 1) * np.conj(tr(b, 1))) ** 2).real
    assert abs(sig(1, 1) - 0.2) < 1e-12 and abs(sig(2, 2) - 0.2) < 1e-12 and abs(sig(1, 2) + 0.2) < 1e-12
    fixed = lambda n: sum(1 for a in range(5) for b in range(5) if (b - n * a) % 5 == b)
    assert fixed(2) / fixed(1) ** 2 == 0.2


def test_the_knots_class_and_level_25():
    from fractions import Fraction as Fr
    assert [(n * n * Fr(2, 5) / 2) % 1 for n in range(5)] == [0, Fr(1, 5), Fr(4, 5), Fr(4, 5), Fr(1, 5)]      # q = x^2/5 on the generator with (g, g) = 2/5
    assert [x for x in range(5) if (x * x - 3 * x + 1) % 5 == 0] == [4] and [x for x in range(25) if (x * x - 3 * x + 1) % 25 == 0] == []
    assert D["F"]["up_phase_orders"] == [25] and D["F"]["down_phase_orders"] == [5]
    run = (HERE / "wz1_checks_run.txt").read_text()
    assert "relative difference 1.5e-06" in run and "difference 3.9e-31" in run
