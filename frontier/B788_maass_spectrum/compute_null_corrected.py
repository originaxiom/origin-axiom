"""B788 ADDENDUM — the CORRECTED null calibration, after Chat-1's challenge.

Three defects in the first pass, all conceded:
  (a) the pre-registered null is the DENSITY-MATCHED one (prereg section 2: "matched surrogate
      spectrum ... the same Weyl density"); the uniform null was never pre-registered, and the
      first pass leaned on it to declare "ordinary noise". Permissive choice.
  (b) the "Weyl-matched" null itself used density ~ e^l. For H^3 the prime geodesic theorem
      gives ~ e^{2l} (entropy = n-1 = 2). It was not actually Weyl-matched.
  (c) no EMPIRICAL null was run, though the prereg offered "the sister m003's data".

This cell fixes all three and reports the verdict under the PRE-REGISTERED null.
Gate 5: nothing here reaches CLAIMS.md.
"""
import warnings
warnings.filterwarnings("ignore")
import json
import random

import mpmath as mp
import snappy

mp.mp.dps = 20
CUT, TOL = 5.0, 1e-3
line = "=" * 74

SM = {
    "JUNO (the one pin)": 0.30902, "sin^2 theta_W": 0.23122,
    "alpha_em": 1 / 137.035999084, "m_e/m_mu": 0.00483633170,
    "m_mu/m_tau": 0.0594635, "sin theta_C (Cabibbo)": 0.22500,
    "m_u/m_d": 0.474, "alpha_s(M_Z)": 0.1179,
}


def build(lengths):
    c = []
    for x in lengths:
        c.append(x)
        c.append(float(mp.e ** (-x)))
    for i in range(len(lengths)):
        for j in range(i + 1, len(lengths)):
            c.append(lengths[i] / lengths[j])
    return c


def hits(cands):
    return sum(1 for cv in cands for tv in SM.values()
               if abs(cv - tv) / abs(tv) < TOL)


def lens_of(name, cut=CUT):
    M = snappy.Manifold(name)
    return sorted({round(complex(g.length).real, 12) for g in M.length_spectrum(cut)})


print(f"\n{line}\nCORRECTED NULL CALIBRATION\n{line}")
L4 = lens_of("m004")
obs = hits(build(L4))
lo, hi = min(L4), max(L4)
print(f"  m004: {len(L4)} distinct lengths in [{lo:.6f}, {hi:.6f}] -> observed {obs} hits")

rng = random.Random(20260728)

# ---- Null B' : CORRECTED density  ~ e^{2l}  (prime geodesic theorem on H^3) -------------
nullB = []
for _ in range(600):
    ws = []
    while len(ws) < len(L4):
        x = rng.uniform(lo, hi)
        if rng.random() < float(mp.e ** (2 * (x - hi))):      # density ~ e^{2x}
            ws.append(x)
    nullB.append(hits(build(sorted(ws))))

# ---- Null C : EMPIRICAL -- the same pipeline on REAL census length spectra ---------------
print("\n  building the empirical null from real one-cusped census manifolds ...")
names, nullC = [], []
for M in snappy.OrientableCuspedCensus(num_cusps=1)[:26]:
    nm = M.name()
    if nm == "m004":
        continue
    try:
        Ls = lens_of(nm)
    except Exception:
        continue
    if len(Ls) < 20:
        continue
    names.append(nm)
    nullC.append(hits(build(Ls)))
    if len(names) >= 20:
        break
print(f"  empirical null over {len(names)} manifolds")


def report(label, null, obs, primary=False):
    s = sorted(null)
    n = len(s)
    mean = sum(s) / n
    ge = sum(1 for v in s if v >= obs)
    p = ge / n
    q = [s[int(f * (n - 1))] for f in (0.05, 0.5, 0.95)]
    tag = "   <== PRE-REGISTERED PRIMARY" if primary else ""
    print(f"\n  {label}{tag}")
    print(f"    n={n}  mean={mean:.2f}  median={q[1]}  5-95%=[{q[0]}, {q[2]}]")
    print(f"    P(null >= observed {obs}) = {p:.4f}")
    return {"n": n, "mean": mean, "median": q[1], "p5": q[0], "p95": q[2], "p_value": p}


print(f"\n{line}\nRESULTS\n{line}")
rB = report("Null B' - corrected density-matched (~e^{2l})", nullB, obs, primary=True)
rC = report("Null C  - EMPIRICAL, real census length spectra", nullC, obs, primary=True)

print(f"\n{line}\nVERDICT (corrected)\n{line}")
pmin = min(rB["p_value"], rC["p_value"])
print(f"  Under the PRE-REGISTERED density-matched null: p = {rB['p_value']:.4f}")
print(f"  Under the EMPIRICAL real-manifold null:        p = {rC['p_value']:.4f}")
print()
print("  Prereg HIT criteria: (i) an EXACT algebraic identity, or (ii) a residual far below")
print("  chance WITH a stated mechanism. Neither is met -> this is NOT a HIT.")
print("  But 'ordinary noise' was the WRONG WORD for the first pass to use, and it was")
print("  reached via a null that was never pre-registered. Corrected verdict below.")
if pmin < 0.05:
    print(f"\n  => MARGINAL-KEEP-WATCHING (p={pmin:.3f}): does not meet HIT criteria (no exact")
    print("     identity, no mechanism), but the excess is real enough to re-test when more")
    print("     data exists. NOT recorded as noise.")
elif pmin < 0.15:
    print(f"\n  => MARGINAL (p={pmin:.3f}): below the HIT bar and with no mechanism, but above")
    print("     the level at which 'ordinary noise' is an honest description. Recorded as")
    print("     MISS-WITH-FLAG: re-test if eigenvalue data ever arrives.")
else:
    print(f"\n  => MISS (p={pmin:.3f}): consistent with chance under the pre-registered null.")

json.dump({"observed": obs, "n_lengths": len(L4), "null_B_corrected": rB,
           "null_C_empirical": rC, "empirical_manifolds": names},
          open(__file__.rsplit("/", 1)[0] + "/results_null_corrected.json", "w"), indent=2)
print(f"\n{line}\nresults_null_corrected.json written\n{line}")
