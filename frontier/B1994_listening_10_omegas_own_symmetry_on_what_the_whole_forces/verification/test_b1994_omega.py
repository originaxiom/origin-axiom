"""B1994's lock: the committed run holds E1 to E3 (the run takes minutes; it is not rerun here)."""
import pathlib
HERE = pathlib.Path(__file__).resolve().parent


def test_omega_symmetry():
    t = (HERE / "omega_sym_run.txt").read_text()
    assert "the shortest: ['Lr', 'Rl'" in t and "W2: the generator Lr: its trace map acts on the readings as (Y, Z, X)" in t
    assert "order 3; eigenvalues on the triplet {1: 1, -1/2 - sqrt(3)*I/2: 1, -1/2 + sqrt(3)*I/2: 1}; fixed axis [[1, 1, 1]]" in t
    assert "W3: on the cube's vertices: fixed [(1, 1, 1), (-1, -1, -1)]" in t and "W3: on the cube's faces: fixed []" in t
    assert "(1, 1, 1): (1, 1, 1), (-1, -1, 1): (-1, 1, -1), (-1, 1, -1): (1, -1, -1), (1, -1, -1): (-1, -1, 1)" in t
