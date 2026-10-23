"""B1731: among the zero-free Higgs lines F_a (B1730), the quadratic invariant det S = a.a, which is the Higgs's factor
of B1659's det Y(S, M) = 4 det S det M tr(eps S M^T) in B1656's frame.  No data.
  A  det S = a.a for S = a_i Q_I + a_j Q_J + a_k Q_K in the frame's own basis (random a)
  B  det S(F_a) = eta^(6-2a) th3^(2a) p(lambda), p = lambda^n + (1 - lambda)^n - 1, n = a/2, lambda = th2^4/th3^4
     (numerically, a in the one-unit and two-unit windows); F_2 null (Jacobi), F_6 = -48 eta^6
  C  exactly (sympy): for every odd n in [-15, 15] the roots of p's numerator outside {0, 1} -- lambda maps the upper
     half plane onto C minus {0, 1}, so det S(F_a) is zero-free iff there are none
  D  an explicit zero: at tau = e^{i pi/3}, lambda = e^{i pi/3} is a root of p for n = 5, 7, -1, ... (n = +-1 mod 6)
  E  in the frame (seeded points, no data, B1726's best rows not used): the Higgs F_2 gives m1 = 0 in every sector
     (det Y = 0 by B1659); F_6 gives m1 != 0 except on lines where B1716's exact zeros act
    python3 -B the_invariant.py      # writes the_invariant.json beside itself
Importing computes nothing."""
import sys, json, math, random, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
WINDOW = (-22, -10, -6, -2, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50)


def _mods():
    sys.path.insert(0, str(ROOT / "frontier" / "B1730_the_zero_free_higgs_lines" / "verification"))
    sys.path.insert(0, str(ROOT / "frontier" / "B1726_the_two_ingredients_replicated" / "verification"))
    import the_zero_free_lines as Z
    import census as K
    return Z, K


def F(a, t, th2, th3, th4, eta):
    eps = 1j ** ((a + 2) // 2); e = eta(t) ** (3 - a)
    return [e * eps * th2(t) ** a, e * eps * th4(t) ** a, e * 1j * th3(t) ** a]


def main():
    import numpy as np, mpmath as mp, sympy as sp
    Z, K = _mods(); _, th2, th3, th4, eta = Z._num(); B = K._modules()["B"]
    out = {}
    # A
    rng = np.random.default_rng(1731); dev = 0.0
    for _ in range(20):
        a = rng.normal(size=3) + 1j * rng.normal(size=3)
        dev = max(dev, abs(np.linalg.det(a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK) - a @ a))
    out["A_detS_minus_a.a"] = float(dev)
    # B
    resB = {}
    for t in (mp.mpc(0.13, 1.07), mp.mpc(-0.31, 1.42), mp.mpc(0.44, 0.93)):
        lam = th2(t) ** 4 / th3(t) ** 4
        for a in WINDOW:
            f = F(a, t, th2, th3, th4, eta); q = f[0] ** 2 + f[1] ** 2 + f[2] ** 2; n = a // 2
            pred = eta(t) ** (6 - 2 * a) * th3(t) ** (2 * a) * (lam ** n + (1 - lam) ** n - 1)
            r = resB.setdefault(str(a), {"rel_dev": 0.0, "abs_if_null": 0.0})
            if a == 2: r["abs_if_null"] = max(r["abs_if_null"], float(abs(q) / max(abs(x) for x in f) ** 2))
            else: r["rel_dev"] = max(r["rel_dev"], float(abs(q / pred - 1)))
            if a == 6: r["vs_-48eta6"] = max(r.get("vs_-48eta6", 0.0), float(abs(q / (-48 * eta(t) ** 6) - 1)))
    out["B_detS_closed_form"] = resB
    # C
    L = sp.symbols("L"); resC = {}
    for n in range(-15, 16, 2):
        p = sp.together(L ** n + (1 - L) ** n - 1)
        num = sp.Poly(sp.numer(p), L)
        if num.is_zero: resC[n] = "identically zero"; continue
        # count roots off {0, 1}: divide out the factors L and (L - 1)
        q = num
        while q.eval(0) == 0: q = sp.Poly(sp.quo(q.as_expr(), L), L)
        while q.eval(1) == 0: q = sp.Poly(sp.quo(q.as_expr(), L - 1), L)
        resC[n] = {"degree_of_numerator": num.degree(), "roots_off_0_1": q.degree()}
    out["C_roots_of_p_off_0_and_1"] = {str(k): v for k, v in resC.items()}
    out["C_zero_free_a"] = [2 * n for n, v in resC.items() if isinstance(v, dict) and v["roots_off_0_1"] == 0]
    out["C_null_a"] = [2 * n for n, v in resC.items() if v == "identically zero"]
    # D
    tz = mp.mpc(0.5, mp.sqrt(3) / 2); lz = th2(tz) ** 4 / th3(tz) ** 4
    out["D_lambda_at_e^{i pi/3}"] = [float(mp.re(lz)), float(mp.im(lz))]
    out["D_detS_at_e^{i pi/3}"] = {str(a): float(abs(sum(x ** 2 for x in F(a, tz, th2, th3, th4, eta))) / max(abs(x) for x in F(a, tz, th2, th3, th4, eta)) ** 2)
                                    for a in (2, 6, 10, 14, -2, 22)}
    # E
    M = K._modules(); te, col = M["te"], M["col"]
    rng = random.Random(4242); cnt = {"F6_m1_nonzero": 0, "F2_m1_nonzero": 0, "sectors": 0, "F6_zero_lines_orders": []}
    for _ in range(16):
        k, re_t, im_t = rng.randrange(266), rng.choice((0.15, 0.3, 0.45, 0.6, 0.75, 0.9)), rng.choice((2.3, 2.6, 2.9, 3.2))
        a_, b_ = K.lines()[k]; t = complex(re_t, im_t); w = float(a_) * t + float(b_); tm = mp.mpc(re_t, im_t)
        Lm = float(np.interp(im_t, [q[0] for q in col], [q[1] for q in col]))
        for aa in (6, 2):
            hv = [complex(x) for x in F(aa, tm, th2, th3, th4, eta)]; m = max(abs(x) for x in hv); hv = [x / m for x in hv]
            S = hv[0] * B.QI + hv[1] * B.QJ + hv[2] * B.QK
            for sec, (lf, rf) in K.SECT.items():
                x, yy = B.sector_twists(w, t, B.SIXY[lf], B.SIXY[rf]); R = B.residues(x, yy, t); c = B.cA(x, yy, t, R)
                u = {s: (math.sqrt(2 * math.pi * Lm + c[s]) * R[s] if c[s] is not None and 2 * math.pi * Lm + c[s] > 0 else 0) for s in B.UNITS}
                sv = np.linalg.svd(B.coupling(S, B.weighted_M(u)), compute_uv=False)
                nz = sv[2] / sv[0] > 1e-10
                if aa == 6:
                    cnt["sectors"] += 1; cnt["F6_m1_nonzero"] += int(nz)
                    if not nz: cnt["F6_zero_lines_orders"].append(math.lcm(a_.denominator, b_.denominator))
                else: cnt["F2_m1_nonzero"] += int(nz)
    out["E_frame"] = cnt
    json.dump(out, open(HERE / "the_invariant.json", "w"), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))


if __name__ == "__main__":
    main()
