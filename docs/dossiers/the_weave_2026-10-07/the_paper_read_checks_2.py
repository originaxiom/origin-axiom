"""W99's addendum (relay §150): the paper read's second checks, of P9 draft 3 at main's 4cc3658a8.

A verification read, not a sealed arc: no rule, no prediction. Each check was first run in scratch (disclosed in the
NOTE's W99); this file repeats them in one run, and its output is committed as written.
- T3 part 3: dim M_k(rho) for rho = chi_eta^21 (x) rho_u at k = -1/2, 3/2, ..., 27/2, exactly. f is in M_k(rho) exactly
  when F = eta^3 f is in M_w(rho_u), w = k + 3/2, with the T-invariant component's constant term zero. M_w(rho_u) is the
  space of triples of degree-w polynomials in (A, B, C) = (theta2^2, theta3^2, theta4^2), modulo Jacobi's
  B^2 = A^2 + C^2,
  that are equivariant under S and T.
- The residue proposition (B1650; chat1's M10): the paper's displayed sum against chat1's form of the field's square.
- The turns of Delta: the lift's against rho's.

Run from the repository root: python3 docs/dossiers/the_weave_2026-10-07/the_paper_read_checks_2.py
"""
import json
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = {"what": "W99's addendum, the paper read's second checks of P9 draft 3 (main @ 4cc3658a8)"}

# ---------------------------------------------------------------- T3 part 3, exactly
A, B, C = sp.symbols("A B C")
I = sp.I
JAC = B**2 - A**2 - C**2
RT = sp.Matrix([[I, 0, 0], [0, 0, 1], [0, 1, 0]])                 # rho_u on (theta2^2, theta3^2, theta4^2)
RS = -I * sp.Matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]])


def red(e):
    return sp.expand(sp.rem(sp.expand(e), JAC, B))


def basis(w):
    return [A**a * C**(w - a) for a in range(w + 1)] + [B * A**a * C**(w - 1 - a) for a in range(w)]


def coords(e, bs):
    p = sp.Poly(red(e), A, B, C)
    out = [p.coeff_monomial(m) for m in bs]
    assert sp.expand(sum(c * m for c, m in zip(out, bs)) - red(e)) == 0
    return out


def sub_matrix(g, bs):
    v = g * sp.Matrix([A, B, C])
    rep = {A: v[0], B: v[1], C: v[2]}
    return sp.Matrix([coords(m.xreplace(rep), bs) for m in bs]).T


dims = {}
for w in range(1, 16, 2):
    bs = basis(w)
    n = len(bs)
    big = sp.Matrix.vstack(*[sp.kronecker_product(sp.eye(3), sub_matrix(g, bs)) - sp.kronecker_product(g, sp.eye(n))
                             for g in (RS, RT)])
    K = big.nullspace()
    vals = [m.subs({A: 0, B: 1, C: 1}) for m in bs]
    ctrow = sp.Matrix([[0] * n + vals + vals])                    # constant term of P_B + P_C
    rank = (ctrow * sp.Matrix.hstack(*K)).rank() if K else 0
    dims[str(sp.Rational(2 * w - 3, 2))] = {"dim M_w(rho_u)": len(K), "dim M_k(rho)": len(K) - rank}
OUT["T3 part 3: k -> dimensions"] = dims

# ---------------------------------------------------------------- the residue proposition (chat1's M10)
mp.mp.dps = 40
tau, z = mp.mpc(0.13, 1.07), mp.mpc(0.21, 0.37)
q = mp.exp(1j * mp.pi * tau)
t2, t3, t4 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q), mp.jtheta(4, 0, q)
eta = mp.exp(1j * mp.pi * tau / 12) * mp.qp(mp.exp(2j * mp.pi * tau))


def wp(x):
    return (mp.pi**2 * t2**2 * t3**2 * mp.jtheta(4, mp.pi * x, q)**2 / mp.jtheta(1, mp.pi * x, q)**2
            - mp.pi**2 / 3 * (t2**4 + t3**4))


rho = {"i": -t2**2 / (2 * mp.pi * eta**3), "j": -t4**2 / (2 * mp.pi * eta**3), "k": 1j * t3**2 / (2 * mp.pi * eta**3)}
zr = {"i": mp.mpf(1) / 2, "j": tau / 2, "k": (1 + tau) / 2}
rr = sum(v**2 for v in rho.values())
disp = sum(rho[r]**2 * wp(z - zr[r]) for r in rho)
const = sum(rho[r]**2 * wp(zr[r]) for r in rho)
square = -(rr * wp(z) - const)
OUT["the residue proposition at tau = 0.13+1.07i, z = 0.21+0.37i"] = {
    "the paper's displayed sum, sum rho_r^2 wp(z - z_r)": [float(mp.re(disp)), float(mp.im(disp))],
    "|sum rho_r^2 wp(z_r)|": float(abs(const)),
    "|the field's square, -[(rho.rho) wp(z) - sum rho_r^2 wp(z_r)]|": float(abs(square)),
    "wp(1e-8) * 1e-16 (Laurent check)": float(mp.re(wp(mp.mpf("1e-8")) * mp.mpf("1e-16"))),
}

# ---------------------------------------------------------------- the turns of Delta
s_mat = sp.exp(-I * sp.pi / 4) ** 21 * RS                      # rho(s), s the image of Delta^-1 = R L^-1 R


def turns(M):
    out = []
    for ev, mult in M.eigenvals().items():
        t = sp.nsimplify(sp.arg(sp.nsimplify(ev)) / (2 * sp.pi)) % 1
        out += [str(t)] * mult
    return sorted(out)


OUT["the turns of rho(s), the lift of Delta"] = turns(s_mat)
OUT["the turns of rho(Delta) = rho(s)^-1"] = turns(s_mat.inv())

text = json.dumps(OUT, indent=1, ensure_ascii=False) + "\n"
(HERE / "the_paper_read_checks_2.json").write_text(text, encoding="utf-8")
print(json.dumps(OUT, indent=1, ensure_ascii=False))
