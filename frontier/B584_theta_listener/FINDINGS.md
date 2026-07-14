# B584 — Round 3: THE LISTENER — the golden amplitude is entirely θ-odd

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; no SM quantities
(the B580 binding rule); firewall intact. Preregistered (PREREGISTRATION.md),
computed blind, locks green (`tests/test_b584_theta_listener.py`, 5 pass).**
Run: `python3 theta_listener.py` (pyenv, ~1 s; reuses B238 + B245 machinery).

## The question (fixed by X3's theorem, and the owner's proposal)

X3 (B583): the vacuum is C-fixed and [C,S] = [C,T] = 0 — filling/vacuum probes
never hear the θ-odd sector. So **what is the minimal nontrivial listener?** The
owner proposed: the object's mirror.

## The answer — the mirror in ANTIPHASE, and it hears everything

**1. The mirror alone is deaf (R3-3, computed).** A bare knot state has
components J_λ(K), and dual color = same invariant: on su(3),
`J_3(4₁) = J_3̄(4₁)` exactly (B245's validated IMMM formulas, `H^sym_[1]` vs
`H^antisym_[1,1]` at `A=q³`, 8 generic points, agreement to 1e-15). So every
bare knot state — the object's AND the mirror's — has **zero θ-odd component**:
the third unhearability (bare knots, not just vacua, are θ-even sources).

**2. The nontrivial listener is the antiphase mirror channel (R3-2, the
operational identity).** The θ-odd states are `u_λ = (e_λ − e_λ̄)/√2` — object
minus mirror in superposition. Since `P_odd = (1−C)/2`:
> **tr_odd ρ = ½ ( Z − Z_C )**, `Z_C = tr(C ρ)` = the C-twisted (mirror-glued)
> bundle amplitude.
Listening to the θ-odd voice = playing the bundle twice — once plainly, once
mirror-twisted — and taking half the difference. This is B582's mirror-double
made operational on the stage.

**3. The BLIND result (R3-1): on the golden stage SU(3)₂, the θ-odd listener
hears the ENTIRE invariant.**
> `tr_even ρ(RL) = 0` exactly; `tr_odd ρ(RL) = −1/φ` — **all of the banked
> Z = −1/φ (B238) is θ-odd.** `Z_C = +1/φ` (the mirror-twisted play is the
> plain play with the sign flipped).
The θ-odd 2×2 block is the **order-10 golden rotation**: eigenvalues
`e^(±3πi/5)` (primitive 10th roots), trace `2cos(3π/5) = −1/φ`, det 1. The
θ-even 4-dim block is a **silent order-20 clock**: eigenvalues
`e^(±iπ/10), e^(±9iπ/10)` — two conjugate pairs that cancel exactly (trace 0).

**4. The level-rank re-read (one number, two opposite sectors).** On SU(2)₃
every rep is self-dual, C = 1, there IS no θ-odd sector — the same value −1/φ
is trivially all-θ-even there. The level-rank pair SU(2)₃ ↔ SU(3)₂ (B238,
shared κ = 5) realizes **one number in two opposite parity sectors**: all-even
on one side, all-odd on the other. Consistent with level-rank = conjugation
(B242/B243) now seen at the sector level.

**5. E₆ level 2 (R3-4, cited from banked C3).** The θ-odd 3-space block has
char poly (λ−1)(λ²+1): listener amplitude tr = 1, order 4. So the listener's
clock is **stage-dependent**: order 10 (golden, SU(3)₂) vs order 4 (E₆₂) —
cf. L77's θ-odd clock orders.

## Reading (firewalled)

The chord's law sharpens: chirality is heard only by an observer holding the
object and its mirror in antiphase — and on the golden stage that listener
hears *everything*: the figure-eight's golden amplitude is not partially θ-odd,
it is θ-odd outright, while the θ-even channel carries a perfectly cancelling
silent clock. The value −1/φ that has recurred since B204 was, on this stage,
always the chiral channel's voice.

## Gates and discipline

Banked gates reproduced: modular gate green; Z = −1/φ (B238); C central,
|S²| = C (B238's normalization carries a global sign: S² = −C — recorded);
even/odd decoupling exact (off-blocks ~1e-15). Prereg falsifiers: "odd block
trivial" did NOT fire; "J_3 ≠ J_3̄" did NOT fire. MB13 sweep done pre-prereg
(B238/B242/B243/B245/C3/B580-R1/X3 found and reused — no rediscovery).

## Anchors

B238 (stage + Z = −1/φ), B570-C3 (E₆₂ odd block), B583-X3 (second
unhearability), B582 (the mirror-double play), B245 (colored formulas),
B242/B243 (level-rank = conjugation), L77 (the θ-odd clock).
