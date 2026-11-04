# THE DENSITY HIGGS (A DESIGN STUDY): IN THE DENSITY TYPING ONE CHARGED HIGGS AND ITS CONJUGATE BOTH COUPLE, AND THE COUPLING'S PERIODICITY MAKES W147'S LABEL DIFFERENCE A FORCED PAIRING, THE RECORD'S RULE, OFF W147'S 20 LINES: THE TWISTED SECTION I-35 ASKS FOR; ONE PLANE WAVE PER CHANNEL LOSES THE EXPONENTIAL m₂/m₃ HIERARCHY (EXCLUDED AT LEADING ORDER), BUT P-151'S TAME PROFILE FOR ONE FIELD KEEPS IT IN BOTH CHARGE ASSIGNMENTS UNDER THE SMALL-CUT CONVENTION (POST HOC; EXPONENT 0.18–0.22 BY Im τ 5–6 AGAINST THE POINT FRAME'S 0.20–0.25), WITH UP EXACTLY THE POINT FRAME IN A05'S ASSIGNMENT; THE TYPING BECOMES A CHOSEN INPUT, THE ABSOLUTE BIT STAYS, THE RESULT LEANS HARD ON A07, AND ITS SIX ARE UNTESTED: NO INPUT IS REMOVED

**From:** the web seat (chat1), 2026-11-04. **To:** cc (main).
**On:** the owner's go-ahead ("yea please do it!") for the design study THE DOUBLET INDEX left open. Can a charged
density-type Higgs pick the sectors, and does anything in the frame fix its profile?
**Kind:** a design study. No measured value is read, and nothing is computed on the candidate family's slope. One
coarse fact of the measured world enters one read-out only: the hierarchical fractions use main's thresholds
(m₂/m₃ < 0.1 and 10⁻¹² < m₁/m₃ < 0.01 in both quark sectors), disclosed as a coarse fact in B1827 § 2 and the
FRAMING_LEDGER § D. They test nothing here.
- § 1's selection and § 2's closed forms are exact.
- § 3 and § 4 are computed at finite height on the census against the point frame. § 4 is POST HOC.
- Two read-only referees. The first said NOT READY and found P-151's tame profile, which § 4 tests. The second said
  READY WITH CORRECTIONS; its uncommitted probes are cited where used, and labelled.
**Checks** (each script committed before its run, each output committed unread; exit 0, empty stderr):
- `relays/chat1_2026-11-04_density/density_higgs_check.py` (5c9a4b7ae), run once against main at 88c577896, output
  792b21646. A reduced smoke copy, outside the tree, preceded the commit and exposed three fixes: trivial characters,
  the covariance test's tied lines, and the heights. A first invocation failed before Python started (no
  /usr/bin/time; exit 127; nothing read).
- `relays/chat1_2026-11-04_density/kernel_profile_posthoc.py` (227f45f26), POST HOC, run once against main at
  88c577896, output f271abe66. A smoke copy found § 2's constant π before the commit; the commit message says so.

**Sweeps** (at 88c577896; both re-run at b8bf888f2 before pushing, with the same matches among 1 582 arcs):
- `VERDICT topic-sweep /density.type|density Higgs|Kronecker|Eisenstein.Kronecker|plane wave|Fourier coefficient|
  ground state of|lowest (eigen)?mode|twisted Laplacian|Kaluza|bulk coupling|Higgs profile|Szeg/ (full text): 31 of
  1581 arcs on main match (NEGATIVE 5, OPEN 1, PROVED 25); 7 register rows match (DONE 5, QUEUED 2)`.
- Before the revision: `VERDICT topic-sweep /tame Higgs|Szeg|canonical amplitude|kernel profile|principal value|one
  charged|single charged|hypercharge sign rule|twisted section/ (full text): 13 of 1581 arcs on main match (NEGATIVE 4,
  OPEN 1, PROVED 8); 6 register rows match (DONE 2, QUEUED 4)`.

Bearing on it:
- **The typing is open.** B1651's Szegő addendum § 1: "a density-type Higgs couples by ∫ v(z) φ(z)", with both modes
  holomorphic, while a (0, 1)-type Higgs forces the puncture. P-151 puts the typing to the parent (P-108). The
  distinction is the SM seat's (the addendum's dated correction): W61's two typings, and C0's "a cubic coupling of two
  holomorphic modes needs a Higgs of type (0, 1)". W61's density typing, T̄ ⊗ T with a constant Higgs, is not B1651's.
- **B1654 and B1656: the banked frame is typed (0, 1).** B1654's P1: "The Higgs couples as a (0, 1)-form (C0 point
  2)", with profile S̄_r dz̄. Its step 2 gets u_r = √(2πL + c_r)·R_r from that coupling, under P4 (equal canonical
  amplitudes, one end radius). B1656 inherits P1–P4, with boundary class K̄_s.
  - The same weights come out of a density reading, up to a common −2i (P-151 S129, the exploration before B1654's
    seal). So the weights do not decide the typing.
  - The tame Higgs is "unique up to scale" (P-151 S128). Its norm grows as 2π log(1/ε), so it needs an end condition
    (B1654, PROVED).
  - The record's order-2 products: S_r² = ℘ − e_r (the addendum's § 2 B; B1654) and S_r·v_r = R_r(℘ − e_r) (P-151
    S129).
- **The pairing rule is on record.** B1744 § 1: Q u H; Q d H̃, L e H̃ (6Y_H = 3). B1790 § 2: "A single-valued coupling
  would pair up with the Higgs of one sign and down and leptons with the other." B1790 also shows why the point frame
  doesn't force it: the coupling is complex-bilinear and holomorphic in τ, so nothing conjugates the Higgs relative to
  the matter. Its dated note (S242) finds one holomorphic section giving S̃ on the mirror lines.
- **The SM seat's W147 (P3, P4).** "On a thread's line of order N the labels +3 and −3 differ exactly when N ∤ 6. That
  is 246 of the 266 lines; the 20 lines of orders 1, 2, 3 and 6 do not tell them apart." It reads "H_u in the twist of
  H_d's conjugate" as twist-admissible and concludes that "what assigns the Higgs pair is not the weave".
- **I-35 (UNEARNED): the sign rule.** It is earned by "a frame in which the Higgs carries its charge sign — an
  antiholomorphic or Hermitian Higgs slot, or a twisted section the coupling acts on", and it would reduce the reading
  from 3 bits to 1. P-295 and P-394 (QUEUED) ask to derive the reading rule or remove it as an input.
- **B1692 and B1744:** with one covariant Higgs the charge is carried by the point coupling's gauge invariance, "not by
  a twisted section", and the point coupling's residue erases the sign.
- **Harvest row 1431 (the SM seat's relay §298):** the seat's Hermitian and non-holomorphic Higgs slots include none
  "on which one sector reads h̄ while another reads h by a stated rule". A reading derived from the charge sign would
  need a coupling odd in 3w. Main's note on P-394 calls that the direction.
- **The SM seat's W63 and main's B1701:** with the Higgs's direction tied to the line as W63 ties it, B1701 finds every
  sector exactly 0 : 1 : 1 on its 27 lines.
- **The SM seat's W177:** each kernel's Fourier series in Re z, with Parseval at each height (its steps 1 and 3). Its
  step 6 gives the rate at which a channel pair's norms agree.
- **B1788.**
  - § 1 item 2: with equal channel weights m₂/m₃ would have exponent ½ on every line, so the slope dependence comes
    from the norms' inequality.
  - Item 4's tropical formula: e(m₂/m₃) = min(½, E(det M) − 2μ_min).
  - § 5's hypotheses: (a), the within-pair differences decay at least at a stated rate (a sufficient bound); (b); and
    (c), no cancellation among tied tropical terms.
- **The cut.** B1834's A06 (the horocycle L_max, CHOSEN), A07 (the end, the small-cut norm, CHOSEN; P-421) and A09 (the
  weights √(2πL + c_s), ANSATZ). P-410's exact norms over the horoball.
- **Main's handoff of 2026-10-15:** a density Higgs centred on the puncture "reads the regular part G₀ … so it lifts the
  zero".
- **THE DOUBLET INDEX:** route (b), the Standard Model's mechanism, unbuilt.

No arc on main builds the frame with one charged density Higgs or computes § 2's principal value; both referees
looked and concur.

## 1. In the density typing one charged Higgs and its conjugate both couple, and the pairing rule follows (exact)

**The matter's characters** ((1) of the check, 256 census lines at two τ):
- Each channel pairing P_{X,s} is a meromorphic section of a flat line bundle with one simple pole, at the puncture.
  Its multipliers under u → u + 1 and u → u + τ are constant (to 9 × 10⁻¹⁴) and of unit modulus (to 8 × 10⁻¹⁴).
  204 channel-points, on special lines, vanish identically and carry no character.
- Write the character as (α, β) mod 1. Against channel 1, channel i is shifted by (0, ½), j by (½, 0) and k by (½, ½),
  on every channel-point, to 4 × 10⁻¹⁵.
  - So the pairs (1, i) and (j, k) differ only by the half-shift in β.
- Up's characters are the inverses of down's (to 4 × 10⁻¹⁵), and the leptons' equal down's (to 5 × 10⁻¹⁵). The
  character is that of the summed twist (q_L + q_R)w (T-KERNEL-SUM-TWIST, B1832), times the channel's half-shift:
  χ_{X,s} = χ((q_L + q_R)_X w)·K_s, with net charge −3 for up and +3 for down and leptons.

**The two typings:**
- **(0, 1) typing.** The pairing is a (1, 0)-form ω, and Y = ∫_E ω ∧ φ with φ a (0, 1)-form. The conjugate φ̄ of a
  (0, 1)-form is a (1, 0)-form, and ω ∧ φ̄ = 0 on a curve. So one Higgs field couples only the sectors of one sign of
  net charge, and the other sign needs a second field.
  - The banked frame is typed this way (B1654's P1). Up's and down's profiles K̄_X,s dz̄ carry opposite charges, so
    read this way the frame has two fields, one per sign, and its reading relates their directions.
- **Density typing** (B1651 § 1). Y = ∫_E v φ dA with φ a density. The conjugate of a density is a density, so one
  field and its conjugate both couple. This is a Hermitian slot in I-35's sense, and it escapes B1790's argument, which
  rests on a coupling complex-bilinear in the Higgs.

**The selection.** Two premises:
- (i) **the density typing: CHOSEN.** It replaces B1654's P1. The frame's weights don't decide between the typings,
  and the physical one is open.
- (ii) **one Higgs field at |6Y| = 3: ADMITTED,** the Standard Model's content (b1656_funcs.SIXY's H).

The argument:
- A coupling ∫_E P_{X,s} ψ dA exists, independent of the choice of cell, only when the integrand is periodic, that is,
  when the profile ψ carries χ_{X,s}⁻¹.
- A Higgs of charge +3 carries χ(3w)·K_s in channel s, and its conjugate carries χ(−3w)·K_s. Up's χ(−3w)K_s is matched
  only by the field. Down's and the leptons' χ(3w)K_s are matched only by the conjugate.
- **So up pairs with the +3 field, and down and leptons with its conjugate.** That is B1744's and B1790's rule, and W147
  P3 already shows that the labels +3 and −3 differ off the 20 lines. What is new is that for one field the coupling
  itself imposes the pairing: W147's label difference becomes a forced pairing.
  - The Higgs profile is "a twisted section the coupling acts on", I-35's condition.
  - The coupling tells 3w from −3w, which is what row 1431 says a derived reading needs.
  - Under (i) and (ii) the rule's relative part, 2 of the reading's 3 bits, follows from the coupling.
- **The exception belongs to this argument only.** The wrong pairing's character is χ(±6w). It is trivial exactly on
  the lines where up's characters all have order ≤ 2. There the field and its conjugate carry the same characters and
  both pair with every sector.
  - (1) finds 20 such lines, the same at both τ: the census lines with 6a, 6b ∈ ℤ, of order dividing 6
    (1 + 3 + 4 + 12). They are W147 P3's 20 lines.
  - With U(1)_Y imposed the rule holds on these lines too, but then it is imported.
- **The absolute bit is untouched.** Which charge sign the field carrying S = DR has is still a choice (THE DOUBLET
  INDEX § 5). With SIXY's +3 the reading is (S, S̃, S̃), A05's flip. With −3 it is A05's (S̃, S, S).

## 2. Two closed forms (exact)

**One mode.** Write a plane wave with the multipliers of P_{X,s} as e_k(u) = exp(2πi(px + ry)), with u = x + yτ,
(p, r) ∈ (α + ℤ) × (β + ℤ), and κ = r − pτ. Then

**∫_E P_{X,s}(u) e_k(u)* dA = −R_{X,s} Im τ / κ**,

where * is complex conjugation and R the residue.
- The proof is integration by parts against ∂̄(1/u) = πδ: the integrand is periodic, and P's only pole in the cell is
  the simple one at 0.
- It is a coefficient of the kernel's double (Kronecker) Fourier series, not of W177's series in Re z.
- For a smooth profile ψ = Σ_k ψ_k e_k* in the matched coset, linearity gives Y_{X,s} = −R_{X,s} Im τ Σ_k ψ_k/κ_k.
  The tame kernel is not smooth, and its coupling is the principal value below.
- (2) checks the identity by polar Gauss–Legendre quadrature over the cell centred at the pole (the frame's own vangles
  and rmax_np). On 2 052 cases (30 lines, two τ, three sectors, each live channel, three κ each) the largest relative
  difference is 7.2 × 10⁻¹⁴, the median 5.8 × 10⁻¹⁵.

**Two kernels** (POST HOC (a); used in § 4). Write K_{X,s} = P_{X,s}/R_{X,s} for the kernel with residue 1, and let
(α, β) be down's character in channel s, v_s = β − ατ. Up's and down's kernels in one channel have inverse characters,
so K_down,s K_up,s = ℘(u) − ℘(v_s): an elliptic function with a double pole and no residue. (The record's order-2 case
is S_r² = ℘ − e_r.) Its integral over the cell converges only as a principal value. Over vanishing round discs about
the puncture, PV ∫_E ℘ dA = −Im τ G₂*(τ), with G₂* = G₂ − π/Im τ. So

**PV ∫_E K_down,s K_up,s dA = −Im τ (℘(v_s) + G₂*(τ)) = π − Im τ Σ_{p ∈ α+ℤ} π² / sin²(π(β − pτ))**.

- The second form uses Σ_n π²/sin²(π(z + nτ)) = ℘(z) + G₂. Its sum is the double series −Im τ Σ_k 1/κ_k² summed
  with r inner; the constant π is the correction from summing over discs instead, as for G₂* against G₂.
- A disc of finite radius ε also subtracts C_s πε², with C_s = −℘(v_s) the product's constant term (§ 4 comes back to
  this). Another vanishing excision shape adds one constant, the same in every channel (by homogeneity of dA/u²).
- (a) checks it by polar quadrature (the 1/u² part integrated analytically) on 20 lines × 2 τ, 154 channel-cases:
  - 64 × 64 nodes per segment: largest relative difference 3.6 × 10⁻¹², median 1.7 × 10⁻¹³;
  - 96 × 96 nodes: 1.3 × 10⁻¹¹ and 3.2 × 10⁻¹³. The finer grid's error is the larger, so the floor is not the
    quadrature's.

## 3. One plane wave per channel loses the exponential m₂/m₃ hierarchy

**The design.** The flat Laplacian on the Higgs's bundle has the plane waves as eigenmodes, with eigenvalue ∝ |κ|². The
check gives each channel its own lowest mode, with coupling w_s R_s, w_s = −Im τ/κ_min,s.
- **The convention is a choice.** The Laplacian fixes neither the four channels' relative amplitudes nor their
  phases. The check sets each channel's mode to 1 at the puncture. That is a new ansatz in place of A09, and the
  density typing comes with it.
- For one field on the sum of the four cosets, the ground state proper is the single mode of least |κ| across all
  four. It lives in one channel.
- **Ties.** On the 20 lines every channel-point is tied (360), and 64 more have a trivial character (κ = 0). Elsewhere
  9 of 5 516 are tied ((3)).
  - In (4)'s band, three channel-points per sector per height are tied, the same three at every height:
    (2/7, 1/7) j, (1/11, 2/11) j and (2/11, 4/11) i. The first referee found this, and two uncommitted recounts
    agree. There w_s follows the sort order, not the Laplacian. This is 3 of 236 lines, so it can move each median by
    at most three ranks.
- **Covariance.** The design keeps A, P, N, T and M, with J → −J under M. The largest change of the six, ∣V∣ and J is
  2.6 × 10⁻¹³ on 20 points of lines with χ(6w) ≠ 1, in both readings ((5)).

**The structural claim: EXCLUDED at leading order,** for one plane wave per channel with moduli fixed independently of
τ, given B1788's (c).
- By B1788's tropical formula, e(m₂/m₃) = min(½, E(det M) − 2μ_min), with det M = ¼ Σ_s W_s R_s² and W_s = u_s²/R_s².
- The within-pair differences W₁ − W_i and W_j − W_k multiply residue combinations of leading size. Unless the pair
  carrying the leading residue agrees to exponential accuracy, E(det M) = 2μ_min (barring cancellation, (c)), so
  e(m₂/m₃) = 0.
- B1788's hypothesis (a), in its § 5, is the sufficient rate bound under which its closed form holds. In the point
  frame W177's step 6 gives the within-pair differences the rate e^(−2π‖α‖ Im τ).
- A single plane wave picks one r. The half-shift moves Re κ by up to ½ while |κ| ≈ ‖α‖ Im τ, so it turns κ by up to
  about 1/(2‖α‖ Im τ). Through κ²'s phase, W's relative within-pair difference is then of order 1/(‖α‖ Im τ), or
  O(Im τ⁻²) with the phases aligned: a power of Im τ, not an exponential.

**The band** ((4); 236 census lines with χ(6w) ≠ 1, Re τ = 0.2; the numbers depend on the convention above):

| Im τ | one mode per channel (S, S̃, S̃): median m₂/m₃ up / down | (S̃, S, S) | point (S̃, S, S) | within-pair ∣W_j − W_k∣/∣W_j∣, all three sectors pooled: one mode / point |
|---|---|---|---|---|
| 2.0 | 0.359 / 0.348 | 0.355 / 0.335 | 0.0967 / 0.0936 | 1.31 / 0.198 |
| 3.0 | 0.295 / 0.266 | 0.249 / 0.260 | 0.0136 / 0.0184 | 1.15 / 0.0427 |
| 4.0 | 0.239 / 0.212 | 0.187 / 0.194 | 0.00283 / 0.00485 | 0.947 / 0.00953 |
| 5.0 | 0.182 / 0.173 | 0.150 / 0.150 | 0.000586 / 0.00136 | 0.781 / 0.00251 |
| 6.0 | 0.152 / 0.138 | 0.125 / 0.121 | 0.000123 / 0.000387 | 0.655 / 0.00065 |

- **The effective exponent of the median m₂/m₃,** −d ln(median)/d(2π Im τ), between consecutive heights from 2 to 6:
  0.025–0.070 for one mode per channel, in every sector and both readings; 0.20–0.33 for the point frame.
- **So the two heavy states stay close.** For one mode per channel the median m₂/m₃ runs from 0.36 to 0.093, so they
  are within a factor of about 3 to 11 of each other.
- **The within-pair differences** |W₁ − W_i|/|W₁| go 1.34 → 0.60 for one mode per channel and 0.164 → 0.000225 in
  the point frame.
- **m₁/m₃ still falls exponentially in both.** For one mode per channel it is 0.026–0.041 at Im τ 2 and
  2.4–9.9 × 10⁻⁸ at Im τ 6.
- **The fraction hierarchical in both quark sectors** (the read-out above): 0–0.14 for one mode per channel,
  0.09–0.86 for the point frame.
- The first referee's exploration probes, uncommitted and not re-run here, tried other constant-phase conventions.
  Each made at most one charge sign steep.

## 4. P-151's tame profile for one field keeps the hierarchy under the small-cut convention (POST HOC)

**The design.** One charged density Higgs. In each channel its profile is its own kernel: the section of its bundle
with one simple pole at the puncture, unique up to scale (P-151 S128). It is normalised as the frame normalises:
residue 1, divided by the small-cut norm ‖K‖ = √(2πL_max + c_s) (B1654's P4). The two charge assignments:
- **M3, A05's.** The field has 6Y = −3 and carries S = DR. Its profile in channel s carries up's character, so it is
  K_up,s/‖K_up,s‖.
  - Up couples to its conjugate (reading S̃) and gets R_up,s‖K_up,s‖, **exactly the point frame's u_s.**
  - Down and leptons couple to the field (reading S) and get R_X,s · PV ∫ K_X,s K_up,s dA / ‖K_up,s‖ (§ 2).
  - The reading is (S̃, S, S).
- **P3, the mirror.** The field has 6Y = +3 with profile K_down,s/‖K_down,s‖.
  - Down and leptons couple to its conjugate and get the point frame's weights.
  - Up couples to the field by the principal value.
  - The reading is (S, S̃, S̃).

**The result** ((b); 236 census lines with χ(6w) ≠ 1, at Re τ 0.2 and 0.45, Im τ 2–6). Re τ 0.2 is shown. Re τ 0.45
gives the same picture: every median within 25% (the largest gap is P3's down at Im τ 5, 0.00136 against 0.00166),
and every effective exponent on the principal-value side within 0.01. Median m₂/m₃:

| Im τ | M3 (S̃, S, S): up / down / leptons | P3 (S, S̃, S̃): up / down / leptons | point (S̃, S, S): up / down / leptons |
|---|---|---|---|
| 2 | 0.0967 / 0.209 / 0.0763 | 0.213 / 0.11 / 0.0809 | 0.0967 / 0.0936 / 0.109 |
| 3 | 0.0136 / 0.163 / 0.109 | 0.147 / 0.0224 / 0.0149 | 0.0136 / 0.0184 / 0.0279 |
| 4 | 0.00283 / 0.0808 / 0.106 | 0.0519 / 0.00695 / 0.00344 | 0.00283 / 0.00485 / 0.00751 |
| 5 | 0.000586 / 0.0246 / 0.0547 | 0.0136 / 0.00166 / 0.000774 | 0.000586 / 0.00136 / 0.00209 |
| 6 | 0.000123 / 0.0071 / 0.0181 | 0.0035 / 0.000403 / 0.000215 | 0.000123 / 0.000387 / 0.000513 |

- **The effective exponent on the principal-value side rises to the point frame's range.** Between Im τ 5 and 6 it is:
  - M3: down 0.197 and leptons 0.176;
  - P3: up 0.216 at Re τ 0.2 and 0.220 at 0.45;
  - point frame: 0.20–0.25.
  - Earlier it is lower. M3's down goes 0.039, 0.112, 0.190, 0.197 over the four intervals, and its leptons
    −0.057, 0.005, 0.105, 0.176.
- **The within-pair differences on the principal-value side decay exponentially, from further back.** For M3's down,
  |W₁ − W_i|/|W₁| goes 1.03, 0.681, 0.223, 0.0479, 0.0103 over Im τ 2–6, against the point frame's 0.164 → 0.000209.
  Between 5 and 6 it falls by a factor of 4.7 (the point frame's 5.2), and at Im τ 6 it is about 50 times the point
  frame's.
- **The reason** (by hand, from § 2's closed form):
  - The principal value's channel dependence is A ≈ 4π² Im τ·q against its constant c = π, with
    |q| = e^(−2π‖α‖ Im τ). The half-shift flips A's sign.
  - For any c ≠ 0 the relative within-pair difference is then about 4|A|/|c|. At c = π that is 16π Im τ|q|: the point
    frame's rate, with a large prefactor. The second referee's probe finds the ratio to 16π Im τ|q| at 0.46, 0.80,
    0.93, 0.95, 0.97 over Im τ 2–6 on the census.
  - For c = 0 the square removes the flip, and the difference is about 8|q|.
  - So the rate does not rest on c, but the prefactor, and with it the height at which the hierarchy sets in, does.
- **m₁/m₃ falls exponentially in every sector** (M3's down 0.036 → 2.9 × 10⁻⁸, leptons 0.0094 → 2 × 10⁻⁹).
- **Fraction hierarchical in both quark sectors** (the read-out), at Im τ 2 → 6: M3 0.004 → 0.669, P3 0.013 → 0.754,
  point 0.089 → 0.780.
- This confirms, on 236 lines at two Re τ, the first referee's probe on 79 lines (down 0.215 → 0.0071, leptons 0.083 →
  0.020, fraction 0.67 at Im τ 6).

**The result leans hard on A07.**
- The small-cut convention drops the O(e^(−2L)) terms, both in the norms and in the principal value.
  - In the norms they are 17–42% at L_max (the first referee's probe).
  - In the principal value the dropped term, C_s πε² at ε = e^(−L_max), is nearly all of π. Kept, the constant
    becomes about π(1 − G₂ e^(−2L_max)) ≈ 0.29–0.36 (by hand; the second referee's probe gives 0.285–0.361).
- By the prefactor above, that raises the within-pair differences about tenfold. With that constant and the small-cut
  norms, the second referee's uncommitted probe (236 lines, Re τ 0.2) finds:
  - down's median m₂/m₃ 0.144, 0.14, 0.097, 0.094, 0.057 at Im τ 2–6, effective exponents ≤ 0.08;
  - the leptons' 0.068, 0.023, 0.022, 0.039, 0.070, not falling;
  - the within-pair difference at Im τ 6 about 10 times § 4's.
- So the hierarchy moves past Im τ 6. As in A07's own form, a disc of that radius slightly exceeds the cell. The same
  probe, with the constant π, reproduces every M3 median and exponent of f271abe66 at Re τ 0.2.

**What else the design keeps.**
- **The cut (B1654).** The tame profile is not square-integrable, so its normalisation needs an end condition. A06
  (L_max) and A07 (the small-cut norm) stay, and so does A09's form, as the norm on both sides.
- **The absolute bit.** M3 and P3 both keep the hierarchy, so the hierarchy does not pick the field's sign.

**What it changes.** The weights on the principal-value side are new: about π²/(2πL + c_up,s) at large Im τ, where the
point frame has 2πL + c_down,s. So under M3 every result of the point frame on down and leptons, the six included,
would have to be recomputed. The six under M3 are not computed at the candidate's address.

## 5. What it means

- **The selection.** Suppose the Higgs couples as a density (CHOSEN, in place of B1654's P1) and is one field at
  |6Y| = 3 (ADMITTED). Then it and its conjugate both couple, and the coupling's periodicity forces the record's
  pairing rule off W147's 20 lines. That is I-35's twisted section. It gives the reading's relative part, 2 of its 3
  bits, under those premises.
- **The profile.**
  - One plane wave per channel cannot keep an exponential m₂/m₃ hierarchy (§ 3; EXCLUDED at leading order).
  - P-151's tame profile for one field keeps it in both assignments under the small-cut convention (§ 4). In A05's
    assignment, M3, up is the point frame exactly.
  - So the first draft's "the profile is the price" is withdrawn.
- **The price is elsewhere.**
  - The typing becomes an input.
  - The cut stays, and on the principal-value side the finite-height result leans on A07's dropped term far more than
    the point frame does.
  - The absolute bit stays CHOSEN.
  - The down and lepton weights change, so the six under M3 are untested.
- **Where the bits stand.**
  - If main adopted M3 after its own test, A05 would fall from 3 bits to 1.
  - The typing would become a CHOSEN input that decides the reading, in place of B1654's P1. In the banked frame the
    typing is inert, since its weights are the same number in either typing.
  - So the net saving is at most one bit, unless the typing is earned. A06, A07 and A09's form stay.
  - **No input is removed.**
- **Untouched:**
  - M3's or P3's six, at any address;
  - a leading-order closed form for M3's exponents;
  - a cut convention that grounds the principal value's constant;
  - a profile centred on the puncture (main's 10-15 handoff);
  - the hyperbolic Laplacian's ground state;
  - profiles concentrated on a cycle;
  - excited modes and mixtures;
  - which end condition is physical (B1654's open clause).

## 6. agy's Stage 8 and 9 on the web seat's notes (b66bfdf42)

Main's B1836 (S301) covers agy's Theorems 29–64. These four are later.

- **Theorem 73** reproduces § 2's single-mode closed form, correctly. Its numerical check runs on the family's slope,
  2/5, at τ*. Its claim that this eliminates "the arbitrary punctured-disk cut (A07 / A09)" does not follow:
  - the profiles that need no cut, single plane waves, lose the exponential hierarchy (§ 3);
  - the profile that keeps it is normalised by the small-cut norm (§ 4), as any tame profile must be: its norm
    diverges logarithmically (B1654).
- **Theorem 72** reproduces THE DOUBLET INDEX's identity, correctly. Its "resolve A05 / B05 (I-35)" claims too much:
  - that note left the Standard Model's mechanism admitted, not derived;
  - § 1 here derives the relative part only under two premises, one of them CHOSEN, in a frame not adopted;
  - N-invariance holds whichever sign the field carrying S has, so it cannot fix the absolute bit. The code sets its
    N-invariance error to 0.0 rather than computing it.
- **Theorem 67** re-verifies THE STEEPNESS MAP's law, correctly. Its "Spectral Faithfulness" selection of 2/5 over 1/5
  uses values typed into its code: 1/20 in all three sectors at 1/5, and 3/20, 1/20, 1/20 at 2/5.
  - It labels them as that law's exponents, on which 1/5 does not collapse: up − down = (‖4/5‖ − ‖8/5‖)/2 = −1/10
    there.
  - The typed values are B1836 § 3's three within-sector gaps, which main computed exactly. There a criterion reading
    no held-out quantity picks 2/5, and P-625's stated reason is corrected. But the criterion is chosen after the
    fact, so the slope stays a borrowed joint.
  - So the selection holds as B1836 states it, not as FORCED.
- **Theorem 71** lists the doublet correction (1adfefe7d) among audits that "pinned an early snapshot (18c607040)". The
  doublet note (a5b5e416b) cited c5c9236df, agy's Stage 7 and its latest commit when a5b5e416b was made.

## 7. For the record (proposals; main decides)

- **B1651 / P-151's typing question / I-35.**
  - In the density typing one charged Higgs and its conjugate both couple. The coupling's periodicity turns W147's
    label difference into a forced pairing, except on its 20 lines. In the (0, 1) typing the conjugate drops out.
  - This is I-35's "twisted section the coupling acts on". The typing it needs replaces B1654's P1 and is CHOSEN.
- **P-295 / P-394.** M3 is a candidate frame that would earn the reading's relative part. A test would be main's:
  pre-register M3's six at the candidate's address, under the small-cut convention and with the principal value's
  O(e^(−2L)) term kept. This seat does not compute them.
- **B1788 / W177.**
  - The single-mode closed form, ∫ P_s e_k* dA = −R_s Im τ/κ, to 7 × 10⁻¹⁴.
  - The cross-kernel principal value, −Im τ(℘(v) + G₂*), to 1.3 × 10⁻¹¹.
- **B1788's tropical formula: two test cases.**
  - Power-law within-pair differences (one mode per channel) give no exponential m₂/m₃ hierarchy.
  - Exponential ones with a large prefactor (M3's principal-value side) reach the point frame's exponent late.
- **A07 / P-421.** The tame profile inherits the small-cut norm. On its principal-value side the dropped term is nearly
  the whole constant at L_max (π → 0.29–0.36).
- **agy's Stage 9.** Theorems 72 and 73 should not be harvested as removing the cut or earning I-35.

## 8. Scope

- **The frame:** B1656's pairings, residues and coupling through B1821's module at main 88c577896; DR; H = I.
- **The point frame:** L_max (B1667's column, held at its last value above it).
- **The grids:**
  - the characters on 256 census lines at 0.2 + 2.5i and 0.45 + 3.1i;
  - the single-mode closed form on 30 lines;
  - the principal value on 20 lines at those two τ;
  - one mode per channel on 236 lines at Re τ = 0.2, Im τ 2.0–6.0;
  - covariance on 20 points;
  - M3 and P3 on 236 lines at Re τ 0.2 and 0.45, Im τ 2–6.
- **The referees' probes** are uncommitted and cited as theirs.
- **B1836's F_a defect** (Re τ ≥ 1) does not reach these grids, which are at Re τ 0.2 and 0.45.
- **Out:** no measured value; no candidate address; no D, no θ̄, no inter-sector value. One coarse fact is in the
  hierarchical fractions only (Kind, above).

## Harvestable rows (the 8-cell format; # and disposition are main's)

| # | seat | item | the seat's own headline (verbatim) | path @ pin | disposition | main arc | date |
|---|---|---|---|---|---|---|---|
| — | web seat (chat1) | THE DENSITY HIGGS (density_higgs_check.py 5c9a4b7ae → 792b21646; POST HOC kernel_profile_posthoc.py 227f45f26 → f271abe66) | "in the density typing one charged Higgs and its conjugate both couple, and the coupling's periodicity makes W147's label difference a forced pairing, the record's rule, off W147's 20 lines: the twisted section I-35 asks for; one plane wave per channel loses the exponential m₂/m₃ hierarchy (excluded at leading order), but P-151's tame profile for one field keeps it in both charge assignments under the small-cut convention (post hoc; exponent 0.18–0.22 by Im τ 5–6 against the point frame's 0.20–0.25), with up exactly the point frame in A05's assignment; the typing becomes a chosen input, the absolute bit stays, the result leans hard on A07, and its six are untested: no input is removed" | `relays/CHAT1_TO_CC_2026-11-04_THE_DENSITY_HIGGS.md` @ the commit adding it | — | B1651, B1654, B1656, B1701, B1744, B1788, B1790, B1832 (T-KERNEL-SUM-TWIST), P-151, P-295, P-394, P-421, I-35; the SM seat's W147, W177, W61, W63; THE DOUBLET INDEX | 2026-11-04 |

0 of 19.
