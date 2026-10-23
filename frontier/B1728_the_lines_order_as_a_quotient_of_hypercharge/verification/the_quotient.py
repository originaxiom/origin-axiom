"""B1728 (P-296): the line's order as a quotient of hypercharge.  In B1656's frame (the functions B1723 sealed) a field of
charge q on the flat line w = alpha tau + b gets the twist (q alpha, 2 q b), so on a line of exact order N the frame sees the
charges 6Y mod N (Q 1, u -4, d 2, L -3, e 6).  Parts:
    A  step 1: thc(a + k, b + 2m) = e^{4 pi i m a} thc(a, b), so a charge shift by N multiplies a sector's bilinear, its
       residues, weights, M and Y by one phase; the ratios and |V| are unchanged (live, five lines, both readings)
    B  step 2: bil(y, x) = bil(x, y)^T, M(y, x) = M(x, y)^T and Y(y, x) = Y(x, y)^T for every S in span(i, j, k) (S and S~);
       the control S = 1, where eps S is antisymmetric, breaks it.  Step 3: bil(-x, -y, u) = -bil(x, y, -u), so negating
       both twists leaves the residues, the norms, M and Y unchanged
    C  the law, order by order: on two lines of each exact order 1-12 at one tau, which sector pairs coincide (up = down,
       down = leptons, up = leptons) against the charges mod N, up to swap and overall sign
    python3 -B the_quotient.py      # writes the_quotient.json beside itself
Importing computes nothing."""
import sys, json, math, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
TAU = 0.3 + 2.4j
L_END = 0.6
_B = {}


def frame():
    if not _B:
        sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification")); _a = sys.argv; sys.argv = ["x"]
        import b1656_funcs as B
        sys.argv = _a; _B["B"] = B
    return _B["B"]


def M_of(x, y, t=TAU, L=L_END):
    B = frame(); R = B.residues(x, y, t); c = B.cA(x, y, t, R)
    u = {s: (math.sqrt(2 * math.pi * L + c[s]) * R[s] if c[s] is not None and 2 * math.pi * L + c[s] > 0 else 0) for s in B.UNITS}
    return B.weighted_M(u)


def higgs(seed=1728):
    B = frame(); rng = np.random.default_rng(seed); a = rng.normal(size=3) + 1j * rng.normal(size=3)
    S = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK
    return {"S": S, "St": B.EPS @ np.conj(S) @ B.EPS.T}


def sector(alpha, b, ql, qr, S, t=TAU):
    B = frame(); w = float(alpha) * t + float(b)
    x, y = B.sector_twists(w, t, ql, qr)
    Y = B.coupling(S, M_of(x, y, t))
    sv = np.linalg.svd(Y, compute_uv=False)
    return Y, np.array([sv[1] / sv[0], sv[2] / sv[0]])


def dlog(p, q):
    return float(max((abs(math.log(a / c)) for a, c in zip(p, q) if a > 1e-12 and c > 1e-12), default=0.0))


def part_a():
    B = frame(); rng = np.random.default_rng(1); u = 0.01 * np.exp(2j * np.pi * np.arange(16) / 16); T = 2 * TAU; worst = 0.0
    for _ in range(20):
        a, b = rng.uniform(-1, 1, 2); k, m = int(rng.integers(-3, 4)), int(rng.integers(-3, 4))
        lhs = B.thc(a + k, b + 2 * m, u, T); rhs = np.exp(4j * np.pi * m * a) * B.thc(a, b, u, T)
        worst = max(worst, float(np.max(np.abs(lhs - rhs)) / np.max(np.abs(rhs))))
    H = higgs(); shift = 0.0; phase = 0.0
    for (al, bb), N in (((Fr(1, 3), Fr(2, 3)), 3), ((Fr(1, 4), Fr(1, 2)), 4), ((Fr(2, 5), Fr(1, 5)), 5), ((Fr(1, 6), Fr(1, 3)), 6), ((Fr(3, 10), Fr(1, 10)), 10)):
        for sec, (lf, rf) in SECT.items():
            ql, qr = B.SIXY[lf], B.SIXY[rf]
            for rn, S in H.items():
                Y0, r0 = sector(al, bb, ql, qr, S); Y1, r1 = sector(al, bb, ql + N, qr - 2 * N, S)
                shift = max(shift, dlog(r0, r1))
                lam = np.vdot(Y0.ravel(), Y1.ravel()) / np.vdot(Y0.ravel(), Y0.ravel())
                phase = max(phase, float(np.max(np.abs(Y1 - lam * Y0)) / np.max(np.abs(Y0))), abs(abs(lam) - 1))
    return {"thc_shift_identity_max_rel": worst, "charge_shift_by_N_ratio_dlog_max": shift, "Y_global_phase_residual_max": phase}


def part_b():
    B = frame(); rng = np.random.default_rng(2)
    out = {"bil_T": 0.0, "M_T": 0.0, "Y_T_S": 0.0, "Y_T_St": 0.0, "control_S_eq_1": 0.0, "bil_neg": 0.0, "M_neg": 0.0, "Y_neg_S": 0.0, "Y_neg_St": 0.0}
    for _ in range(3):
        x = (rng.uniform(-.5, .5), rng.uniform(-1, 1)); y = (rng.uniform(-.5, .5), rng.uniform(-1, 1)); uu = 0.13 + 0.07j
        out["bil_T"] = max(out["bil_T"], float(np.max(np.abs(B.bil(y, x, uu, TAU) - B.bil(x, y, uu, TAU).T))))
        Mxy, Myx = M_of(x, y), M_of(y, x)
        out["M_T"] = max(out["M_T"], float(np.max(np.abs(Myx - Mxy.T)) / np.max(np.abs(Mxy))))
        for rn, S in higgs(int(rng.integers(1 << 30))).items():
            Yxy, Yyx = B.coupling(S, Mxy), B.coupling(S, Myx)
            out["Y_T_" + rn] = max(out["Y_T_" + rn], float(np.max(np.abs(Yyx - Yxy.T)) / np.max(np.abs(Yxy))))
        Y1, Y2 = B.coupling(np.eye(2, dtype=complex), Mxy), B.coupling(np.eye(2, dtype=complex), Myx)
        out["control_S_eq_1"] = max(out["control_S_eq_1"], float(np.max(np.abs(Y2 - Y1.T)) / np.max(np.abs(Y1))))
        mx, my = (-x[0], -x[1]), (-y[0], -y[1])
        out["bil_neg"] = max(out["bil_neg"], float(np.max(np.abs(B.bil(mx, my, uu, TAU) + B.bil(x, y, -uu, TAU)))))
        Mn = M_of(mx, my); out["M_neg"] = max(out["M_neg"], float(np.max(np.abs(Mn - Mxy)) / np.max(np.abs(Mxy))))
        for rn, S in higgs(int(rng.integers(1 << 30))).items():
            Yp, Yn = B.coupling(S, Mxy), B.coupling(S, Mn)
            out["Y_neg_" + rn] = max(out["Y_neg_" + rn], float(np.max(np.abs(Yn - Yp)) / np.max(np.abs(Yp))))
    return out


def lines_of_order(N, k=2):
    out = []
    for j in range(N):
        for m in range(N):
            if math.gcd(math.gcd(j, m), N) == 1: out.append((Fr(j, N), Fr(m, N)))
    # two lines: the first with alpha != 0 and the first with alpha = 0 if any (else the second)
    a_nz = [l for l in out if l[0] != 0]; a_z = [l for l in out if l[0] == 0]
    pick = a_nz[:1] + (a_z[:1] if a_z else a_nz[1:2])
    return pick[:k]


def law(N):
    B = frame(); q = {f: B.SIXY[f] % N if N > 1 else 0 for f in ("Q", "u", "d", "L", "e")}
    neg = {f: (-B.SIXY[f]) % N if N > 1 else 0 for f in q}
    def same(s1, s2):
        (a, b), (c, d) = SECT[s1], SECT[s2]
        return any((q[a] == r[c] and q[b] == r[d]) or (q[a] == r[d] and q[b] == r[c]) for r in (q, neg))
    return {"up=down": same("up", "down"), "down=lep": same("down", "lep"), "up=lep": same("up", "lep")}


def part_c(tol=1e-8):
    B = frame(); H = higgs(); rows = []; agree = 0; total = 0
    for N in range(1, 13):
        pred = law(N)
        for (al, bb) in lines_of_order(N):
            r = {sec: {rn: sector(al, bb, B.SIXY[lf], B.SIXY[rf], S)[1] for rn, S in H.items()} for sec, (lf, rf) in SECT.items()}
            seen = {}
            for key, (s1, s2) in (("up=down", ("up", "down")), ("down=lep", ("down", "lep")), ("up=lep", ("up", "lep"))):
                d = max(dlog(r[s1][rn], r[s2][rn]) for rn in H)
                seen[key] = {"dlog": d, "equal": d < tol}
                zero = any(min(r[s][rn]) < 1e-12 for s in (s1, s2) for rn in H)
                if not zero:
                    total += 1; agree += (seen[key]["equal"] == pred[key])
            rows.append({"N": N, "line": [str(al), str(bb)], "law": pred, "seen": seen,
                         "masked_by_exact_zero": {s: bool(any(min(r[s][rn]) < 1e-12 for rn in H)) for s in SECT}})
    return {"rows": rows, "unmasked_pairs": total, "agree_with_law": agree}


def main():
    out = {"A": part_a(), "B": part_b(), "C": part_c()}
    json.dump(out, open(HERE / "the_quotient.json", "w"), indent=1)
    print(json.dumps({"A": out["A"], "B": out["B"], "C": {k: out["C"][k] for k in ("unmasked_pairs", "agree_with_law")}}, indent=1))
    for r in out["C"]["rows"]:
        print(r["N"], r["line"], {k: ("=" if v["equal"] else "%.1e" % v["dlog"]) for k, v in r["seen"].items()}, "law:", {k: v for k, v in r["law"].items() if v}, "zeros:", [s for s, z in r["masked_by_exact_zero"].items() if z])


if __name__ == "__main__":
    main()
