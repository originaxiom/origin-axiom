# Phase C — Exhaustive survey of emergence-paths

This directory is the **systematic survey** of mechanisms by which "nothing being
unstable" could produce reality. It is governed by `../GOVERNANCE.md` and follows
the probe-and-verdict pattern established by `../frontier/B1`–`B5`.

The goal is **not** to validate a single mechanism (Phases 0–B already did that for
the L/R/A record system and the figure-eight). The goal is to **map the path-space**
— enumerate plausible emergence-mechanisms, probe each until it carries a definite
verdict, and let the resulting map be the deliverable.

The user's framing — *"exhaust all possible paths until reality emerges, if it does
at all"* — is taken at face value. The honest expected outcome is that most paths
will `STALLED` at the same wall the existing frontier probes hit (well-defined
content, unconstructed bridge to an observable). Recognizing that wall as
*universal across mechanism classes* would itself be a finding.

## Ground rules (carried over from `../GOVERNANCE.md`)

- Nothing in `paths/` is a `proven` claim. Probes are *logged observations*.
- A probe is finished only when its `FINDINGS.md` ends with **exactly one** of the
  four verdict labels listed below. No "interesting, continue."
- A probe that produces a result the gate (`GOVERNANCE.md` §5) accepts may be
  promoted to `../CLAIMS.md`. None is expected to.
- The anti-overclaim glossary (`GOVERNANCE.md` §8) applies. Probes name their
  mathematical content precisely and refuse to dress it in physics language they
  haven't earned.

## Verdict labels

| Label | Meaning |
|---|---|
| `PRODUCES-OBSERVABLE` | The path yields a quantity that distinguishes it from competing paths or matches a measurement. Rare; triggers the `conditional → proven` gate. |
| `STALLED` | Well-defined content; an unconstructed step. The specific missing step is named in the findings. |
| `DEAD` | Falsified, shown circular, or shown numerological. Cross-linked to `../docs/ARCHIVE.md` if it was ever a claim. |
| `NEEDS-EXPERTISE` | Requires specific domain knowledge unavailable here. Flagged cleanly for outside input. |

## Layout

```
paths/
├── README.md                        this file
├── PATHS.md                         the 25-path registry
├── MECHANISM_CLASSES.md             the class structure (A–L) with rationale
├── philosophical/
│   └── PHILOSOPHICAL_PATHS.md       P1–P5 — separate register for non-mathematizable paths
├── E5_vilenkin_tunneling/           first-batch probe
├── E11_entropic_emergence/          first-batch probe
└── E14_categorical_initial_object/  first-batch probe
```

Existing frontier work (`../frontier/B1`–`B5`) is cross-linked from `PATHS.md` for
the paths it partially explored (E1, E2, E3, E6, E20) — not duplicated.

## First batch

Three paths spanning maximally different mechanism classes:

1. **E14** — categorical / initial-object (formal: is "nothing" even well-defined?)
2. **E11** — entropic emergence (statistical: does counting alone suffice?)
3. **E5** — Vilenkin tunneling (physics-literature: does the mainstream answer work?)

See `PATHS.md` for the full registry and per-path stubs.
