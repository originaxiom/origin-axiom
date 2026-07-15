# B606 — the norm bridge (runs under NORM_FORM_PREREG.md, sha256 cc1ba3e1…)

## Post-seal, PRE-RUN realization (registered before any cell output)

The sealed MB12 note asserted "both outcomes live" for NF-1 without
computing it. Scrutiny against the banked factorizations decides it:
τ₄ = 2⁷·3·7·**97** and τ₈ = 2¹⁴·3³·5·7³·11·13·**31·607·49297** carry
large primes that appear NOWHERE in N₄ = 2⁹·3²·5·7·13 or
N₈ = 2¹⁵·3⁵·5³·7²·11. Any nonzero k₄ (resp. k₈) introduces 97 (resp.
31·607·49297) on one side with no partner, so the exact identity forces
k₄ = k₈ = 0, which fails on N₈ ≠ N₄. **NF-1 as sealed is
pre-determined-fail** — the third sealing lapse of this class today
(V1's vacuous operation, V3's unsatisfiable clause, NF-1's decidable
scan), each caught one step later in the pipeline. The cells run as
sealed; the expected outcome is D-nf; and the DIAGNOSIS is itself the
finding: **the torsions and the hearing integers are arithmetically
independent beyond the small primes** — the torsions carry arithmetic
(97; 31, 607, 49297) that the responses provably do not, so no pure
torsion-power normalization can ever close the value gauge. Per the
locked D-nf clause, the value question needs richer data (word-response
norms; the E₆₂ off-diagonal data).

Standing lesson to add to the MB12 memory: "both outcomes live" is a
CLAIM — compute the discriminating fact (here: prime supports) before
sealing, not after.

Run log follows; each cell banked blind per the sealed order.
