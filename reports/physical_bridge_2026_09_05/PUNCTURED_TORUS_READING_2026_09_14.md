# Punctured-torus source custody and reading boundaries

Local research checkpoint after fc3c9470. No B number is allocated,
no incoming branch is merged, and no physical milestone or R30 execution
is claimed. The [assessment](PUNCTURED_TORUS_GEOMETRY_2026_09_14.md)
separates published statements, elementary consequences and planned work.

## Personal primary reading

No paper reading or interpretation was delegated.

| Source | Actual reading boundary | Status |
|---|---|---|
| Minsky, math/9807001v3 | All 68 PDF pages, printed 559-626, including every section, proof and references; all nine figures visually inspected on PDF pages 8, 10, 16, 20, 22, 28, 30, 38 | Complete reading, not an independent formal proof verification |
| Thurston, math/9801045v1 | All 32 PDF/printed pages, all sections/proofs/references; all six figures visually inspected on pages 1, 3, 6, 12, 14, 15 | Complete reading after the supplied-file intake; not an independent formal proof verification |
| Jorgensen, Annals 106 (1977), 61-72 | All twelve supplied screenshots, in chronological order, covering pages 61-72 without gaps, all eleven sections, five figures and references | Complete personal reading; explicit reconstruction is cited, not independently recertified in full |
| Jorgensen, Cambridge chapter (2003), publisher pages 183-208 | Publisher bibliography, editorial note and available summary | Full text not obtained/read; 2001 is the workshop date |

Minsky PDF: 609188 bytes,
SHA-256 `58c1798079e3f999627625aaa92a86ea28f231fbe92951fb64b98fbc8e07a879`.
URL: https://arxiv.org/pdf/math/9807001v3.
Layout text: SHA-256 `87fee1373deba61ed2d26155f3d1a95d74f8e135cf2859441bae6be16e47e72b`.

Thurston PDF: 1353910 bytes,
SHA-256 `e2c8d6df33dea0d72742c960c3851c167ae78ca662a362ad2dcdf0e7881e5f8c`.
URL: https://arxiv.org/pdf/math/9801045.

The supplied `9801045v1.pdf` is byte-for-byte the same Thurston copy.
Its original ten-page targeted reading was extended to every remaining
page: 5-6, 11-17 and 20-32. The full-text access duty for Jorgensen 1977
is discharged by the supplied screenshots; the distinct 2003 chapter
has not been supplied or read. The [supplied-source receipt](PUNCTURED_TORUS_SUPPLIED_SOURCES_2026_09_14.json)
records the thirteen basenames, exact bytes/digests and page mapping.
The [local checker](punctured_torus_supplied_source_check.rb) verifies
file signatures, bytes, hashes and the declared page sequence. It cannot
certify reading or a theorem; those remain explicit personal attestations.

Jorgensen reading map: pages 61-63 introduce the existence statements,
the hyperbolic/isometric-sphere model and Lie-product involution;
64-65 give the parameters, matrices and conjugation relations;
66-68 give the polyhedra, face pairings and group presentations;
69 proves the fibre description and smooth finite-cover existence;
70 gives further branched-sphere examples; 70-72 contain the remarks
and references. No independent all-face Poincare-polyhedron verification
or finite-index subgroup enumeration is claimed. The displayed return
matrix and central-versus-parabolic limit distinction in the assessment
are elementary hand consequences with their conventions stated, not a
new certified cusp construction. The tentative uniqueness remark and
the historical use of “Kleinian” are not promoted to new no-go theorems.

Downloaded papers remain local; this checkpoint does not redistribute
their full texts or the supplied screenshots. Temporary working directory:
`/tmp/oa-punctured-torus-sources.6DY9UE`.
The versioned URLs and hashes identify the copies if that directory is
later cleaned. The files named `jorgensen_1977_jstor.pdf` and
`jorgensen_pairs_2003.pdf` there are **HTML responses, not PDFs**.
Their filename extensions and successful HTTP transfers were not
accepted as evidence of access. The indexed full-book mirror returned
404, and the direct Annals guessed PDF URL did not yield a source.
A nonblocking request for the two missing PDFs was sent to the owner;
the subsequent images supplied the complete 1977 paper, as recorded above.

Several long terminal displays were truncated. The omitted Minsky
passages on pages 50, 52-53 and 67-68 and Thurston pages 1 and 10 were
read again explicitly; these were read-only retrievals, not repeated
scientific calculations. A locale failure in `shasum` was replaced by
Ruby's digest calculation on the same downloaded bytes.
During supplied-file intake, a further locale failure exited before
producing hashes; `LC_ALL=C` succeeded on the unchanged files. A
read-only figure-location lookup needed explicit UTF-8 after Ruby
rejected its text as US-ASCII. No paper bytes or scientific data changed.

## Repository coverage and non-adoption boundaries

Fetched origin-main: `b94ed03aecba8aae3afc62504e22ec664c26e94f`.
Paper-review: `d08d1f9834f2e5ceb92ff6e33c2ea1f466446a80`.
Outside bench: `d2d70b692dc473f4dbffd57a62fa400567696ee2`.
Own starting HEAD: `fc3c9470a0a9a1442f30bae10b4ffc217f5e7ee4` on
`audit/physical-bridge-2026-09-05`.

The [read-only scan](punctured_torus_history_scan.rb) completed once,
exit 0. Its [published receipt](PUNCTURED_TORUS_HISTORY_2026_09_14.json)
preserves all 28 reference SHAs, two extra historical tips, object
population digest, counts, matching blob IDs, one example path per
blob and matching line numbers by regex. Branch labels alone are
replaced with numbered aliases. The raw named receipt remains in
`Documents/temp001`, 80687 bytes, SHA-256
`c6dbdc81da4478bea11b617171067863dc84bcf53e9e3350459f7724edea5c92`.
This scans prior/deleted content, not just deleted filenames; it does
not scan untracked files or prove semantic absence. Its `fibered_face`
regex misses `fibred`; the assessment explicitly limits that count.

A later fetch completed after the supplied-source reading. Paper-review
advanced by eight commits to `31cfd0325d947f797fcd480d2acc32ed526e2913`,
and the outside bench by sixteen to `d3309b1d7881c2c573622ddb621e0444ff9d1909`.
The [late-fetch receipt](PUNCTURED_TORUS_LATE_FETCH_2026_09_14.json)
keeps that event separate from the original history population. B1404's
complete 355-line FINDINGS and 323-line producer were personally read,
as was the updated alias table. The assessment receives its substantive
literature connection but checks the fixed-directions/return-power
equivalence separately. Neither its producer nor its tests were executed.
The other new commits were inspected by log and change list only, not
adopted from their headlines. The earlier Minsky zero is historical,
not an assertion of current absence after B1404.

Read completely at the stated pins:

The seven path-qualified entries have [byte/digest receipts](PUNCTURED_TORUS_REPO_RECEIPTS_2026_09_14.json).
The [receipt checker](punctured_torus_receipt_check.rb) validates those
bytes, the publication transform and every recorded matching blob's
line lists. It is not a new absence scan or mathematical certificate.
Its follow-up version additionally checks the three late-fetch file
receipts; the original seven-file first-run capture remains unchanged.

- paper-review B1400 FINDINGS and current SM-seat alias table;
- paper-review [lineage decision](https://github.com/originaxiom/origin-axiom/blob/d08d1f9834f2e5ceb92ff6e33c2ea1f466446a80/docs/handoffs/LINEAGE_DECISION_2026-09-13.md);
- outside memo 214 and `outside_bench/seals/L71_CUSP_SLOPE_PREREG.md`;
- outside `certificates/is_anything_real_on_it.py` and its saved output;
- the historical sB1282 sibling-faces addendum at blob
  `c0e07f16d6601f8c5baa43291ed191964c63f563`.

The historical theorem-registry blob
`03d5a771ee9284159aeb88dc8b389a0748d9bcd5` was read only through line 45,
including the sole Maskit match. A name in a search-lead column is
not adoption of that person's theorem. B1403's latest change list was
inspected, not its complete proof/producer; its headline is not imported.
The sibling-faces addendum's finite specialization sweep is not used
here as a proof about all fibrations. The outside photonic producer was
read but not executed or accepted as an experimental-theory verdict.
The lineage memo is a recommendation, not authority to move main; no
canonical branch pointer was moved.

The current banking protocol and permanent alias table were read.
The first received alias table spent B1403 and pointed to B1404 on that
bench. The late version names B1409 as next, while the fetched tip
already contains B1409's sealed design; a next-number line is not a
reservation for this audit. No B number or shared buffer is taken.
Independent receiving-seat verification and the old red banking gates
are not discharged by a source-reading checkpoint.

An inherited read-only lookup handle was no longer available after
resumption; its terminal result was not recovered or claimed. The
new history scan has its own successful terminal receipt. No scientific
source, test or seal was changed or run in this literature checkpoint.
R29 remains the latest executed scientific round. Reporting checks
are recorded separately after staging the reader-facing changes.
The first reporting gate run returned 25 PASS / 5 FAIL: four inherited
failures plus this receipt's unqualified citation of a remote-only
lineage path. That citation is repaired above to the pinned remote URL.
The first failure log is preserved; a follow-up is a reporting repair,
not a replacement of a scientific outcome.
The [final reporting receipt](PUNCTURED_TORUS_FINAL_CHECKS_2026_09_14.txt)
records the follow-up's 26 PASS / 4 inherited FAIL, source checks,
manifest/link checks and the separately corrected ad-hoc seal-parser
lookup. No full-suite green or independently accepted main bank is claimed.
