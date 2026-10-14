# W86's evidence: the five auditors' reports and their own checks

This folder keeps the evidence behind W86 (`../W86_RULE.md`; the record is W86's section of `../NOTE.md`). W86 checked
the web seat's whole branch (`chat1/web-seat` at 9fbab9f5e) at the owner's order of 2026-10-14: "verify all from chat1
so its not based on wrong computations or bugs for conclusions, or misinforment".

## What is here, and who wrote it

- **Five reports,** one per group of chat1's folders:
  - `REPORT_selection.txt`: the selection folder (the thread frame, the Lagrange law and their post hocs) and its relay;
  - `REPORT_meditation.txt`: the meditation "What we are missing" and the branch README;
  - `REPORT_field.txt`: the field, the condensate in M and the first row;
  - `REPORT_scale.txt`: the scale (with chat1's root-share and sign checks) and the mysteries note;
  - `REPORT_oct06.txt`: the seven folders and relays of 2026-10-06. It is interim: the auditor's draft of its sections
    joined with its interim hand-back, which carries the graded findings. Its last heavy re-runs were still running
    when W86 was recorded; their outcome is noted in W86's section with a date.
- **Each report was written by a read-only auditor,** an agent the seat set to one group of folders under W86's rule.
  The auditors ran chat1's scripts unchanged from a `git archive` of 9fbab9f5e in the seat's scratch space, read the
  code, checked every number against the outputs and every citation at its source, and wrote their own checks. They
  edited nothing in the repository and pushed nothing.
- **The auditors could not write files.** The seat saved each report from the auditor's hand-back, verbatim except for
  three hygiene edits, disclosed here:
  - absolute scratch paths are shortened to `<scratch>/` or `<session>/`, and the repository's path to `<repo>`;
  - two sentences name the author of chat1's commits; they now read "authored under a name other than originaxiom";
  - one branch name is shortened to "the outside-bench branch".
  The reports are kept as `.txt` because they cite the record's ids and paths in the auditors' own words, which the
  repository's citation and path gates hold only for its living `.md` text.
- **The auditors' own check scripts and their outputs** sit in one subfolder per report (`selection/`, `meditation/`,
  `field/`, `scale/`, `oct06/`), byte-identical to what ran. They expect the auditors' scratch layout (the extracted
  folders beside them) and are kept as evidence, not as code that runs from the repository. Shell wrappers and
  run-metadata files (`.meta`) that held machine paths, binary caches (`.pkl`, `.npz`) and outputs over 300 kB were
  left out.

## How the seat used them

- **The seat read every report and owns every finding.** W86's section lists each finding with its grade:
  - A: it changes a conclusion chat1 draws, or one the record has taken from chat1;
  - B: a wrong number or claim that changes no conclusion;
  - C: a citation or wording slip.
- **Every A finding was re-checked on the seat's own code** in a labelled post hoc, committed before its one run
  (`../the_chat1_record_checked_posthoc2.py` for the first two, `../the_chat1_record_checked_posthoc3.py` for the
  third).
- **The B findings marked so in W86's section were re-checked by the seat at source,** from chat1's committed files.
  The others stand on the auditors' reports and checks here.

0 of 19.
