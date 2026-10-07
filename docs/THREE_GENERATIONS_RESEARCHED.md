# THREE GENERATIONS, RESEARCHED FIRST — what the physical "three" is, how every known construction obtains it, and what a frame must be able to see

cc (main), 2026-10-07; arc B1496 (sealed `02a95f4e6`, six expectations with priors before the report was read). The
owner's word: "should we do a deep research on three generations to understand them first, so we dont expect eyes
from the blind?" The research: a deep-research workflow at the owner's approval — five angles, 23 primary sources
fetched, 114 claims extracted, 25 verified by three adversarial votes each, 22 confirmed, 3 refuted, 105 agents — its
report archived at `frontier/B1496_three_generations_researched/verification/research_report.json`; every arithmetic
identity it rests on re-derived on main (`shape_identity.py`). What is marked VERIFIED below is verified against a
downloaded primary source by the run and, where arithmetic, by main; UNVERIFIED is said so. No count is computed
here; nothing is promoted. **0 of 19.**

## 1. What "three generations" is (the specification)

| requirement | the established statement | status |
|---|---|---|
| **(1) the count is an index** | heterotic E₈×E₈ on a Calabi–Yau threefold X with a stable SU(n) bundle V (c₁ = 0): ind(V) = Σ(−1)^p h^p(X, V) = ∫ ch₃(V) = ½∫ c₃(V) = −h¹(V) + h²(V) = −(families) + (anti-families); standard embedding V = TX: N = ∣½χ(X)∣ = ∣h^{1,1} − h^{2,1}∣, three needs χ = ±6. F-theory: χ(R) = n_R − n_{R*} = ∫_{S_R} G₄ over the matter surface. CHSW's own 1985 model (quintic/(ℤ₅×ℤ₅), standard embedding) had **four** generations | VERIFIED (arXiv:0808.3621, 0911.0865, 1112.1097; 1111.1232, 1107.5337; CHSW at abstract level) |
| **(2) vector-like pairs do not count** | a pair contributes with opposite signs to the one-loop Chern–Simons terms and cancels identically (Grimm–Hayashi eq. 2.31); h¹ and h² can both be non-zero with the index fixed — Braun's quintic quotient has one 5–5̄ pair the index cannot see | VERIFIED (1111.1232; 0909.5682) |
| **(3) three is obtained by selection: a free quotient and characters** | for G acting freely, χ(X/G) = χ(X)/∣G∣ and ind(V/G) = ind(V)/∣G∣, so three downstairs needs 3∣G∣ upstairs; the quotient bundle's cohomology is the G-invariant part of the cover's under an equivariant structure, unique up to a character of G — a Wilson line = flat line bundle — which selects the χ-isotypic piece; by the holomorphic Lefschetz formula **the index refines per character**: h²_n − h¹_n = (dim n/∣G∣)·ind for every irrep n (BCDD fn. 11). Tian–Yau χ = −18, free ℤ₃, quotient χ = −6; the quintic monad with ind = −75 over ℤ₅×ℤ₅ has H¹ = 3 × regular representation (Braun eq. 55); the (8,44) dP₆×dP₆ hypersurface with free ℤ₁₂ has −36/12 = −3 per character | VERIFIED (0909.5682, 1112.1097, 1104.0247, 0911.0865, 0808.3621). **Caution (a claim refuted 0–3):** "every Wilson line gives three 10's" holds only where the vanishings H⁰ = H² = H³ = 0 are proved in that character (Braun's quintic by computation); in general only the *index* per character is forced |
| **(4) the shape: as many 5̄'s as 10's** | n_10 = h¹(V), n_5̄ = h¹(Λ²V), n_1 = h¹(V ⊗ V*); the exact identity ch₃(Λ²V) = (n − 4)·ch₃(V) + c₁(V)·ch₂(V) gives, at n = 5 and c₁ = 0, ind(Λ²V) = ind(V): **the net 5̄ count equals the net 10 count automatically** — it is 4d anomaly cancellation (AGLP 1202.1757 eq. 4.18, Braun fn. 13). Main re-derived it: with Chern roots x_i, Σx_i = 0, ch₃(Λ²V) = [(n − 1)Σx_i³ + 3Σ_{i≠j}x_i²x_j]/6 = (n − 4)·ch₃(V) since Σ_{i≠j}x_i²x_j = −Σx_i³; `shape_identity.py`, ranks 2–8 | VERIFIED (three symbolic derivations in the run, one on main) |
| **(5) no chiral exotics** | separately from the index: h²(V) = h¹(V*) = 0 (no anti-10's) and h²(Λ²V) = h¹(Λ²V*) = 0 (no 5's beyond the Higgs pair); positive monads have h¹(V*) = 0; Braun's model has one pair whose presence depends on the Wilson-line character | VERIFIED (0808.3621, 0909.5682, 1202.1757) |
| **(6) nobody derives three** | in the one systematic scan that survived verification (He–Lee–Lukas), three is a **filter**: ind(V) = 3k, k ∣ χ(X), k among the allowed group orders — 2190 positive monads cut to 21; the paper's own words: "impose a basic three-family constraint … to filter". Every other construction in the pool (Tian–Yau, the quintic quotient, the ℤ₁₂ quotient, F-theory flux) chooses a space, bundle, group order or flux whose index is three. The Q4 survey items — anomaly arguments, asymptotic-freedom bounds, triadophilia (0706.3134), family symmetries A₄/S₃/Δ(27)/ℤ₃ — produced no surviving claim either way | VERIFIED for the pool; the universal negative is consistent with every surviving claim and not proven by it |
| **(7) empirically three** | the Z invisible width: N_ν = 2.9963 ± 0.0074 after the 2020 luminosity reanalysis (from 2.984 ± 0.008); light neutrinos coupling to the Z with Standard-Model strength, the LEP dataset closed | VERIFIED (PDG 2020/2025; arXiv:1912.02067, 1908.01704) |
| **(8) the orbifold mechanism** | T⁶/ℤ₃: the order-3 rotation of the hexagonal lattice, ω = [[0, −1], [1, −1]], has ∣det(ω − 1)∣ = 3 fixed points per T² factor, 27 in all, each carrying a twisted-sector 27; Wilson lines cut the multiplicity 27 → 9 → 3; the orbifold Euler number (1/3)(0 + 8·27) = 72 = 2(36 − 0) matches the resolved (36, 0) | arithmetic VERIFIED on main (`shape_identity.py`); the mechanism (Dixon–Harvey–Vafa–Witten 1985/86; Ibáñez–Nilles–Quevedo 1987) **UNVERIFIED in this run** — no surviving claim; the fetched orbifold sources (hep-ph/0411286, hep-th/9304045, 0802.2809, 0812.3503) were dropped at the budget, not refuted |
| **(9) the E₈ family triplet** | E₈ ⊃ E₆ × SU(3): whether the three of the family SU(3) and the Hodge-number three coincide in the standard embedding (where that SU(3) is the holonomy) | **UNADDRESSED** by the run; the record's B1275 verified the E₈ structure (six classes of 27 in orbits of three under A₂) |

## 2. The record's two frames, mapped and graded

| | F-CI (main's; B1418's definitions) | F-HE (the SM seat's harmonic E₈ frame) |
|---|---|---|
| what it counts | fixed points ∣det(X − I)∣ of an orientation-preserving isometry X on a cusp; three = the order-3 rotation of a hexagonal end (B1291) | the class index I(E) = n(E) − n(E*) of a flat module on a cusped 3-manifold; a generation = an interior class of an extension W₁ = [[V, c], [0, L]] with V = ν ⊗ four |
| the physics it is the shape of | **the orbifold count**: three fixed points of a global order-3 symmetry on a hexagonal torus, distinguished by characters (row 8) | **the smooth count**: an index on closed-cycle cohomology of a cover, cut by characters of a free deck group (rows 1, 3) — the room n(ν⁴) = closed-cycle classes (B1493–B1494), the companion = the cover with deck group T, the members = its characters, the index per character = Shapiro's ⊕_χ H¹(M; V ⊗ χ) |
| what the physics requires that the frame checks | the rotation must be a symmetry of the whole object (B1490: an order-3 isometry fixing a hexagonal end) | the count is an index, vector-like pairs cancel (I = n − n* does this by construction); the shape and no-exotics conditions are **separate** here: the class index is not a characteristic-class integral, so row 4's identity has no analogue — B1495's orbit module reads (10′, 5̄′) = (3, 9) where an SU(5) bundle could not |
| what the family lacks | no generated state has a global order-3 isometry; the hexagonal end is m003's (B486: m004's cusp is rectangular); L8a15's order-3 isometries cycle its ends and fix none | no closed cycle on any object the genesis determines (T-COMPANION-NO-ROOM); where a companion has room (m135's, at eight sign characters) no end carries the character, and the floor gives zero; on N₄₅ — a cover chosen by a character — ends and room meet and the count reaches two |
| grade against the specification | sees row 8's three only on an object with the symmetry; the family has none; **blind by construction on the family** | sees rows 1–3 and 5 (B1485–B1494 are honest index counts with their cusp decompositions); must check row 4 by hand (B1495 did; it fails on the direct sum); **blind on the family for want of closed cycles** |

**The one dictionary error the research exposes.** Three generations in the smooth mechanism is **one** rank-5 bundle
of index three — never three rank-5 bundles. The orbit module of B1495 (W₁ ⊕ W₂ ⊕ W₃, rank 15) is outside the E₈
dictionary altogether; its (3, 9) is not a failure of the orbit but of the object read. If the three members of L8a15
are to be one generation-triplet in this dictionary they must be *one* rank-5 module whose index is three — a module
the record has not built (a glued module, B1495's hatch), and whose Λ² would then have to be read.

## 3. The blind spots, stated

1. **A one-ended fibred state cannot carry an index of three in any module** (B1487, B1493): it has no closed cycles
   and one end; in the physics table it is a space with h^{2,1} = h^{1,1}. Asking it for three was expecting eyes from
   the blind — the frames were right to read one.
2. **A companion cannot either at the trivial line** (T-COMPANION-NO-ROOM), and where it has room no end is special:
   the two supplies of the count (the ends — the floor; the closed cycles — the cap) are separated on the family and
   meet on character-chosen covers (N₄₅). In the physics table that is the difference between a quotient of a
   simply-connected cover with χ = 3·∣G∣ and a fibred manifold.
3. **The orbifold three needs a global symmetry the grammar's acts exclude**: the order-3 element of SL(2, ℤ) is
   elliptic (trace −1), not a positive word and not Anosov. (A reading; firewall.) The record's F-CI three sits on
   two-cusped members of m004's class (B1418: m202, s959, o10_150726) where such a symmetry exists.
4. **The baseline for THE_BAR**: no framework derives three; every one selects. A selection on the record is the
   state of the art in physics, not below it; a derivation — a reason internal to the genesis for an object with
   index three — would be new. The record's candidate for that reason is the Lefschetz number: three ends ⇔ L³R, the
   only state whose act has three fixed points (B1494, the SM seat's Proposition A) — a number the genesis determines,
   on an object whose frames read one (B1492, B1493) and whose orbit reads (3, 9) (B1495).

## 4. Open after the research (for the next cells, in order)

- Build the **one** rank-5 module from L8a15's three members (a glued module: the three members as a single flat
  bundle, as B1486 fused two orders) and read I(W) and I(Λ²W) — the physics' object, not the direct sum.
- Verify row 8 (the orbifold mechanism) from a primary source on main — the run dropped it at its budget.
- Row 9: the E₈ family triplet against B1275 — is the deck ℤ/3 of L8a15 a ℤ/3 ⊂ SU(3)_family, and does that SU(3)
  coincide with a holonomy (which it cannot on a hyperbolic 3-manifold) or with a symmetry?
- The open questions the research itself names: whether H¹(cover) ≅ 3 × regular representation holds beyond
  Braun's quintic; whether any construction derives three; the orbifold-to-smooth bridge as a character selection;
  the vector-like spectrum in F-theory.

## 5. Sources (verified in the run unless marked)

Anderson thesis arXiv:0808.3621 · He–Lee–Lukas arXiv:0911.0865 · Braun–Candelas–Davies–Donagi arXiv:1112.1097 ·
Braun arXiv:0909.5682 · Bini–Favale arXiv:1104.0247 · Anderson–Gray–Lukas–Palti arXiv:1106.4804, 1202.1757 ·
Grimm–Hayashi arXiv:1111.1232 · Braun–Collinucci–Valandro arXiv:1107.5337 · PDG 2020/2025 light-neutrino review ·
Janot–Jadach arXiv:1912.02067 · Voutsinas et al. arXiv:1908.01704 · CHSW Nucl. Phys. B258 (1985) 46 (abstract) ·
triadophilia arXiv:0706.3134 (fetched; no surviving claim) · orbifolds hep-ph/0411286, hep-th/9304045, 0802.2809,
0812.3503 (fetched; dropped at the budget; UNVERIFIED) · Dixon–Harvey–Vafa–Witten 1985/86, Ibáñez–Nilles–Quevedo 1987
(standard; not read in this run).
