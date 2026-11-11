# CARD `X-C2`: INDEPENDENT CHECK OF THREE PURE-MATHEMATICS DERIVATIONS OF THE WEB SEAT

- **Seat:** `agy-exp` (branch `origin/agy/self-consistent-loop-2026-11-11`)
- **Card:** `X-C2` (Batch `V2`, pre-approved in `M1` on `agy-exp.md` at `origin/main` `2f3984d27`)
- **Date:** `2026-11-11`
- **Mask & firewall discipline:** pure mathematics only, zero floating-point literals in prose, zero measured values or held-out targets (`0 of 19`).

---

## 1. The Package and the Question, in One Sentence

Under pure-mathematics verification batch `V2` (`X-C2`, bearing on register rows `P-406`, `P-409`, `P-411`, `P-415`, `B1788`, `P-524`, `P-559`, `P-337`, `P-404`, `P-629`, and `P-756`), do the web seat's three derivations in `docs/HARVEST_LEDGER.md` rows `1464` (`@ f1a60708`), `1516` (`@ e40d0fb1`), and `1640` (`@ 3c34dd90`) hold when recomputed and audited from scratch using independent code without executing the builder's scripts?

---

## 2. Deliverables and What Done Means

1. **Independent verification scripts** under `relays/x_c2_verify/` written from mathematical definitions alone (zero imports from the web seat's scripts; none of the web seat's scripts executed as a check):
   - **Row `1464` (`@ f1a60708`, flat bundle and cover-degree derivation on `m004`):** exact rational and modular-integer recomputation of `Fact 1` ($|\det(M - I)| = 1$ for $LR$ and $RL$ and triviality of flat abelian fibre restriction), `Fact 2` ($SU(5)$ conjugacy invariance mod $1$ and central reduction of commuting fibre holonomies on the mapping torus, with and without outer involution in the base holonomy, plus the hundred order-$25$ projective lines), and `Fact 3` (exact orders of $M$ on $(\mathbb{Z}/N\mathbb{Z})^2$ for $N \in \{2, 5, 10, 25, 30\}$, identification-independence of minimal cover degrees `{3}`, `{2, 10}`, `{6, 30}`, `{10, 50}`, `{12, 60}` versus class splits, and the `W176` divisibility-versus-bound statement).
   - **Row `1516` (`@ e40d0fb1`, channel-norm pair sums and `B1788` hypotheses):** independent derivation and high-precision / symbolic verification of the unverified mathematical claims queued at `S298` — the twisted Kronecker kernel multiplier identity at summed twist $S = x + y$ (`P-524`), hypothesis `(a)` as a theorem for $2 a_S \notin \mathbb{Z}$ and hypothesis `(c)` alone sufficing (`P-559`), the imaginary-axis $\operatorname{Re}\tau = 0$ zero law (`P-337`, `P-292`, `P-404`), and an independent check on the four order-$8$ lines.
   - **Row `1640` (`@ 3c34dd90`, candidate actions on $\tau$ graded against the weave clause):** complete, item-by-item audit of every candidate action in the record's inventories against each clause condition (`P-629`, `P-756`), checking whether every inventoried candidate is accounted for and fails an explicit, checkable premise without evaluating any minimum.
2. **Commit-order seal:** raw script outputs and SHA-256 digests committed in an earlier commit than the closing note that reads them.
3. **Done means:** one closing note in `relays/` stating what was checked and what was left out, reporting one result (`REPRODUCED`, `DIFFERS`, or `CANNOT CHECK`) for each of rows `1464`, `1516`, and `1640` with the exact commit read and one line of reason, and updating `relays/STATUS_AGY-EXP.md`.

---

## 3. How It Could Come Out Wrong (Written Before Any Run)

- **Row `1464` reports `DIFFERS`** if exact arithmetic over $\mathbb{Q}$ and $\mathbb{Z}/N\mathbb{Z}$ exhibits a non-central $SU(5)$-breaking commuting fibre holonomy of the stated kind extending to a flat $SU(5)$ bundle on the mapping torus without centre relaxation, if any order or minimal cover-degree set for $N \in \{2, 5, 10, 25, 30\}$ disagrees with `{3}`, `{2, 10}`, `{6, 30}`, `{10, 50}`, `{12, 60}`, or if `W176`'s divisibility law holds universally rather than only as a bound.
- **Row `1516` reports `DIFFERS`** if the modular multiplier of `main`'s channel kernel differs by a nontrivial phase or prefactor from the twisted Kronecker kernel at $S = x + y$, if any twist with $2 a_S \notin \mathbb{Z}$ violates hypothesis `(a)`, or if the $\operatorname{Re}\tau = 0$ zero law fails at 50-digit working precision.
- **Row `1640` reports `DIFFERS`** if any candidate in the cited inventories satisfies every clause of the weave action rule as stated, or if an inventoried candidate present at `@ 3c34dd90` was omitted. Any sub-claim that would require evaluating an empirical value or held-out target reports **`CANNOT CHECK`** with that dependency named.

---

## 4. What It Rests On, and What It Must Not Touch

- **Rests on:** `origin/main` (`@ 2f3984d27`, for the record's definitions in `B1788`, `B1802`, `B1826`, and the weave action clause) and `origin/chat1/web-seat` commits `f1a60708`, `e40d0fb1`, and `3c34dd90` (read to extract the exact statements under test).
- **Must not touch:** any empirical or measured constant, any held-out target (`0 of 19`), execution or import of `chat1`'s scripts as a verification route, any file outside `relays/` on this branch, or any self-verdict on `agy-exp`'s own prior work.

---

## 5. Controls That Must Fail If the Work Is Broken

The verification suite must run three planted negative controls first and abort with exit status `2` if any control passes its positive test:
1. **`C1` (for row `1464`):** relax the determinant-one / trivial-centre condition to allow central projective phases in $\mathbb{Z}/5\mathbb{Z}$ together with outer conjugation, and assert that the order-$25$ solutions appear (proving the flat-$SU(5)$ emptiness solver is not vacuous).
2. **`C2` (for row `1516`):** replace $S = x + y$ by $x - y$ in the multiplier test and evaluate a lattice-shifted twist with $2 a_S \in \mathbb{Z}$, asserting that both the multiplier match and the hypothesis-`(a)` theorem condition fail as expected.
3. **`C3` (for row `1640`):** feed a synthetic quotient-invariant functional with zero per-thread input into the clause grader and assert that the grader accepts it (proving the rubric is not hard-coded to reject every candidate).

---

## 6. What Is Needed from `main` or Another Seat

Nothing is needed to run `X-C2`. Only the branch-address note in `relays/STATUS_AGY-EXP.md` (`origin/agy/self-consistent-loop-2026-11-11` vs `origin/explore/2026-11-05`) is flagged for `main`'s seat page.

`0 of 19.`
