# sm:B1551 THE SPIN COVER — HELD as a draft (a thread result under THE WEAVE)

cc (the SM-derivation seat), 2026-10-07. **HELD, never sealed.** The owner's rule of the same day, now WORKING_RULES's THE
WEAVE — WEAVE OR THREAD? (`docs/THE_WEAVE.md`), puts this arc on one thread: m004's binary tetrahedral cover S, the kernel
of π₁(m004) → SL(2, F₃), of degree 24. In the weave's terms S is the common point's structure (W3 of
`docs/dossiers/the_weave_2026-10-07/`) seen on one thread, so any count read here is a thread result.

## What is here

The draft code (`draft_b1551/`) and one design-time structure census, kept so the work is not lost. No count was computed.
- `spin_lib.py`: S as the double cover of sm:B1550's tetrahedral cover N by the spin sign ε; its presentation; the
  characters; two routes (S's own Reidemeister–Schreier presentation, and Shapiro on N).
- `census.py`: every orbit of S's deck group 2T on S's characters of order dividing 4. Route P̃ reads every orbit; route S̃
  reads every orbit with a member, and the first 100 without one.
- The record: `census.jsonl.gz` (`gzip -n`; `census_sha256.txt`), collected into `population.json`.
- `run.py`, `read_out.py`, `controls.py`: the unsealed draft of the counts and their controls.

## What the census found (structure, design time)

- **2,800 orbits** of 2T on the 65,536 characters of order dividing 4. 107 orbits were read in both routes, and the routes
  agree on (h¹, r¹, n) at every one.
- **Seven member orbits, 42 members, every one pulled back from N.**
  - 12 sign members with interior 2: N's two sign orbits, A and B fused.
  - 24 order-4 members with interior 1: N's size-6 orbits.
  - 6 order-4 members with interior 4: N's size-3 orbits.
- **S has no member of its own at these orders.** So one module on S carries at most two generations at a sign member,
  where the interior is 2. Three in one module would need S's own members at other orders.

## Why it is held

It reads one thread. The weave's question is what the joint action of every move forces on every thread at once. The
spin cover reappears there for every odd-trace thread (W3), and B1538's T-THE-QUATERNION-LINE (room four over s) holds for
every Anosov monodromy. If the arc is resumed, it is resumed as a weave census over every odd-trace thread's spin cover.
