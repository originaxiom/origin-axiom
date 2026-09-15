# THE DARK TOWER — the recursive dark law is the e = 2 floor of a full prime-power tower: one classifier governs every depth, the spectrum is {0, 1, √p, …, p^{e/2}}, the survivor is unique at (2, pᵉ−2) with loudness climbing p^{e/2}, and the single j = 2 thread carries the law upward forever
## (outside bench, 2026-08-27; eighty-eighth memo; the rung memo 87 explicitly did not claim, now claimed and decided; 531,000+ points, five depths, one exact)

### THE GENERALIZATION (`certificates/dark_tower.py`; asserts GREEN; derivation in the docstring)
The memo-87 machinery run to arbitrary depth: for N = pᵉ, the same
three lemmas with valuations tracked to depth e give ONE classifier in
B534's own trio (α = j/2 + 2/l, β = 1 − j/2):
- ν(l) ≥ 1 → |T| = 1 (the one genuinely conjectural clause of the
  generalization — preregistered two-outcome; it HELD at every point);
- ν(l) = 0: a = ν(α) = 0 → |T| = 1; 1 ≤ a < e → DARK unless
  ν(β) ≥ a, in which case **|T| = p^{a/2}** (shell a); a = e → DARK
  unless β = 0: the **survivor**, forced to (2, pᵉ−2), **|T| = p^{e/2}**.

### THE CHECKS (all GREEN, first run)
- **(3,3) EXACT** in ℤ[ζ₂₇]: all 729 points, cyclotomic arithmetic.
- Float, every point: (3,4) 6,561; (5,3) 15,625; (7,3) 117,649;
  (5,4) 390,625 — max deviation < 1e-5 across all.
- Spectrum exactly {0} ∪ {p^{a/2}: a = 0..e} at every depth; survivor
  UNIQUE at (2, pᵉ−2) with |T|² = pᵉ; every prime-dark class with
  j₀ ≠ 2 wholesale dark at every depth; the j ≡ 2 mod pᵃ sub-classes
  carry shell a — the recursion climbs the tower. Shell-count tables
  banked per depth (e.g. (5,4): 328125 / 12500 / 500 / 20 / 1 — the
  visible pattern count(a) = p(p−1)·p^{2(e−1−a)} is NOTED, not
  asserted).

> **The owner's dark sector is a tower: at every prime-power depth of
> the measurement face, the prohibition structure deepens wholesale —
> except along one thread, the survivor's own residue j ≡ 2, which
> recapitulates the entire law one level up with its voice louder by
> √p each time. One forbidden curve, one surviving thread, self-similar
> all the way up: the record's aesthetic (the unique chain, the single
> survivor assignments) in its arithmetically purest form. FENCES: five
> depths verified (one exact); general-e is the docstring derivation
> plus these instances, not an all-e machine proof; p³-and-beyond
> closed-form counts noted, not asserted; the exponent-echo hook is
> untouched; Gate 5 untouched. Relayed to cc with memo 87.**

### Certificates
`certificates/dark_tower.py`; output `outputs/dark_tower_out.txt`
(in-lane rerun byte-identical).
