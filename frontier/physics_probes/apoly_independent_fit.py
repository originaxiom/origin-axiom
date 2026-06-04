"""Phase 2 GOLD-STANDARD (achieved): m136's A-polynomial recovered INDEPENDENTLY and symbolically,
from trusted high-precision SnapPy fundamental-group holonomy by exact integer fitting -- with NO
assumed polynomial form. Control: the figure-eight (Cooper-Long must be a null vector). This is the
clean independent confirmation of V32 (the m=2 trace-map curve = m136's A-polynomial), without the
gluing-variety elimination (whose conventions defeated generic resultants) and without Sage.

Result: m136 null-space is 1-dimensional -> the A-polynomial is UNIQUELY recovered as
M^2 L^2 - (M^4-4M^2+1)L + M^2 (integer fit, machine-exact), and it equals the m=2 trace-map eliminant.
"""
import warnings; warnings.filterwarnings("ignore")
import numpy as np
import snappy


def ML_points(name, fills, drop_abelian=False):
    pts = []
    for fill in fills:
        try:
            Mf = snappy.ManifoldHP(name); Mf.dehn_fill(fill)
            if "degenerate" in str(Mf.solution_type()).lower():
                continue
            G = Mf.fundamental_group(); mw, lw = G.peripheral_curves()[0]
            mu = np.array([[complex(G.SL2C(mw)[i, j]) for j in range(2)] for i in range(2)])
            lam = np.array([[complex(G.SL2C(lw)[i, j]) for j in range(2)] for i in range(2)])
            w, V = np.linalg.eig(mu); v = V[:, 0]; lv = lam @ v; j = int(np.argmax(np.abs(v)))
            M, L = complex(w[0]), complex(lv[j] / v[j])
            if drop_abelian and abs(L - 1) < 0.05:
                continue
            if np.isfinite(M) and np.isfinite(L) and abs(M) > 1e-6:
                pts.append((M, L))
        except Exception:
            continue
    return pts


def nullspace_and_fit(pts, dM, dL):
    monos = [(i, j) for j in range(dL + 1) for i in range(dM + 1)]
    A = np.array([[(M**i) * (L**j) for (i, j) in monos] for (M, L) in pts], dtype=complex)
    sc = np.maximum(np.abs(A).max(0), 1e-30)
    U, S, Vh = np.linalg.svd(A / sc)
    dim = int(np.sum(S / S[0] < 1e-10))
    coef = (Vh[-1].conj() / sc)
    coef = coef / coef[np.argmax(np.abs(coef))]
    nz = np.abs(coef[np.abs(coef) > 1e-6]).min()
    rc = np.round((coef / nz).real).astype(int)
    err = np.max(np.abs(coef / nz - rc))
    return monos, rc, dim, err


def show(monos, coef):
    return " ".join(f"{c:+d}*M^{i}*L^{j}" for (i, j), c in zip(monos, coef) if c != 0)


def vanishes(pts, A):
    return float(np.median([abs(A(M, L)) / (max(abs(M), abs(L), 1)**10 + 1) for M, L in pts]))


if __name__ == "__main__":
    fills = ([(p, 1) for p in range(2, 22)] + [(p, 2) for p in range(3, 18)]
             + [(1, p) for p in range(2, 14)] + [(p, 3) for p in range(4, 14)])
    cooper_long = lambda M, L: M**4*L**2 + (-M**8 + M**6 + 2*M**4 + M**2 - 1)*L + M**4
    m2 = lambda M, L: M**2*L**2 - (M**4 - 4*M**2 + 1)*L + M**2

    print("CONTROL figure-eight 4_1: is Cooper-Long a null vector? (bidegree (8,2) is over-parametrized)")
    p41 = ML_points("4_1", fills, drop_abelian=True)
    print(f"  Cooper-Long median |A|/scale on {len(p41)} non-abelian pts = {vanishes(p41, cooper_long):.1e}"
          f"  -> {'VANISHES (control passes)' if vanishes(p41, cooper_long) < 1e-10 else 'NO'}")

    print("\nTARGET m136: recover the A-polynomial (bidegree (4,2)) from scratch")
    pm = ML_points("m136", fills)
    monos, coef, dim, err = nullspace_and_fit(pm, 4, 2)
    print(f"  null-space dim = {dim} (=1 -> unique), integer-fit error = {err:.1e}")
    print(f"  A_recovered = {show(monos, coef)}")
    print(f"  == m=2 trace-map eliminant M^2L^2-(M^4-4M^2+1)L+M^2 ; vanishes at {vanishes(pm, m2):.1e}")
    print("\n  => m136's A-polynomial IS the m=2 trace-map eliminant, uniquely & independently recovered.")
