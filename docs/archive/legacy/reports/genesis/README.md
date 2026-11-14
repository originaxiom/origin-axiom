# Genesis era — original Origin Axiom documents (October 2025)

This directory holds the four earliest surviving documents of the project, predating
the May-2026 governance framework. They are **historical only**. Per
`../../../GOVERNANCE.md`, no claims may be extracted from them.

The reason these four documents are curated here, while the rest of the Oct-2025
"Non-Cancelling Principle" archive remains in `legacy/raw/` (git-ignored), is that
the **Session 3 synthesis (2026-05-27)** reconnected the original field-theory
intuition documented here to the algebraic skeleton (A = LR, figure-eight, φ)
locked by Phase A. They are now provenance for that reconnection — see
`PROGRESS_LOG.md` entry "2026-05-27 — Session 3 synthesis".

## Files

| File | Date | Role | In public tree? |
|---|---|---|---|
| `00_Conceptual_foundation.pdf` | Oct 2025 | The conceptual master document. Records three moves: (1) Euler-identity-as-cancellation → φ^φ seed; (2) pivot to θ-agnostic, dropping φ^φ as input; (3) **non-cancellation as the sole core invariant**. The "Origin Axiom" name and posture come from this PDF. | **Yes** — committed (verified free of personal identifiers). |
| `01_Master.txt` | Oct 2025 | First working conversation transcript. Contains the seed formula proposal, the Lagrangian `L = (1/2)(∂Φ)² + α[1 - cos(Φ)]`, and the honest critique that the cosine potential has the **wrong minimum** (at Φ = 0, conflicting with non-cancellation). | No — see note below. |
| `02_Master_file_2.txt` | Oct 2025 | Execution-oriented indexing. Documents the numerical pipeline (Phase II-A/B, Phase III cavity, convergence tests). | No — see note below. |
| `03_Master_phase3.txt` | Oct 2025 | Verification of numerical outputs from Phase II/III/IV simulations. | No — see note below. |

### Why the three `.txt` transcripts are not in the public tree

This repository is **public**. The three raw conversation transcripts contain
personal identifiers — including **third-party email addresses** and the author's
own contact details and name — that should not be published. They are therefore
**git-ignored** here (`.gitignore`: `legacy/reports/genesis/*.txt`) and retained
in full under the git-ignored archive `legacy/raw/old/even older/e_origin axiom/`
(see `PROVENANCE.md` §3.0), which is the project's private record.

The committed `00_Conceptual_foundation.pdf` carries the actual conceptual
content of the genesis era and was verified to contain no personal identifiers.
The historical substance of the three transcripts — the cosine-potential
Lagrangian and the "wrong minimum" critique — is summarised in the table above
and in `PROGRESS_LOG.md` (2026-05-27), so nothing of research value is lost from
the public record. If a redacted version of the transcripts is ever wanted in the
public tree, that is a deliberate follow-up, not a default.

## Why these are not claim-sources

1. They predate `GOVERNANCE.md`. The promotion-gate concept did not exist yet.
2. The numerical results (cosine-potential simulations) are **superseded** by the
   derived cubic potential `V(τ) = κ(τ³/3 - τ²/2 - τ)` of P16 (Session 3
   synthesis, 2026-05-27). The cosine guess had a minimum at zero; the derived
   cubic has its minimum at φ — which is the *correct* shape for the
   non-cancellation intuition.
3. The φ^φ aesthetic seed was dropped by the project itself (move (2) above)
   long before Phase A. It belongs only in the historical record.

## Their actual value

The intellectual arc:

```
Oct 2025 — non-cancellation intuition (this directory)
             ↓
Dec 2025 — θ-agnostic scalar framework (origin-axiom-framework, see PROVENANCE §2)
             ↓
May 2026 — knot-theory turn (legacy/raw/old/Oa_05-26)
             ↓
May 22 2026 — algebraic skeleton locked (Phase A: P1–P13)
             ↓
May 27 2026 — Session 3 synthesis: derived potential closes the search
                  opened in 00_Conceptual_foundation.pdf
```

The PDF and conversation transcripts here are the **upstream** of that arc. They
document where the project's central question came from, in the user's own
words, before any of the current vocabulary existed. That is their role.
