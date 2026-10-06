# B1477 — WHAT DECIDES THE SWAP: a mirror that shears the cusp fixes no spin structure (a theorem), the ¼ class is the rhombic class (1,205 amphichiral cusped manifolds, no exception, in the orbit form), and CS = 0 does not protect a survivor

**Verdict: PROVED** — for Theorem A, and for it alone. The shear law is graded separately and lower: **its sealed form
was KILLED on one manifold** (the registered kill fired; by the sealed reading rule that line reads NEGATIVE for the
sealed sentence), **its one-cusped form holds on the census (181 of 181), and its orbit form — written after and because
of the kill, sealed a second time, tested on a range not opened before — holds on 283 of 283 and 922 of 922.** A census
law, conjectural beyond the manifolds read. Scope: frame F-CI; the installed orientable cusped census (212,641 manifolds)
and the multi-component link exteriors of HTLinkExteriors (120,574); reach *general* for Theorems A and B, *class* for
the law. cc (main), 2026-10-06. First seal `673e52be5` (sha256 31acad53); second seal `1e11c51ce` (sha256 ea209e9d).
L246 between Phases 1c and 2; L194 sharpened. No value, no count. **0 of 19.**

**Credit where the arc turned.** The audit lane's R92 (2026-10-04: the isometries act on Spin(M) affinely; a bounded word
search certifies no swap) is the reason this arc exists: it made me look for certificates that enumerate nothing. The
torsion certificate (B1476 §2b) was the first; Theorem A is the second; Theorem B the third.

## 0. Seen first, and literature

The sweeps are quoted in the first seal (`VERDICT topic-sweep /cusp shape|rhombic|rectangular cusp|shear/: 60 of 1348 arcs
on main match (NEGATIVE 9, OPEN 6, PROVED 45)`, and two more): no arc relates the mirror's action on the cusp lattice to
a spin structure or to the ¼ class; the prior that matters is B1239 with lead L194 (the ¼ class is cusp-local; "SnapPy's
`Isometry` exposes the cusp action's linear part only"). **Literature:** not searched beyond what the record cites.
Calegari's lemma on the longitude's trace and Meyerhoff–Ouyang's cusped η–CS relation are cited from memory and unread on
this bench; **no cell and no proof here rests on either** (the owner's rule of 2026-10-06): the trace sign is computed on
every lift, and Theorems A and B are proved on this page. Whether the shear law is known I do not know; it is asked of
the audit lane.

## 1. Theorem A (proved), and what it certifies

*If an isometry f of a cusped hyperbolic M preserves a cusp and fixes a spin structure s (an SL(2,ℂ) lift ρ_s), the
peripheral sign character σ_s(γ) = tr ρ_s(γ)/2 ∈ {±1} is f_*-invariant.* (τγ is conjugate to f_*γ; a parabolic's trace is
real.) A mirror acts on H₁ of an invariant cusp torus by an involution of determinant −1: **rectangular** (≡ 1 mod 2) or
**rhombic** (fixing one nonzero class w mod 2, exchanging the other two). *A rhombic mirror fixes no spin structure with
tr ρ_s(w) = −2.* On a one-cusped manifold w is the rational longitude L, all mirrors have the same type, and the type is
the parity of 2·Re(Mu/L) of the cusp shape.

**On the census (C2; `range_spin.py`): all 75 one-cusped amphichiral manifolds at CS ≡ ¼ are rhombic and have
tr ρ_s(L) = −2 on every lift — P2 holds, 75 of 75 — so on each of them NO spin structure is fixed by any mirror: 292 of
292 spin structures, by a proof whose only inputs are an exact integer matrix and three signs.** B1475's seven are among
them. The two routes to the type (SnapPy's exact isometry cusp maps; the cusp shape) agree on 181 of 181.

## 2. The shear law

| | sealed statement | result |
|---|---|---|
| **P1** (80%) | CS ≡ ¼·#{f-invariant cusps on which f is rhombic}, for every reversing f | **FAILS AS SEALED: 282 of 283.** One-cusped **181 of 181** (75 at ¼ all rhombic, 106 at 0 all rectangular); multi-cusped 101 of 102; **o10_150729** (five cusps, ¼) is MIXED — one of its mirrors fixes no cusp |
| **Q1** (90%, second seal) | the orbit form on the same 283 | **HOLDS: 283 of 283**, o10_150729 included (and t12067, the other member with an odd orbit longer than one) |
| **Q2** (80%, second seal) | the orbit form on every amphichiral multi-component link exterior | **HOLDS: 922 of 922** (305 two-, 339 three-, 194 four-, 74 five-, 10 six-cusped; 126 at ¼); 25 have an odd orbit longer than one; **on 9 of them the first seal's sentence would have been MIXED**; 1,037 of 120,574 exteriors unread (SnapPy could not decide their isometries) |

**What failed and why.** The sealed sentence counted cusps fixed by f itself. A mirror that moves cusps in an odd cycle
of length ℓ fixes none of them, yet f^ℓ is a mirror preserving each. **The orbit form:** *CS ≡ n(f)/4 (mod ½), n(f) the
number of odd cusp-orbits of f on which f^ℓ is rhombic.* It was written after seeing the kill and is graded as that: a
corrected statement, sealed anew before its cells ran, confirmed on a range I had not opened. **B1239's swap corollary
has the same hidden hypothesis** ("fill each swapped pair") and is false as stated — o10_150729 has a mirror fixing no
cusp and CS = ¼; it is true for mirrors with no odd cusp-orbit (addendum filed there).

**L194.** Its conjecture — a mirror acting freely on every cusp it preserves excludes ¼ — is contained in the law (a
free action on a torus is a glide, which needs a rectangular lattice), and the instrument gap it named is closed: the
linear part of the cusp action is enough. A census law, not a proof; the filling sketch of the first seal remains a
sketch.

## 3. Existence at zero: the equivalence for the manifold is dead

| | sealed statement | result |
|---|---|---|
| **P3** (97%) | no contradiction of Theorem A | **HOLDS.** No certified spin structure is torsion-real, none is witnessed. (The signed spectrum is the weakest certificate: symmetric to cutoff 2.5 on some spin structure of 10 of 67 ¼ members where A and the torsion both certify.) |
| **P4** (75%) | a torsion-real spin structure exists ⟺ CS ≡ 0 (rank one) | **FAILS: 167 of 174.** Seven zero-class, rectangular, one-cusped members have none, and no symmetric signed spectrum either: **v3103, t10425, o10_085947, o10_134228, o10_146654, o10_148196, o10_149515** |
| **P5** (80%) | B1476's nine zero-class cusped members: none NONE-CERTIFIED | **HOLDS:** 7 EXISTS by witness (m136 four of eight, s880 four of eight, s883 two of four — exactly its torsion-real count on m136), 2 UNDECIDED |
| **P6** (50%) | the 37 closed amphichiral manifolds: none NONE-CERTIFIED | **FAILS: 15 NONE-CERTIFIED**, 13 EXISTS, 9 UNDECIDED (six of the nine have a single spin structure, which every isometry fixes) |

**"A mirror-invariant spin structure exists ⟺ CS ≡ 0" is KILLED** — by v3103 among cusped manifolds and by m082(1,3)
among closed ones, with twenty more. What stands is one direction: at ¼ none survives (a theorem on the one-cusped
census members). At zero, and on closed manifolds where CS is always zero (B1239), something else decides.

**The spectrum instrument was validated after the first NONE verdicts and before they were believed** (post-seal,
disclosed): every word SnapPy returns carries its listed complex length (worst miss 5e−13), and the sign-free multiset
{tr²} is conjugation-symmetric on every manifold tried — so an asymmetry of the signed multiset is the signs'.

## 4. Theorem B (post-seal; proved; not a sealed prediction)

*A closed geodesic whose holonomy rotates by π has a purely imaginary trace on every lift. A mirror that fixes a spin
structure cannot map such a geodesic to itself (the trace would equal its own conjugate), nor can its odd powers; so it
permutes the rotation-π geodesics of each length in orbits of even size. Hence: **an odd number of rotation-π geodesics at
some length ⟹ no spin structure is fixed by any mirror*** — read off the unsigned length spectrum, with no spin structure
and no isometry in sight. `pi_geodesics.py` (cutoff 3.0, 196 manifolds of known status): an odd count occurs on 39
manifolds, **all 39 certified NONE**; on none of the 20 with a witnessed survivor and none of the 90 with torsion-real
candidates. It accounts for 11 of the 15 closed NONE manifolds, 3 of the 7 zero-class cusped ones, 25 of 64 at ¼.
**Unexplained at this cutoff:** v3103, t10425, o10_085947, o10_149515 and four closed manifolds (m078(5,1) among them) —
certified none, mechanism not identified. That residue is Phase 2's first cell.

## 5. What it means, and what it does not

- **For the family (the object, under the owner's rule).** Seven of its thirteen amphichiral rank-one members have a
  rhombic cusp and six a rectangular one; the seven are the ¼ members and the members on which no fermionic
  configuration is mirror-symmetric. A5 selected a rectangular member. The bit that separates them is a parity of the
  boundary torus' lattice under the mirror — the place the audit lane, by its own route, says "the boundary choice
  carries the asymmetry".
- **For chirality.** Where a hand can be registered without a continuous choice is now located and has a proof: at a
  rhombic cusp. The *sign* of the hand is still the ℤ/2 nothing selects. No four-dimensional chiral count follows.
- **For generations.** Nothing. This arc counts one bit.
- **The imported expectation, stated separately:** none was used.

## 6. Disclosed

Post-seal: the range was corrected before the seal to the installed census (212,641, not 61,911); the torsion cell's
`setup` was repaired on the controls before the seal; the spectrum validation, Theorem B and `pi_geodesics.py` are
post-seal and labelled; the orbit form is post-hoc with respect to the first seal and was sealed separately. 17 members'
spectra failed in SnapPy's Dirichlet construction and are unread. Numerical, not exact, except the integer cusp maps.
**The grading is mine and is offered for attack:** the sealed reading rule tied the arc's PROVED to P1 holding with no
MIXED; P1 has one. I have therefore not graded the law PROVED in any form, and I have kept the token PROVED for Theorem A,
which that rule's own NEGATIVE branch says stands. If an auditor reads the rule as binding the token, the token is
NEGATIVE for the sealed sentence and nothing else on this page changes.
