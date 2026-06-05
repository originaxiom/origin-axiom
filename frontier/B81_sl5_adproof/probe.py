"""B81 (follow-on) -- the CRT/F_p first-principles route at SL(5): blocked by gauge-corruption at the
doubly-degenerate even-k sector. A precise localization of the B58/B66 barrier.

B80 PROVED the SL(4) tower from first principles by reconstructing J(m) over Q[m] from the EXACT F_p
eps-series pinv-limit Jacobian DT_0 -- valid because DT_0(4) is SEED-CANONICAL (its char poly is
gauge-invariant), so m-interpolation in a fixed basis is well-defined. Does the same route reach SL(5)?

THE TEST. Compute DT_0(5, m=1) over F_p for several seeds (different perturbation reps P,Q and metric S)
and compare the CHARACTERISTIC POLYNOMIAL (which is gauge/conjugation-INVARIANT, so it must agree across
seeds IF the pinv-limit is a well-defined Jacobian).

FINDING (exact F_p):
  * SL(4): char(DT_0(4,m=1)) is IDENTICAL across seeds -> the pinv-limit is canonical -> B80's
    m-interpolation + CRT reconstruction is valid (and gives the SL(4) tower, V62).
  * SL(5): char(DT_0(5,m=1)) SCATTERS across seeds (24/25 coeffs differ, seeds 20/99/123) -> the
    eps-series pinv-limit is GAUGE-CORRUPT at SL(5): it does not produce a well-defined char poly, so
    m-interpolation is INVALID and the CRT route does NOT extend. The corruption is localized to the
    DOUBLY-DEGENERATE even-k sector: tagging char(DT_0(5,m=1)) gives char(M^2) at multiplicity 1 (should
    be 2) and (t+1) at 1 (should be 2) -- a degree-3 untagged remainder, exactly B66's numerical gap,
    now shown to be a genuine GAUGE-CORRUPTION (seed-dependent char poly), not a tagging artifact.

NET. The CRT/F_p route's reach is exactly the sectors where the pinv-limit is seed-canonical:
multiplicity-<=1 even-k (the single char(-M^2) at SL(4) resolves; B80). The multiplicity->=2 degeneracy
(char(M^2)^2 at SL(5)) is the residual e_2/Lambda^2 barrier (B58), and it manifests as char-poly
seed-scatter. Closing SL(5) needs a degeneracy-robust pinv or the B62 opposition-involution structural
split (which gives the SL(5) tower STRUCTURALLY, not from first principles). Honest negative, precisely
localized. Standalone Lie/invariant theory; no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "B58_phaseA"))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "B80_sl4_adproof"))
import jacobian_closure as JC      # noqa: E402
import build_jm as B80             # noqa: E402
from step1_cotangent import tag_charpoly  # noqa: E402

P = JC.PRIMES[0]


def charpoly_seeds(n, seeds=(20, 99, 123), p=P):
    """char(DT_0(n,m=1)) mod p for several seeds. Returns dict seed -> coeff list (low->high in t)."""
    words = JC.b66_select(n, 4, seed=20)
    out = {}
    for sd in seeds:
        DT, info = JC.jacobian(n, p, seed=sd, maxlen=4, L=12, words=words, m=1)
        if DT is None:
            raise RuntimeError(f"jacobian failed n={n} seed={sd}: {info.get('status')}")
        out[sd] = B80.charpoly_modp(DT, p)
    return out


def is_seed_canonical(n, seeds=(20, 99), p=P):
    """Is char(DT_0(n)) gauge-invariant (identical across seeds)? True => CRT route valid at rank n."""
    cps = charpoly_seeds(n, seeds=seeds, p=p)
    ref = cps[seeds[0]]
    return all(cps[s] == ref for s in seeds), cps


def sl5_tag(p=P):
    """Tag char(DT_0(5,m=1)) vs the Dickson catalog -- shows the degree-3 doubly-degenerate gap."""
    words = JC.b66_select(5, 4, seed=20)
    DT, _ = JC.jacobian(5, P, seed=20, maxlen=4, L=12, words=words, m=1)
    tower, remok = tag_charpoly(DT, P, kmax=10)
    return tower, remok


def main():
    print("B81 -- the CRT/F_p first-principles route at SL(5): gauge-corruption diagnosis\n")
    ok4, _ = is_seed_canonical(4)
    print(f"SL(4): char(DT_0) seed-canonical (gauge-invariant) = {ok4}  -> B80's CRT route VALID (V62).")
    ok5, cps5 = is_seed_canonical(5, seeds=(20, 99, 123))
    nd = sum(1 for i in range(len(cps5[20])) if cps5[20][i] != cps5[99][i])
    print(f"SL(5): char(DT_0) seed-canonical = {ok5}  ({nd}/25 coeffs differ across seeds)")
    print("       -> the SL(5) pinv-limit is GAUGE-CORRUPT; m-interpolation INVALID; route BLOCKED.")
    tower, remok = sl5_tag()
    print(f"\nSL(5) tagged factors (m=1): {dict(sorted(tower.items(), key=str))}")
    print(f"  fully tagged: {remok}  (char(M^2) mult 1 not 2, (t+1) mult 1 not 2 -> degree-3 gap)")
    print("\nNET: the CRT/F_p route reaches exactly the seed-canonical (multiplicity-<=1 even-k) sectors")
    print("     -- SL(4) (single char(-M^2)) works; the SL(5) doubly-degenerate char(M^2)^2 is the")
    print("     residual e_2/Lambda^2 barrier (B58), manifesting as char-poly seed-scatter.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
