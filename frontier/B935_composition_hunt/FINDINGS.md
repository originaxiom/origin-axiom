# B935 — THE COMPOSITION HUNT: rigidity + a rank-2 degeneracy — the forced compositions produce NOTHING new, and the reason is structural

**Date:** 2026-08-07 · **Seat:** computation agent (interrupted by an auth failure;
completed and amended by cc) · blind — no measured number contacted.

## The result

The closed whitelist of four forced compositions — (i) R-conjugation R^T Ĝ R,
(ii) the polar/singular decomposition of Ĝ, (iii) both orderings ĜR and RĜ,
(iv) the v-weight conjugation D_v^{1/2} Ĝ D_v^{-1/2} — yields **exactly four
invariant triples, most of them FORCED to coincide**:

- eig(R^T Ĝ R) = eig(Ĝ) exactly (orthogonal similarity, verified 4.6e-151)
- eig(D_v-conj) = eig(Ĝ) exactly (diagonal similarity, 1.5e-151)
- eig(ĜR) = eig(RĜ) exactly (the AB/BA theorem, 3.1e-151)
- sv(R^T Ĝ R) = sv(ĜR) = sv(RĜ) = sv(Ĝ) exactly

**No composition is independent.** The hunt's premise — that composing the
object's four cascade classes might yield a new shape — is answered NO by
similarity, not by numerics.

## The structural reason: THE OVERLAP MATRIX IS RANK 2

The singular-value cubic of Ĝ has an **exact zero root** (det X2 = 0 exactly;
the same for the v-conjugate): one direction of the S register has **no overlap
whatsoever** with the A family. Consequences:

- The composed matrices' eigen-triples are not descending-positive — **the
  cascade index is UNDEFINED for them** (one entry is exactly 0).
- **Zero compositions land in the [1.2, 1.6] band** (band_flags = []).
- The object's register mixing geometry has only TWO nonzero directions: it
  **cannot** produce a three-term mixing cascade by this route at all.

## Banked base classes (for the record)

v-weights ASCENDING (4.410, 2.886, 2.386; index 0.448) · m_S descending
(index 1.838, matching B929's T1) · the S–A moduli (B930) · the rotation's
rational spectrum (B930).

## Amendments (both logged, both the same species as B930's)

(1) the design asserted three positive singular values — the object has two
(positivity assumed again; the abort was the finding). (2) The belt bar of
1e-80 exceeded this machinery's precision floor (sqrt-of-small costs half the
digits; B930's independent belt lands at 3.9e-76 by the same route) —
recalibrated to the house 1e-40 standard with the achieved value recorded.

## Files

`compose.py` → `results.json`, rerun logs · locks: `tests/test_b935_b938.py`.
