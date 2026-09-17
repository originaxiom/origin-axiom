# xB009 — the odd sector is NOT the door: √−3 cancels there too, and its whole content is one already-known bit

**Status: banked (frontier, `sep16-branch`). Verdict NEGATIVE.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE any cell ran** — sha256
`5d8ea291aba92cd9d92d1a0878095a26c4a9d41f6a42775b562656ce312c8159`, committed `ba60fac`.
**Short by instruction:** the owner has ruled that a negative is not a deliverable, and the seal
committed this arc to one paragraph if it came back empty. It came back empty. Gate 5 untouched.

## The result against the sealed criteria

| cell | sealed criterion | outcome |
|---|---|---|
| **C0** | B425's own validations must reproduce on this port | **PASS** — relator forces `u²+u+1` (as a factor of `u⁴+u²+1`), trivial rep gives `t²−3t+1`, adjoint regularises to **−3**, even-sector Galois invariance holds |
| **O1** | does the odd lift exist, how many? | **PASS** — `ρ_geo` is already `SL(2,ℂ)`-valued, so `Sym^n` is defined for all `n`; `H¹(M;ℤ/2) = ℤ/2` gives **exactly two lifts**, differing by the sign character `ε` |
| **O2** | **THE HEADLINE** — does `√−3` survive for odd `n`? | **NO. Prior WRONG.** Galois-invariant at `n = 0…7`, odd and even alike: `√−3` **cancels** in the odd sector too |
| **O3** | does odd separate m003/m004? | **YES** — odd separates, even does not |
| **O4** | how much does it carry? | **exactly one bit** |

## The one paragraph

**My sealed prior for O2 was wrong.** B425 found `√−3` present in the Fox matrix and cancelling in
every even determinant; I predicted the cancellation would fail for odd `n`, because even/odd is a
Galois/duality split. It does not fail. **The Fox determinant is Galois-invariant at every `n` from
0 to 7** — the odd sector carries **no new field**. O3's separation is real but empty: the entire
difference between m003 and m004 in odd `Sym^n` is the substitution **`t → −t`** and nothing else
(verified `n = 1, 3, 5`), which is the sign character `ε` of O1 — **exactly one bit, and the same
bit xB007 already identified as knot-ness, `det(φ_*−I) = ±1`.** The trace numbers that appear,
`3, 7, 18, 47, 123, 322`, are **Lucas `L₂, L₄, …, L₁₂`** — golden by construction, B423's dynamical
side, not new arithmetic either. **So the odd sector sees the sign, as designed, and carries
nothing beyond it. This seat's reading of xB007 was over-optimistic, exactly as the seal named in
advance, and the direction is closed.**

## One correction of this seat's own, made before anything shipped

A first draft of O4 printed *"THE ODD SECTOR IS GENUINELY NEW INFORMATION"* on the strength of
separation alone. **That was overstated.** Separation says the odd sector sees something the even
cannot; it does **not** say the something is large. O4 now **measures** it — `t → −t`, one bit — and
says so. The E33 shape (over-correction's mirror: over-claiming from a true-but-thin result) caught
in the same session it was written.

## What is NOT claimed

The temptation the seal fenced against — *odd sector = spin = 4d spinor = matter* — is **not**
claimed, and is now moot: there is nothing in the odd sector to carry across. No identification is
made, no ledger row opened, `creates_law` false, nothing to `CLAIMS.md`, F2 or Gate 5.

**Provenance.** `verification/odd_sector.py` (C0, O1–O4) → `reproduce.sh`. **Reuses B425's own
validated machinery unchanged** — `sym_power_mod`, `eval_TA_at`, `geom_TA`, `galois_invariant` are
general in the exponent and were only ever *called* with even arguments; nothing in B425 was
modified. Cross-refs B425 (the even computation and its controls), B423 (the dynamical/golden
side), B1242 (the 27 and 78 are even), xB007 (the sign, and the lead this arc tests and closes).
