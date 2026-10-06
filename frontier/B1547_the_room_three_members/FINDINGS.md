# B1547 — THE ROOM-THREE MEMBERS: SEALED; NO COUNT AT A MEMBER READ. On the golden cover N₄₅, at the characters of order 8 trivial on every cusp whose fourth power has room three, where can three live, and what do those classes read?

cc (the SM-derivation seat), 2026-10-06. **Status: SEALED. The run starts after the banked identity holds. This document holds
no outcome of the run.** It states what is proved at design time, what is sealed, what was checked before the run, and how the
run will be read. The verdict, the read-out and the surfaces come at the bank. **Price:** unchanged, 0 of 19.

## Seen first

The repo sweep and the literature are in the seal's §0. Twelve terms over every head (fetched 2026-10-06, 22:43Z):
- "resonance variet" and "characteristic variet" are absent; "common loops" is only in this arc's own files.
- "golden member" names two other objects (the metallic family's figure-eight, and this seat's order-5 golden-lift
  characters), so this arc's members are called the room-three members.
- "cusp-trivial", "room 3" and "fourth root" lead to this seat's own sm:B1535–B1546, none of which reads a character of N₄₅
  other than the trivial one.

The literature read: Dimca, Papadima and Suciu on cohomology jump loci (arXiv:0902.1250), Menal-Ferrer and Porti
(arXiv:1001.2242) and Nosaka's triple cup products (arXiv:1808.08532). None computes these members. Standing: NEW-AS-SWEPT for
the strata of these members and their counts.

## 1. What is proved at design time (the seal's §3)

- **The room on N₄₅.** The fifteen order-2 characters that are fourth powers of cusp-trivial characters have n = 1 (ten) or
  n = 3 (five, one τ-orbit). By Theorem C, three at a member whose fourth power has order 2 needs ν⁴ among the five.
- **Corollary 1.** At a member trivial on every cusp (b0 = 0, room exactly three), a class reading I(W₁) = −3 lies in the cup
  map's kernel K0^ν and vanishes on at least three of the five cusps (Theorem C (ii) with sm:B1545's Lemma F′). So it lies in
  a stratum X_U = K0^ν ∩ {c vanishes off U}, |U| ≤ 2, with support exactly U.
  - At the trivial character a class off the interior has a ≥ 1 (sm:B1546). Here it need not, because c lies in H¹(N; V ⊗ χ),
    not H¹(N; V). So classes supported on one or two cusps are read too.
- **Lemma G.** Among the classes of support U, a generic class of X_U has the least I(W₁) and the least I(Λ²W₁).
- **Lemma Γ** (Galois-conjugate members read alike, since the four is defined over ℚ(√3)), **the deck symmetry** (the other
  four room-three characters through τ) and **the other order** (through ν̄ = ν⁷).

## 2. What is sealed

- **The seal.** `PREREGISTRATION.md` was committed with this document, with its sha-256 in `docs/SEAL_LEDGER.md`, before
  `run.py` read any count at a member. `ARTIFACT_HASHES.txt` pins the seven sealed files.
- **The population** (§5 of the seal): the 1024 members over χ0, in route R and route F, 2048 tasks. At each member the
  structure, the sixteen strata and the distinct ones, each distinct stratum read at three generic classes; in route R also a
  generic class of K0^ν and one of H¹ (the load-bearing checks).
- **Ten predictions with priors** (§7): P6 (the floor I(W₁) ≥ −2 at every stratum) 80%, P8 (three) 7%, P10 (a
  generation-shaped stratum) 25%.
- **The reading rules** (§9): PROVED if a stratum's generic class reads (−3, −3) in two routes, after the audit at two more
  primes; NEGATIVE if no stratum reads I(W₁) = −3 with I(Λ²W₁) ≤ −3, and then no class at any such member over the five
  room-three characters carries three, in either order; OPEN otherwise.

## 3. What was checked before the run (the seal's §6)

Controls K1–K8 hold, in both routes where they apply: the population named alike, every member trivial on every cusp, τ's
orbit, Lemma Γ's input, the banked count (4, −10) at the trivial character, the strata at eight sample members, the read-out
on twenty-one synthetic cases, route F's basis routine. Structure only was read before the seal; counts only at the trivial
character, where they are banked.

## 4. What is not decided here

Members over the five that are not trivial on every cusp; members with ν⁴ = 1; members whose fourth power has order three or
more; the special classes of a stratum whose generic class reads I(W₁) = −3 with Λ² below −3; other covers; which class and
which cover the genesis selects (GENESIS GAP4, THE_BAR).
