"""W91: the twisted coupling vector at weight -1/2 for every characteristic pair, exact. The rule (W91_RULE.md) was
committed before this script; the object, the cells and the priors are there.

The object (B1653's argument form; units (1, i, j, k) <-> thetas (1, 2, 4, 3); c = (-i, -1, -1, i); w = psi1 tau - psi2):
    V_s(tau) = c_s exp(i pi psi1^2 (ku^2 + kd^2) tau) theta_s(ku w|tau) theta_s(kd w|tau) / theta_1'(0|tau),
with theta_s(z|tau) = jtheta(s, pi z, e^{i pi tau}) and theta_1'(0|tau) = 2 pi eta^3. With q = e^{2 pi i tau}:
    exp(i pi tau k^2 psi1^2) theta[a1, a2](k w|tau)
        = sum_n e^{2 pi i a2 n} e^{-2 pi i (n + a1) k psi2} q^{(n + a1 + k psi1)^2 / 2}
times -i for theta_1 (a = (1/2, 1/2)); a = (1/2, 0), (0, 1/2), (0, 0) for theta_2, theta_4, theta_3. So
    V_s = (c_s / 2 pi) q^{-1/8} T_s(q) P(q),   P(q) = 1 / sum_m (-1)^m (2m + 1) q^{m(m+1)/2}   (Jacobi: eta^3),
where T_s is a sum of terms with exact rational exponents and exact root-of-unity phases. That is the deliverable:
exact,
with no rounding, and P's integer coefficients.

  U1  the series against direct evaluation (mpmath jtheta and eta) at five tau and twelve pairs, < 1e-40 relative
  U2  the null quaternion, sum_s V_s^2 = 0, < 1e-40 at every point and pair
  U3  the untwisted limit: V_1 = 0, and -2 pi V_i = theta2^2/eta^3, -2 pi i V_k = theta3^2/eta^3,
      -2 pi V_j = theta4^2/eta^3,
      with the eigenlines' exponents 1/8 (coefficient 4), -1/8 (2) and 3/8 (8)
  U4  the lowest exponent of each channel equals the closed form, for every pair at N = 9, 11 and 12
  U5  closure on chat1's two threads with the delivered generator, to 1e-30

Two interpretations, fixed here before the run (disclosed):
  - U4 is tested on the channels that are not identically zero. A channel is identically zero when its theta factor
    vanishes at every tau: theta_1 at a characteristic with k psi in Z^2 (delta or u-bar in the lattice). Those are
    counted and reported, not tested. "The lowest exponent" is the lowest with a non-zero coefficient, the phases at
    that exponent summed; the closed form is the minimum over n, m. A cancellation at the minimum fails U4.
  - U5 evaluates the generator to the exponent its points need (chat1's threads sit at Im tau ~ 0.02-0.04, where
    exponent 30 does not converge). The truncation at 30 is the delivery's format, not the object's definition. It
    evaluates the generator in factored form (the two exact theta sums over D(q)), which is the same object as T_s P
    expanded, without the expansion's cost at exponent ~1000.

Run: python3 the_twisted_coupling_vector.py  ->  the_twisted_coupling_vector.json beside it (and the delivery file).
"""
import gzip
import itertools
import json
from fractions import Fraction as Fr
from math import gcd, floor, ceil, sqrt
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
OUT = HERE / "the_twisted_coupling_vector.json"
DELIVERY = HERE / "the_twisted_coupling_vector_delivery.json.gz"
mp.mp.dps = 60
UNITS = ("1", "i", "j", "k")
THETA = {"1": 1, "i": 2, "j": 4, "k": 3}
CHAR = {1: (Fr(1, 2), Fr(1, 2)), 2: (Fr(1, 2), Fr(0)), 4: (Fr(0), Fr(1, 2)), 3: (Fr(0), Fr(0))}
CC = {"1": mp.mpc(0, -1), "i": mp.mpc(-1), "j": mp.mpc(-1), "k": mp.mpc(0, 1)}
SECTORS = {"up": (1, -4), "down": (1, 2), "leptons": (-3, 6)}
EMAX = 30


# ----------------------------------------------------------------------------------------------- the exact generator
def theta_terms(s, k, psi, emax):
    """exp(i pi tau k^2 psi1^2) theta_s(k w|tau) as {exponent: [phase turns, ...]} with exponents <= emax (exact)"""
    a1, a2 = CHAR[s]
    x = a1 + k * psi[0]
    out = {}
    lo, hi = floor(-x - sqrt(2 * emax) - 1), ceil(-x + sqrt(2 * emax) + 1)
    for n in range(lo, hi + 1):
        e = (n + x) ** 2 / 2
        if e > emax:
            continue
        turns = (a2 * n - (n + a1) * k * psi[1]) % 1
        if s == 1:
            turns = (turns - Fr(1, 4)) % 1                     # the factor -i
        out.setdefault(e, []).append(turns)
    return out


def product_terms(s, ku, kd, psi, emax):
    """T_s = (first theta) (second theta), exponents <= emax + 1/8 (the q^{-1/8} shifts them down)"""
    A, B = theta_terms(s, ku, psi, emax + Fr(1, 8)), theta_terms(s, kd, psi, emax + Fr(1, 8))
    out = {}
    for ea, pa in A.items():
        for eb, pb in B.items():
            e = ea + eb
            if e > emax + Fr(1, 8):
                continue
            out.setdefault(e, []).extend((x + y) % 1 for x in pa for y in pb)
    return out


def P_coeffs(jmax):
    """1 / sum_m (-1)^m (2m + 1) q^{m(m+1)/2}, integer coefficients to q^jmax"""
    d = [0] * (jmax + 1)
    m = 0
    while m * (m + 1) // 2 <= jmax:
        d[m * (m + 1) // 2] += (-1) ** m * (2 * m + 1)
        m += 1
    p = [0] * (jmax + 1)
    p[0] = 1
    for j in range(1, jmax + 1):
        p[j] = -sum(d[i] * p[j - i] for i in range(1, j + 1))
    return p


def V_series(ku, kd, psi, emax):
    """V_s = (c_s / 2 pi) q^{-1/8} T_s P as {exponent: complex coefficient}, exponents <= emax"""
    P = P_coeffs(int(emax) + 2)
    out = {}
    for u in UNITS:
        T = product_terms(THETA[u], ku, kd, psi, emax)
        ser = {}
        for e, turns in T.items():
            c = mp.fsum(mp.expjpi(2 * mp.mpf(t.numerator) / t.denominator) for t in turns)
            for j, pj in enumerate(P):
                E = e - Fr(1, 8) + j
                if E > emax:
                    break
                if pj:
                    ser[E] = ser.get(E, 0) + c * pj
        out[u] = {E: CC[u] / (2 * mp.pi) * v for E, v in ser.items()}
    return out


def ev_generator(ku, kd, psi, t, emax):
    """the delivered generator evaluated in factored form: (c_s / 2 pi) q^{-1/8} A(q) B(q) / D(q), with A and B the two
    exact theta sums (their exponents and phases from theta_terms) and D = sum_m (-1)^m (2m + 1) q^{m(m+1)/2}"""
    def ev_terms(T):
        return mp.fsum(mp.expjpi(2 * mp.mpf(x.numerator) / x.denominator)
                       * mp.exp(2j * mp.pi * t * mp.mpf(e.numerator) / e.denominator)
                       for e, ts in T.items() for x in ts)
    q = mp.exp(2j * mp.pi * t)
    D, m = 0, 0
    while m * (m + 1) // 2 <= emax + 2:
        D += (-1) ** m * (2 * m + 1) * q ** (m * (m + 1) // 2)
        m += 1
    out = {}
    for u in UNITS:
        A = ev_terms(theta_terms(THETA[u], ku, psi, emax))
        B = ev_terms(theta_terms(THETA[u], kd, psi, emax))
        out[u] = CC[u] / (2 * mp.pi) * mp.exp(-2j * mp.pi * t / 8) * A * B / D
    return out


def ev_series(ser, t):
    q = mp.exp(2j * mp.pi * t)
    return {u: mp.fsum(v * mp.exp(2j * mp.pi * t * mp.mpf(E.numerator) / E.denominator) for E, v in ser[u].items())
            for u in UNITS}


# ----------------------------------------------------------------------------------------------- direct evaluation
def eta(t):
    q = mp.exp(2j * mp.pi * t)
    return mp.exp(2j * mp.pi * t / 24) * mp.qp(q)


def V_direct(ku, kd, psi, t):
    w = mp.mpf(psi[0].numerator) / psi[0].denominator * t - mp.mpf(psi[1].numerator) / psi[1].denominator
    fac = mp.exp(1j * mp.pi * (mp.mpf(psi[0].numerator) / psi[0].denominator) ** 2 * (ku ** 2 + kd ** 2) * t)
    nome = mp.exp(1j * mp.pi * t)
    d1 = 2 * mp.pi * eta(t) ** 3
    return {u: CC[u] * fac * mp.jtheta(THETA[u], mp.pi * ku * w, nome) * mp.jtheta(THETA[u], mp.pi * kd * w, nome) / d1
            for u in UNITS}


def closed_lowest(s, ku, kd, psi):
    a1 = CHAR[s][0]
    m1 = min((n + a1 + ku * psi[0]) ** 2 for n in range(-40, 41)) / 2
    m2 = min((n + a1 + kd * psi[0]) ** 2 for n in range(-40, 41)) / 2
    return m1 + m2 - Fr(1, 8)


def zero_channel(s, k, psi):
    return s == 1 and (k * psi[0]).denominator == 1 and (k * psi[1]).denominator == 1


def lowest_nonzero(s, ku, kd, psi):
    T = product_terms(s, ku, kd, psi, Fr(6))
    for e in sorted(T):
        c = mp.fsum(mp.expjpi(2 * mp.mpf(t.numerator) / t.denominator) for t in T[e])
        if abs(c) > mp.mpf(10) ** -30:
            return e - Fr(1, 8), c
    return None, None


# ----------------------------------------------------------------------------------------------- the cells
def lines(N):
    return [(Fr(a, N), Fr(b, N)) for a in range(N) for b in range(N) if gcd(gcd(a, b), N) == 1]


def U1_U2():
    taus = [mp.mpc("0.11", "0.6"), mp.mpc("-0.23", "0.9"), mp.mpc("0.31", "1.4"), mp.mpc("0.05", "2.2"),
            mp.mpc("-0.4", "3.0")]
    pairs = [((Fr(1, 9), Fr(2, 9)), -3, 5), ((Fr(1, 9), Fr(2, 9)), 3, -1), ((Fr(1, 9), Fr(2, 9)), 3, -9),
             ((Fr(2, 11), Fr(5, 11)), -3, 5), ((Fr(2, 11), Fr(5, 11)), 3, -1), ((Fr(2, 11), Fr(5, 11)), 3, -9),
             ((Fr(5, 12), Fr(1, 12)), -3, 5), ((Fr(5, 12), Fr(1, 12)), 3, -1), ((Fr(5, 12), Fr(1, 12)), 3, -9),
             ((Fr(1, 3), Fr(0)), 2, 7), ((Fr(3, 7), Fr(1, 7)), 4, -6), ((Fr(0), Fr(0)), 0, 0)]
    worst1, worst2, worst_tail = 0, 0, 0
    for psi, ku, kd in pairs:
        ser = V_series(ku, kd, psi, Fr(EMAX))
        for t in taus:
            a, b = ev_series(ser, t), V_direct(ku, kd, psi, t)
            scale = max(abs(x) for x in b.values())
            worst1 = max(worst1, max(abs(a[u] - b[u]) for u in UNITS) / scale)
            worst2 = max(worst2, abs(mp.fsum(x ** 2 for x in b.values())) / mp.fsum(abs(x) ** 2 for x in b.values()))
            worst_tail = max(worst_tail, abs(mp.exp(2j * mp.pi * t)) ** EMAX)
    return ({"worst relative difference": float(worst1), "worst tail |q|^30": float(worst_tail),
             "holds": bool(worst1 < 1e-40 or worst1 < 10 * worst_tail)},
            {"worst |sum V^2| / sum |V|^2": float(worst2), "holds": bool(worst2 < 1e-40)})


def U3():
    ser = V_series(0, 0, (Fr(0), Fr(0)), Fr(EMAX))
    v1_zero = all(abs(v) < mp.mpf(10) ** -50 for v in ser["1"].values())
    lead = {}
    combos = {"e_i": {E: -2 * mp.pi * v for E, v in ser["i"].items()},
              "v+": {}, "v-": {}}
    th3 = {E: -2j * mp.pi * v for E, v in ser["k"].items()}
    th4 = {E: -2 * mp.pi * v for E, v in ser["j"].items()}
    for E in set(th3) | set(th4):
        combos["v+"][E] = th3.get(E, 0) + th4.get(E, 0)
        combos["v-"][E] = th3.get(E, 0) - th4.get(E, 0)
    for name, ser_ in combos.items():
        e0 = min(E for E, v in ser_.items() if abs(v) > mp.mpf(10) ** -40)
        lead[name] = (str(e0), round(float(abs(ser_[e0])), 12))
    ok = v1_zero and lead == {"e_i": ("1/8", 4.0), "v+": ("-1/8", 2.0), "v-": ("3/8", 8.0)}
    return {"V_1 identically zero": bool(v1_zero), "lowest exponents and |coefficients|": lead, "holds": bool(ok)}


def U4():
    tested = fails = zero = 0
    examples = []
    for N in (9, 11, 12):
        for psi in lines(N):
            for name, (qL, qR) in SECTORS.items():
                ku, kd = qL + qR, qL - qR
                for u in UNITS:
                    s = THETA[u]
                    if zero_channel(s, ku, psi) or zero_channel(s, kd, psi):
                        zero += 1
                        continue
                    tested += 1
                    got, _ = lowest_nonzero(s, ku, kd, psi)
                    want = closed_lowest(s, ku, kd, psi)
                    if got != want:
                        fails += 1
                        if len(examples) < 10:
                            examples.append({"N": N, "psi": [str(psi[0]), str(psi[1])], "sector": name, "unit": u,
                                             "got": str(got), "closed form": str(want)})
    return {"channels tested": tested, "identically zero, not tested": zero, "mismatches": fails,
            "first mismatches": examples, "holds": fails == 0}


def U5():
    """closure on chat1's threads with the generator: the cycle products of the closure phases against the law"""
    def mul(x, y):
        return (x[0] * y[0] + x[1] * y[2], x[0] * y[1] + x[1] * y[3],
                x[2] * y[0] + x[3] * y[2], x[2] * y[1] + x[3] * y[3])

    def word(wd):
        g = (1, 0, 0, 1)
        for ch in wd:
            g = mul(g, (1, 0, 1, 1) if ch == "L" else (1, 1, 0, 1))
        return g

    worst, cases = 0, 0
    for wd, N in (("LLRLLRRLRR", 9), ("LLLLRLRRRLRR", 11)):
        g = word(wd)
        A, B, C, D = g
        base = mp.mpf(-D) / C
        taus = [base + 1j / mp.mpf(C), base + (mp.mpf("0.3") + 1.2j) / mp.mpf(C)]
        floor_im = min(mp.im(t) for t in taus) / max(abs(C * t + D) for t in taus) ** 2
        need = Fr(int(45 * mp.log(10) / (2 * mp.pi * floor_im)) + 1)
        gt = [(A * t + B) / (C * t + D) for t in taus]
        need = max(need, Fr(int(45 * mp.log(10) / (2 * mp.pi * min(mp.im(x) for x in gt))) + 1))
        V0 = [ev_generator(0, 0, (Fr(0), Fr(0)), t, need) for t in taus]
        V0g = [ev_generator(0, 0, (Fr(0), Fr(0)), x, need) for x in gt]
        pi = {}
        for u in ("i", "j", "k"):
            best = None
            for u2 in ("i", "j", "k"):
                r = [V0g[n][u] / ((C * taus[n] + D) * V0[n][u2]) for n in range(2)]
                if best is None or abs(r[0] - r[1]) < best[0]:
                    best = (abs(r[0] - r[1]), u2)
            pi[u] = best[1]
        done = 0
        for a, b in itertools.product(range(N), repeat=2):
            if gcd(gcd(a, b), N) != 1:
                continue
            wg = ((a * A + b * C) % N, (a * B + b * D) % N)
            if wg not in ((a, b), ((-a) % N, (-b) % N)):
                continue
            c = ((a * (a * B + b * D) - b * (a * A + b * C)) // N) % N
            psi = (Fr(a, N), Fr(b, N))
            for name, (qL, qR) in SECTORS.items():
                Vt = [ev_generator(qL + qR, qL - qR, psi, t, need) for t in taus]
                Vg = [ev_generator(qL + qR, qL - qR, psi, x, need) for x in gt]
                chi = {u: [Vg[n][u] / Vt[n][pi[u]] / (V0g[n][u] / V0[n][pi[u]]) for n in range(2)]
                       for u in ("i", "j", "k")}
                seen, prod_ = set(), mp.mpc(1)
                cyc_len = 0
                for u in ("i", "j", "k"):
                    if u in seen:
                        continue
                    x, ln, p = u, 0, mp.mpc(1)
                    while x not in seen:
                        seen.add(x)
                        p *= chi[x][0]
                        x = pi[x]
                        ln += 1
                    law = mp.exp(-2j * mp.pi * c * (qL * qL + qR * qR) / N) ** ln
                    worst = max(worst, abs(p - law), max(abs(v[0] - v[1]) for v in chi.values()))
                cases += 1
            done += 1
            if done == 2:
                break
    return {"cases": cases, "worst (cycle law or tau-dependence)": float(worst), "holds": bool(worst < 1e-30)}


def delivery():
    """the exact generator's data for the Standard Model's sectors on every line with psi1 = 1/N (N = 9, 11, 12):
    per unit, the terms of T_s as [exponent, [phase turns]], and P's integer coefficients"""
    out = {"format": "V_s = (c_s / 2 pi) q^{-1/8} T_s(q) P(q); T_s terms {exponent: [phase turns]}; "
                     "c = (-i, -1, -1, i) for (1, i, j, k); P integer coefficients",
           "P": P_coeffs(EMAX + 2), "cases": []}
    for N in (9, 11, 12):
        for b in range(N):
            psi = (Fr(1, N), Fr(b, N))
            for name, (qL, qR) in SECTORS.items():
                case = {"N": N, "psi": [str(psi[0]), str(psi[1])], "sector": name, "k_u": qL + qR, "k_d": qL - qR,
                        "T": {}}
                for u in UNITS:
                    T = product_terms(THETA[u], qL + qR, qL - qR, psi, Fr(EMAX))
                    case["T"][u] = [[str(e), [str(t) for t in T[e]]] for e in sorted(T)]
                out["cases"].append(case)
    with gzip.open(DELIVERY, "wt", encoding="utf-8") as fh:
        json.dump(out, fh)
    return {"cases": len(out["cases"]), "file": DELIVERY.name}


def readouts():
    out = {}
    for N in (9, 11, 12):
        psi = (Fr(1, N), Fr(0))
        for name, (qL, qR) in SECTORS.items():
            ku, kd = qL + qR, qL - qR
            out[f"N={N}|{name}"] = {u: (None if zero_channel(THETA[u], ku, psi) or zero_channel(THETA[u], kd, psi)
                                        else str(closed_lowest(THETA[u], ku, kd, psi))) for u in UNITS}
    return out


def main():
    out = {"status": "W91: the twisted coupling vector, exact (script committed before its one run)"}
    out["U1"], out["U2"] = U1_U2()
    out["U3"] = U3()
    out["U4"] = U4()
    out["U5"] = U5()
    out["delivery"] = delivery()
    out["read-out: lowest exponents on psi = (1/N, 0)"] = readouts()
    out["cells"] = {k: out[k]["holds"] for k in ("U1", "U2", "U3", "U4", "U5")}
    out["every cell holds"] = all(out["cells"].values())
    OUT.write_text(json.dumps(out, indent=1, default=str) + "\n", encoding="utf-8")
    print("written", OUT.name)
    print(json.dumps(out["cells"], indent=1))


if __name__ == "__main__":
    main()
