# A2: the frame's construction, an inventory of framing commitments

Reader A2. Scope: every choice in how FR-FIB's 3x3 Yukawa matrices are built (fields, twists, generation blocks,
channel weights, radii, Higgs directions, readings, normalisations, comparison conventions).

Sources read: FINDINGS.md of B1642, B1644 (plus its PREREGISTRATION derivation), B1649, B1653, B1656, B1659, B1667, B1691,
B1692, B1693, B1694, B1695, B1716, B1726, B1739, B1740, B1742, B1788, B1789, B1801, B1810, B1817, B1821, B1822, B1824,
B1826; B1790 and B1724 (read for the reading rule); POINT_REGISTER rows P-555, P-562 to P-564. Code read in full:
`b1656_funcs.py` (in B1691's `verification/correction/`, cited as F:line) and `cm_zero_line.py` (B1821, cited as Z:line);
`the_exponents.py` (B1691, cited as X) read for the Higgs sections. No measured-data file was opened; nothing was run.

Conventions of this file. "Status as the record states it": FORCED (with proof ref), CHOSEN, READING, or UNSTATED
(never recorded as a choice in the arc that makes it; a later arc may have named it, said in the note). Quotes are
verbatim and short. Entries are listed by theme, not by importance; the closing list ranks five. Nothing here judges
whether a commitment is derivable.

Entries marked (+) are ones I judge the record does not state as a choice at the point where the code makes it.

---

## A. Fields, representations, what is twisted

### C-01 The generations are three quaternion images of ONE doublet value (+ partly stated)
- commitment: each field has a single fibre zero mode, a doublet F_x, and its three generations are F_x multiplied by the three constant blocks C_p, so every Yukawa entry is a bilinear in the same two doublets.
- type: REPRESENTATION / CONSTRUCTION
- status: CHOSEN in B1644 ("blocks' labels"), later PROVED to force rank <= 2 (B1653), then recorded as a premise in B1789.
- where: F:21 `BLOCKS = [QJ, QI, QK]  # the generations' blocks (B1644)`; B1653 FINDINGS 3 "three generations are three quaternionic images C_p F of one doublet value"; B1789 2(b) "one zero mode per field and generation block".
- excludes: three independent zero modes per field (an h1 of rank 3, cf. the older B632 "h^1(M;27)=3"); generation blocks that are not units of the quaternion algebra; a generation index carried by distinct line bundles.
- alternatives on record: B1653 U6 and its next-step (a coupling with a profile, two points) lifts the zero; B1801/P-564 (agy lane) sketches the three sheets of a 3-fold cover as generations, "not a frame with outputs".
- consequence: rank of the coupling <= 2 at a point and the massless first generation, V = 1 + U(2) (B1653); at the canonical end the lift is 1/L-suppressed (B1716, B1716 Z1-Z2).
- note: the choice of WHICH three units (j, i, k, not 1) is the blocks; the identity block is excluded so the generation space is the imaginary quaternions (the multiplicity space M, B1644).

### C-02 The weak doublet is the fibre's SU(2)/Q8 doublet; the frame carries no electroweak doublet index (+)
- commitment: the matter doublet F_x is the fibre bundle's rank-2 flat bundle with quaternion (Q8) monodromy, paired by the invariant epsilon; no SM SU(2)_L doublet index exists in the frame.
- type: REPRESENTATION
- status: UNSTATED as a choice in the construction arcs; B1790 states the consequence ("the frame carries no electroweak doublet index (P-365)"); B1667 and B1649 scope it to "the fibre frame".
- where: B1822 1 "flat degree-0 rank-2 bundle with a branch point at the puncture. Its monodromy is quaternion-type (Q8)"; B1790 1 "No doublet index"; B1649 sharpening "in the surface frame the null vector is not present".
- excludes: a genuine SU(2)_L doublet with up/down components in a Higgs doublet; a Higgs doublet (B1644 prereg: "A doublet Higgs with two doublet fermions cannot couple").
- alternatives on record: the surface frame (W72, rank 3 overlap; B1653 S3 scoped); the E8 frame ("the Higgs is a flavon", B1649); the thread frame (B1653 dated correction).
- consequence: the SM's "H-tilde for up, H for down" must be imported by hand as the reading (C-14); B1790.
- note: B1667: "that the fibre frame is nature's (B1652)" is not shown.

### C-03 Hypercharge enters the matter ONLY as a flat twist q*w (periodic), nothing else (+ partly stated)
- commitment: the only trace of the charges 6Y (Q 1, u -4, d 2, L -3, e 6) is the flat-line twist (a, b) = (q p1, -2q p2) of each field's theta characteristic; there is no curvature, flux, or non-flat charge dependence.
- type: CONSTRUCTION
- status: CHOSEN (inherited from W59/B1653); B1789 proves the consequence; B1817 tests it.
- where: F:22 `SIXY = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6, "H": 3}`; F:41-43 `twist_of`, `line_w`, `sector_twists`; B1789 2(a) "hypercharge enters only through the flat twists (qα, 2qb), that is, periodically".
- excludes: a net hypercharge flux on the fibre (B1789 2(b): EXCLUDED, "|1 + q n| = 1 for q = 1 and q = 2 forces n = 0"); local curvature of zero net degree (B1789 2(d), not examined; the "route left"); a 24-type vev proportional to Y; any B-L or Pati-Salam structure.
- alternatives on record: B1789 (a)-(d); B1817 (anomaly-fixed charges at N_c = 2, 4, 5; integer 4 or 1/4 recurs); B1793 (zero-net curvature cannot supply c); the agy "Z3 Wilson line" (P-564).
- consequence: the lepton/down relation is slope-controlled and the factor 3 is an input (B1789 NEGATIVE for "c is forced by the frame as built"); on slope 2/5 the leptons equal the down quarks (B1742, B1728).
- note: only the twist ratios q_L, q_R enter the theta characteristics, so the SM's integer-charge pattern is seen only mod the line's order N (B1726 posthoc: "the frame sees 6Y mod N").

### C-04 The Higgs is UNTWISTED in its internal direction; its charge is carried only by gauge invariance of a point coupling (+)
- commitment: the Higgs's internal direction S is a modular form of tau alone (theta functions at argument 0, no line), although the Higgs carries 6Y = 3; its charge appears only through the matter twists summing to +-3w.
- type: CONSTRUCTION / REPRESENTATION
- status: UNSTATED when built (B1692 states it as a limitation: "the twisted Higgs (the Higgs's own charge on the line is carried, as in B1653, by the point coupling's gauge invariance, not by a twisted section)"); named and queued as P-562 on 2026-11-03.
- where: Z:42-46 `direction()` (R, DR, a0, F_a evaluated at theta_2,3,4(0, q) only); X (Higgs sections as q-series, no line); B1744 as cited in B1790 1: "the Higgs at its own hypercharge twist ±3w fails inside the point coupling. The residue quaternion is even".
- excludes: a Higgs section carrying the twist 3w (theta_1-type at the twist); a nonzero identity component of S that follows from such a twist (P-562); a Higgs in a non-trivial flat bundle.
- alternatives on record: B1744 (Higgs at its own twist, NEGATIVE inside the point coupling, as cited); P-562 (open, QUEUED).
- consequence: with C-05 and the null cone (B1739), both quark sectors' lightest states lock to one direction and the CKM corners invert (B1739; B1826 item 3).
- note: P-562 text: "FR-FIB's Higgs directions are modular forms of tau alone, with no identity channel, while the Higgs carries 6Y = 3".

### C-05 The Higgs's internal 2x2 orientation S has NO identity component; it is built from i, j, k only (+)
- commitment: S = a_i QI + a_j QJ + a_k QK, a vector in the adjoint (imaginary quaternions), while the matter carries all four channels (1, i, j, k) including an identity residue R_1.
- type: REPRESENTATION / CONSTRUCTION
- status: CHOSEN in B1644 (the "adjoint" Higgs, motivated by single-valuedness); the exclusion of the identity is stated as a derivation step, but the consequence for the sectors is first named in B1739/B1826.
- where: Z:70 `Sm = a[0] * B.QI + a[1] * B.QJ + a[2] * B.QK`; F:20 `UNITS` includes "1" for the matter; B1644 prereg 1: "scalar Higgs can (B1642: ε-type, antisymmetric), and so can a triplet (adjoint) Higgs"; B1649 K1 tests S = s0*1 + a.(i,j,k) at the residue only.
- excludes: a singlet (identity) channel in S; a scalar Higgs (B1642, antisymmetric, spectrum (1,1,0)); a general S in span(1,i,j,k) at the frame's census.
- alternatives on record: B1642 (scalar/identity: Y antisymmetric, masses (1,1,0)); B1649 K1 and B1659 (S in M2(C) in identities); P-562 (a singlet channel from a twisted Higgs).
- consequence: B1739 "Each sector's lightest state sits on h-bar (reading S) or h (reading S-tilde)", |V_ud| ~ r^1/2, r = |h.h|/|h|^2 ~ e^{-pi Im tau}; B1826 item 3 (corner inversion, |V_ub|/|V_td| = 11.3); P-555.
- note: the example the task supplies; it also fixes u_1 = R_1 drops out of the lift only through D (B1716).

### C-06 One Higgs direction `a` shared by the three sectors, with only the reading differing (+ partly stated)
- commitment: in the census a single Higgs vector a (of the 13 directions) is used for up, down and leptons; sectors differ only through their twists and their S vs S-tilde reading.
- type: SHARED-MODULUS / CONSTRUCTION
- status: CHOSEN ("one Higgs for the three sectors", B1692 setting); relaxed in B1742 (H_u != H_d) and B1693 (two Higgs).
- where: Z:62-71 (`a = direction(d, tau)` outside the sector loop; `Sm` built per sector from the same `a`); B1692 "one Higgs for the three sectors"; B1693 "The up quarks need a Higgs of their own — the pattern of a two-Higgs completion".
- excludes: separate Higgs directions per sector (two-Higgs); direction different between up and down.
- alternatives on record: B1742 (H_u = F6, H_d = F22, chi2_six 1.188, "a READING, not a derivation"; the pair chosen by the data); B1740 (F_-2 in every sector).
- consequence: B1693 T1 excludes one Higgs at the point-coupling level but B1695 and B1693's correction say at the canonical end one Higgs is not excluded; the two-Higgs pair is data-chosen (B1742).
- note: B1742 shows `D = 9` follows on (2/5,k/10) lines for H_d = F22.

### C-07 Neutrinos, Majorana terms and the Higgs's own sector are outside the frame
- commitment: only the charged-fermion Yukawas (up, down, charged lepton) are built; the neutrino sector, Majorana masses and mixing PMNS are not part of the coupling.
- type: SCOPE-CUTOFF
- status: CHOSEN (stated in B1656 "What it does not show").
- where: F:23 `SECTORS = {"up", "down", "lep"}`; Z:38; B1656 3 "the neutrinos (a Dirac pairing L–ν^c has δ = −3w and is lifted, D = 2.90, the reviewer's unsealed computation, not a cell)".
- excludes: L-nu^c Dirac pairing; seesaw; PMNS.
- alternatives on record: B1656's unsealed reviewer computation; B1826 declines the agy lane's PMNS ("read from a basis-dependent overlap") and neutrino masses ("a mislabelled η⁶, factor 5.24").
- consequence: none recorded in the frame's results; the "0 of 19" scorecard counts only the charged-fermion parameters in scope.
- note: B1656 also: "the interacting weave (one fibre at ω, the field held fixed)" is outside.

### C-08 The theory is read at tree level / one frozen fibre; the weave's dynamics and gauge dynamics are absent
- commitment: the Yukawa matrices are the leading-order (tree) point/residue coupling on one fibre at a fixed tau, with no loops, running, or interacting weave.
- type: SCOPE-CUTOFF / INTERPRETIVE
- status: CHOSEN (disclosed repeatedly).
- where: B1659 3 "The interacting weave. This is one τ, a frozen piece"; B1656 3; B1693 "the 10% allowance's adequacy for the running between the fibre's scale and M_Z is not shown".
- excludes: running to a common scale; loop corrections; the weave's tau dynamics; a tau determined by a potential.
- alternatives on record: B1686/W62 (tau runs to a cusp under the potential; cited in B1691); B1637 (modular fits need 21+ parameters).
- consequence: the comparison uses "running masses at M_Z" with a 10% allowance in quadrature (B1693, B1695, B1726); the allowance's adequacy is "not shown".
- note: see C-34 for the comparison convention.

---

## B. The shared modulus and the line

### C-09 One tau for all three sectors (+ in code; stated as the d-e/B1693 wall)
- commitment: a single modulus tau (one fibre) serves the up, down and lepton sectors and the Higgs.
- type: SHARED-MODULUS
- status: CHOSEN (named as an obstruction in B1693/B1694: "one fibre has one τ").
- where: Z:54-64 (`tau` argument to `rows_at` shared across `SECTORS`); B1694 "Each sector sits at the τ where the curve meets its own m₂/m₃ ... one fibre has one τ, so the three sectors as computed here cannot share a fibre without a line or further Higgs fields (B1693)".
- excludes: a different tau per sector (B1694's sector-wise curve, up Im tau ~ 3.1, down ~ 2.5, leptons ~ 2.1); a sector-dependent point of the moduli space.
- alternatives on record: B1694 (each sector at its own tau; no curve passes all three); B1695 (one line, one tau, six ratios from two continuous numbers, chi2 minimum 61.3); P-555 (two addresses, firewalled).
- consequence: B1694 "the down quarks and the leptons miss in opposite directions"; B1825 (least chi2_ten 291 against 23) "never together" at one address; P-555 budget "a free second address ... leaves C_ten <= 0.36 — dead".
- note: B1821 mirror (-conj tau, (alpha,-b)) is a symmetry, not a second address (P-555 S288 closed for the CKM).

### C-10 One flat line w = alpha*tau - b shared by all fields; charges multiply it
- commitment: a single torsion line w (a point of the Jacobian, one complex parameter) twists every field by (its 6Y charge) x w; there is no separate line per sector, and the Higgs/matter share it.
- type: SHARED-MODULUS / CONSTRUCTION
- status: CHOSEN; B1692 (title "a twisted line per sector") varies the tested lines but each field sees the same w times its charge.
- where: F:42 `def line_w(p1, p2, t): return p1*t - p2  # W59's holonomy phases (B1653)`; F:43 `sector_twists`; Z:58 `w = B.line_w(line[0], line[1], tau); x, yy = B.sector_twists(w, tau, ql, qr)`.
- excludes: independent lines per sector or per field; non-torsion (continuous) lines in the census; lines not of the form alpha*tau - b with rational alpha, b (e.g. generic complex w).
- alternatives on record: the zero line (Z docstring: "(no Wilson line: the parameter-free choice)"); B1692 / B1695 (alpha = j/96, j <= 48; beta = 0 only); B1713's 266 lines of order 1-12; W59's 18 lines at omega (B1653, B1656); W60's half-period line (B1686).
- consequence: B1692: spread of m2/m3 across sectors at most 4 (point coupling); B1695 "wrong sector assignments fit as well"; the lepton/down relation by line order (B1728, B1742).
- note: the line family is (real) 2-parameter (alpha, b); the sectors' twists are integer multiples, hence only line order mod charges matters (C-03).

### C-11 The lines are torsion points of order N <= 12 (266 lines), alpha in [0, 1/2], Re tau in [0, 1/2]
- commitment: the census ranges over 266 torsion lines of order 1-12 (plus mirrors) and a bounded tau strip.
- type: SCOPE-CUTOFF
- status: CHOSEN (stated as the census's range; "NOT FOUND within the reach; nothing excluded beyond it", sealed B1825 summary).
- where: B1726 1 "B1713's 266 lines of order 1–12, at Re τ ∈ {0.05..0.85} and Im τ 2.05–3.45"; B1821 2 "Re τ ∈ [0, ½] suffices"; B1817 "every α = j/N with N ≤ 30".
- excludes: lines of order > 12; non-torsion lines; Re tau outside the strip; Im tau outside 1-4 (L clamped at Im tau = 4, B1788 5).
- alternatives on record: B1785/B1786 (orders up to 30; other windows); B1817 N <= 30; B1788 closed form at leading order in Im tau for all alpha.
- consequence: the sealed B1825 bound is a "reach" bound; the "orders 5 and 10" band of the six (B1726 posthoc B; B1728).
- note: B1716 correction records a second exact-zero family on Re tau = 0 that the order-4 law does not name.

### C-12 The mirror symmetry is exact, so the census halves; J's sign is never predicted
- commitment: outputs at (-conj tau, (alpha, -b)) equal those at (tau, (alpha, b)) row by row with J -> -J, and the census scores only |J|.
- type: CONVENTION / CONSTRUCTION
- status: FORCED (B1790 found the map; B1821 confirms numerically; "a proof sketch is owed").
- where: B1821 1 "log10 outputs agree to 5.8e-07 ... J (with its sign flipped) to a relative 5.6e-08"; B1821 2 "J's sign is not predicted".
- excludes: a frame in which the sign of CP violation is a prediction.
- alternatives on record: none found (a symmetry, not a choice); P-555 mirror rule (down at -conj tau) tested and closed for the CKM.
- consequence: the card scores |J| only; "a world and its mirror image cost the same address".
- note: S-tilde is S at -conj tau with K negated (B1790).

---

## C. The channel weights, radii, and regularisation

### C-13 The coupling is a regularised L^2 overlap whose four residue channels are weighted by sqrt(2 pi L + c_s), c_s the regularised norm (+ partly stated)
- commitment: each of the four residue channels (1, i, j, k) of the rank-one pole is weighted by sqrt(2 pi L + c_s) (c_s: the finite part of the channel norm after removing 2 pi log(1/eps)), instead of equal weights.
- type: CONSTRUCTION / NORMALISATION
- status: CHOSEN in B1653/B1654 ("the end condition"); B1654 "the norm of the boundary class" derives it from the L^2 norm of the pole; the choice of L^2 (flat) norm is B1654/B1822.
- where: Z:72 `u = {k: (math.sqrt(2 * math.pi * L + c[k]) * R[k] if c[k] is not None and 2 * math.pi * L + c[k] > 0 else 0) ...}`; F:55-67 `cA` (`eps=1e-5`, subtracts `2*np.pi*math.log(1/eps)` and adds `scale**2*np.pi*eps**2*abs(A0[s])**2`); F:125 `weighted_M(u)`; B1788 1.2: "With equal channel weights √(2πL + c_s): M would be rank one, Y = Aᵀ(εS)B rank ≤ 2 and m₁ = 0".
- excludes: equal channel weights (the large-L limit, B1646/B1654); a different norm (hyperbolic or magnetised-torus norm); channels weighted by something other than the matter's regularised norm.
- alternatives on record: the large-L point coupling (B1653-B1654, B1646, B1691: exponents 1/2 etc.); the exact horoball norm (see C-15, S238 retraction).
- consequence: B1716 det M = 1/4 sum c_s R_s^2, "independent of L"; the first generation's lift is 1/L (B1716) and the whole slope-dependence of exponents "comes from the inequality of the channel norms c_s" (B1788 1.2); B1826 item 1 (c_s sector-blind).
- note: u_s = 0 when 2 pi L + c_s <= 0 (clipped; "nothing is clipped" on the grids, B1716 correction 3; but "the 1-channel's weight 2πL + c₁ vanishes at L ≈ 0.617", B1810 2.3).

### C-14 The regularisation is a single end radius L (a cut at eps = e^{-L}) shared by all four channels, all sectors, all lines
- commitment: one cut L = L_h(tau), the same for every channel, every sector and every line (line-independent by construction), set by tau alone through B1667's canonical horocycle.
- type: CONSTRUCTION / SHARED-MODULUS
- status: FORCED "given the canonical construction" (B1810 card: "line-independent by construction"); the choice of a canonical horocycle is CHOSEN (C-15).
- where: Z:51 `radii(tau)` returns (L_max, L_2) for the tau only; B1810 frame card "end radius L = L_h(τ), B1667 (line-independent by construction) FORCED (canonical construction)"; B1667 2: "fix ε as a function of τ alone".
- excludes: a per-sector or per-line L; L as a free number (B1654 "a regulator"); different L for the Higgs and the matter.
- alternatives on record: B1654 (L free; hierarchy needs "L in the hundreds"); B1660 (fitted L: NEGATIVE, chi2 34.4); S201 (a per-sector horocycle moves the leptons the wrong way, quoted in B1789).
- consequence: "the end supplies no hierarchy" (B1667: L_max in [0.643, 0.691], L_2 in [2.292, 2.777]); the hierarchy is "a statement about τ" and fixed Im tau; B1826 "channel norms are sector-blind".
- note: L is "clamped beyond B1667's column" (B1788 5, B1817) at Im tau = 4.

### C-15 The canonical end is a discrete choice between two horocycles, L_max (maximal embedded) or L_2 (length 2)
- commitment: the end datum is one of two canonical horocycles of the punctured fibre's hyperbolic metric; the census ranges over both, scored as a discrete choice.
- type: CONSTRUCTION / CONVENTION
- status: CHOSEN ("What remains is a discrete choice between canonical horocycles", B1667 2; "horocycle h: max, 2 — CHOSEN", B1810 card).
- where: B1667 2 "which canonical horocycle, if either, is the physical end" not shown; Z:63 `for Ln, L in (("L_max", Lmax), ("L_2", L2))`.
- excludes: other canonical cuts (e.g. a different horocycle length, an injectivity radius, a geodesic-distance cut); the flat-metric cut that B1654 used.
- alternatives on record: B1654 free L; B1726 dated note S238: "This arc's L_max is the small-cut norm 2πL + c_s evaluated at L = L_max(Im τ) ..., not the maximal horoball's exact norm. At L_max the exact twisted norms lie 35–38% below it, and with them the six fail near the four families' rows" (P-421; RETRACTIONS).
- consequence: in the S238 note the six fail with the exact end; radii between the two choices change which rows are best (B1726 best rows alternate L_max / L_2).
- note: the maximum cusp area runs 4.21-5.95 (B1667).

### C-16 The radius is a hyperbolic horocycle but the coupling's norm and cut live in the flat coordinate z (mixed metric) (+)
- commitment: the end radius comes from the hyperbolic metric that uniformises the punctured fibre, while the norm c_s and the cut eps are computed in the flat coordinate z on the torus; the two are tied only by the identification L = log(1/eps).
- type: INTERPRETIVE / CONSTRUCTION
- status: UNSTATED as a choice (B1667 §2 notes "That is true in the flat metric. In the hyperbolic metric ... the puncture is a cusp with canonical neighbourhoods"; the identification of the two cuts is not listed as a commitment).
- where: B1667 2 (the paragraph on B1654's regulator); F:55-67 (`cA` integrates over `rmax_np` parallelogram in the flat coordinate with `eps` a flat disc).
- excludes: a norm taken in the hyperbolic metric; a horoball-shaped cut region in the integral (the S238 note, C-15, shows the horoball and the flat disc differ by 35-38% in c_s).
- alternatives on record: S238 (the web seat's THE EXACT END, reproduced on main).
- consequence: "the six fail near the four families' rows" under the exact end.
- note: separate from C-15's choice of WHICH horocycle: this is the choice of what region is cut.

### C-17 The L^2 integration region is the fundamental parallelogram around the puncture with its centrally symmetric structure
- commitment: the channel norms integrate over the torus's fundamental cell centred at the puncture (`rmax_np` polar quadrature to the cell boundary), minus the eps-disc.
- type: CONSTRUCTION
- status: UNSTATED (assumed by the code; B1716 correction uses "the parallelogram and the ε-disc are centrally symmetric" as a premise of a proof).
- where: F:46-49 `rmax_np`, `vangles`; F:55 `cA`; B1716 correction 2: "since the parallelogram and the ε-disc are centrally symmetric and a0 ↦ −a0".
- excludes: a different fundamental domain (the norm is periodic, so only the puncture-centred cell is natural; the horoball region is not the cell).
- alternatives on record: none found (the 4-fold cover test in B1822 uses doubly periodic |F|^2).
- consequence: B1716's cancellation law (pairing of channels with equal c_s) uses this symmetry.
- note: B1822 1: "∣F_x∣² is doubly periodic, so the physical L² metric is the flat one".

---

## D. Kinetic normalisation and generations

### C-18 The generation kinetic metric is H = I (T-NORM), a CHOSEN input; the flat structure leaves 8 real parameters per field
- commitment: the census reads singular values of Y directly, which is physical only if the generations' kinetic metric H is proportional to the identity.
- type: NORMALISATION / CONVENTION
- status: CHOSEN (B1822: "H = I is a CHOSEN input, counted on the card"; earlier argued FORCED at B1654 §1.11, now graded "proves at best a diagonal H").
- where: Z:73-74 `Y = B.coupling(...)`; `np.linalg.svd(Y)` (plain SVD); B1822 3 "G = H·‖F_x‖² ... T-NORM holds if and only if H ∝ I."; the typing table (9, 3, 3, 2, 1, 1, 1 real parameters).
- excludes: any H not proportional to I (a diagonal H with three free scales, democratic mixing, 8 real parameters per field).
- alternatives on record: B1822's own computations ("a 10% weight on one mode moves the mass ratios by 0.007 decades; a democratic mixing of 0.1 moves them by 0.045 decades and the CKM moduli by 0.08"); P-564 (the 3-fold cover's 2-dim commutant H = aI + bJ).
- consequence: "the outputs move with H"; H = I is forced only by three one-dimensional typings, "none ... derived on the record" (B1822 3).
- note: the null worlds share it, "so it cancels in p2 and p_K but not in the framework's length" (B1822 4).

### C-19 Generations are ordered by singular value; the CKM uses left singular vectors of the SAME doublet field Q
- commitment: generation k of a sector is its k-th singular value (ascending), and V = U_up^dagger U_down from the left (doublet) singular vectors, with the physical gauge-eigenstate basis being the block basis of Q.
- type: CONVENTION
- status: UNSTATED as a choice (standard for SM Yukawas; B1653: "Up and down share Q, so V = 1 ⊕ U(2) for every line").
- where: Z:74 `u_, s, _ = np.linalg.svd(Y); o = np.argsort(s); s = s[o]; U[sn] = u_[:, o]`; Z:77 `Vm = U["up"].conj().T @ U["down"]`; Z:76 degeneracy flag `1e-8`.
- excludes: a different identification of the up and down generation bases (e.g. via right singular vectors, or via a block-labelled basis rather than mass order); a CKM defined from a common block basis.
- alternatives on record: none found.
- consequence: the corner inversion appears in |V| (B1826); where a sector is degenerate to 1e-8, V is "undefined" (B1810 card).
- note: Q is the SAME field in up and down, so the left doublets are common by construction; this is the SM's own structure and is not a free choice, but the choice that Q's three generation blocks are the C_p (C-01) fixes the basis.

### C-20 One Higgs normalisation: only ratios m1/m3, m2/m3 and |V|, J are produced; each sector's absolute scale is free
- commitment: the frame outputs mass ratios within each sector, the CKM and J; there is no absolute Yukawa or vacuum expectation value, so each sector's overall scale (and tan beta, the top/bottom/tau scale ratios) is not constrained.
- type: SCOPE-CUTOFF / NORMALISATION
- status: CHOSEN (the card's "outputs" row: "per sector (m₁/m₃, m₂/m₃); the full 3×3 ∣V∣; J").
- where: B1810 frame card "outputs"; Z:75 `row[sn] = [float(s[0] / s[2]), float(s[1] / s[2])]`; B1693 "A test of a structure, not a value derived."
- excludes: absolute masses (m_t, m_b, m_tau, the b/tau ratio), y_t at a scale, tan beta.
- alternatives on record: none found (six ratios plus mixing is the scorecard).
- consequence: the 19-parameter count "0 of 19" can claim at most 10 ratios (six + four) from the frame; the other scale parameters are outside by construction.
- note: B1659 geometric-mass law and B1716 identities are statements about ratios only.

---

## E. The Higgs directions (the 13/12 menu)

### C-21 H-cov: the Higgs direction is a covariant section (a vector-valued modular form of the matter's representation rho_R), a tagged hypothesis, "not derived"
- commitment: the direction a in the multiplicity space is a vector-valued modular form for the SAME representation as the matter's residue triplet R.
- type: CONSTRUCTION / INTERPRETIVE
- status: CHOSEN (tagged "H-cov ... a dictionary choice, not derived", B1691; P-115 open).
- where: B1691 "The tagged hypothesis (H-cov). The Higgs's direction a in M is a covariant section ... H-cov is a dictionary choice, not derived"; B1700 scope note "∂R's end data are FK10's tagged unit".
- excludes: non-covariant (constant) directions (B1646's constant directions give no hierarchy); a section of a different representation; non-holomorphic or non-modular directions; a direction fixed by a potential.
- alternatives on record: B1646 constant directions (control: "no hierarchy"); B1691's table; B1740's F_-2 is outside H-cov's proofs ("The F_a lie outside H-cov's proofs (B1730; the census referee)", B1810 scope).
- consequence: B1691 "reduction to exponents and one scale, not a derivation of a number"; the section's free coefficients leave "no inequality" (B1691 addendum S160).
- note: B1810 card lists the directions as "ADMITTED: an infinite family".

### C-22 The 13 (now 12 distinct) Higgs directions: DR, a0, R, t = -5/288, and F_a for a in {-10, -6, -2, 6, 10, 14, 18, 22, 26}; "n = 1" end data (+ partly stated)
- commitment: the census menu is B1809's Table T (DR, a0, R, t) plus B1730's zero-free F_a at n = 1 for ten values of a (written 2 = R); a0 = eta^4 F_-2/6 identically, so 12 are distinct.
- type: CONSTRUCTION / SCOPE-CUTOFF
- status: CHOSEN ("ADMITTED: an infinite family; n = 2 adds a from −22 to 50, not tabulated", B1810 card); "F₆ and F₂₂ entered the record through B1742's data-informed fit" (B1810 5).
- where: Z:37 `DIRS = ["DR", "a0", "R", "t=-5/288"] + ["F_%d" % a for a in (-10, -6, -2, 6, 10, 14, 18, 22, 26)]`; Z:31-32 (the Q dict); Z:44-46 `eps = 1j ** ((a_ + 2) // 2)`; B1824 title "TWO OF B1810'S THIRTEEN DECLARED HIGGS DIRECTIONS ARE ONE".
- excludes: F_a with n >= 2 (a from -22 to 50); any section not in the module generated by R, DR, D^2R with end data on v_+ one unit; the weight-7/2 section with t other than the listed ones (the module is a 3-dim family at weight 3/2/ (B1700: three-dimensional space (W46's three))).
- alternatives on record: B1697 (the Higgs without end data unique at weight 7/2: a0 = D^2R - E4 R/48, no hierarchy); B1700 (∂R unique holomorphic off v_+); B1730 (F_a family, zero-free); B1731; B1742 (F6, F22 pair); B1740 (F_-2).
- consequence: "'parameter-free' needs a qualifier. The directions are an infinite discrete family ... the outputs are a comb indexed by it" (B1810 3); B1824 changes the look-elsewhere count.
- note: the phase eps = i^((a+2)/2) for F_a (Z:44) is a convention that does not enter singular values (overall phase of S) but a different convention gives a "tau-dependent scalar" (B1824 3).

### C-23 The Higgs carries end data of one unit on v_+ (FK10's tagged unit), picking out ∂R among covariant sections
- commitment: the hierarchy-bearing Higgs is the section carrying one unit of end data on v_+; "the Higgs without end data" gives no hierarchy.
- type: CONSTRUCTION / INTERPRETIVE
- status: CHOSEN (tagged; B1700 "∂R's end data are FK10's tagged unit (W46's), not a second datum"; B1697 scope note).
- where: B1697/B1700 scope notes appended to B1691, B1694, B1695: "this arc's hierarchy rests on the Higgs carrying end data on v₊, a datum of FK10's kind (P-245)"; "So this arc holds given Λ, the unit and H-cov in R's own module."
- excludes: the Higgs without end data (a0 = D^2R − E4R/48 → m2/m3 → 1/2, no hierarchy); end data of 0 or >= 2 units except through the n = 1/2 F_a menu.
- alternatives on record: B1697 a0; B1730 F_a family with n = 2.
- consequence: hierarchy exists only with the unit; "the weight-3/2 Higgs directions form a three-dimensional space ..., ∂R is its only member holomorphic off v₊ and the only one giving a hierarchy" (B1700 via B1691).
- note: see C-24 for the tag Lambda.

### C-24 Lambda, the cusp unit: a tagged postulate in the frame (inherited)
- commitment: the coupling's cusp unit (the tagged postulate "Λ") is assumed throughout.
- type: INTERPRETIVE
- status: CHOSEN ("tagged postulate"; B1691 and several arcs: "given Λ, the unit and H-cov").
- where: B1692 "In the fibre frame, given Λ and one covariant Higgs"; B1693 "In this frame (Λ; B1653's residue coupling and charges)"; B1700 note.
- excludes: frames without the cusp unit; frames where the unit differs (W46's index +-3 on 4D).
- alternatives on record: memory index: "Cusp unit = tagged postulate (owner 2026-10-09): FK10's unit; W46 gives a 4D index ±3" (not re-read here).
- consequence: not given in my scope beyond the tag.
- note: I record this because every positive in my scope cites "given Λ".

### C-25 The Higgs section is evaluated by the same section at the same tau as the matter (a holomorphic function of tau); the reality r = |h.h|/|h|^2 ~ e^{-pi Im tau} is then forced
- commitment: the Higgs's direction is a holomorphic q-series in tau (theta nulls and Serre derivatives), so it has h.h = eta^6/4 exactly and is nearly null at the hierarchy band.
- type: CONSTRUCTION
- status: FORCED for the sections on record (B1739: "h·h = η⁶/4 exactly"); the choice of holomorphic sections is C-21.
- where: B1739 1 "R·R ∝ θ₂⁴ + θ₄⁴ − θ₃⁴ = 0 (Jacobi), to 10⁻³¹"; "The section the censuses use (B1691's components) has h·h = η⁶/4 exactly"; "F₆·F₆ = −48η⁶ exactly".
- excludes: non-holomorphic (Hermitian) or twisted sections with h.h of order |h|^2 (a "Higgs that is not null at hierarchy τ — one led at the cusp by the non-null eigenline e_i, which no Higgs on record is").
- alternatives on record: B1740 (F_-2, non-null; masses off by 132, chi2_six 3688); B1742 (two nearly null directions, both read S).
- consequence: B1739: "The hierarchy and an unmixed light generation exclude each other" under the SM reading; "the six's best row carries a CKM 4–24 times too large".
- note: the near-nullity is also what makes the hierarchy (B1740: "removing it removes both").

---

## F. The readings S vs S-tilde

### C-26 Eight reading assignments (S or S-tilde per sector) are admitted as a discrete menu; the assignment is NOT derived
- commitment: each sector reads the Higgs as S or S~ = eps conj(S) eps^T; the census ranges over all eight assignments as a discrete choice.
- type: CONVENTION / INTERPRETIVE
- status: READING (B1790: "the eight reading assignments are physically distinct and the global flip is not a convention"; "Reading each sector S or S̃ (eight), B1790: CHOSEN (not derived)", B1810 card).
- where: Z:60-71 `for rd in itertools.product((0, 1), repeat=3)` and `if r: Sm = B.EPS @ Sm.conj() @ B.EPS.T`; B1790 title "THE READING IS NOT DERIVED IN B1656'S FRAME".
- excludes: a derived hypercharge sign rule; additional readings (conj(S) alone, B1724 S* "covariant exactly under Γ⁰(2)"); readings dependent on the line.
- alternatives on record: B1660 (three readings S, S~, S*); B1724 (S* excluded by non-covariance); B1744 (Higgs at own twist, fails: "the charge sign is erased"); B1742 (all S with two Higgs).
- consequence: "the six's reading and an unmixed light generation exclude each other" at the hierarchy band (B1739); the nine use S~ throughout, the six use the split (B1726).
- note: B1790 2: "An imported hypercharge sign rule (an unearned identification) would reduce the reading to one bit, and that bit is genuine."

### C-27 S* (plain conjugate) is excluded from the menu on covariance grounds (B1724); only S and S~ remain
- commitment: S* (conj of components without eps conjugation) is dropped because it is T-covariant only under Gamma^0(2) (index 3); so it is not on the menu.
- type: CONVENTION
- status: FORCED for the covariance requirement (B1724, "S* is covariant exactly under Γ⁰(2) (index 3)"); the requirement itself is a CHOSEN principle.
- where: B1724 title and §3; B1726 "The covariant readings S and S̃ only (B1724)."
- excludes: S* as a third reading (B1660 used it); modular-covariant-only requirement is not a physical derivation.
- alternatives on record: B1660 (S, S~, S*).
- consequence: B1692's up-sector readings check shows the one-Higgs spread bound holds for every reading including conj(S).
- note: tie to C-26.

---

## G. The lepton factor and sector asymmetry

### C-28 The lepton factor c = 3 is inserted by hand in the comparison (multiplies the lepton m2/m3 by 3 and divides m1/m3 by 3); not derived in the frame
- commitment: after computing the frame's lepton ratios, they are rescaled by a factor c = 3 (Georgi-Jarlskog 3), with c = 1 giving a different (worse) fit.
- type: NORMALISATION / INTERPRETIVE
- status: CHOSEN ("the two ingredients put in by hand (the lepton factor 3 and the reading rule)", B1726); B1789 NEGATIVE for derivation; B1817 closes the twist-charge route.
- where: B1789 1 "In the instrument (B1726/B1741 compare.py, errs): c = 3 multiplies the frame's lepton m₂/m₃ by 3 and divides its m₁/m₃ by 3"; B1726 3 C: "The factor 3 is what makes the six specific (B1725: 2.34, 14%)".
- excludes: c as a free continuous number (B1726 R4: 0.92%, "at the bar"); c = 1; c from the charge structure (B1817: limits 4, 1/4, 1 or line constants, none 3 at N_c = 3).
- alternatives on record: B1789 (a)-(d); B1817 (anomaly-fixed charges at N_c = 2, 4, 5); S201, B1729, Pati-Salam, E6 (D = 1, B1738); the web seat's Clebsch (worsens).
- consequence: "On the six's slope family the frame's leptons equal its down quarks in the second generation at leading order (R₂ → 1), so that 3 is an input" (B1789); on order-5 lines D = 9 exactly, P-094 excludes D = 9 at 14 sigma (B1726 posthoc, B1742).
- note: the SU(5) 5-ality alignment makes leptons and down quarks identical for slope in 2/5 family; the factor 3 breaks it "as the 45 does".

### C-29 The sectors are distinguished only by their charge pairs (q_L, q_R); the Higgs charge is not a separate input
- commitment: up (1, -4), down (1, 2), leptons (-3, 6) are the only per-sector data; the Higgs 6Y = 3 enters only through q_L + q_R = -3 (up), +3 (down, leptons).
- type: CONSTRUCTION
- status: FORCED given the hypercharges (B1810 card "sectors ... FORCED given the hypercharges"), with the SM charge assignments imported.
- where: Z:38 `SECTORS = [("up", 1, -4), ("down", 1, 2), ("lepton", -3, 6)]`; B1790 2: "Each sector's net charge is q_L + q_R: up −3, down +3, leptons +3."
- excludes: charge assignments in other GUT embeddings (e.g. SO(10), E6); lepton charges derived from the frame.
- alternatives on record: B1817 (anomaly-fixed charges at N_c = 2, 4, 5); "fictitious leptons (-3, 5)" control in B1656 E5(c) (lifted).
- consequence: B1656 E4: with q_L - q_e = -9 = -3 q_H the lepton first generation is exactly massless on W59's order-9 lines; B1716 order-4 law; B1703 "u = d iff N | 6".
- note: these laws are statements about integer charge ratios mod N.

### C-30 Up and down coincide up to phase wherever N | 6 (B1703), so they differ only through the reading at the symmetric points
- commitment: this is a consequence of C-03 and C-10, not a choice, but it determines the table at the symmetric points.
- type: CONSTRUCTION (consequence)
- status: FORCED (B1703, cited in B1810).
- where: B1810 2.1 "This is B1703: u = d iff N ∣ 6, on every line of order dividing 6, at every τ".
- excludes: a frame that distinguishes u and d at order dividing 6.
- alternatives on record: none found.
- consequence: "up and down differ only through the reading" at the four configurations (B1810 3).
- note: included for completeness.

---

## H. Locality: point vs profile

### C-31 The coupling is a LOCAL residue at the puncture (a point coupling), not a profile/overlap on the fibre
- commitment: the Yukawa is read from the pole's residue (and finite part) at the single point z = 0; the Higgs is localised at the puncture and couples through the residue.
- type: LOCALITY
- status: CHOSEN ("The Higgs's localization at the puncture and its coupling through the residue are hypotheses", B1642 4); B1653: "only a coupling that does not act as a point does".
- where: F:44 `residues(x, y, t, rad=0.01, N=256)` (circle mean of pair(z)*z); F:55 `cA` (regularised norm, a profile around the puncture); B1653 title "the fibre's zero modes read at one point ... form a rank-one bilinear"; B1653 3 "What lifts the zero is a coupling's shape, not a line: two points; a profile with a non-zero holomorphic moment ...; a profile about the puncture".
- excludes: a Higgs profile on the fibre (tilted, anisotropic, or elliptic, which lift the zero, U6 b-d); two-point couplings; the surface-frame overlap integral (rank 3, W72); a Higgs profile that is a Szego kernel (B1653 5, P-151 "the Higgs's profile").
- alternatives on record: B1653 U6 (profiles lift, with sizes); B1653 5 (Szego kernel candidate, firewalled); W72 (surface frame overlap rank 3); B1651.
- consequence: rank <= 2 at a point: first generation exactly massless in the L-free limit "V = 1 ⊕ U(2) for every line"; the frame's lift at finite L is the profile-about-the-puncture (U6d) effect.
- note: B1653 3: "P-128 hands its question to P-151 and the parent (P-108): what is the physical Higgs's profile on the fibre, and which typing reads it?" The canonical-end (C-13) is a specific profile about the puncture.

### C-32 The fibre frame is chosen over the surface and thread frames
- commitment: the whole construction lives on the punctured torus fibre at modulus tau, not on the surface (family over tau) or an E8 frame.
- type: SCOPE-CUTOFF / INTERPRETIVE
- status: CHOSEN (B1810 card: "frame B1656's flat fibre frame (FR-FIB, B1809): CHOSEN (the frame)"; B1649 sharpening: "The result holds in the fibre frame; in the surface frame the null vector is not present, and in the E8 frame the Higgs is a flavon").
- where: B1810 frame card; B1649 sharpened note; B1653 dated correction (S129): the surface/thread frames' couplings "integrate over τ, along the family or a closed geodesic, not over the fibre".
- excludes: the surface frame (rank 3 overlap, W72); the thread frame; the E8 frame.
- alternatives on record: W72 (surface), W73; B1801 (agy lane, G2 3-cycle Q), P-564 (cover).
- consequence: the whole of the zero law (B1649, B1653) depends on the frame; "the null vector is not present" in the surface frame.
- note: B1667 2: "that the fibre frame is nature's (B1652)" not shown.

---

## I. Comparison conventions (tree-level outputs against data)

### C-33 The frame's tree-level ratios are compared with M_Z running masses with a 10% running allowance in quadrature
- commitment: the six ratios are compared with B1637's pinned running masses at M_Z (Huang-Zhou 2021) with sigma^2 = rel^2 + 0.10^2, treating the frame's ratios as scale-independent.
- type: NORMALISATION / INTERPRETIVE
- status: CHOSEN (stated allowance; "the 10% allowance's adequacy for the running between the fibre's scale and M_Z is not shown", B1693).
- where: B1693 data paragraph; B1695 G1 "chi2 < 14.86 with σ² = the data's errors² + B1637's 10%²"; B1742 "σ² = rel² + 0.10², B1720's".
- excludes: running the frame's Yukawas between the fibre scale and M_Z; a different scheme (pole masses); a scale-dependent comparison.
- alternatives on record: B1637 (10% allowance origin).
- consequence: the chi2 thresholds (16.75, 14.86, 21.67, 23.21) depend on it; B1825's chi2_ten 291 vs 23.
- note: I did not open B1637's data; only the record's text.

### C-34 The six ratios are scored as (m2/m3, m1/m3) per sector, so the "worst factor within 2" and chi2_six measure; a second metric chosen after the first
- commitment: the match criteria (worst factor, chi2_six, specificity against random hierarchies of a stated prior) are main's measures; "the calibration's random prior is main's choice, stated".
- type: CONVENTION
- status: CHOSEN (B1695 "What it does not do ... the calibration's random prior is main's choice"; B1726 "main's measure (the worst factor) and main's calibration").
- where: B1695 after-the-seal; B1726 1; B1735 note: "post hoc, τ fitted".
- excludes: other metrics (e.g. log-chi2 with full error model); a different random target prior.
- alternatives on record: B1735 precision cells (chi2_six 3.09); THE_BAR (p < 0.01 Bonferroni, B1726 posthoc E).
- consequence: B1726 "ingredients chosen on the seat's rows with the data in view (×22 would give 0.026)".
- note: outside my scope strictly (comparison design), listed because the user's scope names "comparison of tree-level outputs".

---

## J. Numerical / construction conventions that shape the output

### C-35 The theta-function realisation (explicit branches, NK = 24 truncation, jtheta limitations) fixes valid ranges: |Re tau| < 1 for the F_a sections
- commitment: the code sums theta_2 explicitly with q^{1/4} = e^{i pi tau/4} and uses mpmath jtheta only for theta_3, theta_4; F_a sections are exact only for |Re tau| < 1.
- type: CONVENTION / SCOPE-CUTOFF
- status: CHOSEN, disclosed (B1742 4, B1821 2 "The evaluator's guard: the F_a sections are exact only for ∣Re τ∣ < 1 (mpmath's θ₂ branch)").
- where: F:27 `NK = 24`; F:28-33 `thc`, `th1`; F:73-78 `th_mp` (explicit q^{1/4}); Z:44-46 (`th2, th3, th4 = mp.jtheta(...)` in `direction`); B1824 3 disclosed "mpmath's jtheta(2, 0, q) ... principal q^{1/4} is the wrong branch for ∣Re τ∣ > 1".
- excludes: the strip |Re tau| >= 1; B1634/B1674 (earlier jtheta branch defects).
- alternatives on record: W144/P-354.
- consequence: the census stays inside the strip; a lock asserts it.
- note: Z:44-46 calls `mp.jtheta(2, 0, q)` directly in `direction` for the F_a (a = 6, 10, ...); with Re tau in [0, 1/2] this is within the principal-branch range, so no error, but the code relies on it.

### C-36 Radii (L_max, L_2) are interpolated from B1667's Re tau = 1/4 column by Im tau only (+)
- commitment: for a given tau the census uses the end radii from B1667's column Re tau = 1/4, linearly interpolated in Im tau, regardless of Re tau.
- type: CONSTRUCTION / CONVENTION
- status: UNSTATED as a commitment in the arcs that use it (B1726: "interpolated along its Re τ = 1/4 column, as B1726 does", only in the evaluator's docstring Z doc and B1726 (not read in full here); B1667 itself shows L depends on Re tau).
- where: Z:29 `col = sorted(... if abs(p["tau"][0] - 0.25) < 1e-9)`; Z:51 `np.interp(tau.imag, ...)`; Z docstring "B1667's two radii (interpolated along its Re tau = 1/4 column, as B1726 does)".
- excludes: the exact Re-tau-dependent radii of B1667 at each tau (B1667 reports L over the grid, range 0.643-0.691 for L_max and 2.292-2.777 for L_2, so the interpolation error is bounded by that spread but not stated).
- alternatives on record: B1667 grid (48 points + 4 + 2 controls); B1810 uses B1667's exact point at (i) and omega = e^{i pi/3}.
- consequence: not recorded; B1667's range shows the radii vary by a few percent across the grid, with L_max near 0.617 where the 1-channel weight vanishes (B1810 2.3).
- note: I flag it as plausible hidden because L_max sits near the point where 2 pi L + c_1 = 0 (B1810), so small L errors change weights.

### C-37 omega is taken as e^{i pi/3} (B1667's point), and the "configuration-fixed" points are four
- commitment: the symmetric points are (i, 0), (omega, 0), (i, (1/2,1/2)), (omega, (1/3, 2/3)) with omega = e^{i pi/3} for the cusp-of-moduli grid.
- type: CONVENTION
- status: FORCED given the frame (B1810 card; "ω taken as e^{iπ/3} (B1667's point)").
- where: B1810 card configurations row; B1809 2 (cited).
- excludes: omega = e^{2 pi i/3} (an equivalent point by T-translation but a different tau in the strip); other symmetric points.
- alternatives on record: none found.
- consequence: at omega every listed direction falls on a stabiliser eigenline and the output is (0, 1) or rank one (B1810 2.2).
- note: B1691 uses the same omega.

### C-38 Truncation of precision: values below 1e-9 set to 0; degeneracy tolerance 1e-8 for V
- commitment: singular-value ratios below 1e-9 are zeroed in the table; V is "undefined" when any sector's gap ratio is below 1e-8.
- type: CONVENTION
- status: CHOSEN, stated in the card.
- where: Z:76 `if min(...) < 1e-8: deg.append(sn)`; B1810 1: "Values below 10⁻⁹ are set to 0".
- excludes: other thresholds.
- alternatives on record: none found.
- consequence: "V defined in 400 of 832 rows"; the counts of distinct outputs depend on it (B1810 "114/128/110/128 counted floating-point noise" in the draft).
- note: minor.

---

## K. Structural constraints derived (not choices) that fix what the frame can produce

These are not commitments, but they are the walls the commitments above produce; listed so the reader can map them.

### C-39 Consequence list (wall map)
- rank <= 2 and first-generation zero (B1653, from C-01 + C-31); lifted at finite L by the channel norms (B1716 Z1; det M = 1/4 Σ c_s R_s^2).
- exact zeros: electron massless on W59's lines at omega (B1656); order-4/order-2 law (B1716) and a second family at Re tau = 0, alpha in {1/12, 1/4, 5/12} (B1716 correction; B1826: c_j + c_k - c_1 - c_i = 0 there).
- the channel norms are identical across sectors (B1826 item 1; follows from C-14 and the Higgs twist ū = ±3w).
- exponent closed form e(m2/m3) = 1/2 - (||2 q_L alpha|| + ||2 q_R alpha||)/2 at leading order (B1788), conditional on hypotheses (a)-(c).
- the near-null Higgs and CKM corner inversion (B1739, B1826).
- lepton = down at order-5 lines (B1728, B1742).
- up and down coincide for N | 6 (B1703).

---

## The five commitments in my scope that most plausibly hide something

1. **C-04 / C-05 (the Higgs is untwisted and has no identity component).** It is where the frame's one known structural miss (corner inversion; B1739, B1826) originates, was UNSTATED as a choice at construction (B1692 mentions it only as a "does not do"), and the record's own attempt at the alternative (B1744, Higgs at its own twist) was done inside the point coupling, which erases the charge sign, so the question of a twisted internal direction is untested in the finite-L four-channel frame (P-562 open).
2. **C-02 (no electroweak doublet index; the fibre's Q8 doublet stands in for SU(2)_L).** The SM reading of H for down and H-tilde for up is imported by hand (B1790), and the "doublet" pairing by epsilon is a property of the fibre bundle, not of the weak group; every sector asymmetry rests on this identification.
3. **C-13 / C-16 / C-15 (the channel weight sqrt(2 pi L + c_s) with a flat-coordinate norm and a hyperbolic horocycle radius).** The weights are what lift the first generation and carry the entire slope dependence (B1788), they mix two metrics, and the record has already found that the exact end shifts c_s by 35-38% and kills the six near the four families' rows (B1726 S238 note, P-421).
4. **C-18 (H = I).** A CHOSEN input with 8 real free parameters per field that move outputs by 0.045 decades and the CKM moduli by 0.08 (B1822); the census, the comparisons and every sealed null share it, so any result that compares at that level of precision (the four's chi2 of 0.35, the twelve-percent misses) is conditional on a metric nobody derived.
5. **C-01 / C-31 (three generations as three quaternion images of one doublet read at a point; mass-ordered left singular vectors).** It forces rank <= 2 and the unitary V = 1 + U(2) structure at leading order, so the first generation's zero, the Cabibbo structure, and the corner order all come from the same two assumptions (one doublet, one point), and the generation basis (BLOCKS = [QJ, QI, QK]) fixes which quaternion directions the Higgs's three components multiply.

(Near misses for the list: C-36, the radii taken from the Re tau = 1/4 column only by Im tau, UNSTATED and sitting next to the point where the 1-channel weight vanishes; C-09/C-10, one tau and one line for all sectors, which the sealed B1825 shows cannot carry masses and mixing together.)

Count: 39 entries (C-01 to C-39; C-39 is a wall map, C-30, C-12 and C-25 are consequences recorded as forced).
