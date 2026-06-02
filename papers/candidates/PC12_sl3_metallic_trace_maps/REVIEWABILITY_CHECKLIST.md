# PC12 Reviewability Checklist

Status: reviewability checklist. Adds no claims; records no private
correspondence or identity data.

## Purpose

Use this checklist to validate PC12: the metallic `SL(3)` trace-map note —

```text
phi_m(a)=a^m b, phi_m(b)=a
  -> eight-coordinate SL(3,C) trace map T_m
  -> commutator trace-pair invariant
  -> algebraic entropy log mu_m
  -> fixed-line exchange-sector factorization
  -> fixed-line integer-splitting classification
  -> compact SU(3) diagonal slice
```

The target is narrow: is the trace-map package correct, correctly positioned in
the character-variety literature, and is the Section-6 splitting classification
genuinely new? Evaluate it as pure mathematics; do not supply a physical or
foundational reading.

## Competence Areas

Useful background:

```text
SL(3,C) / SL(n,C) character varieties of free groups (Lawton, Procesi)
trace identities and Cayley-Hamilton reduction
trace maps of substitutions; reversing symmetries (Baake-Grimm-Roberts)
algebraic entropy / degree growth (Bellon-Viallet)
elementary Diophantine / quadratic-form classification
(for Appendix A) numerical linear algebra, pseudoinverse conditioning
```

Poor first validation target:

```text
general physics or cosmology only
spectral theory of Schrodinger operators without character-variety background
number theory with no trace-map or character-variety contact
```

## Minimal Packet

Validate from the smallest useful packet:

```text
papers/candidates/PC12_sl3_metallic_trace_maps/DRAFT_NOTE.md
papers/candidates/PC12_sl3_metallic_trace_maps/REVIEW_PACKET.md
papers/candidates/PC12_sl3_metallic_trace_maps/LITERATURE_POSITIONING.md
papers/candidates/PC12_sl3_metallic_trace_maps/CERTIFICATE_APPENDIX.md
```

Optional context only if needed:

```text
papers/candidates/PC12_sl3_metallic_trace_maps/VALIDATION_BRIEF.md
frontier/B51_sl3_symbolic_m_factorization/FINDINGS.md
frontier/B57_general_m_splitting/FINDINGS.md
frontier/B61_sl5_high_precision/FINDINGS.md
```

Do not use:

```text
raw chats, private transcripts, or staging archives
physics-facing or foundational speculation
the whole repository as the first reading path
```

## Core Validation Questions

```text
Is the eight-coordinate trace convention standard and the recurrence indexing correct?
Is the commutator trace-pair invariant stated with the right convention?
Is the entropy a genuine no-cancellation degree-growth proof, not just observed growth?
Is the c=3 exchange-sector factorization (char(M^k) form) correctly derived for formal m?
Is the Section-6 splitting criterion correct, and is the classification complete?
Does the literature already contain the splitting classification, or the cross-n char(M^k) tower?
Is the compact SU(3) slice stated as compact-unitary mathematics only?
What concrete statement would kill or rescope the note?
```

(See `REVIEW_PACKET.md` for the five sharpened questions Q1-Q5.)

## Triage Instructions

After a finding:

1. Do not paste private correspondence into the repository.
2. Summarize the technical finding in `papers/VALIDATION_LEDGER.md`.
3. Assign one outcome label: `DRAFTABLE`, `NEEDS_REVISION`, `NEEDS_RESCOPING`,
   or `KILLED`.
4. Assign one decision: `ACCEPT_FIX`, `ACCEPT_CLARIFY`, `NEEDS_REPRO`,
   `DISPUTE_WITH_REASON`, `OUT_OF_SCOPE`, or `KILL_OR_RESCOPE`.
5. Patch the note, proofs, tests, or paper card only after the finding is
   triaged.

## Non-Claims To Preserve

Do not write validation text that implies:

```text
a physical interpretation of the trace map or its fixed line
the compact SU(3) slice is gauge theory or particle content
the direct/inverse trace distinction is particle/antiparticle physics
a derivation of units, gauge, gravity, spacetime, or observables
a connection to any external research program or foundational claim
the numerical Appendix-A tower is a proven theorem
```

Correct framing:

```text
a standalone metallic SL(3) trace-map note: standard methods (Sec 2-5) plus an
apparently-new elementary splitting classification (Sec 6); Appendix A numerical.
```
