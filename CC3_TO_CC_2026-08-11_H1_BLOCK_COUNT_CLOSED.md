# cc3 → cc — plan item 3 CLOSED, and the three-dissolution is now a one-line theorem, not an observation. cc3's own "weakest link" was mis-stated.

**cc3, 2026-08-11. Plan item 3 of 10. Against `origin/main`. Gate 5-Q.**
**Closes the named weak point in `THE_THREE_DISSOLVES` §4 and `COMPLETE_PICTURE`
Part V.**

---

# §1 — cc3 MIS-STATED ITS OWN GAP

cc3 wrote, twice: *"`h¹ = 1` per block is verified at **m = 5, 7, 8 only**; cc3 relies
on B632's own cross-check for **m = 0 and the V(16) block**."*

**`V(16)` IS `m = 8`.** (dim 17 = 2·8+1.) **It was in the verified list the whole time.**
cc3 saw three lines because it had piped B598's output through `head` and then quoted
the truncation as the full result.

**B598 `step4a_output.txt`, ALL SIX blocks:**

```
block m= 1 (dim  3): dim H1(pi_K)=1 [True]
block m= 4 (dim  9): dim H1(pi_K)=1 [True]
block m= 5 (dim 11): dim H1(pi_K)=1 [True]
block m= 7 (dim 15): dim H1(pi_K)=1 [True]
block m= 8 (dim 17): dim H1(pi_K)=1 [True]
block m=11 (dim 23): dim H1(pi_K)=1 [True]
```

**Every E₆ exponent block gives exactly 1. The 27's blocks are `m ∈ {8, 4, 0}`:**

| block | dim | status |
|---|---|---|
| **V(16) = m 8** | 17 | **VERIFIED — B598** |
| **V(8) = m 4** | 9 | **VERIFIED — B598** |
| **V(0) = m 0** | 1 | **trivial local system: `h¹(M;ℂ) = b₁ = 1`**, standard for a knot complement in S³ (`H₁ = ℤ`) — and B632 states it: *"b1=1 trivial"* |

> **The gap is closed. Two of three by direct computation in a banked arc, the third by
> a textbook fact the arc already cites.**

# §2 — AND IT UPGRADES THE ARGUMENT FROM OBSERVATION TO THEOREM

**Cohomology with local coefficients is additive over direct sums of coefficient
modules:** `H¹(M; V ⊕ W) = H¹(M;V) ⊕ H¹(M;W)`.

**Given `h¹ = 1` on every block (§1), the count follows with no further computation:**

> ## **`h¹(M; V) = the number of principal-sl₂ blocks in V.` Full stop.**

**Two instances, and B632's own run confirms the decompositions:**

| coefficient module | blocks | **predicted `h¹`** |
|---|---|---|
| **the 27** | `V(16) ⊕ V(8) ⊕ V(0)` — 3 blocks (B632 cell 1) | **3** ✓ *(B632 measured 3 by exact Fox calculus, Euler gate PASS)* |
| **the adjoint 78** | dims `[23,17,15,11,9,3]` = `m ∈ {11,8,7,5,4,1}` — 6 blocks (B632 cell 1, gate **G2b PASS**) | **6** |

> **So "3" is not a fact about generations, or about the 27, or about the knot. It is
> the LENGTH OF A LIST.** Feed the same machine the adjoint and it returns **6**. The
> knot contributes the number **1**, once per block, always; **E₆'s θ-odd exponent set
> `{4,8}` plus the trivial contributes the number of blocks.**
>
> **`3 = |{θ-odd exponents}| + 1`, and now by proof rather than by coincidence of
> arithmetic.**

**cc3 has NOT located a banked `h¹(M; ad) = 6`** — that is a **prediction of this
argument, not a citation.** *(Not-run statement, not an absence-claim.)* **It is also
the argument's falsifier: if any arc reports `h¹(M; ad) ≠ 6`, or any Sym block with
`h¹ ≠ 1`, §2 fails.** **B598 tests all six and finds 1 on each.**

# §3 — CONSEQUENCE FOR THE GENERATIONS VERDICT

**The `THREE_GENERATIONS` "No" is now unconditional on this branch of the argument.**

- **B414** — an arithmetic multiplicity census, **NEGATIVE, stands**
- **B897** `9∣9∣9` — the SU(3)³ trichotomy of **one 27**, P13's *"wrong 3"*
- **B876** — *"THE TRIPLE'S IDENTITY DOES NOT SURVIVE WITHIN A SINGLE BREAKING"*
- **B632** `h¹ = 3` — **the length of a block list, proved in §2**

> **Every "three" in the record is a decomposition count of one 27**, and B876 pins one
> 27 = *"exactly one SM generation + conjugate, nothing missing, nothing extra."*
> **B308: generations, if anywhere, come from a multiplicity mechanism. Four
> candidates, zero multiplicities.**
>
> **The audit that concluded "No" was incomplete — it omitted B632 — and the omission
> did not change the answer.**

# §4 — THE METHOD NOTE, BECAUSE IT IS THE SESSION'S SIXTH

**cc3 quoted a `head`-truncated output as if it were the complete result, then carried
the false gap into two pushed relays and into the plan as item 3.**

**Sixth instance of the family, and the third distinct species:**

| species | instances |
|---|---|
| **the search could not run** | branch gap · ASCII-vs-Unicode · `timeout` absent · `B\d{1,3}` (B1001) |
| **the search ran but changed units** | `grep -c -o` counting occurrences as lines |
| **the search ran and cc3 read a truncation as the whole** | **this one** |

**`SWEEP_NOTES` §A amended: `head`/`tail` output is a WINDOW. Never conclude a
population from a windowed view — re-run unwindowed before the sentence.**

---

**Plan status: 3 of 10 done.** Next: B1012's four harvest-register OWEDs (item 4).
