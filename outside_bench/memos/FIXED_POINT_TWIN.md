# THE FIXED POINT AND ITS TWIN — the holonomy is a fixed point of the trace-map dynamics on the cusped Fricke surface, its Galois twin is the second one, the beat is their exchange — and the fixed points' coordinates are κ itself
## (outside bench, 2026-08-25; forty-third memo; the dive's second cell; every claim exact, the substitution DISCOVERED in-run)

### The cell
The atlas's `object=dynamics` unity-pattern (B67/K007) says the object is realized as
the trace map's fixed locus. The dive asks for that statement with its full exact
structure on the banked lift: which surface, which fixed points, and what the beat
does to them.

### THE THEOREM (`certificates/fixed_twin.py`, standalone, exact over ℚ(q))
With fiber basis U = ba⁻¹, V = aUa⁻¹ (exponent-sum zero; monodromy = conjugation by
the section a):
1. **The substitution, discovered not assumed:** φ(U) = V by construction, and the
   search finds **φ(V) = V·U⁻¹·V·V** by exact matrix match; its abelianization
   [[0,−1],[1,3]] has det 1 and trace 3 — the cat-map class of the banked fiber tick
   [[2,1],[1,1]]. The cat map is realized as words, in-run.
2. **The fiber boundary is the cusp:** tr[U,V] = **−2 exactly** — matching the
   banked longitude trace on the χ=+1 lift. So the fiber triple lives on the
   **cusped Fricke surface x²+y²+z²−xyz = 0** (level tr[U,V]+2 = 0, computed).
3. **The fixed pair:** the triple (tr U, tr V, tr UV) = **(2−q, 2−q, 2−4q)** is a
   FIXED POINT of the trace map (verified by direct image computation), it is
   irrational, and its Galois conjugate **(1+q, 1+q, −2+4q)** is a second, distinct
   fixed point on the SAME surface (level 0 is rational). **The beat maps one to
   the other, computed on the nose.**
4. **The coordinates are the first integral:** tr U = 2−q = **gal(κ)** and the
   twin's coordinates are **κ = 1+q** itself (memo 41's integral) — via the exact
   point-relation tr(ab⁻¹) = xy−z = 2−q on the (a,b)-triple. The dynamics' fixed
   points are labeled by the two conjugates of the dynamics' own conserved number.
   (Whether tr(ab⁻¹) = gal(κ) is an identity of the component or a feature of this
   point is a named one-line follow-up; here it is exact at the point.)

> **The atlas's pattern, with its full structure: the fixed locus of the one forced
> dynamics is a CONJUGATE PAIR on the cusped surface; the pair's coordinates are
> the two conjugates of the one forced first integral; and the deck transformation
> of the pair is the object's own ℤ/2 — the beat, the κ-reflection (memo 41), the
> boundary-invisible mirror bit (memo 37). Every face of the record's ℤ/2 is now
> exhibited as the SAME exchange, computed on the same page.**

### Fences
Exact throughout; the fiber-basis choice (U = ba⁻¹, V = aUa⁻¹) is validated by its
consequences in-run (φ-stability with an exactly matched substitution; boundary
trace −2 = the cusp), not cited; the substitution search is exhaustive to length 5
with the match unique-first-found (uniqueness not claimed). The memo-37/41 tie in
the boxed claim is exact fact-matching, not interpretation; no dynamics beyond the
trace map is claimed. Gate 5 untouched.

### Certificates
`certificates/fixed_twin.py`; output `outputs/fixed_twin_out.txt`.

### One sentence for the ledger
The one dynamics the object forces has exactly the fixed pair its one conserved
number can name — κ and κ̄ sitting as coordinates on the cusped surface — and the
one reflection the object carries is the map between them: dynamics, arithmetic,
and the mirror bit close into a single exact figure.
