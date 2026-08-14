# B918 — V-L3: the hierarchy element V into the Kummer machinery — [α_V] = C: the value layer sits in the charge class, and its denominator ideal is the observer's place to the fourth power

**Date:** 2026-08-05 · **Seat:** computation subagent (for cc banking) · **Status:** DRAFT — exact tier for every verdict (four symbolic cube certificates, exact non-cube witnesses, exact place valuations); the pipeline identification v_g² = roots(HIER) numeric-certified at the 90-digit belt floor (V-L2 exactification remains the registered floor)

## The question (register item V-L3)

Handoff 7's §LXV put the hierarchy into K: the three generation weights
v_g² are one K-element's conjugate orbit, v_g² = V(ρ_g), with minimal
cubic led by 953⁴ — the seventh cubic of the √77 family. B910 completed
the Knus–Paques table of the first four cubics ([α_μ] = [α_gen] = [α_κ]
= C, [α_vac] = C⁻¹). V-L3 asks: where does the VALUE-layer element sit
in F*/(F*)³ (F = ℚ(√77, √−3)), and what do the value primes
{953, 1129, 421493} look like as places of K under V — is the degree-one
place "the observer's place" (H-B917-SPLIT)?

## The numeric anchor (stage 0, this bench)

The relay pipeline (solo norms.py atom construction + belt100 coupling
loop) rerun here at TRUE dps 100 — the §LXIV throttle (`mp.mp.dps=50`,
`sp.N(r,48)` inside norms.py) removed at exec time, third-party code in
an isolated namespace. Reproduced: 15 atoms (6 colored, 9 colorless),
17 couplings, residuals 953λ−2304 = 2.8e-85 and 953·CCC−13824 = 3.5e-85
(the belt floor), and the three v_g² at 95 digits:

- v₁² = 5.69496465426270228001143950186439098035115372418250329726…
- v₂² = 8.32706418238040182368054522265982401117594371566353983842…
- v₃² = 19.4508737756638681283888496627508985170727429570988247761…

(Note for the record: the six CCl couplings are the full symmetric
v_i·v_j table; the triple (5.6949…, 6.8863…, 10.5248…) sometimes quoted
is (v₁², v₁v₂, v₁v₃), not the v_g² triple — the exact product law
e₃ = 2³²3¹¹/953⁴ ≈ 922.41 adjudicates: only (v₁², v₂², v₃²) has that
product.)

## The hierarchy cubic, pinned exactly (stage 1)

e_i·953⁴ land on integers to < 1e-70 (with e₃ = 27·2304⁴ the EXACT
banked P9 anchor, pure integers):

> **HIER(x) = 953⁴·x³ − 2⁸3⁹·13·421493·x² + 2²¹3⁸·17·1129·x − 2³²3¹¹**

- primitive, **irreducible over ℚ**; disc = 2⁶⁴3²⁴5⁶7³·11·73²·214189²,
  squarefree kernel **{7,11}** ✓ — the √77 family (and B917's
  disc(hierarchy) reproduced digit-for-digit);
- e₁'s numerator carries 13·421493, e₂'s carries 17·1129 (§LXVI ✓);
- its three real roots = the belt anchors to 7.3e-88;
- **[1,2] split over K = ℚ[ρ]/μ, root certified exactly**:
  **V(ρ) = 1084447130452992/139398566318089
  + (2399403349337702400/1812181362135157)·ρ
  + (3020358603911646412800/23558357707757041)·ρ²**
  with HIER(V(ρ)) ≡ 0 mod μ(ρ) (polynomial remainder, exact);
  coordinate denominators 13²·953⁴ | 13³·953⁴ | 13⁴·953⁴;
- the branch identity is the identity map (ascending ρ_g ↦ ascending
  v_g², max err 7.3e-88), HG2 reproduced;
- **the solo seat's numeric K-linear certificate (HG2, residual 3e-83 on
  their bench) is EXACTIFIED here**:
  V·(19474 − 1154453ρ − 18197524ρ²) + (−152295 − 15081984ρ
  − 50844672ρ²) ≡ 0 mod μ — exact, their two integer triples verbatim.

## The Kummer element and the theorem (stage 2)

B910 construction, one fixed convention (α = (−27q + 3s√−231)/2,
s = +√(disc/77)):

**α_V = 971519719161915524236273846912397869056/953¹²
+ (2³¹3¹³5³·7·73·214189/953⁸)·√−231**

— the value prime enters the DENOMINATOR (953¹², 953⁸), where μ and κ
carried their primes as numerator content (13⁶, 19⁶); the V-generator's
index primes 73·214189 sit in the √−231 numerator.

Local scans (8 clean primes, 32 clean embedding-tests per pair, twist
set ζ₆ᵃε₇₇ᵇ) for discovery; every positive proved by exact symbolic
cubing, every dead twist carrying an explicit χ₃-witness (asserted
exhaustive):

1. **α_V / α_μ = γ³** with **γ = 3362527904156467200/(13³·953⁴)
   − (27239886398914560/(13³·953⁴))·√−231** — verified by exact
   symbolic cubing (and re-verified in radical arithmetic sharing no
   code, `independent_check.py`).
2. **α_V / α_gen = γ³** with γ = 26861739/(2²·953⁴)
   − (41889411/(2·5·7·11·953⁴))·√−231.
3. **α_V / α_κ = γ³** with γ = 2ζ₆·(u + v√−231),
   u = 609584158276853760/(19³·953⁴), v = −295648656434933760/(19³·953⁴).
4. **α_V · α_vac = γ³** with γ = 2ζ₆·(u + v√−231),
   u = 207516007799370547200/(13·953⁴), v = −1681090132047298560/(13·953⁴).
5. α_V·α_μ, α_V·α_gen, α_V·α_κ, α_V/α_vac: **non-cubes at all 9 twists**
   (exact χ₃-witnesses per twist in `results.json`); α_V itself a
   non-cube at all 9 twists — the class is nontrivial.

> **[α_V] = C = [α_μ] in F*/(F*)³, with NO unit twist — under the one
> fixed convention the hierarchy element carries exactly the charge
> orientation. The One-Class theorem extends to the value layer: all
> four structure/value cubics with a root in K (μ, generic, κ, V) are
> the SAME Knus–Paques element; the vacuum remains the lone inverse.
> Consequently vacuum ⊕ V = split — the vacuum field annihilates the
> hierarchy cubic exactly as it annihilates the charge cubic.**

### The five-element multiplication table (C := [α_μ], group ℤ/3)

Assignments: [α_μ] = [α_gen] = [α_κ] = [α_V] = C, [α_vac] = C⁻¹.

| · | α_μ | α_gen | α_vac | α_κ | α_V |
|---|---|---|---|---|---|
| **α_μ** | C² | C² | 1 | C² | C² |
| **α_gen** | C² | C² | 1 | C² | C² |
| **α_vac** | 1 | 1 | C | 1 | 1 |
| **α_κ** | C² | C² | 1 | C² | C² |
| **α_V** | C² | C² | 1 | C² | C² |

V-row consistent with all 8 scans + 4 certificates (asserted); the
4-element sub-table equals B910's banked table entry-for-entry
(asserted).

### Certificate structure

The B910 pattern extends with one refinement: the same-side ratios
V/μ and V/gen are **untwisted elements of ℚ(√−231)** (no ζ₆ at all —
irrational, unlike the rational μ/gen, but twist-free), while the
cross-pencil V/κ and the annihilation V·vac are **2ζ₆·ℚ(√−231)**,
exactly the compact-certificate shape. Every V-certificate denominator
carries **953⁴ alongside the partner's prime** (13³ for μ, 19³ for κ,
13 for vac): the value prime rides every bridge to the value layer.

## The place structure (stage 3) — H-B917-SPLIT answered: YES

Exact preliminaries: e₁, e₂, e₃ have lowest-terms denominator EXACTLY
953⁴, so the characteristic-polynomial valuation argument
(V³ = e₁V² − e₂V + e₃) confines V's denominator support to places over
953 and bounds v ≥ −4 there. Monic model y = lead(μ)·ρ, p ∤ disc(model)
for all three value primes (asserted); simple-root Hensel lift to
p⁴⁰; degree-two valuations via the lifted cofactor quadratic (the
residue algebra is the field F_p², so {1, y} is an integral basis).

| p | ρ at the deg-1 place | v_w(V) deg-1 | v_w(V) deg-2 | norm check |
|---|---|---|---|---|
| 953 | ρ ≡ 612 | **−4** | **0** | −4 + 2·0 = v_p(N) = −4 ✓ |
| 1129 | ρ ≡ 70 | 0 (residue 617) | 0 (residue 581 + 387y) | 0 ✓ |
| 421493 | ρ ≡ 153127 | 0 (residue 107540) | 0 (residue 39306 + 166513y) | 0 ✓ |

> **YES — theorem-shape. V's denominator ideal is (the degree-one place
> over 953)⁴, EXACTLY: all four powers of the λ-denominator sit on the
> one place of K where ρ has a rational residue — the observer's place —
> and none on the degree-two place.** The other two value primes enter
> through numerator congruences instead, each localized exactly:
> at **421493** (e₁'s prime) the TRACE of the V-residues vanishes
> (617-analogue: 107540 + Tr_deg2 ≡ 0); at **1129** (e₂'s prime) the
> SECOND symmetric function of the V-residues vanishes
> (N_deg2 + res₁·Tr_deg2 ≡ 0). Both congruences verified exactly with
> the 953⁴-unit correction (asserted).

So the three value primes play three distinct roles in V's biography:
953 = the pole (denominator, deg-1 place only), 421493 = the trace
zero, 1129 = the e₂ zero.

## Tier statement

Exact tier: HIER as an exact object (irreducibility, disc, split, root
certificate, HG2 exactification), α_V, all cube certificates and
χ₃-witnesses, the table, the integrality lemma, all valuations,
residues and congruences. Numeric-certified tier: the identification of
HIER's roots with the PIPELINE's v_g² (90-digit belt, reproduced on
this bench at dps 100 with residuals ~3e-85); the V-L2 exactification
pass remains the registered floor for that identification.

## Files

- `v_kummer.py` → `results.json` (anchors, the pinned cubic + exact
  root, α_V, scans with witnesses, the four cube certificates, the
  five-element table, the place structure + verdict); runtime ~1 s
  (the belt regeneration, 122 s, lives in the session scratchpad per
  relay discipline — driver `b918_belt.py`, output `b918_belt_out.json`)
- `independent_check.py` — re-verifies γ(V/μ) and one χ₃-witness
  through sympy radical arithmetic (no shared code)

## Depends on

B866 (μ), B888 (the two weight cubics), B902/B910 (the construction +
the four banked classes), B917 (the value-arc verification + P9 at
receipt), solo ledger §LXIV–LXVI (the belt, HG1/HG2, the product law —
re-derived and exactified here).

## Registered follow-ups

- The 953-residue of the UNIT part of V at the observer's place (and
  whether the residues 617/107540/… carry structure) — untouched.
- V-L2: exactify the pipeline (couplings as exact algebraic numbers),
  closing the last numeric-certified link.
- The Galois-orbit question one level up: the wall-matching (B910's
  registered follow-up) now has a value-layer edge — does the
  generation functor's S₃-action permute the three conjugates of V
  compatibly with the Kummer orientation?


## Banking-seat note (cc, 2026-08-05)

Both verification paths rerun at banking (independent_check + the full script).
Two banked headlines: (1) **the One-Class theorem now spans the whole value
layer** — five elements, one nontrivial class C and its inverse, with V
untwisted in C; (2) **the observer's-place theorem** — H-B917-SPLIT resolved
YES: den(V) = 𝔭₁(953)⁴ exactly, the hierarchy's pole living entirely on the
unique degree-one place. The prime-role trichotomy (pole / trace-zero /
e₂-zero) and the numerator-vs-denominator asymmetry (structure primes 13⁶/19⁶
above, value prime 953⁴ below) are banked as structure. The agent's catch of
the brief's wrong triple (adjudicated by the exact product law) is noted as
verify-don't-trust working against the dispatcher itself. The V-L2
exactification of the pipeline link (v_g² ↔ HIER roots, currently 7.3e-88
numeric) remains the registered floor.
