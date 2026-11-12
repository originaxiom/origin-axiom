# SM-C4 — the parameter inventory: names, kinds and what each rests on, with no value on the page

*Closes the card `relays/cards/SM_C4_parameter-inventory.md`, approved by main as proposed (M6), with M6's addition:
where the record's nineteen and the Standard Model's nineteen differ as lists, this page says so row by row. The count
it must match, `relays/sm_c4/parameter_count.json`, was committed first (a85ea5bda). The table's own checks and their
planted errors are `relays/sm_c4/inventory_checks.py`. For the record's column it opened only what M6 allows: the
total-inputs scoreboard (its .md and .json files), GENESIS, the programme, the arcs' verdict lines and this seat's own
record. It opened none of the files M6 names as not to be opened. No value is written, looked up, computed or compared.
The only figures on the page are counts.*

## 1. The Standard Model's parameters

The rows are the Standard Model's free parameters, 19 with massless neutrinos. Beside them stand the neutrino sector's
7 for Dirac masses, and 2 more for Majorana masses, 26 or 28 in all. The count is from the field content, not from
this table (§ 4).

| id | name, symbol | sector | kind | dimension | definition, with the scheme and scale a value must name | where it sits in the Lagrangian | the record's coordinate (§ 2) | what the record says about it |
|---|---|---|---|---|---|---|---|---|
| S01 | hypercharge coupling, g₁ (or g′) | gauge | gauge coupling | dimensionless | running coupling in MS-bar at a scale μ, conventionally μ = M_Z; its normalisation must be named: the plain hypercharge coupling g′, or g₁ normalised as a generator of the grand-unified group, which differ by a fixed group-theory factor | the U(1)_Y covariant derivative and kinetic term | g_1 (the list does not state the normalisation) | frame A: no frame. Frame B (the agy lane's complete picture) claims it, with the SU(5) normalisation among its borrowed joints (F6). The physical lane's row 1527 gives the leading SU(5) relation between the weak couplings at tree level; its comparison with a measured angle is CANNOT CHECK under the firewall and is made by no one. Row 1518 gives the two-loop running. Not earned |
| S02 | weak coupling, g₂ (or g) | gauge | gauge coupling | dimensionless | running coupling in MS-bar at μ, conventionally M_Z | the SU(2)_L covariant derivative and kinetic term | g_2 | as S01: no frame in A, claimed in B, rows 1518 and 1527 on its running and its tree relation; not earned |
| S03 | strong coupling, g₃ (or α_s) | gauge | gauge coupling | dimensionless | running coupling in MS-bar at μ, conventionally M_Z, with the number of active flavours named | the SU(3)_c covariant derivative and kinetic term | g_3 | frame A: no frame; frame B claims it; not earned |
| S04 | Higgs mass parameter, μ² | Higgs | Higgs-sector parameter | dimensionful (mass squared) | MS-bar at μ; equivalently, with λ, the pair m_H (pole mass) and v | the quadratic term of the Higgs potential | v, with S05 (the pair maps to the pair) | frame A: no frame. The programme allows at most one dimensionful and one dimensionless anchor, sealed in advance; v is the list's dimensionful member. Not earned |
| S05 | Higgs quartic, λ | Higgs | Higgs-sector parameter | dimensionless | MS-bar at μ; equivalently m_H/v | the quartic term of the Higgs potential | m_H, with S04 | frame A: no frame; frame B claims it. The record's frames choose a Higgs direction; it is a borrowed joint of frame A (A04, chosen). Not earned |
| S06 | strong vacuum angle, θ (physical: θ̄) | vacuum angle | strong vacuum angle | dimensionless | θ̄ = θ − arg det(Y_u Y_d): only this combination is physical; it does not run at low orders | the topological term θ G G̃ of the strong force, and the phases of the quark Yukawa matrices | theta-bar (the list names the physical combination) | frame A: graded an input. Frame B claims it, with the mirror relation that sends θ̄ to −θ̄ (T-FRAME-MIRROR, B1836) as a joint. The weave's group fixes no CP phase (GENESIS v1.32, B1611). Not earned |
| S07 | up quark mass, m_u | quark masses | fermion mass | dimensionful | running mass in MS-bar at a low scale μ_L; a ratio to another quark mass at a common scale is scheme-independent to leading order | Q̄ Y_u H̃ u: an eigenvalue of Y_u times v | m_u/m_c | frame A claims the ratio m_u/m_c at B1841's row (the node V:SIX, a level-1 READING: the quark four are not specific); 12 borrowed joints feed it, among them the scale, tree level at M_Z with no running (A12, chosen). Frame B claims it. Not earned |
| S08 | charm quark mass, m_c | quark masses | fermion mass | dimensionful | running mass in MS-bar at its own scale, m_c(m_c), or at a common μ | Q̄ Y_u H̃ u | m_c/m_t | frame A claims m_c/m_t, as S07; frame B claims it; not earned |
| S09 | top quark mass, m_t | quark masses | fermion mass | dimensionful | the pole mass or the MS-bar mass, which differ by QCD corrections; the pole mass is defined only up to an ambiguity of the order of the strong scale | Q̄ Y_u H̃ u | y_t (with v) | frame A: no frame for y_t; frame B claims it; not earned |
| S10 | down quark mass, m_d | quark masses | fermion mass | dimensionful | running mass in MS-bar at μ_L | Q̄ Y_d H d | m_d/m_s | frame A claims m_d/m_s, as S07; frame B claims it; not earned |
| S11 | strange quark mass, m_s | quark masses | fermion mass | dimensionful | running mass in MS-bar at μ_L | Q̄ Y_d H d | m_s/m_b | frame A claims m_s/m_b, as S07; frame B claims it; not earned |
| S12 | bottom quark mass, m_b | quark masses | fermion mass | dimensionful | running mass in MS-bar at its own scale, m_b(m_b), or at a common μ | Q̄ Y_d H d | m_b/m_t | frame A holds m_b/m_t out, sealed and firewalled under the owner's hold; no value of it is read here. Frame B claims it, its value sealed. Not earned |
| S13 | electron mass, m_e | lepton masses | fermion mass | dimensionful | pole mass | L̄ Y_e H e | m_e/m_μ | frame A claims m_e/m_μ at B1841's row. On its line the leptons are the down sector, Y_e proportional to the transpose of Y_d, with a lepton factor c that is fitted (A10). Frame B claims it. Not earned |
| S14 | muon mass, m_μ | lepton masses | fermion mass | dimensionful | pole mass | L̄ Y_e H e | m_μ/m_τ | frame A claims m_μ/m_τ, as S13; frame B claims it; not earned |
| S15 | tau mass, m_τ | lepton masses | fermion mass | dimensionful | pole mass | L̄ Y_e H e | m_τ/m_b | frame A holds m_τ/m_b out, sealed and firewalled; no value of it is read here. Frame B claims it, its value sealed. Not earned |
| S16 | quark mixing angle θ₁₂ (the Cabibbo angle) | quark mixing | quark mixing angle | dimensionless | an angle of the CKM matrix in the standard parametrisation, at a low scale; equivalently \|V_us\| with the other two angles; it runs only weakly | the misalignment of Y_u and Y_d under the rotations of Q, u and d | \|V_us\| | frame A: in none of its four lists (claimed, held out, graded an input, no frame); its status says the CKM four are not claimed at its row (P-555). Frame B claims it. The weave's symmetry reduces none of the 13 flavour parameters (GENESIS v1.35, B1620). Not earned |
| S17 | quark mixing angle θ₂₃ | quark mixing | quark mixing angle | dimensionless | as S16; equivalently \|V_cb\| | as S16 | \|V_cb\| | as S16 |
| S18 | quark mixing angle θ₁₃ | quark mixing | quark mixing angle | dimensionless | as S16; equivalently \|V_ub\| | as S16 | \|V_ub\| | as S16 |
| S19 | quark CP phase, δ (CKM) | quark mixing | CP phase | dimensionless | the phase of the CKM matrix in the standard parametrisation; the rephasing-invariant measure is the Jarlskog invariant J, which with the three angles fixes δ only up to δ ↔ π − δ | as S16 | J (or delta_CP): the list names two coordinates that are not equivalent | as S16. CP violation is allowed on the weave and not forced, and the weave fixes no CP phase (B1611). Not earned |
| S20 | neutrino mass m₁ | neutrino (Dirac or Majorana) | neutrino mass | dimensionful | a mass eigenvalue; the ordering of the three (normal or inverted) is a discrete choice to be named, and only two splittings and one absolute scale are separately defined | Dirac: L̄ Y_ν H̃ ν_R; Majorana: the dimension-five operator (L H)(L H) | none: the record's list has no neutrino row | GENESIS v1.33 (B1616, NEGATIVE as sealed): a Majorana mass for the triplet has no invariant in Sym² T, and the residual-vacuum reading of the neutrino masses fails on the observed oscillation splittings. That comparison is the record's own; it is not made here |
| S21 | neutrino mass m₂ | neutrino (Dirac or Majorana) | neutrino mass | dimensionful | as S20 | as S20 | none | as S20 |
| S22 | neutrino mass m₃ | neutrino (Dirac or Majorana) | neutrino mass | dimensionful | as S20 | as S20 | none | as S20 |
| S23 | lepton mixing angle θ₁₂ (PMNS) | neutrino (Dirac or Majorana) | lepton mixing angle | dimensionless | an angle of the PMNS matrix in the standard parametrisation | the misalignment of Y_e and the neutrino mass term | none | GENESIS v1.35 and v1.36 (B1620, B1625): in some frames the PMNS reduces to two parameters, of the TM1 or TM2 type, depending on the tensor and the frame; the record's falsifier P10 is registered. None of it is a derived value |
| S24 | lepton mixing angle θ₂₃ (PMNS) | neutrino (Dirac or Majorana) | lepton mixing angle | dimensionless | as S23 | as S23 | none | as S23 |
| S25 | lepton mixing angle θ₁₃ (PMNS) | neutrino (Dirac or Majorana) | lepton mixing angle | dimensionless | as S23 | as S23 | none | as S23 |
| S26 | lepton CP phase, δ (PMNS) | neutrino (Dirac or Majorana) | CP phase | dimensionless | the Dirac phase of the PMNS matrix; the same caveat on J as S19 | as S23 | none | as S23; the weave fixes no CP phase (B1611) |
| S27 | Majorana phase α₂₁ | neutrino (Majorana only) | Majorana phase | dimensionless | a phase that survives only if the neutrino masses are Majorana; it does not enter oscillations | the dimension-five operator | none | nothing on the record names it |
| S28 | Majorana phase α₃₁ | neutrino (Majorana only) | Majorana phase | dimensionless | as S27 | as S27 | none | as S27 |

## 2. The record's nineteen, row by row against the Standard Model's

The record's list is the total-inputs scoreboard's observables, rows 1 to 19, with four more beyond them. It counts
the same 19 as the Standard Model with massless neutrinos, in other coordinates.

| the record's row | the Standard Model's rows | how they map | where the lists differ |
|---|---|---|---|
| m_u/m_c, m_c/m_t, m_d/m_s, m_s/m_b, m_e/m_μ, m_μ/m_τ | S07 to S14, as ratios within each family | with m_b/m_t, m_τ/m_b and y_t, the eight ratios and one Yukawa coupling give the nine masses back; the map is invertible given v | ratios, not masses: a frame that derives the six fixes six of the nine mass degrees of freedom, not six masses |
| m_b/m_t, m_τ/m_b | S09, S12, S15 | the two links between the families | held out by frame A; the firewall applies to them |
| y_t | S09, with v | the top Yukawa coupling, which with v gives m_t | a coupling, not a mass: the scheme of y_t and of m_t must be named together |
| \|V_us\|, \|V_cb\|, \|V_ub\| | S16, S17, S18 | invertible: the three moduli give the three angles | none, once the parametrisation is named |
| J (or delta_CP) | S19 | J fixes δ only up to δ ↔ π − δ | the list names two coordinates that are not equivalent; one of them, or the rule that fixes the other, must be named |
| g_1, g_2, g_3 | S01, S02, S03 | the same | g_1's normalisation is not stated in the list |
| theta-bar | S06 | the same physical combination | none; θ itself is not physical, and the list rightly names θ̄ |
| m_H, v | S04, S05 | the pair (μ², λ) maps to the pair (m_H, v) | invertible at tree level; beyond it the map depends on the scheme. v is dimensionful and is the natural anchor; the dimensionless content of the pair is λ |
| M_Pl/v, ρ_DE/v⁴, η_B, Ω_DM/Ω_b (the four beyond the nineteen) | none | outside the Standard Model | gravity's scale, the vacuum energy, the baryon asymmetry and the dark matter: not parameters of the Standard Model's Lagrangian |
| none | S20 to S26 (Dirac), and S27, S28 (Majorana) | — | the record's list has no neutrino row; with massive neutrinos the Standard Model has 26 or 28 |

**Four consequences of the coordinates the record chose:**
- **Claims are made in ratios.** Progress on a frame should be read in the coordinates it claims.
- **The scheme and scale are part of each ratio.** Frame A's choice, tree level at M_Z with no running, is a borrowed
  joint (A12). The ratios across families (m_b/m_t, m_τ/m_b) run strongly with the scale.
- **The firewall's design depends on these coordinates.** Holding out the two links between the families, while
  claiming the ratios within them, is a test only in ratio coordinates.
- **The nineteen are dimensionless but for two.** Only v and m_H carry dimension, and v is the anchor the programme
  allows.

## 3. What the record says about the whole list

- **Earned: 0 of 19.** No value is derived and none is predicted (the scoreboard; WHERE_WE_STAND).
- **The identification price is 13:** the identifications between the record's objects and the Standard Model's
  objects that are still unearned (the scoreboard).
- **Frame A, the record's candidate:**
  - it claims 6 rows, at a level-1 reading, and holds 2 out;
  - it grades θ̄ an input and gives no frame to y_t, the three gauge couplings, m_H and v;
  - the CKM four are in none of its four lists, and only its status line says they are not claimed at its row;
  - it has 13 borrowed joints, of which 10 are chosen, 2 fitted and 1 an ansatz.
- **Frame B, the agy lane's complete picture:**
  - it claims all 23 rows, with 44 borrowed joints;
  - its own counter certifies none.
- **The weave's symmetry reduces none of the 13 flavour parameters** without a frame (GENESIS v1.35, B1620). Values
  need a forced modulus, dynamics or end data (GENESIS v1.33).

## 4. How the table was checked

- **The count:** `relays/sm_c4/parameter_count.json`, committed before the table.
  - The Yukawa matrices' moduli and phases, less the angles and phases of the flavour rotations, plus the phases left
    unbroken, give 13 flavour parameters with massless neutrinos (19 in all), 26 with Dirac masses and 28 with
    Majorana masses.
  - A planted count with one flavour rotation left out is caught.
- **The table's own checks:** `relays/sm_c4/inventory_checks.py` and its output.
  - The rows by sector and kind must equal the count.
  - No definition cell may hold a figure.
  - No parameter may stand twice.
  - Three planted errors are run on copies of this page, and each must be caught: a sector's row deleted, a figure
    written into a definition, and one parameter entered again under another name.
- **Labels (§ 12):**
  - the count: computed once; tested against a planted error;
  - the table's checks: computed once; tested against planted errors (3 planted);
  - what the record says: read from the files named, and not independently checked.

## 5. What was not done

- **No value.** No row carries a value, a range or a fit, and none was looked up.
- **The record's column is from the files M6 allows.** The framing ledger and the look ledger were not opened, so the
  framing ledger's test commitments are not in this table. WP-4.4's bar, null and look count stay main's and the
  owner's.
- **The physical lane's rows 1518 and 1527** are cited as this seat verified them in SM-C2. Their comparison with
  measurement is made by no one.
- **Beyond the nineteen:** the four rows the record lists outside the Standard Model are named, not inventoried.
- **A fix to this seat's own check before its in-tree run.** The figure check first counted a reference to another
  row ("as S16") as a figure, and the control failed. It now removes row ids first. The control passes, and each
  plant is still caught, each by the check meant for it.

0 of 19.
