# Q1 REWRITE — the SEAM-A Gate 2 send, restated from B1198/B1201/B1209
## (outside bench, 2026-08-29; drafted at the owner's "write it", after memo 138 found Q1 stale by eight post-queue arcs. NOT SENT — the send is the owner's act under the owner's name, per the queue's own mechanics. This is a drop-in replacement for `docs/SPECIALIST_SEND_QUEUE.md`'s Q1 row plus the one-pager it would ship as.)

**Why it needed rewriting.** The queue was built at B1179. Q1's status
line still reads *"FLOOR (B1156); the a-priori MISMATCH refuted; the
full/Arakelov row carries Vol as the Borel regulator; the one bar is the
cusped extension."* Since then **eight arcs landed on this bar**, and one
of them **closed a route we had hoped for**. **The rewrite narrows the
ask** — the literature half is now partly done in-house, so the
specialist is asked something sharper.

---

## PART 1 — THE DROP-IN ROW

| # | bar | the bounded question (honest status) | who (type) | what a specialist could REFUTE | priority |
|---|---|---|---|---|---|
| Q1 | **SEAM-A Gate 2** (the prize crossing) | Does the Andersen–Hansen closed-surgery↔Vol correspondence extend to the cusped m004 — i.e. can a Kim-style arithmetic-CS **action** over ℚ(√−3) carry a finite-phase→Vol map? **Status, updated 2026-08-29:** the a-priori MISMATCH is refuted and the seam is a precise FLOOR (B1156). **The literature half is now in hand and verified on-bench** (B1209): Lee, arXiv:2502.11950, Thm 2 constructs for any complete finite-volume hyperbolic 3-manifold a **mixed Tate motive over the invariant trace field whose Beilinson regulator is the complex volume** — and m004's invariant trace field **is ℚ(√−3)**, so it lands over our field **by the general statement, with no special-casing**. **One route is now CLOSED with a mechanism:** Lee's choice of tangential base point is a torsor under **ℤ/\|a₁\|**, and **\|a₁\| = 1 at all four ideal points of m004** — re-derived independently from our own banked A-polynomial (B67: every Newton-polygon edge has \|ΔL\| = 1; boundary slopes ±4). **The torsor is trivial**, so it supplies **nothing free**, and there is **no contact** with the programme's orientation bit. **The W₀ bar therefore stands unchanged**, and the remaining bar is narrower than when this queue was written. | arithmetic-topology / arithmetic-CS (Kim school); quantum-topology (AH lineage) | that the cusped extension **provably fails** ⇒ SEAM-A seals as MISMATCH (an *answer*, not a loss); or that some **other** structure supplies the free archimedean marking, which would reopen the route we closed | ★★★★ (the one live crossing) |

---

## PART 2 — THE ONE-PAGER (what would actually be sent)

**Subject:** a bounded question on cusped arithmetic Chern–Simons and complex volume

We are a small independent programme working on one hyperbolic
3-manifold, the figure-eight knot complement **m004**, and its arithmetic.
We have one bounded question and a specific reason to think it is the
right one to ask. Everything below is either published work we cite, or
our own computation with a repository pointer.

**The setting.** We are trying to determine whether a Kim-style
**arithmetic Chern–Simons action** over ℚ(√−3) can carry a
finite-phase → volume map for the **cusped** m004 — the cusped analogue
of the Andersen–Hansen closed-surgery ↔ Vol correspondence. We call this
our "Gate 2". Our own a-priori mismatch argument against it has been
refuted (by us), and what remains is a precise floor rather than an
obstruction.

**What we already have, so you are not asked to redo it.**
Lee (arXiv:2502.11950, Thm 2) constructs, for any complete finite-volume
hyperbolic 3-manifold, a **mixed Tate motive over the invariant trace
field whose Beilinson regulator is the complex volume**. We obtained and
read §7.4 and Appendix A. Since m004's invariant trace field is
**ℚ(√−3)**, that construction lands over our field **by its general
statement** — no special-casing needed. Lee verifies Conjecture 7.4.2
for 4₁ (= m004) in Appendix A by direct computation on the
Neumann–Zagier potential.

**A route we closed ourselves, and why we mention it.** We had hoped
Lee's *choice of tangential base point* might supply a free archimedean
marking our construction lacks. **It does not.** The admissible set is a
torsor under **ℤ/|a₁|**, and (a₁, b₁) is a primitive edge vector of the
A-polynomial's Newton polygon; for m004 every edge has |ΔL| = 1, so
**|a₁| = 1 at all four ideal points** and the torsor is **trivial**. We
derived this independently from our own banked A-polynomial rather than
resting on the appendix, and Lee's own Appendix A reports the same four
cases. We also checked that the 4₁ confirmation does **not** rely on the
CS = 0 degeneracy. **So there is nothing free there for our manifold**,
and we would rather tell you that than have you find it.

**The question.**
> Given a mixed Tate motive over ℚ(√−3) whose Beilinson regulator is the
> complex volume, and given that the tangential base point supplies no
> freedom for this manifold — **does the Andersen–Hansen correspondence
> admit a cusped extension carrying a finite-phase → Vol map, or is there
> a structural obstruction to one?**

**Either answer is useful to us.** A proof that the cusped extension
fails **seals our Gate 2 as a mismatch**, which we would record as an
answer, not a loss. A construction, or a pointer to one we have missed,
opens the only live crossing we have.

**Status, honestly.** Conjecture 7.4.2 remains a **conjecture** in
general — verified by Lee for 4₁ and, for at least one ideal point, 5₁.
We assert nothing beyond those cases. Our own contributions here are the
|a₁| = 1 derivation and the negative result about the tangential base
point; the motive construction is Lee's.

**Pointers.** Repository, arc B1209 (the verification and the
A-polynomial computation), B1156 (the floor), B67 (the banked
A-polynomial).

---

## PART 3 — WHAT CHANGED, FOR THE RECORD

| | before (B1179) | after (this rewrite) |
|---|---|---|
| literature half | *"in hand rather than absent"* | **obtained, read, verified on-bench** (B1209) |
| tangential base point | hoped-for *"outside instance of the missing archimedean marking"* | **CLOSED with a mechanism** — torsor trivial, \|a₁\| = 1, independently derived |
| CS = 0 contact | untested | **checked and closed** — the appendix does not use it |
| trace field | assumed compatible | **confirmed by the general statement** — ℚ(√−3), no special-casing |
| the ask | broad | **narrower, and one dead end removed before asking** |

**The rewrite makes this a better send, not a weaker one.** We now tell
the specialist what we closed ourselves, which is the difference between
a question and a fishing trip.

**Not sent.** No address touched, no external contact of any kind. The
send is the owner's act under the owner's name.

---

# Q2 DISPOSITION (2026-08-29) — the staleness flag was MINE and it was WRONG; Q2's ask stands

**Memo 138 flagged Q2 STALE on two keyword hits. Re-checked, the flag is
substantially a FALSE POSITIVE of this bench's own detector** — of exactly
the shape B1210 caught on its own first pass ("MOSTLY NOISE"). Corrected
here rather than carried.

**Two objects, same two words:**

| | subject | target |
|---|---|---|
| **Q2 (B1137)** | regulators as **values** — L-values, ζ_K, ζ_F, π, √3, √5, log φ, ζ(3) | the **18 sealed SM targets** |
| **the flagged hits (B1198/B1209)** | a regulator **map** — Lee's mixed Tate motive | the **complex volume**, a *geometric* invariant |

**Verified:** neither B1198 nor B1209 mentions J₃(𝕆), the exceptional
domain, the M(𝕆,ℂ) closing, or Tier B. **Q2's ask stands as written.**

**And the obvious follow-on is already a banked negative:** B1126 swept
the **volume/ζ_K(2) family** among its 16 sealed periods against 22
live-fetched SM targets — 352 pairs, 351 below two significant figures,
consistent with noise. So B1209's *"the complex volume is a Beilinson
regulator"* opens **no** untested SM route.

## Two small honest additions to Q2's status line

**(i)** Cite **B1209 as adjacent-not-contradicting** — an outside
published Beilinson regulator over our own field exists, for a different
object and a geometric target. A specialist in this area will know that
paper; saying we know it too costs nothing and reads better than silence.

**(ii)** Name the **B1137 basis corner** ourselves, with its size stated:
the volume is swept as a **period** (B1126) but is **not a basis element**
in B1137's bounded-height **combination** sweep, and those are different
instruments. **This is an untested corner of one instrument, not a hole in
the negative** — and adding the volume to the basis and re-running is a
**bounded in-house cell, not a specialist question.** Naming it pre-empts
the obvious referee question and costs one clause.

## ⚠ AN ERROR CAUGHT INSIDE THE CHECK, recorded because it is the check's own subject

R3's first version tested `"vol" in claim` and returned **TRUE** — because
`vol` is a substring of **"in·vol·ves"** (*"an involves_regulator gate"*).
**A substring false positive, inside the cell written to catch a keyword
false positive.** Fixed by extracting the basis and matching on words.
The lesson is the cell's own thesis turned on itself: **a keyword detector
must be spot-checked on its own hits — including when the detector is
mine and the hit confirms what I expected.**

**Net:** **Q1 rewritten** (its staleness was verified case-by-case, not
from keyword hits — that call stands). **Q2 stands as written**, with two
one-clause additions. **Q3–Q6 READY.** **All six are now decision-ready.**
