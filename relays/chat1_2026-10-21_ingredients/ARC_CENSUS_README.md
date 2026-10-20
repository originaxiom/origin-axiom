# arc_census.csv: every arc directory on main, by ingredient (a reading aid)

chat1, 2026-10-21, for `THE_INGREDIENTS_MAP.md`. Read from main at 3418b9ca6. 0 of 19.

- **What it is.** One row per directory under `frontier/` on main: 1 450 rows (numbers up to B1681; B58 has three
  sub-arcs and B89T is separate). The columns:
  - `verdict`, from `arc_verdict.json` where it exists, else from the findings' verdict line;
  - `date`, the first date in the findings' head (main's history was re-rooted on 2026-10-06, so commit dates are not
    used), or the neighbours' median where that date is out of line (538 rows);
  - `title`, the findings' title;
  - `buckets`, one or more ingredient buckets (FOUNDATION, BRIDGE-I31 to I34, GAUGE, SPACETIME, FRAME, TAU, HIGGS,
    LINE, END, CP/SIDE, WHICH-THREAD, DYNAMICS, the VALUE buckets, NEUTRINO, OTHER-PHYSICS, INFRASTRUCTURE, PURE-MATH);
  - `cites_*`, direct mentions of the arc's number in six ingredient ledgers: IDENTIFICATION_LEDGER,
    SM_SPECIFICATION_LEDGER, OPEN_LEADS, POINT_REGISTER, GENESIS.md and the paper's tex;
  - `orphan_physics` = 1 when the arc is in a physics bucket and none of the six cites its number;
  - `cited_in_law_map_or_theorem_registry`, for the same test against LAW_MAP and THEOREM_REGISTRY;
  - `number_vs_data_curated`, arcs that compare a number with data (read by hand);
  - `supersedes`, `superseded_by` and `corrected_by_later_arc`.
- **How it was made.**
  - A read-only sweep applied keyword rules to the title, the one-line claim and the first sixty lines of each findings
    file (weighted 3, 2 and 1), and corrected about 120 assignments by hand after reading. Its scripts are not
    committed.
  - chat1 then recomputed the orphan flag with a stricter citation match, which un-flagged ten arcs cited inside slash
    lists (B153, B274, B282, B289, B426, B434, B883, B1159, B1167, B1273).
  - chat1 dropped two free-text columns (the one-line claim, the head banner) and a column found unreliable (other
    files citing the arc).
  - It replaced with "[…]" five title or verdict fields that quote names of tools from main's own text.
- **How to read it.**
  - The bucket counts are approximate.
  - The orphan test counts direct citations only. A range citation ("B1615–B1618") does not count, and a seat-prefixed
    reference (`sm:B…`) is excluded.
  - An orphan is an arc to look at, not an error. About a third of a read sample of orphans are process arcs.
  - Arcs bucketed only OTHER-PHYSICS are not flagged.
- **Headline counts** (recomputed on the file):
  - verdicts: PROVED 957, NEGATIVE 349, OPEN 93, none 36, RETRACTED 12, other 3;
  - 302 orphans, all dated 2026-09-18 or earlier. 93 of them are cited in LAW_MAP or THEOREM_REGISTRY, 167 also carry
    INFRASTRUCTURE, and 95 are in the GAUGE bucket (70 PROVED);
  - 66 arcs compare a number with data.
- sha256 of `arc_census.csv`: bd416bd0b63d65fbad3d756271db4b590a88a1b4f441d4d34b175912ca15e349.

chat1, 2026-10-21. 0 of 19.
