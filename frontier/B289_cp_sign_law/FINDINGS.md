# B289 — Is the CP sign forced? The CS sign law and its ℚ(√−3) Galois meaning

**Status: banked. Math (CS sign law + Galois reading) verified two methods; physics firewalled; nothing to
`CLAIMS.md`.** Phase II of the seam arc (wall #3, chirality/CP). B286 found the cusped object amphichiral (`CS=0`)
and generic closings chiral with `CS(p,−q)=−CS(p,q)` on a sample; B289 makes it robust and reads its meaning.

## Four findings
1. **Forced sign law (mechanism — POSITIVE).** Over **all 78 hyperbolic closings** `(p,q)`, `|p|,|q|≤8`, `gcd=1`:
   every closed manifold is **chiral** (`CS ∉ {0,½} mod 1`) and obeys **`CS(p,−q) = −CS(p,q)`** exactly. The
   **oriented slope forces the CP sign.** Two methods agree (mod ½): `chern_simons()` and
   `Im(complex_volume)/(2π²)` — `78/78`.
2. **Amphichiral locus empty.** No hyperbolic closing has `CS ∈ {0,½}` — **closing always breaks amphichirality/CP**.
3. **Handedness = ℚ(√−3) Galois conjugation (structural — POSITIVE).** The mirror slope `(p,−q)` realises **complex
   conjugation of the geometric holonomy** (orientation reversal → `CS → −CS`). At the cusp this complex conjugation
   is the nontrivial element of `Gal(ℚ(√−3)/ℚ)`: it swaps the two Riley roots `u ↔ u²`, which is **exactly** the
   involution that flips B285's commutator phase `κ = u²+2 = √3·e^{∓iπ/6}` between `+π/6` and `−π/6` (the
   `τ`/amphichirality swap). So the **closing's `CS` sign and the cusp's `±π/6` sign are two faces of the same
   `ℚ(√−3)` involution.** (The `verdict.py` recomputes the `±π/6` flip in sympy.)
4. **But the sign is not object-derivable (NEGATIVE on forcing).** The object is amphichiral (`CS=0`) and CP-symmetric
   — it delivers `±π/6` symmetrically (B252/B285). The closing forces **a** sign; **which** sign is the
   external/seam choice (the `τ`-fork).

## Two methods (verify-don't-trust)
- **`chern_simons()`** (the SnapPea CS, mod 1) and the independent **`Im(complex_volume)/(2π²)`** (the Cheeger–Chern–
  Simons imaginary part, mod ½) agree on all 78 closings (mod ½, the complex-volume normalization). The earlier
  per-run `mod 1` mismatches on a handful were a complex-volume precision artifact; the **sign law is `78/78`
  via `chern_simons`** regardless.
- The Galois half is **recomputed symbolically** (sympy): `κ = u²+2` at `u = ω, ω²` gives `arg = ∓π/6`, the Galois
  sign swap.

## Where this lands (the matter map, one of three pieces)
This is the **CP-sign** piece of the seam's contribution to a Sakharov-style "where matter comes from" picture:
- **magnitude** `π/6` — forced in the **bulk** by the `ℚ(√−3)` arithmetic (B285);
- **sign** — forced to **exist** at the **seam** (the oriented closing, B289), via the same `ℚ(√−3)` involution;
- **which** sign — **not** object-derivable (the `τ`-fork); and the baryon **magnitude** — external (freeze-out, S005
  HELD). One of three forced; firewalled.

## The fence
Pure topology/arithmetic. The "CP → baryon asymmetry" reading is **HELD/[LEAP]** in `speculations/`; the sign choice
is the `τ`-fork, explicitly **not** banked. The object is CP-symmetric; B289 shows the *closing* breaks it with a
forced sign *law*, not a forced sign. Nothing to `CLAIMS.md`.

`cp_sign_law.py` (sage-python: SnapPy CS census, sign law, amphichiral search, complex-volume cross-check) ·
`verdict.py` (pyenv; recomputes the B285 ±π/6 Galois flip) · `tests/test_b289_cp_sign_law.py`. Related: `B286` (the
seam), `B285` (the ±π/6 magnitude), `B282` (ℚ(√−3) atom), `B252` (CP-symmetry), `B271` (τ/amphichirality), `B250`
(complex volume), `B287`/`B288` (the other selection axes).
