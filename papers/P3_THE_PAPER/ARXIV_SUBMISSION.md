# THE ARXIV BUNDLE — how the paper is shipped (S11, 2026-09-16)

The paper is submitted as **source + ancillary files**, with a frozen repository snapshot deposited under a
persistent identifier before the upload. The bundle is built outside the tracked tree (the submission copy carries
the full author block, which the repository's privacy rule keeps out of tracked files); everything below is
reproducible from the tracked tree in one pass.

## What the bundle contains

| path (inside the bundle) | what it is | built from |
|---|---|---|
| `main.tex` | the paper, full author block, `\date{2026-09-16}`, every full-line `%` comment stripped (arXiv source is public) | `papers/P3_THE_PAPER/main.tex` with the author/date lines substituted and comment lines removed |
| `anc/README.md` | what the package certifies and what it does not | `verification_package/README.md` |
| `anc/MANIFEST.md`, `anc/MANIFEST.json` | every claim → records, seals, scripts, locks; commit hash of the tree it was built from | `verification_package/build_manifest.py` |
| `anc/REPORT.md` | the last package run (seals, locks) | `verification_package/run_package.py` |
| `anc/build_manifest.py`, `anc/run_package.py` | the builder and the one-command runner (run inside the snapshot) | same |
| `anc/make_snapshot.sh` | makes the snapshot tarball named by commit, for the deposit | same |
| `abstract.txt` (bundle dir, not uploaded as a file) | the metadata abstract, plain text with `$…$`, under arXiv's 1 920-character limit | the paper's `abstract` environment |

The paper's own abstract is the short one (metadata-length); the long account that was the abstract through S10b
is the unnumbered **Summary of results** section that follows the front matter, so nothing was cut, only moved.

## The order of operations at submission (owner's hand; each step is a decision the repository does not make)

1. **Freeze.** Commit the tree; `git status` clean. Run `bash papers/P3_THE_PAPER/verification_package/make_snapshot.sh`
   (writes `audit/paper_submission/origin-axiom-<commit>.tar.gz` + its sha256).
2. **Deposit the snapshot** (Zenodo or equivalent; the repository's mirrors are not persistent identifiers).
   Record the DOI.
3. **Write the DOI into the paper**: the appendix intro in `scripts/checks/paper_provenance.py` carries
   "DOI to be assigned at deposit" — replace with the identifier, regenerate the appendix block
   (`python3 scripts/checks/paper_provenance.py --tex`, splice between the GENERATED markers), rebuild
   (`bash papers/P3_THE_PAPER/build.sh`), rerun the paper locks (`tests/test_paper_*.py`,
   `tests/test_p3_verification_package.py`), rebuild the manifest (`build_manifest.py`), commit. The manifest
   records the commit it was built at; the paper commit is that commit's child, by construction.
4. **Rebuild the bundle** from the new tree (the recipe is the S11 entry in `docs/SUBMISSION_CAMPAIGN.md`);
   `tar -czf` the bundle directory; check it builds standalone with two `pdflatex` passes in an empty directory.
5. **Upload**: source (`main.tex` + `anc/`), the metadata abstract from `abstract.txt`, primary `math.GT`,
   cross-list `hep-th`, `math.NT`; MSC 57K32 (11F06, 17B25, 81T50, 46L36). A first submission in `math.GT` may
   require endorsement; the endorsement request is the owner's, not the repository's.
6. **After the identifier is issued**, record it in `docs/SUBMISSION_CAMPAIGN.md` and the paper's `\date`/footnote
   if the venue asks for it.

## What stays owner-gated

The deposit, the upload and its endorsement, the venue after the preprint, and any change to the author block.
No step above is run by a seat without the owner's word.
