# MEMO 171 — THE σ BRIDGE COMPARES TWO DIFFERENT QUANTITIES, AND SIX CUSPS WERE NEVER THE REQUIREMENT

**Banked 2026-09-07 · outside bench (lane 1B).** Owner: *"what do you need to solve σ once forever?
craft a plan and execute it."* Executed: **the literature search memo 169 identified and nobody had
done.** Gate 5 untouched — no measured value anywhere. **Nothing here claims σ = 1.**

---

## 1. WHAT THE LITERATURE SAYS, AND IT IS THE OBJECT GC-6 SAID WAS MISSING

`B1191`/GC-12 closed the fingerprint route with: *"the bridge's remaining object is EXACTLY typed: **a
genuine boundary character no banked artifact supplies.**"* Memo 169 then measured the gap that
matters: **`Ẑ`, `GPPV`, `false theta`, `logarithmic VOA`, `half-index`, `homological block` — zero
occurrences across all 1122 arcs and every doc.**

**Searched, and the object exists:**

1. **`Ẑ`-invariants ARE the characters of logarithmic vertex operator algebras.** That is the
   boundary character, and it is standard.
2. **Its effective central charge is read off Cardy-like coefficient growth:**
   `a_n ~ exp(2π√(c_eff·n/6))`.
3. **And the relation that matters:** `c_eff = c − 24·min(h_i)` — the effective and the **Virasoro**
   central charge **differ by the minimal conformal weight**, and coincide only when `h_min = 0`,
   i.e. **only for unitary theories.**
4. **`F_K`, the knot-complement analogue of `Ẑ`, is explicit for the figure-eight** — our knot — is
   annihilated by the **quantum A-polynomial**, and satisfies
   `lim_{q→1} F_K(x,q) = (x^{1/2} − x^{−1/2})/Δ_K(x)`.

---

## 2. THE TYPE ERROR, LOCATED ON A SPECIFIC LINE

GC-6's headline is *"`c = 6` is SIX cusp-boson units; the banked `T[4₁]` (one cusp) supplies **ONE**."*
**Read its script**, `frontier/B1190_close_loop_batch2/verification/gc6_l154_bridge.py`:

```python
# Cardy growth estimator: c_eff(n) = 6 n (log a_{n+1} - log a_n)^2 / pi^2
def c_eff_series(coeffs, skip=4): ...
P1 = [0]*(NMAX+1); P1[0] = 1            # eta^-1 coefficients = p(n)
ce6 = c_eff_series(chi0)                #  (E6)_1 vacuum character -> 6
cu1 = c_eff_series(P1)                  #  u(1) free boson        -> 1
```

> **The estimator is run on `(E₆)₁` and on `η⁻¹`. It is NEVER run on the object.**

**The "ONE" is the `c_eff` of `η⁻¹` — a free boson — used as a MODEL for the object's cusp.** GC-6's
own caveat concedes it: *"The 3d index of `T[m004]` was **NOT computed**."*

**Why that is a kind error and not a shortcut.** A free boson is **unitary**: `h_min = 0`, so
`c_eff = c = 1` and the distinction is invisible. **A `Ẑ`/`F_K` boundary character is logarithmic —
non-unitary by construction — where `c_eff ≠ c`.** So the comparison runs:

| side | quantity actually used | type |
|---|---|---|
| target `(E₆)₁` | `c = 78/13 = 6` | **Virasoro** central charge |
| "object" | `c_eff(η⁻¹) = 1` | **effective** charge of a **unitary substitute** |

**Two different quantities, on two different objects, compared as if one number.** This is precisely
`B1231`'s named dominant failure mode: *two structures whose labels match, in different places,
joined without a map.*

---

## 3. WHAT THE REQUIREMENT ACTUALLY IS

Not six cusps. The condition is on the **true boundary character** of the object:

> **`c = c_eff + 24·h_min = 6`.**

**If** the object's boundary character has `c_eff = 1`, this needs **`h_min = 5/24`** — an exact,
checkable rational, in place of a topological count. **`5/24` does not appear anywhere in the corpus
in this role** (its five hits are unrelated).

---

## 4. THIS DISSOLVES MY OWN NEGATIVE FROM THIS MORNING

`certificates/six_cusp_reachability.py` proved **no cover of m004 to degree 12 has six cusps** (max 5,
at degree 10; control reproduces `B1295`'s 87 covers / 201 cusps exactly). I reported that as closing
the route.

**It closes nothing, because six cusps were never the requirement.** The count came from substituting
a unitary free boson for a logarithmic boundary character. **The negative stands as a fact about
covers and is void as an argument about σ.** Recorded against myself: I ran a correct computation
against a requirement I had not audited.

---

## 5. WHAT REMAINS — a finite computation, not a theorem that does not exist

The corpus's own words for L154 were *"a theorem that does not exist."* **It is now a computation:**

1. **Obtain `F_K(4₁)`** as an explicit `q`-series. The literature computes it to any order, and the
   **corpus already holds the A-polynomial** (`B67`, with the Newton-polygon data re-derived at
   `B1201`); `F_K` is annihilated by its quantum version.
2. **Run GC-6's own estimator on it** — the same `c_eff_series` function, now on the object rather
   than on a substitute.
3. **Extract `h_min`** from the leading exponent and form `c = c_eff + 24·h_min`.
4. **Test `c = 6`.** Either it lands — and σ = 1 with the last continuous input converting to an
   output — or it does not, and σ is an anchor with a *reason* instead of a missing bridge.

**Step 1 is the only one needing anything outside this bench**, and it is retrieval, not invention.

---

## 6. WHAT THIS DOES NOT CLAIM — read before quoting any of it

- **σ is not solved and nothing says `σ = 1`.** The bridge's arithmetic requirement has been
  **re-typed**, not met.
- **The object's boundary character is not exhibited here.** Whether `T[m004]` even *has* an
  `F_K`/`Ẑ` in the relevant sense is exactly what `Q11` asks Dimofte, and is not settled by finding
  the general theory.
- `B1064`'s O3 **stands**: `CS = 0` still deletes the quantized sector, and nothing above touches it.
  **A re-typed count does not restore a deleted attachment** — these are two separate blockers and
  only the first has moved.
- `h_min = 5/24` is **conditional** on `c_eff = 1` for the true character, which is itself the
  unverified free-boson inheritance. If the real `c_eff` differs, the target moves with it.
- The literature above is **read from search results, not from the papers themselves** — arxiv.org is
  blocked from this machine. **Grade: CITED/UNVERIFIED**, and the relations should be checked against
  primary sources before anything is built on them.
