# xB016 — ADDENDUM 1: P3 done properly, its withdrawn mechanism PROVED, and Route 3 CLOSED — with two of this arc's own cells corrected by the literature

**2026-09-17. `PREREGISTRATION.md` untouched (`56447437…`); new cells P7–P9 in
`verification/p3_proper.py`. Owner's instruction: "go for proper p3".**

P3 banked with three soft edges, all named in its own text: the census stopped at degree 8; the
mechanism was **withdrawn** after a systole measurement turned out to be a swallowed exception; and
the constant `1/(6π)` was **quoted from memory**. All three are settled here. Two of them settle in
this arc's favour. **The third overturns P4 and P6.**

---

## P7 — the census, extended: P3 strengthens

| degree | #covers | min | max | median | #trivial torsion | #exceeding the cyclic limit |
|---|---|---|---|---|---|---|
| 2–8 | 38 | 0.000000 | 0.474072 | 0.135305 | 7 | 0 |
| 9 | 11 | 0.000000 | 0.474109 | 0.060135 | 3 | 0 |
| 10 | 38 | 0.000000 | 0.474121 | 0.034147 | 9 | 0 |
| **all** | **87** | **0.000000** | **0.474121** | **0.090203** | **19** | **0** |

**Over twice the evidence, and the finding sharpens**: the rate still spans the whole range down to
zero, **19 of 87 covers have no torsion at all**, the median *falls* as degree grows, and **not one
cover exceeds the cyclic tower's limit**. The rate is the tower's.
*Still a measurement, not a theorem:* the range is degree ≤ 10.

---

## P8 — the mechanism P3 withdrew, now PROVED

The relator `aaabABBAb` has exponent vector `(a,b) = (1,0)`, so `H₁ = ℤ²/⟨(1,0)⟩ = ℤ` and the
abelianisation is **`φ(a) = 0`, `φ(b) = 1`. The generator `a` is nullhomologous.**

`tr(a) = −1.5 + 0.8660254038i`. Its **modulus is √3 < 2** — and P3's first draft therefore
classified it as elliptic and threw it away. **That test was wrong**: in `SL(2,ℂ)` an element is
loxodromic iff its trace is not in the **real** interval `[−2,2]`, and a hyperbolic 3-manifold group
is torsion-free and has no elliptics at all. Corrected, `a` is loxodromic with translation length

> **1.087070144996** — which is **m004's systole**, agreeing with SnapPy's `length_spectrum` to
> **12 digits** on an independent instrument.

**The two-sided argument, both directions exact:**

* **Upper.** `a` is nullhomologous, so its class is `0` in `H₁ = ℤ` and hence `0` in `ℤ/n` for
  **every** n. It lies in `ker(π₁ → ℤ → ℤ/n) = π₁(M_n)`, so it is a closed geodesic of the **same**
  length in every cyclic cover: `systole(M_n) ≤ 1.0870701450`.
* **Lower.** Any closed geodesic of `M_n` projects to a closed geodesic of m004 of length `ℓ/d`,
  `d ≥ 1`, so `systole(M_n) ≥ systole(m004) = 1.0870701450`.

> **`systole(M_n) = 1.0870701450` exactly, for every n. The injectivity radius does not grow, so the
> cyclic tower does NOT converge to the universal cover.** P3's withdrawn mechanism is restored as a
> proof.

---

## P9 — the literature came back, and it corrects two of this arc's own cells

The sweep commissioned before xB016 banked returned **after** banking. It **confirms** P2 and P3 and
**overturns P4 and P6.**

**(a) P2 CONFIRMED, more strongly than P2 argued.** The on-shell action of complex Chern–Simons
**is** the complex volume, `s₀ = i(Vol + i·CS)` (Dimofte–Gukov–Lenells–Zagier, arXiv:0903.2472
eq. 4.6), and torsion enters at **one loop** as `S₁ = ½ log(T(M;E_ρ)/2)`, the Ray–Singer torsion
(same paper, eqs. 2.1–2.3) — order `ħ⁰`, while the action is order `1/ħ`. Putting a torsion in the
exponent as an entropy **double-counts the same expansion at two orders in `ħ`**. And a cusp is not
a horizon: in Gukov's own dictionary (hep-th/0306165 §1.2) a cusp is the worldline of a **massless
point particle**, a zero-angle conical defect. **Two further kills P2 did not have:** the
identification is **knot-dependent** (the trefoil has `M(Δ) = 1`, giving `σ = 0`), and feeding
`1/(6π)` in instead gives `c = 1/π ≈ 0.318` — deep quantum, the regime where a semiclassical
on-shell action is meaningless. **Self-undermining both ways.**

**(b) The `1/(6π)` attribution was wrong, and it was mine.** P3 called it *"the asymptotic
torsion-growth rate associated with a hyperbolic 3-manifold."* **It is a conjecture, not a theorem**
— Bergeron–Venkatesh (arXiv:1004.1083) **Conjecture 1.3**. Their **Theorem 1.4** requires **strongly
acyclic** coefficients and a **cocompact** lattice; `ℤ`-coefficients are not strongly acyclic and a
cusped manifold is not cocompact, **so it does not apply here at all**. With `ℤ`-coefficients the
only theorem is an **upper bound** — Lê (arXiv:1412.7758, Thm 1): `limsup log t₁(Γ_k)/[Π:Γ_k] ≤
vol(X)/6π` for **exhaustive nested** towers — and Lê's §1.5 notes there is **not one known example**
of a hyperbolic 3-manifold with a trace-convergent tower where the limit is even positive.

**(c) And the factor of 8.9 has a clean reason — which is P8's, in group-theoretic form.**
`log M(Δ) = 0.9624` is the **L²-torsion of the ℤ-cover** (Lück Thm 1.40; Bergeron–Venkatesh
**Cor. 7.7**, exactly the fibred case, giving `log|H₁(V_N)_tors|/N → log M(P_f)` — **per cover
degree, not per volume**). `vol/6π` is the **L²-torsion of the universal cover** (Lück–Schick, GAFA
9 (1999) 518–567). **Two different invariants of the same manifold.** The hypothesis that fails is
exactly the one P8 proves fails: for `Γ_n = ker(π₁ → ℤ/n)` the intersection of the `Γ_n` is
`[π₁, π₁]`, **not** the identity — the tower is not exhaustive. **P8's constant systole is the
geometric witness of the same fact, found independently on this bench.** *Also corrected:* dividing
by **volume** was this seat's own step; every theorem in this area divides by **cover degree**.

**(d) P4's "`k` must be even" is WITHDRAWN — it is unsupported.** Witten (arXiv:1001.2933 eq. 2.2):
`I = −s·Im W + ℓ·Re W` with `s ∈ ℂ`, `ℓ ∈ ℤ` — **the only condition is that `ℓ` (= `k`) is
integral.** Gukov (hep-th/0306165 §1.1): *"The other parameter, s, is not quantized"*, constrained
only to be real or imaginary by unitarity. Dimofte (arXiv:1409.0857 §2.1): *"one quantized (k) and
the other continuous (σ)."* **Nothing couples `k` and `σ`.** And the framing escape hatch does not
exist: for **complex** Chern–Simons the eta-invariant **vanishes** (Gukov eq. 3.36; Witten 1991), so
there is no `exp(2πi c/24)` to cancel against. The cusped mod-½ ambiguity is resolved in the
literature by **lifting** — a decoration/spin structure, the invariant living in `ℂ/4π²ℤ` rather
than `ℂ/π²ℤ` (Zickert arXiv:0710.2049; DGLZ §3) — **not** by constraining `k`. **P4's own flag was
right and was the whole story:** P4 said the statement holds *"in one normalisation"* and that the
record pins none. The sweep reads the inference as an artifact of mixing Meyerhoff–Neumann's
**manifold-invariant** normalisation with Witten's **field-theory** one. **The gap P4 named stands —
the record still pins no normalisation — but the constraint P4 derived from it does not.**

**(e) So P6's recommendation is withdrawn too, and this is the real upgrade.** P6 named **Route 3**
as the one to re-open, on the ground that pinning the normalisation would turn well-definedness into
an equation relating the level to the framing anomaly. **There is no such equation**: `η = 0` kills
the framing term, and Witten's own treatment of the complex/cusped case (1001.2933 §4.3) keeps `ℓ`
integral and works on a **cover** where `exp(iI)` is defined, rather than constraining anything.

---

## What this addendum changes

> **All three routes are now closed, and the third is closed by the literature rather than by a
> guess.** `σ` is a **free continuous parameter of complex Chern–Simons theory** — that is the
> theory's own statement, not an accident of this object — so **no invariant of m004 or of its
> family can fix it by this route.** Path A does not cross, and the reason is now a citation:
> **Witten arXiv:1001.2933 eq. (2.2).**

**xB016's verdict is unchanged (Path A does not cross). What changes is that it is now
*better-founded than the arc that banked it*: P2's kill is confirmed and doubled, P3's kill is
doubled in evidence and its mechanism proved, and P4's constraint and P6's re-open recommendation
are both withdrawn.**

**Three errors of this seat's own in these cells, all recorded:** the `|tr| > 2` loxodromy test
(wrong criterion, cost the sharpest form of P8) · the `1/(6π)` attribution (a conjecture cited as a
theorem — the **second** time in two arcs that a remembered citation was wrong) · and **dividing by
volume when every theorem in the area divides by cover degree**.

**Artifacts:** `verification/p3_proper.py` (P7–P9), `verification/p3_proper.json`,
`verification/p3_proper.out`.
