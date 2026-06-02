# PC12 Review Packet — Metallic SL(3) Trace Maps

Status: external-review packet. A guide for a specialist audit of the metallic
`SL(3)` trace-map note. It promotes no claim and adds nothing to the claims
ledger. The mathematical object is meant to be evaluated on its own terms, as
character-variety / algebraic-dynamics mathematics.

## Review Target

The candidate is a short computational note: the trace map induced on the
rank-two `SL(3,C)` character variety by the metallic free-group automorphisms

```text
phi_m(a) = a^m b,    phi_m(b) = a        (m >= 1),
```

with (i) an explicit eight-coordinate Cayley-Hamilton form, (ii) a commutator
trace-pair invariant, (iii) algebraic entropy `log mu_m` (`mu_m` the metallic
mean), (iv) an exchange-symmetry factorization of the fixed-line linearization,
and (v) an integer-splitting classification of the antisymmetric fixed-line
quartic.

Per the internal literature screen (`LITERATURE_POSITIONING.md`), (i)-(iii) and
the exchange factorization are **standard methods** applied to this family
(Lawton; Horowitz; Procesi; Baake-Grimm-Roberts; Bellon-Viallet). The one
component not located in the literature is the **fixed-line integer-splitting
classification** (Section 6 of the note). An appendix records a *numerical*
higher-rank (`SL(n)`) continuation that is not part of the theorem package.

## Files To Read

Primary (the note + its support):

```text
papers/candidates/PC12_sl3_metallic_trace_maps/DRAFT_NOTE.md
papers/candidates/PC12_sl3_metallic_trace_maps/LITERATURE_POSITIONING.md
papers/candidates/PC12_sl3_metallic_trace_maps/CERTIFICATE_APPENDIX.md
papers/candidates/PC12_sl3_metallic_trace_maps/VALIDATION_BRIEF.md
```

Secondary (computational support):

```text
frontier/B48_sl3_metallic_trace_maps/FINDINGS.md          # trace map, invariant, entropy, splitting, SU(3)
frontier/B49_sl3_certificate_proof_hardening/FINDINGS.md  # splitting proof modules
frontier/B51_sl3_symbolic_m_factorization/FINDINGS.md     # symbolic-m c=3 sector factorization
frontier/B54_general_c_exchange_structure/FINDINGS.md     # [J(m,c),P]=0 on the whole fixed line
frontier/B55_c1_fixed_line_structure/FINDINGS.md          # c=1 sectors, general m
frontier/B57_general_m_splitting/FINDINGS.md              # splitting classification m=1..6
frontier/B59_sl4_factorization/, B60_sln_tower/, B61_sl5_high_precision/  # Appendix A tower
frontier/B62_opposition_involution/                       # opposition-involution identification (Q4)
```

## Reproduction Commands

From the repository root:

```bash
python frontier/B48_sl3_metallic_trace_maps/probe.py
python frontier/B48_sl3_metallic_trace_maps/probe.py --deep
python frontier/B49_sl3_certificate_proof_hardening/probe.py
python frontier/B51_sl3_symbolic_m_factorization/probe.py
python frontier/B55_c1_fixed_line_structure/probe.py
python frontier/B57_general_m_splitting/probe.py
python frontier/B61_sl5_high_precision/probe.py        # Appendix A tower (~3 min)
python -m pytest -q                                     # full suite
```

Expected: full suite `102 passed, 1 skipped`.

## The Mathematics To Check

1. **Trace coordinates and recurrences.** The eight generators `x1..x8` and the
   third-order Cayley-Hamilton recurrences `tau_k, sigma_k` (note Section 2,
   `CERTIFICATE_APPENDIX.md`). Confirm the coordinate convention is standard
   (Lawton's minimal generators) and the recurrences are indexed correctly.

2. **Exchange-sector factorization (note Section 5).** The reversing symmetry
   `P` with `[J(m,c),P]=0`, and the `c=3` sector polynomials

   ```text
   symmetric:     (t-1)(t+1)(t^2-(m^2+2)t+1) = (t-1)(t+1) char(M^2)
   antisymmetric: (t^2+mt-1)(t^2-(m^3+3m)t-1) = char(M^{-1}) char(M^3)
   ```

   for `M=[[m,1],[1,0]]`, proved symbolically for formal `m` (B51/B54).

3. **Splitting criterion + classification (note Section 6).** The palindromic
   quartic `chi(t)=t^4-At^3+Ct^2+At+1`; the criterion `D=A^2-4(C+2)` a square and
   `A+sqrt(D)` even; the integer-splitting list (`c=1,3`; `c=0,3|m`; `c=2,6|m`;
   `c=-1,2|m`; `c=-3,m=2,3`; `c=-9,-11,m=1`); and the proof modules (square-gap
   propagation, finite strips, global exclusions).

4. **Appendix A tower (numerical).** The `m=1` cross-`n` table; whether the
   `char(M^k)` / sign-sector / parity structure is known or derivable.

## Non-Claims To Enforce

Reject any draft wording that implies:

```text
a physical interpretation of the trace map, its coordinates, or its fixed line
the compact SU(3) slice is a gauge theory or particle content
the direct/inverse trace distinction is particle/antiparticle physics
a derivation of units, gauge groups, gravity, spacetime, or observables
a connection to any external research program or foundational claim
the numerical Appendix-A tower is a proven theorem
```

The correct status is: a standalone higher-rank trace-map arithmetic note;
Sections 2-4 standard methods; Section 6 an elementary, apparently-new Diophantine
classification; Appendix A a numerical observation.

## Draft Readiness Checklist

Before PC12 becomes `DRAFTABLE`:

```text
note reads cold for a character-variety / algebraic-dynamics specialist  -- DONE (DRAFT_NOTE.md)
standard blocks (Sec 2-5) stated with citations, not re-proved           -- DONE
Thm-4 splitting proof architecture assembled (criterion + modules)       -- DONE (B49/B57); polished global-exclusion prose still worth writing
literature positioning, with the cross-n tower folded in                 -- DONE (LITERATURE_POSITIONING.md)
reproduction appendix naming exact probes/tests                          -- DONE
independent specialist read of Section 6 + the Appendix-A tower          -- THIS PACKET (pending)
```

## Validation Questions

The five questions a specialist read should answer:

```text
Q1. Is the fixed-line integer-splitting classification (Section 6) genuinely
    absent from the literature, or a special case of a known family?
Q2. Is the fixed-line Jacobian sector factorization (char(M^k) / sign-sector /
    parity, Section 5) a known consequence of the Baake-Grimm-Roberts
    reversing-symmetry framework, or new for this family?
Q3. Is the empirical cross-n tower (Appendix A; n=3,4 complete, n=5 to 22/24)
    known or derivable from Lawton/Procesi SL(n,C) coordinates plus the
    substitution action -- i.e. is there a representation-theoretic reason the
    multipliers are exactly char(M^k) of the metallic companion?
Q4. Is the SL(5) 2-mode residual (fixed-line rank-loss / pseudoinverse
    discontinuity) the expected obstruction? And is the structural identification
    of those 2 modes sound -- namely, that the exchange involution is the
    opposition involution theta=-w0 on the sl(n) root system, whose height-2
    eigenspace split (char(M^2)^2.char(-M^2) for sl(5), reproducing sl(3)/sl(4))
    forces the 2 modes to be a second char(M^2)? (See frontier/B62.) Is the
    symbolic ambient SL(n,C) trace ring the route to a full proof?
Q5. What standard terminology or existing theorem should replace any
    project-specific phrasing that remains?
```

## Outcome Labels

After review, assign exactly one:

```text
DRAFTABLE       = the note and its caveats are sound enough to draft
NEEDS_REVISION  = sound, but presentation or the Section-6 proof needs repair
NEEDS_RESCOPING = a result survives only in a narrower form
KILLED          = a central trace-map, invariant, entropy, or classification claim fails
```

## Current Decision

```text
Prepare PC12 for external mathematical review (character varieties / algebraic
dynamics). Do not merge with physics-facing or foundational material; that
framing is kept out of this note and its packet.
```
