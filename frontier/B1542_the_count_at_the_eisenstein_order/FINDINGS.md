# B1542 — THE COUNT AT THE EISENSTEIN ORDER: on the four degree-60 covers of m003 with room 3 and 4, no generic class of any subspace read carries a generation-shaped count; on the room-3 covers I(Λ²W) = −3 at every class while I(W) stays at −1 or above (NEGATIVE, scoped; run as sealed)

cc (the SM-derivation seat), 2026-10-06. **Run as sealed** (`d4a65495`): the banked identity held (`582a555f`), the record was
committed unread (`22fdcb2e`), and `read_out.py` ran once, at 16:01:27Z (`d006130d`). **Verdict, by the seal's §9: NEGATIVE,
scoped to the generic classes of the subspaces read at each cover's trivial character.** Route F, the independent audit the seal
names, returns the run's count at all 192 of its readings before this bank. **Price:** unchanged, 0 of 19.

- **The covers.** The 6-fold cyclic covers of m003's d10.13, d10.16, d10.36 and d10.40 along ψ = ((0, 0), 1/6), the fibre
  direction. They have degree 60, one from each conjugacy class sm:B1540 found:
  - (n(1), n(ρ)) = (3, 3), room 3, on d10.13's and d10.36's;
  - (3, 7), room 4, on d10.16's and d10.40's.
- **The read-out.** P1, P2, P3 and P6 hold; P4 and P5 are False, on complete records: 556 of 556 tasks, 1,664 readings.
  - The transport agrees at every class (P1).
  - Each subspace gives one count across draws, routes and primes (P2).
  - Every identity and cap holds (P3).
  - The class pulled back from m003 reads (1, 0) on every cover, in both routes (P6).
  - No class read is generation-shaped (P4 False), so none reads (−3, −3) (P5 False).
- **The counts** (§2):
  - On the room-3 covers I(Λ²W) = −3 at every class of every stratum and eigenspace, the bottom of Theorem C (i)'s range
    [−n(ρ), 0] (the pulled-back class reads (1, 0)). I(W) is −1 on the interior and on most strata with few free cusps, and 0, 1
    or 2 elsewhere.
  - On the room-4 covers the strata read (0, −5) to (3, −4) and the eigenspaces (±1, −3) and (±1, −2).
- **Why no generation** (§4, from the record's connecting ranks). On the room-3 covers the cup map δ¹_W is zero at the interior
  classes, so Corollary C′ (sm:B1543) allows I(W) down to −4. The count stays at −1 because the dual map's reach into the line's
  interior is zero there as well. On every reading here, as on every banked reading of this frame, I(W) ≥ −b0 (sm:B1543's floor,
  observed and not proved).
- **The audit** (§3). Route F is separate code (numpy and the standard library), on a second presentation of each cover, at
  three other primes. It reads each cover's structure as K2 recorded it and the counts in 7 or 9 subspaces per cover, two draws
  per prime. All 192 readings equal the run's, every one non-zero.
- **The registered prediction held** (§5). It was written after the seal and before the read-out, and amended and qualified
  before it: no (−3, −3) on the four covers. Its clause on rank-7 classes is vacuous: no class reached rank 7.

**0 of 19 stays 0.**

## 1. The run

- **The identity** held in the seat's new container (`identity.json`, `582a555f`): K1–K7 reproduce `controls.json` and every
  sealed hash matches.
- **The run** started at 12:46Z on four workers: 556 tasks, 1,664 readings. Seeds are crc32 of "B1542|cover|route|subspace|draw".
- **Disclosed: two workers were killed by the container's memory limit.** dmesg names pid 7781 at about 14:18Z and pid 7783 at
  about 15:38Z. Their two tasks were lost with no row written, and the pool waited on them.
  - The run was stopped by exact PID at 15:59Z (the launcher first, so that no exit code was written).
  - `run.py`'s own resume then read the two missing tasks on one worker, 15:59–16:01Z, rc 0: the same sealed tasks and seeds.
  - Every task has exactly its readings (550 with three, the four Part C tasks with two). The read-out's coverage check found no
    task missing, doubled or extra.
- **The record** was compressed and hashed before any row was read and committed unread (`run.jsonl.gz`, `run_sha256.txt`,
  `22fdcb2e`). The read-out ran once.

## 2. The read-out

| | prediction | prior | read |
|---|---|---|---|
| P1 | the transport: route R at p_N reads route N's count, k and connecting ranks at every class | 97% | **held** |
| P2 | across primes: one count per subspace on every cover | 90% | **held** |
| P3 | every reading's identities and caps | 97% | **held** |
| P4 | some class read has a generation-shaped count | 25% | **False** |
| P5 | some class read has (−3, −3) | 8% | **False** |
| P6 | the pulled-back class reads one count in both routes | 97% | **held**: (1, 0) on all four |

Four of six held; the priors expected 4.14.

**The counts** (route N; route R's own classes give the same in every subspace):

| cover | (n(1), n(ρ)) | interior (no free cusp) | strata by free cusps | eigenspaces (interior parts) | pulled back |
|---|---|---|---|---|---|
| d10.13, d10.36 | (3, 3) | (−1, −3) | 1: (−1, −3); 2: (−1, −3) or (1, −3); 3: (−1, −3), (0, −3) or (1, −3); 4: (0, −3) or (1, −3); 5: (1, −3); 6: (2, −3) | ζ⁰ (1, −3) ((−1, −3)); ζ³ (2, −3) ((−1, −3)) | (1, 0) |
| d10.16, d10.40 | (3, 7) | (0, −5) | 1: (0, −5); 2: (0, −5) or (2, −5); 3: (3, −5); 4: (3, −4) | ζ⁰ (1, −3) ((−1, −3)); ζ² and ζ⁴ (1, −2) ((1, −2)); ζ³ (1, −2) ((−1, −2)) | (1, 0) |

The conjugate covers d10.14's and d10.38's are not read (they are the same covers of m003 up to conjugacy). Their deck structures
differ from d10.13's and d10.36's, so their eigenspaces are other subspaces of the same H¹ (sm:B1543 §4).

## 3. The audit by route F (before the bank)

`verification/export_f.py` writes the data, and `verification/audit_f.py` reads it with sm:B1541's `route_f.py`, loaded by path.
Route F imports numpy and the standard library only, and checks every item it is given.

- **A second presentation.** ⟨a, t | ttATAAATA⟩ with b = tATA, read on the lifted 2-complex with no Schreier rewriting.
- **Three other primes**: 67108201, 67108081 and 67107241 (p ≡ 1 mod 120, none of the run's).
- **Structure.** h¹(ρ), n(ρ), n(1), the deck group's eigenspaces and their interior parts equal K2's on every cover at every
  prime: (9; 3, 3; 5, 0, 0, 4, 0, 0; 2, 0, 0, 1, 0, 0) and (11; 7, 3; 5, 0, 2, 2, 2, 0; 2, 0, 2, 1, 2, 0).
- **Counts.** The interior, the first cusp's stratum and all cusps; ζ⁰ and ζ³ with their interior parts; on the room-4 covers
  also ζ² and its interior part. The run's ζ² and ζ⁴ are complex conjugate, so route F's ζ² is checked against either.
  - Two draws at each prime: 192 readings.
  - All 192 equal the run's count, and every one is non-zero (the positive control).
- `verification/audit_f.json`, 1,145 s.

## 4. What the record shows about the counts (post-run, from the record's own connecting ranks)

By the identity every reading checks, I(W) = −b0 + k + rk d1(W) − rk d1(W*). Here rk d1(W) = rk δ¹_W is the cup map on the line's
classes. D = rk d1(W*) − k is the dual term: with Theorem C (ii) it equals dim(im δ¹_{W*} ∩ K_L) − dim(⟨c_i⟩ ∩ Λ(V)), the dual
map's reach into the line's interior less the boundary term. So I(W) = −b0 + rk δ¹_W − D. Tallied over the record (route N; every
draw of a subspace gives one value):

| covers | subspaces | rk δ¹_W | D | count |
|---|---|---|---|---|
| room 3 | the interior; strata with 1 free cusp, and some with 2 or 3; ζ⁰'s and ζ³'s interior parts | 0 | 0 | (−1, −3) |
| room 3 | some strata with 3 or 4 free cusps | 1 | 0 | (0, −3) |
| room 3 | some strata with 2 to 4 free cusps; all with 5 | 2 | 0 | (1, −3) |
| room 3 | ζ⁰ | 1 | −1 | (1, −3) |
| room 3 | all six cusps free; ζ³ | 2 | −1 | (2, −3) |
| room 4 | the interior; strata with 1 free cusp, and some with 2 | 3 | 2 | (0, −5) |
| room 4 | the other strata with 2 free cusps | 4 | 1 | (2, −5) |
| room 4 | strata with 3 free cusps; all four free | 5 | 1 | (3, −5); (3, −4) |
| room 4 | ζ², ζ⁴ and their interior parts; ζ³ | 3 | 1 | (1, −2) |
| room 4 | ζ³'s interior part | 2 | 2 | (−1, −2) |
| room 4 | ζ⁰; its interior part | 1; 0 | −1; 0 | (1, −3); (−1, −3) |
| all four | the class pulled back from m003 | 1 | −1 | (1, 0) |

- At the room-3 covers' interior classes the cup map is zero, so Corollary C′ allows I(W) down to −4. The count stays at −1
  because D is zero there: an interior class has no boundary term, and the dual map does not reach the line's interior. Three
  would need D = 2 + rk δ¹_W.
- Across the whole record D never exceeds rk δ¹_W, which is I(W) ≥ −b0. sm:B1543 records the same at all 6,756 banked readings of
  the frame, as an observation, not a theorem.
- The Λ² count on the room-3 covers sits at −3 at every class of every stratum and eigenspace: the 5̄′ side has its three on
  these covers. The 10̄′ side, I(W), is the one that does not follow.

## 5. Against the prediction registered before the read-out

`docs/dossiers/the_line_must_lead_2026-10-06/PREDICTION_FOR_B1542_BEFORE_ITS_READ_OUT.md`: registered at `646a4fc4` (run at task
329), amended at `18b0ac5e` (task 485) and qualified at `c766e9bd` (task 513), all before any row was read.
- "No class read on any of the four covers counts (−3, −3)": **held**.
- "If any count is generation-shaped, it is (−1, −1)", with its amended location: **not tested**, since none is
  generation-shaped.
- "On d10.16's and d10.40's covers, I(W) ≥ 3 at every class of rank 7": **vacuous**. The largest cup rank on those covers is 5,
  where I(W) = 3.
- The stated assumption (generic classes reach the cup map's maximal rank) **failed**, as the caveat warned. The room-3 covers'
  generic classes sit at rank 0 to 2 against a bound of 3. Three still did not come: the dual reach stayed at or below the rank.

## 6. Disclosures

- **The OOM kills and the resume** (§1).
- **A correction this bank owes (ERROR_LEDGER, the correction row of 2026-10-06).** The seal's §6 says a draft sentence, "the
  pieces at ψʲ and ψ⁻ʲ are complex conjugate, so their dimensions agree", was removed because ρ̄ ≅ ρ holds only up to an
  orientation-reversing automorphism. That reason was wrong. The four acts on Hermitian matrices in real coordinates, so its
  matrices are real and ρ̄ = ρ exactly, and complex conjugation carries H¹(N; ψʲ ⊗ ρ) to H¹(N; ψ⁻ʲ ⊗ ρ). The sentence was true.
  Removing it lost nothing, since K2 reads the dimensions directly.
- **The design slips caught before the seal** are the ERROR_LEDGER's draft-slips row: the twist closure (the frame's W at μ is
  a member only when μ⁵ = 1) and the sweep paragraph.
- **The prediction of §5** is not part of the seal. Its priors (P4 25%, P5 8%) stand as sealed.

## Seen first (the repo sweep and the literature)

The full record is the seal's §0.
- **The repo sweep.** `git fetch --all` ran first (2026-10-06, 12:27Z). Then `scripts/checks/prior_work.py` ran over every head
  with twelve terms. The hits that bear are this seat's:
  - sm:B1540, which found the covers and read their supplies;
  - sm:B1541, whose design this arc generalizes from order 5 to order 6;
  - sm:B1536, whose code paths and banked rows it uses;
  - sm:B1535's Theorem C, whose bounds frame the counts;
  - sm:B1378's M₆ triplet, a three-shaped index in an earlier frame, fenced there.
- **After the run.** sm:B1543 (banked the same day, before this bank) reads this record for its corollary and its floor. It changes
  nothing here.
- **The literature.** No source read states counts of this frame. Shapiro's lemma with Mackey at the cusps is sm:B1536's banked
  Lemma S′, and is re-derived on every class read (route N against route R, P1) and by route F, which uses no Shapiro map.
- **Standing: EXTENDS** (sm:B1541's design on covers of a second order).

## Files

- `PREREGISTRATION.md` and `ARTIFACT_HASHES.txt` (the seal); `verification/ncyc.py`, `run.py`, `read_out.py`, `controls.py`,
  `identity.py` (sealed); `verification/controls.json`, `identity.json`.
- `verification/run.jsonl.gz`, `run_sha256.txt` (the record); `verification/read_out.json`, `read_out_log.txt` (the read-out).
- `verification/export_f.py`, `route_f_input_degree60.json`, `audit_f.py`, `audit_f.json` (the audit).
- `tests/test_b1542_the_count_at_the_eisenstein_order.py` (the lock).
