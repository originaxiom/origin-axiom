# B1862 — The audit's first corrections: eight findings reproduced on main and corrected where they stand

*Main, 2026-11-10 (S306o). The advisor seat's audit (harvest row 1629; P-757) asks that every finding be reproduced on
main's own code before anything is changed. This arc corrects the first eight that main reproduced, taking main's
own recent arcs first. Each correction keeps the original text beside it, and each has a
lock that recomputes the corrected fact. No physical value is computed and nothing is compared with data. 0 of 19.*

## 1. The answer first

| finding | what was wrong | what is true, recomputed on main | where it is corrected |
|---|---|---|---|
| E13 | B567 said 21 distinct eigenvalues at level 165, and a lock pinned 21 | **20.** The projective order is 20, so every eigenvalue is a 20th root of one constant. Four eigenvalues are −1, where the angle's branch cut lies, and the lock counted them as two clusters | B567's findings; `tests/test_b567_hamiltonian.py` now counts on the circle |
| E3 | B1856 equated "invisible to every state" with E ≡ ±I mod 5 | **E ≡ +I only.** ρ(−I) is the parity operator, +1 on the even sector and −1 on the odd. Of the 643 rung-invisible defects, 338 have +I and 305 have −I | B1856's findings (the sentence, and a third condition), its verdict line, a new exact script and a computing lock |
| L5 | B1847's lock compared a list with its own sort, and subtracted literals from a literal | the claim behind the first is **true on the data**: Im τ rises strictly as s falls to 0 on eight rows | B1847's lock: a real check with a planted failing case |
| E4 | B952's lemma: "the centralizer of a set of semisimple elements contains a maximal torus" | **false without "commuting"**: in sl(2), diag(1, −1) and the swap have zero common centralizer | B952's findings; the cascade's own elements commute, so its conclusion stands |
| E11 | "sin(π/7) has no radical closed form" | it has none in **real** radicals; it is expressible by complex radicals (its field is abelian) | the dated literature page, with a note |
| E10 | the front page's command to look up one arc printed the corpus card whatever the arc | — | `scripts/atlas/query.py`: `card <arc>` prints that arc |
| E6 | B862's "kernel computed exactly" built no map: it tested a condition derived by hand in a comment | the fact, **ℤ₆**, is right, and is now computed from the map in exact arithmetic: six elements on a complete grid, cyclic | `frontier/B862_global_form/global_form.py`, a dated note in its findings, its lock |
| E8 | B854's consequence, "no non-abelian gauge algebra arises as the centralizer", read as general | it is computed for **the principal embedding only**, as the arc's own § 7 says | B854's findings (the sentence) and its verdict line |

- **No conclusion of any arc changes.** B567's negative, B1856's reading of the run of 6, B1847's value, B952's rank
  argument, B862's ℤ₆ and B854's negative all stand. What changes is a count, a quantifier, two checks that checked
  nothing, a lemma's hypothesis, a computation that was not one, a scope and a sentence.
- **Two of the eight were in arcs main verified this month** (B1856, B1847). B1856's gap was in main's own sentence: the
  two sentences before it already said that only the identity is a scalar on the whole space.

## 2. Each correction, with its check

- **E13, B567.**
  - The lock sorted the eigenvalues' angles on the line and clustered them. An eigenvalue at angle π is returned on
    both sides of the cut, so it was counted twice on some machines and once on others. The lock failed on the
    advisor seat's machine and passed on main's.
  - Now each eigenvalue is placed on the lattice of 20th roots of the constant that U²⁰ is a multiple of. The lock
    asserts that every eigenvalue lies on the lattice, that the count is at most the order, and the full multiplicity
    list: 12, 12, 12, 12, 11, 11, 10, 10, 10, 10, 7, 7, 7, 6, 6, 5, 5, 4, 4, 4, which sums to 165.
- **E3, B1856.**
  - `verification/parity_split.py` checks that ρ(S)² is the map e_x → e_(−x) against the representation itself, for
    either sign of the transform, and splits B1853's defects by the sign of E. It prints integers only.
  - The charge premise E ≡ ±I is "invisible to every state" only under a parity superselection rule. That is now a
    third condition in the arc's reading, beside the two it had.
  - The run of 6 has E ≡ +I. It was least among all 643, so it is least among the 338.
- **L5, B1847.** The rise is checked by a helper that a second test feeds a table with one value out of order. The
  distance from the record's readings is taken from the cluster's own least value.
- **E4, B952.** The lock computes, in exact arithmetic, the common centralizer in sl(2) of the two elements (dimension
  0), of one of them alone (dimension 1), and of two commuting semisimple elements of sl(3) (at least 2).
- **E11.** The lock recomputes the minimal polynomial, 64x⁶ − 112x⁴ + 56x² − 7, irreducible with six real roots.
- **E10.** The lock runs the command for two arcs and for an unknown one.
- **E6, B862.** The kernel of g(A, B, a) = diag(A e^{−2ia}, B e^{3ia}) is found by exact enumeration: the two centres
  and a grid of sixths, which is complete since the first block forces 2q into the thirds. A grid twelve times finer
  finds nothing more. The lock also runs the enumeration for another map and gets a different kernel, so the
  computation can tell maps apart. `results.json` did not change.
- **E8, B854.** A scope note on the sentence and on the verdict line. No computation.

## 2b. One of main's own fixes of the same day did not pass the audit's planted test

- **At Review 77 main widened the `tracked-deps` gate** after its fresh-clone suite found B1854's lock reading three
  ignored logs. The gate then read every lock's own-directory paths.
- **Main's reader planted the audit's violation PV25** (a lock that reads a file matched by `.gitignore`) in a scratch
  clone. The gate caught it only when the ignored file was on disk. In a clean checkout the file is absent, and the
  gate passed. The push hook runs in a clean checkout, so the gate could fire on the author's tree and never at push.
  It also read only one of the two idioms the record's locks use for their own directory.
- **Now** a lock's own-directory path that git would ignore is refused whether or not the file exists
  (`git check-ignore --no-index`), and the `os.path.join(os.path.dirname(__file__), …)` idiom is read. A base inside
  another folder is resolved with its chain: read without it, three older locks' force-added files resolved to the
  repository's root.
- **The controls** (`tests/test_tracked_deps_locks.py`) plant nothing on disk for the clean-checkout case: three idioms,
  each refused; a name that is absent and not ignored passes; a generator is left alone.

## 3. What is not done here

- **E4's acceptance row also asks for a lock on the rank of the centralizer that the cascade uses.** Not computed
  here. E4 is partly fixed.
- **E11 has two other parts** (a slice-dependent "golden factor"; fixed points said to lie on the upper half-plane).
  Not checked here.
- **E8's acceptance row also asks that "none was computed" be replaced by the banked table** of the other classes.
  Main has not located that table. E8 is partly fixed.
- **The other eight findings main has reproduced** (E2, E5, E7, L7, L9, L10, M1, M3) are not corrected here. They are
  next, with enforcement (the programme's WP-0.7, WP-0.8, WP-0.3).
- **The seat's re-audit decides whether each row is accepted.** Main's states are in B1861's `PROGRAMME.md` § 8.

## Seen first

- **The repo sweep:** for each finding, a grep for the old statement across the tree before the edit. "21 distinct"
  stands in B567's findings, its lock, and two dated logs; the logs are history and are not edited. "invisible to
  every state" stands in B1856's findings and verdict line and in the generated verdict view. The lemma's sentence
  stands in B952's findings only.
- **The literature:** none needed. Each fact is elementary and is recomputed.

## Disclosed

- **The audit found these; main did not.** Three of the arcs concerned had been read at decadal reviews.
- **B567's lock passed on main's machine with the wrong count.** A lock that passes at home is not evidence that the
  number is right; this one compared a count that depended on the sign of a rounding error.
- **The dated logs still carry B567's old count** (the changelog's and the progress log's entries of that day). They
  are append-only history.

## Reproduce

```
python3 -m pytest -q frontier/B1862_the_audits_first_corrections/verification/ tests/test_b567_hamiltonian.py \
  frontier/B1856_charge_or_symmetry_at_five_verified/verification/ frontier/B1847_the_level_surfaces_own_modulus/verification/
python3 -B frontier/B1856_charge_or_symmetry_at_five_verified/verification/parity_split.py
python3 scripts/atlas/query.py card B1812
```
