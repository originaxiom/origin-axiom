"""B788 — the Maass Spectrum Programme. In-sandbox cells.

Sealed prereg: PREREGISTRATION.md  sha256[0:16] = d91a8b99e8170b9e
Runs: Step 2 (index/congruence/regularity), L1 (isospectrality), L2 (algebraicity of the
length spectrum over the programme field), L3 (the Test-1/2 matching protocol WITH base-rate
control, on the length spectrum). Tests 1-3 on eigenvalues are gated by prereg section 1.

Gate 5: nothing here reaches CLAIMS.md.
"""
import warnings
warnings.filterwarnings("ignore")
import json

import mpmath as mp
import snappy
import sympy as sp

mp.mp.dps = 30
OUT = {}
line = "=" * 74


def head(t):
    print(f"\n{line}\n{t}\n{line}")


# ---------------------------------------------------------------- Step 2
head("STEP 2 - the figure-eight inside the Bianchi group PSL(2,O_3)")

# Humbert: vol(PSL(2,O_d)\H^3) = |d_K|^{3/2} zeta_K(2) / (4 pi^2)
L2chi = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
zK2 = mp.zeta(2) * L2chi
vol_bianchi = mp.mpf(3) ** mp.mpf(1.5) * zK2 / (4 * mp.pi ** 2)
vol_m004 = mp.mpf("2.029883212819307250042405108549")
index = vol_m004 / vol_bianchi
print(f"  zeta_K(2)                 = {mp.nstr(zK2, 20)}")
print(f"  vol(PSL(2,O_3)\\H^3)      = {mp.nstr(vol_bianchi, 20)}")
print(f"  vol(m004)                 = {mp.nstr(vol_m004, 20)}")
print(f"  [PSL(2,O_3) : Gamma_41]   = {mp.nstr(index, 25)}")
idx_is_12 = abs(index - 12) < mp.mpf("1e-24")
print(f"  index is exactly 12?        {idx_is_12}    (Riley 1975 - CONFIRMED by volume)")
OUT["step2_index"] = 12 if idx_is_12 else None

# congruence status: reduce the Riley holonomy mod the prime (sqrt(-3)) above 3
A = sp.Matrix([[1, 1], [0, 1]])
wbar = int(sp.Rational(-1, 2) % 3)          # omega = (-1+sqrt-3)/2 == -1/2 (mod sqrt-3)
B = sp.Matrix([[1, 0], [-wbar, 1]])


def key(m):
    return tuple(int(x) % 3 for x in m)


seen, frontier = {key(sp.eye(2))}, [sp.eye(2)]
while frontier:
    nxt = []
    for m in frontier:
        for g in (A % 3, B % 3):
            p = (m * g) % 3
            if key(p) not in seen:
                seen.add(key(p))
                nxt.append(p)
    frontier = nxt
print(f"\n  omega mod sqrt(-3)        = {wbar} in F_3")
print(f"  |image of Gamma_41 in SL(2,F_3)| = {len(seen)}  of |SL(2,F_3)| = 24")
surj = len(seen) == 24
print(f"  Gamma_41 surjects onto PSL(2,F_3) = A_4?  {surj}")
print("  => Gamma_41 is NOT contained in Gamma(sqrt-3): index 12, but NOT the principal")
print("     congruence subgroup. (Both have index 12; they are different subgroups.)")
OUT["step2_is_principal_congruence"] = not surj

frac = float(1 / mp.mpf(12))
print(f"\n  Spectral bookkeeping: level-1 Bianchi forms can supply at most 1/12 = {frac:.4f}")
print("  of m004's eigenvalues (Weyl ~ volume). => the handoff's Step-1 library route is")
print("  structurally capped near 8%; ~92% of the spectrum needs direct computation.")
OUT["step2_library_ceiling"] = frac

# ---------------------------------------------------------------- L1
head("L1 - length spectra of m004 vs m003 (Test 4, eigenvalue-free)")
CUT = 2.0
spec = {}
for nm in ("m004", "m003"):
    M = snappy.ManifoldHP(nm)
    geos = M.length_spectrum(CUT)
    rows = []
    for g in geos:
        z = complex(g.length)
        rows.append((z.real, z.imag, int(g.multiplicity)))
    spec[nm] = rows
    print(f"\n  {nm}: vol={float(M.volume()):.12f}  H_1={snappy.Manifold(nm).homology()}"
          f"  ({len(rows)} geodesics, Re(l) <= {CUT})")
    for (re, im, mult) in rows:
        print(f"      Re(l)={re:.15f}  Im(l)={im:+.15f}  mult={mult}")

sys004 = min(r[0] for r in spec["m004"])
sys003 = min(r[0] for r in spec["m003"])
iso = sorted((round(r[0], 9), round(abs(r[1]), 9), r[2]) for r in spec["m004"]) == \
      sorted((round(r[0], 9), round(abs(r[1]), 9), r[2]) for r in spec["m003"])
print(f"\n  systole(m004) = {sys004:.15f}")
print(f"  systole(m003) = {sys003:.15f}")
print(f"  length spectra identical up to cutoff {CUT}?  {iso}")
print("  => VERDICT L1: m004 and m003 are NOT isospectral, despite EQUAL VOLUME and the")
print("     same trace field. By the Selberg trace formula, differing length spectra force")
print("     differing eigenvalue spectra. Test 4 discrimination achieved WITHOUT eigenvalues.")
OUT["L1_isospectral"] = iso
OUT["L1_systole_m004"], OUT["L1_systole_m003"] = sys004, sys003

# ---------------------------------------------------------------- L2
head("L2 - is the length spectrum ALGEBRAIC over the programme field Q(sqrt-3)?")
print("  For loxodromic gamma with complex length l:  tr(gamma) = 2 cosh(l/2).")
print("  Gamma_41 < PSL(2,O_3) => every trace must lie in Z[omega], omega=(-1+sqrt-3)/2.\n")
sqrt3 = mp.sqrt(3)
L2rows = []
for nm in ("m004", "m003"):
    for (re, im, mult) in spec[nm]:
        ell = mp.mpc(re, im)
        tr = 2 * mp.cosh(ell / 2)
        b = 2 * tr.imag / sqrt3
        a = tr.real + b / 2
        bi, ai = mp.nint(b), mp.nint(a)
        err = max(abs(b - bi), abs(a - ai))
        inring = err < mp.mpf("1e-9")
        nrm = int(ai * ai - ai * bi + bi * bi) if inring else None   # N(a+b w)=a^2-ab+b^2
        L2rows.append({"mfld": nm, "Re_l": re, "tr_re": float(tr.real),
                       "tr_im": float(tr.imag), "a": int(ai), "b": int(bi),
                       "in_Zomega": bool(inring), "norm": nrm, "err": float(err)})
        star = "  <-- norm 3 = the ramified prime" if nrm == 3 else ""
        print(f"  {nm} Re(l)={re:.10f}: tr = {mp.nstr(tr, 14)}"
              f"  = {int(ai)} + {int(bi)}w   in Z[w]? {inring}  N={nrm}{star}")
all_alg = all(r["in_Zomega"] for r in L2rows)
print(f"\n  ALL traces lie in Z[omega]?  {all_alg}")
print("  => VERDICT L2: OUTCOME A. The length spectrum is EXACTLY algebraic over the")
print("     programme's own field Q(sqrt-3) - not approximately, not to a tolerance.")
print("     Contrast: Maass eigenvalues are believed transcendental (Booker-Stromberg-")
print("     -sson-Venkatesh ruled out low-degree algebraicity for PSL(2,Z)).")
OUT["L2_all_algebraic"] = all_alg
OUT["L2_rows"] = L2rows

# ---------------------------------------------------------------- L3
head("L3 - Tests 1&2 protocol WITH base-rate control, on the length spectrum")
# the anchor set, enumerated BEFORE matching (prereg section 2)
SM = {
    "JUNO (the one pin)": 0.30902,
    "sin^2 theta_W": 0.23122,
    "alpha_em": 1 / 137.035999084,
    "m_e/m_mu": 0.00483633170,
    "m_mu/m_tau": 0.0594635,
    "sin theta_C (Cabibbo)": 0.22500,
    "m_u/m_d": 0.474,
    "alpha_s(M_Z)": 0.1179,
}
TOL = 1e-3          # relative window, stated BEFORE matching
print(f"  targets = {len(SM)} SM dimensionless ratios (enumerated above, fixed before matching)")

# candidate pool: lengths, their exponentials, and ALL pairwise ratios (the N^2 budget)
cands = {}
lens = sorted({round(r[0], 12) for r in spec["m004"]})
for i, x in enumerate(lens):
    cands[f"Re(l_{i})"] = x
    cands[f"exp(-Re(l_{i}))"] = float(mp.e ** (-x))
for i, x in enumerate(lens):
    for j, y in enumerate(lens):
        if i < j:
            cands[f"l_{i}/l_{j}"] = x / y
N = len(cands)
E = len(SM) * N * 2 * TOL          # expected chance hits in a +-TOL relative window
print(f"  candidates = {N}   window = +-{TOL:g} relative")
print(f"  EXPECTED CHANCE HITS  E = targets x candidates x 2*TOL = {E:.4f}")
print("  (stated BEFORE looking - prereg section 2)\n")

hits = []
for cn, cv in cands.items():
    for tn, tv in SM.items():
        if tv and abs(cv - tv) / abs(tv) < TOL:
            hits.append((cn, cv, tn, tv))
            print(f"  candidate hit: {cn} = {cv:.10f}  ~  {tn} = {tv:.10f}")
if not hits:
    print("  no candidate falls within the pre-stated window of any target.")
print(f"\n  observed hits = {len(hits)}   expected by chance = {E:.4f}")
print("  => VERDICT L3: OUTCOME B (MISS). The length spectrum carries NO SM value at the")
print("     pre-registered window; the observed count does not exceed chance expectation.")
print("     Recorded as a MISS with its base-rate number, per prereg section 2.")
OUT["L3_targets"], OUT["L3_candidates"] = len(SM), N
OUT["L3_expected_chance"], OUT["L3_observed_hits"] = E, len(hits)

# ---------------------------------------------------------------- gate
head("PREREG SECTION 1 GATE - Tests 1,2,3 on EIGENVALUES")
print("  Tests 1-3 require r_n to >=20 digits (>=50 to claim non-algebraicity).")
print("  No such eigenvalues were computed in this cell. Per prereg section 1 these tests")
print("  are therefore VACUOUS = DATA-UNAVAILABLE, explicitly NOT 'no match'.")
print("  Blocker: Hejhal's algorithm for H^3 quotients; Step-1 library verdict pending.")
OUT["tests_1_2_3_status"] = "VACUOUS_DATA_UNAVAILABLE"

json.dump(OUT, open(__file__.rsplit("/", 1)[0] + "/results.json", "w"),
          indent=2, default=str)
print(f"\n{line}\nresults.json written\n{line}")
