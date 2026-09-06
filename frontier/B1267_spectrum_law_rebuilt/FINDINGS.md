# B1267 — THE SPECTRUM LAW REBUILT FROM THE REPOSITORY'S OWN 27, AND EXTENDED: B1086's named residual paid, the 27̄ rows computed, and the subregular double never reaches three

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact throughout; ranks over ℚ(ω) by two-prime modular reduction, the single-manifold rows also by exact elimination over ℚ(ω); every group element a polynomial in a nilpotent — no floats anywhere) · **Price: unchanged at 14**

## Why this arc — the residual B1086 named and nobody paid

**B1086** banked the spectrum law, `h¹(D_t; 27) = 5` for the untwisted and θ-even dials and **`2` for the θ-odd
dials**, on the outside bench's certificate, and named its residual exactly: *"an own-code rebuild of the dial
matrices themselves (the e-centralizing highest vectors hv8/hv16); until then the twisted rows rest on the
verified certificate + the B634 corroboration."* Nineteen days and ~180 arcs later the certificate is still
outside the repository (`frontier/B1087_charge_grading/b1087_grading.py` reads it from a scratchpad path), the
twisted rows have never been recomputed on a repository instrument, and **MAIN_GOAL JOIN 1** rests on them.

This arc rebuilds everything from the one exact object the repository does hold — **B883's `rep27.json`**, the
78 integer 27×27 matrices of e₆ on the 27 — with no reference to the certificate.

## 1. The instrument (`verification/e6_instrument.py`)

| what | result |
|---|---|
| B854's Chevalley bracket re-implemented; `rep27.json` checked to BE a representation | ρ([x,y]) = [ρx, ρy] on 400 random basis pairs, exact |
| the principal sl₂ (e, h, f) from the Cartan matrix, `[e,f] = h` exact | 27 = **17 + 9 + 1** (h-spectrum {±16,…,0³}) |
| the six highest-weight vectors of the principal blocks (the dial slots) | hv2, hv8, hv10, hv14, hv16, hv22 |
| **θ-parity by bracket closure** ⟨sl₂, hv⟩ | **hv8, hv16 → 78 = e₆**; hv10, hv14, hv22 → **52 = f₄** — B265/B576's dichotomy, recomputed |
| the subregular sl₂ E₆(a₁), weighted Dynkin (2,2,2,0,2,2), generic e in g₂, f solved | orbit dimension **70**, 27 = **13 + 9 + 5** |

Every exponential used below is `exp` of a nilpotent 27×27 matrix — a terminating polynomial, exact over ℚ(ω).

## 2. The law, own code (`verification/spectrum_law.py`; run record `verification/spectrum_law_run.txt`)

Presentation ⟨a, b | a w b⁻¹ w⁻¹⟩, w = b a⁻¹ b⁻¹ a, Riley a ↦ [[1,1],[0,1]], b ↦ [[1,0],[u,1]], u = 1 + ω; the E₆
representation ρ(a) = exp(e), ρ(b) = exp(u f). The relator holds on the 27 (checked exactly); the longitude
λ = w w* commutes with ρ(a) and has trace 27 (the unipotent lift). The double: B1036's three-generator
presentation ⟨a, b, d | R(a,b), R(a,d), L(a,b) L(a,d)⁻¹⟩, ρ(d) = g_t ρ(b) g_t⁻¹, g_t = exp(t·hv).

| object | 27 | 27̄ |
|---|---|---|
| the cusped M, principal | **h⁰ = 1, h¹ = 3** (modular AND exact ℚ(ω) elimination agree: rank d⁰ = 26, rank d¹ = 25) | h⁰ = 1, **h¹ = 3** |
| D_t, dial **hv8**, t = 0 / 1 / 2 / ω | **5 / 2 / 2 / 2** | **5 / 2 / 2 / 2** |
| D_t, dial **hv16**, t = 0 / 1 / 2 / ω | **5 / 2 / 2 / 2** | **5 / 2 / 2 / 2** |
| D_t, dial **hv14** (θ-even), t = 0 / 1 / 2 / ω | **5 / 5 / 5 / 5** | **5 / 5 / 5 / 5** |

**B1086's law is reproduced cell for cell on a repository instrument**, and — computed here for the first time
rather than inferred from Poincaré duality — **the 27̄ row equals the 27 row in every cell**, with h⁰ dropping
1 → 0 exactly when the θ-odd dial is switched on (the trivial summand of 17+9+1 is no longer invariant: the
amalgam's image is all of E₆).

## 3. The extension: B1257's subregular embedding

B1257 selects the **subregular** orbit by Brieskorn–Slodowy and reads off 13 + 9 + 5, "three chiral". On the
same instrument:

| object | 27 | 27̄ |
|---|---|---|
| the cusped M, subregular | **h⁰ = 0, h¹ = 3** (rank d⁰ = 27, rank d¹ = 24) | h⁰ = 0, **h¹ = 3** |
| D with a dial X in the 8-dim centralizer of e_sub, t = 1: | | |
| — X ∈ the sl₂ itself (closure 3) or closure 36 (three slots) | **6** | **6** |
| — X with closure e₆ (five slots) | **4, 4, 6, 6, 6** | **4, 4, 6, 6, 6** |

So the subregular double is **6 untwisted** (2 + 2 + 2, one seam-born class per nontrivial block, exactly as
B1036's mechanism predicts with no trivial block) and **4 for two of the dense dials** — the subregular analogue
of 5 → 2. **No dial, in either embedding, reaches 3, and every row has h¹(27) = h¹(27̄).** For the subregular
case the dense-closure slots do not all give the same count (4 and 6 both occur): the centralizer of a subregular
nilpotent is non-abelian, and the count depends on the direction within it, not only on its closure.

## 4. What this settles for JOIN 1

- B1086's twisted rows now rest on **two independent instruments** (the certificate and this one); its named
  residual is **paid**.
- The **27̄ rows are computed, not deduced** — the closed wall (B1260 (1)) is seen numerically in every cell.
- B1257's subregular route, even if I-25 were earned, produces **3 vector-like classes on the cusped object and
  4 or 6 on the double** — never a net count, never three on the closed object (consistent with B1256's
  2026-09-06 addendum: the sl₂ frame cannot carry chirality).

## Controls

- The instrument's dichotomy **can fail**: three of the five non-trivial slots close to f₄, two to e₆.
- The modular ranks are taken at two primes ≡ 1 (mod 3) and must agree; the single-manifold rows are also
  computed by exact elimination over ℚ(ω) and agree (rank d⁰ = 26, rank d¹ = 25).
- The relators are checked to hold exactly for every representation before any cohomology is taken (the
  amalgam's third relator included), so a wrong dial would have failed before it could produce a number.
- The subregular orbit dimension (70) and the principal block structure (17+9+1) are reproduced from
  independent data (B1256/B1257 and B327 respectively).

## Verification

`verification/e6_instrument.py` (self-checks) and `verification/spectrum_law.py` (the full table, ~35 min);
`verification/spectrum_law_run.txt` is the run record. Lock: `tests/test_b1267_spectrum_law_rebuilt.py`
(the instrument checks and the cusped rows fast; one twisted-double row in the slow lane).

- **Feeds on:** B883 (the 27), B854 (the bracket and the principal triple), B1086 (the law and its residual),
  B1036 (the double's presentation), B265/B576 (the θ-parity dichotomy), B1256/B1257 (the subregular selection),
  B1260 (the closed wall).
- **Registers:** no identification change; I-25 and I-26 unchanged in status, their content sharpened (§4).
