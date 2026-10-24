# W151 — the two-object route: a constant-ratio pair of sections never gives the nine's target's pattern (the pair lemma), three sections reach its class, and a constant-coefficient sum does not follow the cone (the rule, committed before the script)

The SM-derivation seat, 2026-10-24. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **W149** showed that no single holomorphic section of ρ ⊗ χ reaches the nine's target. The breaking chain's fork
  (section 5) left "two objects" open, and main's B1747 leaves "a second doublet with equal readings".
- **The owner approved the two-object route** ("yes i agree thank you, do them", 2026-10-24; relay §255, item 6).
- **The physical form:** two directions read the same way, each a section, with a constant ratio κ. The Higgs
  direction is then h = A + κB. Main's B1743 pencils (κ free, five pairs, the best 41.9) are the post-hoc data side
  of the same question. This arc is the structure side, data-free.

## The objects

- **The catalogue:** W146's twelve record forms (R, ∂R and F_a for a ∈ {−10, −6, −2, 2, 6, 10, 14, 18, 22, 26}) and
  their twelve complex conjugates, which are antiholomorphic. That makes 24 objects, 276 unordered pairs, 2 024
  unordered triples and 300 bilinears X·Y (squares included).
- **The lines** (W146's): l1 = x, l3 = y − iz, l7 = y + iz. Then h·h = l1² + l3 l7 and X·Y = l1 l1′ + (l3 l7′ +
  l7 l3′)/2. Conjugation exchanges l3 and l7 and keeps the rates.
- **The rates.** A component that falls like e^{−2πρy} along τ = iy has rate ρ. It is read from the slope over
  y ∈ [6, 8] and rounded to the lattice (1/24)ℤ.
- **For a sum h = Σ κ_i X_i with generic constant κ_i:**
  - its line rates are the componentwise minima;
  - ρ_lead = min(ρ₃, ρ₇) and m = min(ρ₁, ρ₃, ρ₇);
  - **D** = ρ₁ − ρ_lead, so ln|δ| falls at slope −2πD (δ = √2 l1 over the leading null line, as in W149's chart);
  - **E** = rate(h·h) − 2m, so ln I falls at slope −2πE. E ≥ 0 always.
  - rate(h·h) is the least rate among the nonzero bilinears X_i·X_j; for generic κ their leading terms cannot cancel.
    h·h identically zero gives E = ∞.
  - A bilinear counts as identically zero when it is below 10⁻⁴⁵ of \|X\|\|Y\| at y = 6, 7 and 8 (60 digits).
- **The identity behind the chart** (by hand): ε + δ²/2 = h·h / l3², for the chart through h₀.
- **The target's box** (from W149's read-out, −0.632 for ln|δ| on L₂, and W146's K4, +0.243 for ln I on L₂ and −0.145
  over all ten optima, with a margin):
  - ln|δ| slope in [−0.85, −0.45], that is D ∈ {2/24, 3/24};
  - ln I slope in [−0.5, 0.5], that is E ∈ {−1/24, 0, 1/24}.

## Weave or thread

**The lemma (Q3) is weave-type.** It holds for every pair of holomorphic or antiholomorphic sections of ρ ⊗ χ, at
any weight and any character, the two members' characters free to differ, and it uses only ρ(T)'s eigenvalues on the
lines (W149's C3). **The census (Q1, Q2, Q4, Q5)** is over every form in W146's record list and its conjugate, with
none hand-picked.

## The cells, with predictions, priors and pre-mortems

| cell | prediction | prior |
| --- | --- | --- |
| Q1 | **The rates (by hand, then read).** In units of 1/24, (ρ₁, ρ₃, ρ₇) is (3, 9, −3) for R and for ∂R; (3 + 2a, 3 − a, 15 − a) for F_a with a ∈ {−10, −2, 6, 14, 22} (sign ε = +1); (3 + 2a, 15 − a, 3 − a) for a ∈ {−6, 2, 10, 18, 26} (ε = −1); the conjugates swap the last two. Every read rate lies within 10⁻⁶ of its lattice point. So every ρ₁ is 3 mod 4 and every null rate is 1 mod 4 (in 24ths), and on the catalogue D ∈ 1/12 + (1/6)ℤ and E ∈ (1/6)ℤ | 97% |
| Q2 | **The exact zeros.** Of the 300 bilinears exactly 20 vanish identically: R·R, R·F₂, F₂·F₂, R·∂R and F₂·∂R (since R = F₂/(2η⁴), R·R = 0 and its derivative); F₋₂·∂R and F₁₀·∂R (F_a·R is a constant times η² for a = −2 and 10, and then F_a·∂R = 0); F₋₁₀·F₁₄, F₋₆·F₁₀ and F₋₂·F₆ (Jacobi's identity, a + b = 4); and the conjugates of these ten | 80% |
| Q3 | **The pair lemma.** For A, B holomorphic or antiholomorphic sections of ρ ⊗ χ_A and ρ ⊗ χ_B and generic constant κ, h = A + κB satisfies: **if 0 < D < ¼, then E ≥ min(2D, ¼).** In words: while δ falls slower than e^{−π Im τ/2}, I falls at least as fast as \|δ\|² or as e^{−π Im τ/2}, whichever falls slower. On the catalogue, all 276 pairs obey it | 95% |
| Q4 | **The pair census.** Exactly 20 pairs have 0 < D < ¼, all with D = 1/12 and E = 1/6: X ∈ {R, R̄, ∂R, ∂R̄, F₆, F̄₆} with Z ∈ {F₋₂, F̄₋₂}; X ∈ {F₁₄, F̄₁₄} with Z ∈ {F₋₆, F̄₋₆}; X ∈ {F₂₂, F̄₂₂} with Z ∈ {F₋₁₀, F̄₋₁₀}. So no pair lies in the target's box. Exactly 15 pairs have E = 0 with D > 0, all with D ≥ ¼: (X, Y) with X ∈ {R̄, ∂R̄, F₆} and Y ∈ {R, ∂R, F̄₆}, and (F_a, F̄_a) for a ∈ {2, 10, 14, 18, 22, 26}. A direct evaluation of h·h at κ = 0.37 + 0.81i gives the same E on every pair whose h·h is not identically zero | 88% |
| Q5 | **Three members reach the class.** Of the 2 024 triples exactly 22 lie in the target's box, all with D = 1/12 and E = 0. They are (X, Y, Z) with X leading l3 and Y leading l7 at one rate m, and Z e₁-led with ρ₁(Z) = m + 1/12. For m = −3/24: X ∈ {R̄, ∂R̄, F₆}, Y ∈ {R, ∂R, F̄₆}, Z ∈ {F₋₂, F̄₋₂} (18). For m = −11/24: (F₁₄, F̄₁₄) with F₋₆ or F̄₋₆ (2). For m = −19/24: (F₂₂, F̄₂₂) with F₋₁₀ or F̄₋₁₀ (2). Among them is (R̄, R, F₋₂). The class's slope for ln\|δ\| is −π/6 ≈ −0.52, the nearest the catalogue allows to the target's −0.63 | 80% |
| R | **Read-outs** (no prediction): the (D, E) distribution over the pairs and over the triples; the pairs with E = 0 and their D. On B1743's ten rows (W146's sha-checked target), the ratio \|ε + δ²/2\| / (\|δ\|²/2). Across the eight L₂ rows, the spread (largest distance from the mean) of δ²/2 and of ε + δ²/2 | — |

**The lemma's proof (by hand, fixed now).**
- Take h null-led with 0 < D < ¼. Let g = \|ρ₃ − ρ₇\| for h. In h·h = l1² + l3 l7 the two terms have rates 2m + 2D
  and 2m + g. So E ≥ min(2D, g), and E = g when g < 2D, since the l3 l7 term then leads alone with a nonzero
  coefficient.
- Suppose g < ¼. Let X be the member that gives h's lead line its rate m, and Y the member that gives the other null
  line its rate m + g.
  - X ≠ Y, since one section's two null lines differ by ½ mod 1.
  - X's e₁ rate is at least ρ₁(h), which exceeds m, and differs from m by ±¼ mod 1. So ρ₁(X) ≥ m + ¼.
  - Y's e₁ rate differs from m + g by ±¼ mod 1 and exceeds m. If it were below m + g, it would be at most
    m + g − ¼ < m. So ρ₁(Y) ≥ m + g + ¼ ≥ m + ¼.
  - A pair has no third member, so ρ₁(h) = min(ρ₁(X), ρ₁(Y)) ≥ m + ¼, that is D ≥ ¼, a contradiction.
- So g ≥ ¼, and E ≥ min(2D, ¼). ∎ With three members the third can supply ρ₁, which is Q5.

**Pre-mortems** (how each cell could fail for a reason that is not the finding):
- **Q1.**
  - The F_a with large a have components near 10⁻⁷⁰ at y = 8. They are products, so 60 digits suffice.
  - Slopes over [6, 8] carry relative corrections near e^{−6π} or below, far inside 10⁻⁶. A miss of the lattice is an
    instrument failure first.
  - The signs ε are W143's `eps_of`, read before the rule.
- **Q2.**
  - A nonzero bilinear could fall below the threshold. By hand, the smallest nonzero one on the catalogue is near
    e^{−2π·6·(42/24)} ≈ 10⁻²⁹ of \|X\|\|Y\| at y = 6, and a true zero computes near 10⁻⁶⁰.
  - A mixed bilinear (one holomorphic member, one antiholomorphic) could vanish along τ = iy by an accident of the
    axis. By hand none does; an extra zero would be a finding about the axis, diagnosed before anything else.
  - The list was 16 in a first pass. Checking every ∂R·F_a's leading coefficient by hand, (10 − a)/6 or a single
    nonzero term, found the two at a = −2 and 10, and the identity behind them. A further missed zero would show as an
    extra member, and would be diagnosed as a hand slip first.
- **Q3.**
  - "Generic κ" can hide a cancellation for special κ. The lemma is about generic κ, and the census uses the rates.
  - Exact zeros in bilinears raise E. They cannot lower it.
- **Q4.** The counts are by hand from Q1's table. A count that differs, with Q1 and Q3 holding, is a hand slip, to be
  diagnosed as such.
- **Q5.**
  - The class needs the leads' cross term X·Y (rate 2m) to stay below Z's own l1² term (rate 2m + 4/24). By hand it
    does.
  - The count of 22 is by hand, with the same risk as Q4's.
- **R.** The ratio and the spreads use fitted values, so they describe; they do not test.

## What the outcomes mean (fixed now)

- **Q3 and Q4 hold.** Two directions read the same way, each a holomorphic or antiholomorphic section, with a constant
  ratio, cannot give the target's pattern. For the target's δ slope (−0.63), I would have to fall at slope −1.26 or
  faster, and the target's I is flat (+0.24 on L₂). This holds for every section of ρ ⊗ χ at any weight and
  character, not only the catalogue's. B1743's pencils (best 41.9) are consistent with it. The second-doublet route of
  B1747, read as such a sum, needs three or more sections, a ratio that varies with τ, or a section that is neither
  holomorphic nor antiholomorphic.
- **Q5 holds.** Three sections reach the target's asymptotic class, at the nearest lattice slope −π/6.
- **The cone-tracking reading (by hand; R reads the target's numbers).**
  - For a triple in the class, ε = l7/l3 tends to a constant ε∞, with corrections of relative order q^{1/3} or
    smaller (the members' other null exponents lie at least 8/24 above the leads), while δ²/2 falls like q^{1/6}. So
    ε + δ²/2 = ε∞ + δ²/2 + O(q^{1/3}).
  - So \|ε + δ²/2\| moves across the band as δ²/2 does, unless ε∞ sits near −δ²/2 at one point.
  - The target holds \|ε + δ²/2\| near 0.01 while \|δ\|²/2 moves from 0.055 to 0.039 on L₂ (W149's rows). Following
    the cone with a constant defect needs h·h's δ²-term to cancel. That is a quadratic relation among the
    coefficients, the structure of a square h = ψ ⊗ ψ (M is the symmetric square of the cube group's spinor), plus a
    constant off-cone part.
  - A ψ whose two components lead 1/8 apart (possible for a sum of two spinor sections; one spinor section's
    components are ¼ apart) squares to a point on the cone moving like q^{1/8}, as S204 describes the target. This is
    named as the next candidate, not claimed.
- **Any cell fails:** the failure is the finding, and it is diagnosed before anything else is said.
- **This is data-free.** The read-outs of the target's numbers are a description, not a test.

## What stays out

- κ varying with τ, and the vev ratio from a potential (the doublet potential itself).
- The twisted spaces' zero-free lines (W133, W143) beyond the catalogue's F_a.
- Spinor-valued sections and the squared route (named as the next candidate).
- Sums of four or more members; sections that are neither holomorphic nor antiholomorphic.
- Different readings for H_u and H_d (S212's two-doublet frame), and any χ² or comparison beyond the read-outs.

## Seen before the rule (disclosed)

- **Read:**
  - B1743's table, the five pencils and their 41.9;
  - the web seat's RECORD PAIRS (96.3);
  - S204's description;
  - W146's lemma on the classes (1/8, 3/8, 7/8), its K4 slopes and its exact zeros R·R, F₂·F₂ and R·∂R;
  - W143's `eps_of`;
  - W149's read-outs (the rows' δ and ε + δ²/2, the L₂ slope −0.632).
- **By hand:**
  - the rates table, the residues mod 4 and the lattices for D and E;
  - R = F₂/(2η⁴), and the Jacobi zeros at a + b = 4;
  - the leading coefficient of every ∂R·F_a; F₋₂·R = −3η²/2 and F₁₀·R = −24η², and from them F_a·∂R = 0 at a = −2
    and 10 (F_a·∂R = (2/n) η^{−a} q d/dq(η^a G) − (E₂/12) G with G = F_a·R and n = a + 2, and directly at n = 0);
  - the pair lemma and its proof;
  - the counts 20, 15 and 22, and the members of each;
  - the bound on the smallest nonzero bilinear;
  - the identity ε + δ²/2 = h·h / l3², the cone-tracking reading and the squared-spinor reading;
  - from W149's rows: \|ε + δ²/2\| ≈ 0.0098 against \|δ\|²/2 ≈ 0.050 at Im τ 2.1.
- **A first draft** of this rule stated the lemma as "E = 0 only if D = 0, D ≥ ¼ or D < 0", with E measured from the
  null lead, and argued Q3 from the catalogue's gaps. The general bound and the lattice argument replaced it before
  the commit. The same draft listed 16 exact zeros; the two at F₋₂·∂R and F₁₀·∂R were added by hand before the
  commit.
- **Not run:** no script exists.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
