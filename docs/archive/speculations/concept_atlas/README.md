# The Concept Atlas — a physics-concept guidebook for the object

**Status: a governed instrument of the `speculations/` room (owner-requested, 2026-07-07).
Firewalled one-way; nothing here promotes to `CLAIMS.md`; every card cites banked B/V/P numbers
for traceability only. The two never-crossed lines (numerology; tower-eigenvalues=masses) bind
every card.**

## Why this exists

The firewall taught the program to *refuse* interpretation but gave it no governed place to
*practice* it — so every approach to the physics wall happened "in the dark" (owner's diagnosis).
This atlas is the fix: **naming-as-exploration, honestly labeled** — a card deck mapping physics
concepts to the object's mathematics, each card stating exactly what is banked, what merely
rhymes, what is empty, and what is already dead. It is a guidebook for intuition and probe
design, never a ledger of claims.

## The card format

```
## <concept>
- physics essence: what the concept IS, mathematically, in physics
- object counterpart: the banked structure(s) that correspond, with B/V/P numbers
- status: MAPPED-EXACT | RHYME | EMPTY | KILLED   (+ tags [MATH]/[HOOK]/[LEAP])
- sharpen: the computation that would sharpen the card
- trap: the falsifier / the known kill / the pre-registered trap
```

**Status meanings.** `MAPPED-EXACT`: the object owns an exact, banked structure that IS the
concept's mathematical content (at the stated level — often kernel/form, never value).
`RHYME`: a real structural resemblance, unassembled or unproven — motivation-grade.
`EMPTY`: no known counterpart; the card records the absence honestly.
`KILLED`: the identification was tried and died; the card records why and where (tombstones).

## Use

```
python3 query.py list              # all cards + statuses
python3 query.py card entropy      # print one card
python3 query.py status KILLED     # all cards with a given status
```

Cards are edited like any speculation: statuses may be upgraded/downgraded only with a citation;
a value-match on any card is HELD(value-matching) by default (GOVERNANCE.md rule).
