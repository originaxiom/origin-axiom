# S029 — the homology torsion as the center / one-form symmetry of `T[M]` (`m → ℤ/m`)

**Status: `POSTULATED`.** Firewalled; not a claim. The **mathematical fact is proved** (B126); the **physics reading
is fenced** by five explicit kill conditions below. Nothing promotes to `../CLAIMS.md`; the physics chapter stays
CLOSED; P1–P16 untouched.

## The proved fact (math tier, B126/V115)

The orientable metallic bundle `M_m² = R^m L^m` has
```
   H₁(M_m) = ℤ ⊕ (ℤ/m)²     (Smith normal form of M_m² − I = m·M_m, invariant factors (m,m); SnapPy m=1..7).
```
The metallic parameter `m` **is** the order of the homology torsion — structural, no free choices. `m=1` (figure-eight)
has no torsion (`H₁=ℤ`); `m=2` has `(ℤ/2)²`; `m=3` has `(ℤ/3)²`; …

## The dictionary (established physics, citable)

In the 3d-3d correspondence the **torsion of `H₁(M)` controls the one-form (center) symmetry and the line-operator
spectrum / polarization of `T[M]`** (Dimofte–Gaiotto–Gukov arXiv:1108.4389; Aharony–Seiberg–Tachikawa "reading
between the lines"; Gukov–Hsin–Pei "Generalized Global Symmetries of `T[M]` theories" — **Part I** arXiv:2010.15890
= JHEP 04 (2021) 232 (framework/polarization), **Part II** arXiv:2511.13696 = JHEP 05 (2026) 087 (the
`H₁`-torsion → line-operator-spectrum result)). A `ℤ/n` center one-form symmetry is what an `SU(n)`-type gauge
theory carries.

## The suggestive match (the HOOK — and why it is fenced, not banked)

The chain `m → ℤ/m torsion → ℤ/m one-form symmetry` is a **well-defined mathematical chain with no free choices**.
The *evocative* continuation is: `ℤ/2` = center of `SU(2)`, `ℤ/3` = center of `SU(3)`, and the Standard Model gauge
group is `SU(3) × SU(2) × U(1)`. This is the most physics-adjacent structural fact in the project. **It is fenced**,
for five reasons — each a concrete kill condition (apply our own discipline; no exception for beauty):

1. **Center ≠ group.** `ℤ/2` is the center of `SU(2)`, `SO(3)`, **and** `Sp(1)`; `ℤ/n` does not determine the group.
   Pinning a group needs the full `T[M]` computation. *(Kill: the group is not recoverable from the center.)*
2. **The doubling.** We get `(ℤ/m)²`, **not** `ℤ/m` — but `SU(m)` has center `ℤ/m`. The second factor is the second
   homology generator of the torus fiber. *(Kill: the torsion has the wrong rank for an `SU(m)` center unless a
   capping/Dehn-filling halves it — uncomputed.)*
3. **`T[M]` is a rank-1 ABELIAN theory.** `T[4₁]` and its siblings are concrete small `U(1)` 3d N=2 SCFTs (two ideal
   tetrahedra; ≈ `U(1)` + 2 chirals; DGG). The `ℤ/m` is a one-form symmetry of *that abelian theory's line spectrum /
   polarization* — **not** evidence that the gauge group is `SU(m)`. **Conflating "has a `ℤ/m` one-form symmetry" with
   "is an `SU(m)` gauge theory" is the core category error.** *(Kill: the gauge group is `U(1)`, not `SU(m)`.)*
4. **Combining different `m` needs gluing.** The Standard Model needs `SU(3) × SU(2) × U(1)` *simultaneously* — one
   object with mixed torsion — not three separate manifolds `M_2, M_3`. The glued character variety is uncomputed.
   *(Kill: no single metallic object carries `ℤ/3 ⊕ ℤ/2` together.)*
5. **Small-integer value-matching.** `2` and `3` are the only small centers; matching the SM's small groups is the
   same *shape* as the killed value-matches (the cosmological constant `S014`, the CS-crossover `k≈4↔n=4`): a number
   coincided, with no derivation of *why that number*. *(Kill: same null-hypothesis family as `S014`.)*

**Companion fork (B127).** The "select an `SU(m)` *theory*" reading has the same shape as the Fibonacci-anyon reading:
both give the *symmetry / fusion data* (cheap) and never the *defining data* (the gauge group; the braiding/central
charge). The metallic family's quantization is **non-unitary + achiral** (CS=0, B127), so even the topological-matter
landing is the **Yang–Lee** side, fusion-rule-only — see `S030` and the K-C/K-D kills (`TOMBSTONES.md`).

**Now tombstoned as a bridge (B128, K-F).** A direct empirical test closes the "single torsion → broken vacuum →
`SU(n)`" sub-reading: `H₁` torsion tracks **periodicity / symmetry-order**, *not* chirality. The achiral double
`RRLLRRRLLL` is single-torsion (`ℤ/61`) while the **chiral** `(1,2,3)` is also single (`ℤ/157`), and the *doubled*
`(ℤ/m)²` is the high-symmetry **periodic** `(R^mL^m)^k` feature — so torsion rank carries no chirality/breaking
signal. Combined with kill #3 (rank-1 abelian; center≠gauge), the torsion→gauge bridge is **DEAD** (`K-F`,
`TOMBSTONES.md`, V117). The **mathematical fact** (`m` = torsion order, B126) stays banked; only the bridge reading is
killed.

**Strengthened (B129) — the fence is "abelian × discrete," not "rank 1."** A chat-only over-claim (never banked) held
the firewall is rank-1 because single bundles are one-cusped, "structurally sealed at rank 1." That is **wrong**: a
single bundle *is* one-cusped rank-1 abelian, but its finite **covers are multi-cusped and rank-2** — the silver
bundle `b++RRLL` has degree-2 covers reaching `(cusps, free_rank)=(2,2)` (verified, SnapPy). The fence survives because
a cover's extra cusps are **copies of the same boundary torus** permuted by the deck group: `T[cover]` is a discrete
gauging/orbifold of copies of the rank-1 abelian `T[M]`, **not** a new irreducible non-abelian theory. So the correct
fence is: **the metallic family produces abelian × discrete, never an irreducible *simple non-abelian* factor — rank
can grow by covering, but only by replication.** This *strengthens* kill #3 (it now covers the covers, not just the
base) and is corroborated from inside the tower by B129/`K012` (the SL(3) tower is sealed in ℚ(√−3): no off-sublocus
irreducible content, no new field). Same lesson as `K-F`: the structure yields more abelian/discrete data, never a
simple non-abelian factor.

## What would promote or kill it

The decisive computation is **Gang–Kim–Lee–Park technology**: construct `T[M_2]` and `T[M_3]` explicitly and read off
their gauge content + one-form-symmetry sector. If the line-operator spectrum genuinely organizes as `SU(2)`-/`SU(3)`-
*type* beyond the abelian `U(1)` core (kill #3), and if Dehn filling resolves the doubling (kill #2), the reading
strengthens. The literature ceiling stands regardless: even a maximally-favorable reading lands at **N=4 SYM / N=2\***
(B126 ladder), not the Standard Model — so this is, at most, a structural fingerprint, never a derivation of the SM.

**Reading the standing frame.** The *fact* (`m` = torsion order) is real and banked (B126); the *bridge* (→ `SU(m)` →
SM) is the firewalled overlay, kept here with kills so a future run neither re-derives it as a discovery nor forgets
the underlying structural fact.

## The SM-distinguishing firewall (cartography, B139 — a framing note, not a result)

The "SM through multiplicity" calculations (B139) decompose the question *"can multiplicity produce the Standard
Model?"* and sharpen the firewall statement. **Multiplicity permits MORE structure** — more abelian couplings
(coupling count = cusp count in 3d-3d), a discrete trace-fork (B131/`S032`-B), chiral objects (a CS-sign;
B128/`K011`) — **but it cannot permit the two structures that distinguish the SM from a generic emergent gauge
theory:**

1. a **simple non-abelian factor** — *contingently* blocked: each cusp gives a `U(1)` (Mostow); an `SU(2)` would
   need a cusp-swap acting as a **Weyl reflection** ("Gate-1", `S033`, prior LOW, tool-gated). This is the
   abelian-wall sibling of this entry's kill #3.
2. **irreducible chirality** — *structurally* blocked: the mirror (`swap_{R↔L} ∘ reverse`) sends the monodromy
   `M → Mᵀ`, so it preserves trace / char poly / Perron field / volume and only flips the CS sign (B139; the
   SM-side face of `det = −1 → CS = 0`, `../philosophy/P009`). Chirality is a CS-sign, **not** an inequivalence —
   the SM's parity violation (mirror = a *different* theory) is absent. Guard **MB9** (group-level ≠ gauge-level)
   keeps the *non-abelian group* generated by the monodromy from being misread as *non-abelian gauge* content.

This is a sharper phrasing than "permits but never forces": it names *which* two structures are unreachable and
*why* (one contingently, one structurally — both confirming the firewall, neither a crossing). The lone falsifier
is the genus ladder (`../docs/OPEN_LEADS.md`, B139-G), which would at most yield **emergent** chirality. Cross-ref
`S033` (Gate-1), `../philosophy/P009` (the chirality articulation + caveat), `../REPRODUCIBILITY.md` MB9.

Related: **B126**/V115 (the proved `H₁` torsion + the ladder map), `../knowledge/K006` (the 3d-3d firewall), `S024`
(the Hitchin/N=4 ceiling), `S027` (the quantum-modular door), `LADDER_LITERATURE.md` (citations), `../philosophy/P007`
(the reframe), `S030` (the Fibonacci/Yang–Lee fork, added B127). External: DGG arXiv:1108.4389;
Aharony–Seiberg–Tachikawa; Gukov–Hsin–Pei "Generalized Global Symmetries of `T[M]`" Part I arXiv:2010.15890 (JHEP
04(2021)232) + Part II arXiv:2511.13696 (JHEP 05(2026)087). *(Cho–Gang–Kim arXiv:2007.01532 — "M-theoretic Genesis"
— concerns non-hyperbolic 3-manifolds → unitary topological orders; it is **not** a `T[M]`-torsion citation, removed
here.)*
