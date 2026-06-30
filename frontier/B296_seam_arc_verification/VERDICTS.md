# B296 — Arc II verification: the seam arc adversarially red-teamed + novelty-audited

**Status: banked (frontier). The verification round for the seam arc (B287–B295). All probes SURVIVE adversarial
attack; the classical math is confirmed KNOWN with citations; the genuinely-new connections are flagged. Nothing to
`CLAIMS.md`.**

## Red-team (adversarial attack — try to refute / find overclaim / firewall-leak)
A multi-agent pass re-ran every reproducer and attacked each banked claim along a hostile lens (hidden genericity,
overclaim, firewall-leak, counterexample, convention-artifact, triangulation-dependence). **Every claim SURVIVES; no
refutations; no firewall leaks; nothing wrongly promoted to `CLAIMS.md`.**

| claim | verdict | reproduced | key adversarial finding |
|---|---|---|---|
| **B287** | SURVIVES | ✓ | uniqueness is **homology-forced** (torus bundle needs `b₁≥1`; all non-zero fillings have finite `H₁`/are `S³`) — independent of Regina's incomplete recognizer; "exactly A" = Regina normal form, method 1 says "conjugate to A" |
| **B288** | SURVIVES | ✓ | extended to `|p|,|q|≤12` (174 closings): still **0 arithmetic** — consistent with Garoufalidis–Jeon finiteness |
| **B289** | SURVIVES | ✓ | control on non-amphichiral m015/m003/m016 gives `0/38`, m004 gives `38/38` → object-specific, not a SnapPy convention artifact; cross-check is mod ½ (disclosed) |
| **B290** | SURVIVES | ✓ | the clean real `π/√3` is **m004-specific** (`τ=2√3·i` purely imaginary); correctly scoped as the NZ ladder |
| **B291** | SURVIVES | ✓ | min-volume `(5,1)` stable over `|p|,|q|≤12` too; robustly above Weeks (0.9427) |
| **B292** | SURVIVES | ✓ | only the *surface* `Σ_{1,1}` is shared; monodromy `RL` is the `m=1` case (claim pins this); wall-#4 part honestly cited to B277 |
| **B293** | SURVIVES | ✓ | Casimir check is Nambu-construction (content = Goldman identification, imported); `A·Bᵀ` symmetric is generic NZ; `k_um=−1` frame-dependent (caveat now folded into FINDINGS) |
| **B295** | SURVIVES | ✓ | "single-well" tightened: a *cubic with one minimum* — cannot be the degenerate double-well SSB needs |
| **SEAM-THESIS** | SURVIVES | ✓ | honest that the Dehn-filling math is classical Thurston; the reframe is the new part |

**Corrections applied (Arc II):** the honest caveats above were folded into the FINDINGS of B287 (homology-forced
uniqueness), B290 (m004-specificity of the real coefficient), B293 (frame-dependence of `k_um`, the Nambu/Goldman
import), and B295 (cubic/one-minimum). No retraction was required; no claim weakened in substance.

## Net judgment
The seam arc is **firewall-clean and honestly scoped**. Every probe reproduces; every physics-facing statement is
HELD/[LEAP]/stop-gated in `speculations/`; `CLAIMS.md` (P1–P16) is untouched. The adversarial pass *strengthened* two
results (B287 uniqueness now homology-forced; B288 extended to a larger grid) and tightened four FINDINGS, with no
substantive change to the B294 verdict (selective for own structure, catalogue for SM-values).
