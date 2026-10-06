# B1477 — PREREGISTRATION: WHAT DECIDES THE SWAP — the mirror's shear on the cusp, the ¼ class, and existence at zero

**Sealed before any cell runs on any member other than the two controls.** cc (main), 2026-10-06. L246 between Phase 1c
(B1476) and Phase 2; pays or kills L194's cusp-local conjecture on the way. One sealed arc, kills named, no value
match, no physics banked.

**The question B1476 left.** At CS ≡ ¼ no spin structure survives the mirror (13 of 13, certified by the odd torsion);
at CS ≡ 0 the geometric lift is sometimes fixed and sometimes swapped. *What decides it?* Two questions, kept apart:
(A) what makes a spin structure impossible to fix — a mechanism, with a proof; (B) whether, where nothing forbids it, a
mirror-invariant spin structure actually exists — *an amphichiral manifold has a mirror-invariant spin structure exactly
when CS ≡ 0 (mod ½)*, the equivalence for the manifold that B1476's cells did not test.

## 0. Seen first

**The record, swept in its own vocabulary (2026-10-06).**
- `VERDICT topic-sweep /cusp shape|rhombic|rectangular cusp|shear/: 60 of 1348 arcs on main match (NEGATIVE 9, OPEN 6, PROVED 45)` — read: the matches are about the cusp *shape as a number* (B712, B762, B859: m004's 2√−3; B675: silver's −2i; B803: "the cusp is rectangular" against B486's hexagonal claim; B1294: "all eight cusp maps diagonal ±1" on m004). None relates the mirror's action on the cusp lattice to a spin structure or to the ¼ class.
- `VERDICT topic-sweep /longitude.*trace|trace.*longitude|Calegari/: 15 of 1348 arcs on main match (NEGATIVE 2, PROVED 13)` — read: longitude *holonomy* in the carrier and A-polynomial arcs (B67, B1113, B1149, B1295); none on the sign of the longitude's trace under a lift.
- `VERDICT topic-sweep /spin structure.*(cusp|torus|peripheral)|peripheral.*spin/: 2 of 1348 arcs on main match (PROVED 2)` — B940 (the Dirac run on (m004, ρ₁)) and B1233; neither states a peripheral obstruction.
- `already_banked --wide cusp shear rhombic spin longitude`: 0 hits on the ledger and scheduled surfaces; the arc-level matches (B1149, B1233, B1242, B1277, B1294) are the ones just read.
- **The prior that matters: B1239 and L194 (OPEN, ★★★).** B1239 proved the ¼ class excluded on closed amphichiral manifolds (APS) and on cusped ones whose mirror fixes no cusp (the swap corollary, bucket A 28 of 28), and located the residue on mirror-invariant cusps (bucket B: 6 zero, 5 quarter; every one-cusped amphichiral manifold). L194's refined conjecture: *a mirror acting freely on every cusp it preserves excludes ¼*; its stated instrument gap: "SnapPy's `Isometry` exposes the cusp action's linear part only … not the translation". **This arc proposes that the linear part is enough**: a free (glide) action needs a rectangular lattice, so "rhombic ⟺ ¼" would contain L194's conjecture.
- B279 (the mirror fixes both spin structures of every knot complement), B1474/B1475/B1476 (the swap table, the pairing, the ¼ law and its torsion certificate), the audit lane's R92 (the affine action; a bounded search certifies no swap).

**What I have computed or seen before this seal (all of it).**
- B1476's stored tables: the family's thirteen (classes, witnesses, torsion on every spin structure); the outside census (the geometric lift's fate on 15 cusped and 37 closed; the odd torsion on every spin structure of the twelve rank-one cusped members: 0 torsion-real on the six at ¼, two or more on the six at 0, m136 four of eight). B1239's bucket counts (28 / 6+5 / 8+3+2754) and example names, not which bucket-B member has which cusp type.
- **The two controls, and only these, on every instrument of this arc** (run 2026-10-06 in the session scratchpad, before the seal):

  | | m004 (CS 0) | m003 (CS ¼) |
  |---|---|---|
  | reversing isometries (of 8) | 4, each f(L) = −L, f(Mu) = Mu + 4L — **rectangular** | 4, each f(Mu) = ±(Mu − 3L) — **rhombic** |
  | 2·Re(shape Mu/L) | −4.000 | 3.000 |
  | tr ρ_s(L) on the two lifts | −2, −2 | −2, −2 |
  | tr ρ_s(Mu) | +2, −2 | −2, +2 |
  | Theorem A certifies non-invariant | 0 of 2 | 2 of 2 |
  | odd torsion real | 2 of 2 | 0 of 2 |
  | signed trace spectrum symmetric (cutoff 3.0: 37 / 35 geodesics) | 2 of 2 | 0 of 2 (parts at length 0.8626) |
  | witness (matrix route) | both fixed | none; NONE-CERTIFIED |

  and one chiral control for the criterion's failing side: m015 has no reversing isometry and 2·Re(shape) = 2.3303 (not an integer).
- A sketch, by thought and not by computation, of why the ¼ class should follow the shear (§2, labelled as a sketch).

**Nothing else.** In particular the cusp type of no member other than m004 and m003 has been computed by me; that knot complements are rectangular (the meridian is preserved) is general knowledge.

## 1. Theorem A (proved here; the cells test its hypotheses and its consequences)

Let M be a cusped hyperbolic 3-manifold, c a cusp with peripheral subgroup P ≅ ℤ², and s a spin structure, that is an
SL(2,ℂ) lift ρ_s of the holonomy. Every γ ∈ P is parabolic, so tr ρ_s(γ) = 2σ_s(γ) with σ_s(γ) = ±1, and σ_s : P → {±1} is a
homomorphism (commuting parabolics multiply their signs). 

**Theorem A.** *If an isometry f of M with f(c) = c fixes s, then σ_s ∘ f_* = σ_s on P.*

*Proof.* f fixes s means there are an automorphism τ of π₁ inducing f and C ∈ SL(2,ℂ) with C·ρ_s(g)·C⁻¹ = ρ_s(τg) (f
preserving orientation) or C·conj ρ_s(g)·C⁻¹ = ρ_s(τg) (f reversing it), for every g, with no sign character. For γ ∈ P,
τγ is conjugate to f_*γ, so 2σ_s(f_*γ) = tr ρ_s(τγ) = tr ρ_s(γ) or its conjugate = 2σ_s(γ), the trace being real. ∎

**Corollary (the rhombic obstruction).** An orientation-reversing f preserving c acts on H₁(T_c; ℤ) by an involution F of
determinant −1, so F is conjugate in GL(2,ℤ) to diag(1, −1) (**rectangular**: F ≡ 1 mod 2) or to the swap of coordinates
(**rhombic**: F mod 2 fixes exactly one nonzero class w and exchanges the other two, x and x + w). In the rhombic case
σ_s ∘ f_* = σ_s forces σ_s(x) = σ_s(x + w), that is **σ_s(w) = +1**. So: *if the mirror is rhombic on an invariant cusp
and tr ρ_s(w) = −2, then f does not fix s.* On a one-cusped M the fixed class is the rational longitude L (f preserves
the kernel of H₁(T) → H₁(M; ℚ)), every reversing isometry has the same type (two of them differ by an
orientation-preserving isometry, which acts by ±1 on H₁(T) because it too preserves L), and in a basis (Mu, L) the type
is the parity of the shear k in f(Mu) = ∓Mu + kL — equivalently 2·Re(Mu/L) of the cusp shape is odd (rhombic) or even
(rectangular). When L has odd order in H₁(M; ℤ) the sign σ_s(L) is the same for every s; it is −1 on both controls
(the longitude bounds, and a bounding curve carries the bounding spin structure — Calegari's lemma, **cited from memory
and not read on this bench; the cells compute tr ρ_s(L) on every member and do not rely on it**).

**So on a one-cusped amphichiral manifold with a rhombic cusp and tr ρ_s(L) = −2 for every s, no spin structure is fixed
by any mirror** — a proof, with no enumeration of isometries by word search and no numerics beyond the signs of three
traces. That is the mechanism proposed for B1475's seven.

## 2. The conjecture the cells test (not proved)

**The shear law.** *For an amphichiral cusped hyperbolic M and any orientation-reversing isometry f:
CS(M) ≡ ¼ · #{cusps c : f(c) = c and f is rhombic on c} (mod ½).* It contains B1239's swap corollary (no invariant cusp
⟹ 0) and L194's conjecture (free on a cusp ⟹ glide ⟹ rectangular ⟹ no contribution).

*Sketch, labelled as a sketch.* Filling an invariant cusp along an invariant slope gives a closed amphichiral manifold,
whose CS is ≡ 0 (B1239); the core geodesic is preserved by the extended mirror, so its torsion θ satisfies
θ ≡ −θ + 2πj with j the shear in the basis (slope, dual), giving θ ≡ jπ and a contribution j/4 to the filling formula.
What is **not** proved is that the analytic term at the invariant filling equals CS(M): B1239 already noted there is no
sequence of invariant slopes to take a limit over. The law is therefore a conjecture, and the census decides it.

## 3. The cells, fixed now

- **C1 — the shear census** (`range_census.py`). Range: every manifold of the installed orientable cusped census
  (SnapPy 3.3.2: 212,641 manifolds, at most ten tetrahedra — the family's o10 members lie inside it; B1239 read its first
  61,911), one-cusped or not. Prefilter: CS class 0 or ¼ to 1e−7 (amphichirality forces it; a manifold whose CS is
  unavailable is kept). Then SnapPy's complete self-isometry list (`is_isometric_to(self, return_isometries=True)`): for
  every reversing f, the invariant cusps and the rhombic ones (cusp map ≢ 1 mod 2). Recorded per manifold: the parity of
  the rhombic count for every reversing f (MIXED if they disagree).
- **C2 — Theorem A's hypotheses and reach** (`range_spin.py`, (a)–(b)). On every one-cusped amphichiral member of C1 (cap,
  declared now: the first 400 in census order if there are more, and the family's thirteen whatever their position): tr ρ_s(L) and tr ρ_s(Mu) on every lift; the shear by
  the exact route and by the shape; the number of spin structures Theorem A certifies non-invariant.
- **C3 — the two numerical certificates on the same members** (`range_spin.py`, (c)–(d)): the odd torsion R₁ at t = 2, 3,
  0.6 on every spin structure (H₁ of rank one; real or imaginary to 1e−9 counts as real, the lenient reading of B1476);
  the spin-signed trace spectrum T_s = {tr ρ_s(γ) : γ a closed geodesic of length ≤ 2.5} against its complex conjugate as
  multisets (`signed_spectrum.py`; traces rounded to 1e−6). Each is necessary for invariance, neither sufficient.
- **C4 — existence at zero** (`zero_witness.py`). On every zero-class member of B1476's outside lists (nine cusped, 37
  closed): every reversing automorphism the matrix route finds (word length 5, 6, 7; up to 40), its η, and for every
  spin structure χ the partner (η·χ)∘τ⁻¹; a fixed χ is a **witness**. Non-existence is never read off the search: a spin
  structure is certified non-invariant only by Theorem A, by non-real torsion (B1476's `r92_certificate.json`, rank one),
  or by an asymmetric signed spectrum at cutoff 3.0. Member verdict: **EXISTS** / **NONE-CERTIFIED** / **UNDECIDED**.

**Instruments at the seal (sha256, first 16):** `cusp_shear.py` 77dee8454a311b02, `signed_spectrum.py` 5938c76e9042a440, `range_census.py` 21be4ca1b77eec48, `range_spin.py` 59bebfd596cc50dd, `zero_witness.py` 4c7cc47bfbcb5cb7. Compiled against the record's APIs; run on m004, m003 (and m015 for the failing side) only.

## 4. Predictions, with priors

| | prediction | prior |
|---|---|---|
| **P1** | **the shear law on the whole range:** on every amphichiral manifold C1 finds, CS ≡ ¼ ⟺ the rhombic count is odd, the same for every reversing isometry (no MIXED) | 80% |
| **P2** | **Theorem A covers the ¼ class:** on every one-cusped member at ¼ the mirror is rhombic *and* tr ρ_s(L) = −2 on every lift — so "no spin structure survives" is a theorem there, with no numerics beyond three signs | 70% (it fails if some ¼ member's longitude has even order and a lift with tr L = +2) |
| **P3** | **no contradiction of the theorem:** no spin structure that Theorem A certifies non-invariant is torsion-real-and-spectrum-symmetric-and-witnessed; in particular no witness on a certified one | 97% (a violation is an instrument error and is reported as one) |
| **P4** | **the torsion side of the equivalence on the range:** a one-cusped rank-one amphichiral member has a torsion-real spin structure exactly when CS ≡ 0 (B1476: 25 of 25) | 75% |
| **P5** | **existence at zero, cusped:** each of the nine zero-class cusped members outside the family is EXISTS or UNDECIDED — none NONE-CERTIFIED | 80% |
| **P6** | **existence at zero, closed:** each of the 37 closed amphichiral census manifolds is EXISTS or UNDECIDED — none NONE-CERTIFIED | 50% (the geometric lift is swapped on 14 of the 25 decided; nothing I know forces a survivor) |

**Kills, named.** *The shear law* (P1) dies on one amphichiral manifold with (¼, even) or (0, odd), or one MIXED.
*The equivalence for the manifold* — "a mirror-invariant spin structure exists ⟺ CS ≡ 0" — dies on one zero-class member
with every spin structure certified non-invariant (P5/P6), or one ¼ member with a witness (excluded where P2 holds).
*The mechanism's reach* (P2) dies on a ¼ member that Theorem A does not fully cover; the law may survive it, and then the
remaining spin structures stand on the numerical certificates alone and the page says so.

**Reading rule for the verdict.** PROVED (reach: the range) iff P1 holds on every member with no MIXED and P3 shows no
violation — then L194 is paid as a census law with a proved spin corollary, its own derivation still open. NEGATIVE
(scoped to this mechanism) iff P1 has an exception: the shear does not decide the ¼ class, and Theorem A stands as a
sufficient condition only. The existence question (P5, P6) is reported on its own line whatever P1 does: HOLDS ON THE
TESTED / KILLED BY ⟨member⟩ / OPEN.

## 5. Disclosed

- The idea came while correcting B1476: the audit lane's R92 (the affine action, the insufficiency of a bounded search)
  made me look for a certificate that enumerates nothing; the torsion certificate was the first, Theorem A is the
  second. **R92 is credited as the cause of both.**
- The controls were run on every instrument before this seal (table in §0); an instrument fault found on them — the
  torsion cell picked up B1476's φ-free `setup` through a module-level replacement — was repaired before the seal.
- The witness route's coverage is bounded (word length ≤ 7); this arc reads existence only from witnesses and
  non-existence only from certificates, so the bound cannot produce a false kill, only an UNDECIDED.
- The signed spectrum rests on SnapPy's length spectrum being complete to the cutoff (numerical, not certified) and on
  the words it returns being words in the unsimplified presentation the lifts are computed on (checked on the two
  controls by the symmetric / asymmetric outcome, not otherwise).
- Numerical, not exact: SnapPy HP holonomy, traces to 1e−6, torsion to 1e−9. Theorem A's use needs only signs.
- **The owner's rule of 2026-10-06 (verify all load-bearing mathematics, published or not) — applied:** no cited result
  is load-bearing here. Theorem A is proved on this page; the longitude's trace sign is computed on every lift rather
  than taken from Calegari's lemma (cited from memory, unread on this bench); Meyerhoff–Ouyang's cusped η–CS relation is
  cited by L194 and unread, and no cell uses it; B1239's closed-manifold exclusion (APS as printed in CGHN, read there) is
  used only in the sketch of §2, which is not a proof and is not claimed.
- Under the owner's rule the statements are about the family and the census, member by member; "the object" is not
  written for a fact about m004.

## 6. Scope

Frame: F-CI — the mirror's action on spin structures (SL(2,ℂ) lifts), the cusp lattice, and the Chern–Simons class.
Objects: the orientable cusped census (C1); its one-cusped amphichiral members (C2, C3); B1476's zero-class lists (C4).
Reach: *general* for Theorem A (proved); *class* for the shear law (a census law on the range, conjectural beyond).
No physical quantity is computed and none is matched. **0 of 19 before; 0 of 19 after, whatever the cells return.**
