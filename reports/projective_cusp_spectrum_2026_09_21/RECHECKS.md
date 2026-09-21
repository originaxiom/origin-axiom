# F11 execution, reading and failure-preservation receipt

September 21, 2026. Initial state clean at 5dc9b730 on
audit/fork-2026-09-20. The preceding goal turn was progress, not a wait
or blocker. No live scientific handle was inherited or restarted.

## Reading and scope

Read F10's frozen proof and F02's domain proof, F07's bounded-complex
argument and R27's Fox/affine cocycle implementations. Revisited the
working rules, campaign and relevant framework/ladder/lead/law/kill
entries. Broad combined searches produced truncated output; that is
not counted as a fresh full-document or population read.

The two already_banked queries in DESIGN.md returned 132 broad hits /
4 settled multi-term hits, and 29 broad hits / 1 settled multi-term hit,
respectively. The five flagged B1149/B1186/B598/B975/B870 FINDINGS bodies
were read; truncated combined outputs were followed by bounded rereads,
including all of B598's later corrections. These are navigation counts,
not missing-result or novelty certificates. No fresh all-head fetch.

Personally read primary HTML Arnold--Falk--Winther 0906.4325v3 section
3.1 and the initial 3.2 discussion: closed-range cohomology, Hodge
decomposition, compactness implication and domains. This is a selected
theory-section reading, not the entire paper. Bruning--Lesch's publisher
abstract was located, but no uninspected proof from it is used. No PDF
or applicable artifact skill was used this turn. No subagents were used.

## Original seal and first outcome

Four original scientific files and F10's imported producer were hashed
in d9e65b. SEAL.json was generated from the command output. Explicit
staging and whitespace check passed, and commit **85454725** (16d8c7)
completed before execution. Existing Python 3.12.1 / SymPy 1.14.0:

```
python3.12 -m pytest -q reports/projective_cusp_spectrum_2026_09_21/test_verify.py
```

Session 90549: initial 1a1ae8, f9ea8e, dabca7, final e7641e, exit 1:
**3 failed, 27 passed in 64.87s**. FIRST_RUN_TRANSCRIPT.txt transcribes
the received chunks and complete failure reports; it is explicitly not
presented as a separately captured raw terminal file. The failed IDs
are the three nontrivial phases of
test_every_positive_rank_exception_is_geometric. They returned TWO
positive rank roots, not the expected at-most-one root at q=1.

The unchanged producer was then run to display all maximal-minor
certificates. Session 86013, initial cc2bd8, 69d806, final e5c71c,
exit 0. MINOR_LOCUS_OUTPUT.txt contains the concatenated tool-returned
stdout. It gives (q-1)^2, q^2-34q+1 and q^2-14q+1, with 70 minors
per matrix, only q-power denominators and B gcd 1 throughout.
This is a discovery AGAINST the prior, not a numerical or code repair.

An optional process-list command was denied by the sandbox (daff58).
The live pytest handle itself supplied terminal state, so no process
was restarted or inferred stopped from that denial. Post-original-run
9b1b62 showed clean status and the original five hashes unchanged.

## Unchanged antecedents

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py \
  reports/nonsplit_cusp_growth_2026_09_20/test_verify.py \
  reports/full_flag_growth_2026_09_20/test_verify.py \
  reports/parent_twist_gap_2026_09_20/test_verify.py \
  reports/isotropic_parent_core_2026_09_20/test_verify_v2.py \
  reports/core_gluing_invariance_2026_09_20/test_verify_v2.py \
  reports/balanced_parent_2026_09_20/test_verify.py \
  reports/balanced_vertex_2026_09_20/test_verify.py \
  reports/projective_escape_2026_09_21/test_verify.py \
  tests/test_physical_bridge_parent_vertex.py
```

Session 3354, initial 9dfefa, final 255c6d, exit 0:
**196 passed, 1 warning in 39.17s**. Plink's optional tkinter GUI
warning did not affect these non-GUI checks. This is not a full-suite
claim, and retained failed test versions are not reclassified passing.
The working tree stayed read-only during the original scientific runs.

## Sealed post-failure correction and stronger tests

EXCEPTION_ADDENDUM.md explicitly withdraws the failed expectation and
states the new count to test: rank J=3 and H1=1 at both roots for each
nontrivial character and its dual. New exception_verify.py uses exact
arithmetic in the relevant quadratic field, with independent nonzero
3-minor and non-coboundary certificates. test_verify_v2.py re-exports
every unaffected original test with its parameterization, replaces only
the named failed expectation, and tests that accounting explicitly.

Five correction/output files plus the two unchanged original scripts
were hashed in d301c8. CORRECTION_SEAL.json was generated from that
output. Commit **15c32b3c**, chunk 499285, preceded the follow-up:

```
python3.12 -m pytest -q reports/projective_cusp_spectrum_2026_09_21/test_verify_v2.py
```

Session 41298, initial d48c05, 3d61ec, final e4a40d, exit 0:
**40 passed in 173.71s**. CORRECTED_TEST_OUTPUT.txt is the concatenated
tool-returned stdout. No scientific edits occurred during or after it.
This does not erase the original three failures or turn the correction
into a pre-discovery prediction.

The sealed exceptional producer was separately run for retained explicit
witnesses: session 99716, initial 22063c, 9b42b1, 9e38e5, final 819364,
exit 0. EXCEPTION_WITNESSES.txt concatenates those tool-returned stdout
chunks. All six character/dual calculations have ranks 4 and 3, H1=1,
closed cocycle and non-boundary witnesses. These are cochain certificates,
not spatial harmonic mode profiles or an independent code implementation.

The read-only check 646713 verified all 12 original/correction/imported
hash entries and a clean tree. A diff from 5dc9b730 over F10, F08/F09
and the other-seat physical-bridge scientific/report directory was empty
before reporting follow-through. No prior scientific file was modified.

## Verification grade

Reporting-only render_loci.py plotted the exact roots already verified,
without a new spectral fit. Render 0c4d2e, session 54344, final 07315c,
exit 0; Matplotlib used a temporary cache after its default cache was
unwritable. EXCEPTIONAL_LOCI.png was viewed: labels were legible with
no clipping, the geometric endpoint was explicitly excluded from the
L2 theorem, and neither axis nor caption identified q with a physical
constant. Check cd8f1e verified whitespace, 12 sealed hash entries,
13 report links and an empty diff for the original scientific files.
After context continuation, 21c703 reconfirmed the branch and exact
report-only working-tree changes; no scientific run was restarted.

Exact finite checks verify the full-frequency algebraic homotopy,
matrix radial identities, norm controls, all-parameter member rank loci
and explicit exceptional classes. Complete-space compactness and the
L2 cohomology comparison are authored analytic arguments with the stated
hypotheses, not consequences of finite sampling or external peer review.
No global harmonic-metric existence computation or physical anomaly /
interaction / gravity completion was performed. Only local reporting
and predecessor follow-through pointers follow these runs; no push,
main bank, shared B allocation or repository-wide certification.
