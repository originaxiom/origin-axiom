# S005 — baryon-asymmetry amplitude `|Z(W1)/Z(W2)| ≈ 10⁻⁹`

**Status: `HELD(value-matching)`.** Firewalled; **explicitly not support.** See the HELD rule in `GOVERNANCE.md`.

**The proposed calculation.** From the B106 D1 Jacobian/torsion data at the W1 and W2 components, form the
Chern–Simons-amplitude ratio `n_B/n_γ ≈ |Z(W1) − Z(W2)| / |Z(W1) + Z(W2)|`, and check whether it lands near the
observed `≈ 10⁻⁹`.

**Why it is HELD, not ACTIVE/SUPPORTED.**
- **No derivation** that this ratio *is* `n_B/n_γ` (requirement (a) of the HELD rule unmet) — the identification
  "W1/W2 amplitude ratio = baryon-to-photon ratio" is asserted, not derived.
- **No banked W1/W2 amplitude formula exists** (B96's CS amplitude is volume-controlled, a restatement; there is no
  W1-vs-W2 split in the repo) — so the calculation also needs new machinery before it can even be run.
- **No null-hypothesis test** (requirement (b)) — `≈ 10⁻⁹` over an unconstrained ratio is exactly the failure mode
  that killed the cosmological-constant value (`S014`): one must ask how often a random pair matches as well.

**Rule for promotion.** The number MAY be computed once the amplitude is defined — but it stays HELD (a number in
search of a meaning) until BOTH a derivation that it is `n_B/n_γ` AND a passed null test exist. **Do not bank
`≈10⁻⁹` as evidence.** The *structural* A↔B asymmetry that motivates it is the separate `SUPPORTED` item `S004`.

Related: `S004` (the structural sibling), `S014` (the value-match that this discipline exists because of).
