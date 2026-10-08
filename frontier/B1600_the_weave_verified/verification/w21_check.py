#!/usr/bin/env python3
"""B1600, addendum: main's check of the SM seat's W21 (the hand by Hodge type) by an independent implementation.
V = (+)_p H^1(F2; chi_p (x) rho_Q) (W10's space).  The puncture loop [a, b] acts by -1 on every block, so each block is a
local system on the orbifold torus with one cone point of order two, Gamma = <a, b | [a, b]^2>, whose rational H^2 is
one-dimensional; the Hodge-Riemann form is the cup product H^1(Gamma; W) x H^1(Gamma; W-bar) -> H^2(Gamma; C) = C, times i,
with the sign fixed on the untwisted torus (i int dz ^ dz-bar = 2 Im tau > 0 for u = dz with periods (1, tau)).  The cup
product on the one-relator presentation is evaluated on the bar-resolution 2-cycle of the relator r = x_1^e_1 ... x_n^e_n,
    F = sum_i [r_<i | x_i^e_i]  -  sum_{e_i = -1} [x_i | x_i^-1],
so  (u u v)(F) = sum_i B(u(r_<i), rho(r_<i) v(x_i^e_i)) - sum_{e_i = -1} B(u(x_i), rho(x_i) v(x_i^-1)),  B the hermitian
form on W (rho_Q unitary).  Checks: F is a cycle (the pairing annihilates coboundaries); H(x, y) = x^dagger Hm y hermitian;
invariant under L, R and the sign, reversed by the swap; signature (3, 3); definite on W10's two triplets with opposite
signs; which triplet is positive, named by its character chi(L).  Writes w21_check.json."""
import json, pathlib, io, contextlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
with contextlib.redirect_stdout(io.StringIO()):
    import w10_check as W
I2 = np.eye(2, dtype=complex); PAR = W.PAR


def rep_letter(c, p):
    g = W.rho[c.lower()] * W.chi(p, c.lower())
    return g if c.islower() else np.linalg.inv(g)


def cocycle_on_word(z, word, p):
    val = np.zeros(2, dtype=complex); M = I2.copy()
    for c in word:
        if c.islower():
            val = val + M @ z[c]; M = M @ rep_letter(c, p)
        else:
            Mi = rep_letter(c, p); val = val + M @ (-(Mi @ z[c.lower()])); M = M @ Mi
    return val


def cup(u, v, p, relator="abABabAB"):
    B = lambda x, y: np.vdot(y, x)
    total = 0; prefix = ""; M = I2.copy()
    for c in relator:
        total += B(cocycle_on_word(u, prefix, p), M @ cocycle_on_word(v, c, p))
        if c.isupper():
            total -= B(cocycle_on_word(u, c.lower(), p), rep_letter(c.lower(), p) @ cocycle_on_word(v, c, p))
        prefix += c; M = M @ rep_letter(c, p)
    return total


def cup_trivial(u, v, relator="abABabAB"):
    val = lambda z, w: sum((z[c] if c.islower() else -z[c.lower()]) for c in w)
    total = 0; prefix = ""
    for c in relator:
        total += val(u, prefix) * np.conj(val(v, c))
        if c.isupper():
            total -= val(u, c.lower()) * np.conj(val(v, c))
        prefix += c
    return total


out = {}
tau = 0.3 + 1.1j; cal = 1j * cup_trivial({"a": 1.0, "b": tau}, {"a": 1.0, "b": tau})
SIGN = 1 if cal.real > 0 else -1
out["calibration"] = {"tau": [tau.real, tau.imag], "i*(dz u dz-bar)(F)": [cal.real, cal.imag], "2 Im tau": 2 * tau.imag, "sign": SIGN}
rng = np.random.default_rng(21); p0 = PAR[0]
w = rng.normal(size=2) + 1j * rng.normal(size=2)
du = {"a": rep_letter("a", p0) @ w - w, "b": rep_letter("b", p0) @ w - w}
v = {"a": rng.normal(size=2) + 1j * rng.normal(size=2), "b": rng.normal(size=2) + 1j * rng.normal(size=2)}
out["annihilates_coboundaries"] = bool(abs(cup(du, v, p0)) < 1e-10 and abs(cup(v, du, p0)) < 1e-10)
basis = []
for p in PAR:
    Bp, _ = W.BASES[p]
    for k in range(2):
        vec = Bp[:, k]; basis.append((p, {"a": vec[:2], "b": vec[2:]}))
n = len(basis); Q = np.zeros((n, n), dtype=complex)
for i, (p, zi) in enumerate(basis):
    for j, (q, zj) in enumerate(basis):
        if p == q:
            Q[i, j] = SIGN * 1j * cup(zi, zj, p)
Hm = Q.conj()                                     # H(x, y) = x^dagger Hm y
out["hermitian"] = bool(np.allclose(Hm, Hm.conj().T, atol=1e-10))
ev = np.linalg.eigvalsh((Hm + Hm.conj().T) / 2); out["eigenvalues"] = np.round(ev, 8).tolist(); out["signature"] = [int(sum(ev > 1e-9)), int(sum(ev < -1e-9))]
out["invariance"] = {name: {"invariant": bool(np.allclose(M.conj().T @ Hm @ M, Hm, atol=1e-8)), "reversed": bool(np.allclose(M.conj().T @ Hm @ M, -Hm, atol=1e-8))}
                     for name, M in (("L", W.ML), ("R", W.MR), ("sign", W.MS), ("swap", W.MP))}
Mx = np.vstack([np.kron(np.eye(6), g) - np.kron(g.T, np.eye(6)) for g in W.G_LR])
U_, s_, Vh = np.linalg.svd(Mx); null = Vh[-2:].conj(); X = None
for vv in null:
    Xc = vv.reshape(6, 6, order="F")
    if np.linalg.norm(Xc - np.trace(Xc) / 6 * np.eye(6)) > 1e-6:
        X = Xc; break
evX, VX = np.linalg.eig(X); groups = {}
for i, e in enumerate(evX):
    groups.setdefault(tuple(np.round([e.real, e.imag], 4)), []).append(i)
pieces = []
for k, idx in groups.items():
    Qp, _ = np.linalg.qr(VX[:, idx]); Ht = Qp.conj().T @ Hm @ Qp; evp = np.linalg.eigvalsh((Ht + Ht.conj().T) / 2)
    chL = np.trace(Qp.conj().T @ W.ML @ Qp)
    pieces.append({"dim": len(idx), "H_eigenvalues": np.round(evp, 8).tolist(), "chi_L": [round(chL.real, 6), round(chL.imag, 6)],
                   "chi_L_turns": round(float(np.angle(chL) / (2 * np.pi)) % 1, 4), "definite": "positive" if all(evp > 1e-9) else ("negative" if all(evp < -1e-9) else "indefinite")})
out["pieces"] = pieces
pos = [pc for pc in pieces if pc["definite"] == "positive"]; neg = [pc for pc in pieces if pc["definite"] == "negative"]
out["T_positive_T_bar_negative"] = bool(len(pos) == 1 and len(neg) == 1 and pos[0]["dim"] == 3 and neg[0]["dim"] == 3)
out["holomorphic_triplet_chi_L_turns"] = pos[0]["chi_L_turns"] if pos else None
json.dump(out, open(HERE / "w21_check.json", "w"), indent=1); print(json.dumps(out, indent=1))
