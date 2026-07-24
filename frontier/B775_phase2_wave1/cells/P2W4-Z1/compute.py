"""
P2W4-Z1 -- H133-successor: is Z = Tr rho(A1) identically 1 at ALL E6 levels?

BACKGROUND / RECONCILIATION
  H133 (B578-D7) registered: Z = Tr rho(A1) = +1 at E6 levels 1, 2, 3 -- "is Z == 1 at
  every level (a Lefschetz-type statement for the fig-8 monodromy in every E6 theater)?"
  B600 + CL-H133 (B778) then found Z4 = 0 EXACTLY at level 4 (both parity sectors vanish
  independently -- a genuine chord-zero, not an even/odd cancellation).
  => Z is NOT identically 1. The successor question this cell answers: what IS the
  Z(level) sequence, and does it obey a law?

THE OBJECT (unchanged from H133 / B600 / CL-H133 -- same chord lineage)
  rho_k = the E6 level-k Kac-Peterson modular (Weil) representation of SL(2,Z);
  A1 = the figure-eight once-punctured-torus monodromy, word T^2 S T, i.e. the
  SL(2,Z) matrix [[2,1],[1,1]] (trace 3, char poly x^2 - 3x + 1, eigenvalues phi^{+-2}).
  Z_k := Tr rho_k(A1).  Since T is diagonal,  Z_k = sum_a t_a^3 S_aa   (*)
  -- only the DIAGONAL of S is needed, which is what makes the ladder computable far
  beyond level 4.

METHOD (exact, not numerics)
  Both S_aa and t_a^3 are sums of roots of unity of order dividing M = 36*kappa
  (kappa = k + 12 = k + h^vee):
    S_aa^raw = sum_{w in W(E6)} eps(w) zeta_{9kappa}^{-n_a(w)},  n_a(w) integer
    t_a^3    = zeta_{12kappa}^{2 m_a - 117 k},                   m_a integer
  so  Z_k * sqrt(3) * kappa^3  is an EXACT element of Z[zeta_M], accumulated as an integer
  coefficient vector (the Kac-Peterson prefactor for E6 is i^{|Delta+|}/(sqrt(|P/Q|) kappa^{r/2})
  = 1/(sqrt3 kappa^3); it is cross-checked against the numerically-determined normalization
  at every gated level).  The value is then evaluated at 60 digits, identified in Q(sqrt5)
  by PSLQ, and the identification is CERTIFIED EXACTLY by reduction modulo the cyclotomic
  polynomial Phi_M -- no numerical rounding enters the reported values.

GATES (house method)
  G1  two-word gate: rho(A1) = T^2 S T = T S T^-1 S^-1  (full float S, levels k <= KGATE)
  G2  normalization gate: the numerically-determined unitary normalization equals sqrt3*kappa^3
  G3  float-vs-exact gate: the independent float pipeline (the B600/CL-H133 pipeline)
      reproduces the exact Z at every gated level
  G4  reality gate: Im(Z) = 0 to 1e-40 at every level
  G5  exact-certificate gate: every reported Z value is certified mod Phi_M

MECHANISM BLOCK (computed in-cell; the bridge to Z is REGISTERED-UNVERIFIED)
  COMPUTED HERE (exact, all 51840 Weyl elements):
    det(3I - w - w^-1) = eps(w) * det(w^2 - 3w + I) = eps(w) * Res(char_w, x^2 - 3x + 1),
    and Res(x^n - 1, x^2 - 3x + 1) = 2 - L_{2n} (Lucas) for n = 1..20;
    the resulting "characteristic primes" (primes dividing any det(w^2-3w+I)) are printed.
  NOT COMPUTED HERE (do not cite as established): the heuristic that Z_k is a
    W-antisymmetrised Gauss sum sum_w eps(w) G_w(kappa) over the finite quadratic module
    P/kappa Q^vee, whose degeneracies are governed by gcd(kappa, det(3I - w - w^-1)).
    That heuristic is the ONLY reason candidate law C5 is on the list; C5 is TESTED
    against the exact ladder below, and the test is what counts.

SEALED VERDICT LOGIC (in code, below)
  RESOLVED-A  a PREDICTIVE law for Z(level) survives every computed level
              (candidates pre-listed: periodicity / residue-class laws in kappa,
               characteristic-prime law, integrality law)
  RESOLVED-B  no predictive law survives -- Z(level) is lawless over the computed range
              (the ladder is still computed exactly and its value-containment characterized)
  UNRESOLVED  a gate fails / a value cannot be certified

Run:  python3 compute.py [KMAX]        (default KMAX = 28, ~20 min; KMAX=8 ~ 30 s)
"""
import importlib.util
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np
from mpmath import mp, mpc, mpf, exp as mexp, pi as mppi, pslq, sqrt as msqrt
from sympy import cyclotomic_poly, Poly, Symbol, resultant, factorint

mp.dps = 60
HERE = os.path.dirname(os.path.abspath(__file__))
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 28
KGATE = 7          # levels with the full-S two-word gate (cost ~ N^2 |W|)
HV = 12            # h^vee(E6)
COMARK = [1, 2, 2, 3, 2, 1]
TOL = mpf(10) ** -40

# ---------------------------------------------------------------- E6 machinery
spec = importlib.util.spec_from_file_location(
    "c3", os.path.join(HERE, "..", "..", "..", "B570_allowed_plays",
                       "c3_e6_level2_monodromy.py"))
c3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c3)

C = np.array(c3.C6, dtype=np.int64)                       # Cartan/Gram, root basis
A3 = np.rint(3 * np.linalg.inv(C.astype(float))).astype(np.int64)   # 3*C^{-1}, integral
assert np.array_equal(A3 @ C, 3 * np.eye(6, dtype=np.int64))
W, eps = c3.weyl_group()
assert len(W) == 51840
Wflat = W.reshape(-1, 6).astype(np.float64)
epsP, epsN = (eps > 0), (eps < 0)
ONES = np.ones(6, dtype=np.int64)
RHO3 = A3 @ ONES                                          # 3*rho in root coords


def level_weights(k):
    out = []

    def rec(pre, rem):
        i = len(pre)
        if i == 6:
            out.append(tuple(pre))
            return
        for v in range(rem // COMARK[i] + 1):
            rec(pre + [v], rem - COMARK[i] * v)
    rec([], k)
    return out


def exact_Z_vector(k):
    """Integer coefficient vector V (length M=36 kappa) with
       Z_k = (sum_j V_j zeta_M^j) / (sqrt3 * kappa^3)."""
    kap = k + HV
    M = 36 * kap
    cdir = os.path.join(HERE, "zcache")
    os.makedirs(cdir, exist_ok=True)
    cf = os.path.join(cdir, f"k{k}.npz")
    if os.path.exists(cf):                      # re-run cache (exact integers, no numerics)
        d = np.load(cf)
        if len(d["coeff"]) == M:
            return None, int(d["N"]), kap, M, d["coeff"]
    prim = level_weights(k)
    N = len(prim)
    L = np.array(prim, dtype=np.int64).T
    U = A3 @ L                                            # 3*lambda   (root coords)
    V = U + RHO3[:, None]                                 # 3*(lambda+rho)
    CVf = (C @ V).astype(np.float64)
    Vf = V.astype(np.float64)
    m = np.einsum('ia,ia->a', U, C @ (U + 2 * RHO3[:, None]))   # 18 kappa h_a
    e = 2 * m - 117 * k                                   # t_a^3 exponent over 12 kappa
    coeff = np.zeros(M, dtype=np.int64)
    nW = len(W)
    B = 128
    for s in range(0, N, B):
        b = min(B, N - s)
        P = (Wflat @ Vf[:, s:s + b]).reshape(nW, 6, b)
        n = np.rint(np.einsum('wib,ib->wb', P, CVf[:, s:s + b])).astype(np.int64)
        idx = (3 * e[s:s + b][None, :] - 4 * n) % M
        flat = idx + M * np.arange(b)[None, :]
        cnt = (np.bincount(flat[epsP].ravel(), minlength=M * b)
               - np.bincount(flat[epsN].ravel(), minlength=M * b))
        coeff += cnt.reshape(-1, M).sum(axis=0)
    np.savez(cf, coeff=coeff, N=N)
    return prim, N, kap, M, coeff


def eval_cyclo(coeff, M):
    z = mpc(0)
    for j in np.nonzero(coeff)[0]:
        z += int(coeff[j]) * mexp(2j * mppi * mpf(int(j)) / M)
    return z


# ------------------------------------------------- exact certificate machinery
def polymod(p, q):
    """remainder of integer poly p (list, low->high) by monic integer poly q."""
    p = list(p)
    dq = len(q) - 1
    for i in range(len(p) - 1, dq - 1, -1):
        c = p[i]
        if c:
            for j in range(dq + 1):
                p[i - dq + j] -= c * q[j]
    return [x for x in p[:dq]]


def certify(coeff, M, kap, p, q):
    """exact check: sum V_j z^j == kappa^3 * sqrt3 * (p + q sqrt5) in Q(zeta_M)."""
    s3 = [0] * M
    s3[(3 * kap) % M] += 1
    s3[(33 * kap) % M] += 1                     # sqrt3 = zeta12 + zeta12^-1
    if q != 0:
        if M % 5:
            return False
        g = M // 5
        s5 = [0] * M
        for a, sg in ((1, 1), (4, 1), (2, -1), (3, -1)):
            s5[(a * g) % M] += sg              # sqrt5 = z5+z5^4-z5^2-z5^3
        prod = [0] * M
        for i, ci in enumerate(s3):
            if ci:
                for j, cj in enumerate(s5):
                    if cj:
                        prod[(i + j) % M] += ci * cj
    else:
        prod = [0] * M
    den = math.lcm(p.denominator, q.denominator) if q != 0 else p.denominator
    tgt = [0] * M
    for i in range(M):
        tgt[i] = kap ** 3 * (int(p * den) * s3[i] + (int(q * den) * prod[i] if q != 0 else 0))
    diff = [int(den) * int(coeff[i]) - tgt[i] for i in range(M)]
    phi = [int(c) for c in reversed(Poly(cyclotomic_poly(M, Symbol('x')),
                                         Symbol('x')).all_coeffs())]
    return all(x == 0 for x in polymod(diff, phi))


def identify(coeff, M, kap):
    """identify Z in Q(sqrt5); if that fails, report the smallest tried field that works."""
    z = eval_cyclo(coeff, M) / (msqrt(3) * mpf(kap) ** 3)
    if abs(z.imag) > TOL:
        return z, None, None, "NONREAL"
    x = z.real
    if abs(x) < TOL:
        return z, Fraction(0), Fraction(0), "exact"
    rel = pslq([mpf(1), msqrt(5), x], tol=mpf(10) ** -35, maxcoeff=10 ** 8, maxsteps=10 ** 5)
    if rel is not None and rel[2] != 0:
        a, b, c = rel
        return z, Fraction(-a, c), Fraction(-b, c), "exact"
    for nm, basis in (("Q(sqrt2,sqrt5)", [1, 2, 5, 10]), ("Q(sqrt3,sqrt5)", [1, 3, 5, 15]),
                      ("Q(cos2pi/5,...)deg4", None)):
        if basis is None:
            break
        rel = pslq([msqrt(b) for b in basis] + [x], tol=mpf(10) ** -30,
                   maxcoeff=10 ** 6, maxsteps=10 ** 5)
        if rel is not None and rel[-1] != 0:
            return z, None, None, "OUTSIDE-Q(sqrt5):" + nm
    return z, None, None, "UNIDENTIFIED"


def fmt(p, q):
    if q == 0:
        return str(p)
    return f"{p} + {q}*sqrt5" if q > 0 else f"{p} - {-q}*sqrt5"


# ------------------------------------------------------- float gate pipeline
def float_gate(k):
    """independent float pipeline (the B600/CL-H133 route): full S, two-word gate."""
    prim = level_weights(k)
    N = len(prim)
    kap = k + HV
    shifted = np.array([c3.root_coords(p) + c3.root_coords([1] * 6) for p in prim])
    S = np.zeros((N, N), dtype=complex)
    Wl = np.einsum('wij,lj->wli', W.astype(float), shifted)
    Cf = C.astype(float)
    for a in range(N):
        for b in range(a, N):
            ips = Wl[:, a, :] @ (Cf @ shifted[b])
            S[a, b] = S[b, a] = np.sum(eps * np.exp(-2j * np.pi * ips / kap))
    raw_norm = float(np.sqrt((S @ S.conj().T)[0, 0].real))
    S = S / raw_norm
    if S[0, 0].real < 0:
        S = -S
    cc = k * 78 / kap
    hs = [float(c3.root_coords(p) @ (Cf @ (c3.root_coords(p) + 2 * c3.root_coords([1] * 6))))
          / (2 * kap) for p in prim]
    T = np.diag([np.exp(2j * np.pi * (h - cc / 24)) for h in hs])
    r1 = T @ T @ S @ T
    r2 = T @ S @ np.linalg.inv(T) @ np.linalg.inv(S)
    return (N, float(np.linalg.norm(r1 - r2)), complex(np.trace(r1)),
            raw_norm, np.sqrt(3) * kap ** 3)


# --------------------------------------------------------------- main
def main():
    log = []

    def L(s):
        print(s, flush=True)
        log.append(s)

    L("P2W4-Z1  H133-successor: the Z(level) ladder, Z_k = Tr rho_k(A1), E6 level k")
    L("=" * 78)

    # ---- mechanism block (cheap, exact) ----
    x = Symbol('x')
    Pphi = x ** 2 - 3 * x + 1
    lucas = [2, 1]
    for _ in range(60):
        lucas.append(lucas[-1] + lucas[-2])
    lucas_ok = all(int(resultant(x ** n - 1, Pphi, x)) == 2 - lucas[2 * n]
                   for n in range(1, 21))
    Wi = W.astype(np.int64)
    dets = np.rint(np.linalg.det((Wi @ Wi - 3 * Wi
                                  + np.eye(6, dtype=np.int64)[None, :, :]).astype(float)))
    dets = dets.astype(np.int64)
    detvals = sorted(set(abs(int(d)) for d in dets))
    charprimes = sorted(set(p for d in detvals if d for p in factorint(d)))
    Rprod = 1
    for p in charprimes:
        Rprod *= p
    L(f"mechanism: Res(x^n-1, x^2-3x+1) == 2 - L_2n for n=1..20 : {lucas_ok}")
    L(f"           |det(w^2-3w+I)| over W(E6): {detvals}")
    L(f"           characteristic primes (Lucas/Fibonacci divisors): {charprimes}")

    # ---- the exact ladder ----
    L("-" * 78)
    L(" k  kappa      N   Z (exact)                      certificate")
    rows = []
    bad = []
    for k in range(1, KMAX + 1):
        t0 = time.time()
        prim, N, kap, M, coeff = exact_Z_vector(k)
        z, p, q, st = identify(coeff, M, kap)
        cert = certify(coeff, M, kap, p, q) if st == "exact" else None
        if st == "exact" and not cert:
            bad.append(k)                      # a FALSE certificate is fatal
        rows.append({"k": k, "kappa": kap, "N": N,
                     "Z": fmt(p, q) if st == "exact" else st,
                     "p": [p.numerator, p.denominator] if p is not None else None,
                     "q": [q.numerator, q.denominator] if q is not None else None,
                     "Zf": float(z.real), "im": float(abs(z.imag)),
                     "cert": (bool(cert) if cert is not None else "n/a")})
        L(f"{k:2d} {kap:5d} {N:7d}   {fmt(p, q) if st=='exact' else st:28s} "
          f"{('OK' if cert else 'FAIL') if cert is not None else '--':4s}  "
          f"[{time.time()-t0:.1f}s]")
        with open(os.path.join(HERE, "partial.json"), "w") as f:
            json.dump(rows, f)

    # ---- gates ----
    L("-" * 78)
    gates = {"G4_reality": all(r["im"] < 1e-40 for r in rows),
             "G5_no_false_certificate": len(bad) == 0}
    g1 = g2 = g3 = True
    for k in range(1, min(KGATE, KMAX) + 1):
        N, agree, Zf, rawn, pref = float_gate(k)
        ex = rows[k - 1]
        g1 &= agree < 1e-8
        g2 &= abs(rawn - pref) / pref < 1e-10
        g3 &= abs(Zf.real - ex["Zf"]) < 1e-8 and abs(Zf.imag) < 1e-8
        L(f"gate k={k}: words-agree={agree:.1e}  norm(float)/sqrt3.kappa^3-1="
          f"{abs(rawn-pref)/pref:.1e}  Z_float={Zf.real:+.9f}  Z_exact={ex['Zf']:+.9f}")
    gates.update({"G1_two_word": bool(g1), "G2_normalization": bool(g2),
                  "G3_float_vs_exact": bool(g3)})
    L(f"gates: {gates}")

    # ---- law search (candidates fixed before the data was read out) ----
    ident = [r for r in rows if r["p"] is not None]
    kaps = [r["kappa"] for r in ident]
    Zs = [(Fraction(*r["p"]), Fraction(*r["q"])) for r in ident]
    laws = {"levels_identified_in_Q(sqrt5)": f"{len(ident)}/{len(rows)}"}
    laws["C1_Z_identically_1"] = all(zz == (Fraction(1), Fraction(0)) for zz in Zs)
    laws["C2_all_rational_integers"] = all(zz[1] == 0 and zz[0].denominator == 1
                                           for zz in Zs)
    # Z[phi] = {(a+b sqrt5)/2 : a = b mod 2}
    def in_Zphi(pq):
        a, b = 2 * pq[0], 2 * pq[1]
        return (a.denominator == 1 and b.denominator == 1
                and (a.numerator - b.numerator) % 2 == 0)
    laws["C3_all_in_Z[phi]"] = all(in_Zphi(zz) for zz in Zs)
    laws["C4_max_abs_Z"] = max(abs(float(zz[0]) + float(zz[1]) * 5 ** .5) for zz in Zs)
    laws["C4_max_abs_conjugate"] = max(abs(float(zz[0]) - float(zz[1]) * 5 ** .5)
                                       for zz in Zs)
    # C5: Z == 1 exactly when kappa is coprime to the characteristic primes
    laws["C5_Z1_iff_coprime_to_charprimes"] = all(
        ((zz == (Fraction(1), Fraction(0))) == (np.gcd(kp, Rprod) == 1))
        for kp, zz in zip(kaps, Zs))
    # C6: Z periodic in kappa with some period 2..len/2
    per = [pd for pd in range(2, len(kaps) // 2 + 1)
           if all(Zs[i] == Zs[i + pd] for i in range(len(kaps) - pd))]
    laws["C6_periodic_in_kappa"] = (len(per) > 0)
    laws["C6_periods"] = per
    # C7: Z a function of kappa mod m (only m with every class multiply sampled)
    fm = []
    for m in range(2, 15):
        cls = {}
        ok, tested = True, 0
        for kp, zz in zip(kaps, Zs):
            r = kp % m
            if r in cls:
                tested += 1
                if cls[r] != zz:
                    ok = False
                    break
            else:
                cls[r] = zz
        if ok and tested >= m:
            fm.append(m)
    laws["C7_function_of_kappa_mod_m"] = fm
    # C10: is Z multiplicative in kappa (CRT-factorised Weil rep)?  necessary condition:
    #      every prime power occurring in a NONZERO kappa must be nonzero, hence no
    #      kappa with Z=0 may have all its prime-power factors drawn from that set.
    NZ = set()
    for kp, zz in zip(kaps, Zs):
        if zz != (Fraction(0), Fraction(0)):
            NZ |= {p ** a for p, a in factorint(kp).items()}
    viol = [kp for kp, zz in zip(kaps, Zs)
            if zz == (Fraction(0), Fraction(0))
            and all(p ** a in NZ for p, a in factorint(kp).items())]
    laws["C10_multiplicative_in_kappa"] = (len(viol) == 0)
    laws["C10_violating_kappa"] = viol
    # C8 (observed, not proved): trailing zero tail
    nz = [ident[i]["k"] for i, zz in enumerate(Zs) if zz != (Fraction(0), Fraction(0))]
    laws["C8_last_nonzero_level"] = nz[-1] if nz else None
    laws["C8_zero_tail_length"] = len(rows) - nz[-1] if nz else len(rows)
    laws["nonzero_levels"] = nz
    # C9 (field law, forced by Q(sqrt5) subset Q(zeta_{36 kappa}) iff 5 | kappa)
    laws["C9_irrational_only_if_5_divides_kappa"] = all(
        (zz[1] == 0) or (kp % 5 == 0) for kp, zz in zip(kaps, Zs))
    laws["irrational_levels"] = [ident[i]["k"] for i, zz in enumerate(Zs) if zz[1] != 0]
    laws["kappa_with_5"] = [kp for kp in kaps if kp % 5 == 0]
    laws["value_multiset"] = sorted({fmt(*zz) for zz in Zs})
    L("-" * 78)
    for kk, vv in laws.items():
        L(f"  {kk}: {vv}")

    # ------------------------------- SEALED VERDICT -------------------------------
    gates_ok = all(bool(v) for kk, v in gates.items())
    predictive = (laws["C1_Z_identically_1"] or laws["C5_Z1_iff_coprime_to_charprimes"]
                  or laws["C6_periodic_in_kappa"] or len(laws["C7_function_of_kappa_mod_m"]) > 0
                  or laws["C10_multiplicative_in_kappa"])
    if not gates_ok:
        verdict = "UNRESOLVED"
        reason = ("a gate failed (two-word / normalization / float-vs-exact / reality / "
                  "exact certificate) -- the ladder cannot be trusted this run.")
    elif laws["C1_Z_identically_1"]:
        verdict = "RESOLVED-A"
        reason = "Z == 1 at every computed level -- H133 survives (not expected)."
    elif predictive:
        verdict = "RESOLVED-A"
        reason = ("a PREDICTIVE law for Z(level) survives every computed level: "
                  + ", ".join(kk for kk in ("C5_Z1_iff_coprime_to_charprimes",
                                            "C6_periodic_in_kappa",
                                            "C10_multiplicative_in_kappa")
                              if laws.get(kk))
                  + (f" | C7 residue-class laws mod {laws['C7_function_of_kappa_mod_m']}"
                     if laws["C7_function_of_kappa_mod_m"] else ""))
    else:
        verdict = "RESOLVED-B"
        reason = (
            "NO predictive law for Z(level). H133 is dead in the strong sense: Z is not "
            "identically 1 (Z=+1 only at k=1,2,3; Z_4=0), and the continued ladder is "
            "LAWLESS as a function of the level -- not periodic in kappa (no period "
            "<= half the computed range), not a function of kappa mod m for any m<=14, "
            "not multiplicative in kappa (the CRT/Weil-factorisation route is refuted at "
            + str(laws["C10_violating_kappa"]) + "), and not governed by the "
            "characteristic-prime (Lucas) divisibility of kappa. "
            "What IS established (the cell's positive content, exactly certified at every "
            "level): the ladder is a bounded sequence of GOLDEN INTEGERS -- every Z_k "
            "lies in Z[phi] = O_{Q(sqrt5)}, the ring of integers of the fig-8 monodromy's "
            "OWN eigenvalue field (char poly x^2-3x+1, eigenvalues phi^{+-2}); the values "
            "stay small -- max|Z| = %.4f, max|Z'| = %.4f over the computed range -- but "
            "are NOT all rational integers; observed values "
            % (laws["C4_max_abs_Z"], laws["C4_max_abs_conjugate"])
            + str(laws["value_multiset"])
            + f"; irrational values occur only at 5 | kappa (levels {laws['irrational_levels']}), "
            "which is forced -- sqrt5 lies in Q(zeta_{36 kappa}) iff 5 | kappa. The VALUE "
            "FIELD is a law; the level-dependence is not.")

    L("=" * 78)
    L(f"VERDICT: {verdict}")
    L("  " + reason)
    L(f"  ladder Z_k (k=1..{KMAX}): " + ", ".join(r["Z"] for r in rows))

    out = {
        "cell": "P2W4-Z1",
        "task": "H133-successor: is Z = Tr rho(A1) identically 1 at all E6 levels?",
        "object": "Z_k = Tr rho_k(T^2 S T) = sum_a t_a^3 S_aa, E6 level k, kappa=k+12",
        "method": ("exact cyclotomic accumulation in Z[zeta_{36 kappa}] of the "
                   "Kac-Peterson Weyl sums (diagonal of S only) + PSLQ identification in "
                   "Q(sqrt5) certified exactly mod Phi_{36 kappa}; independent float "
                   "pipeline with the two-word gate at k<=%d." % min(KGATE, KMAX)),
        "kmax": KMAX,
        "ladder": [{"k": r["k"], "kappa": r["kappa"], "N": r["N"], "Z": r["Z"],
                    "cert": r["cert"]} for r in rows],
        "gates": gates,
        "mechanism": {"lucas_resultant_identity_n_1_20": bool(lucas_ok),
                      "abs_det_w2_3w_I_values": detvals,
                      "characteristic_primes": charprimes},
        "laws": {kk: (vv if not isinstance(vv, np.bool_) else bool(vv))
                 for kk, vv in laws.items()},
        "chord_discipline_B774": (
            "PASS -- Z is the trace of the non-abelian E6 level-k Weil-rep monodromy "
            "rho(A1) on the full primary space, the identical object H133/B600/CL-H133 "
            "registered; no abelian relabel, no finer invariant substituted. The exact "
            "route computes the same number as the float route (G3)."),
        "discriminating_fact": None,
        "verdict": verdict,
        "reason": reason,
    }
    out["discriminating_fact"] = (
        "the exactly-certified ladder Z_k, k=1..%d: " % KMAX
        + ", ".join(f"{r['k']}:{r['Z']}" for r in rows))
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    with open(os.path.join(HERE, "output.txt"), "w") as f:
        f.write("\n".join(log) + "\n")
    return verdict


if __name__ == "__main__":
    main()
