# xB024 ADDENDUM 2 (2026-09-17) — Neumann's CS paper read at source: L194's blocker priced, L223's literature half CLOSED

**Beyond the seal.** `PREREGISTRATION.md` untouched (`9880dc01…`). Continues Addendum 1.

---

## 1. WHAT WAS OBTAINED, AND WHAT WAS NOT

**Obtained and read at source:** W. D. Neumann, *Combinatorics of Triangulations and the
Chern–Simons Invariant for Hyperbolic 3-Manifolds*, Topology '90, de Gruyter (1992) 243–271 —
free as `cspaper.pdf` on Neumann's Columbia page, parsed locally.
**This is the paper the Chern–Simons formula in Snap/SnapPy comes from**, so every `CS` number this
programme has ever computed rests on it, and until now nobody here had opened it.

**NOT obtained. Meyerhoff–Ouyang remains unread after a genuine multi-route attempt.** The routes
tried are named so the next attempt does not repeat them:

| route | result |
|---|---|
| Cambridge Core (the journal) | paywall, abstract only |
| arXiv | not present |
| Neumann's Columbia preprints page | **no eta paper listed** (it has `cspaper.pdf`, `cs2.pdf`, `nrarith.pdf`, `snappaper3.pdf`) |
| EuDML search | interface not fetchable |
| Springer (Meyerhoff–Neumann 1992, CMH) | paywall |
| **empirical substitute: compute `η` ourselves** | **CLOSED — SnapPy exposes only `chern_simons`; there is no `eta` accessor.** `η` lives in Snap, the separate PARI program, not on this bench. |

**Exact citations, taken from CGHN's own bibliography (authoritative, read at source):**
- R. Meyerhoff and W. D. Neumann, *An asymptotic formula for the eta invariants of hyperbolic
  3-manifolds*, **Comment. Math. Helv. 67:1 (1992) 28–46**
- R. Meyerhoff and M. Ouyang, *The η-invariants of cusped hyperbolic 3-manifolds*,
  **Canad. Math. Bull. 40:2 (1997) 204–213**
- M. Ouyang, *A simplicial formula for the η-invariant of hyperbolic 3-manifolds*,
  **Topology 36:2 (1997) 411–421**

**The grade stays UNREAD, and per this register's rule it supports nothing.** Addendum 1's lesson
applies in the other direction too: **a genuine multi-route failure is reportable, a single failed
fetch is not.**

## 2. THE NORMALISATION, PINNED AT SOURCE — L223's LITERATURE HALF CLOSES

**Neumann §1, verbatim:**

> *"All manifolds in this paper are assumed to be oriented. If M is a complete hyperbolic 3-manifold
> which is compact, then its Chern–Simons invariant `CS(M)` is well-defined modulo `2π²`. If M is
> non-compact then Bob Meyerhoff has shown in [M] that there is still a natural definition of
> `CS(M)` which is well-defined modulo `π²`. Let `V(M) = Vol(M) + i·CS(M)`…"*

**CGHN §5A, verbatim:**

> *"There are two commonly used normalizations of Chern–Simons invariant in the literature, related
> by `cs(M) = (1/2π²)·CS(M)`."*

**L223 registered the normalisation as UNPINNED**, naming three candidates: SnapPy's `cs` (mod ½ for
cusped), *"Neumann's `CS = 2π²·cs` (mod `π²`)"*, and a level-normalised `CS/2π`.

> **The record's statement of Neumann's normalisation is EXACTLY RIGHT, and now read at source from
> both ends:** `cs = CS/(2π²)` (CGHN §5A) and cusped `CS` well-defined mod `π²` (Neumann §1),
> which are the same statement as SnapPy's `cs ∈ ℝ/(½)ℤ`.

**L223's LITERATURE half is therefore CLOSED.** What remains open in L223 is **record-internal
bookkeeping** — *which* normalisation enters B1012's `k`-coupling, whose script carries `CS` as a
bare sympy symbol. **That was never a literature question**, and this addendum does not close it.

**Also confirmed at source:** `V(M) = Vol(M) + i·CS(M)` is **Neumann's own definition** of the
complex volume — the object the programme calls `Vol + i·CS` — well-defined mod `2iπ²ℤ` (compact)
or `iπ²ℤ` (cusped).

## 3. THE FORMULA'S OWN AMBIGUITY — RECORDED AS A QUESTION, EXPLICITLY NOT AN IDENTIFICATION

**Neumann §1, verbatim:**

> *"Using a result of Dupont [D] we can find a version of the formula in which this constant is at
> least a rational multiple of `iπ²` (Theorem 1 below). Using a more careful analysis of the
> relevant combinatorics we are able to give a version (Theorem 2) in which the constant is
> conjecturally in `(iπ²/6)ℤ` and is thus determined up to a **six-fold ambiguity**."*

xB015 found a **ℤ/12** index on B1186's family (`24·CS mod 12`). Neumann's Theorem 2 carries a
**conjectural six-fold ambiguity** in the constant.

> **THIS IS RECORDED AS A QUESTION AND IS NOT AN IDENTIFICATION.** Two structures whose labels are
> both small integers, arising in different places, with **no map between them exhibited**, is the
> programme's own most-repeated error class (B813; B1223's *"direct is not semidirect"*; two
> instances in this session alone). **6 and 12 are not claimed to be related.** What is worth a
> later arc is the narrower, checkable question: *does the six-fold ambiguity in Theorem 2's
> constant interact at all with the ℤ/12 index, or are they independent?* **Unanswered here.**

## 4. WHAT THIS CHANGES

- **L223: literature half CLOSED**, bookkeeping half open and still **not a crossing candidate**.
- **L194: unchanged and still open.** Its blocker is now **priced precisely**: Meyerhoff–Ouyang, with
  six named dead routes and **no empirical substitute**, because SnapPy has no `η`.
- **Nothing else.** No value, no new mechanism, no crossing.

**Gate 5 absolute. Nothing to `CLAIMS.md`.**
