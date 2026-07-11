# B528 — The DGG higher-rank gauge group: RESOLVED (computed + cited)

**Why this exists.** The ROAD-TO-REALITY handoff read the higher-rank 3d–3d gauge group as **U(N−1)
nonabelian**; I had banked **abelian U(1)^{r_K}** — flagged SHAKY by the B525 audit (cited, not computed).
The owner: *"compute it… you are a serial false killer."* So I (1) computed the actual gauge data from
SnapPy's Neumann–Zagier datum, and (2) ran a 99-agent adversarial deep-research on the primary sources
(`deep_research_report.md`). The result honours **both** seats. Firewalled; nothing to `CLAIMS.md`.

## What I computed (SnapPy, figure-eight, from the NZ datum — not cited)
The gluing/NZ matrix is **integer-valued**:
```
[ 2 1 0  2 1 0]  edge   [ 1 0 0  0 0 -1]  cusp (meridian)
[ 0 1 2  0 1 2]  edge   [ 1 1 1  1 -1 -3] cusp (longitude)
```
- **SL(2) gauge group = U(1)^{N−c} = U(1)^{2−1} = U(1)** — the textbook T[4₁] = U(1) + 2 chirals.
  **Abelian, computed.** Integer NZ data is the signature of an *abelian* CS-matter theory.
- **The handoff's "N−1" ladder = the cusp/boundary Cartan rank K−1** (K=2→1, 3→2, 4→3) — the *abelian*
  U(1)^{K−1} flavor/boundary symmetry, not a gauge group. Computed.

## What the research confirmed (primary sources, 3-0 adversarial)
- **(a) SL(2): ABELIAN.** DGG (arXiv:1108.4389) verbatim: T[M] is "the IR fixed point of an **abelian**
  Chern–Simons–matter theory"; Gang–Yonekura (1803.04009 eq 1.3): figure-eight = "a U(1)_0 vector coupled
  to two charge +1 chirals." Matches my computation.
- **(b) K≥3: STILL ABELIAN, no nonabelian ladder.** Dimofte–Gabella–Goncharov (arXiv:1301.0192) abstract
  verbatim: "**Just as for K=2, the theories T_K[M] are described as IR fixed points of abelian
  Chern–Simons–matter theories.**" Single-tetrahedron ladder (their Table 1.6): K=2 U(1) flavor / no gauge;
  K=3 U(1)^4 / no gauge; K=4 U(1)^9 / no gauge; **K=5 first gauge group, and it is abelian U(1)²**. Flavor
  rank U(1)^{(K−1)²}. **There is NO U(2)@K=3 or U(3)@K=4 — no U(N−1) nonabelian gauge ladder.**
- **(c) The "U(N−1) nonabelian gauge" reading is a gauge-vs-structure-group CONFLATION.** The nonabelian
  SL(N,ℂ)/PGL(K,ℂ) is the **structure group** of the flat connection / the gauge group of complex
  Chern–Simons *on M* — DGG explicitly state K "**does not appear as the rank of a gauge group**." So the
  generic-gauge claim "U(N−1) at rank N" is **FALSE as stated.** My "abelian at all K" was **correct** —
  and is now computed (SL(2)) + cited (all K), no longer a bare citation.

## The part I would have false-killed (the honest other half)
**The handoff's "U(N−1)" is NOT baseless.** (e), 3-0 verified: **Gang–Kim–Romo–Yamazaki (arXiv:1510.05011)**
give a genuinely **nonabelian** description of T_N[M] **in the defect setting**, built from the **T[SU(N)]
domain-wall quiver U(1)×U(2)×⋯×U(N−1)** (nonabelian for N≥3) — required because codimension-4 defects are
labelled by SU(N) representations an abelian description *cannot see*; a Higgsing prescription maps it back
to the abelian description. That quiver's top factor is **exactly U(N−1)**. So the handoff was pointing at a
**real nonabelian object** — the domain-wall quiver in the defect sector — and misattributing it as "the
generic DGG gauge group." Cordova–Jafferis (1305.2891): the M5-brane reduction gives complex *nonabelian*
Chern–Simons — again the structure-group/CS side, not the T[M] gauge group.

## Verdict (both seats, fairly)
| claim | verdict |
|---|---|
| generic 3d gauge group of T_N[4₁] is abelian at all K | **TRUE** (computed SL(2); cited DGGon "abelian CS-matter" all K) |
| "U(N−1) nonabelian is THE generic gauge group at rank N" | **FALSE** — gauge↔structure-group conflation (DGG: "K is not a gauge rank") |
| the "N−1" pattern | the abelian cusp Cartan rank K−1 (computed) — and echoes the defect quiver's top factor |
| a genuine nonabelian U(1)×U(2)×⋯×U(N−1) exists in the 3d–3d story | **TRUE**, but only in the **defect sector** (Gang–Kim–Romo–Yamazaki), not the generic T_N[M] gauge group |

**Net:** my banked "abelian at all K" stands — now computed + cited, no longer SHAKY. But the honest lesson
(the reason to *investigate*, not dismiss): the handoff's nonabelian instinct corresponds to a **real object**
(the T[SU(N)] defect quiver) that a flat "you conflated it, abelian, done" would have buried. Both are true at
once: generic gauge abelian, defect-sector quiver nonabelian. Cross-refs: [[B524]] (updated), [[B490]]
T-NOGO-DGG (holds — no *generic* nonabelian gauge), `deep_research_report.md`.
