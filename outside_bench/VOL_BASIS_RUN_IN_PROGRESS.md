# THE VOLUME-IN-BASIS PROBE — RUNNING (scaffold banked mid-run, push-as-you-go clause 4)
## (outside bench, 2026-08-29. Seal: `seals/VOL_BASIS_PREREG.md`, committed and pushed BEFORE any computation. Replaced by a memo on completion.)

**The corner being closed.** B1137's regulator basis omits the complex
volume; B1209 banks that the complex volume **is** a Beilinson regulator
over ℚ(√−3). **Honest prior: a ninth value-crossing negative.** The cell
exists to close the corner, not to expect a hit.

## SETUP CONFIRMED SO FAR

- **Instrument reused verbatim** from the pinned commit — B1137's
  `regulators.py`, `basis.py`, `targets.py`, `pslq_probe.py`. No
  re-implementation, no re-tuned thresholds.
- **Sealed targets load with the matching hash:**
  `sha256 = e93efeaa132bf7c1a6e0a3a9d41a436ff03d2aea5f626a2b404a5ef8a317e101`,
  **18 targets**, loaded verbatim from B743, not re-selected here.
- **Basis omission re-confirmed from primary:** the pruned basis contains
  **no `vol`, no `CS`**.
- **Vol(m004) computed, not quoted:** from ½·Im Li₂(e^{2iθ}) at θ = π/3,
  Vol = 6Λ(π/3) = **2.029883212819307250042405108549040571883**, agreeing
  with the known value to **30 dps**.
- **Pipeline validated** on B1137's own smoke test (4 cells, 25 s).

## RUNNING NOW

1. **GATING REPRODUCTION CONTROL** — the full 216-cell real grid on the
   **unmodified** basis. Per seal §5, **if this does not recover B1137's
   headline (0 of 18 targets involve a regulator), no extended result may
   be reported at all.**
2. ✅ **HYGIENE PRE-STEP — RETURNED (seal §4 satisfied).** PSLQ at
   **dps 220, H = 10⁶** against B1137's **25-element pruned basis**:

   | direction | verdict |
   |---|---|
   | `vol` | **INDEPENDENT — keep** |
   | `vol_pinorm` | **INDEPENDENT — keep** |
   | `vol_over_zetaK2` | **INDEPENDENT — keep** |

   **0 dropped.** So the cell is **not** worthless on seal §4's first
   ground: the volume is a genuinely **new direction**, not a redundancy
   of the existing regulators. *(For contrast, B1137's own hygiene check
   found and dropped six exact linear redundancies among its raw and
   π-normalized entries — so this instrument does find dependence when it
   is there.)* **Target-free: no SM value was loaded.**

**CONTROL STILL RUNNING** (216 cells, ~20 min). **Nothing about targets
is claimed until it returns.** The two-outcome and the
four-gate hit discipline are fixed in the seal and are not editable.
