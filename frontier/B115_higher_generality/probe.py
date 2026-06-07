"""B115 -- higher-rank and higher-genus generality of degree=rank (exploratory scoping; #4 + #5).

Two exploratory questions about how far degree=rank (L = c*M^n) and the off-locus sector generalize. Both are
HONEST SCOPINGS: a tractable computable piece + the specific obstruction for the rest. NO physics; no CLAIMS.md;
the rho_n proof stays the prize; P1-P16 untouched.

#5 -- the off-locus sector at SL(4). B110 proved the off-locus sector is EMPTY for 4_1 at SL(3) (all 3
irreducible components lie ON the forced locus tr A = tr A^-1). TRACTABLE CHECK (this probe): the two known SL(4)
Dehn-filling reps (B106 principal {1,1,omega,omega^2}, secondary the 8th roots) are ALSO ON the forced locus
(tr A = tr A^-1: principal 1=1, secondary 0=0). So -- exactly as at SL(3) -- the KNOWN SL(4) components are
forced-locus; any off-locus SL(4) content lives in OTHER, UNCOMPUTED components. OPEN: there is no SL(4)
figure-eight character-variety classification (the SL(3) one is Heusener-Munoz-Porti arXiv:1505.04451; no SL(4)
analogue exists in the literature), so whether off-locus SL(4) components EXIST is genuinely uncomputed -- the
specific obstruction is the missing SL(4) figure-eight character-variety classification.

#4 -- genus-2 generality (Task 6 / B91). degree=rank L = c*M^n is a peripheral property of the once-punctured-
torus (genus 1, F_2) bundle, ESTABLISHED for the whole metallic family (all m: L = (-1)^{n-1} M^n, B71/B83/B89).
SCOPING: genus-2 generality asks whether the analogous relation holds for a genus-2 surface bundle (F_4, a
different fundamental group with a richer peripheral/boundary structure). This needs a genus-2 SL(n)
character-variety construction NOT in the repo (the trace-map machinery here is F_2 / once-punctured-torus
specific). The specific obstruction: the genus-2 peripheral structure (more boundary curves; the longitude is no
longer a single commutator [A,B]); degree=rank's "L = power of M" presumes the genus-1 peripheral pairing
(meridian = monodromy, longitude = the single puncture). Scoped as a future probe with this obstruction named;
the genus-1 metallic-family degree=rank (B71/B83) is what is established.

This stage records the SL(4)-forced-locus check (computable) + the two honest scopings.
"""
from __future__ import annotations

import numpy as np

_W = np.exp(2j * np.pi / 3)
_Z = np.exp(1j * np.pi / 4)
_SL4_SPECTRA = {"principal": [1, 1, _W, _W ** 2], "secondary": [_Z, _Z ** 3, _Z ** 5, _Z ** 7]}


# --------------------------------------------------------------------------- #
# #5 -- the SL(4) off-locus check (the computable piece)
# --------------------------------------------------------------------------- #
def sl4_dehn_filling_on_forced_locus():
    """The two known SL(4) Dehn-filling reps (B106) are ON the forced locus tr A = tr A^-1 (like SL(3), B110)."""
    out = {}
    for name, spec in _SL4_SPECTRA.items():
        s = np.array(spec, complex)
        trA, trAinv = complex(s.sum()), complex((1 / s).sum())
        out[name] = {"tr_A": trA, "tr_Ainv": trAinv, "on_forced_locus": abs(trA - trAinv) < 1e-9}
    return {"per_component": out, "all_on_forced_locus": all(v["on_forced_locus"] for v in out.values()),
            "conclusion": "the known SL(4) Dehn-filling reps are forced-locus (like SL(3)); off-locus SL(4) "
                          "content (if any) is in OTHER, uncomputed components",
            "obstruction": "no SL(4) figure-eight character-variety classification exists (the SL(3) one is "
                           "Heusener-Munoz-Porti 1505.04451; no SL(4) analogue) -- off-locus SL(4) is genuinely "
                           "uncomputed/OPEN"}


# --------------------------------------------------------------------------- #
# #4 -- genus-2 scoping (the obstruction)
# --------------------------------------------------------------------------- #
def genus2_scope():
    """degree=rank L=c*M^n is a genus-1 (once-punctured-torus, F_2) peripheral property, established for the whole
    metallic family (B71/B83). Genus-2 generality needs new machinery; the obstruction is the genus-2 peripheral
    structure."""
    return {"established_genus1_metallic": "L = (-1)^{n-1} M^n for the metallic once-punctured-torus family, all m "
                                           "(B71/B83/B89)",
            "genus2_status": "OPEN -- requires a genus-2 SL(n) character-variety construction not in the repo",
            "obstruction": "the genus-2 peripheral structure: more boundary curves; the longitude is no longer a "
                           "single commutator [A,B]; degree=rank's 'L = power of M' presumes the genus-1 "
                           "meridian=monodromy / longitude=single-puncture pairing",
            "scoped_as": "a future probe (Task 6 / B91), with the obstruction named"}


def main():
    print("=" * 78)
    print("B115 -- higher-rank + higher-genus generality of degree=rank (exploratory scoping)")
    print("=" * 78)
    print("\n[#5] off-locus at SL(4): are the known SL(4) Dehn-filling reps on the forced locus?")
    r = sl4_dehn_filling_on_forced_locus()
    for name, v in r["per_component"].items():
        print(f"    {name}: tr A={v['tr_A']:.3f}  tr A^-1={v['tr_Ainv']:.3f}  forced-locus={v['on_forced_locus']}")
    print(f"    all forced-locus: {r['all_on_forced_locus']}")
    print(f"    => {r['conclusion']}")
    print(f"    obstruction: {r['obstruction']}")
    print("\n[#4] genus-2 generality of degree=rank:")
    g = genus2_scope()
    print(f"    established (genus 1, metallic): {g['established_genus1_metallic']}")
    print(f"    genus-2: {g['genus2_status']}")
    print(f"    obstruction: {g['obstruction']}")
    print("\nVERDICT: the known SL(4) Dehn-filling reps are forced-locus (like SL(3)); off-locus SL(4) + genus-2")
    print("degree=rank both need machinery not in the repo -- scoped OPEN with the specific obstructions. NO physics.")


if __name__ == "__main__":
    main()
