# B242 — the three SU(3)'s of the figure-eight: a trichotomy on three faces

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Run: `python trichotomy.py` (pyenv). HOMFLY polynomials Sage/SnapPy-verified.

## The trichotomy — three distinct SU(3)'s, one per face
The figure-eight carries **three genuinely different objects** sharing the letters "SU(3)", one on each of three
of its four faces:

| # | SU(3) object | face | what it is | specificity |
|---|---|---|---|---|
| **(1)** | **SL(3,ℂ) character variety** [B71] | classical geometry | `Fix(T₁²)` = 3 components, dim 2 (V0 geometric=Sym², W1/W2 Dehn-filling) — the space of SL(3,ℂ) flat connections | golden/object (a variety) |
| **(2)** | **level-rank gauge `SU(3)₂`** [B238] | quantum | a Chern–Simons gauge group at level 2, dual to `SU(2)₃` (`κ=k+N=5`); knot value `−2/φ`, bundle WRT `−1/φ` | figure-eight-specific |
| **(3)** | **Gang–Yonekura flavor `SU(3)`** [B241, arXiv:1803.04009] | SCFT | a global *flavor* symmetry of `T[K]`, from the `A₁` (SU(2)) theory | **twist-universal** |

They are distinct in **type** (a variety vs a number vs a symmetry) *and* **specificity** (golden vs golden vs
twist-universal). Conflating them is exactly the same-letter glue the program guards against.

## The new result — the (1)↔(2) edge, and the unifying mechanism
The relation between the quantum `SU(3)₂` and the level-`SU(2)₃` is the **level-rank duality**, and at the golden
root `q=e^{iπ/5}` (the shared `κ=5`) it acts on the fundamental KNOT invariant as **complex conjugation**:

> level-rank sends `a=qᴺ ↦ a=q^{κ−N}`; at `κ=5`, `q^{5−N}=q⁵·q^{−N}=−q^{−N}`, so `a² ↦ q^{−2N}=\overline{q^{2N}}`.

Therefore the `SU(2)₃` invariant (`a=q²`) and the `SU(3)₂` invariant (`a=q³`) coincide **exactly iff the invariant
is real iff the knot is amphicheiral** (`P(a)=P(a⁻¹)`). Computed (fundamental invariant `= HOMFLY(a=qᴺ, z=q−q⁻¹)`):

- **amphicheiral** `4₁, 6₃, 8₉` → `SU(2)₃ = SU(3)₂` **exactly**. The figure-eight: `−2/φ` (= B240's `J₂`; B238's
  bundle WRT is `−1/φ`, same golden field).
- **chiral** `3₁, 5₂` → `SU(2)₃` and `SU(3)₂` are genuine **complex conjugates** (differ).

**This unifies the two themes:** *amphichirality* (the B240/B241 keeper) **is exactly the condition** for the
*level-rank coincidence* (B238) to be exact. The golden value `−2/φ` then comes from `2cos(4π/5)=−φ`.

## The other edges
- **(1)↔(2): quantization.** The `SU(3)_k` WRT/colored invariant is the quantization of the SL(3,ℂ) character
  variety; (1) is the classical phase space (all levels), (2) is the level-2 quantum invariant (volume conjecture
  as `k→∞`). Same SL(3) gauge structure, classical vs quantum — related, not identical.
- **(3) vs (1),(2): distinct** [B241]. The flavor `SU(3)` is universal across all hyperbolic twist knots and is a
  symmetry of an SCFT, not a gauge group or a variety. Verified the negative (this session's lesson).

## Firewall note
A purely quantum-topology / character-variety / rep-theory result. It further sharpens the `H37` deflation: the
*three* SU(3)'s the program touches do **not** unify into one "gauge group" — they are three different objects
related by standard maps (quantization; level-rank). The physics framing (SU(3) = the strong force) stays
firewalled. Anchors: B71/B129 (SL(3,ℂ)), B238 (SU(3)₂ WRT), B240 (golden colored Jones / amphichirality),
B241 (GY distinction). Literature: Gang–Yonekura arXiv:1803.04009; Naculich–Schnitzer / arXiv:2106.15012
(level-rank duality of knot invariants).
