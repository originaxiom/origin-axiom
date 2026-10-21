"""B1688 -- the tricritical Ising model's fusion ring is Ising x Fibonacci (P-226): the check re-run live (one bijection; the
twists fix Ising nu = 7 times the conjugate Fibonacci, c = 7/10 mod 8); the bite: the Ising x Ising ring of the same size
is rejected, and the stored output agrees."""
import importlib.util, io, json, contextlib, itertools, pathlib
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1688_tricritical_ising_as_ising_times_fibonacci" / "verification"


def _run():
    spec = importlib.util.spec_from_file_location("tci", A / "tci_vs_ising_fib.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_fusion_and_twists_live():
    m = _run()
    assert len(m.match) == 1 and m.found == [{"ising_nu": 7, "fib": "Fib-bar", "c_mod_8": "7/10"}]
    # the bite: a wrong product of the same size (Ising x Z2) does not match the TCI ring
    Z = np.zeros((2, 2, 2), int); Z[0, 0, 0] = Z[0, 1, 1] = Z[1, 0, 1] = Z[1, 1, 0] = 1
    P = np.einsum("abc,xyz->axbycz", m.I, Z).reshape(6, 6, 6)
    assert not any(np.array_equal(m.N, P[np.ix_(p, p, p)]) for p in itertools.permutations(range(6)) if p[0] == 0)


def test_stored_output():
    d = json.loads((A / "tci_vs_ising_fib.json").read_text(encoding="utf-8"))
    assert d["fusion_equal"] and d["bijections"] == 1 and d["map"]["(1, 4)"] == "e x 1"
