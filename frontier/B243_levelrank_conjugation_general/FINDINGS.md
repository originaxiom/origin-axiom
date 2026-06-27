# B243 — the level-rank=conjugation mechanism across levels: universal, and a refuted "metallic ladder"

**Status: banked observation (frontier). Nothing to `CLAIMS.md`; P1–P16 untouched; firewall intact.**
Generalizes B242. Run: `python levelrank_general.py` (pyenv); field degrees Sage-verified.

## Finding 1 — the mechanism is UNIVERSAL (not golden-specific)
B242 showed the level-rank duality `SU(2)₃↔SU(3)₂` acts as complex conjugation on the fundamental knot invariant at
`κ=5`. This is **level-independent**: for every `k`, `SU(2)_k ↔ SU(k)_2` at `q=e^{iπ/κ}` (`κ=k+2`) sends
`a=q² ↦ a=q^k = q^{κ−2} = −q^{−2}` (since `q^κ=e^{iπ}=−1`), so `a² ↦ q^{−4}=\overline{a²}` — **complex conjugation**.
Hence `SU(2)_k = SU(k)_2` **exactly iff the invariant is real iff the knot is amphicheiral**, at *every* level.

Verified `k=2..10`: figure-eight (amphicheiral) → exact coincidence at all `k`; trefoil (chiral) → complex-
conjugate pairs at all `k` (`k=2` is the self-dual `SU(2)₂↔SU(2)₂` point, `a=q²↦a=q²`). So B242's golden
coincidence is **one instance of a universal mechanism**; the golden value `−2/φ` is just the `k=3` specialization.
*(Specificity filter: the mechanism is universal; the value is level-specific.)*

## Finding 2 — the "metallic ladder" is REFUTED (verify-don't-trust caught it)
The figure-eight's level-rank-self-dual value `V(k)=2cos(4π/κ)−2cos(2π/κ)+1` is **golden** `−2/φ` at `k=3` and
**silver** `1−√2` at `k=6` — which *looks* like a metallic ladder `V(m²+2) ∈ ℚ(√(m²+4))`. **It is not.** Sage-
verified algebraic degrees:

| k | κ | V(k) | field |
|---|---|---|---|
| 1,2,4,8 | 3,4,6,10 | `1, −1, −1, 0` | **ℚ** (rational) |
| **3** | **5** | `−2/φ` | **ℚ(√5)** golden (m=1) |
| **6** | **8** | `1−√2` | **ℚ(√2)** silver (m=2) |
| 10 | 12 | `2−√3` | ℚ(√3) |
| 5,7,9,**11**,12 | 7,9,11,**13**,14 | — | degree 3,3,5,**6**,3 |

`V(k)` is quadratic-or-rational exactly at the small-`φ(κ)` levels; the **only** quadratic ones are
`k∈{3,6,10}` (`√5, √2, √3`). Golden (`κ=5`) and silver (`κ=8`) coincide with metallic fields `m=1,2` **only because
5 and 8 happen to be those levels** — **bronze** (`κ=13`, `m=3`) has `deg V(11)=6`, **not in `ℚ(√13)`**. The metallic
correspondence is a **2-case coincidence**, not a ladder. *(A seductive pattern, refuted at `m=3` before banking.)*

## Finding 3 — scope of the clean statement
The exact "`=`conjugation" holds for the **self-transpose fundamental** rep (single box, `Rᵀ=R`). For higher colors
the level-rank duality **transposes** the Young diagram (`SU(2)_k` color `N` ↔ `SU(k)_2` in the column/antisymmetric
`Λ^{N−1}`), relating *different* invariants — so it is a genuine duality, not pure conjugation.

## Net
A universal mechanism (deflated from golden-specific) + a refuted ladder (the golden/silver metallic values are a
coincidence of the `φ(κ)≤2`-small levels, not a pattern). Firewall-clean quantum-topology. Anchors: B242 (the
κ=5 case), B238 (level-rank WRT), B204 (metallic WRT period), B240/B241 (amphichirality). Literature: Naculich–
Schnitzer / arXiv:2106.15012 (level-rank duality of knot invariants).
