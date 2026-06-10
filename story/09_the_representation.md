# 09 — The representation, crystallized

> Narrative, not claim. Cites the mathematics one-way.

Chapter 04 collapsed the sprawl to one object, `ρ_n`, and one target: decompose it. The next long arc
(**B111–B124**) did not close that target — the wall still stands — but it *crystallized* what `ρ_n` is, split the
problem into a proved half and an open half, and gave the open half a name.

## The sign half, proved

The first real progress was to cut `ρ_n` into two questions. The **signs** — which sectors are `char(+M^h)` and
which are `char(−M^h)` — turned out to be governed entirely by the **opposition involution** `θ = −w₀` (chapter 04,
`../knowledge/K005`). An elementary root-system lemma (the reversal involution on the height-`h` root spaces) plus the
contragredient/parity assignment gives the multiplicities
```
   mult char(M^h) = ⌈(n−h)/2⌉,     mult char(−M^h) = ⌊(n−h)/2⌋,
```
for **all `n`**, engine-free — no Procesi ring, no ε-series (**B112**, V99). That is the first piece of the catalog
proved from first principles at every rank. The fixed-root sign was pinned to `(−1)^{h+1}` (**B118**, V106), and two
tempting shortcuts to the *other* half were killed cleanly and tombstoned (`θ → c`, `s_n → c`: an order-≤2 symmetry
cannot reach the order-4 degree=rank scalar).

## The magnitude half has a name: `Sym^n(W)`

The **magnitudes** — the multiplicity sequence `μ_d` itself — were reframed, not closed. The interleaving insight
(**B117**, V104) showed the tower is the **Sym two-sequence** `μ_d = [2≤d≤n] + [0≤d≤n−3]`, one object rather than a
"bulk plus a promotion," dissolving the old "degree=rank promotion" picture. Then (**B122**, V111) the two-sequence
got a clean closed form as **symmetric powers of a 3-dimensional representation**:
```
   ρ_n  =  Sym^n(W)  ⊕  ( Sym^{n−3}(W) ⊖ W ),       W = V ⊕ 1.
```
This is a genuine `GL(2)`-module identity (verified symbolically, det-independent, `n ≤ 8`). And `W` is **canonical**:
it is the **external monodromy `SL(2)`'s fundamental** (**B121**, V109), `det(W) = −1` — the same orientation sign
that runs through the whole project (`../knowledge/K002`, `K008`). The naïve guess "`W` = the Fricke 3-space" is
wrong precisely because Fricke `= Sym²(V)` carries the *internal* principal (Kostant) `sl(2)` with `det = +1`; the
tower carries the *external* one (mixed parity), and the two agree only at `n = 2`. So `ρ_n` is the symmetric algebra
of the external fundamental — and the project finally knows, exactly, which 3-dimensional representation it is climbing.

## The wall, re-aimed

Here honesty matters: `Sym^n(W)` is module-iso-*equivalent* to the two-sequence — proving it for all `n` is the same
as proving `μ_d`. There is **no functorial `Sym(W) → trace-ring` map**; the one clean coincidence (`Sym⁴(3) = 15 =
sl(4)`) is special to `n = 4` and does not generalize. So the arc **re-aimed the prize** without lowering it: *prove
the tower is functorially `Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`.* That functorial construction is the wall, and it is exactly
where the project stands.

## Two asides that fell out for free

Once `ρ_n` was understood this cleanly, two small results dropped out — both banked as **firewalled** asides, never as
physics:

- **Arithmeticity** (**B123**, V112): the figure-eight is the *unique* arithmetic knot (Reid 1991), shape `e^{iπ/3}`,
  trace field `ℚ(√−3)`. This is the **third** independent reason `m = 1` is special — joining the systole and the
  expansion threshold (`../knowledge/K009`).
- **Reciprocity / time-reversal** (**B124**, V113): the spectrum is reciprocal-closed `(λ, 1/λ)` and time-reversal
  acts as `λ ↔ 1/λ` — but this is **generic symplectic** geometry, not a metallic feature, and the mode count is
  *exactly* forward/backward symmetric (no arrow). The one metallic-specific residue is a `det = −1` **chirality (P)**
  asymmetry, not a time direction. The "two-headed time" reading it invites is labeled and fenced
  (`../philosophy/P006`), firewalled from physical time.

## Where the crystallization leaves us

The object is now sharp: `ρ_n` is the symmetric algebra of a canonical `det = −1` three-dimensional rep; its **signs**
are proved (all `n`), its **magnitudes** are named (`Sym^n(W)`) but not functorially constructed, and the `n ≥ 5`
catalog stalls at exactly that missing functor (three distinct obstacles converge there, V91). The proven core
`P1–P16` is untouched; the physics chapter stays CLOSED; the speculation that motivates the next calculation lives,
labeled, in `../speculations/` and `../philosophy/`.

That is the state: one small self-generating object, fully recognized as a representation, with one sharp functorial
theorem left to prove.

→ `10_chirality_and_completeness.md` (the internal questions close), then `11_the_bridge_and_the_wall.md` (the
outward reach and the boundary). ← back to `00_the_question.md`. See also `08_where_it_stands.md`,
`../knowledge/K008`, `../ARCHITECTURE.md`.
