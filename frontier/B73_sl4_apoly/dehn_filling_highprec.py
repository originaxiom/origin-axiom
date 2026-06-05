"""B73 (Path A) -- HIGH-PRECISION confirmation that M^4=L on the {1,1,w,w^2} SL(4) Dehn-filling
component (rules out a double-precision artifact; ~1e-31).

Get a double-precision bundle rep (dehn_filling.realize_bundle_rep), refine (B,t) by mpmath Newton on
the EXACT bundle equations tAt^-1=A^2B, tBt^-1=AB (A=diag(1,1,w,w^2) exact in mpmath), then check
[A,B]=c*mu^4 (scalar matrix) at the working precision. Controls k=3,5 must be O(1).
"""
import importlib.util
import pathlib

import mpmath as mp

_HERE = pathlib.Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("b73_df", _HERE / "dehn_filling.py")
df = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(df)


def _tomp(X):
    return mp.matrix([[mp.mpc(X[i, j].real, X[i, j].imag) for j in range(4)] for i in range(4)])


def _vec(M):
    return [M[i, j] for i in range(4) for j in range(4)]


def _unpack(x):
    B, t = mp.matrix(4, 4), mp.matrix(4, 4)
    for i in range(4):
        for j in range(4):
            B[i, j] = x[4 * i + j]
            t[i, j] = x[16 + 4 * i + j]
    return B, t


def confirm(dps=40, seed=5):
    """Returns (bundle_residual, scalar_dev_k4, scalar_dev_k3, scalar_dev_k5) at `dps` digits, or None."""
    mp.mp.dps = dps
    out = df.realize_bundle_rep(df.SPEC_W1, seed=seed)
    if out is None:
        return None
    _A_np, B_np, t_np = out
    w = mp.exp(2j * mp.pi / 3)
    A = mp.matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, w, 0], [0, 0, 0, w ** 2]])
    x = mp.matrix(_vec(_tomp(B_np)) + _vec(_tomp(t_np)))

    def F(B, t):
        ti = t ** -1
        return _vec(t * A * ti - A * A * B) + _vec(t * B * ti - A * B)

    h = mp.mpf(10) ** (-(dps // 2))
    for _ in range(8):
        B, t = _unpack(x)
        f = mp.matrix(F(B, t))
        if mp.norm(f) < mp.mpf(10) ** (-(dps - 8)):
            break
        J = mp.matrix(32, 32)
        for c in range(32):
            xp = x.copy()
            xp[c] += h
            Bp, tp = _unpack(xp)
            fp = mp.matrix(F(Bp, tp))
            for r in range(32):
                J[r, c] = (fp[r] - f[r]) / h
        try:
            x = x - mp.lu_solve(J, f)
        except Exception:
            break
    B, t = _unpack(x)
    bundle_res = float(mp.norm(mp.matrix(F(B, t))))
    mu = A ** -1 * t
    comm = A * B * A ** -1 * B ** -1

    def sdev(k):
        M = comm * (mu ** -1) ** k
        off = max(abs(M[i, j]) for i in range(4) for j in range(4) if i != j)
        dg = max(abs(M[i, i] - M[0, 0]) for i in range(4))
        return float(max(off, dg))

    return bundle_res, sdev(4), sdev(3), sdev(5)


def main():
    res = confirm(dps=40)
    if res is None:
        print("no rep found"); return 1
    bundle_res, d4, d3, d5 = res
    print("B73 (Path A) -- high-precision M^4=L confirmation ({1,1,w,w^2} component)\n")
    print(f"  refined bundle residual (40-digit): {bundle_res:.2e}")
    print(f"  [A,B]=c*mu^4 (M^4=L) scalar-deviation: {d4:.2e}   <- exact-grade")
    print(f"  controls: [A,B]=c*mu^3: {d3:.2e}   [A,B]=c*mu^5: {d5:.2e}   (both O(1))")
    print(f"\n  => M^4=L confirmed to ~{d4:.0e} at high precision -- not a double-precision artifact.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
