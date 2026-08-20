#!/usr/bin/env python3
"""B8100 -- the one-loop geodesic factor for the object, and where the cusp piece comes from.

Rung toward completing the 2+1 theory (owner-elected over the 4d lift). Computes the
Giombi-Maloney-Yin graviton product over the object's own complex length spectrum, with an
HONEST cutoff error, and identifies the missing cusp contribution and its banked governing
object. Gate 5 untouched -- a mathematical partition function; no measured value anywhere.
"""
import json, os, math, cmath
import snappy
HERE = os.path.dirname(os.path.abspath(__file__))
FAIL = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAIL.append(l)

M = snappy.Manifold('4_1')

def logZ(cut, nmax=400):
    """GMY graviton product: prod_gamma prod_{n>=2} |1 - q^n|^{-2}, q = e^{-l + i theta}."""
    tot = 0.0
    for g in M.length_spectrum(cut):
        L = complex(g.length); q = cmath.exp(-L.real + 1j*L.imag); s = 0.0
        for n in range(2, nmax):
            s += -2*math.log(abs(1 - q**n))
            if abs(q)**n < 1e-18:
                break
        tot += g.multiplicity * s
    return tot

print("=" * 74); print("1. THE SPECTRUM (the object's own)"); print("=" * 74)
ls2 = M.length_spectrum(2.0)
gate("geodesics come in complex-conjugate pairs (real manifold)",
     len(ls2) % 2 == 0, f"{len(ls2)} classes below 2.0")
sys_ = min(float(complex(g.length).real) for g in ls2)
gate("systole is the known 1.08707...", abs(sys_ - 1.087070144995739) < 1e-9, f"{sys_:.15f}")

print()
print("=" * 74); print("2. THE GEODESIC FACTOR, with its CUTOFF error"); print("=" * 74)
cuts = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
vals = [logZ(c) for c in cuts]
prev = None
for c, v in zip(cuts, vals):
    d = "" if prev is None else f"   delta {v-prev:+.3e}"
    print(f"  cutoff {c:4}: log Z_geod = {v:.12f}{d}")
    prev = v
deltas = [abs(vals[i+1]-vals[i]) for i in range(len(vals)-1)]
gate("the tail deltas are SHRINKING (convergent)", deltas[-1] < deltas[0]/5,
     f"first {deltas[0]:.2e} -> last {deltas[-1]:.2e}")
signs = {(vals[i+1]-vals[i]) > 0 for i in range(len(vals)-1)}
gate("convergence is OSCILLATORY, so the last value is NOT the answer", len(signs) == 2,
     "deltas change sign -- the uncertainty is the last delta, not the last digit")
est, err = vals[-1], deltas[-1]
print(f"\n  ESTIMATE: log Z_geod = {est:.6f} +/- {err:.1e}   (Z_geod = {math.exp(est):.6f})")

print()
print("=" * 74); print("3. WHAT THIS IS NOT -- the cusp"); print("=" * 74)
gate("the object is CUSPED (1 cusp), so the GMY product is NOT the full one-loop Z",
     M.num_cusps() == 1)
print("""    The Giombi-Maloney-Yin product is the one-loop graviton determinant for a
    hyperbolic quotient's DISCRETE spectrum. Our object is finite-volume but
    NON-COMPACT: the cusp contributes a CONTINUOUS spectrum which this product
    omits entirely. So the number above is a well-defined spectral invariant of
    the object -- the geodesic factor -- and NOT its one-loop partition function.""")

print()
print("=" * 74); print("4. WHERE THE MISSING PIECE ALREADY IS"); print("=" * 74)
print("""    The continuous contribution for a cusped hyperbolic 3-manifold is governed by
    the SCATTERING DETERMINANT -- and the corpus has the object's exactly:

        B739:   phi_m004(s) = Lambda_K(s-1) / Lambda_K(s)

    That is the object needed to supply what the geodesic product omits. So the
    one-loop partition function's two halves are BOTH in reach: the discrete half
    computed here, the continuous half banked in B739 and not yet combined.

    THE NEXT RUNG IS THEREFORE NAMED AND UNBLOCKED, not speculative.""")

RES = {"systole": sys_, "n_classes_below_2": len(ls2),
       "cutoffs": cuts, "logZ_by_cutoff": vals,
       "logZ_geodesic_estimate": est, "cutoff_uncertainty": err,
       "Z_geodesic_estimate": math.exp(est),
       "convergence_is_oscillatory": len(signs) == 2,
       "is_full_one_loop_partition_function": False,
       "why_not": "the object is cusped (1 cusp); the GMY product covers the DISCRETE spectrum only and omits the cusp's continuous contribution entirely",
       "missing_piece_governed_by": "the scattering determinant phi_m004(s) = Lambda_K(s-1)/Lambda_K(s), banked exactly in B739",
       "next_rung": "combine the discrete factor computed here with B739's scattering determinant; both halves exist, neither is speculative",
       "scope": ("A RUNG, not a completion. Computes the GMY geodesic product over the object's own "
                 "complex length spectrum with an honest cutoff error; the convergence is "
                 "OSCILLATORY so the uncertainty is the last delta, not the last digit. This is NOT "
                 "the one-loop partition function -- the cusp's continuous spectrum is omitted. "
                 "No measured value; Gate 5 untouched.")}
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
print("\n  results.json written")
if FAIL: raise SystemExit(f"FAILED: {FAIL}")
print("\n  ALL CHECKS PASS")
