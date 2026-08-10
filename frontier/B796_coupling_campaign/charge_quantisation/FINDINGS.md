# ROW 3 DISCHARGED — charge quantisation follows from B862's ℤ₆, and nobody said so

cc3, 2026-08-10. **Gate 5-Q.** The hypercharge values below are *representation
labels* in the standard normalisation, not measured quantities. No measurement
enters and nothing is compared to data.

## The implication, written down

B862 derives the gauge group as the **quotient** `[SU(3)×SU(2)×U(1)]/ℤ₆`, with
the kernel computed exactly. A representation of the *covering* group descends
to the quotient iff the ℤ₆ generator acts trivially, i.e. iff

```
        t/3  +  d/2  +  Y   ≡   0   (mod 1)
```

with **t** = colour triality (0, 1, 2), **d** = weak duality (0 or 1), **Y** =
hypercharge.

**That congruence is charge quantisation.** In the unquotiented group,
hypercharge is a free real label — nothing forbids a colour-singlet,
weak-singlet with `Y = √2`. Under the quotient, **Y is determined modulo 1 by
the colour and weak representations.** Charges lie on a lattice fixed by (t, d).

## Checked

Every SM multiplet descends:

| multiplet | t | d | Y | t/3 + d/2 + Y |
|---|---|---|---|---|
| Q (3,2) | 1 | 1 | 1/6 | **1** |
| u^c (3̄,1) | 2 | 0 | −2/3 | **0** |
| d^c (3̄,1) | 2 | 0 | 1/3 | **1** |
| L (1,2) | 0 | 1 | −1/2 | **0** |
| e^c (1,1) | 0 | 0 | 1 | **1** |
| ν^c (1,1) | 0 | 0 | 0 | **0** |
| H (1,2) | 0 | 1 | 1/2 | **1** |

**All seven integral.** The SM's matter content is exactly a representation of
the **quotient**, not merely of the cover.

And the controls — fine in the cover, **forbidden** by the quotient:

| a colour/weak singlet with Y = 1/2 | → 1/2 | **FORBIDDEN** |
|---|---|---|
| a colour/weak singlet with Y = 1/3 | → 1/3 | **FORBIDDEN** |
| a quark doublet with Y = 1/3 | → 7/6 | **FORBIDDEN** |

The controls matter: without them the congruence could be a vacuous identity
satisfied by everything. It is not — it **excludes**, which is what makes it a
quantisation condition rather than bookkeeping.

## Why this is worth banking

The Standard Model **does not explain why quark charges are thirds.** It is
among the oldest "why is it like that?" facts in the subject, and the usual
answer is *"embed it in a simple group"* — which is an assumption, not a
derivation, and which leaves the **global form** free.

**B862 derives the global form.** So the programme's answer to charge
quantisation is not "assume SU(5)" but "the descent forces ℤ₆, and ℤ₆ is the
quantisation condition." **That is a stronger route than the standard one**, and
it is one line from a result the programme already has.

## Scope — stated tightly

- **The implication is elementary.** Given the quotient, the congruence is
  immediate; nothing here is deep. **The content is that nobody wrote it down**,
  so a derived consequence of a banked theorem sat unclaimed.
- **It inherits B862's conditionality exactly** — the cascade, and through it
  **P5 menu completeness**, which the content ledger identifies as the single
  most load-bearing unproved thing in the picture. **Charge quantisation is
  therefore DERIVED-GIVEN-P5, not unconditional**, and the ledger row should say
  so.
- **Not claimed:** any hypercharge *normalisation* — B991 proves that is
  impossible for anyone. Only the **relative** quantisation, which is the part
  that is physically meaningful and the part the SM leaves unexplained.

Reproduce: `python3 charge_quantisation.py` (asserts all seven descend and all
three controls fail).
