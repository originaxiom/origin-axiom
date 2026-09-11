# B1333 addendum — the evaluation: the trigger does not fire

The instrument of B1333 makes §14's named computation possible. Here it is, run.

## What was asked

Falsifier 6 of THE PAPER, listed there as an **upgrade trigger** rather than a falsifier:

> *Exhibit a non-zero index, with its four identities intact, on an unprotected twist sector of a
> chiral cover of the object.* … *it would move the chirality bit from* withheld at every computed
> sector *to* supplied on the tower, *and §8 names where to look (the multi-cusped chiral covers).*

## Pass 1 — every recognisable cover, mod 13

All 51 chiral multi-cusped covers of `m004` to degree ten that PSLQ recognises over `Q(zeta_12)`;
the holonomy is recognised **exactly** and only the ranks are taken mod `p`.

```
COVERS 51 | SECTORS 5706 | identity-broken 0 | prime-skips 8
LIVE sectors (t0>=1): 1324        sectors with >=2 LIVE CUSPS: 336
prediction violations: 0
NON-ZERO INDEX: 0
```

The distribution reaches `(5 cusps, 5 live, t_0 = 10)`. **Every sector returns `I = 0`.**

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
cover of the object to degree ten, with the four identities intact in every one of 6192 sectors,
**the index does not go non-zero**. In particular it does not go non-zero in the 336 sectors with
**two or more live cusps** — the regime that cannot exist on one cusp, and the one place B1332's
vanishing mechanism was known to stop applying. The vanishing is more robust than the mechanism
that was found for it.

**Does not settle.** The trigger is **not fired**; it is also **not proved unfireable**. Honestly:

- the broad pass is at one prime (`p = 13`), with 8 cover/prime pairs skipped for bad reduction;
- the exact pass covers the two 5-cusped covers at one germ shape, not the whole family;
- the germ set is lean (`Sym^2`, `Sym^1 (+) Sym^1`-type sums up to `Sym^2 (+) Sym^2`), not the full
  range B1330 used on the one-cusped targets;
- 3 of the 54 covers resist PSLQ at 60 digits and were not evaluated at all.

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
