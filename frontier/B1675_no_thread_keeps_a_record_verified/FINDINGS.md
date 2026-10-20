# B1675 — NO THREAD KEEPS A RECORD, VERIFIED ON MAIN: at the common point no thread, and not the moves together, fixes a private class (a class the puncture cannot detect); only a shear or the mirror does — so a measurer whose record is a fixed state can keep it only at an end (a relational record is not excluded)

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-20. POINT_REGISTER P-197. 0 of 19.
- **What this arc re-banks.** The SM seat's W34, the observer layer on the weave. Its rule (1915fe928) came before its
  script (ddd62c4ee), which came before its output (47a86fa8b), all on 2026-10-08 on the seat's branch. The paper's
  draft 9 cites it in §8 ("no thread keeps a record"), with the owner's question about the measurer (the seat's relay
  §155).
- **How it was verified.** The seat's lock passes. One reading pass for main reproduced the table with its own
  cohomology code (`verification/main_check/v2_w34_independent.py`), without importing the seat's. Main checked the
  report and derived the table's dimensions from Q₈'s characters.

## 0. Seen first

`VERDICT topic-sweep /private state|keeps a record|observer layer|measurer|pointer state/: 6 of 1445 arcs on main match (PROVED 6)`
— chiefly B761 (QP-2, the private states, FLAT), whose quantity this is. **Literature:** the restriction of H¹ of a
cusped hyperbolic 3-manifold to its boundary is injective for these coefficients (Menal-Ferrer and Porti, Osaka J. Math.
49, 2012); pointer states as the states a measuring interaction leaves fixed (Zurek 2003).

## 0b. Disclosed

- **The definition was not in the received statement.** It lives in W34's rule file. Draft 9 now states it: the
  kernel of the restriction H¹(F₂; Sym^{2k}ρ_Q) → H¹ of the puncture, z ↦ z([a, b]), at the quaternion point
  ρ_Q (a ↦ i, b ↦ j).
- **One wording was loose.** The private space at rank three is four-dimensional, not "the three parity lines".
  Draft 9 is corrected.
- **The census's precision.** The seat decided 747 of the 758 states at 60 digits and the other 11 at 120 digits after
  its run. Main's independent census, at double precision, has its smallest non-zero singular value at 0.599, far from
  any degeneracy.

## 1. What holds

| claim | result |
|---|---|
| the blocks at the common point | (dim V, dim H¹, rank to the puncture, private) = (3, 3, 3, 0), (5, 7, 3, 4), (7, 8, 6, 2) for k = 1, 2, 3. This is dim H¹ = dim V + m₀, rank = dim V − m₀, private = 2m₀, with m₀ = 0, 2, 1 the multiplicity of Q₈'s trivial character in Sym^{2k}ρ_Q |
| no thread keeps a private class | **holds** on all 758 states to word length 12 (379 cyclic words, both signs), in every block, and also with the opposite composition order |
| the joint action keeps none | **holds** for L and R together, and with P and −I added |
| a shear or the mirror keeps one | **holds:** at rank three (k = 1, 2), L and R each keep one private class and P keeps two; at rank four, P keeps three |
| why | a thread acts on the private states as its hyperbolic matrix (eigenvalues λ^{±1}, λ > 1) tensored with a map of finite order, so it fixes nothing; a shear is unipotent and fixes one line |

On all of H¹, by contrast, many threads keep a class (718 of 758 in the first block), so the restriction to private
states does the work.

## 2. What it says

- **A fixed record exists only at an end.** A state that its own motion keeps exists only for a shear (a cusp) or
  the mirror, never for a thread or the weave's joint action. This is a statement of the weave, not of one thread.
- **A relational record is not excluded** (the audit lane's reading, 2026-10-20; main agrees). The proposition is about
  fixed vectors. A relation between two changing parts can persist without either being fixed: if x ↦ Ax and
  ℓ ↦ ℓA⁻¹, then ℓx is kept. Whether such a record exists between the private states V and a measurer's states W is
  whether the moves admit a non-zero equivariant map Hom_G(W, V). That is open, and part of the foundations quest
  (P-204).
- **What it buys, and what it does not.** With the composition lemma of draft 9's §8, counting the measurer among the
  threads buys, for magnitudes, the unit and nothing else. It fixes no number. 0 of 19.

## 3. Files

- `verification/received/`: W34's rule, script, output and post-hoc script, copied from the SM seat's branch at
  `ba48b718d`, with `SHA256_RECEIVED.txt`.
- `verification/main_check/`: main's independent census and its run, and the seat's lock run.
- The lock: `tests/test_b1675_no_thread_keeps_a_record_verified.py`.
