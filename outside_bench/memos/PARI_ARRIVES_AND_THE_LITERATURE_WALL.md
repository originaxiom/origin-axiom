# Memo 219 — PARI ARRIVES AND IS VALIDATED; AND THE LITERATURE CHANNEL IS NARROWER THAN "UNREAD"

**Authorization:** the owner, this session — *"lets read the literature, also install pari safe in your box."*
**Certificate:** `outside_bench/certificates/pari_arrives.py` ·
**Output:** `outside_bench/outputs/pari_arrives.txt`
**No seal** — this records a capability, a validation, and a measured constraint.

---

## 1. PARI/GP is installed, safely

`apt-get install pari-gp` from the **signed Ubuntu `noble/universe` archive**:
**GP/PARI 2.15.4**, amd64, GMP-6.3.0, plus `pari-galdata`, `pari-elldata`, `pari-seadata`,
`pari-doc`. **No third-party source, no build from source, no TLS verification disabled, no
proxy bypass.** Two `ppa.launchpadcontent.net` PPAs are refused by the egress gateway; they
are unrelated to PARI and were left refused. Disk after install: 28 G free of 252 G.

## 2. Validated against a hand proof before being used for anything

`B1093` proved five facts about `K = ℚ[x]/(x³ − 12x − 5)` **by hand** — its own words:
*"no PARI; sympy + hand-rolled algorithms."* A new tool's first job is to agree with what
the bench already proved the hard way.

| fact | B1093, by hand | PARI, this run |
|---|---|---|
| field discriminant | `6237 = 3⁴·7·11` | **6237** |
| `ℤ[θ] = O_K` | Dedekind's criterion at the sole candidate `p = 3` | **index 1** |
| totally real | signature map surjective, signs fill `{±1}³` | **`[3, 0]`** |
| class number | `h(K) = 1` **proved** via Minkowski bound ≈ 17.55, all eight prime ideals exhibited principal | **1**, class group `[]` |
| fundamental units | `N(θ²+2θ−4) = +1`, `N(3θ²+6θ+2) = −1` | **`x²+2x−4`** and **`3x²+6x+2`** |
| narrow class number | `h⁺ = h = 1` | **`[1, [], []]`** |

> **7 of 7 checks agree.** A tool that reproduces a hand proof is usable; one that does not
> is not.

*Operational note: the first attempt used `bnfinit(…, 1)` — the unconditional-certification
flag — and hung. That is the flag's cost, not the install's; without it the whole computation
returns in under a second.*

## 3. The literature channel, measured rather than assumed

Memos 211, 214 and 218 each ended with a clause of the form *"literature, unread here."* That
was imprecise. **The full texts are not reachable from this box at all**, and the block is at
the network gateway, not in my willingness:

| attempt | result |
|---|---|
| `arxiv.org/abs/0712.1377` | **`EGRESS_BLOCKED`** — *"blocked by the network egress proxy"* |
| `people.tamu.edu/~rowell/RSW.pdf` (the author's own copy) | **`EGRESS_BLOCKED`** |
| `escholarship.org/uc/item/9pv08032` | **`EGRESS_BLOCKED`** |
| **WebSearch** | **works** |

> **So "read the literature" is not currently available to this bench: only search summaries
> are.** The gateway's policy is not something to work around, and no attempt was made to.
> The honest replacement for *"unread here"* is **"unreachable from here, by a named network
> policy, with search summaries as the only channel."**

## 4. What the search channel did establish — labelled, because it is not a read

**SEARCH-DERIVED, NOT READ. None of the following is a theorem this bench has verified, and
none of it is cited as such.**

- **Rowell–Stong–Wang, "On classification of modular tensor categories" (arXiv:0712.1377):**
  unitary modular tensor categories of **rank ≤ 4** are classified — **35 up to ribbon tensor
  equivalence**, obtainable from **10 non-trivial prime UMTCs** by direct product and symmetry
  operations.
- **Mignard–Schauenburg, "Modular categories are not determined by their modular data"
  (arXiv:1708.02796, published Lett. Math. Phys. 2021):** arbitrarily many pairwise
  inequivalent modular categories can share the same modular data — **and the smallest known
  such family is rank 49**, for `G = ℤ₁₁ ⋊ ℤ₅`.

## 5. What this does and does not do to L72's residual

Both facts point the same way for the rank-3 Müger centraliser of memo 211: the rank-3 case
sits inside a finite classified list, and the known failure of modular data is fourteen times
further up the rank ladder.

> **It is still not discharged.** This bench does not close a residual on search summaries —
> that is the same standard that made memos 206, 211 and 218 worth anything. **What changes
> is the quality of the handoff:** the residual's blocker is no longer *"someone should read
> a paper"* but **a named, reproducible network egress policy**, and the two specific
> documents that would settle it are identified by arXiv number.

## 6. What PARI opens, and it is not this

The residual PARI was wanted for is **memo 204 addendum 4**: *"is `E` split over `K` itself?"*
— reduced there to the ramification of one quaternion algebra over `K`, unramified at all
three real places, and explicitly handed off as *"a question a seat with a number-theory
package (`pari`/`sage`) could answer directly."*

**That handoff is now half-answerable here, and the missing half is not PARI's.** The
quaternion algebra is pinned by memo 204 only as *"contains `K(√77)` as a maximal subfield"*
— i.e. as `(77, b)_K` with `b` **unknown**. PARI decides splitting from `(a, b)`; it cannot
supply `b`.

> **The live computable item is therefore the one memo 204 called intractable: the explicit
> 48×48 commutant over ℚ, "twice killed by resource limits" under sympy.** PARI's linear
> algebra over ℚ is a different instrument from sympy's, and that computation is the next
> thing to attempt. **Named, not attempted here.**

---

## ADDENDUM 1 (2026-09-13, same day) — §5's "still not discharged" is SUPERSEDED

§5 concluded that L72's residual *"is still not discharged"*, because the two settling
documents were unreachable from this box. **The owner then supplied both as PDFs.**

**Read, quoted and verified in memo 220, the residual closes.** RSW §5.4, verbatim:
*"For the (A₁, 5)_½ fusion rule, all unitary MTCs are the one listed in last subsection and
those from the two symmetries S → −S and complex conjugate."* Our centraliser's fusion rules
and quantum dimensions match RSW §5.3.6 and Theorem 3.2(3) exactly, and it is the complex
conjugate of their listed representative.

**What stands unchanged:** §3's measurement of the egress block — `arxiv.org`,
`people.tamu.edu` and `escholarship.org` all `EGRESS_BLOCKED`, WebSearch the only channel —
and §4's insistence that search summaries are not a read. **That insistence is exactly why
the upload mattered**: memo 220 shows the summary-level principle (*"modular data determines
the category"*) would have discharged the residual **wrongly**.

---

# ADDENDUM 2 (2026-09-13) — **§6's "LIVE COMPUTABLE ITEM" IS DISCHARGED WITHOUT BEING RUN** (memo 222)

§6 closed: *"THE LIVE COMPUTABLE ITEM IS THEREFORE THE ONE MEMO 204 CALLED INTRACTABLE: the
explicit 48×48 commutant over ℚ … PARI's rational linear algebra is a different instrument.
NAMED, NOT ATTEMPTED HERE."*

**It is still not attempted, and it is no longer needed.** The owner supplied KMRT on
2026-09-13. Memo 222 answers the question that computation was named for — *is `E` split over
`K`?* — **YES**, from KMRT Prop. 43.6 plus a finite, exhaustive local computation (`n_p ≤ 1`
for every rational prime `p`; see memo 204 ADDENDUM 5).

> **§6 is SUPERSEDED on this point.** The 48×48 commutant is no longer the bench's live
> computable item; it would now only *re-derive* an answer already in hand by a cheaper route.
> Anything it could still contribute is the explicit `a ∈ K×`, not the split/non-split verdict.

**§5's egress measurement stands unchanged**, and its lesson is reinforced for the third time:
the blocker was never the arithmetic, it was the reading channel. Three papers and one book,
all owner-supplied, have now settled three items this box could not reach —
L72's uniqueness residual (memo 220), memo 210's two successors (memo 221), and memo 204
addendum 4's `E`-question (memo 222).
