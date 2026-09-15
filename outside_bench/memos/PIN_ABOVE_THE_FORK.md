# PIN ABOVE THE FORK — both Gieseking-level structures restrict to the beat-selected spin structure, χ = −1 does not even extend as a character, and the spin selection acquires a THIRD independent derivation: pure H₁ arithmetic of t² = a
## (outside bench, 2026-08-25; thirty-sixth memo; campaign cell A4; every claim exact)

### The question (one level above memo 28)
Memo 28 settled the two spin structures on the orientable M = m004. The Gieseking N —
whose deck symmetry IS the beat — carries its own ℤ/2-torsor of Pin-level structures.
Preregistered two-outcome: the restriction map H¹(N;ℤ/2) → H¹(M;ℤ/2) is an
isomorphism (the Pin bit is the spin bit in disguise) or the zero map (a genuinely
new bit; and then WHICH spin structure the upstairs structures land on becomes a
sharp question).

### THE THEOREM (`certificates/a4_pin.py`, standalone; holonomy identities re-verified in-run)
With Γ = ⟨a,b | R⟩ and Γ_G = ⟨a,b,t | R, tat⁻¹ = a, tbt⁻¹ = β(b), **t² = a**⟩ —
the last relation forced by faithfulness: (W·gal)² = W·conj(W) = A exactly, the
memo-16/28 identity, re-verified — exact Smith-form arithmetic gives:
1. **H₁(Γ) = ℤ** (relator abelianizes to a = b); H¹(M;ℤ/2) = ℤ/2 — the two spin
   structures, as banked.
2. **H₁(Γ_G) = ℤ⟨t⟩ with a = b = 2t** (β is homologically trivial — letter counts
   verified); H¹(N;ℤ/2) = ℤ/2 — exactly two Pin-level structures upstairs.
3. **The restriction map is ZERO**: every ℤ/2-character of Γ_G kills a = 2t and
   b = 2t. **Both upstairs structures restrict to χ = +1 — the beat-selected spin
   structure.** The genuinely new bit is the t-sign (which structure upstairs), and
   it lives entirely over the selected side.
4. **The obstruction, cohomologically bare:** χ = −1 extends to Γ_G iff χ̃(t)² =
   χ(a) = −1 has a solution in {±1} — it has none. χ = +1 extends in exactly two
   ways (χ̃(t) = ±1: the Pin-level pair).

> **Memo 28's selection theorem now has three independent derivations: the exact
> intertwiner/norm-form route (memo 28), the rep-level closure on matter (memo 29),
> and now the H₁ arithmetic of the extension — one line deep: t² = a and a is odd
> in H₁(N), so the odd character cannot climb. The deepest form yet: the beat
> selects χ = +1 because the meridian is twice the Gieseking generator.**

### Fences
Exact throughout; the presentation of Γ_G rests on t² = a, which is *derived* (faithful
holonomy + the verified matrix identity), not assumed. Terminology per memo 28's
red-team fence: what lives on N are Pin-type structures (a non-orientable manifold has
no spin structure); this memo's computation is character/H₁ arithmetic — the torsor
count and restriction behavior — and does not construct Clifford-bundle data. The
codex internal-A1 fence (B1145) is inherited wherever "spin" is read physically.
Gate 5 untouched.

### Certificates
`certificates/a4_pin.py` (standalone — no machinery imports); output
`outputs/a4_pin_out.txt`.

### One sentence for the ledger
One level above the fork nothing splits: both structures on the object's non-orientable
self restrict to the single spin structure its beat already chose — because the
meridian is 2t upstairs — and the only new freedom is the sign of the beat itself,
a bit the selected side carries whole.
