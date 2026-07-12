# B548 — The un-hideability census (pre-registration)

*Committed before compute. Tests the conjecture sharpened by the Hoffman +
Barrett pointers: an object is faithfully reconstructable from any window
(UN-HIDEABLE) iff its reconstruction prior is INTRINSIC (self-priored) — the
grammar alone collapses the abelianization's lifts to a single conjugacy
class. B535 proved σ is un-hideable (17,280 lifts → 2 = {σ, conj}). Census:
which small substitutions share the property?*

**Method:** for a family of primitive substitutions on 2-4 letters, take the
incidence matrix, enumerate all substitutions with the same column Parikh
vectors (the "lifts"), and count distinct languages after grammar+language
filtering (as in B535 C2). UN-HIDEABLE := grammar+language collapses lifts to
one conjugacy class (a small constant, all conjugate); HIDEABLE := many
distinct languages survive.

**Predictions:** (1) Fibonacci a→ab, b→a is un-hideable (small alphabet, rigid
grammar). (2) Un-hideability correlates with the Pisot/irreducible-charpoly
property, NOT with alphabet size. (3) A reducible or high-permutation-freedom
substitution is hideable. **Falsifier:** un-hideability tracks alphabet size
only, or is universal (every substitution un-hideable) → the property is
trivial and the conjecture is vacuous.
