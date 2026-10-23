"""B1737 (P-311; L233 (b)): the slope law's s(chi) against the chi-twisted Shintani zeta value at s = 0 of Z^2 modulo the
monodromy (Sczech's Eisenstein cocycle at the torsion point), computed independently of the slope instrument.
  A  for each level of the reader's list, every non-trivial monodromy-fixed character: the exact slope (B1438's
     exact_slopes, cyclotomic arithmetic) against Z(0, chi) = sum_{p in Pi(w, w')} chi(p) / (1 - chi(w))^2, Pi the half-open
     fundamental parallelogram of <gen> on the positive cone of the abelianised monodromy M (gen = M if its eigenvalues
     are positive, else M^2 with the value halved per generator); the claimed law s = Z - (1/2) #(-I)
  B  the control: Z at two different choices of w
  C  the trivial character: Shintani's constant-term zeta(0) against -Psi(M)/12, Psi = Rademacher's Phi - 3 sign(c(a + d))
    python3 -B the_slope_is_a_zeta_value.py
Importing computes nothing."""
import sys, io, json, math, cmath, itertools, contextlib, pathlib
from fractions import Fraction as Fr
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
ROOT = next(q for q in HERE.parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
LEVELS = [("+LR", 2), ("+LR", 3), ("+LR", 4), ("+LR", 5), ("+LLR", 3), ("+LLLR", 3), ("+LLRLR", 2),
          ("-LR", 1), ("-LR", 2), ("-LR", 3), ("-LR", 4), ("-LLRLR", 1), ("-LLLRLR", 1), ("-LLR", 2), ("-LLR", 3), ("-LLRR", 1)]


def _sl():
    sys.path.insert(0, str(ROOT / "frontier" / "B1438_the_slope_law" / "verification"))
    with contextlib.redirect_stdout(io.StringIO()):
        import slope_law as SL
    return SL


def abel_M(SL, eps, word, k):
    Phi = SL.ic.Phi_of(eps, word, k)
    ex = lambda w: (sum((g == 1) - (g == -1) for g in w), sum((g == 2) - (g == -2) for g in w))
    px, py = ex(Phi[1]), ex(Phi[2])
    return np.array([[px[0], py[0]], [px[1], py[1]]], dtype=object)          # columns: the images of e_x, e_y


def parallelogram(w, w2):
    """lattice points t1 w + t2 w2 with 0 < t1 <= 1, 0 <= t2 < 1 (exact)"""
    det = w[0] * w2[1] - w[1] * w2[0]
    xs = [0, w[0], w2[0], w[0] + w2[0]]; ys = [0, w[1], w2[1], w[1] + w2[1]]
    out = []
    for x in range(min(xs), max(xs) + 1):
        for y in range(min(ys), max(ys) + 1):
            t1 = Fr(x * w2[1] - y * w2[0], det); t2 = Fr(w[0] * y - w[1] * x, det)
            if 0 < t1 <= 1 and 0 <= t2 < 1: out.append((x, y))
    assert len(out) == abs(det)
    return out


def cone(M):
    Mf = np.array(M, dtype=float); ev, V = np.linalg.eig(Mf.T)           # left eigenvectors: rows l with l M = lambda l
    return ev.real, V[:, 0].real, V[:, 1].real


def Z0(M, i, j, N, which=0):
    ev, l1, l2 = cone(M)
    pos = (ev > 0).all(); G = M if pos else M.dot(M)
    chi = lambda v: cmath.exp(2j * math.pi * ((i * v[0] + j * v[1]) % N) / N)
    found = []
    for r in range(1, 12):
        for w in itertools.product(range(-r, r + 1), repeat=2):
            for sg in (1, -1):
                if sg * (l1 @ np.array(w, dtype=float)) > 0 and (l2 @ np.array(w, dtype=float)) * sg > 0 and abs(chi(w) - 1) > 1e-9 and w not in found:
                    found.append(w)
        if len(found) > which + 2: break
    w = found[which]; w2 = tuple(int(x) for x in G.dot(np.array(w, dtype=object)))
    assert abs(chi(w2) - chi(w)) < 1e-12, "the character is fixed by the generator"
    z = sum(chi(p) for p in parallelogram(w, w2)) / (1 - chi(w)) ** 2
    return z if pos else z / 2


def dedekind(h, k):
    return sum(Fr(0) if (i % k == 0 or (h * i) % k == 0) else (Fr(i, k) - Fr(1, 2)) * (Fr((h * i) % k, k) - Fr(1, 2)) for i in range(1, k))


def rademacher_Psi(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    if c == 0: Phi = Fr(b, d)
    else: Phi = Fr(a + d, c) - 12 * (1 if c > 0 else -1) * dedekind(d, abs(c))
    sgn = lambda x: (x > 0) - (x < 0)
    return Phi - 3 * sgn(c * (a + d))


def zeta0_trivial(M):
    """Shintani's constant-term formula on the positive cone modulo <gen> (Q = l1 l2)"""
    ev, l1, l2 = cone(M); pos = (ev > 0).all(); G = M if pos else M.dot(M)
    w = next(w for r in range(1, 9) for w in itertools.product(range(-r, r + 1), repeat=2)
             if (l1 @ np.array(w, dtype=float)) > 0 and (l2 @ np.array(w, dtype=float)) > 0)
    w2 = tuple(int(x) for x in G.dot(np.array(w, dtype=object)))
    tot = 0.0
    for l in (l1, l2):
        a, b = float(l @ np.array(w, dtype=float)), float(l @ np.array(w2, dtype=float))
        for p in parallelogram(w, w2):
            c = float(l @ np.array(p, dtype=float))
            tot += (c * c / 2 - c * (a + b) / 2 + a * a / 12 + b * b / 12 + a * b / 4) / (a * b)
    return (tot / 2) if pos else tot / 4


def main():
    SL = _sl(); rows, worst, worst_w, n = [], 0.0, 0.0, 0
    for st, k in LEVELS:
        eps = 1 if st[0] == "+" else -1; word = st[1:]
        N, F, S = SL.exact_slopes(eps, word, k); M = abel_M(SL, eps, word, k); nI = k if eps < 0 else 0
        zz = cmath.exp(2j * math.pi / N)
        for (i, j, _), s in S.items():
            if (i, j) == (0, 0): continue
            sv = sum(float(c) * zz ** e for e, c in enumerate(s.c))
            z = Z0(M, i, j, N); z2 = Z0(M, i, j, N, which=1)
            d = abs(sv - (z - nI / 2)); worst = max(worst, d); worst_w = max(worst_w, abs(z - z2)); n += 1
        triv = zeta0_trivial(M); psi = rademacher_Psi([[int(x) for x in r] for r in M])
        rows.append({"level": [st, k], "N": N, "characters": sum(1 for key in S if key[:2] != (0, 0)),
                     "M": [[int(x) for x in r] for r in M], "zeta0_trivial": triv, "-Psi/12": float(-psi / 12)})
    out = {"characters": n, "max |s - (Z - #(-I)/2)|": worst, "max |Z(w) - Z(w')|": worst_w, "levels": rows,
           "max |zeta0 + Psi/12| (trivial)": max(abs(r["zeta0_trivial"] - r["-Psi/12"]) for r in rows)}
    json.dump(out, open(HERE / "the_slope_is_a_zeta_value.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "levels"}, indent=1))
    for r in rows: print(r["level"], r["characters"], r["M"], round(r["zeta0_trivial"], 12), round(r["-Psi/12"], 12))


if __name__ == "__main__":
    main()
