# B1709 — THE REVIEW TOOLS READ THE OWNER'S MIRROR (Review 67's R67-1): A SEAL IS "ON EVERY REMOTE" WHEN IT IS ON ORIGIN AND ON THE LaCie MIRROR, READ IN THE MIRROR ITSELF

**Verdict: PROVED (a tooling repair with a failing-path test; no data).** cc (main), 2026-10-22. 0 of 19.
- **The defect.** `scripts/review/review_tools.py` named Codeberg as this repository's second mirror. Codeberg has been
  disabled since R66-1; the owner's mirror is the LaCie bare repository (`git push backup`). Every seal of Review 67's
  window therefore reported "seal not on every remote" for that reason alone.
- **The repair.** `MIRRORS = ("origin", "backup")`. A new `on_mirror(commit, remote)` reads a mirror through its
  remote-tracking ref when there is one, and otherwise — a mirror pushed to but never fetched, a local bare repository —
  in that repository itself (`git --git-dir <path> merge-base --is-ancestor <commit> main`). The pure `seal_check` is
  unchanged.
- **Checked.** Review 67's window read again (`--anchor a498554e2`): the seven seals (B1693–B1702) report no defect. A
  failing-path test builds a work repository and a bare mirror, pushes one commit and not the next, and requires the
  first to be found on the mirror and the second reported absent (`tests/test_review_tools.py`).
- **Left as it is.** `harvest_debt.py`'s Codeberg entries name where the seats push their own lanes, not this
  repository's mirror.

## 0. Seen first

`VERDICT topic-sweep /mirror|git push backup|LaCie|seal not on every remote|R66-1|R67-1/ (full text): 260 of 1481 arcs on main match (NEGATIVE 52, OPEN 18, PROVED 189, RETRACTED 1)` — Review 66's R66-1 (the mirror resolved
by the LaCie repository) and Review 67's §1 (the stale list named, R67-1). **Literature:** none.

## 1. Files

- `scripts/review/review_tools.py` (MIRRORS, `on_mirror`); `tests/test_review_tools.py` (the live mirror list and the
  failing-path test).
