# B246 — the figure-eight volume conjecture: which volume does the large-color SU(N) invariant see?

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Thread-2 follow-on to B244. `quantum_volume.py` (pyenv, mpmath). Symmetric colored HOMFLY = Itoyama–Mironov–
Morozov–Morozov arXiv:1203.5978 eq 4 (validated in B245).

## The question
B244 found the SL(3,ℂ) **geometric** component of `4₁` has complex volume `8.1195 = 4·Vol` (the principal `Sym²`,
classical/Ptolemy). Does the large-**color** quantum SU(3) invariant grow at that rate — is there an "SL(3) volume
conjecture" hitting `4·Vol`? (The naive expectation, worth testing rather than assuming.)

## The result — the naive expectation is FALSE (verify-don't-trust)
The symmetric-rep large-color growth `(2π/p)·log|H_{[p]}(A=qᴺ; e^{iπ/(p+1)})|` extrapolates (least squares,
`p=200,400,800,1600`):
- **SU(2)** → **2.0298** ✓ — the standard Kashaev–Murakami–Murakami volume conjecture, `Vol(4₁)=2.0299`.
- **SU(3)** → **2.0297** — *also* the complement volume, **not** `8.1195` (nor `2·Vol`).

The SU(3) structure **washes out** because `A=q³ → 1` as `q → 1`: the symmetric large-color limit sees only the
knot-complement volume, **group-independently**. So there is no "symmetric SL(3) volume conjecture → 4·Vol".

Two consequences, both computed:
- The **SL(3) geometric volume `8.1195`** is the **principal-rep** (`Sym²` of the geometric SL(2)) *discrete
  flat-connection* datum (B244, classical) — not a large-color limit. Seeing it quantum-mechanically would need
  reps growing along the **Weyl vector `ρ`**, which the symmetric rep does not approach.
- The **fixed-`A` ('t Hooft / large-N)** generalized volume *is* nonzero and `A`-dependent (`0` at `A=1`, `5.09` at
  `1.5`, `8.70` at `2.0`, `13.79` at `3.0`) — the **Q-deformed A-polynomial** volume (Aganagic–Vafa,
  arXiv:1204.4709), a **continuous** curve in `A`. It does not single out `8.1195` either.

## The honest map of the quantum↔classical edge (completing B244)
Three distinct limits, three distinct things — keeping them apart is the point:
| limit | what it sees | where |
|---|---|---|
| large **level** (fixed rep) | geometric saddle's Chern–Simons action, in the **phase** | B244 |
| large **color** (symmetric rep, `A=qᴺ`) | knot-**complement** volume `2.0299`, in the modulus, group-independent | **B246 (here)** |
| fixed **A** ('t Hooft) | continuous `A`-dependent generalized volume | B246 (here) |

The SL(3) geometric `8.1195` lives in **none** of these — it is the principal-rep classical complex volume (B244).
So thread 2's "the components are the classical saddles the WRT quantizes" is sharpened: the *symmetric* quantum
limit does **not** recover the SL(3) geometric volume; that volume is genuinely classical/principal-rep data.

## Verification
Formula validated in B245 (`p=1` = fundamental HOMFLY; `A=q²` = B240 colored Jones). The extrapolation model
`v(p)=V + c·log(p)/p + d/p` is the known figure-eight VC asymptotic (`J_N ~ N^{3/2} e^{N·Vol/2π}`). SU(2)
self-checks against the established VC (→2.0299). Firewall-clean. Anchors: B240 (colored Jones), B244 (Ptolemy SL(3)
volume), B245 (colored HOMFLY tool). Literature: Kashaev; H./J. Murakami (volume conjecture); Aganagic–Vafa
(Q-deformed A-polynomial / fixed-A volume).
