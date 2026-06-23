# B197 — the figure-eight volume-tie is broken by torsion-freeness (a verified chat2 increment)

**Date:** 2026-06-23. **Status:** foundation-stress (Step-1 selection, CLAIMS C1); **form-side**, `K010` boundary.
A cross-session (chat2, 2026-06-23) probe stress-tested the figure-eight selection; **independently re-derived
here** (verify-don't-trust — own enumerator + SnapPy, not chat2's scripts). **The one genuine new increment:** P10's
*unresolved* m003 volume-tie is **broken by torsion-freeness** — among torsion-free bundles the figure-eight is the
**unique** volume minimum. The rest of the chat2 note re-derives already-banked work (K016 selection criteria, P10
filters) and is **cited, not re-banked**. **Firewall-side:** no scale/Λ/contents; **nothing to `../../CLAIMS.md`**;
P1–P16 frozen. Ledger V189. Reproducer `volume_selection.py` (`ALL CHECKS PASS`).

## The increment (verified)

P10 (post-V145) records that minimum hyperbolic volume *"ties the sister m003 … does **not** uniquely select 4₁ …
suggestive, NEEDS-SPECIALIST."* The tie is real but **cross-family** and **torsion-broken**:

| | volume | H1 | b++ ? |
|---|---|---|---|
| **figure-eight** (m004 = b++LR = 4₁) | 2.0298832128 | ℤ (torsion-free) | yes |
| **m003** (the sister) | 2.0298832128 (identical) | **ℤ/5 + ℤ** (torsion) | **no** (not a positive-word bundle) |

So the m003 tie is excluded by the **torsion-free** filter the trace-3 sieve already uses: **among torsion-free /
within b++, the figure-eight is the unique volume minimum** (verified over all 241 b++ bundles to length 10; next
smallest is the LRR/LLR chiral pair at 2.6667). This **sharpens** P10's volume filter from "ties m003 (not unique)"
to "unique among torsion-free."

## Independently re-derived (the full battery)

- **C1 [identity]** `b++LR ≅ m004 ≅ 4₁` (figure-eight): vol 2.0298832128, H1=ℤ, 1 cusp (SnapPy).
- **C2 [combinatorial min]** among the **2587** cyclically-reduced positive (b++) L/R necklaces with both letters to
  length 14, `LR` is the **unique** minimum trace (=3) **and** the unique shortest word; the metallic family
  `R^mL^m` has trace `m²+2` (3,6,11,18). *(Overlaps K016 — cited, not new.)*
- **C3 [the increment]** the volume tie broken by torsion-freeness (table above) — the genuine new, verified result.
- **C4 [chiral seal corroboration]** the chiral pair `b++RRL` / `b++RLL` have equal volume (2.6667, orientation-even)
  and opposite Chern–Simons `CS = ±1/48` (orientation-odd) — the mirror-closure seal with real CS values.

## Honest framing (per the V145 self-audit — do NOT re-inflate)

V145 deliberately reworded P10 to *"trace-3 sieve **proved**; the four further filters are suggestive, not proven to
uniquely select — NEEDS-SPECIALIST."* This increment **respects** that:
- the **trace-3 algebraic sieve (P10) remains the only proof** of uniqueness;
- volume is now **"unique *given* torsion-free"** — a sharpening, but it **leans on the same torsion-free condition**
  the trace-3 sieve uses, so it is **not an independent axis**;
- shortest-word / min-trace are **correlated** (short ⟹ small trace);
- the irreducible **"prefer simplicity" premise remains permanent** — this does not derive selection-at-all from the
  axioms, only shows the *object* is robust to *which* simplicity measure, *given* selection.

So B197 **hardens C1 modestly** (it resolves the volume filter's m003 caveat) — it does **not** make the figure-eight
selection "independently overdetermined" (the chat2 note's headline overstated this; the corrected reading is here).

## A proposed P10 sharpening (owner-gated — NOT committed)

P10's parenthetical *"[ties the sister m003 … does not uniquely select 4₁]"* could be sharpened to *"[ties the sister
m003 among all bundles, but **uniquely selects 4₁ among torsion-free** — m003 carries ℤ/5 torsion (B197); volume is
unique-given-torsion-free, not an independent proof]."* This is a CLAIMS edit and is **proposed for owner approval
only** — not made here.

## Scope / honesty
- Form-side only (*which* object is selected); no scale/Λ/contents; `K010` character-variety boundary.
- The "unique volume min" needs the scope **"within b++ / among torsion-free"** — a *stated* restriction (b++ is the
  metallic family's home; torsion-free is the trace-3 sieve's filter). Among **all** once-punctured-torus bundles the
  m003 same-volume manifold exists; the tie is broken only by the (motivated) torsion-free condition.
- The "CF-period-1 = metallic" sub-claim of the chat2 note is **not** re-derived here (not load-bearing; the
  elementary fact λ_m=[m;m,m,…] period-1 with m=1 minimal is standard).
- Cross-chat provenance: chat2 2026-06-23; **independently re-derived** before banking (verify-don't-trust); the bulk
  re-derives K016/P10 and is cited, not re-banked. Nothing to `../../CLAIMS.md`.

## Anchors
`CLAIMS.md` P10 (the trace-3 sieve + the four suggestive filters; the V145 down-tiering this respects), `K016` (the
m=1 selection criteria — min-volume #1, etc.; the bulk overlap), `K017`/`B146` (the "soft joint" this stress-tests),
`P9` (the m003 volume coincidence). External: SnapPy (volumes, homology, Chern–Simons); the figure-eight =
once-punctured-torus bundle with monodromy RL (trace 3); m003/m004 the minimal-volume cusped hyperbolic pair.

## Reproduction
`python frontier/B197_figure_eight_volume_torsionfree/volume_selection.py` — C1 identity; C2 combinatorial min;
C3 the volume tie broken by torsion-free (the increment); C4 the chiral CS seal; C5 the firewall/V145 framing.
Prints `ALL CHECKS PASS`. Fast locks in `tests/test_b197_figure_eight_volume_torsionfree.py` (2 tests; volume part
SnapPy-`importorskip`-gated).
