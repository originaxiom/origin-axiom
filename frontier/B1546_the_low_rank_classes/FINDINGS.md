# B1546 — THE LOW-RANK CLASSES: SEALED; NO COUNT AT A CLASS OF CUP RANK ONE OR TWO READ. Where can three still live on N₄₅ at the trivial character, and what do the classes of cup rank one and two read?

cc (the SM-derivation seat), 2026-10-06. **Status: SEALED. The run starts after the banked identity holds. This document holds
no outcome of the run.** It states what is proved at design time, what is sealed, what was checked before the run, and how the
run will be read. The verdict, the read-out and the surfaces come at the bank. **Price:** unchanged, 0 of 19.

## Seen first

The repo sweep and the literature are in the seal's §0. Twelve terms over every head (fetched 2026-10-06, 20:15Z):
- "Veronese", "secant variety", "rank-one class" and "square of a class" are absent.
- "persymmetric" occurs only inside "supersymmetric".
- "cup rank" leads to this seat's own cup-map arcs (sm:B1542, sm:B1544), which map no rank locus outside the cup map's
  kernel.

The literature read: Nosaka's twisted triple cup products (arXiv:1808.08532), Monroe's branched bending (arXiv:2604.22004),
and Menal-Ferrer and Porti (arXiv:1001.2242, for the cusp-torus facts). None states the structure of Proposition L. Standing:
NEW-AS-SWEPT for Proposition L on N₄₅ and for Lemma M.

## 1. What is proved at design time (the seal's §3)

- **Where three can live on N₄₅** (Corollary F′ with sm:B1544). A class reading I(W) = −3 has cup rank one or two. It is an
  interior class, or an interior class of cup rank one plus a class of K0(S) for one of the ten sets S of three cusps.
- **Proposition L.** The interior classes of cup rank at most two are, in the deck grading, the classes c of a
  ten-dimensional space Kc0 whose symmetric 4 × 4 matrix S(c) has rank at most two.
  - S is a linear isomorphism of Kc0 onto the symmetric matrices, and rk δ¹_W(c) = rk S(c).
  - So the classes of cup rank one are the squares S(c) = ℓℓᵀ, a 4-dimensional family, and those of rank at most two form a
    7-dimensional one.
  - The ten eigen-lines found first (u_j, w_j, v_a, v_b) are the unit matrices of S: u_j is a diagonal entry, w_j, v_a and
    v_b are off-diagonal pairs.
  - Its checks L0–L3 are exact mod p, in both routes at two primes. They are: the grading of H² is direct; the pencils have
    rank 2 at every y with kernels in K_−j; the image on Kc is 4-dimensional, and its γ-part forces γ = 0 (a Gröbner basis);
    and F is persymmetric after scaling.
- **Lemma G‴.** A family's generic class has the least I(W) on it.
- **Lemma M.** At an interior class of Kc0, I(W) = −1 − μ with μ ≥ 0, a Massey-type boundary rank. The floor holds there iff
  μ = 0, and three there needs μ = 2.

## 2. What is sealed

- `PREREGISTRATION.md` was committed with this document, with its sha-256 in `docs/SEAL_LEDGER.md`, before `run.py` read any
  count at a class of cup rank one or two. `ARTIFACT_HASHES.txt` pins every sealed file.
- **The population** (§5 of the seal), three classes per subspace in each of route F and route R:
  - Z1, the generic square;
  - Z2, the sum of two generic squares;
  - X:S for the ten three-cusp sets, a generic square plus a generic class of K0(S);
  - the ten eigen-lines.
  In all, 22 subspaces, 66 tasks and 132 readings.
- **Predictions** P1–P8 with priors. P5, the floor, has prior 40%. P7, (−3, −3) in both routes, has prior 5%.

## 3. What was checked before the run

Controls K1–K7 hold in both routes (`verification/controls.json`):
- K1, the structure, with Proposition L and Lemma M's input;
- K2, the cochain formula for the cup map;
- K3, the banked counts (4, −10), (−1, −10), (3, −10) and (0, 0);
- K4, the read-out on synthetic rows, thirteen cases;
- K5, the cusps;
- K6, Lemma F at the generic class (5, −5);
- K7, the squares' draw.

Read before the seal: structure only, and counts only at banked classes.

## 4. How the run will be read (the seal's §9)

- **PROVED** if a subspace reads (−3, −3) in two routes with P1–P4. Route F then re-reads it at its next two primes before the
  bank.
- **NEGATIVE** if P1–P4 hold on complete records and every family's generic class reads I(W) ≥ −2. Then no class of N₄₅ reads
  I(W) = −3 at the trivial character, and the golden cover carries no three in this frame there.
- **OPEN** otherwise.
