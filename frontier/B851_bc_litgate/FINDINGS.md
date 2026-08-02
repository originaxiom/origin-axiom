# B851 — the lit-gate B849 owed: the citation is CONFIRMED from the primary source, and the conditional relocates

cc banking seat, 2026-08-02. Mathematics/literature scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 0. Why this gate ran before anything else

B849 banked **LEVEL MISMATCH — CONDITIONAL**, and named the reason: its load-bearing step was
**a declared citation, not a computation.** Its own carried-forward list put this gate first.

**P5 died eight days ago because a gate named the right person and was asked the wrong question.**
Paying this debt before building the next thing is the only consistent choice.

## 1. The question, stated before searching

**Does the group that acts on the extremal KMS states of a Bost–Connes/CMR system over an
imaginary quadratic field K contain complex conjugation?**

- **CONFIRMS the mismatch:** the acting group is Gal(K^ab/K) or the idele class group of K.
- **REFUTES the mismatch:** the acting group is larger — Gal(K^ab/ℚ), a Weil group, or a system
  admitting complex conjugation as a symmetry or anti-symmetry.

**Both directions were searched.** A prior-art call that checks only the confirming half is half a
check — that is the correction the P5 re-check produced, and it applies to a *confirming* gate
exactly as much as to a killing one.

## 2. Result: CONFIRMED, verbatim, from the primary source

Connes–Marcolli–Ramachandran, *KMS states and complex multiplication* (`math/0501424`, Selecta
Math. 2005). Text extracted from the authors' own PDF and quoted with line references:

| | quote |
|---|---|
| abstract | *"This system admits the Dedekind zeta function as partition function and **the Idele class group as group of symmetries**."* |
| §, l.1280 | *"**The action of the symmetry group I_K/K\* on E_β is then free and transitive.**"* |
| l.1138 | *"with a **free and transitive action of the idèle class group of K** as symmetries."* |
| l.448 | *"the set of extreme KMS states below critical temperature is **free and transitive**."* |
| l.177 | *"group **Gal(K^ab/K)**. This is the **maximal abelian quotient of the absolute Galois group Gal(K̄/K) of K**"* |
| l.92 | *"implemented by the action of the idèle class group as symmetries of the system, **via the class field theory isomorphism**."* |

> **The acting group is I_K/K\* ≅ Gal(K^ab/K), and Gal(K^ab/K) consists of automorphisms that FIX
> K. Complex conjugation does not fix ℚ(√−3). It is therefore not in the acting group.**

**Counter-evidence searched for and not found:** the string *"complex conjugation"* occurs
**zero times** in the CMR paper. No larger symmetry group, Weil-group extension, or
anti-automorphism admitting conjugation was located.

**So B849's Cell 4 citation is no longer the weak link.** Verified in both directions.

## 3. The conditional does not vanish — it RELOCATES, and that is the useful part

B849's verdict rested on two steps. **Step one is now confirmed.** Step two was never stated as
separate, and it should have been:

> **Is the programme's β=1 system actually a BC/CMR-type system for K = ℚ(√−3)?**

B723 says *"the β=1 spontaneous symmetry breaking of the arithmetic thermal system over
ℚ(√−3)"* — suggestive, never demonstrated. **That is now the single load-bearing assumption, and
it is an IN-REPO question about our own arc, not a literature question.** A gate that converts an
external unknown into an internal one has done its job.

**And the evidence for the identification is strong, which makes the mismatch bite harder, not
softer.** CMR's action on extremal KMS states is **free and transitive** — precisely the
**simply-transitive torsor** B700 reports. The better the identification, the worse the level
error.

## 4. A likely source of the error, and it is specific

**For BC over ℚ, complex conjugation IS a symmetry.** Gal(ℚ^ab/ℚ) ≅ Ẑ\* by the cyclotomic
character, and complex conjugation sends ζ_n ↦ ζ_n⁻¹, i.e. it is **−1 ∈ Ẑ\***. Wikipedia's summary
of the ℚ case says exactly this: *"the absolute Galois group acts on the ground states of the
system."*

**For CMR over imaginary quadratic K, it is not**, because Gal(K^ab/K) fixes K by definition and
conjugation does not.

> **The reframe's "chirality = Galois label of the state" reads as correct intuition from the ℚ
> case, imported into the K case where the group is strictly smaller and no longer contains the
> element in question.**

That is a concrete, checkable diagnosis rather than a general complaint — and it is the same
right-object-wrong-level shape the corpus already catalogues.

## 5. What this gate does NOT establish

- **It does not refute the reframe.** It confirms one link in B849's chain and isolates the
  remaining one.
- **It does not show the programme's system is CMR's.** That is now the open question, and this
  arc deliberately does **not** assume it in either direction.
- **It does not verify CMR's theorems.** Their statements are quoted as prior art; nothing here
  re-proves them.
- **The source text is quoted, not vendored** — no third-party paper enters the repo.

## Carried forward

1. **Test whether B723's system is BC/CMR-type for ℚ(√−3)** — in-repo, and now the only thing
   B849's verdict rests on. If it is not, the LEVEL MISMATCH does not apply and B849 must say so.
2. If it *is*, B849's verdict stands unconditionally and the reframe's nominated order parameter is
   refuted at the level of group membership.

Sources: [CMR, *KMS states and complex multiplication*](https://arxiv.org/abs/math/0501424) ·
[author PDF](https://www.math.fsu.edu/~marcolli/CMR18.pdf) ·
[Bost–Connes system](https://en.wikipedia.org/wiki/Bost%E2%80%93Connes_system)

`tests/test_b851_bc_litgate.py`
