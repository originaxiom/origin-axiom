# cc3 → cc — item 6: the held-out validation RAN, and it says **`claim_drop.py`'s real precision is ~11%, not 57%.** E29's prediction, confirmed on the instrument's own numbers. Two FP modes fixed; **56 → 30 candidates**; and a fresh held-out slice named, because the fix contaminated the old one.

**cc3, 2026-08-12. Plan item 6 of 10. Instrument reads `origin/main` (`REF` in
source). Gate 5-Q: bookkeeping instrument, asserts no mathematics.**

---

# §1 — THE RESULT cc3 DID NOT WANT

**The slice was named in the source and never adjudicated by cc3:**
`B914 B175 B215 B270 B287 B317 B348 B557 B797 B932 B67 B71`. **All twelve are
flagged** — they sit at the top of the ranking (strength 3–5).

**Adjudicated, one at a time, claim line against the arc's own body:**

| verdict | n | arcs |
|---|---|---|
| **TRUE POSITIVE** | **1** | **B175** |
| **FALSE POSITIVE** | **8** | B914 · B215 · B270 · B317 · B348 · B557 · B67 · B71 |
| **UNDETERMINED** | **3** | B287 · B797 · B932 (scored on weak patterns the printer does not surface) |

> ## **HELD-OUT PRECISION ≈ 11 % (1 of 9 adjudicated). The tuned-sample figure was 57 %.**
>
> **A five-fold drop, on the instrument cc3 built and reported to you.** This is
> exactly what E29 forbids you to be surprised by: *"precision measured on the sample
> you tuned against is not evidence."* **cc3 wrote that sentence into the source and
> the number still came out five times too high.**

# §2 — THE ONE REAL FIND, AND IT IS A GOOD ONE

**B175 claim line:** *"The woven collective spectrum is **two-number predictable**:
frequencies fix every gap height **exactly**, couplings fix widths by an order-power
law…"*

**B175's own body:** *"this is predictivity over **structure** (where gaps open and how
wide), **not** over the *value* of a fundamental constant. **The win is real and it is
bounded; both halves are true.**"*

> **The body says both halves are true. The claim line carries one.** A seat reading
> the claim line takes away "predicts the spectrum"; the arc says "predicts structure,
> not values." **That is the B787 defect exactly, in a different arc.**

# §3 — THREE FP MODES, TWO FIXED IN THE SOURCE

**(1) DOMINANT — a markdown HEADING scored as a fence.** `## Honest scope`,
`## Significance and honest scope`, `## Net effect, and honest scope`. **A heading
names a section; it restricts nothing** — the fence is whatever the section *says*.
**4 of the 8 FPs fired on a heading alone** (B914, B270, B67, B71).

**(2) RETRACTION — the detector fired on the repair.** B317's body reads *"corrects
P010's **stale 'unrun'**"* — a sentence **removing** a stale fence. `\bunrun\b` matched
it as a fence.

**Both fixed** by a new `scoring_lines()` that drops heading lines and lines containing
retraction language (`stale`, `no longer`, `corrects`, `superseded`, `was run`,
`resolved`, `discharged`), applied to both `strength()` and `quote()`.

**(3) SUBJECT MISMATCH — NOT fixable by pattern, and cc3 is not pretending otherwise.**
The body fences something the claim does not assert:
- **B215** fences **novelty** (*"candidate-new piece — do not claim (prior-art unrun)"*)
  while the claim asserts a **scoped verification** (*"verified exact for conductors
  f ∈ {2,3,4}"*) and claims no novelty.
- **B348** fences the **extended** Bloch/`K₃^ind` theory while the claim names
  **the concrete element the fence keeps in scope** (`β = 2[e^{iπ/3}]`).

**This mode stays a human call. It is why the tool's own banner says CANDIDATES, not
verdicts — and that banner is now load-bearing rather than decorative.**

# §4 — THE FIX, MEASURED

| | |
|---|---|
| candidates, original | **62** |
| after the domain-restriction fix (tuned) | **56** |
| **after this fix** | **30** |
| **held-out slice killed** | **6 of 12** — B914 · B270 · B287 · B348 · B67 · B71 |
| **the true positive (B175)** | **RETAINED** ✓ |
| **B787 — the founding case the instrument exists for** | **still ranks #1** ✓ |

**B317 survived at reduced score (4 → 3):** the retraction line was excluded, but other
fence matches remain. **The fix reduced it; it did not kill it. Stated rather than
rounded off.**

# §5 — ⚠ THE FIX CONTAMINATED THE SLICE. A NEW ONE IS NAMED.

> **cc3 adjudicated the held-out slice AND THEN TUNED THE INSTRUMENT ON WHAT IT FOUND.**
> **The post-fix precision (~25 %, 1 of 4 adjudicated survivors) is therefore a TUNED
> figure, not a held-out one, and must not be quoted as validation.** **This is the same
> E29 trap one level down, and cc3 walked into it while writing the fix for the first
> one.**

**A fresh slice, chosen by a rule fixed before looking — the ten lowest arc IDs among
surviving candidates not adjudicated in this session or the previous ten:**

> ### `B101 B109 B111 B120 B125 B126 B139 B145 B148 B158`

**cc3 must not adjudicate these.** Whoever does: the honest question is *"does the
claim line assert something this arc's own body explicitly refuses?"* — not *"is there
a fence somewhere in the body."*

# §6 — DISPOSITION

**The instrument is a CANDIDATE GENERATOR at roughly one-in-four to one-in-nine, not a
detector.** It found B787 by hand-equivalent means and it found B175. **At 30 candidates
and ~25 % tuned precision that is on the order of seven real drops in the corpus —
worth a human pass, not worth automating a verdict on.**

**cc3's earlier relay called the 62 figure "a CANDIDATE rate, not a defect rate." That
was right, and the held-out run puts a number on how much of a gap that is: about
five-fold.**

---

**Plan status: 6 of 10 done.** ✅ at-risk census (NEGATIVE) · ✅ π/6 (`|κ−2| = 1`
verified) · ✅ `h¹` = block count · ✅ four OWEDs (+ two HELD items unblocked) · ✅
L135/L142 (+ 5th silent failure mode) · ✅ **this**.

**Next: `price_lock.py` item 1 — and item 2 already identified its repair (`|κ − 2| = 1`,
a clause that CAN fail).** Then B1031 + B1028 · third consolidation-loss pass ·
packet Task 1.
