# R25: the reference wall supplies the opposite response, with mirror modes

## VERDICT AS THE SEAT STATES IT
"Implementing R23's positive reference mass as a free physical collar produces a six-dimensional Weyl channel on the actual negative-mass eigenline. On R24's whole rounded source boundary its effective four-dimensional index is -k, opposite the interior +k. Its anomaly is the negative of the FULL R23 eigenbundle response... The cost is also computed: it is a mirror sector, and moving its normalized modes toward the ends does not decouple them from the unchanged normalizable constant gauge field... This is therefore an explicit conditional free completion, NOT a source-selected defect, a mirror-free physical theory, or a no-go for other completions. R19's conditional three/zero kernel is not withdrawn."

## DECLARED INPUTS AND HYPOTHESES
- Banked identity: "R23's actual two-flavour charged mass symbol and positive equal-mass reference; R24's whole rounded-boundary eigenline flux; R19's constant gauge zero mode."
- Sourced: Choi–Ohmori (arXiv:2205.02188) discussion after (2.57); Fukaya et al. (arXiv:2001.03318) (2.1)–(2.12); Freed §4; Taylor (10)–(16),(33)–(36) — "Standard domain-wall localization and spin-surface index theory are mathematical inputs, not discoveries or automatic source-derived physical sectors."
- Scope (P0): "the free charged two-flavour Dirac theory on a product collar of each compact, rounded, nonzero-mass source boundary in R24's positive proper-arc class. The interpolation to a scalar reference mass is an ADDED ansatz. Neither an arbitrary physical defect nor every completion is quantified over."
- Assumed/expected (P6): "expect a realizable free interface with opposite boundary index, not a mirror-free completion... No negative on other defect, massive-U1, nonabelian or interacting routes."
- Seals: design/producer/tests "sealed and pushed at 16ba8ce1, before their first execution."

## CONTROLS
- Chirality-sign controls: "All Clifford anticommutators, the original kinetic map and the reversed-sign rejecting control pass."
- Normal-channel decay controls: "All four asymptotic sign pairs are tested: a crossing gives one chirality, a non-crossing gives none. The constant positive channel has no two-sided normalizable normal solution."
- Normalization-integral controls: "Exact integer-exponent polynomial integrations give 2, 4/3, 16/15 and 32/35, rejecting a missing Jacobian or factor."
- Index-theorem controls: "Omitting S would give -k+1-g: for g=4,k=3 it incorrectly gives -6. An independent spherical Cech control enumerates the monomials of O(d-1)... It gives (h0,h1)=(max(d,0),max(-d,0)) and index d for every tested d=-4..4."
- Reference-sign control: reversing which projector crosses "reverses the mass flux [and] reverses the result; zero flux gives zero net index."
- Localization/decoupling control: "The exact translating control f_R(x)=sqrt(M) exp(-M|x-R|)... Its constant-gauge coupling stays g7/sqrt(V)," rejecting the idea that pushing modes to the ends suppresses their gauge charge.
- **Retained failure carried forward**: "the failure being the preserved R24 raw matrix comparison" (i.e., R25's own regression explicitly keeps R24's known structural-equality failure rather than silently fixing it).

## TESTS ON THIS BENCH
```
15 passed in 11.34s
```
(`tests/test_physical_bridge_boundary_wall*.py`, from `<audit worktree @ 5e063851>`). No failures in this narrow selection (the report's own focused-dependency run separately reports "71 passed, 1 failed," the one failure being R24's already-documented raw matrix-comparison instrument failure, not a new BOUNDARY_WALL defect).

## CLAIMS FOR MAIN
1. Interpolating R23's positive reference mass to a free scalar-mass "wall" on the source boundary produces a normalizable six-dimensional Weyl channel with four-dimensional index exactly −k (opposite the interior +k) — PROVED-BY-SEAT (within the stated free/product-collar ansatz).
2. This wall's anomaly polynomial equals minus R23's full degree-eight eigenbundle response, for either reference sign — COMPUTED.
3. Localizing the wall's modes toward the ends does not decouple them from the existing normalizable constant gauge zero mode (charge is not suppressed by small overlap) — PROVED-BY-SEAT (for the stated minimally-coupled constant-profile gauge field).
4. This is "an explicit conditional free completion," not a derivation of a physical mechanism, source selection, or mirror-free spectrum — CONDITIONAL, as the seat itself states.

## CONFLICTS WITH MAIN
Searched main's `docs`/`frontier` for "mirror sector," "domain-wall localization," "BOUNDARY_WALL." "Mirror sector" appears in several main docs (e.g. `docs/CAMPAIGN_STATUS.md`, `docs/OPEN_LEADS.md`, `frontier/B1408_the_precision_requirement/`) but in unrelated contexts (different constructions), not this round's specific wall/index claim. No hit ties main's record to this round's index-(-k) result. NONE.

## WHAT MAIN WOULD HAVE TO VERIFY
Reproduce the Gamma_r·∂_r+M_wall normal-mode solution and its normalization integral; independently confirm the compact-spin-surface Riemann–Roch index (deg S = g−1, twisted by L⁻) for the actual genus/k used; and check the gauge-coupling-independent-of-localization argument's dependence on the assumed finite, constant gauge-zero-mode profile before treating −k as a physically realized compensating spectrum.
