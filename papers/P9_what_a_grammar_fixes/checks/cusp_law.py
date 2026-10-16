"""The matter's defect toward the cusp of moduli (a check for the paper's Section 5).

With B1654's own route A (its sealed instrument, imported unchanged), D = sum_r c_r R_r^2 at tau = x + iy, and
q = e^{i pi tau}. The paper states the leading term
    D / (q |rho|^2)  ~  e^{-i pi x/2} [ 8 pi^2 y + 4 pi (1 + e^{-2 pi i x}) - 32 pi ln 2 ],
which at x = 0 is B1654's 8 pi^2 y + 8 pi (1 - 4 ln 2). The check computes both sides at x = 0, 3/10, 1/2, 1 and
y = 4, 5 and asserts a relative agreement better than 10^-3. It also shows that the x = 0 form alone fails off the axis.
"""
import math, pathlib
import numpy as np

ROOT = next(d for d in pathlib.Path(__file__).resolve().parents if (d / "frontier").is_dir())
SRC = sorted(ROOT.glob("frontier/B1654_*/verification/the_norm_of_the_boundary_class.py"))[0]
src = SRC.read_text()
src = src[:src.index("# ---------------------------------------------------------------- route B")]
src = src.replace("def thetas(z, tau):", "K = 40\ndef thetas(z, tau):", 1)
b1654 = {"__file__": str(SRC)}
exec(compile(src, str(SRC), "exec"), b1654)


def lhs(tau):
    R = b1654["R_A"](tau)
    c = {r: b1654["cA"](r, tau, 1e-5) for r in (2, 3, 4)}
    D = sum(c[r] * R[r] ** 2 for r in (2, 3, 4))
    return D / (np.exp(1j * np.pi * tau) * b1654["nR2"](R))


def leading(x, y):
    return np.exp(-1j * np.pi * x / 2) * (8 * np.pi ** 2 * y + 4 * np.pi * (1 + np.exp(-2j * np.pi * x)) - 32 * np.pi * math.log(2))


worst, off_axis = 0.0, 0.0
for x in (0.0, 0.3, 0.5, 1.0):
    for y in (4.0, 5.0):
        a, b = lhs(complex(x, y)), leading(x, y)
        rel = abs(a / b - 1); worst = max(worst, rel)
        naive = 8 * np.pi ** 2 * y + 8 * np.pi * (1 - 4 * math.log(2))
        off_axis = max(off_axis, abs(a / naive - 1))
        print(f"x = {x:4.2f}, y = {y:.0f}:  D/(q|rho|^2) = {a.real:+.6f}{a.imag:+.6f}i   leading = {b.real:+.6f}{b.imag:+.6f}i   rel {rel:.1e}")
print(f"worst relative deviation from the general leading term: {worst:.1e}")
print(f"the x = 0 form alone, off the axis: worst relative deviation {off_axis:.2f}")
assert worst < 1e-3 and off_axis > 0.5
print("all checks pass")
