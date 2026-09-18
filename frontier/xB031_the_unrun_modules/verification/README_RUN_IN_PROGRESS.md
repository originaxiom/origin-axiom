# xB031 verification — WORK IN PROGRESS at this commit

**The cells are still running at this commit. Nothing here is a result yet.**

- `c2_reducible_index.py`, `c2_run.py` — **copied BYTE-IDENTICALLY from B1418**
  (`sha256 d4468ef15b33f820a424ac5a0b1e66d4698bf5c983ffc062e5587dceb78bf9cc` and
  `d729b8b6ca8e98c100cffaaa72c67ceefa9ac92ee64e54134f56282eb1266869`; `diff` against
  `frontier/B1418_the_family_as_the_object/verification/` is empty). **No line adapted.**
- `x1_control.py` / its output — **X1 CONTROL PASSED**: B1418's own `m010` witness returns
  `I = +1`, `I^ss = 0` through this copy.
- `x2_complete.py`, `x2.out` — B1418's own `run()` on `t12835`, `MS = [1,2,3]`, **budget removed**,
  to complete the 3 325 modules B1418 left NOT RUN. **INCOMPLETE at this commit.**
- `x3_extend.py`, `x3.out`, `x3_partial.json` — `m = 4, 5, 6` on the 24 loci carrying the four
  order-signatures where B1418 found `|I| = 2`. **INCOMPLETE at this commit.**

**Interim only, and not a finding until the runs finish:** `m=4 → {−1,0,1}`, `m=5 → {−1,0}`,
`m=6 → {0}` over the first 975 modules, with `I^ss = 0` throughout (the drift control holds).
**This points AGAINST the sealed prediction `|I| = ⌈m/2⌉`** (`19aa3866`), which expected the first
`|I| = 3` at `m = 5`.

**The four fences in `PREREGISTRATION.md` bind whatever these return** — `I^ss = 0`, B1413's
theorem-zero on the geometric class, `t12835` is not the object, and **an index of 3 would not be
three generations.** Gate 5 absolute.
