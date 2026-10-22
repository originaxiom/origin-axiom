# B1708 — W120 AND W121 ON MAIN (the SM seat's relays 200–201; the owner's main task as relayed: the record's 3d gravity carried to 4d): THE CONE, THE LEAST VOLUME, THE TWELVES AND THE TRIPLET'S LIFTS VERIFIED — AND EACH IS A CLASSICAL FACT, NAMED: THE MILNE UNIVERSE, THE MINIMAL-VOLUME CUSPED MANIFOLDS, THE STRINGY COSMIC STRINGS

**Verdict: PROVED (verified on main's own code; no data).** cc (main), 2026-10-22. The SM seat's W120 and W121, done at
the owner's order of 2026-10-22 as the seat relays it ("carry the record's 3d gravity, which has no gravitons, to 4d
gravity with propagating ones, as the main task"), ask main to check them and to say how GENESIS FK10 should read. 0 of 19.
- **(1) The cone (W120), exact** (sympy): for g of constant curvature κ (Ric = 2κg), the metric −dt² + t²g has
  Ric_tt = 0, Ric_ij = 8(κ + 1)/(1 + κr²)² δ_ij: **Ricci-flat iff κ = −1.** So every hyperbolic thread is the space of a flat
  4d vacuum on which gravitons propagate. *Prior art:* this is the Milne universe — the interior of Minkowski space's
  future light cone quotiented by the 3-manifold's group; any hyperbolic 3-manifold gives one. Nothing in it is specific
  to the record beyond the record being hyperbolic.
- **(2) The least volume (W120's post hoc census)** (SnapPy, 482 orientable punctured-torus bundles over every necklace
  word in L, R to length 10, both monodromy signs): **the least is ±LR, 2.0298832128 (m004, m003)**, then ±LLR and ±LRR at
  2.6667. *Prior art:* m003 and m004 are the minimal-volume orientable cusped hyperbolic 3-manifolds (Cao–Meyerhoff 2001).
  The seat's reading — the tick's universe least among threads, with the volume as the 4d vacuum flow's attractor
  energy (Fischer–Moncrief) — is a reading: that theory is for closed spatial sections, and the threads are cusped.
- **(3) The twelves (W120)**: SL₂(ℤ)'s abelianisation from its presentation (S⁴ = 1, S² = (ST)³) has Smith form
  (1, 12): **ℤ/12**, with χ(T) = χ(R) = 1, χ(L) = 11, χ(LR) = 0. A product of positive twists (conjugates of T) is trivial
  only if their number is a multiple of 12.
- **(4) The fibre's metric (W120)**: Im τ^p ∣η∣^{2q} is SL₂(ℤ)-invariant **only for q = 2p** (deviation 10⁻³⁰ against
  0.1–0.6 otherwise); near a pinched fibre (z ~ e^{2πiτ}) Im τ∣η∣⁴ ~ (−log∣z∣/2π)∣z∣^{1/6} (the exponent 0.16672, 0.166670,
  0.1666667 at ∣z∣ = 10⁻³, 10⁻⁵, 10⁻⁷). *Prior art:* the metric e^φ∣dz∣² + (1/Im τ)∣dx + τdy∣² with e^φ = Im τ∣η∣⁴∣h∣² and a
  deficit 2π/12 per string, closing at 12 strings and at 24 on K3, is Greene–Shapere–Vafa–Yau's stringy cosmic strings
  (1990). W120's fibre section is that construction read on the record's τ.
- **(5) The triplet's lifts (W121)**: ρ_T built from its definition (B1634: the multiplier of η²¹(θ₂², θ₃², θ₄²), weight
  23/2; solved from four τ, residual 10⁻³⁴), T_a = T, T_b = S T S⁻¹: **(T_aT_b)^k is scalar exactly at k = 3, 6, 9, 12,
  with values −i, −1, i, 1** — twelve twists give −I₃, twenty-four give I₃. So the rational elliptic surface (12 strings)
  cannot carry the triplet and K3 (24) is the least closed solution that can. **Not verified here:** W121's index count
  (−30 for ρ_T, −36 for ρ̄_T on K3; −15χ(O_S) and −18χ(O_S) in general), which needs its index formula; registered.
- **What it means, and the answer to the seat.** The cone, the twelves and the scalar lifts hold on main's instruments,
  and each is a classical fact read on the record. 4d gravity in this form supplies units of end data only in twelves
  (and the triplet only in twenty-fours), and by W121 the resulting counts are never ±3 — so GENESIS FK10's single unit
  at the weave's cusp is **not** supplied by the closed 4d solutions, and stays a tagged postulate. The sentence for FK10
  joins the next amendment (P-254). No G, no carrier and no chiral three come out of the step to four dimensions.
- **What it does not do.** W121's −15χ(O_S) law; the seat's further readings (the attractor energy for cusped threads);
  the literature of each classical fact beyond naming it.

## 0. Seen first

`VERDICT topic-sweep /Milne|stringy cosmic|cosmic string|Ricci.flat|four.dimensional gravity|4d gravity|graviton|elliptic surface|K3/ (full text): 34 of 1480 arcs on main match (NEGATIVE 7, OPEN 4, PROVED 23)` —
read for gravity: B1165 (the object's gravitational sector is generic — built from holonomy and volume, it survives
swapping m004 for a non-arithmetic knot), B97 (Lorentzian signature by construction) and B1343 (elliptic fibrations
only through the Kodaira IV* fibre as an ADE face). None treats the Milne cone or the stringy cosmic strings; B1165's
verdict agrees with (1) here — the cone works for any hyperbolic 3-manifold. **Literature:** the
Milne universe; C. Cao and G. R. Meyerhoff, "The orientable cusped hyperbolic 3-manifolds of minimum volume", Invent.
Math. 146 (2001); B. Greene, A. Shapere, C. Vafa and S.-T. Yau, "Stringy cosmic strings and noncompact Calabi–Yau
manifolds", Nucl. Phys. B 337 (1990); A. Fischer and V. Moncrief on the reduced Hamiltonian of 3+1 vacuum gravity —
named as context, not re-derived.

## 1. Files

- `verification/w120_w121_on_main.py` → `w120_w121_on_main.json`, `w120_w121_run.txt` (absolute paths in a library
  warning replaced by `<python>`).
- The lock: `tests/test_b1708_w120_w121_on_main.py`.
