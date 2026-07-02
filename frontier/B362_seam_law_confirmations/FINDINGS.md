# B362 — the law's confirmations: three pre-registered predictions, three hits (11 pairs, 0 counterexamples)

**Status: banked (frontier), EXACT tier (B358 engine). The B361 pre-registrations, run same-day. Firewalled;
nothing to `CLAIMS.md`.**

| pair | prediction (B361) | **verdict (exact)** |
|---|---|---|
| (2,7) | bright (both seeds doubly-elliptic) | **BRIGHT** ✓ — 12/17, `s ∈ {±1/48, ±1/96}` |
| (1,5) | dark (no doubly-elliptic seed) | **DARK** ✓ — 0/6 |
| (4,5) | dark | **DARK** ✓ — 0/6 |

**The local law now stands at 11 exact pairs, zero counterexamples:** bright = {(1,2), (2,3), (2,4), (1,7),
(3,7), (2,7)}; dark = {(1,3), (1,4), (3,5), (1,5), (4,5)} — exactly the pairs containing a doubly-elliptic
seed (m ∈ {2, 7}: char poly irreducible mod 3 *and* mod 5).

**Another value-echo:** (2,7)'s `s`-set equals (1,7)'s (`{±1/48, ±1/96}`), while (1,2)'s richer 12-value set
shows the value-map depends on the key seed as well as the partner — logged for the post-L57 value-map pass.

Tiers: EXACT verdicts; the law remains a law of the computed range (11 points), theta-lift sector, pending
L57. Reproducer: `seam_confirm.py` (regenerable); test: `tests/test_b362_seam_law_confirmations.py`.

**Provenance.** B361 (the pre-registrations), B358–B360 (the arc), L57.
