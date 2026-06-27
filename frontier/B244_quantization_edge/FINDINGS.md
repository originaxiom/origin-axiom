# B244 — the (1)↔(2) quantization edge: does SU(3)₂ see the 3 components of the SL(3,ℂ) character variety?

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Thread 2 of the trichotomy (B242). `quantization_edge.py` (pyenv); `sl3_volumes.py` (sage-python, SnapPy Ptolemy).

## The question
The trichotomy's (1)↔(2) edge: the classical **SL(3,ℂ) character variety** (B71: 3 components — V0 geometric=Sym²,
W1/W2 Dehn-filling) vs the quantum **level-rank `SU(3)₂`** (B238/B242). Does the `SU(3)₂` invariant "see" the 3
components?

## The honest answer: NO at level 2 — they are the classical saddles it quantizes
- The `SU(3)₂` fundamental invariant of `4₁` is a **single number** `−2/φ` (B242); it does **not** individually
  resolve the 3 components. Resolution into components is a `k→∞` (semiclassical) phenomenon — the asymptotic
  expansion of the WRT/colored invariant is a sum over flat connections (Witten/Gukov), **not** a level-2 fact.
- The **fundamental** rep cannot see the volume at all: `P_{4₁}(a=q³, z=q−q⁻¹) → 1` as `k→∞` (no exponential
  growth). Seeing the components needs the **large-color** limit (color `~k`; the SL(3) volume conjecture).

## What is computed — the classical saddles (the new piece)
Via SnapPy's Ptolemy variety (N=3; Garoufalidis–Thurston–Zickert), the figure-eight's boundary-unipotent SL(3,ℂ)
reps: obstruction class `c0` has **3 reps** (matching B71's 3 components), with **distinct complex volumes**:

> `V0` (geometric, `=Sym²` of the SL(2) discrete-faithful rep): `Vol = 8.11953285 = 4 × Vol(SL(2))` — exactly the
> `(n³−n)/6 = 4` factor at `n=3`. `W1, W2` (Dehn-filling): `Vol = 0`.

This **confirms B71's `V0=Sym²` identification through the volume**, and shows the 3 components are *geometrically
distinct saddles* (one carrying all the volume, two with none — `CS=0` throughout, the figure-eight being
amphicheiral).

## Verdict — the edge is quantization
The `SU(3)_k` WRT/colored invariant **quantizes** these three classical SL(3,ℂ) saddles; at the small level `k=2`
it is a single number that resolves nothing, and the components emerge only in the `k→∞` asymptotics (dominated by
the geometric `V0`, `Vol=8.1195`). So the (1)↔(2) edge of the trichotomy is the **classical↔quantum**
correspondence, and thread 2 computes its *classical* side (the three saddle volumes) — the answer to "does SU(3)₂
see the components" is **no at level 2, yes only asymptotically**. Firewall-clean. Anchors: B71/B99 (SL(3,ℂ) char
variety), B238/B242 (SU(3)₂ quantum), B240 (amphichirality → `CS=0`). Literature: Garoufalidis–Thurston–Zickert
(Ptolemy / SL(n) complex volumes); Witten, Gukov (WRT asymptotics = sum over flat connections).
