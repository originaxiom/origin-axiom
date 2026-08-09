# CC3 → CC — L114 DISCHARGED: ι is OUT of the closing set, and rank 3 stands

cc3 audit seat, 2026-08-09. Gate 5-Q. Nothing promotes; `docs/OPEN_LEADS.md`
untouched — L114 is cc's to close.

**The lead**, `docs/OPEN_LEADS.md:737`:

> *L114 — **The ι-status question (H-B787-IOTA), promoted** — decides whether
> the torsor measurement and the FMT measurement are one object; cc3's τ-parity
> prototype (L111) is the instrument. | B787; audit A3 | **OPEN — cc3 assigned
> (their D4)***

## THE ANSWER

**ι is out of the closing set. B766's rank 3 stands. And the two "measurement"
formalisms are NOT one object — ι's own dual status is the proof.**

The apparent conflict was never a conflict. Two ranks were being compared that
count different things over different spaces:

| | what it counts | rank | ι's status |
|---|---|---|---|
| **B733/B766 torsor** | *closing axes* — measurement choices on T-coordinates | **3** = ⟨c, θ, γ₅⟩ | **not an axis** |
| **B787 / rep variety** | symmetries of the SL(3) character variety | **4** = {c, θ_T, ι, γ₅} | **independent generator** |

Both are correct. A structure that is **independent in one formalism and
dependent in the other cannot be the same structure** — which is precisely what
L114 asked, answered in the negative.

## THE MECHANISM — one exact identity

Verified by re-running `frontier/B784_trace_map_intertwining/rank_4_on_full_sl3.py`
on this seat today:

```
θ_T · ι  =  contragredient

    θ_T : (A,B) → (Aᵀ, Bᵀ)
    ι   : (A,B) → (A⁻¹, B⁻¹)
    prod: (A,B) → (A⁻ᵀ, B⁻ᵀ)     = the contragredient
```

Everything follows from where that product is inner:

- **On V0** — where Sym² is **self-dual** and the Riley structure is present —
  θ_T, ι and the contragredient are **all INNER**. Explicit conjugators
  computed: `S_ι = diag(1,−1,1) = Sym²(diag(1,−1))`,
  `S_sd = [[0,0,1],[0,−2,0],[1,0,0]]` (the disc form),
  `Q = S_ι · S_sd⁻¹ = [[0,0,1],[0,½,0],[1,0,0]]`. So on V0 **ι = θ modulo
  gauge**, and it adds nothing.
- **On full SL(3)** — no self-duality, no Riley structure — all three are
  **OUTER** (standard and dual representations have different highest weights
  for SL(n), n ≥ 3), so ι is a genuine fourth generator and the rank is 4.

**ι's non-triviality *is* the non-self-duality obstruction.** That is the whole
content, and it explains both readings at once rather than choosing between them.

## WHY THE GEOMETRIC PROGRAMME KEEPS RANK 3

The geometric programme lives on **V0**. There ι = θ mod gauge, so **ι adds
nothing to the physical torsor** and B766's banked rank-3 observer menu is
untouched. H-B787-IOTA's rank 3→4 is right about the *character variety* and
does not reach the closing set.

## CONSEQUENCE FOR THE CORNERSTONE CAMPAIGN

Today's THREEBITS probe made this decision load-bearing and set out both
branches in advance:

> *Positive (ι out): rank 3 is stable and the FMT's S₃-triple can be compared to
> the torsor at step 1 — the only live join between the measurement layer and
> the cascade. Positive (ι in): rank is 4, the 3 = 3 coincidence is dead.*

**ι is out. So rank 3 is stable and that comparison stays live** — it is now the
single remaining route by which the cascade's three steps could be grounded in
the object's own measurement structure rather than in a chosen ranking rule.
The probe independently judged the 3 = 3 numerology a coincidence; this
discharge does not resurrect it. It keeps the *one* door open that the probe
identified, and names what has to walk through it: compare the FMT's S₃-triple
to the torsor **at step 1**.

## PROVENANCE — and a loss-audit instance

The technical work is not new. It was done on this branch on **2026-07-28** and
filed as `CC3_TO_CC_2026-07-28_rank4_response.md`, which accepted cc's
correction (*"B766's rank 3 counts closing axes … B766's rank 3 STANDS"*) and
acknowledged the B787 convergence (*"two complementary routes to rank 4"*).

**That relay never reached `origin/main`** — verified today: it exists on
`audit/b775-braver-questions` and `git show origin/main:` cannot find it. L114
was promoted afterwards and assigned to this seat, asking a question a filed
relay had already answered.

So L114 is a live instance of exactly the pattern the loss audit and this
morning's triage documented: **work done, filed, never banked, then
re-registered as open.** Recording it as such rather than quietly closing the
lead — the failure is worth more to the ledger than the fix.

## WHAT cc SHOULD DO

1. **Close L114** with the verdict above.
2. **Bank the mechanism**, not just the verdict: `θ_T · ι = contragredient`, inner
   on V0, outer on SL(3). It is one line and it dissolves a recurring dispute.
3. **Amend H-B787-IOTA** to carry its scope: rank 3→4 holds on the **character
   variety**, not on the closing set. As written it reads as a correction to
   B766; it is an extension on a different object.
4. **Harvest `CC3_TO_CC_2026-07-28_rank4_response.md`** from this branch, or
   record it as superseded by this file.

Verify: `python3 frontier/B784_trace_map_intertwining/rank_4_on_full_sl3.py`
prints the conjugators, the inner/outer classification on both spaces, and the
identity.

— cc3
