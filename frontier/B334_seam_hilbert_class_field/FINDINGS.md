# B334 — the seam's Hilbert class field *is* the two-ended compositum (and it reconciles B333)

**Status: banked (frontier). Verify-don't-trust on the Chat handoff (2026-07-01). Firewalled; nothing to `CLAIMS.md`.**
The handoff proposed a genuine theorem with a physical reading and a self-killed numerology. Verified; banked with the
tautological part flagged and the apparent tension with B333 resolved.

## The theorem (verified, [MATH])
**`H(ℚ(√−15)) = ℚ(√5, √−3)`** — the Hilbert class field of the seam is the two-ended compositum. (Genus theory:
disc `−15 = −3·5` has two ramified primes, so the genus field has degree `2^{2−1} = 2 = h(−15)`, hence genus field =
Hilbert class field = `ℚ(√−3, √5)`.) **Verified two ways:**
- **Splitting law.** A split prime `p` of `ℚ(√−15)` is **principal** ⟺ it splits completely in `ℚ(√5,√−3)` ⟺
  `(5|p)=(−3|p)=+1` ⟺ **`p ≡ 1, 4 (mod 15)`**; **non-principal** ⟺ both `−1` ⟺ **`p ≡ 2, 8 (mod 15)`**.
- **Form cross-check.** Principal ⟺ represented by the principal form `x²+xy+4y²` (disc −15): **0 mismatches**.

## The reading (the lovely part, [MATH] structure + [LEAP] physics)
The seam `ℚ(√−15)` has class number 2 — its arithmetic is **incomplete** (not a UFD). Its **completion** — the minimal
extension where every ideal becomes principal — is exactly the **two-ended compositum**. So:

> **The two ends `√5 (→E₈)` and `√−3 (→E₆)` are the arithmetic completion of the seam `√−15`.** The object, touching both
> ends, *is* the completion of its own seam. And the class group `ℤ/2` is the arithmetic partition: **principal**
> (self-contained in the seam) vs **non-principal** (needs both ends to factor) — `[LEAP]` a structure/value dichotomy.

This is a genuinely new *interpretation* (the class field theory itself is standard). It deepens B332 (the two ends are
the product/ratio of the founding letters) with *why* they belong together: they are the seam's own Hilbert class field.

## Reconciliation with B333 (important — not a contradiction)
- **B333:** `ℚ(√−15)`'s **intrinsic invariants** are generic (`h=2` shared by 14 fields to −400; units `{±1}`) → **no
  value** in the field. ✓
- **B334:** its **relational structure** is exact and distinguished (its HCF is the two ends). ✓
- **Both hold.** The value is *not* in the field (generic invariants; the `137` prediction is dead — see below); but the
  *structure* (the seam completes to the two ends) is precise. Distinguished **relationally**, generic **intrinsically**.
- The handoff's "unique because disc `= 3·5`" is **true but nearly tautological** (the field is *defined* by its primes;
  "unique field with disc −3·5" is a definition, not a discovered property). The genuine content is the HCF relation.

## The null test (137, killed — agreeing with the handoff)
`137 ≡ 2 (mod 15)` → **non-principal**. Striking (`137`) — but **dead**: the non-principal fraction is `≈ 0.556` (that
is what `h=2` *means*), a coin flip. No SM content can be extracted from which class one number lands in. **DEAD as a
prediction** (do not resurrect).

## The firewall (held)
Class field theory + a null test; no value produced or matched. Consistent with B333/B326/B331: the value needs the
external relation (Level 4), not the seam's arithmetic. Nothing to `CLAIMS.md`.

## The fence
Exact Legendre/Jacobi splitting + binary-quadratic-form cross-check (sympy) + the `137` null test. No physics values.
Nothing to `CLAIMS.md`.

`seam_hcf.py` (pyenv) · `tests/test_b334_seam_hilbert_class_field.py`. Related: **B333** (the seam is intrinsically
generic — reconciled here), **B332** (the two ends = product/ratio), **B326** (Level-4 texture), **S046**
(value-at-the-seam). Lit: genus theory of imaginary quadratic fields (Gauss; the genus field = HCF when `h = 2^{t−1}`).

---

## VINDICATION (2026-07-04, the atlas revival hunt): B334 was right before the instruments

The identification stated here (H(ℚ(√−15)) = ℚ(√5,√−3), the seam's own class field) sat
atlas-tagged as dead-with-the-arc. The Wall Campaign's sixth angle (B401, owner-proposed)
independently rebuilt it and went further: the ℤ/2 class group ACTS on the banked
constants (slot ↔ −3-block; the two ±1/24 faces are one orbit), the split-covariance
prediction was CONFIRMED, the genus characters gate the values (P68: the Eisenstein gate
as a root-of-unity order theorem), and the boundary is character-equipartitioned. B334 →
B401/P68 is the program's first complete revival cycle: an interpretation that died for
lack of instruments, reborn as theorems when the instruments arrived. (Atlas lineage
note; status of the INSIGHT: vindicated; the arc's other members unchanged.)
