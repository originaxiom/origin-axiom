"""B1676 -- the tick on the weave, verified on main (the SM seat's W107). Live, to word length 12: every odd-trace thread's
tick has a rank-one operator mean exactly when #L = #R (mod 8) (76 of 322), each rank-one line a body diagonal of the
parity basis, and the mean of the means a scalar. The bite: flipping the sign of one letter's lift breaks the mod-8
rule on some threads. Stored: main's full run to length 16 (916 of 3 822; 0.0799 I)."""
import contextlib, importlib.util, io, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1676_the_tick_on_the_weave_verified"


def _setup():
    spec = importlib.util.spec_from_file_location("om", ROOT / "frontier" / "B1617_the_weave_at_tau_omega" / "verification" / "weave_at_omega.py")
    om = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(om)
    T_of = lambda auto: om.cp.restrict(om.M_of(auto), om.cp.TB)
    TL, TR = T_of({"a": "a", "b": "ab"}), T_of({"a": "ab", "b": "b"})
    Ta, Tb = T_of({"a": "a", "b": "abA"}), T_of({"a": "baB", "b": "b"})
    _, P = np.linalg.eig(Ta + 0.3719 * Tb); P, _ = np.linalg.qr(P)
    return TL, TR, P


def _lyndon(nmax):
    w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        if m >= 2: yield "".join("LR"[c] for c in w)
        while len(w) < nmax: w.append(w[len(w) - m])
        while w and w[-1] == 1: w.pop()


def _census(TL, TR, P, nmax=12):
    odd = rank1 = agree = 0; means = []; trimax = True
    for w in _lyndon(nmax):
        M2 = np.eye(2, dtype=int)
        for ch in w: M2 = M2 @ (np.array([[1, 1], [0, 1]]) if ch == "L" else np.array([[1, 0], [1, 1]]))
        if int(np.trace(M2)) % 2 == 0: continue
        odd += 1
        T = np.eye(3, dtype=complex)
        for ch in w: T = T @ (TL if ch == "L" else TR)
        X, N = T.copy(), 1
        while not np.allclose(X, np.eye(3), atol=1e-9): X = X @ T; N += 1
        mean = sum(np.linalg.matrix_power(T, k) for k in range(N)) / N
        r = int(np.linalg.matrix_rank(mean, tol=1e-8))
        agree += (r == 1) == ((w.count("L") - w.count("R")) % 8 == 0)
        if r == 1:
            rank1 += 1; v = np.linalg.svd(P.conj().T @ mean @ P)[0][:, 0]
            trimax &= bool(np.allclose(abs(v), 1 / np.sqrt(3), atol=1e-6))
        means.append(P.conj().T @ mean @ P)
    avg = sum(means) / len(means)
    return odd, rank1, agree, trimax, avg


def test_the_tick_on_the_weave_to_length_12():
    TL, TR, P = _setup()
    odd, rank1, agree, trimax, avg = _census(TL, TR, P)
    assert (odd, rank1, agree) == (322, 76, 322) and trimax
    d = np.abs(np.diag(avg))
    assert np.allclose(d, d[0], rtol=1e-9) and np.abs(avg - np.diag(np.diag(avg))).max() < 0.1 * d[0]


def test_the_bite_the_lift_sign_moves_the_class():
    TL, TR, P = _setup()
    odd, rank1, agree, _, _ = _census(-TL, TR, P)
    assert agree < odd                                                 # the mod-8 rule is the convention's, not the line's


def test_stored_full_run():
    run = (A / "verification" / "main_check" / "tick_on_the_weave_main_run.txt").read_text()
    assert "odd trace: 3822" in run and "rank-one tick means: 916; zero: 2906" in run and "holds on 3822 of 3822" in run
    assert "diagonal [0.0799 0.0799 0.0799]" in run
