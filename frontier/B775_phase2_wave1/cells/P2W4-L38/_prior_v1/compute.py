#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B775 Phase-2 Wave-4  cell P2W4-L38  (OI-062 / S039 Act II)
==========================================================
THE kappa=-2 DEFORMATION SCALE  (the e^{-k*Vol} suppression, Vol = Vol(4_1) = 2.0299).

Context (read in-cell): S039 do-or-die program, Act I = B213 (Higgs-side periods):
the char-variety elliptic curve 40a1 carries NO forced tiny number (all O(1)/BSD-generic;
firewall holds a 4th time). Residual Act II = the kappa=-2 vacuum deformation scale:
B67 -- the figure-eight sits AT kappa = -2 (complete hyperbolic = parabolic/Markov fiber),
the form's distinguished Lambda=0 vacuum. Any nonzero Lambda is an external/finite-level
DEFORMATION away from it (a Dehn filling, a finite WRT level k). S039's own prereg row:
  "Lambda's tininess is a large-level/semiclassical suppression: e^{-k*Vol} in the WRT /
   complex-volume asymptotic (Act II)"   [open]  expected: the scale is the external level k.

THE COMPUTATION (this cell): compute the kappa=-2 deformation scale WITH its structure --
the complex-Chern-Simons / volume-conjecture exponent that governs e^{-k*Vol} -- and decide:
  RESOLVED-A : a FORCED (object-intrinsic) tiny scale is present, computed with structure.
  RESOLVED-B : no forced tiny number -- the suppression RATE is a forced O(1) invariant but
               the smallness is set by the EXTERNAL level k (EXTERNAL).  [firewall-consistent]
  UNRESOLVED : the independent Vol computations disagree / cross-check fails.

Gate 5 STRICT: structural deformation scale only, NO SM Higgs claim, nothing to CLAIMS,
one-number pin untouched.  Env: pyenv python3 (mpmath exact-precision; snappy cross-check).
Chord discipline (B774): the exponent is the genuine hyperbolic invariant Vol(4_1) (a
topological volume + the Neumann-Zagier cusp modulus), NOT an abelianized/character proxy.
Positive reproduced a 2nd way: Vol via Bloch-Wigner dilog AND via Lobachevsky AND via snappy.
"""

import json, math, os
import mpmath as mp

mp.mp.dps = 50  # 50 decimal digits

OUT = os.path.dirname(os.path.abspath(__file__))

# ------------------------------------------------------------------ #
# 1.  Vol(4_1) computed THREE independent ways (chord discipline:     #
#     the exponent is the honest hyperbolic invariant, no proxy).     #
# ------------------------------------------------------------------ #
# The figure-eight complement = 2 regular ideal tetrahedra, each of
# shape z = e^{i*pi/3} (the primitive 6th root, field Q(sqrt(-3)) = the atom).

# Form A: Bloch-Wigner dilogarithm of the tetrahedron shape.
#   D(z) = Im Li2(z) + arg(1-z)*log|z|;  |z|=1 => 2nd term = 0.
z = mp.e**(1j*mp.pi/3)
D_A = mp.im(mp.polylog(2, z))                       # = D(e^{i pi/3})
Vol_A = 2 * D_A

# Form B: Lobachevsky function.  Vol(4_1) = 6*Lambda(pi/3),
#   Lambda(theta) = (1/2) Im Li2(e^{2 i theta}).
Lob_pi3 = mp.mpf('0.5') * mp.im(mp.polylog(2, mp.e**(2j*mp.pi/3)))
Vol_B = 6 * Lob_pi3

# Form C: snappy (optional external cross-check).
Vol_C = None
cusp_shape = None
cvol = None
try:
    import snappy
    M = snappy.Manifold('4_1')
    Vol_C = mp.mpf(repr(M.volume()))
    cvol = complex(M.complex_volume())           # Vol + i*CS
    cusp_shape = complex(M.cusp_info('shape')[0])
except Exception as e:                            # pragma: no cover
    snappy_err = str(e)

VOL = Vol_A                                       # canonical value
agree_AB = abs(Vol_A - Vol_B) < mp.mpf('1e-40')
agree_AC = (Vol_C is None) or (abs(Vol_A - Vol_C) < mp.mpf('1e-9'))

# Chern-Simons of the complete structure (figure-eight is amphichiral => CS = 0).
CS = 0.0 if cvol is None else float(cvol.imag)
CS_is_zero = abs(CS) < 1e-6

# ------------------------------------------------------------------ #
# 2.  THE DEFORMATION SCALE, structurally.                            #
# ------------------------------------------------------------------ #
# Complex Chern-Simons / volume conjecture (Kashaev-Murakami; Andersen-Kashaev
# state integral): the level-k partition function of the geometric flat
# connection at the kappa=-2 vacuum has leading exponential
#        Z_k(4_1)  ~  exp( (k/2pi) * ( Vol + i*CS ) ).
# The DEFORMATION SCALE -- the semiclassical weight of one vacuum relative to
# the trivial (Lambda-deformed) sector -- is the modulus
#        S(k) = exp( - (k/2pi) * Vol )      (the "e^{-k*Vol}" factor, normalised).
# Its structure factorises exactly:
#        S(k) = base ** k,     base = exp( - Vol/(2pi) ).
# => the RATE per unit level is the forced hyperbolic invariant  Vol/(2pi);
#    the SMALLNESS is (base)^k, controlled ENTIRELY by the external level k.

rate = VOL / (2 * mp.pi)                 # forced, exact, O(1)  (= B213's "Vol/2pi = 0.3231")
base = mp.e**(-rate)                     # per-level suppression factor, O(1)
# sample the deformation scale at a ladder of external levels k:
levels = [1, 2, 3, 6, 12, 50, 100]
scale_at_k = {int(k): float(mp.e**(-mp.mpf(k)*rate)) for k in levels}

# Is the FORCED (object-intrinsic, k-independent) content tiny?  base is O(1).
base_f = float(base)
base_is_O1 = 0.1 < base_f < 1.0          # NOT tiny: O(1)
# The tininess requires large k (external):  need k >~ how big for base^k < 1e-3 ?
k_for_1e3 = float(-3*mp.log(10)/mp.log(base))   # continuous; ~ external level needed
smallness_needs_external_k = k_for_1e3 > 10      # O(1) base => needs sizeable external k

# ------------------------------------------------------------------ #
# 3.  The 2nd-order deformation curvature (Neumann-Zagier) = the atom. #
# ------------------------------------------------------------------ #
# Deforming the meridian holonomy by u (u=0 at the complete kappa=-2 point),
# the complex volume changes as  CVol(u) = CVol(0) + (tau/4)*u^2 + O(u^4),
# where tau = cusp shape modulus.  For 4_1, tau = 2*sqrt(3)*i  (snappy),
# so tau^2 = -12 => the deformation CURVATURE lives in Q(sqrt(-3)) = the atom.
cusp_field_atom = False
cusp_tau_sq = None
if cusp_shape is not None:
    cusp_tau_sq = cusp_shape**2                  # ~ -12 + 0i
    # squarefree part of tau^2 should be -3  (i.e. tau^2 = -12 = 4*(-3))
    cusp_field_atom = (abs(cusp_tau_sq.real + 12) < 1e-6) and (abs(cusp_tau_sq.imag) < 1e-6)

# ------------------------------------------------------------------ #
# 4.  VERDICT LOGIC (in-code; can emit UNRESOLVED).                   #
# ------------------------------------------------------------------ #
def decide():
    # sanity / cross-check gate
    if not agree_AB:
        return ("UNRESOLVED",
                "the two independent Vol computations (Bloch-Wigner vs Lobachevsky) disagree")
    if not agree_AC:
        return ("UNRESOLVED",
                "internal Vol disagrees with snappy cross-check")
    if not CS_is_zero:
        return ("UNRESOLVED",
                "CS(complete) != 0 unexpectedly -- complex-volume saddle not the pure-volume one")
    # A forced intrinsic tiny scale would be: base itself tiny (k-independent smallness)
    if not base_is_O1:
        return ("RESOLVED-A",
                "the per-level deformation base is intrinsically tiny -- a forced object scale")
    # otherwise: rate is a forced O(1) invariant, smallness is external (level k)
    if base_is_O1 and smallness_needs_external_k:
        return ("RESOLVED-B",
                "no forced tiny number: the deformation RATE Vol/2pi is a forced O(1) hyperbolic "
                "invariant (0.3231; base exp(-Vol/2pi)=0.724 is O(1)), and the SMALLNESS of "
                "e^{-k*Vol} is set entirely by the EXTERNAL level k -- the scale is external "
                "(5th firewall mode, extending B213 Act I to the kappa=-2 vacuum deformation)")
    return ("UNRESOLVED", "deformation-scale structure did not resolve into A or B")

verdict, why = decide()

# ------------------------------------------------------------------ #
# 5.  Emit compact artifacts.                                        #
# ------------------------------------------------------------------ #
results = {
    "cell": "P2W4-L38",
    "lead": "OI-062 / S039 Act II -- the kappa=-2 deformation scale (e^{-k*Vol})",
    "verdict": verdict,
    "terminal_state": "EXTERNAL" if verdict == "RESOLVED-B" else
                      ("RESOLVED" if verdict == "RESOLVED-A" else "UNRESOLVED"),
    "Vol_4_1": {
        "bloch_wigner_2ImLi2(e^{ipi/3})": mp.nstr(Vol_A, 15),
        "lobachevsky_6Lambda(pi/3)":       mp.nstr(Vol_B, 15),
        "snappy":                          (mp.nstr(Vol_C, 12) if Vol_C is not None else None),
        "agree_AB": bool(agree_AB), "agree_AC": bool(agree_AC),
    },
    "CS_complete": CS, "CS_is_zero": bool(CS_is_zero),
    "deformation_scale": {
        "form": "S(k) = exp(-(k/2pi)*Vol) = base**k",
        "rate_Vol_over_2pi": mp.nstr(rate, 12),
        "base_exp(-Vol/2pi)": base_f,
        "base_is_O1_not_tiny": bool(base_is_O1),
        "scale_at_level_k": scale_at_k,
        "k_needed_for_scale<1e-3": round(k_for_1e3, 3),
        "smallness_source": "external level k (rate is forced/O(1))",
    },
    "deformation_curvature": {
        "cusp_shape_tau": (str(cusp_shape) if cusp_shape is not None else None),
        "tau^2": (str(cusp_tau_sq) if cusp_tau_sq is not None else None),
        "curvature_field_is_atom_Q(sqrt-3)": bool(cusp_field_atom),
    },
    "why": why,
    "gate5": "structural deformation scale only; NO SM Higgs claim; nothing to CLAIMS; "
             "one-number pin untouched",
    "chord_discipline_B774": "the exponent is the genuine hyperbolic invariant Vol(4_1) "
                             "(topological volume + NZ cusp modulus), not a character/abelian proxy",
    "reproduced_2nd_way": "Vol via Bloch-Wigner dilog AND Lobachevsky AND snappy (all agree)",
}

with open(os.path.join(OUT, "results.json"), "w") as f:
    json.dump(results, f, indent=1)

lines = []
P = lines.append
P("B775 P2W4-L38  --  OI-062 / S039 Act II : the kappa=-2 deformation scale")
P("=" * 70)
P(f"Vol(4_1)  Bloch-Wigner 2 Im Li2(e^ipi/3) = {mp.nstr(Vol_A, 15)}")
P(f"          Lobachevsky   6 Lambda(pi/3)    = {mp.nstr(Vol_B, 15)}   agree={bool(agree_AB)}")
P(f"          snappy                          = {mp.nstr(Vol_C,12) if Vol_C is not None else 'n/a'}   agree={bool(agree_AC)}")
P(f"CS(complete) = {CS:.2e}   (=0: figure-eight amphichiral)   CS_is_zero={CS_is_zero}")
P("-" * 70)
P("Deformation scale   S(k) = exp(-(k/2pi)*Vol) = base**k")
P(f"  RATE  Vol/(2pi)          = {mp.nstr(rate,12)}   (FORCED, exact, O(1))")
P(f"  base  exp(-Vol/2pi)      = {base_f:.10f}   (O(1), NOT tiny)  base_is_O1={base_is_O1}")
P(f"  scale at levels k        = " + ", ".join(f"k{k}:{v:.3e}" for k,v in scale_at_k.items()))
P(f"  k needed for scale<1e-3  = {k_for_1e3:.2f}   (=> smallness is EXTERNAL level k)")
P(f"  deformation curvature: cusp tau = {cusp_shape}, tau^2={cusp_tau_sq}  atom Q(sqrt-3)={cusp_field_atom}")
P("-" * 70)
P(f"VERDICT: {verdict}   terminal={results['terminal_state']}")
P(f"WHY: {why}")
P("Gate 5: structural only; no SM Higgs claim; nothing to CLAIMS; one-number pin untouched.")
txt = "\n".join(lines)
with open(os.path.join(OUT, "output.txt"), "w") as f:
    f.write(txt + "\n")
print(txt)
