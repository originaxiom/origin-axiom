# F10 reading, review and execution receipt

September 21, 2026. Initial fork HEAD 9c0d1c67, branch
audit/fork-2026-09-20. Pending F10 drafts were the only untracked work;
they had not been executed. No other scientific process was restarted.
This is local follow-through of the report-guided audit, not an assertion
that the full TOE objective has been achieved.

## Reading and prior art

The prior queries and exact scope are in DESIGN.md. B1115/B1122 were
inspected; a combined output was truncated and is not a complete-reading
certificate. B101 and the SL4 paper README distinguish their constructions
from the representation used here. No new all-head fetch or absence
certificate was performed. Old history-sweep receipts remain historical.

The main author personally read the full extracted text of the 26-page
Ballas author PDF dated March 28, 2014 in consecutive slices, including
definitions, geometry and section-6 matrices. The matrix page (PDF page 22)
was rendered with Poppler and visually inspected; not every page was
visually reviewed. Web PDF screenshots failed, so a local rendering was
used. Initial sandbox download failed DNS; the same read-only primary-source
download subsequently succeeded with network approval. The PDF SHA256 is
cdb095d17aba2f228ede3bfc52731afd66caa569c02bbf32ed97ed621d874468.
The URL is linked at point of use in FINDINGS.md. No repository copy or
redistribution of the full paper is claimed. No agent summarized a paper.

The PDF skill guided extraction and visual matrix verification. Its complete
current instructions were read. Heusener--Porti and a Ballas predecessor
were discovered but not read or used as proved inputs. Published nearby
convex geometry is credited, not independently reproved.

The working/pre-compute and banking protocols were revisited; the fork's
local-report policy keeps this work outside shared B numbering and main
banking. Other-seat banking records are historical inputs, not certificates
of this fork. No empirical premise or measured-constant comparison is used.

## Independent analytic checks and seal

One bounded analytic reviewer checked the general cusp norm lower bound,
its sharp rank-one comparator and whole-boundary cohomology argument.
A second read-only reviewer checked the local moment/norm/gauge formulas
and pairing scope by hand. Neither ran scripts, edited files or read/summarized
papers. These reviews are not external peer review or independent code.

Before sealing, the second review prompted the explicit word 'invertible'
in the antilinear-map proof. A later suggestion to narrow the finite-cover
phrase 'flat bundle maps' is carried in FINDINGS.md's explicit scope;
the sealed proof was not silently edited. The hand-derived determinant
certificate was confirmed from the unchanged symbolic producer below.

All four scientific files and three transitive producers were hashed in
aa3a3e; SEAL.json was constructed from that command output. Explicit-file
staging and whitespace check passed. Science commit **ee0d62ea**, chunk
143199, preceded the first run. No scientific edits followed execution.

## First execution

Existing Python 3.12.1, SymPy 1.14.0 environment:

```
python3.12 -m pytest -q reports/projective_escape_2026_09_21/test_verify.py
```

Session 93114, initial 924d75, final 7b2c6b, exit 0:

```
20 passed in 4.05s
```

Checks include the knot relation, longitude word and characteristic
polynomial, actual geometric-point intertwiner, cusp conjugacy, finite
power controls, projective-rescaling distinction, full matrix flatness
and moment, norm asymptotics, wrong-profile comparator, diagonal control,
torus chain contraction and the energy quadratic-form identity.
The infinite-domain conclusions remain authored analytic arguments;
finite controls do not replace them. No global PDE or eigenmode census ran.

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
  tests/test_physical_bridge_parent_vertex.py
```

Session 22627, initial 278bfd, intermediate 0774fb, final 5dadc1,
exit 0: **176 passed, 1 warning in 29.18s**. The optional Plink GUI's
tkinter import warning did not affect these non-GUI checks. The working
tree was read-only during both scientific suites. Previously retained
failed versions were not erased or included as passing tests.

## Post-run custody and exact determinant display

After both suites finished, the sealed producer was loaded read-only to
display its factored expressions. Session 91524, initial 96b977, final
71edef, exit 0:

```
cusp conjugator determinant: -(q + 1)**2/4
longitude trace difference: -(q - 1)**3*(q + 1)**3/q**3
longitude minus identity determinant: -(q - 1)**4*(q**2 + q + 1)/q**3
```

The first display strengthens the generic nonzero assertion and three
sample checks with an explicit all-positive-q invertibility certificate.
It agrees with the reviewer's nilpotent-chain derivation. This is reuse
of the sealed producer, not a second implementation or a new test count.

The same final output repeats all seven hashes unchanged. Before report
updates, git diff --exit-code 9c0d1c67 over F01--F09, the other-seat
physical-bridge reports and its parent-vertex test returned exit 0.
Chunk 178943 had also shown clean status and no post-seal F10 diff.

These outputs are transcriptions of tool receipts, not separately stored
raw terminal logs. Reports and scoped follow-through pointers are the
only post-execution edits. No repository-wide suite/gate run, push or
independent main banking is claimed.

## Report-only follow-through review

The second reviewer read FINDINGS.md and this receipt after drafting and
reported no concrete mathematical scope error. It confirmed the explicit
invertibility qualification, separation of the determinant display from
sampled tests, local/global and ordinary/L2 boundaries, and Ballas credit.
It did not validate the paper independently, run the suites or certify
main banking. Only the F08/F09 findings and the two living audit reports
receive dated follow-through pointers; their frozen science is unchanged.

Final read-only reporting check ba3c58: all seven scientific/producer
hashes match the seal, 16 local links resolve in F10 and its two direct
predecessor reports, whitespace check passes, and the five-file F10
scientific diff from ee0d62ea is empty. This is a scoped reporting check,
not a repository-wide link audit or independent banking certificate.
