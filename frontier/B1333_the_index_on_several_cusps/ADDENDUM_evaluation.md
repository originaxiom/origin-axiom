# B1333 addendum — the evaluation: the trigger does not fire

The instrument of B1333 makes §14's named computation possible. Here it is, run.

## What was asked

Falsifier 6 of THE PAPER, listed there as an **upgrade trigger** rather than a falsifier:

> *Exhibit a non-zero index, with its four identities intact, on an unprotected twist sector of a
> chiral cover of the object.* … *it would move the chirality bit from* withheld at every computed
> sector *to* supplied on the tower, *and §8 names where to look (the multi-cusped chiral covers).*

## Pass 0 — all 54, not 51: the three "unrecognised" covers were a normalisation artifact

`d9_5`, `d10_6`, `d10_8` failed PSLQ at 60 digits. The diagnosis matters: **every trace of all three,
traces of squares included, lies in `Q(sqrt-3)`** — so the arithmetic survives and nothing is wrong
with the covers. What failed was the *conjugate* chosen. The normalisation conjugates by a matrix
built from a cusp's meridian fixed point and then rescales by one chosen entry; that can push
individual entries out of `Q(zeta_12)` while every trace stays in `Q(sqrt-3)`. Trying the other
natural rescalings recognises all three immediately, and their relators check out at `+-I`.

**All 54 chiral multi-cusped covers are now exact over `Q(zeta_12)`.** (A first pass mis-read a
PSLQ degree-5 "minimal polynomial" as evidence of a bigger field; at 80 digits with coefficients to
`10^10` that is inside the spurious-relation zone — 60 digits of freedom against a 45-digit
tolerance — and it was discarded rather than reported.)

`v2873` — B1330's one-cusped target that stayed mod-`p` only — is **not** fixed by this and remains
unrecognised. That caveat stands.

## Pass 1 — every cover, three primes

All 54 covers, `p = 13, 37, 61`, holonomy recognised **exactly** with only the ranks taken mod `p`:

```
COVERS 54 | SECTORS 38070 | identity-broken 0 | prime-skips 9
LIVE sectors (t0>=1): 7739        sectors with >=2 LIVE CUSPS: 1841
prediction violations: 0
NON-ZERO INDEX: 0
```

The distribution reaches `(5 cusps, 5 live, t_0 = 10)`. **Every sector returns `I = 0`.**
(The first pass — 51 covers, one prime, leaner germs, 5706 sectors — is in
`logs/sweep_lean.log` and agrees.)

**The derived prediction holds in all 5706 sectors, with no exception**: a cusp where `psi` is
non-trivial is invisible to the index (`t_0 = t_1 = 0`), so the index sees only its live cusps.

## Pass 2 — the richest sectors, exactly over `Q(zeta_12)`

`mod p` is **not** a proof here, and the reason is worth stating: `r_1` is a *difference* of two
ranks and each can drop mod `p`, so there is no clean one-sided bound of the kind that would let a
mod-`p` zero force an exact zero. The sectors where this matters most — the most live cusps, where
cancellation between cusps is possible — are therefore redone in exact arithmetic:

```
d10_32, d10_17  (the two 5-cusped chiral covers)
EXACT SECTORS 486 | identity-broken 0
with >=2 live cusps: 58        (including 2 with ALL FIVE cusps live)
NON-ZERO (EXACT): 0
```

## What this settles, and what it does not

**Settles.** The computation §14 says is owed is done. Across every recognisable chiral multi-cusped
cover of the object to degree ten, with the four identities intact in every one of 38556 sectors,
**the index does not go non-zero**. In particular it does not go non-zero in the 1841 sectors with
**two or more live cusps** — the regime that cannot exist on one cusp, and the one place B1332's
vanishing mechanism was known to stop applying. The vanishing is more robust than the mechanism
that was found for it.

**Does not settle.** The trigger is **not fired**; it is also **not proved unfireable**. Honestly:

- the broad pass is mod `p` at three primes, with 9 cover/prime pairs skipped for bad reduction;
- the exact pass covers the two 5-cusped covers at one germ shape, not the whole family;
- the germ set reaches `Sym^4` and `Sym^2 (+) Sym^4` but not the full range B1330 used on the
  one-cusped targets.

So this is a strong negative over a wide but not exhaustive family, and it is recorded as that.
Widening it is cheap now that the covers are cached and the instrument exists.

## What it means for the two branches

§14 gives chirality two branches: exhibit a non-zero index on the tower, or prove none exists.
This closes off a large part of the first and correspondingly strengthens the second — the same
direction B1330, B1331 and B1332 have been pushing. The multi-cusp case was the last structurally
distinct place the first branch could have fired inside the current framework, and it did not.

Reproduce: `verification/cache_covers.py <lo> <hi>` (recognise and cache the covers once),
`verification/sweepc.py` (the mod-`p` pass; `GERMS=lean|mid|full`, `PRIMES=13,37,61`),
`verification/exactconf.py <tags>` (the exact confirmation). Logs: `verification/logs/sweep_lean.log`,
`verification/logs/exact_5cusp.log`.
