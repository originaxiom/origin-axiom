# xB029 — THE G₂-MSSM READ AT SOURCE: the source's arithmetic reproduces, its visible sector is assumed rather than derived, and a computational gap it names is half-closed by machinery this record already owns

**Seat `xb`, `sep16-branch`, 2026-09-18. PREREGISTRATION sealed at `9150fe94` before any cell existed.**

**B. S. Acharya, K. Bobkov, G. L. Kane, P. Kumar, J. Shao, *The G₂-MSSM — An M Theory motivated model
of Particle Physics*, arXiv:0801.0478v2** (MCTP-07-43, UCB-PTH-08/01). **The owner supplied the PDF.**
**UNCITED → READ-AT-SOURCE.** The record cites Acharya–Witten and Acharya hep-th/0212294; **it has
never cited this paper.**

---

## G1 — THE SOURCE'S OWN ARITHMETIC REPRODUCES

| check | source says | recomputed | |
|---|---|---|---|
| **eq. (8)** `P_eff = 28(Q−P)/(3(Q−P)−8)` at `Q−P = 3` | **84** | **84.0** | exact |
| the same at `Q−P = 4` | **28** | **28.0** | exact |
| the family `Q−P = 3…8` | *"for larger `Q−P` the `P_eff` required … is smaller"* | `84, 28, 20, 16.8, 15.08, 14` | monotone ✓ |
| **Appendix A worked example** `P=15, Q=18, M=10, λ=80, k=99` | **`P_eff = 58`** | **59.74** | within rounding ✓ |
| `N < 14Q/((3(Q−P)−8)π)` at `Q=18` | shrinks with `Q−P` | `80.2, 20.1, 11.5, 8.0` | ✓ |

**And one thing the recomputation shows that the source's prose does not.** In their own example,
**`log k` contributes only `4.60` of the `59.74` — 7.7 %. The other 92.3 % comes from the tuned flat
connection**, because `G·λ = 26 × 80 = 2080 ≡ 1 (mod 99)`, putting `4sin²(Gπλ/k)` at its smallest
non-zero value. **Their "large `k` is needed" is really "`k` large AND `λ` tuned so that `Gλ ≡ ±1`
(mod `k`)" — a one-in-`k` coincidence.** Solving their own formula for `P_eff = 84` at `M = 10` gives
**`k ≈ 316`**.

---

## G2 — WHAT THE SOURCE ASSUMES, IN ITS OWN WORDS

| the visible sector's… | the source's own sentence |
|---|---|
| **GUT group and its breaking** | *"In our analysis henceforth, we will **assume** a GUT gauge group in the visible sector which is broken to the SM gauge group, with at least an MSSM chiral spectrum, by background gauge fields (Wilson lines)."* |
| **chiral spectrum — hence the count of three** | same sentence: *"with at least an MSSM chiral spectrum"* |
| **the conical singularities that carry it** | *"The observable sector three-manifold is **assumed** to contain conical singularities at which chiral matter is supported."* |
| **the Yukawa couplings** | *"…it is very difficult technically to compute the Yukawa couplings quantitatively. Therefore, for our phenomenological analysis, we will **assume** that the (normalized) Yukawa couplings are the same as those of the Standard Model."* |
| **the hidden sectors** | *"We **assume** that the G₂ manifolds which we consider have singularities giving rise to two non-Abelian, asymptotically free gauge groups."* |
| **the landscape that tunes Λ** | *"we have **assumed** effectively that the space of G₂ manifolds scans `P_eff` finely enough such that vacua exist with values of the cosmological constant as observed."* |
| **whether the manifolds exist at all** | *"very little is known in general about the set of all compact G₂ manifolds … there do not currently exist any concrete ideas about that space either!"* and, in the conclusions, *"one of the most outstanding problems is to construct global examples of G₂ manifolds with the right structure of conical and orbifold singularities. **This would require a major breakthrough from a mathematical point of view.**"* |

**The sealed prediction holds: all four of the GUT group, the Wilson-line breaking, the MSSM chiral
spectrum and the Yukawas are ASSUMED. None is derived.**

**The calibration, stated at its correct width.** This seat's standing negatives are a generation
count **fixed at one and never three** (xB026) and **no derived value** anywhere. **Those are the
field's open problems, not this seat's peculiar failure** — the leading M-theory-on-G₂ phenomenology
programme assumes exactly them. **And that is a calibration, not a licence.** An assumption shared
with the literature is still an assumption; **nothing here moves Gate 5, and the record's own
negatives stand exactly as they stood.**

---

## G3 — THE TORSION LEAD: all four sealed conditions met, exactly

Appendix A, eq. (A3), verbatim: *"`S = S′ + 2N_c log(Vol(Q̂)Λ³_cutoff)`, where `Vol(Q̂)` is the volume
of the hidden-sector three-manifold `Q̂` and **`S′` can be expressed in terms of certain topological
invariants of `Q̂`, known as the "Ray-Singer analytic torsion"**."* Computed there **only for lens
spaces**, with `T_O = −log k`, `T_λ = log(4sin²(Gπλ/k))`, `P_eff = −T_O − M·T_λ` (A12) — and the
source's own limitation, verbatim: *"**at present it is not known how to compute the torsion for other
three-manifolds**, it is possible that a large `P_eff` can be obtained more "naturally" in other
examples."*

Measured on the record's own tower `b++(LR)ⁿ` (xB027's driver), `n = 1…120`:

| sealed prediction | result |
|---|---|
| `\|Tor H₁(Xₙ)\| = L₂ₙ − 2` exactly | **120 of 120, zero mismatches** — `1, 5, 16, 45, 121, 320, 841, 2205, …` |
| growth constant `log α = 0.9624236501` per degree | **measured `0.962423650`; relative deviation `0.000e+00`** |
| first `n` with `log\|Tor H₁\| ≥ 84` is **88** | **88** (`n=87 → 83.7309`, `n=88 → 84.6933`) |
| vacuity control: torsion grows, `n=1` torsion-free | **both hold** (`H₁(m004) = ℤ`) |

At the crossing the cusped volume is `88 × 2.029883 = 178.63`. **Under the Bergeron–Venkatesh closed
rate `1/(6π)` the same 84 would need volume `1583.4` — a factor `8.86` more.** The tower's rate is set
by the **Mahler measure of `t² − 3t + 1`**, not by a volume law.

---

## G3b — FENCE 2, MEASURED — AND THE SEAT'S SEALED PRIOR ON IT IS WRONG

The preregistration declared: *"this seat expects FENCE 2 to be the one that bites"* — that the
attractive rate would be a property of the **cusp**, while `Q̂` must be **compact**.

**It does not bite.** Searching closing slopes (`b₁ = 0`) on each `Xₙ`: **for every `n` from 2 to 18 a
closed filling exists whose `|H₁|` is EXACTLY `L₂ₙ − 2`**, hyperbolic from `n = 3` on, at volumes
**strictly below** the cusped ones (`n=18`: `34.68` against `36.54`). **Calibration in front:** `n=2`
gives `|H₁| = 5` — the 2-fold branched cover of the figure-eight is the lens space `L(5,2)` — and
`n=3` gives `16`. **The growth rate is not a property of the cusp.**

### Two of this arc's own cells were void, and both are recorded rather than overwritten

- **v1 VOID.** It filled the meridian **before** covering. That gives `S³`, which has no covers, so
  the cell printed *"no cover"* eleven times and **measured nothing while reporting a result shape.**
- **v2 VOID.** It covered first, then filled `(1,0)`. That worked at `n = 2,3`; **for `n ≥ 4` the
  filled manifold still had `b₁ = 1`** — `(1,0)` is the homological longitude there and the fill
  killed nothing, so the "closed `|H₁|`" column was the **cusped torsion reprinted** and its
  *"19 of 19"* was **contaminated**. **The `b₁` column caught it**, and it was only in the printout
  because the cell happened to print it.

---

## THE VERDICT

**What is established.** The source's arithmetic reproduces (G1). Its visible sector — GUT group,
Wilson-line breaking, MSSM chiral spectrum, Yukawas — is **assumed in its own words** (G2). The
**`T_O` term** of its `P_eff` is **exactly computable** on a hyperbolic family this record already
owns, with an exact closed form, an exact growth constant and an exact crossing degree (G3), and the
**compactness fence does not obstruct it** (G3b).

**What is NOT established, and each of these is load-bearing.**

1. **The generalisation `T_O = −log k ⟶ −log|Tor H₁(Q̂)|` IS THIS SEAT'S INFERENCE FROM ONE WORKED
   EXAMPLE, NOT A STATEMENT THE SOURCE MAKES.** The source gives `T_O` for lens spaces only. **This
   is precisely the proxy-for-predicate move that killed xB023 Addendum 1 three commits ago**, and it
   is flagged here in the same breath as the result rather than after it fails.
2. **The `T_λ` term is NOT computed.** Ray–Singer torsion of a **non-trivial flat bundle** on a
   hyperbolic 3-manifold is untouched here. **The source's gap is HALF-closed, not closed.**
3. **`P_eff` itself is not computed for anything.** It needs `C₁/C₂` — **both** hidden sectors, their
   volumes and a cutoff. None of that exists here.
4. **THE TRADE IS NOT SHOWN TO BE FAVOURABLE.** The lens route needs `k ≈ 316` **plus** a
   one-in-`k` tuning. The torsion route needs **no tuning** but `|H₁| ≈ 3 × 10³⁶` — an 88-fold cover.
   **That is a different largeness, not the absence of one**, and this arc does **not** claim the
   exchange is an improvement.
5. **SECTOR.** `P_eff` is a **hidden-sector** quantity; the closing puts the object in the **visible**
   sector (L220/L221). **A number on the object's tower is about a different three-cycle.**
6. **The post-2008 experimental status** of this paper's predictions (light gauginos, sub-TeV gluinos,
   wino LSP) is **not settled here** and is registered as **OPEN**, not answered from memory.

**Registered as L225.** **No value. No generation count. No physics reading. Gate 5 absolute.
Nothing to `CLAIMS.md`.**

## SCORING THE SEAT'S PRIOR

G1 reproduces **(correct)** · G2 confirms and reads as a calibration **(correct)** · G3's closed form
holds and the crossing is 88 **(correct)** · **"this seat expects FENCE 2 to be the one that bites"
— WRONG; it does not bite** · "the best outcome is a well-posed lead and a corrected register, not a
bridge" **(held to)**. **Four for five, with the miss on the one prediction that was about this
seat's own judgement rather than about the mathematics.**
