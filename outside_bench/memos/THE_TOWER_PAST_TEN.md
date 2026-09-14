# Memo 230 — THE TOWER PAST TEN: the index is still zero, and the honest report is how little was actually examined

**Certificate:** `outside_bench/certificates/the_tower_past_ten.py` ·
**Output:** `outside_bench/outputs/the_tower_past_ten.txt` ·
**Seal:** `outside_bench/seals/THE_TOWER_PAST_TEN_PREREG.md`
(sha256 `25048f404d6fffe56a1c79c51239784ffb18ee9aa3b29da08313a8624dcf84fd`, committed first)

**Occasion — the owner: *"go"*.** Memo 229 named the tower past degree 10 as *"the one place the
owner's question still has a computable answer."* This went there.

**CELL 1 = B. C1–C5 pass.**

---

## 1. The result

| degree | covers | in-domain sectors | **nonzero** | ±I discarded | identities discarded |
|---|---|---|---|---|---|
| 11 | 26 | 0 | 0 | 0 | 0 |
| 12 | 62 | 17 | **0** | 14 | 5 |
| 13 | 39 | 0 | 0 | 0 | 0 |
| 14 | 89 | 1 | **0** | 4 | 7 |
| **total** | | **18** | **0** | 18 | 12 |

**Every in-domain sector on the object's own tower past degree 10 returns `I = 0`.**

## 2. And the number that matters more than the null: **18 sectors**

The preregistered population was **47** one-cusped covers with torsion ≥ 3. What actually happened:

* **17 rejected** — the relator does not evaluate to `±I` at tolerance, so the geometric rep is not
  usable as a `PSL` rep there;
* **30 reached** the character loop;
* of those, only the ones carrying a **cusp-trivial character of order > 2** inside the cap produce
  any sector at all — **18 in total**.

> **So this is a null over EIGHTEEN SECTORS, not over forty-seven manifolds, and certainly not over
> "the tower".** The coverage is printed in the certificate rather than implied, because the
> difference between those three statements is the whole value of the run.

## 3. What the seal forbids me from saying

Declared **before** the run, and it binds:

> **There is NO live positive control in characteristic zero anywhere in the record.**
> B1297's own MB12: *"Algebraic non-vacuity shown (random presentations…); **live non-vacuity NOT
> established** (60 census manifolds, 12 sectors, all zero)."*
> B1335's nonzero index is over **`𝔽_p`**, its title reads *"and its **refutation in characteristic
> zero**"*, and its verdict is **NEGATIVE**.

> ### This null is WEAK evidence about the tower and STRONG evidence only about the instrument's standing behaviour. **It is NOT "the tower is vector-like."**
>
> An instrument that has never returned a nonzero on **any** real manifold in characteristic zero,
> returning zero on eighteen more sectors, has told us **almost nothing new about the covers** — and
> that is the honest reading, not a modest one.

## 4. The controls, and what each was for

* **C1 — algebraic non-vacuity, in this run:** random presentations return `I ≠ 0`. **Without this
  the cell would be void**, since a scan by an instrument that cannot fire is not a scan. **PASS.**
* **C2 — the record reproduced:** the same adapted code over census manifolds returns **all-zero
  with the identities holding**, matching the banked result, before being pointed at new ground.
  **PASS.**
* **C3 — B1335's named `±I` trap:** odd `Sym^k` is valid only where the relators evaluate to `+I`;
  B1335 records that the `−I` case *"produced this bench's last false positive."* **18 odd-power
  sectors discarded** on that test.
* **C4 — the four identities:** **12 sectors discarded** for violating them, rather than reported.
* **C5 — the character cap (400/manifold)** is printed with the result, so the population is never
  overstated. Several covers carry torsion of order 199, 720, 1885; their character groups are not
  exhausted and the memo does not pretend otherwise.

## 5. What this changes, honestly

**Memo 229 called the tower past degree 10 "the one place the question still has a computable
answer." That was too strong, and this run is why.** The place is computable, but the *instrument*
pointed at it has no demonstrated live positive in characteristic zero — so a null there cannot
distinguish *"the covers are vector-like"* from *"this index never fires on real manifolds."*

> **The frontier moves rather than closes.** The live question is no longer *"is there a nonzero
> index higher up the tower?"* but **"can this index be made to fire on ANY real manifold in
> characteristic zero at all?"** — which is **B1297's own open item**, stated there and still open,
> and which no amount of scanning higher covers will settle.

**What would settle it:** a live positive anywhere — or a proof that the char-0 vanishing is forced,
which B1335 established **cannot** come from the index identities and domain conditions alone,
since over `𝔽_p` those permit `I ≠ 0`.

*Gate 5 untouched. Nothing promotes. No arc retracted. No physics reading is licensed.*
