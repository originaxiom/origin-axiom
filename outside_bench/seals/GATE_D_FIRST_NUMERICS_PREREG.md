# SEAL — GATE D, THE FIRST NUMERICS AT THE OBJECT'S OWN κ

**Sealed 2026-08-30, pushed BEFORE any computation.**

The owner asked whether Q7–Q10 are ours. Exhausted first, per the standing rule, and the answer is
**two of four, partly** (`THE_GATE_OWNERSHIP.md`). This cell takes the one the corpus itself says is
ours: **Gate D — "Obstruction / tier: non-self-adjoint spectral theory. Specialist (*some in-sandbox
numerics possible*)."** `already_banked.py` on its terms returns **0 settled arcs at threshold** —
genuinely untouched, from the same instrument that discriminated correctly on the cosmology
controls.

## 0. The object of the cell, derived not chosen

The Fibonacci trace map `(x,y,z) ↦ (xy − z, x, y)` preserves
`I(x,y,z) = x² + y² + z² − xyz − 2` — **the programme's own κ**. For the Fibonacci Hamiltonian at
coupling λ the orbit starts at `((E−λ)/2, E/2, 1)` with `I = λ²/4`, and the spectrum is exactly
`{E : the orbit stays bounded}`.

The record fixes the object's invariant: **`κ(P₀) = 1+ω`, `ω = e^{iπ/3}`** — and
`1 + ω = 3/2 + i√3/2`, so `|κ| = √3` and `arg κ = π/6`, i.e. **`κ = √3·e^{iπ/6}`, exactly the value
`OPEN_PROBLEMS.md` Gate D names.** That will be verified in-cell as step 0.

So the coupling is **forced, not selected**: `λ² / 4 = 1 + ω`, i.e. `λ = 2(1+ω)^{1/2}` — complex,
so the cocycle is **non-self-adjoint**, which is precisely the gate's question.

## 1. The cells

### D-0 — arithmetic check, before anything
Verify `1 + ω = √3·e^{iπ/6}` exactly and that `I` is invariant under the trace map to machine
precision on random complex points. **If either fails the cell voids** and nothing below is run.

### D-1 — positive control · **BLIND**
At **real** λ > 0 (`I = λ²/4 > 0`, the Damanik–Gorodetski regime), the bounded-orbit set in `E` must
reproduce the known structure: a **Cantor subset of the real line, of zero Lebesgue measure**.
- **D1-REPRODUCES** — the real-λ set is totally disconnected, on ℝ, with measure shrinking under
  refinement.
- **D1-FAILS** — it does not, in which case **the instrument is wrong and no object result may be
  reported.** This gate is binding.

### D-2 — the object · **BLIND**
At the forced complex λ, compute the bounded-orbit set over a complex `E`-grid by escape time.
- **D2-STRUCTURED** — the set is a proper fractal subset of ℂ: empty interior, and box-counting
  dimension strictly between 0 and 2.
- **D2-DEGENERATE** — it is not: it has interior, or is empty, or collapses to a curve/line.

### D-3 — is the complexity the object's, or generic? · **BLIND**
The B996 lesson, applied in advance: run the same computation at **control κ values of the same
modulus** (`√3·e^{iθ}` for several θ, including θ = 0 which is real) and compare the dimension.
- **D3-SPECIFIC** — the object's θ = π/6 is distinguishable from same-modulus controls.
- **D3-GENERIC** — it is not, i.e. every complex κ of that modulus looks alike.

**Honest prior, stated:** I expect **D2-STRUCTURED** and **D3-GENERIC**. Complex trace maps
generically produce fractal escape sets, and this programme's own history is that structure
survives and specificity does not. Recording it so a D3-SPECIFIC result is not read as confirmation
of what I expected.

## 2. What this cell cannot conclude

- **A numerical picture is not a theorem.** It cannot prove or disprove a Damanik–Gorodetski-type
  result. What it can do is establish whether the object's cocycle even *has the shape* DG
  describes — a hyperbolic-looking, totally disconnected invariant set — which is the first thing a
  specialist would ask before spending time, and which nobody has looked at.
- **No Hermitian result transfers.** The record warns this explicitly, and memos 137/143–147 are the
  machinery it warns about. **Nothing from those memos is reused here**; the cocycle is rebuilt.
- It does not answer Gate D. It reduces the specialist's unknown from "is there anything there?" to
  a measured statement.

## 3. Gate 5

No measured physical value enters. κ is the object's own invariant, computed from ω.
