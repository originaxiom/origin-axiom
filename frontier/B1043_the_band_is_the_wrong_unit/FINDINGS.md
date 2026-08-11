# B1043 — the band is the wrong unit, and it made this refresh restore a settled question as open

**Date:** 2026-08-11 · **Lane:** the consolidation refresh, auditing **its own method**. Gate 5
untouched; zero anchors; nothing to `CLAIMS.md`.
**Files:** `verify.py` → `results.json` (8 checks) · lock `tests/test_b1043_band_unit.py`.

**Occasion.** Sweeping band **B200–B299** — the campaign's next unit of work — the first row read,
**B232**, turned out to be a law this refresh had already restored from a *different* band.

---

## 1. THE CORRECTION, AND IT IS TO MY OWN ARC

**B1039 restored B141's Item 4 as an open conjecture**, carefully and with the tier named:
*"a CONJECTURE in its own arc (a 60/60 numerical search) and restored as one."*

> ### It is not open. **B564 closed it** — and says so in its own first paragraph.
>
> *"The SL(3) φ-fixed locus contains no irreducible representation: **φ-fixedness pins A to finite
> order**, which forces the intertwiner to split block-diagonally."* … *"**This confirms the B141
> Item-4 conjecture** and extends B142's principal-only (Klein-4) result to the full locus."*

And it closed it **by symbolic elimination** — precisely the route **B141 itself named as *"the
rigorous path"*** and **B142 called *"the symbolic-elimination prize"***. The cluster's own stated
prize had been claimed, four hundred arcs later, and the restoration did not know.

**Nothing I read could have told me, and that is the point.** **B141 and B142 carry no forward
pointer to B564** — verified — and B564 is four bands away. Campaign step 1 says *read the bodies,
not the claim lines*; I did, and the bodies are silent, because a body cannot cite its own future.

## 2. THE MECHANISM

**B1037 dispositioned debt by BAND.** A band is an interval of B-numbers — that is, of **banking
date**. A law is a statement about **what an arc says**. Where a law spans bands, a band-wise sweep
**cuts it**, and cuts it *silently*, because the in-band bodies never mention the out-of-band
sibling.

**B1037's headline stands unchanged** — *"37 rows are 17 statements."* What is added: **the 17 do
not close at the band boundary.**

## 3. THE SHAPE, MEASURED ON THIS REFRESH'S OWN RESTORATIONS

| restored law | siblings **still in debt**, by band |
|---|---|
| **the tower** (B1038) | **B33** (B000s) · **B232** (B200s) · **B522** (B500s) |
| **φ-fixed reducibility** (B1039) | **B564** (B500s) — *and it closes the cluster's open question* |
| **the metallic exponent** (B1039) | **B75**, **B77** (B000s) · **B106** (B100s) · **B257** (B200s) |
| **isomonodromy** (B1040) | **none** |

**Eight siblings across four bands** — and **isomonodromy is the control**: B1040's cluster really
was band-local, so a law *can* be complete inside one band. **The finding is that most are not**,
and a sweep that assumes they are will report a band closed while its laws are not.

## 4. B232 IS NOT A SIBLING — IT IS THE SAME LAW, DIFFERENTIATED

Verified symbolically for `n = 3..12`:

| | |
|---|---|
| **B1038 (band form)** | `ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`, `W = V ⊕ 1` |
| **B232 (step form)** | `ρ_n ≅ ρ_{n−1} ⊕ Sym^n(V) ⊕ Sym^{n−3}(V)` |

**The second is the first's difference.** `band(n) − band(n−1) = Sym^n(V) + Sym^{n−3}(V)`, exactly,
via the functorial hinge `Sym^a(V⊕1) = ⊕_{k≤a} Sym^k(V)` that B1038 already had to verify. Both
give `dim = n²−1`; the step size is `2n−1`, telescoping to `n²−1`.

> **Not two results. One law, stated two ways, banked in two bands** — and the band-wise sweep saw
> one of them.

## 5. WHAT IS **NOT** DONE

**The corpus is not re-dispositioned by topic.** That is a **different instrument** from the band
sweep, it would re-open every band already closed — including B100–B199, whose figures are
published and dated — and whether to do it, or to retire the band sweep, is the owner's call.
**Registered as L164** with the measurement that motivates it and the eight siblings named, so the
next pass starts from evidence rather than from scratch.

**A cheaper middle path is stated there and deliberately not chosen here:** keep the band sweep and
add **a topic search per law at restoration time** — which would have caught B564 for the price of
one grep.

---

**Verdict: PROVED** as an audit-and-correction. 8 checks.

**Self-correction — this is the fourth time in twenty arcs that the record already held what I was
about to claim, and the first time it cost a published overstatement rather than only a rewrite.**
B1040's `(g,n)` count was classical and `OPEN_LEADS` said so; B511's arcsine bug was caught in
`D3_PARTIAL.md` in July; B1041's headline mechanism was Review 42's. **Each of those I caught
before banking. This one I did not** — B1039 shipped with Item 4 called open, and it took the next
band's sweep to find it. *The near-miss rate was three in eighteen; the miss rate is now one in
twenty, and the difference between them is a grep.*
