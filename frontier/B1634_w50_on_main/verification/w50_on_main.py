#!/usr/bin/env python3
"""B1634 -- THE SM SEAT'S W50 ON MAIN, AND W45'S MULTIPLIER FROM THE THETA CONSTANTS.  W50: on the owner's ruled branch (the
weave <L, R>, even ticks and positivity) the inner automorphisms by a and by b are not moves, so at a generic tau the
weave's residual on T is only scalars and couplings in tau alone are vector-valued modular forms; and T is exactly the
representation of eta^21 (theta_2^2, theta_3^2, theta_4^2).  If so, the theta constants fix the multiplier that B1632 found
W45's chi_{3/2} = 0 to depend on.  Main's own computation; no data.
 V1  every reduced word in L^{+-1}, R^{+-1} of length <= N whose H_1 matrix is I: its automorphism, classified as the
     identity, conj(c^{+-1}) with c = a b^-1 a^-1 b, conj(a^{+-1}) or conj(b^{+-1}), or another inner automorphism.
 V2  the lifts on T of those words: all scalars? (the weave's residual at a generic tau)
 V3  rho_theta from the classical laws (f(-1/tau) = tau^k rho(S) f(tau), f(tau + 1) = rho(T) f(tau), k = 23/2), checked
     numerically on the theta functions at two points; then whether there are scalars alpha, beta and an invertible M
     with M rho_theta(S) M^-1 = alpha S_lift and M rho_theta(T) M^-1 = beta T_lift, for each identification of
     (S_lift, T_lift) in {S~^{+-1}} x {L^{+-1}, R^{+-1}}; and where it holds, which theta goes to which parity line.
 V4  chi_k(rho_theta) by B1632's formula at every allowed half-integral weight: chi_{3/2} and chi_{23/2}.
Writes w50_on_main.json."""
import json, pathlib, os, importlib.util, itertools, cmath, math
import numpy as np
import mpmath as mp
HERE = pathlib.Path(__file__).resolve().parent
FRONTIER = pathlib.Path(os.environ.get("OA_FRONTIER", HERE.parents[1]))
spec = importlib.util.spec_from_file_location("w45", FRONTIER / "B1632_w45_verified_on_main" / "verification" / "w45_on_main.py")
w45 = importlib.util.module_from_spec(spec); spec.loader.exec_module(w45)
om, cp, TB = w45.om, w45.cp, w45.TB
N_MAX = int(os.environ.get("B1634_N", "10"))


def reduced_words(n, letters=("L", "l", "R", "r")):
    inv = {"L": "l", "l": "L", "R": "r", "r": "R"}
    out = [""]
    frontier = [""]
    for _ in range(n):
        nxt = []
        for w in frontier:
            for x in letters:
                if w and inv[x] == w[-1]: continue
                nxt.append(w + x)
        out += nxt; frontier = nxt
    return out


def main():
    out = {}
    L = {"a": "a", "b": "ab"}; R = {"a": "ab", "b": "b"}; Linv = {"a": "a", "b": "Ab"}; Rinv = {"a": "aB", "b": "b"}
    gens = {"L": L, "l": Linv, "R": R, "r": Rinv}
    ident = {"a": "a", "b": "b"}
    conj = lambda x: {"a": om.red(x + "a" + om.inv(x)), "b": om.red(x + "b" + om.inv(x))}
    c = "aBAb"
    named = {"id": ident, "conj(c)": conj(c), "conj(c^-1)": conj(om.inv(c)), "conj(a)": conj("a"), "conj(a^-1)": conj("A"),
             "conj(b)": conj("b"), "conj(b^-1)": conj("B")}
    counts = {k: 0 for k in named}; counts["other_inner_or_unmatched"] = 0; scal = []; nonscalar = 0; total = 0
    for w in reduced_words(N_MAX):
        f = dict(ident)
        for x in w: f = om.compose(f, gens[x])
        if not np.array_equal(om.h1(f), np.eye(2, dtype=int)): continue
        total += 1
        hit = next((k for k, g in named.items() if f == g), None)
        counts[hit if hit else "other_inner_or_unmatched"] += 1
        M = cp.restrict(om.M_of(f), TB)
        s = M[0, 0]
        if np.allclose(M, s * np.eye(3), atol=1e-9): scal.append(round((cmath.phase(s) / (2 * math.pi)) % 1, 6))
        else: nonscalar += 1
    out["V1"] = {"max_length": N_MAX, "words_with_H1_identity": total, "classified": counts}
    out["V2"] = {"lifts_all_scalar": nonscalar == 0, "nonscalar": nonscalar, "scalar_turns": sorted(set(scal))}
    # V3: rho_theta and a numerical check of the classical laws
    k = 23 / 2
    P13 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]], dtype=complex); P23 = np.array([[1, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    rS = cmath.exp(-23j * math.pi / 4) * P13
    rT = cmath.exp(7j * math.pi / 4) * np.diag([1j, 1, 1]) @ P23
    mp.mp.dps = 30
    def F(t):
        q = mp.exp(1j * mp.pi * t); eta = mp.exp(1j * mp.pi * t / 12) * mp.qp(mp.exp(2j * mp.pi * t))
        th = [mp.jtheta(n, 0, q) ** 2 for n in (2, 3, 4)]
        return np.array([complex(eta ** 21 * x) for x in th])
    checks = []
    for t in (mp.mpc(0.13, 1.21), mp.mpc(-0.31, 0.93)):
        lhsT = F(t + 1); rhsT = rT @ F(t)
        lhsS = F(-1 / t); rhsS = complex(t ** k) * (rS @ F(t))
        checks.append({"T_rel_err": float(np.abs(lhsT - rhsT).max() / np.abs(rhsT).max()), "S_rel_err": float(np.abs(lhsS - rhsS).max() / np.abs(rhsS).max())})
    out["V3_theta_law_checks"] = checks
    # the parity basis and the lifts
    Sa = om.compose(om.compose(R, Linv), R)
    TS = cp.restrict(om.M_of(Sa), TB); TL = cp.restrict(om.M_of(L), TB); TR = cp.restrict(om.M_of(R), TB)
    Ta, Tb = (cp.restrict(om.M_of(x), TB) for x in ({"a": "a", "b": "abA"}, {"a": "baB", "b": "b"}))
    _, Pb = np.linalg.eig(Ta + 0.3719 * Tb); Pb, _ = np.linalg.qr(Pb)
    chars = [(int(round(float(np.real(np.vdot(Pb[:, i], Ta @ Pb[:, i]))))), int(round(float(np.real(np.vdot(Pb[:, i], Tb @ Pb[:, i])))))) for i in range(3)]
    to_par = lambda A: Pb.conj().T @ A @ Pb
    Sopts = {"S~": to_par(TS), "S~^-1": to_par(np.linalg.inv(TS))}
    Topts = {"L": to_par(TL), "L^-1": to_par(np.linalg.inv(TL)), "R": to_par(TR), "R^-1": to_par(np.linalg.inv(TR))}
    roots = [cmath.exp(2j * math.pi * m / 48) for m in range(48)]
    found = []
    for (sn, BS), (tn, BT) in itertools.product(Sopts.items(), Topts.items()):
        for (ai, al), (bi, be) in itertools.product(enumerate(roots), enumerate(roots)):
            # M rS - al BS M = 0 and M rT - be BT M = 0, linear in vec(M)
            A1 = np.kron(np.eye(3), rS.T) - al * np.kron(BS, np.eye(3))
            A2 = np.kron(np.eye(3), rT.T) - be * np.kron(BT, np.eye(3))
            Asys = np.vstack([A1, A2]); _, s, Vh = np.linalg.svd(Asys)
            if s[-1] > 1e-8: continue
            Mv = Vh[-1].conj(); M = Mv.reshape(3, 3)
            if abs(np.linalg.det(M)) < 1e-6: continue
            img = [int(np.argmax(np.abs(M[:, j]))) for j in range(3)]       # theta index j -> parity line img[j]
            found.append({"S": sn, "T": tn, "alpha_48ths": ai, "beta_48ths": bi,
                          "theta2_to": chars[img[0]], "theta3_to": chars[img[1]], "theta4_to": chars[img[2]],
                          "monomial": bool(all(np.sum(np.abs(M[:, j]) > 1e-6) == 1 for j in range(3)))})
    out["V3"] = {"line_characters": chars, "equivalences": found[:24], "n_equivalences": len(found),
                 "identifications_with_an_equivalence": sorted({(f["S"], f["T"]) for f in found})}
    ch = {}
    for twok in range(-1, 28):
        kk = twok / 2
        if w45.allowed(kk, rS): ch[str(kk)] = round(w45.chi(kk, rS, rT), 9)
    out["V4"] = {"allowed_weights_chi": ch, "chi_3_2": ch.get("1.5"), "chi_23_2": ch.get("11.5"),
                 "T_eigen_turns": sorted(round((cmath.phase(e) / (2 * math.pi)) % 1, 6) for e in np.linalg.eigvals(rT))}
    json.dump(out, open(HERE / "w50_on_main.json", "w"), indent=1, default=str); print(json.dumps(out, indent=1, default=str)[:4000])


if __name__ == "__main__":
    main()
