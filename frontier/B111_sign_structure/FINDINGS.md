# B111 — the tower's sign structure + the degree=rank exponent (the opposition involution vs the tower)

**Status: `computer-assisted` + symbolic.** Banks the CC-web "sign findings" handoff + the supplement (ADDITION
1/2). The headline: **the tower's sign/multiplicity structure is the opposition-involution closed form, except for
a single degree=rank promotion** — which names both halves of the `ρ_n` prize. NO physics; no `CLAIMS.md`
promotion; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched. Script `probe.py`;
test `tests/test_b111_sign_structure.py`.

## PART 0 — the SL(3) sign rule (engine-free)
`char(J)` at the trivial rep, factored:
- **metallic** (`det N = −1`, `m=1,2,3` identical): `char(M⁻¹)·char(M²)·char(M³)·(t−1)(t+1)`.
- **figure-eight** (`det N = +1`): `char(M²)·char(M⁴)·char(M⁶)·(t−1)²`.

**Correction (verify-don't-trust).** The handoff's parity rule `(t−1)(t+det N)` is **wrong**; the computed parity
is **`(t−1)(t − det N)`** (`det=−1 → (t−1)(t+1)`; `det=+1 → (t−1)²`). The signs are **det-determined, not
m-determined** (the three metallic m give identical structure). `s₂=+1` is SL(3)-specific (SL(4)+ carries
`char(−M²)`).

## The opposition-involution all-heights CLOSED FORM
The `θ = −w₀` action on each height-`h` root space of `A_{n−1}` gives, in closed form,
```
   mult char(M^h) = ⌈(n−h)/2⌉,   mult char(−M^h) = ⌊(n−h)/2⌋,   h = 1 … n−1;
   net (+)-over-(−) char excess = ⌊n/2⌋.
```
Verified against **B62's published height-2 splits** `(1,0), (1,1), (2,1)` at `n=3,4,5` (B62 had only height 2;
this is the all-heights generalization), computed `n=3..12`.

## PATH B / C — the closed form vs the proved tower: the **degree=rank promotion** (the key result)
Diffing the closed form against the **exact repo tower** (`n=3` Lawton Jacobian; `n=4` B80 `_Jm_n4_exact`), using
the `det=−1` identity `char(M^{−h}) = char(−M^h)` (odd `h`), `= char(M^h)` (even `h`):

> **`Tower(n) = [θ closed form, heights 1 … n−1]` with exactly ONE `char(M¹)` promoted to `char(Mⁿ)`.**
> *(verified `n=3,4`, dimension-neutral.)*

The single non-bulk ingredient is **`char(Mⁿ)` — the degree=rank top power**, the longitude `L = c·Mⁿ` (B83/B89):
the meridian `char(M)` is promoted to the longitude `char(Mⁿ)` *inside* the tower. **Decision (the most-leveraged
computation, done first):** the tower's **sign half IS the closed form** (bulk `θ`), and the **only** piece `θ`
does not supply is `char(Mⁿ)` = degree=rank (the peripheral thread). **Both halves of the `ρ_n` prize are now
named:** (i) the bulk `θ`-multiplicity law (closed form), (ii) the single degree=rank promotion `M → Mⁿ`.

## ADDITION 1 — `M^k` scalar/non-scalar: the exponent's algebraic constraint (proved negative)
Pure eigenvalue arithmetic on each component's cusp (meridian) spectrum:
- **SL(4) secondary** (primitive 8th roots `{ζ,ζ³,ζ⁵,ζ⁷}`): `M⁴ = ζ⁴ = −1` is **SCALAR** ⇒ `[A,B] = c·(−1)·Id` is
  trivial ⇒ **`k=4` is ALGEBRAICALLY IMPOSSIBLE**; `k=3` (non-scalar, permutes the eigenvalues) is **forced**.
- **SL(4) principal** (`{1,1,ω,ω²}`): `M³` is scalar but `M⁴` is **non-scalar** ⇒ `k=4` is **allowed**.
- **SL(3) W1** (`{1,i,−i}`): `M⁴` scalar, `M³` non-scalar (the exponent).

This **proves the negative characterization** — *why* `k≠4` on the secondary and *why* `k=4` is allowed on the
principal. **Honest scope (DO-NOT):** it does **not** prove `k=n` on the principal (only *allowed*, not *forced*).

## ADDITION 2 — the cusp order pattern + the `ord−1` TESTED-NEGATIVE
The cusp eigenvalue orders are **`{n−1, n+1, 2n}`** on the three component types (SL3 W1 `ord=4=n+1`; SL4
principal `ord=3=n−1`; SL4 secondary `ord=8=2n`). The simple formula `k = ord−1` **FAILS the all-four hinge** (OK
at SL3, FAIL at SL4 principal and secondary) → **TESTED-NEGATIVE** on `ord−1`. Path A is the right direction; the
specific formula is open.

## Covering degree (A1d) — the candidate positive mechanism (a hypothesis)
The covering map `(cusp parameter μ) ↦ L = c·M^k`: at the **eigenvalue level** `μ ↦ μ^k` is `k`-to-1, so the
covering degree `= k` on all four components (**consistent with** the "mechanism = Weyl-orbit covering degree"
hypothesis). **Honest:** this is the eigenvalue-level degree; whether the **full component covering** (with the
`SL(n)` + Weyl constraints) is exactly `k` needs the character-variety covering map — the **open** part. Logged as
a **hypothesis**, not a solved mechanism.

## `s_n ↔ c` bridge — DEAD
`s_n ∈ {±1}` (order ≤ 2) cannot equal the order-4 secondary `c=i` — the **same parity obstruction** that killed
`θ→c` (B108). Banked DEAD (not a new problem).

## Verdict
The tower's sign structure = the opposition-involution closed form **plus one degree=rank promotion**
`char(M) → char(Mⁿ)`; the exponent `k` is algebraically constrained (the `M⁴`-scalar impossibility forces `k=3`
on the secondary); the simple cusp-order formulas fail; the covering-degree mechanism is a partial-positive
hypothesis. The `ρ_n` prize is now split into a **closed-form bulk half** and a **degree=rank peripheral half**.

```bash
python frontier/B111_sign_structure/probe.py
python -m pytest tests/test_b111_sign_structure.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
