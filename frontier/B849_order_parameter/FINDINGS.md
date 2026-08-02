# B849 — the claimed β=1 SSB has no manifold-level order parameter, and the one it nominates is at the wrong level

cc banking seat, 2026-08-02. Prereg sealed **before** computing: `facb8c0355d8b422`.
Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 0. The correction that came before the numbers

This seat argued, in conversation, that the object's **amphichirality** makes the order parameter
"provably zero" and called it a cheap kill. **That was wrong, and it was withdrawn in the
preregistration before any number existed.**

In SSB the **system** carries the symmetry and the **state** breaks it. A ferromagnet's
Hamiltonian is rotation-invariant — that is the *precondition* for magnetisation, not an argument
against it. **m004's amphichirality is the ℤ/2 existing, which is exactly what SSB requires.**

So Cells 1–3 below **cannot** refute the reframe, and the seal forbids reporting them as if they
could. What they do is close off the easy answer and say what the reframe still owes.

## 1. The instrument, with its positive control

| manifold | vol | CS | class | amphichiral |
|---|---|---|---|---|
| **m004** (the object) | 2.029883 | **0.0000000000** | **0** | yes |
| **m003** (the sister) | 2.029883 | **4.9348022005** | **π²/2** | yes |
| m015 = 5₂ | 2.828122 | −3.0241283765 | free | no |
| m006 | 2.568971 | −2.2529672263 | free | no |
| m007 | 2.568971 | −2.6818349742 | free | no |
| m009 / m010 | 2.666745 | −0.4112 / 4.5236 | free | no |
| m011 | 2.781834 | −3.7867059875 | free | no |
| 6₁ / 6₂ | 3.163963 / 4.400833 | 3.0789 / −3.9970 | free | no |
| 6₃, 8₉ | 5.693021 / 7.588180 | 0.0000000000 | 0 | yes |

> **Positive control PASSES: nine chiral members return CS ≠ 0.**

That clause was sealed in advance for a reason — *"CS(m004) = 0" from an instrument that returns
zero for everything would be uninterpretable.* The control is what makes the object's zero mean
something.

## 2. Cell 3: the lemma holds as sealed, and my implementation was narrower than my own seal

The lemma: for amphichiral M, an orientation-odd invariant satisfies I(M) = −I(M), so 2·I(M) = 0 —
**I is zero *or* 2-torsion.** CS is defined mod π², so the 2-torsion subgroup is **{0, π²/2}**.

**The first implementation checked only `CS == 0`.** It reported **m003 as a lemma violation**.
m003's value is **π²/2 to 4×10⁻¹¹** — the lemma's *other permitted value*, which the code could
not see.

> **The preregistration says "zero-or-half-period". The code said "zero". The seal was right and
> the implementation was narrower than it.**

Corrected to test what was sealed: **5 of 5 amphichiral members are 2-torsion, zero violations.**
This is the session's recurring defect in its cleanest form — *the criterion was stated correctly
and the artifact tested something smaller* — and here the seal, written first, is what caught it.

## 3. Cell 2 verdict, and an unlooked-for discriminating fact

**CS(m004) = 0, exactly.** By the sealed criteria: **ORDER PARAMETER ABSENT (manifold level).**

But the panel produced something the arc was not looking for:

> **m003 and m004 have the same volume, are both amphichiral, and sit in DIFFERENT 2-torsion CS
> classes — 0 versus π²/2.**

That is a **discriminating invariant separating the object from its sister**, a separation this
programme has spent real effort on (B790's non-isospectrality, the B803 class/manifold audit).
It costs one line of SnapPy. **Flagged, not claimed:** CS is a classical invariant and this
distinction is very likely known in the literature; it needs a prior-art gate before it is called
anything more than *a separator we can now compute*. Recorded so it is not rediscovered.

## 4. Cell 4 — the cell with teeth

The reframe nominates **chirality** as the order parameter (B723: *"CHIRALITY = the extremal-KMS /
Galois-embedding LABEL of the state"*). Chirality here is **complex conjugation**.

Computed: **complex conjugation does not fix K = ℚ(√−3)** — it sends √−3 ↦ −√−3. It has order 2.
Therefore it is the nontrivial element of **Gal(K/ℚ)**, and **membership in Gal(K^ab/K) requires
fixing K**, so it is **not** in Gal(K^ab/K).

> **VERDICT: LEVEL MISMATCH — CONDITIONAL.**
> If the group permuting extremal KMS states at β=1 is Gal(K^ab/K), then the symmetry the reframe
> says breaks **is not an element of the group acting on the states that break it.** Right object,
> wrong level — the programme's own most-catalogued defect class.

**The conditional is not decoration.** That Gal(K^ab/K) is the acting group in a
Bost–Connes/Connes–Marcolli–Ramachandran system over an imaginary quadratic field is **a citation,
declared as such in the seal and NOT verified in this sandbox.** P5 died last week because a gate
named the right person and asked the wrong question. This verdict carries CONDITIONAL or it is not
banked.

**What would overturn it:** the acting group being larger than Gal(K^ab/K) (e.g. a system whose
symmetries include Gal(K^ab/ℚ)), or chirality entering through a component this cell does not
model. Either would mean this seat is wrong, and the seal records that in advance.

## 5. What the reframe now owes — stated precisely, which is the arc's actual product

The reframe is **not refuted**. It is **located**:

1. The order parameter **cannot be a topological invariant of M** — every orientation-odd
   invariant is 2-torsion by amphichirality, and m004 sits at 0.
2. It must therefore live on the **state space**, and the reframe must exhibit it there.
3. Cell 4 says which group it must live in — and the nominated candidate, conditionally, does not.

**Both pre-stated expectations were confirmed** (ABSENT at high confidence, LEVEL MISMATCH at
moderate). That is worth flagging rather than celebrating: an arc that confirms its author's
priors is the kind that most needs the seal, and the seal is why the Cell 3 correction is visible.

## 6. What this arc does NOT do

- **Does not refute the reframe.** See §0 and §5.
- **Does not verify the Bost–Connes/CMR identification.** Declared citation; a lit-gate is owed
  before Cell 4 is load-bearing.
- **Does not run T2–T7** (the length-spectrum III₁ shadow, finite-size scaling up the congruence
  tower, the parabolic pressure function, the cascade count, controls, exponents).
- **Nothing to `CLAIMS.md`.** No value, no coupling, no physics.

## Carried forward

1. **Lit-gate on Cell 4's citation** — the single highest-value follow-up, because the whole
   LEVEL MISMATCH rests on it.
2. **Prior-art gate on the m003/m004 CS separation** before it is described as anything new.
3. **T2 next** (the geodesic length spectrum as a computable shadow of the III₁ question) — and
   note that the **370 geodesic lengths are not in main**, the same phantom pattern as the 43
   eigenvalues.

`tests/test_b849_order_parameter.py`
