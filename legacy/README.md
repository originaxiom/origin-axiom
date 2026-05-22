# Legacy — Frozen Prior History

This directory preserves the project's history before the 2026-05-22 consolidation. Per
`GOVERNANCE.md`: **`legacy/` is never edited and is never a source of claims.** It exists for
credibility and traceability — see `../AUDIT_REPORT.md` and `../PROVENANCE.md` for the
reconciled analysis of what is in here.

## Layout

| Path | Tracked in git? | Contents |
|---|---|---|
| `reports/` | yes | Curated **text** reports extracted from the May-2026 master archive: the V4 paper, the Reality Check, the G1–G5 gate reports, `MANIFEST.json`. The authoritative self-assessments of the disciplined work thread. |
| `reports/session_md/` | yes | Loose markdown from the May-2026 sessions: progress log, research/execution plans, early paper drafts, factorization census, "novel findings honest". |
| `handoff/` | yes | `handoff.md` — the optimistic hand-off document. Retained as a historical record; **not** a source of claims (see `GOVERNANCE.md` §2). |
| `github-repos.md` | yes | Pointers to the four superseded GitHub repositories, with their final commit hashes. |
| `raw/` | **no — git-ignored** | The full raw binary archive (~4 GB): all session zip bundles, PDFs, the earlier-era `e_origin axiom` genesis folder, ChatGPT exports, numerical result files, and a local clone of the `00_origin-axiom` GitHub repo. Too heavy for git; preserved on disk and intended for a GitHub Release asset or external backup. |

## Eras represented (oldest first)

1. **`raw/old/even older/e_origin axiom/`** — genesis era (~Oct 2025). The original
   "Non-Cancelling Principle" documents and raw research exports. *Not yet audited in detail.*
2. **`raw/old/even older/00a_OriginAxiom/`** — the `φ^φ` era (pre-Dec 2025).
3. **`raw/old/even older/00_origin-axiom/`** — local clone of the GitHub `00_origin-axiom`.
4. **`raw/old/Oa_05-26/`** — the May-2026 sessions (the knot-theory turn). The
   curated text from this era is what lives committed under `reports/`.
5. **`raw/old/Chatterpillar.pdf`** — the 142-page May-2026 session transcript.

## Recovering raw artifacts

The committed `reports/` text covers the *substance* of the disciplined work. To inspect a
specific raw bundle, browse `raw/` locally. The May-2026 master archive
(`raw/old/Oa_05-26/origin_axiom_all_prior_bundles_MASTER.zip`) contains every
individual session bundle with `MANIFEST.json` SHA256 hashes.
