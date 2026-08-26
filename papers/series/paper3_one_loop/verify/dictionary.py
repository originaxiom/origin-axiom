#!/usr/bin/env python3
"""B8112 -- THE DICTIONARY ENTRY: the AdS3 boundary-graviton one-loop IS Pfaff's Ruelle product.

B8104 closed with ONE named gap: "does the AdS3 boundary-graviton one-loop determinant correspond
to one of Pfaff's rho(m) torsions, and if so which?"  This answers it, and the answer is an
IDENTITY rather than a conjecture -- but it is NOT "one of the rho(m)", which is why the question
as posed had no answer.

THE DEFINITIONS, read from the source (arXiv:1206.0228, Pfaff), not recalled:
  rho(m)  := the 2m-th symmetric power of the standard rep of SL_2(C), on Sym^{2m} C^2, dim 2m+1
  sigma_k := the rep of M = SO_2(R) with highest weight k e_2 -- ONE-DIMENSIONAL
  R(s,sigma) := prod_{[gamma] prime} det(Id - sigma(m_gamma) e^{-s l(gamma)}),  abs. conv. Re(s) > 2

Since sigma_k is ONE-dimensional, sigma_k(m_gamma) = e^{i k theta_gamma}, so

  R(k, sigma_k) = prod_{[gamma] prime} (1 - e^{i k theta} e^{-k l})
                = prod_{[gamma] prime} (1 - q_gamma^k),      q_gamma = e^{-l + i theta}

and q_gamma is EXACTLY the Giombi-Maloney-Yin nome.  Therefore the graviton product

  Z_geod = prod_gamma prod_{n>=2} |1 - q_gamma^n|^{-2}  =  prod_{n>=2} |R(n, sigma_n)|^{-2}.

QUANTIFIER: the complex length spectrum of m004 and Pfaff's Theorem 1.2.  No measured value;
this is a mathematical identification, not a physical prediction.  Gate 5 untouched.
"""
import cmath, json, math, os
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
FAILED = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAILED.append(l)

M = snappy.Manifold("m004")
VOL = 2.029883212819307
KAPPA = 1

def spectrum(cut):
    """Primitive complex length spectrum with multiplicity, as B8100 used it."""
    return [(complex(g.length), g.multiplicity) for g in M.length_spectrum(cut)]

print("=" * 78); print("SECTION 1 -- CONTROLS ON THE SPECTRUM"); print("=" * 78)
sp = spectrum(5.5)
sys_ = min(L.real for L, _ in sp)
gate("systole reproduces the known value", abs(sys_ - 1.087070144995739) < 1e-12, f"{sys_:.15f}")
# Conjugacy must be read MOD 2*pi: a geodesic with theta = pi is its OWN conjugate, since
# e^{i pi} = e^{-i pi}.  B8100 ran this control on M.length_spectrum(2.0) while its HEADLINE
# used cutoff 5.5 -- and no theta = pi class appears below 2.0, so the control passed only in
# the regime where it was vacuous.  Four such classes exist below 5.5.  Control tests the
# neighbour: recorded, and fixed here.
def _has_conj(L, sp):
    for L2, _ in sp:
        # distance to the NEAREST multiple of 2*pi -- a plain % returns ~2*pi for a sum a hair
        # BELOW 2*pi, which silently failed the theta = pi classes.
        w = (L.imag + L2.imag) % (2 * math.pi)
        if abs(L.real - L2.real) < 1e-8 and min(w, 2 * math.pi - w) < 1e-8:
            return True
    return False
selfconj = [L for L, _ in sp if abs(abs(L.imag) - math.pi) < 1e-8]
gate("geodesics come in complex-conjugate pairs MOD 2*pi (real manifold)",
     all(_has_conj(L, sp) for L, _ in sp),
     f"{len(selfconj)} self-conjugate (theta = pi) classes below 5.5")
print(f"  classes below 5.5: {len(sp)}   geodesics with multiplicity: {sum(m for _, m in sp)}")

# ------------------------------------------------------------------ the Ruelle zeta, per n
def R(n, sp):
    """R(n, sigma_n) = prod_{[gamma] prime} (1 - q^n), q = e^{-l+i theta}.  Multiplicity is the
    number of DISTINCT prime classes of that complex length, so it is an EXPONENT on the factor."""
    tot = 1.0 + 0j
    for L, mult in sp:
        q = cmath.exp(-L.real + 1j * L.imag)
        tot *= (1 - q ** n) ** mult
    return tot

print(); print("=" * 78); print("SECTION 2 -- THE IDENTITY, CHECKED AGAINST B8100'S OWN NUMBER"); print("=" * 78)
def logZ_via_R(sp, nmax=400):
    return -2.0 * sum(math.log(abs(R(n, sp))) for n in range(2, nmax))

def logZ_via_gamma(sp, nmax=400):
    """B8100's ordering: gamma outside, n inside."""
    tot = 0.0
    for L, mult in sp:
        q = cmath.exp(-L.real + 1j * L.imag)
        s = 0.0
        for n in range(2, nmax):
            s += -2.0 * math.log(abs(1 - q ** n))
        tot += mult * s
    return tot

a, b = logZ_via_R(sp), logZ_via_gamma(sp)
print(f"  prod over n of |R(n,sigma_n)|^-2 : {a:.15f}")
print(f"  B8100's gamma-first ordering     : {b:.15f}")
gate("THE IDENTITY: the two orderings agree to machine precision", abs(a - b) < 1e-12,
     f"|diff| = {abs(a-b):.3e}")
gate("and it reproduces B8100's banked estimate at cutoff 5.5",
     abs(b - (-0.2729771708384004)) < 1e-9, f"{b:.15f}")

# ---------------------------------------------- WHERE the cutoff uncertainty actually lives
print(); print("=" * 78); print("SECTION 3 -- THE n=2 FACTOR SITS AT THE ABSCISSA OF CONVERGENCE"); print("=" * 78)
print("  Pfaff: R(s,sigma) converges absolutely for Re(s) > 2.  The graviton product starts at")
print("  n = 2 -- the BOUNDARY.  Prediction: all the cutoff wobble lives in the n=2 factor.")
print()
cuts = [3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
rows = []
for c in cuts:
    s = spectrum(c)
    t2 = -2.0 * math.log(abs(R(2, s)))
    t3p = -2.0 * sum(math.log(abs(R(n, s))) for n in range(3, 400))
    rows.append((c, t2, t3p, t2 + t3p))
    print(f"  cutoff {c:4}:  n=2 term {t2:+.9f}   n>=3 tail {t3p:+.9f}   total {t2+t3p:+.9f}")
d2 = [abs(rows[i+1][1] - rows[i][1]) for i in range(len(rows)-1)]
d3 = [abs(rows[i+1][2] - rows[i][2]) for i in range(len(rows)-1)]
print(f"\n  last cutoff-step change:  n=2 term {d2[-1]:.3e}   n>=3 tail {d3[-1]:.3e}")
gate("the n>=3 tail is far more stable under cutoff than the n=2 term",
     d3[-1] < d2[-1] / 10, f"ratio {d2[-1]/max(d3[-1],1e-30):.1f}x")
sgn2 = {(rows[i+1][1] - rows[i][1]) > 0 for i in range(len(rows)-1)}
sgn3 = {(rows[i+1][2] - rows[i][2]) > 0 for i in range(len(rows)-1)}
print(f"  n=2 term changes sign across cutoffs: {len(sgn2) > 1}   n>=3 tail: {len(sgn3) > 1}")
gate("the OSCILLATION B8100 reported is carried by the n=2 term", len(sgn2) > 1)

# ------------------------------------------------------------------ Pfaff's c(m), recomputed
print(); print("=" * 78); print("SECTION 4 -- c(m), RECOMPUTED (B8104 banked values with NO script)"); print("=" * 78)
def c(m):
    """c(m) as printed in the source.  PARENTHESISATION DECLARED, because the transcription is
    ambiguous: the '+m' and '+m+1' are read as INSIDE each factor of the products."""
    A = 1.0
    for j in range(1, m):
        A *= math.sqrt((m + 1) ** 2 + m ** 2 - j ** 2) + m
    B = 1.0
    for j in range(1, m + 1):
        B *= math.sqrt((m + 1) ** 2 + m ** 2 - j ** 2) + m + 1
    r = math.sqrt((m + 1) ** 2 + m ** 2)
    return (A / B) * math.sqrt((r + m) / (r + m + 1))

B8104 = {3: 0.7121142418, 4: 0.5531518273, 5: 0.4522787995}
agree = True
for m in (3, 4, 5):
    mine = c(m) / c(2)
    ok = abs(mine - B8104[m]) < 1e-8
    agree &= ok
    print(f"  m={m}:  c(m)/c(2) = {mine:.10f}   B8104 banked {B8104[m]:.10f}   {'MATCH' if ok else 'DIFFERS'}")
gate("recomputation reproduces B8104's unscripted c(m)/c(2) values", agree,
     "" if agree else "B8104's numbers are NOT reproducible from the declared parenthesisation")

# ------------------------------------------------------- the torsion ratio for our object
print(); print("=" * 78); print("SECTION 5 -- T_X(rho(m))/T_X(rho(2)) FOR THE FIGURE-EIGHT COMPLEMENT"); print("=" * 78)
print("  Thm 1.2:  T(rho(m))/T(rho(2)) = (c(m)/c(2))^kappa * exp(-(1/pi) vol (m(m+1)-6))")
print("                                  * prod_{k=3}^{m} |R(k,sigma_k)|      [kappa = 1]")
print()
TOR = {}
for m in (3, 4, 5, 6):
    cf = (c(m) / c(2)) ** KAPPA
    vf = math.exp(-(1 / math.pi) * VOL * (m * (m + 1) - 6))
    rp = 1.0
    for k in range(3, m + 1):
        rp *= abs(R(k, sp))
    TOR[m] = cf * vf * rp
    print(f"  m={m}:  cusp {cf:.10f}   vol {vf:.6e}   ruelle {rp:.12f}   ->  T ratio {TOR[m]:.6e}")
gate("every Ruelle factor k>=3 is finite and non-zero", all(abs(R(k, sp)) > 0 for k in range(3, 7)))
gate("the torsion ratio decreases in m (the volume term dominates)",
     all(TOR[m] > TOR[m+1] for m in (3, 4, 5)))
# stability of the k>=3 Ruelle product under cutoff -- the number that makes this quotable
rp_by_cut = []
for cc in cuts:
    s = spectrum(cc)
    rp_by_cut.append(abs(R(3, s)) * abs(R(4, s)) * abs(R(5, s)) * abs(R(6, s)))
print(f"\n  prod_{{k=3}}^{{6}} |R| by cutoff: " + "  ".join(f"{v:.10f}" for v in rp_by_cut))
stab = abs(rp_by_cut[-1] - rp_by_cut[-2])
rel = stab / rp_by_cut[-1]
print(f"  last cutoff delta {stab:.3e}  ->  RELATIVE uncertainty on the torsion ratio {rel:.1e}")
# The honest gate is the COMPARATIVE claim, not a threshold picked to be passed: the k>=3 product
# must be at least two orders more cutoff-stable than the n=2 term, which is the actual finding.
gate("the k>=3 Ruelle product is >=100x more cutoff-stable than the n=2 term",
     stab * 100 < d2[-1], f"{d2[-1]/stab:.0f}x")

print(); print("=" * 78); print("THE ANSWER TO B8104'S QUESTION"); print("=" * 78)
print("""
  It is NOT one of the rho(m).  The graviton one-loop is  prod_{n>=2} |R(n,sigma_n)|^{-2}  --
  an INFINITE product of one-dimensional Ruelle zetas.  Each rho(m) torsion is a FINITE object.
  What Pfaff's Theorem 1.2 supplies is the TAIL:  prod_{k=3}^{m} |R(k,sigma_k)| expressed as a
  torsion ratio times an explicit cusp defect and an explicit volume factor.  So

      Z_geod  =  |R(2,sigma_2)|^{-2}  *  lim_{m->infinity} [ (c(m)/c(2))^kappa
                 * exp(-(1/pi) vol (m(m+1)-6)) * T_X(rho(m))/T_X(rho(2)) ]^{-2}

  and the ONE factor Pfaff's ratio does not reach -- n = 2 -- is precisely the one sitting AT
  the abscissa of absolute convergence, which is why the theorem starts at m >= 3 and normalises
  by rho(2), and why B8100's convergence was oscillatory rather than monotone.
""")

RES = {"identity": "R(k,sigma_k) = prod_{[gamma] prime} (1 - q_gamma^k), q = e^{-l+i theta} = GMY nome",
       "graviton_one_loop_is": "prod_{n>=2} |R(n,sigma_n)|^{-2}",
       "is_a_single_rho_m": False,
       "logZ_via_R": a, "logZ_via_gamma": b, "orderings_agree": abs(a - b) < 1e-12,
       "b8100_reproduced": abs(b - (-0.2729771708384004)) < 1e-9,
       "n2_term_by_cutoff": [r[1] for r in rows],
       "n3plus_tail_by_cutoff": [r[2] for r in rows],
       "cutoffs": cuts,
       "n2_last_delta": d2[-1], "n3plus_last_delta": d3[-1],
       "n2_oscillates": len(sgn2) > 1, "n3plus_oscillates": len(sgn3) > 1,
       "c_ratio_recomputed": {str(m): c(m) / c(2) for m in (3, 4, 5)},
       "c_ratio_b8104": {str(m): B8104[m] for m in (3, 4, 5)},
       "c_ratio_agrees": agree,
       "torsion_ratio": {str(m): TOR[m] for m in TOR},
       "ruelle_k3to6_by_cutoff": rp_by_cut,
       "torsion_ratio_relative_uncertainty": rel,
       "self_conjugate_theta_pi_classes": len(selfconj),
       "b8100_conjugate_control_ran_at_cutoff": 2.0,
       "b8100_headline_used_cutoff": 5.5,
       "kappa": KAPPA, "volume": VOL,
       "verdict": ("THE DICTIONARY ENTRY IS AN IDENTITY, AND THE ANSWER TO B8104'S QUESTION IS "
                   "'NONE OF THEM'. sigma_k is ONE-DIMENSIONAL, so R(k,sigma_k) = prod_gamma "
                   "(1 - q^k) with q EXACTLY the GMY nome, and the graviton one-loop is "
                   "prod_{n>=2}|R(n,sigma_n)|^{-2} -- an infinite product, not a single finite "
                   "torsion. Pfaff's Thm 1.2 supplies the k>=3 TAIL as a torsion ratio. The one "
                   "factor it does not reach, n=2, sits AT the abscissa of absolute convergence "
                   "Re(s)>2, which is why the theorem starts at m>=3 and normalises by rho(2) -- "
                   "and why B8100's convergence was oscillatory."),
       "scope": ("The complex length spectrum of m004 and Pfaff arXiv:1206.0228 Thm 1.2. "
                 "Establishes an IDENTIFICATION and computes a torsion ratio; does NOT assemble "
                 "the one-loop partition function -- the cusp's continuous spectrum (B739/B8101) "
                 "is still not included, and Pfaff's torsion is Ray-Singer analytic torsion, "
                 "which is identified with the graviton determinant only through the Ruelle "
                 "factors made explicit here. No measured value. Gate 5 untouched.")}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(RES, fh, indent=1, sort_keys=True, default=str)
print("  results.json written")
if FAILED: raise SystemExit(f"\nCONTROLS FAILED: {FAILED}")
print("\n  ALL CHECKS PASS")
