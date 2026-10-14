# B1650 — addendum (2026-10-14, S125): chat1's root-share check, verified

chat1's root-share check (its name T-ROOT; sealed `13d31f042`, script `fc82fe02a` committed before its one run, findings
`4f179d4d7`; on the web seat's branch at `047b8f7a4`) asks how much of the action-weighted weave, exp(−c·Vol/6π) times
a word weight, falls on the root LR.

**Reproduced** (`verification/root_share_reproduction_record.json`), in a clean checkout at `047b8f7a4`.
- **The first rerun crashed.** A transient exception in SnapPy's solution_type() for LLLRLRRRLRLRLLRLLR left that
  thread in `vols` but not in `sols`, and line 73 raised a KeyError. In isolation the thread is fine: volume
  15.7132169306, all tetrahedra positively oriented. No output was written.
- **The second rerun completed.** Every cell held as committed (Q0, Q1, T1–T8), with no failures. All 31 040 threads'
  volumes and CS equal the committed ones to 1.1·10⁻¹³.
  - t_root.json differs only in the order of exact mirror-pair ties in a read-out (LLR and LRR have identical volume),
    in zero-CS noise and in the timing field.

**Recomputed on main** (`verification/main_root_share_recheck.py` and its `.json`).
- A 60-thread SnapPy spot check of chat1's committed volumes (to 5·10⁻¹⁴) and CS (to 6·10⁻¹⁴).
- Main's own arithmetic on the volumes at c = 6:
  - the root share is 0.2737, 0.5019 and 0.6601 under the word weights 2⁻ⁿ, 3⁻ⁿ and 1/(n(n − 1)L(n));
  - the chiral share is 0.659 and N_eff is 32.4 under the first.

  This is chat1's finding: at c = 6 the action-weighted weave is a plurality that sees the level k.
- The script reads chat1's thread table from the web seat's commit by `git show`, so it needs that branch fetched. It
  is a verification record, not a lock.

**The defect, reported to chat1:** fill the three dictionaries together, so that a transient failure is reported as a
failure, not a crash.

**Naming.** chat1's test is "the root-share check" in main's text, because "T-ROOT" collides with GENESIS's T-ROOT item
prefix (the SM seat's §95; chat1's note).
