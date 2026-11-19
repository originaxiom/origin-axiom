# B1966 — The trade-off's two ends are exact for every channel: a null Higgs makes the two readings' light states orthogonal; a real Higgs is flavour-blind up to a reflection, so m₂/m₃ ≥ 1/3

**Verdict: PROVED** (exact, sympy, from B1736's closed form; one part checked numerically, stated). Main, 2026-11-19.
Data-free. Register rows P-879 and P-847. **0 of 19.**

> *Dated note 2026-11-19 (B1967): the interior's "for every channel" form is false. With tuned channels a Higgs of reality 0.003 gives an aligned mixing with heavy-pair ratios near 1e-3. The two ends proved here stand. What is open (P-879) is whether frame C's own channels reach the tuned region.*

## Seen first

- **Swept, in the record's own words:** `VERDICT topic-sweep /nearly null|non-null Higgs|reality of the Higgs|V_ud|hierarchy and (the )?alignment|dichotomy|Standard Model's reading|trade-off/: 31 of 1706 arcs on main match (NEGATIVE 6, OPEN 4, PROVED 21); 19 register rows match (DONE 12, QUEUED 7)`.
  Also searched for the closed form and for a floor of one third.
- **B1736 (PROVED)** has the coupling in closed form, Y = u hᵀ + h uᵀ − (u·h)·1 + u₁[h]_× + h₀(u₁·1 + [u]_×).
  Frame C's code agrees with it for a pure triplet Higgs (h₀ = 0) to 1e-33 at four points, three sectors and both
  readings (main's check, 2026-11-19).
- **B1727 (PROVED)**, the flavour-blind bound: a Higgs S = 1 gives Y = c·1 + [a]_×, and then m₂/m₃ ≥ 1/3, sharp.
- **B1739 (PROVED):** with the channels off, the light states are h̄ and h.
- **B1740 (NEGATIVE as sealed, for F₋₂):** a non-null Higgs loses the hierarchy.
- **B1743** verifies the web seat's R5, m₂/m₃ ≥ |h·h|/4, in an idealised channel.
- **B1964:** the null-limit lemma in frame C's basis, for Mw of rank 2.
- **B1965 (OPEN):** the trade-off searched at four points.
- **Not found on record:** the two reductions below, each one line long from B1736's form.
- **The literature:** Weyl's inequalities for singular values (as B1727 uses them) and the standard cross-product
  identity a × (b × c) = b(a·c) − c(a·b). Nothing outside the record treats this coupling.

## The results (`verification/endpoints.py`, exact unless stated)

Take a pure triplet Higgs h, channels (u, u₁) and Y = u hᵀ + h uᵀ − (u·h)·1 + u₁[h]_×.

- **E1, for every h, u and u₁:** Y h = (h·h) u and hᵀY = (h·h) uᵀ.
- **E2, a null Higgs (h·h = 0), every channel:**
  - Y h = 0 and hᵀY = 0, so m₁ = 0.
  - The left null vector is h̄. The conjugate reading changes h to h̄ and leaves the channels alone, so its left null
    vector is h.
  - ⟨h̄, h⟩ = conj(h·h) = 0: the two readings' light states are exactly orthogonal, whatever the channels.
  - This is B1739's lemma without its "channels off", and B1964's without its basis and rank conditions.
- **E3, a real Higgs, every channel.**
  - Y is rotation-covariant, R Y(h, u) Rᵀ = Y(Rh, Ru), so take h = e₁.
  - Then Y(1 − 2e₁e₁ᵀ) has symmetric part −(u·e₁)·1, and the rest is antisymmetric: it is of B1727's form c·1 + [a]_×.
  - 1 − 2e₁e₁ᵀ is orthogonal, so the singular values are unchanged, and B1727's sharp bound applies: **m₂/m₃ ≥ 1/3
    for every channel.**
  - So a real Higgs is flavour-blind up to the reflection 1 − 2ĥĥᵀ. This makes B1740's finding a theorem at reality 1
    for every Higgs and channel; B1740 had it for one sealed case, F₋₂.
- **E4, a null Higgs's heavy pair.**
  - By hand: in the basis (h, h̄, h × h̄) the coupling reduces to a 2 × 2 block whose determinant is −2(u₁² + u·u)
    for |h|² = 2.
  - So m₂m₃ = |h|²·|u₁² + u·u|. The heavy pair's hierarchy is the channel quaternion's near-nullity, B1659's det M,
    and not the Higgs's.
  - Checked at five random channels: the ratio is 2.000000000000.

## What it means

- **The trade-off's two ends are theorems for every channel:**
  - at reality 0, the two readings' light states are orthogonal;
  - at reality 1, the two readings coincide but the heavy pair is held at m₂/m₃ ≥ 1/3.
- **Under the charge rule neither end gives an aligned mixing with a hierarchy.** That is B1740's dichotomy, now
  exact at both ends instead of sealed for one Higgs.
- **What stays open is the interior, 0 < r < 1** (P-879). B1965's search found the frontier there at four points:
  alignment 0.9 reached only near r = 1, with m₂/m₃ 0.57 to 0.68.
  - A proof needs a bound that joins the two ends. One route is to perturb from each end: the light vector's angle
    grows like r·|u|/σ₂ near reality 0, and the floor moves continuously from 1/3 near reality 1.

## Not established

- **The interior of the trade-off.**
- **E4 in symbols.** It is derived by hand and checked at five samples, not proven in sympy.
- **Any comparison with data.**

## Files

`verification/endpoints.py` and `endpoints_run.txt`. The lock is `verification/test_b1966_endpoints.py`.

0 of 19.
