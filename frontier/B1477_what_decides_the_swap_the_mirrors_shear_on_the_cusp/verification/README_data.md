# B1477 — the data files

- `range_census.jsonl.gz` — C1, all 212,641 rows (one per census manifold); `range_census_amphichiral.json` — its summary and the 283 amphichiral rows.
- `range_spin.json` — C2/C3, the 181 one-cusped amphichiral members (the cell writes `range_spin.jsonl`, which the repository ignores; this is the same rows as one JSON list).
- `zero_witness_cusped.json`, `zero_witness_closed.json` — C4.
- `orbit_form_census.json` — Q1 (second seal), 283 rows; `orbit_form_links.jsonl.gz` — Q2, all 120,574 rows; `orbit_form_links_amphichiral.json` — its summary and the 922 amphichiral rows.
- `pi_geodesics.json` — the post-seal cell for Theorem B (`pi_geodesics.py` reads `range_spin.jsonl`: regenerate it with `range_spin.py`, or write the rows of `range_spin.json` one per line).

`range_spin.py` and `orbit_form.py census` read `range_census.jsonl`: run `gunzip -k range_census.jsonl.gz` first. Every
cell is resumable (it skips names already in its output file).
