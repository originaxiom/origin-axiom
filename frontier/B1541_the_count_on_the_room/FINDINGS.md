# B1541 — THE COUNT ON THE ROOM: on N₄₅, the degree-45 cover of m003 where room for three first appears, no generic class of the 42 subspaces read carries a generation-shaped count of sm:B1515's frame; the generic counts are (4, −10) to (5, −5) on the cusp strata and (0, −5), (−1, −10), (5, −5), (3, −10) on the deck group's eigenspaces, read in two routes and again by an independent third

cc (the SM-derivation seat), 2026-10-06. Sealed at `6815599a` before `run.py` read any count but the pulled-back class's, which
the banked rows fix (`PREREGISTRATION.md`, sha-256 `6a97c7b4…`, in SEAL_LEDGER).
- **The run.**
  - The banked identity held in the seat's new container (2026-10-06, 12:09:54–12:11:01Z): controls K1–K6 were reproduced,
    and the seven sealed hashes matched. `identity.json` is byte-identical to the one banked at `0160100b`.
  - The sealed run then ran from the start, 12:11:16–12:31:19Z on four workers, rc 0: 127 tasks, 380 readings. The first run
    (2026-10-04) was lost unread with the old container (§4).
  - The record was committed unread before the read-out (`0e126a17`; `run.jsonl.gz`, `run_sha256.txt`).
  - `read_out.py --record` ran once, at 12:42:48Z, after both sha-256s were checked (`da576da5`).
- **Verdict: NEGATIVE, scoped** (the seal's §9): P1, P2, P3 and P6 hold and P4 is False on a complete record.
  - Every one of the 127 tasks was read in full. Route R reads route N's class, transported, with the same count, k and
    connecting ranks at every class (P1). Each subspace gives one count across draws, routes and primes (P2). Every identity
    and cap holds (P3). The pulled-back class reads (0, 0) in both routes (P6).
  - **No class read has a generation-shaped count** (P4 False), so none has (−3, −3) (P5 False).
- **The independent audit** (§3; NO NEGATIVE FROM A BUG). Route F re-derived the counts in nine of the subspaces before this
  bank: separate code, a second presentation, three other primes. All 54 of its readings equal the run's, and all are non-zero,
  so its positive control fires on the same code path.
- **As sealed: 4 of 6 predictions held** (P1, P2, P3, P6). The priors expected 4.12. P4 (20%) and P5 (7%) failed.
- **What it is, and what it is not** (§5).
  - It is the first reading of the frame's counts at a cover's own classes where Theorem C leaves room for three.
  - It covers only the generic classes of the 42 subspaces read, at the trivial character of N₄₅.
  - It says nothing about:
    - the special classes inside a subspace (proper closed subsets, where the count can jump);
    - N₄₅'s other characters;
    - other covers with room for three: sm:B1542's four degree-60 covers are running, and sm:B1538's room-three members of
      the silver pair are next.
  **0 of 19 stays 0.**

## 0. What was found

**The generic counts** (I(W), I(Λ²W)) in every subspace read (`verification/read_out.json`; one count per subspace, three
draws, route N at p_N and route R at p_R):

| subspace (dimension of the classes) | count |
|---|---|
| the interior, and every cusp stratum of one or two cusps | (4, −10) |
| every cusp stratum of three cusps | (5, −7) |
| every cusp stratum of four cusps | (5, −6) |
| all of H¹(N₄₅; ρ) (23) | (5, −5) |
| τ's eigenspace for ζ⁰, the classes from d9.2 (3) | (0, −5) |
| its interior part (2) | (−1, −10) |
| τ's eigenspaces for ζ¹, …, ζ⁴ (5 each) | (5, −5) each |
| their interior parts (4 each) | (3, −10) each |
| the class pulled back from m003 | (0, 0) |

- **The pattern.** I(W) is positive on every subspace but the ζ⁰ eigenspace, and I(Λ²W) is negative everywhere but the
  pulled-back class. The two never meet at a common negative value, so no count is generation-shaped. On all of H¹ and on the
  eigenspaces for ζ¹ to ζ⁴ the count is (5, −5), the anomalous shape (k, −k).
- **The cusp strata depend only on how many cusps are left free.** The 32 strata give four values, by |S|: (4, −10) for at
  most two cusps, then (5, −7), (5, −6) and (5, −5). The deck group permutes the five cusps transitively, and the run reads
  every subset.
- **Inside Theorem C's bounds.** I(Λ²W) ∈ [−18, 0] and I(W) ≥ −5 hold at every reading. The most negative I(W) read is −1,
  on the ζ⁰ interior. I(Λ²W) is never above −5 except at the pulled-back class.
- **Route F's supplies** (§3; the same at every prime and draw):

  | subspace | n(W) | n(W*) | n(Λ²W) | n(Λ²W*) |
  |---|---|---|---|---|
  | the interior, and one cusp | 17 | 13 | 8 | 18 |
  | three cusps | 18 | 13 | 11 | 18 |
  | four cusps | 18 | 13 | 12 | 18 |
  | all of H¹ | 18 | 13 | 13 | 18 |
  | ζ⁰ | 18 | 18 | 13 | 18 |
  | ζ⁰ interior | 17 | 18 | 8 | 18 |
  | ζʲ, j ≠ 0 | 19 | 14 | 13 | 18 |
  | ζʲ interior, j ≠ 0 | 17 | 14 | 8 | 18 |

  n(Λ²W*) = 18 = n(ρ) at every class read, so here I(Λ²W) = n(Λ²W) − n(ρ). A count of (−3, −3) would need n(Λ²W) = 15 and
  n(W*) = n(W) + 3. The classes read give n(Λ²W) ≤ 13 and n(W*) ≤ n(W) + 1.

## 1. The run (as sealed)

### 1.1 What was sealed

The seal's §5. N₄₅ is the 5-fold cyclic cover of m003's d9.2 along the order-5 character pulled back from m003's ℤ/5 torsion.
At its trivial character (n(1), n(ρ)) = (4, 18) and room is 5. It reads three generic draws in each of 42 subspaces:
- the 32 cusp strata, by sm:B1536's Part O on N₄₅;
- τ's five eigenspaces and their interior parts.
It also reads the class pulled back from m003. Route N is Shapiro on m003 with the degree-45 permutation module, at
p_N = 16775281. Route R is N₄₅'s own presentation: it reads route N's class transported at p_N, and its own classes at
p_R = 2147482801.

### 1.2 The banked identity and the run

The identity, the run and the read-out are given above. The seed of every class is crc32 of "B1541|route|subspace|draw", so the
repeated run drew the same classes the lost run would have drawn. Its record: 380 readings (127 in route N, 127 in route R's
own, 126 in route R at p_N on the transported class; Part C has no transported reading). The slowest task took 51.3 s.

## 2. The predictions

| | prediction | prior | outcome |
|---|---|---|---|
| P1 | the transport: route R at p_N reads route N's count, k and connecting ranks at every class | 97% | **True** |
| P2 | across primes: one count per subspace, all draws, both routes | 92% | **True** |
| P3 | every reading's identities hold | 97% | **True** |
| P4 | some class read has a generation-shaped count | 20% | **False** |
| P5 | some class read has the count (−3, −3) | 7% | **False** |
| P6 | the pulled-back class reads (0, 0) in both routes | 99% | **True** |

4 of 6 held, against 4.12 expected. The verdict follows the seal's §9 mechanically (`read_out.verdict`).

## 3. The independent audit: route F

NO NEGATIVE FROM A BUG (WORKING_RULES, 2026-10-01) banks a NEGATIVE only after an independent re-derivation with four
properties. Route F (`verification/route_f.py`, driver `audit_f.py`, record `audit_f.json`) has them:
1. **A different method: a second presentation.** b is eliminated from ⟨a, b, t | taTba, tbTbab⟩ by its first relator
   (b = tATA), leaving ⟨a, t | ttATAAATA⟩. The cover is read on that presentation's lifted 2-complex: vertices X, two edges and
   one face per vertex. The four is carried in the base gauge and W's class on its corner. No Schreier tree is used, and no
   rewriting. The cusps come from route F's own Hermite form of each stabiliser lattice in ⟨l, t′⟩.
2. **Separate code.** `route_f.py` imports numpy and the standard library only. It builds the four mod p from the exact
   holonomy entries in Q(ζ₂₄), taking |det g| from the exact norm by its square class. It uses its own elimination mod p.
   Its data (`route_f_input_n45.json`, written by `export_f.py` from the instrument) is checked by route F itself:
   - the four is a representation of the two-generator presentation;
   - b's matrix and its permutation are its word's;
   - the cusp words commute and are unipotent, not 1;
   - τ commutes with the action and has order 5.
3. **A live positive control on the same code path.** All 54 readings return the run's counts exactly, and every one is
   non-zero. Route F also reads N₄₅'s structure: 5 cusps, h¹(ρ) = 23, n(ρ) = 18, n(1) = 4, τ's eigenspaces (3, 5, 5, 5, 5),
   their interior parts (2, 4, 4, 4, 4).
4. **Several primes.** p = 67108201, 67108081 and 67107241, all = 1 mod 120 and none of the run's, two draws each.

The nine subspaces are the interior, the strata of one, three and four cusps, all of H¹, τ's ζ⁰ eigenspace and one other
eigenspace, and their interior parts. Route F's cusps were matched to sm:B1536's order by their point sets. Route F's ζ⁵
labels need not match the run's, but the run read one count on all four non-trivial eigenspaces. The audit ran
12:56:51–12:59:59Z (188 s). It agrees: 54 of 54.

## 4. Disclosures

- **The first run was lost unread.** The seat's container was replaced between 2026-10-04 and 2026-10-06. That run's record
  was uncommitted (about 119 of its 127 tasks), and no row of it had been read. The run was repeated from the start with the
  same seeds, after the identity held again. ERROR_LEDGER records the loss; the record is now committed before any read-out.
- **A rule slip in the seal.** NO NEGATIVE FROM A BUG (2026-10-01) asks a sealed arc to name its independent route in the
  preregistration. This seal (2026-10-04) did not. The route was written after the read-out and before this bank, and it
  re-derives the read-out's counts rather than choosing what to check from them: the nine subspaces cover every kind read and
  every distinct count the read-out has. sm:B1542, sealed after the rule, names its route in its seal.
  ERROR_LEDGER records the slip.
- **Read after the read-out, before this bank:**
  - route F's 54 readings and its structure (§3);
  - the sums of sm:B1536's banked Part P counts over the order-5 cosets of every banked cover's pulled-back characters,
    computed while designing the next arcs: 210 cosets, none generation-shaped. That is a reading of banked data. It is a
    consequence of the golden lift (§5.2), and its record will be banked by the arc that states it.

## 5. What the reading means

### 5.1 Three generations

At the trivial character of N₄₅, the frame's generic counts are not generation-shaped in any of the 42 subspaces. Room 5 is
a cap, and here the counts are nowhere near the line I(W) = I(Λ²W) < 0: I(W) sits at 3 to 5 while I(Λ²W) sits at −5 to −10.
Only the ζ⁰ interior has I(W) < 0, at −1, with I(Λ²W) = −10. Theorem C's room told where three is not excluded. This arc
shows that on N₄₅'s generic classes it is not realized either.

### 5.2 The golden order is where the frame is closed under twisting

The frame's W at a member ν is [[ν ⊗ ρ, c·ν⁻⁴], [0, ν⁻⁴]] (sm:B1536 §2). Twisting the trivial character's W_c by a character μ
gives the frame's W at the member μ exactly when μ⁵ = 1. So on a 5-fold cyclic cover along a character of order 5, a class
pulled back from below has the count Σ_j count(ν₀ μʲ) of the five members below: Shapiro with Mackey at the cusps, as in the
seal's Proposition P. This is the **golden lift**. It is why the pulled-back class reads (0, 0) here: d9.2's five members
read (0, 0). By the same argument, the ζ⁰ eigenspace's generic counts are the sums of d9.2's generic counts at its five
members; that sum is not read here. At any other order the twisted pieces leave the frame (sm:B1542's seal, §3).

### 5.3 Where three could still be

- **Special classes** of each subspace, where the connecting ranks drop. Lemma G makes the generic count one value per
  subspace, not one value per class.
- **N₄₅'s other characters.**
- **The other room covers.** sm:B1542 reads the four degree-60 covers (room 3 and 4) now. sm:B1538's 1,856 room-three members
  on the silver pair's degree-8 covers are next.

## 6. Prior work and standing

**Standing: EXTENDS** (the seal's §0). sm:B1536's Part O and the deck group's eigenspaces are read on a cover with room above
two, and the counts there are re-derived by an independent route. No source read states counts of this frame.

## 7. What this arc does not decide

- The special classes inside each subspace, and subspaces other than the 42 read.
- N₄₅'s other characters, and other covers with room for three.
- Which class, and which cover, the genesis selects (GENESIS GAP4, THE_BAR).

## Seen first (the repo sweep and the literature)

The full record is the seal's §0.
- **The repo sweep.** `git fetch --all` ran first (2026-10-04, 16:00Z). Then `scripts/checks/prior_work.py` ran over every
  head with twelve terms. N₄₅ appeared only in this seat's golden covers dossier. The hits that bear:
  - sm:B1536, whose code paths and banked rows this arc uses;
  - sm:B1535's Theorem C, whose bounds frame the counts.
- **The literature.** No source read states counts of this frame. Shapiro's lemma with Mackey at the cusps is used as
  sm:B1536's banked Lemma S′; route F re-derives the counts without it, on the cover's own complex.
- **Standing: EXTENDS.**

## Files

- `PREREGISTRATION.md`, `ARTIFACT_HASHES.txt`: the seal.
- `verification/n45.py`, `run.py`, `read_out.py`, `controls.py`, `identity.py`; `controls.json`, `identity.json`: the sealed
  instruments and their records.
- `verification/run.jsonl.gz`, `run_sha256.txt`: the run's record (380 readings).
- `verification/read_out.json`, `read_out_log.txt`: the read-out, once.
- `verification/route_f.py`, `export_f.py`, `audit_f.py`; `route_f_input_n45.json`, `audit_f.json`: the independent audit.
- `tests/test_b1541_the_count_on_the_room.py`: the lock.
