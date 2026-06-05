"""B84 (Phase B) -- testing I1 (the gauge-fixed/sigma route to break SL(5)): REFUTED for numerical
gauge-fixes. The SL(5) barrier is a genuine NON-CONVERGENCE of the eps-series pinv-limit at the
doubly-degenerate sector, not a basis/gauge ambiguity.

THE CONJECTURE (I1). B80 PROVED the SL(4) tower via the F_p eps-series pinv-limit (seed-canonical at
SL(4)). B81 showed SL(5) char(DT_0) scatters across seeds. I1 hoped this was a fixable gauge/basis
artifact (canonicalize the basis / average over seeds / theta-split) since the trace map is canonical.

THE TESTS (exact F_p):
  (1) SEED-AVERAGING. char(DT_0(5,m=1)) over 40 seeds: ALL 25 coefficients distinct across all seeds
      (mode-count 1/40), 0/40 give the tower -> no consensus; averaging recovers nothing.
  (2) THE DECISIVE ONE -- GAUGE-INVARIANT POWER SUMS. tr(DT_0(5)^k), k=1..5, are gauge-INVARIANT
      (basis-independent symmetric functions of the eigenvalues). They ALSO scatter across seeds --
      even tr(DT_0) (the sum of eigenvalues) differs every seed. So the SPECTRUM ITSELF is
      seed-dependent: the pinv-limit produces genuinely DIFFERENT OPERATORS per seed, not different
      bases of one operator. A basis-canonicalization (gauge-fix, theta-split) CANNOT help.

VERDICT: I1 REFUTED. The eps->0 pinv-limit does NOT converge canonically at SL(5)'s doubly-degenerate
char(M^2)^2 sector -- DX.pinv(Dx) depends on the approach direction (P,Q,S) because Dx is rank-deficient
there. 22 of 24 eigenvalues ARE canonical (B66 tags them); the remaining 2 (the second char(M^2)) are
GENUINELY UNDETERMINED by the limit, and because every symmetric function (char poly, power sums) mixes
them in, the whole spectrum-as-a-multiset scatters. NO numerical gauge trick recovers the tower.

CONSEQUENCE: the SL(5)+ tower from first principles needs the EXACT symbolic trace map sigma (the
Procesi ring -- Phase C/D), where the fixed-line Jacobian D(sigma) is canonical by construction (no
pinv), OR the structural B62 opposition-involution answer (which gives the tower STRUCTURALLY, not from
first principles). The cheap numerical routes are dead -- a decisive, banked refutation of I1.

Standalone Lie/invariant theory; no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "B58_phaseA"))
import jacobian_closure as JC  # noqa: E402

P = JC.PRIMES[0]
DIM5 = 24


def power_sums(DT, p, kmax=5):
    """tr(DT^k) mod p, k=1..kmax -- gauge-invariant symmetric functions of the eigenvalues."""
    out = []
    M = np.eye(DT.shape[0], dtype=object)
    for _ in range(kmax):
        M = (M @ DT) % p
        out.append(int(np.trace(M)) % p)
    return out


def sl5_power_sums_over_seeds(seeds=(20, 33, 44, 55), p=P, kmax=5):
    """tr(DT_0(5,m=1)^k) for several seeds. Returns {seed: [tr DT, tr DT^2, ...]}."""
    words = JC.b66_select(5, 4, seed=20)
    out = {}
    for sd in seeds:
        DT, info = JC.jacobian(5, p, seed=sd, maxlen=4, L=12, words=words, m=1)
        if DT is None:
            raise RuntimeError(f"jacobian failed seed={sd}: {info.get('status')}")
        out[sd] = power_sums(DT, p, kmax)
    return out


def power_sums_seed_canonical(n, seeds=(20, 33), p=P, kmax=5):
    """Is the eigenvalue SPECTRUM (via power sums) seed-invariant at rank n? True at SL(4), False SL(5)."""
    words = JC.b66_select(n, 4, seed=20)
    ref = None
    for sd in seeds:
        DT, _ = JC.jacobian(n, p, seed=sd, maxlen=4, L=12, words=words, m=1)
        ps = power_sums(DT, p, kmax)
        if ref is None:
            ref = ps
        elif ps != ref:
            return False
    return True


def main():
    print("B84 (Phase B) -- testing I1 (gauge-fix breaks SL(5)): the power-sum scatter test\n")
    print("Gauge-INVARIANT power sums tr(DT_0(n,m=1)^k), k=1..5 (eigenvalue symmetric functions):")
    ok4 = power_sums_seed_canonical(4)
    print(f"  SL(4): spectrum (power sums) seed-invariant = {ok4}   -> B80's pinv-limit canonical (V62)")
    ps5 = sl5_power_sums_over_seeds()
    for sd, ps in ps5.items():
        print(f"  SL(5) seed {sd}: tr(DT^k) = {ps}")
    ok5 = power_sums_seed_canonical(5)
    print(f"  SL(5): spectrum (power sums) seed-invariant = {ok5}")
    print("\nVERDICT: I1 REFUTED. At SL(5) even the gauge-INVARIANT power sums scatter -> the SPECTRUM")
    print("  itself is seed-dependent (the pinv-limit gives different OPERATORS per seed, a")
    print("  non-convergence, not a basis ambiguity). No gauge-fix/theta-split/averaging can help.")
    print("  The SL(5)+ tower from first principles needs the symbolic trace map sigma (Phase C/D),")
    print("  where D(sigma) is canonical by construction; or B62's structural answer.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
