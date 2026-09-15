HEADLINE
# Punctured-torus source custody and reading boundaries

WHAT IT IS
An intake/provenance note (reading-custody checkpoint) documenting exactly what source material was personally read, its file hashes, and what repo state was fetched — explicitly not a status report, roadmap, or scientific result.

VERDICTS AND CLAIMS
- "Local research checkpoint after fc3c9470. No B number is allocated, no incoming branch is merged, and no physical milestone or R30 execution is claimed." (SCOPE DISCLAIMER)
- Minsky math/9807001v3: "All 68 PDF pages... Complete reading, not an independent formal proof verification."
- Thurston math/9801045v1: "All 32 PDF/printed pages... Complete reading after the supplied-file intake; not an independent formal proof verification."
- Jorgensen 1977 (twelve screenshots): "Complete personal reading; explicit reconstruction is cited, not independently recertified in full."
- Jorgensen 2003 Cambridge chapter: "Full text not obtained/read; 2001 is the workshop date."
- File hashes given for Minsky PDF (SHA-256 `58c17980...`) and Thurston PDF (SHA-256 `e2c8d6df...`).
- "The files named `jorgensen_1977_jstor.pdf` and `jorgensen_pairs_2003.pdf`... are HTML responses, not PDFs" — access failures explicitly flagged, not treated as evidence.
- "The indexed full-book mirror returned 404, and the direct Annals guessed PDF URL did not yield a source."
- Repo pins: origin-main `b94ed03a...`, paper-review `d08d1f9834...`, outside bench `d2d70b692d...`, own HEAD `fc3c9470...` on `audit/physical-bridge-2026-09-05`.
- "This scans prior/deleted content, not just deleted filenames; it does not scan untracked files or prove semantic absence."
- "Its `fibered_face` regex misses `fibred`; the assessment explicitly limits that count." (SELF-LIMITATION)
- Later fetch: paper-review advanced "by eight commits to `31cfd0325d9...`", outside bench "by sixteen to `d3309b1d78...`".
- "B1404's complete 355-line FINDINGS and 323-line producer were personally read... Neither its producer nor its tests were executed."
- "The earlier Minsky zero is historical, not an assertion of current absence after B1404."
- "The lineage memo is a recommendation, not authority to move main; no canonical branch pointer was moved."
- "No B number or shared buffer is taken."
- "A name in a search-lead column is not adoption of that person's theorem" (re: sole Maskit hit).
- Reporting gate results: "The first reporting gate run returned 25 PASS / 5 FAIL... The follow-up's 26 PASS / 4 inherited FAIL."
- "No full-suite green or independently accepted main bank is claimed."

CORRECTIONS TO MAIN OR TO ITSELF
- "The first failure log is preserved; a follow-up is a reporting repair, not a replacement of a scientific outcome" — self-correction of a citation error, not a scientific claim.
- "That citation is repaired above to the pinned remote URL" (re: "this receipt's unqualified citation of a remote-only lineage path" flagged as one of the 5 FAIL items and then fixed) — self-correction of its own prior draft.
- "The earlier Minsky zero is historical, not an assertion of current absence after B1404" — walks back how the earlier zero-count search should be read, given new B1404 material (self-correction of interpretation, paired with the companion GEOMETRY doc).
- No claim that main's record itself is wrong is made in this document.

ROADMAP ITEMS
N/A (this is an intake/reading-custody document, not a status/roadmap doc; it lists no forward task list beyond noting that "R29 remains the latest executed scientific round" and "Reporting checks are recorded separately after staging the reader-facing changes.")

CONFLICTS WITH MAIN
- Checked commit `b94ed03aecba8aae3afc62504e22ec664c26e94f` (claimed origin-main pin) and `31cfd0325d947f797fcd480d2acc32ed526e2913` (claimed paper-review B1404 commit) via `git -C <repo> log --oneline -1 <hash>` style lookup is out of scope for a text grep, but the earlier check in the companion report confirmed `frontier/B1404_the_family_has_a_name/FINDINGS.md` exists in main with Minsky references, consistent with this document's claim of "B1404's complete 355-line FINDINGS... personally read."
- No claim in this document asserts main's docs/frontier record is factually wrong; it is purely custody/provenance. NONE.

WHAT MAIN WOULD HAVE TO VERIFY
Confirm the cited commit hashes (`b94ed03a`, `31cfd0325d9...`, `d08d1f9834...`, `d2d70b692d...`) actually correspond to the claimed states of origin-main/paper-review/outside-bench at the stated dates, and that the referenced receipt JSON/checker scripts (history scan, receipt check) exist and produce the stated pass/fail counts.
