# B1167 — two-seat harvest: codex R017 pays the SEAM-Y up-Yukawa provenance debt; cc3's cusp-shape second separator is ORIENTATION-BLIND (B1163 strengthened, not overturned)

**Status: banked (frontier). Verdict OPEN** — a two-seat integration (integrate-don't-merge), owner-approved.
`verification/reproduce.sh` → `REPRODUCES`. Gate 5 clean. Both seats credited; no merge.

## (A) codex R017 — the SEAM-Y up-Yukawa=0 primary derivations are now branch-local: PROVENANCE DEBT PAID

B1154/B1159-D1/R49-1 flagged codex's height-308 up-Yukawa proof as single-homed in an off-branch audit
workspace. **R017 (`codex/seat-r001` b7faffef) closes it** — the two load-bearing claims + their
self-contained certs are now branch-local. Verified here (codex asked for re-derivation, not a rerun):

- **The C₁₂ Wilson character arithmetic (independently re-derived).** At the selected characters (k=4:
  Q=A₈, u^c=A₄, d^c=A₄, L/e^c/H=A₀; k=8 the swap), **every MSSM operator is C₁₂-neutral** (up Q·u^c·H_u =
  8+4+0 ≡ 0 mod 12; down, lepton, μ likewise) — so C₁₂ imposes **no** family texture zero; it *permits* the
  up coupling Sym²(ℂ³) (dim 6). The up-Yukawa is **not** killed by characters.
- **The vanishing μ_u=0 is codex's cohomological naturality** (H¹(G_Y)=0 factors the cup product to zero at
  chain level; the Higgs lifts through H¹(K₁)=H²(K₁)=0). **FENCED as codex's typed input** — it needs the
  Sage/BCDD monad line-bundle cohomology stack, which codex itself scoped as "not a replacement for
  independent verification of the source cohomology." Not re-derived on this bench.
- **Both certs reproduce** (`verify_yukawa_cup_product_308_scope.py`, `verify_yukawa_exact_spectrum_no_go.py`)
  from b7faffef → PASS, byte-identical to codex's committed outputs (μ_u domain dim 1806, rank 0; the
  Wilson-projected up matrix the exact 1×6 zero; OA-C1055 the one-Higgs no-go).

**Disposition:** the up-Yukawa=0 **conclusion** was already banked as SEAM-Y (B1154, two independent walls —
codex's cohomological emptiness + our arithmetic regulator non-overlap). R017 pays the **provenance**: the
primary derivations are branch-local, cert-reproduced, character-arithmetic independently checked; the
source cohomology stays codex's fenced typed input (the down/lepton Sage chain remains open, codex's own
scope). **The MSSM debt ledger's D1 provenance item (B1159/R49-1) is now PAID** for the up sector.

## (B) cc3 B8138-extended — the cusp shape is a second object-level separator, but ORIENTATION-BLIND

cc3 extended Paper IV's census from 7 to 13 invariants and found **exactly one** new object-level separator:
the **cusp shape**. m004's is **2√3·i ≈ 3.4641 i**, taken by no other member of the 14-manifold ℚ(√−3)
family at any cusp (verified full-precision, all cusps, up to conjugation, nothing within 1e-6 — reproduced
here; the family table matches). cc3 explicitly handed cc the question: *"whether it yields an orientation is
your question, not mine — a modulus is not an orientation."*

**cc's answer: it does NOT.** The cusp shape 2√3·i is **purely imaginary** (real part 1e-15) — a
**rectangular** cusp torus. Orientation-reversal acts τ ↦ −τ̄, and −(2√3 i)‾ = 2√3 i = τ: **the cusp shape is
mirror-fixed.** So, like H₁≅ℤ, it distinguishes m004 (its magnitude 2√3 is unique) but carries **no
chirality** (real part 0) — it is **orientation-blind** and cannot supply the missing W₀. **B1163 is
strengthened, not overturned:** the object-level route list is now **two** (H₁≅ℤ, cusp shape), and *both* are
orientation-blind — the object still provably refuses to self-orient. cc3's "route list is now two"
acknowledged; the second route is examined and closed for W₀.

## A seed for the C5 investigation (owner-directed, task-tracked)

The cusp shape sharpens the C5 question (is m004's Mostow-canonical structure object- or observer-data?) in a
useful way: the object **does** supply an object-canonical *archimedean* datum — the cusp modulus 2√3·i, and
it is **√3-flavored** (tying the ∞-place cusp geometry to the disc-144/ℚ(ζ₁₂) ring-class hinge of B1166/C3).
So the archimedean place is **not** cleanly "all observer": the object hands over the cusp *modulus*
(object-canonical), and withholds only the *orientation* (mirror-fixed). This refines B1165's G3 (frame =
orientation + scale): the **scale** and **orientation** are observer-supplied, but a canonical archimedean
**modulus** (the cusp shape) is object-supplied. Carried to the C5 probe (afterward, per the owner).

## Fences

(A): the μ_u=0 vanishing is codex's cohomological input (fenced, needs the Sage stack); only the character
arithmetic + cert reproduction are own-verified; the conclusion is B1154's, re-homed not re-litigated. (B):
the orientation-blindness rests on the standard τ↦−τ̄ orientation-reversal action + m004's shape being purely
imaginary (own-verified); cc3's family uniqueness reproduced. No firewall crossing; Gate 5 clean (character
arithmetic, cusp moduli, Galois — no measured SM value). Not kill_graph-routed (a harvest; nothing killed —
(A) pays a debt, (B) strengthens B1163).

## Routes

- **codex:** D1 up-sector provenance PAID; the down/lepton Sage chain + the source H¹(G_Y)=0 cohomology remain
  codex's open scope (a future dual-home target). Relayed.
- **cc3:** the cusp-shape second separator is confirmed + typed orientation-blind; B1163's W₀ conclusion
  stands with a two-entry route list, both closed. Relayed.
- **C5 (owner-directed investigation, task #299):** the object supplies a canonical archimedean *modulus*
  (2√3 i, √3-flavored) but not the orientation — the seed for probing object-vs-observer at the ∞-place.
