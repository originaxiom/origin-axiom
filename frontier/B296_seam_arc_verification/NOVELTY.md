# B296 — Novelty audit of the seam arc (prior-art assessment)

**Status: banked (frontier). An adversarial prior-art round on the seam arc's claims, honestly separating the
classical/standard mathematics from the genuinely-new connections. Nothing to `CLAIMS.md`.** Format: KNOWN (cite) /
PARTIALLY-KNOWN / APPEARS-NOVEL / NEEDS-SPECIALIST.

## The classical mathematics — KNOWN (and that is the point)
The arc is built on classical machinery, and the audit **confirms** the attribution (so the program is not claiming
the math as new):

| claim | verdict | prior art |
|---|---|---|
| **1 — distinguished closing.** 0-surgery = Sol torus bundle `[[2,1],[1,1]]`; 10 exceptional fillings; `±1,±2,±3` Seifert, `0,±4` toroidal | **KNOWN** | Thurston (exceptional-surgery classification of the figure-eight, *Notes* 1979); confirmed in multiple sources (arXiv:2409.06543 explicitly: 0-surgery = mapping torus of the cat map `[[2,1],[1,1]]`; arXiv:1310.3472, arXiv:2103.16348). The 0-surgery as the Sol/cat-map bundle is standard. |
| **2 — arithmeticity lost on closing.** Cusped `ℚ(√−3)` arithmetic; closed fillings generically higher-degree, non-arithmetic, no `√−3` | **KNOWN (genericity)** | **Garoufalidis–Jeon**: trace-field degree of `M_{p/q}` grows linearly in the slope (conditional on Lehmer), bounded above/below — so only finitely many arithmetic fillings. The *genericity* (degree growth, loss of arithmeticity) is a theorem; B288 is the explicit figure-eight instance (with `√−3`-membership tested). Also: Hodgson, Neumann–Reid (arithmetic Dehn surgery). |
| **4a — Goldman/NZ symplectic structure.** `{x,y}=2z−xy`, `κ` the Casimir; peripheral `(μ,λ)` the NZ conjugate pair | **KNOWN** | Goldman (the bracket on the one-holed-torus character variety; the cubic Fricke relation as Casimir); Neumann–Zagier (the peripheral symplectic form). Standard. |

## The genuinely-new connections — candidate-novel (the reframe is the new part)
These are the *connections/synthesis*, not the underlying math; the audit found no direct prior art this pass, so they
are flagged conservatively (a fuller literature round is pending):

| claim | verdict | note |
|---|---|---|
| **3 — handedness = trace-field Galois conjugation.** `CS(p,−q)=−CS(p,q)` = complex conjugation of the geometric rep = the `Gal(ℚ(√−3)/ℚ)` swap `u↔u²` = the `±π/6` Eisenstein-phase flip of `κ=u²+2=√3·e^{∓iπ/6}` | **PARTIALLY-KNOWN / NEEDS-SPECIALIST** | the pieces are classical (CS sign under orientation reversal; complex conjugation of trace fields for amphichiral manifolds); the *explicit identification* with the `±π/6` figure-eight commutator phase is the candidate-new packaging — not located in the audit. |
| **4b — Goldman/NZ peripheral clock ↔ Λ-conjugate-to-CS-time.** the peripheral symplectic pairing as the structural analog of Alexander–Magueijo–Smolin's "Λ conjugate to Chern–Simons time" | **APPEARS-NOVEL / NEEDS-SPECIALIST** | no prior work connecting a knot/3-manifold character-variety peripheral symplectic structure to the Kodama/Λ-as-time idea was found. Firewalled as `[HOOK]` regardless. |
| **5 — the reframe.** "an open complement is symmetric; closing it (Dehn filling = interaction with the nothing) breaks amphichirality/CP and generates a sign/scale/clock at the seam" | **APPEARS-NOVEL (framing)** | the math is classical; the *framing* (Dehn filling as boundary symmetry-breaking, the bulk/cusp ingredient split) was not found in the math or physics (3d-3d / Kodama) literature. A synthesis, honestly labeled. |

## Honest scope
This pass confirmed the **classical** claims with citations (which is the goal — correct attribution) and could not
locate direct prior art for the three **novel connections** (3, 4b, 5), which are therefore flagged
**NEEDS-SPECIALIST / APPEARS-NOVEL** and stay firewalled. The novel content is a *reframe + a set of connections*,
not new theorems; the program does not claim the mathematics as original. A fuller prior-art round on claims 3/4b/5 is
left **pending the next pass**.

## Anchors
`VERDICTS.md` (the red-team), `B287`–`B295` (the probes), `B286`/`B294` (the seam + verdict), `B285` (the ±π/6 phase),
`S044` (the Alexander Λ↔CS-time source). Lit: Thurston (exceptional surgeries), Garoufalidis–Jeon (trace-field degree
growth), Goldman / Neumann–Zagier (the symplectic structure), Alexander–Magueijo–Smolin arXiv:1807.01381.
