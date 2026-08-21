# B1114 — LORENTZ ON THE DOUBLE: E₆ ⊇ so(3,1) ⊕ su(3), and the signature is the observer's gluing

**Status: banked (frontier). Verdict PROVED. Harvest arc (LORENTZ_ON_THE_DOUBLE.md;
cloud seat credited) — two-bench: their canonical construction + THIS bench's
independent verifier (own ad-nullspace centralizer code, own crystal-27 re-certified on
all 3003 Chevalley pairs, modular cross-checks over two primes), all four layers
CONFIRMED exact, then RE-RUN by the banking seat (same results). Gate 5 untouched. Lock
`tests/test_b1114_lorentz.py`.**

## THE ONE-LINE LEMMA (why the gauge system is complex)

A real form g₀ of a complex simple Lie algebra contains no nonzero complex subalgebra
(s = i·s and g₀ ∩ i·g₀ = 0 force s = 0). The hatch's composed holonomy is Zariski-dense
in one SL(2,ℂ) (CITED: B1086/B1098, tr[A,B] = 3/2 + (√3/2)i ≠ 2, irreducible
non-elementary), so it **cannot sit inside any real form of E₆** — which EXPLAINS
B715's banked "the native gauge system is inherently complex," rather than merely
observing it. (Verified here: span_ℂ(X,H,Y) is a genuine 3-dim sl₂(ℂ) in e₆(ℂ); the
density premise is cited, its citation status flagged not hidden.)

## THE VERIFIED ALGEBRA (the theorem, exact)

At the A2 landing, the 12 roots orthogonal to the hatch A₂ form an A₂+A₂ subsystem
(6+6), giving the centralizer z = I₁ ⊕ I₂ = sl₃ ⊕ sl₃, both ideals **ℚ-rational**
(root-vector + coroot spans; verified = z_{e₆}(hatch triple), rank 16). Then:

- I₁'s principal JM triple built fresh, exact relations, **commutes with the hatch's
  A2 triple** on all 9 brackets;
- **same class**: reductive centralizer dim 16 both sides + matching 78-entry ad(h)
  spectrum;
- **THE CRUX**: the **joint centralizer of the two commuting A2 triples is EXACTLY
  dim 8** (own nullspace + modular cross-checks), center 0, rank 2 → **su(3)**;
  proven to equal I₂ exactly (the principal sl₂ of I₁ has trivial self-centralizer).

> **E₆ ⊇ (A2-triple) ⊕ (A2-triple) ⊕ su(3); realified: so(3,1) ⊕ su(3) — Lorentz plus
> color, and nothing else.**

## THE SIGNATURE IS THE OBSERVER'S (rigorous, from the ℚ-rationality)

so(3,1) ≅ sl(2,ℂ)_ℝ, whose complexification is sl₂ ⊕ sl₂ with conjugation SWAPPING the
summands. The two ℚ-rational factors I₁, I₂ form a direct sum (I₁ ∩ I₂ = 0), so **no
field automorphism of ℂ/ℚ — in particular the object's own mirror (q ↦ 1−q Galois
twist) — can swap them**: it fixes each setwise. The antilinear swap that glues two
same-class sl₂'s into so(3,1) is therefore **extra data the object does not supply —
the observer's choice of real structure.** B716 ("signature is the observer's") and
B155/B517 ("(1,3) is algebraic inertia") are hereby exhibited constructively at the
Lie-algebra level. The capstone's "spacetime needs both hands" is now a computation.

## THE 27 IN THE GRAVITY READING (verified; also the SPENDING memo's crown)

The joint (h₁,h₂) bi-weight spectrum of the 27: **{(±2,±2):1, (±2,0):4, (0,±2):4,
(0,0):7}, ALL EVEN.** Under the constructed so(3,1) it decomposes as
**(1,1)⊗1_c ⊕ (1,0)⊗3_c ⊕ (0,1)⊗3̄_c** — a 9-state color-singlet **(1,1)** (the
traceless-symmetric rank-2 slot: the metric/spin-2 representation) ⊕ self-dual and
anti-self-dual colored vectors. **The same 27 that is matter in the gauge reading is
geometry (metric + colored flux) in the gravity reading** — double-duty at the content
level, selected by the D5 fork (B1115). Representation-level only; no graviton dynamics
claimed.

## Real-form fence (from ANOMALY_RESOLVED / B1119, folded here)

The so(3,1) ⊕ su(3) result is exact at the COMPLEX Lie-algebra level (brackets and
dimensions, which the invariant form does not enter). The REAL-FORM host that realizes
it is E₆(2) (variant A, color sl(3,ℝ)) or E₆(6) split (variant B, color su(2,1)) —
**neither gives COMPACT (physical) color.** Realizing the Lorentz pair with compact
color is the open 𝔽₂-kernel-sweep question (B1119's C-AR1). So: the algebra is the
object's; making color physical is not yet closed. (This nuance was itself the fruit
of a caught anomaly — a fake invariant form, τ-invariant not ad-invariant, exposed by
the classification-theorem-as-checksum when it returned the impossible character −10.)

## Correction carried (the memo's own, caught by verification)

The memo's line "dim z_{e₆}(e₂) = 36 per B1098's dim-c table" is **mis-sourced**:
B1098's dim_c column is the REDUCTIVE triple-centralizer (max 35), a different
invariant; 36 = dim z(nilpositive alone) is not in that table. **The number 36 is
correct** (independently recomputed here for both X and e₂) — only the citation was
wrong; the same-class conclusion stands. The memo's FAILED first method
(lorentz_double2.txt, 8+9=17 > 16) is superseded and would have been caught by this
bench's rank(I₁∪I₂)=16 check — logged for the error ledger.
