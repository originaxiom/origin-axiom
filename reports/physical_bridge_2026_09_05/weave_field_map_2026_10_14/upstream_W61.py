"""W61: the Yukawa couplings as overlaps at the state W60 selected (tau = omega, a half-period hypercharge line w, the
Higgs copy p* = 3w with a trivial local system), in the T (x) T reading (W39) and the T-bar (x) T reading (B1615). The
rule (W61_RULE.md) was committed before this script.

  Q1  the algebra: for every pair of blocks and every Higgs channel, the coupling's equivariance and its form
  Q2  the sectors (up, down, lepton) at w = (1/2, 1/2), (1/2, 0), (0, 1/2): the 3 x 3 Yukawa matrices in both readings
  Q3  the numbers at omega: F's equivariance (W21's check), N(omega), the T (x) T integrand at sample points

Blocks and parities are written in halves: (1, 0) is the parity (1/2, 0), and (0, 0) the trivial block.

Run: python3 the_couplings_at_the_selected_state.py  ->  the_couplings_at_the_selected_state.json beside it.
"""
import json
import sys
from pathlib import Path

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_holomorphic_triplet_periods as PS  # noqa: E402  (W21's second route: rho_Q, the C_p, the periods, the norm)
import the_one_loop_potential_on_the_fibre as OP  # noqa: E402  (W59: the charges, omega)

OUT = HERE / "the_couplings_at_the_selected_state.json"
RA, RB = np.array(PS.RQ["a"], dtype=complex), np.array(PS.RQ["b"], dtype=complex)
BLOCKS = {(0, 0): np.eye(2, dtype=complex), (1, 0): np.array(PS.CONJ[(2, 0)], dtype=complex),
          (0, 1): np.array(PS.CONJ[(0, 2)], dtype=complex), (1, 1): np.array(PS.CONJ[(2, 2)], dtype=complex)}
PARITIES = [(1, 0), (0, 1), (1, 1)]
TOL = 1e-12


def add(c, d):
    return ((c[0] + d[0]) % 2, (c[1] + d[1]) % 2)


def invariant_form():
    """the bilinear forms B with rho(g)^T B rho(g) = B for g = a, b"""
    rows = []
    for g in (RA, RB):
        rows.append(np.kron(g.T, g.T) - np.eye(4))
    _, s, vh = np.linalg.svd(np.vstack(rows))
    null = vh[s.size - int(np.sum(s < 1e-10)):] if np.sum(s < 1e-10) else vh[-1:]
    J = null[-1].reshape(2, 2)
    return J / J[0, 1]


J = invariant_form()


def character(C, g):
    return complex(np.trace(C @ g @ np.linalg.inv(C) @ np.linalg.inv(g)) / 2)


def couple(c1, c2, p):
    X = BLOCKS[p]
    B = BLOCKS[c1].T @ J @ X @ BLOCKS[c2]
    H = BLOCKS[c2].conj().T @ X @ BLOCKS[c1]
    eq_tt = all(np.allclose(g.T @ B @ g, B, atol=TOL) for g in (RA, RB))
    eq_tbt = all(np.allclose(g.conj().T @ H @ g, H, atol=TOL) for g in (RA, RB))
    lam = H[0, 0]
    return {"c1 + c2 = p": add(c1, c2) == p, "T x T single-valued": bool(eq_tt),
            "T x T form antisymmetric": bool(np.allclose(B + B.T, 0, atol=TOL)),
            "T-bar x T single-valued": bool(eq_tbt),
            "T-bar x T form": "+I" if np.allclose(H, np.eye(2), atol=TOL) else (
                "-I" if np.allclose(H, -np.eye(2), atol=TOL) else "other"),
            "lambda": [float(lam.real), float(lam.imag)]}


def Q1():
    chars = {str(c): [character(C, g) for g in (RA, RB)] for c, C in BLOCKS.items()}
    rows, ok = {}, True
    for c1 in BLOCKS:
        for c2 in BLOCKS:
            for p in PARITIES:
                r = couple(c1, c2, p)
                rows[f"{c1} {c2} {p}"] = r
                ok &= (r["T x T single-valued"] == r["c1 + c2 = p"] == r["T-bar x T single-valued"])
                if r["c1 + c2 = p"]:
                    ok &= r["T x T form antisymmetric"] and r["T-bar x T form"] in ("+I", "-I")
    return {"the invariant form J": [[complex(x) for x in row] for row in J],
            "the blocks' characters (a, b)": {k: [[v.real, v.imag] for v in vs] for k, vs in chars.items()},
            "rows": rows, "holds": bool(ok)}


def Q3():
    mp.mp.dps = 20
    _, _, equiv = PS.periods(OP.OMEGA)
    n96, n48 = PS.l2_norm(OP.OMEGA, npts=96), PS.l2_norm(OP.OMEGA, npts=48)
    rng = np.random.default_rng(6101)
    worst = 0.0
    for _ in range(50):
        z = complex(rng.uniform(0.05, 0.95), 0) + rng.uniform(0.05, 0.95) * OP.OMEGA
        f1 = complex(mp.jtheta(3, mp.pi * z, mp.exp(2j * mp.pi * OP.OMEGA))
                     / mp.sqrt(mp.jtheta(1, mp.pi * z, mp.exp(1j * mp.pi * OP.OMEGA))))
        z2 = z + OP.OMEGA
        f2 = complex(mp.jtheta(3, mp.pi * z2, mp.exp(2j * mp.pi * OP.OMEGA))
                     / mp.sqrt(mp.jtheta(1, mp.pi * z2, mp.exp(1j * mp.pi * OP.OMEGA))))
        fv = np.array([f1, f2])
        for c1 in BLOCKS:
            for c2 in BLOCKS:
                for p in PARITIES:
                    if add(c1, c2) != p:
                        continue
                    B = BLOCKS[c1].T @ J @ BLOCKS[p] @ BLOCKS[c2]
                    worst = max(worst, abs(fv @ B @ fv) / float(np.vdot(fv, fv).real))
    holds = bool(equiv[3] and abs(n96 / n48 - 1) < 1e-8 and worst < 1e-12 and np.isfinite(n96))
    return {"W21's equivariance at omega, by theta numerator (1..4)": {str(k): bool(v) for k, v in equiv.items()},
            "N(omega) with 96 and 48 points": [float(n96), float(n48)],
            "the T x T integrand over |f|^2, largest at 50 points": worst, "holds": holds}, float(n96)


def Q2(N):
    gens = PARITIES
    sectors = {"up (Q u^c H)": ("Q", "u^c"), "down (Q d^c H~)": ("Q", "d^c"), "lepton (L e^c H~)": ("L", "e^c")}
    out, ok = {}, True
    for w in PARITIES:
        p = w  # p* = 3w = w for a half-period
        res = {}
        for name, (f1, f2) in sectors.items():
            q1, q2 = OP.CHARGES[f1], OP.CHARGES[f2]
            ytt = np.zeros((3, 3))
            ytbt = np.zeros((3, 3))
            for i, r in enumerate(gens):
                for k, s in enumerate(gens):
                    c1 = add(r, w) if q1 % 2 else r
                    c2 = add(s, w) if q2 % 2 else s
                    cp = couple(c1, c2, p)
                    if cp["T x T single-valued"]:
                        B = BLOCKS[c1].T @ J @ BLOCKS[p] @ BLOCKS[c2]
                        ytt[i, k] = float(np.max(np.abs(B + B.T))) * N / 2
                    if cp["T-bar x T single-valued"]:
                        ytbt[i, k] = cp["lambda"][0] * N / 2
            sv = np.linalg.svd(ytbt, compute_uv=False)
            res[name] = {"T x T: largest |Y|": float(np.max(np.abs(ytt))), "T-bar x T: Y": ytbt.tolist(),
                         "T-bar x T: singular values": sv.tolist()}
            ok &= float(np.max(np.abs(ytt))) < 1e-10 and np.allclose(sv, N / 2, rtol=1e-12)
            ok &= int(np.count_nonzero(np.abs(ytbt) > 0)) == 3
        ok &= res["down (Q d^c H~)"]["T-bar x T: Y"] == res["lepton (L e^c H~)"]["T-bar x T: Y"]
        out[f"w = {w} (halves), p* = {p}"] = res
    out["holds"] = bool(ok)
    return out


def main():
    q1 = Q1()
    q3, N = Q3()
    q2 = Q2(N)
    out = {"status": "W61: the couplings at the state W60 selected (the rule W61_RULE.md first; one run)",
           "Q1": q1, "Q2": q2, "Q3": q3}
    out["cells"] = {k: out[k]["holds"] for k in ("Q1", "Q2", "Q3")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=lambda x: [x.real, x.imag] if isinstance(x, complex) else float(x))
                   + "\n", encoding="utf-8")
    print(json.dumps(out["cells"], indent=1), "\nevery cell holds:", out["every cell holds"])


if __name__ == "__main__":
    main()
