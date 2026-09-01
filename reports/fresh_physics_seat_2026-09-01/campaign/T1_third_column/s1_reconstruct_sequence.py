"""T1 step 1 -- INDEPENDENT reconstruction of the (3,4,1) exact sequence from COMMITTED data.

B1232 fenced "the (3,4,1) sequence itself" as codex's still-running computation. This script
shows the sequence's EXISTENCE AND DIMENSIONS are already derivable from the committed
character ledger -- no in-flight computation needed for that part.

Committed inputs (all cited by file, none re-measured here):
  [M1] frontier/B1212_two_replies/memos/YUKAWA_CUP_PRODUCTS_308.md
       - B = H^1(Y, Lambda^2 V_308) = (33-dim connecting quotient) + (5-dim Serre-dual coker)
       - connecting-quotient raw C12 character multiplicities (2,4,3,3,2,3,2,3,2,3,3,3)
       - C^18 -> C^21 map: kernel chi_10+chi_11 (dim 2) => rank 16, coker dim 5
       - raw coker labels (0,4,6,8,10); Serre-dual tail labels (0,2,4,6,8)
       - determinant linearisation on Lambda^2 V is chi_{-2} (the raw->physical twist)
       - physical total: 3 Reg + chi_0 + chi_11
  [M2] frontier/B1212_two_replies/documents/program-question-map/evidence/YUKAWA_DOWN_RESIDUE_SPEC_308.md
       - selected block: A_7 (3), B_6 = B_6,conn^2 + <bhat_6>, B_2 = B_2,conn^3 + <bhat_2>
       - 36 = 18 conn/conn + 9 tail6/conn + 6 conn/tail2 + 3 tail6/tail2
       - selection rule rho+sigma = 8 mod 12; skew zero on the repeated (4,4) channel
  [R031A] frontier/B1232_.../codex_certs_rerun.txt: "INPUT B = 3 Reg_C12 + chi_0 + chi_11",
       B_0 generator exponents (0,0,0,0), K-rank 4 (B_0 = K^4, P(B_0) = P^3).

CONVENTIONS (stated per E23 discipline):
  * C12 characters chi_r, r in Z/12, chi_r(g) = zeta_12^r on the marked generator of [M1].
  * "raw" labels are the Cech-side labels; "physical" = raw twisted by chi_{-2}
    (the Lambda^2 V determinant linearisation, [M1]) applied ONCE.
  * Serre duality acts on tail labels by phase inversion r -> -r mod 12 ([M1] "inverse phase").
  * The sequence orientation: the connecting quotient is the SUB (image of the connecting
    map), the Serre-dual tail is the QUOTIENT: 0 -> C -> V -> T -> 0.

MB12: every identification below is asserted with a control that would fail under the
wrong convention (wrong twist, wrong duality phase, wrong tail labels).
"""

REG = [3] * 12  # 3 copies of the regular representation, as a multiplicity vector

def add(u, v): return [a + b for a, b in zip(u, v)]
def basis(labels):
    m = [0] * 12
    for r in labels: m[r % 12] += 1
    return m
def twist(m, k):
    """multiplicity vector of (rep tensor chi_k): chi_r -> chi_{r+k}"""
    return [m[(r - k) % 12] for r in range(12)]

# --- [M1] the committed connecting-quotient multiplicities and the 18->21 arithmetic ---
conn = [2, 4, 3, 3, 2, 3, 2, 3, 2, 3, 3, 3]
assert sum(conn) == 33, "connecting quotient must be 33-dimensional"
ker_dim, src, tgt = 2, 18, 21          # kernel = chi_10 + chi_11 ([M1])
rank = src - ker_dim
coker = tgt - rank
assert (rank, coker) == (16, 5), "18->21 arithmetic must give rank 16, coker 5"
print(f"[1] connecting quotient dim 33, raw multiplicities {tuple(conn)}; 18->21 rank {rank}, coker {coker}")

# --- [M1] tail labels: raw coker (0,4,6,8,10); Serre dual = inverse phase ---
raw_coker = [0, 4, 6, 8, 10]
dual_tail = sorted((-r) % 12 for r in raw_coker)
assert dual_tail == [0, 2, 4, 6, 8], "Serre-dual inverse phase must give (0,2,4,6,8) as committed"
print(f"[2] raw coker labels {tuple(raw_coker)} --(Serre inverse phase)--> dual tail {tuple(dual_tail)} : MATCHES [M1]")

# --- the total raw B and the ONE-application twist to physical ---
B_raw = add(conn, basis(dual_tail))
assert sum(B_raw) == 38, "dim B must be 38 = 33 + 5"
assert B_raw == add(REG, basis([1, 2])), "raw total must be 3 Reg + chi_1 + chi_2 as committed"
B_phys = twist(B_raw, -2)  # the chi_{-2} determinant linearisation, applied ONCE
assert B_phys == add(REG, basis([0, 11])), "physical total must be 3 Reg + chi_0 + chi_11"
print("[3] B_raw = 3 Reg + chi_1 + chi_2 ; twist by chi_-2 (ONCE) -> B_phys = 3 Reg + chi_0 + chi_11")
print("    == R031A's committed INPUT line, independently rebuilt from [M1]'s raw ledger.")

# --- THE (3,4,1) SEQUENCE, reconstructed ---
# physical chi_0 = raw chi_2. Count raw-chi_2 dims on each side of 0 -> conn -> B -> tail -> 0:
dim_C = conn[2]                              # connecting part of the raw-chi_2 block
dim_T = dual_tail.count(2)                   # tail part of the raw-chi_2 block
dim_V = B_raw[2]                             # the whole raw-chi_2 block = physical B_0
assert (dim_C, dim_V, dim_T) == (3, 4, 1) and dim_C + dim_T == dim_V
print(f"[4] THE SEQUENCE: 0 -> C -> V -> T -> 0 with dims ({dim_C},{dim_V},{dim_T})")
print("    C = B_2,conn (3-dim connecting part of the raw-chi_2 block)  [sub]")
print("    V = B_0     (4-dim physical-chi_0 Higgs block; P(B_0) = the P^3, K-rank 4 per R031A)")
print("    T = <bhat_2> (1-dim Serre-dual tail slot, raw label 2)        [quotient]")
print("    -> B1232's fenced '(3,4,1) sequence' EXISTS with exactly these dims, from committed data alone.")

# --- the selected 36-entry block and where the connecting sub sits inside it ---
A7, B6c, B6t, B2c, B2t = 3, 2, 1, 3, 1       # [M2]
census = {"conn/conn": A7*B6c*B2c, "tail6/conn": A7*B6t*B2c,
          "conn/tail2": A7*B6c*B2t, "tail6/tail2": A7*B6t*B2t}
assert census == {"conn/conn": 18, "tail6/conn": 9, "conn/tail2": 6, "tail6/tail2": 3}
higgs_conn_entries = census["conn/conn"] + census["tail6/conn"]   # Higgs leg (B_2) in C
higgs_tail_entries = census["conn/tail2"] + census["tail6/tail2"] # Higgs leg (B_2) in the lift of T
assert (higgs_conn_entries, higgs_tail_entries) == (27, 9)
assert 7 + 6 + 2 == 15 and 15 % 12 == 3      # raw character sum = 3 mod 12; chi_-3 in Delta_G [M2]
print(f"[5] census {census}: annihilation of C = vanishing of the {higgs_conn_entries} Higgs-connecting")
print(f"    entries (3 Q-families x 3 dc-families x 3 connecting Higgs directions); the surviving")
print(f"    observable is the {higgs_tail_entries}-entry tail family matrix (= B1232's 'nine-entry tail' block).")

# --- MB12 CONTROLS: each convention choice above has a failing alternative ---
# (a) wrong twist chi_-3 instead of chi_-2 -> physical total would NOT match R031A's input
assert twist(B_raw, -3) != add(REG, basis([0, 11]))
# (b) unapplied duality phase (using raw coker labels directly) -> B_0 would be 3-dim, no (3,4,1)
B_wrong = add(conn, basis(raw_coker))
assert B_wrong[2] == 3 != 4
# (c) double-applied twist -> wrong extras
assert twist(twist(B_raw, -2), -2) != add(REG, basis([0, 11]))
print("[6] CONTROLS BITE: chi_-3 twist FAILS the R031A match; skipping the Serre inverse phase gives")
print("    dim(raw-chi_2 block) = 3 (no (3,4,1)); double twist FAILS. The conventions are forced.")

print("\nS1 VERDICT: the (3,4,1) sequence is RECONSTRUCTED from committed ledger data;")
print("            annihilation of C == vanishing of 27 typed entries; observable = 9-entry tail block.")
