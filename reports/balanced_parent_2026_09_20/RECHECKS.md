# F08 execution and reading receipt

2026-09-20. The previous goal turn was progress, not a wait or blocker.
Initial authoritative state: clean branch audit/fork-2026-09-20 at
054bebb3. No scientific process was resumed or replaced on a timeout.

## Seal and new run

An initial hash listing was made before a pre-execution symbolic-expression
cleanup in the cusp derivative helper. The final producer hash was then
recomputed (`7c1fa8`) and that final value, with the other three scientific
files and two reused producer hashes, entered SEAL.json. No F08 producer
or test was executed before commit `89be4ccf`. The staged whitespace check
returned exit 0 (`32e6bc`).

Using the existing Python 3.12.1 / SymPy 1.14.0 environment:

```
python3.12 -m pytest -q reports/balanced_parent_2026_09_20/test_verify.py
```

Session 60270, initial chunk `a4b60b`, final `ea812a`, exit 0:
**19 passed in 2.88 s**. There was no failed F08 first run or correction
after observing these test outcomes. Returned output is transcribed here,
not represented as a separately saved raw terminal log.

The finite checks cover explicit local matrix identities and differential
expressions. Homogeneous descent, complete-domain passage, global Codazzi
identification and spectral pairing remain authored analytic arguments.
No global eigenfunctions or independently certified global kernel counts
were computed, and no theorem was tested only by matching prose strings.

## Unchanged antecedents

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py \
  reports/nonsplit_cusp_growth_2026_09_20/test_verify.py \
  reports/full_flag_growth_2026_09_20/test_verify.py \
  reports/parent_twist_gap_2026_09_20/test_verify.py \
  reports/isotropic_parent_core_2026_09_20/test_verify_v2.py \
  reports/core_gluing_invariance_2026_09_20/test_verify_v2.py
```

Session 24600, initial `d038dd`, final `0f62b4`, exit 0:
**123 passed, 1 warning in 23.91 s**. The warning is optional Plink tkinter
GUI availability. These are selected antecedents, not the repository-wide
suite or governance gates. F01-v1/R16/F06-v1/F07-v1 failures remain retained;
the corresponding failed versions are not silently included in a claim of
full green coverage. The working tree was not edited while either run lived.

Post-run hashes (`2f9dc6`) match all four new and two reused producers.
`git diff --exit-code 054bebb3 --` the seven F01--F07 report directories
returned exit 0 (`d2cc98`) before living findings were updated. Working
tree was clean after execution (`388a6a`).

## Repository retrieval and reading

The three already_banked query strings are in DESIGN.md. They are not
universal absence tests. The broad initial regex mixed geometric keywords
with irrelevant occurrences; a Git grep over all report/docs/frontier/test
content also returned truncated output. Neither supports an absence claim.
Narrow filename and body searches followed. R39's full proof was read at
available local pin 8d2cced2; the attempted working-tree path was absent,
so Git supplied that body rather than assuming no prior result existed.

Read R27's finite-twist proof and reductivity follow-on design, F05's
producer, F06's corrected material, and B356's full findings. B356's finite-
group factor-route reality is credited background, not the new operator
claim. B926 was inspected as an incidental hit; its old broad wall language
and withdrawn physical numerical comparisons are not adopted. The original
report-guided all-history inventory remains the available pinned population.
No new all-remote-head retrieval succeeded or was claimed this turn.

## Primary literature, personally read

- [Braun et al. arXiv:1812.06072v2](https://arxiv.org/html/1812.06072v2):
  equations 2.9--2.24 and 2.34--2.42 with surrounding statements, rechecked
  for the full noncommuting action and positive-norm fermion operator.
- [Menal-Ferrer--Porti arXiv:1001.2242v2](https://arxiv.org/html/1001.2242v2):
  the introduction, coefficient definitions and vanishing-theorem scope
  rechecked. Their prior full reading is recorded in R27; it is not counted
  as a fresh complete reading here. Holomorphic symmetric powers are not
  the real-group tensor with conjugate used by F08.
- [Bera arXiv:2408.01522v2](https://arxiv.org/html/2408.01522v2):
  sections 1--4 personally read, including the explicit bundles/operators,
  Proposition 4.3 proof, Lemma 4.6 and the closed-base assumptions of
  section 4.2. Much of section 5 was also returned, but no theorem from it
  is used. The guessed v1 and unversioned HTML URLs initially failed; the
  abstract's actual v2 HTML link succeeded. No abstract-only theorem
  transfer or independent census verification is claimed.

The Codazzi literature supplies a real comparison and further source trail,
not a physical identification between the two actions. Other search-result
snippets about bending, standard representations and Lorentz coefficients
were not used as proof. No PDF, subagent summary, new empirical premise,
external message, publication or shared bank allocation was used.
