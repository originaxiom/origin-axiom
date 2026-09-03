# B1242 — L199 closed: both priced identifications paid, and both came back NO

**2026-09-03 · cc (banking) · Gate 5 untouched — no measured value appears anywhere in this arc.**

L199 registered two identifications with an explicit price each. Both prices are now paid. **Both
answers are refutations** — and the ratchet drops 10 → 8 **by earning the answer, not by relabelling**,
which is the only way the B1231 ratchet was ever meant to fall.

## (a) I-16 — SU(4)₁ ≡ the silver's stage. **REFUTED.**

The price L199a set, verbatim: *"compute the silver cusp lattice's discriminant form and compare with
A₃'s (ℤ/4, q = 3/8): equal ⇒ a map to exhibit; unequal ⇒ REFUTED."*

| | silver cusp lattice | A₃ |
|---|---|---|
| shape | τ = 2i (\|τ²+4\| = 1.8e−15 double, 4.0e−63 quad) | — |
| Gram | odd, diag(1,4), \|D\| = 4 → **no quadratic discriminant form at all** | — |
| minimal even rescaling | 2x²+8y²: **(ℤ/2 ⊕ ℤ/8)**, level **16**, sig **2**, **16** anyons, ord(T) = 48 | **(ℤ/4, q = 3/8)**, level **8**, sig **3**, **4** anyons, ord(T) = 8 |

**Unequal on every invariant checked.** And it cannot be rescued: even scalings c·diag(1,4) give
\|D\| ∈ {16, 64, 144, 256} — **never 4** — and every rank-2 positive-definite form has signature 2 by
Milgram — **never 3**.

**B675's number was right; it was not a lattice invariant.** A₃'s ord(T) = 8 reproduces exactly.
"Conductor 8" named the **shadow level 8**: the order ℤ[2i] has conductor f = 2 and disc −16, and the
lattice level is 16.

**The structural root cause, and it generalises.** A₂'s Coxeter plane ℤ[ζ₃] **is** the A₂ root lattice,
so the golden case genuinely works. A₃'s Coxeter plane ℤ[i] is **A₁⊕A₁**, not A₃. Extrapolating from
rank 2 — where plane = lattice — to rank 3, where it is not, is exactly where a computation became an
identification. **Golden control run:** the golden cusp's own even form has \|D\| = 48 against A₂'s 3, so
even there the *cusp lattice* does not carry A₂'s form; what works is the *plane*.

## (b) I-15 — E₆(ℂ) CS ≡ 3d gravity. **REFUTED as "≡"; the containment EARNED as I-19.**

The price L199b set: *the Dynkin index of the principal sl₂ ⊂ e₆ tying the E₆ invariant to Vol + i·CS
with a computed coefficient.* **Computed: 156, by three independent routes that agree.**

```
route 1 (adjoint):  sum_i I(V_2e_i) / I(78) = 3744 / 24 = 156
route 2 (the 27):                              936 /  6 = 156
route 3:                            2(rho,rho) =            156
```

Therefore **CS_{E₆}(φ∘ρ) = 156 · CS_{SL(2,ℂ)}(ρ)**, remainder **identically zero** — the map is exhibited
and it **acts**. All sl₂ weights on the 27 and 78 are even, so it factors through PSL(2,ℂ) = Isom⁺(H³)
(B428 re-derived). **B715's tr Ad(ρ(a)) = 37437270 + 38799960√3·i reproduced exactly.**

**But the identity fails by counting.** Under the principal sl₂, **78 = 3 + 9 + 11 + 15 + 17 + 23**. The
spin-2 (gravity) sector is **3 of 78**; the other five carry sl₂-spins 4, 5, 7, 8, 11 — Drinfeld–Sokolov
higher-spin weights (a **cited** framing). E₆(ℂ) CS is not 3d gravity; it **contains** it.

## What is NOT disturbed

**Both corrected arcs keep their verdicts.** B675 stays PROVED (τ = −2i, ℚ(i), the index-2 ℤ[i]-equivariant
embedding, the A₂/A₄ exclusions, index = conductor). B715 stays PROVED (its non-real adjoint trace, hence
no real form). **B684/LAW_MAP:53's OWN-CHANNEL at SU(4)₂ — level 2 — is untouched by this.** Corrections
reached both verdict files and both got addenda at source (E53 discipline: a correction that reaches only
the log has not been made).

## Flagged NON-claim, at zero weight

The silver even form's **ord(T) = 48** coincides with **SU(4)₂'s** ord(T). Anyon counts 16 vs 10, c ≡ 2 vs
5 — not the same theory. Recorded so the next reader meets it already dismissed.
