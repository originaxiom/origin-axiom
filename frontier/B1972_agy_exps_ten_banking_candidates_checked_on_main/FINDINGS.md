# B1972 — agy-exp's ten banking candidates, checked on main: the mathematics holds, with corrections; none of the record-level claims (I-37 earned, SE1–SE3, GM1–GM4 and Postulate D retired, B1970's two gates closed, a 2.0-bit floor) follows from it

**Verdict: PROVED** for the checks below.
- Main's own computations (`verification/bank1_topology.py`, `bank_math.py`) confirm every pure-mathematics core it tested, and correct three statements.
- The seat's sixteen sealed scripts were run in a sandbox, under the author's ruling of 2026-11-24. The outputs are in § 2.
- On the record-level claims, the verdict is **NOT EARNED / NOT RETIRED / NOT CLOSED**, for the reasons in § 3.

Main, 2026-11-24, at the author's word: verify BANK-1 to BANK-10 cold, strictly 0 of 19, and bank what verifies. Source:
`relays/AGY_EXP_TO_MAIN_2026-11-24_MASTER_LOAD_BEARING_SYNTHESIS_PEER_VERIFICATION_AND_BANKING_REQUEST.md` on
`origin/agy/self-consistent-loop-2026-11-11` at `9b34bfc03`, read in full by main at source. Data-free: nothing is compared, and
none of the seat's printed flavour numbers is read against anything. **0 of 19.**

**Review 86 corrections (2026-11-24; cold readers' findings, each checked by main; docs/progress/REVIEWS.md, B1975):**
- **BANK-3's checks are identities by construction.** n₁ is defined so that H − V + 29T = 273, and the F⁴ coefficients are typed in. They confirm no anomaly fact, only the selection n₁₆ ∈ {0, 2} by the three criteria.
- **BANK-1 (4)'s uniqueness is among two-node deletions,** as the seat states it.
- **The 3-cusp cover's monodromy group, D5,** is inferred from B1955 and the cover counts. It is not printed.
- **K6:** the coordinate predicate a = b does the selecting. F-C30-03 is about the agy lane's word choice in C30, a related construction.
- **BANK-5: "prefers (3,0,2) because it hits all 3" is withdrawn.** The relay evaluates (3,0,2) as the equivariant branch against agy-002's non-equivariant (3,2,0), and it prices the choice between the two equivariant branches as R1 = 1 bit. The fair point is only that one of the two branches was evaluated against the intervals.
- **The seat's −P₅ sentence contradicts itself.** diag(+1,+1,+1,−1,−1) has a +1 space of dimension 3 on 5, so 6 on 5 + 5̄.
- **The reproduction lock was circular.** It now asserts 16 of 16.

## Seen first

- **Swept:** `VERDICT topic-sweep /Gieseking|m000|8\^3_4|dihedral cover|Kawamura|doublet.triplet|Morrison.Vafa|Hirzebruch|bedrock|input floor|I-37|Postulate D/: 36 of 1713 arcs on main match (NEGATIVE 3, OPEN 4, PROVED 29); 13 register rows match (DONE 7, QUEUED 6)`.
  The matches that bear on the claims are those listed below (GENESIS's SE and GM rows, P-866 and B1955, B1943, B1659,
  B1739, I-37's row); the rest were read by title.
- **The seats' relays to main on these problems.** Read 2026-11-24, before this arc, by four read-only readers whose reports main read in full; harvest rows 1993 to 1996:
  - agy-exp: 14 relays since 2026-11-15, including LINK4, LINK8, R-3S-FINAL and the review of the agy lane's C1 to C24;
  - the agy lane: 20;
  - agy-002: 8;
  - the web seat: 8.
- **The record:**
  - GENESIS SE1 already lists "minimal volume selects m000", and SE2 is "the orientation double cover of m000" (CHOSEN).
  - P-866 and B1955 (2026-11-17) hold the knot's dihedral cover at p = 5, its determinant: three boundary components, branching (1, 2, 2) (Perko; Burde), the link 8³₄.
  - B1943 fixes the act's line of order 5, (1/5, 2/5).
  - B1659 and B1739 give the single point's rank 2 (R null, Jacobi).
  - SM-C13 (harvest row 1808) gives the lepton–down copy on E[5].
  - I-37's row states what would earn it.
- **The literature:**
  - the Gieseking manifold is the smallest-volume cusped hyperbolic 3-manifold, and the figure-eight complement double covers it (Adams 1987);
  - Cao–Meyerhoff (2001) concerns orientable manifolds;
  - the smallest cusped orbifolds are far smaller (Meyerhoff 1985);
  - dihedral quotients of knot groups (Fox);
  - centralizers in so(10) and the orbifold doublet–triplet projection (Kawamura 2001);
  - 6D anomaly cancellation on Hirzebruch bases (Morrison–Vafa; Kumar–Morrison–Taylor).
  - Nothing in BANK-1 to BANK-3's mathematics is new as mathematics.

## 1. Main's own checks (no seat code)

| item | the seat's statement | main's computation | result |
|---|---|---|---|
| BANK-1 (1) | m000 → m004 is the unique index-2 subgroup | SnapPy: m000 non-orientable, volume 1.01494, H₁ = ℤ; its one 2-fold cover is orientable with H₁ = ℤ and isometric to m004 | holds (classical) |
| BANK-1 (1) | m000 is "the Cao–Meyerhoff minimal-volume non-compact orbifold" | m000 is the Gieseking manifold, the smallest cusped hyperbolic 3-*manifold* (Adams). Cao–Meyerhoff is about orientable manifolds, and cusped orbifolds go far lower | **corrected** |
| BANK-1 (2) | no non-abelian quotient of order < 10; D5 unique at 10 | brute force over S₃, S₄, S₅: non-abelian images of orders 10 (D5), 12 (A4) and 120 only; none of order 6 or 8 (abelianization ℤ rules out D4 and Q8) | holds (classical: determinant 5) |
| BANK-1 (3) | the index-10 kernel gives H₁ = ℤ³ and cusps 1 + 2 + 2 = 3, and is 8³₄ | SnapPy: the regular 10-fold (D5) cover has **5 cusps and H₁ = ℤ⁵**; the 3-cusp cover is the **irregular 5-fold** one, isometric to 8³₄ (volume 10.1494, H₁ = ℤ³) | the identification holds for the 5-fold cover and is **already on main's record** (P-866, B1955); the stated kernel is **corrected** |
| BANK-1 (4) | Kac order 8 on affine E8: unique least Cartan determinant 20 = 4·5 | the deletions with mark sum 8 have determinants 20, 24, 30, 32, 48; the least, 20, is unique (SU(5) × SU(4)) | holds; why the order is 8 is the premise |
| BANK-2 (1) | Cent(P₁₀) = so(6)⊕so(4), Cent(J₁₀) = u(5), joint 13 | [P, J] = 0; dimensions 21, 25 and 13 | holds (textbook) |
| BANK-2 (2) | −P₅ keeps solely (H_u, H_d), "zero ad-hoc Kawamura flags" | on 5 + 5̄, P₅ = diag(−1,−1,−1,+1,+1) has a +1 space of dimension 4 (the doublets); the relay's −P₅ has a +1 space of dimension 6 (the triplets) | the projection holds for one sign; **which sign is the parity is the Kawamura choice** the card says it avoids |
| BANK-3 (1, 2) | H − V + 29T = 273 on all 11 bases; ṽ = (4 − n₁₆)/2; the three criteria leave n₁₆ ∈ {0, 2} | the arithmetic holds; the F⁴ term cancels when a 16-hyper counts as 16 + 1̄6̄; ṽ integer, ≥ 0 and ≠ 0 leaves n₁₆ ∈ {0, 2} | holds inside 6D F-theory; the three criteria are choices of physics |
| BANK-4 (3) | K5 = ⟨(1/5, 2/5)⟩ is the unique M_RL-invariant order-5 subgroup | char poly ≡ (λ+1)² mod 5, a single Jordan block, one invariant line (1, 2) | holds for the fixed word M = [[2,1],[1,1]]; it is the record's act line (B1943). The seat's own R-3S-FINAL F-C30-03 shows the kernel changes with the word |
| BANK-4 (3) | K6 = ⟨(1/6, 1/6)⟩ is unique, 0 bits | 12 cyclic order-6 subgroups; 1 contains (1, 1); 4 contain (1/2, 1/2) | unique only under the coordinate predicate a = b. F-C30-03 records that the word T⁴S was adopted "solely to recover (1/6, 1/6)". **Not 0 bits** |
| BANK-4 (3) | τ₀⁺ = (2+i)/5 with j = 1728; τ₈⁺ = 8τ₀⁺ | γ = [[1,0],[2,1]] maps i to (2+i)/5, so j = 1728 is automatic | holds; the factor 8 is BANK-1's Kac premise |

## 2. The seat's sixteen scripts, reproduced in a sandbox

- **Setup:**
  - a sparse shared clone of the seat's branch at `9b34bfc03`, holding `relays/` only;
  - each producer and referee run with `python3 -I` (`verification/reproduce_one.sh`);
  - the output's SHA-256 compared with the committed output.
- **Before running:**
  - the modules are the standard library, mpmath and sympy only;
  - the only subprocess calls are read-only git commands (show, ls-tree, log);
  - each script writes one output file next to itself.
- A reproduction is the seat's computation run again. It is **not** a verification (WORKING_RULES, the rule of 2026-11-24).

| card | script folder | seconds | committed output | rerun output | result |
|---|---|---|---|---|---|
| R-PEER-AUDIT-ALL-SEATS | `r_peer_audit_all_seats_referee` | 41 | `6f2a028e6a48a9dc` | `6f2a028e6a48a9dc` | byte-identical |
| R-PEER-AUDIT-ALL-SEATS | `r_peer_audit_all_seats_verify` | 47 | `5270258bbbcdfa5a` | `5270258bbbcdfa5a` | byte-identical |
| X-BULK-LINK1 | `x_bulk_link1_referee_v3` | 399 | `9890a77ccd2a68fe` | `9890a77ccd2a68fe` | byte-identical |
| X-BULK-LINK1 | `x_bulk_link1_v4_verify` | 123 | `40be4dfb523c6d77` | `40be4dfb523c6d77` | byte-identical |
| X-E6PS-LINK23 | `x_e6ps_link23_referee` | 10 | `eb8c2efd051d0f0c` | `eb8c2efd051d0f0c` | byte-identical |
| X-E6PS-LINK23 | `x_e6ps_link23_v2_verify` | 11 | `f40069d3e879b246` | `f40069d3e879b246` | byte-identical |
| X-FLAVOR-LINK4 | `x_flavor_link4_referee_v2` | 314 | `aa985e7e7fe72e92` | `aa985e7e7fe72e92` | byte-identical |
| X-FLAVOR-LINK4 | `x_flavor_link4_v5_verify` | 255 | `305c0e98bf6f891e` | `305c0e98bf6f891e` | byte-identical |
| X-FLOOR-LINK8 | `x_floor_link8_referee` | 27 | `7c63850099b4a57b` | `7c63850099b4a57b` | byte-identical |
| X-FLOOR-LINK8 | `x_floor_link8_verify` | 118 | `33ca5c7022834bf0` | `33ca5c7022834bf0` | byte-identical |
| X-FOUNDATIONS-LINK7 | `x_foundations_link7_referee` | 36 | `9fbae20509c2a817` | `9fbae20509c2a817` | byte-identical |
| X-FOUNDATIONS-LINK7 | `x_foundations_link7_verify` | 28 | `1e295fd21dfa51f5` | `1e295fd21dfa51f5` | byte-identical |
| X-F-THEORY-FLAVOR-LINK5 | `x_ftheory_flavor_link5_referee_v2` | 646 | `4baeb111d0993fd9` | `4baeb111d0993fd9` | byte-identical |
| X-F-THEORY-FLAVOR-LINK5 | `x_ftheory_flavor_link5_v4_verify` | 720 | `51a2fb04e7e9d03e` | `51a2fb04e7e9d03e` | byte-identical |
| X-HIERARCHY-LINK6 | `x_hierarchy_link6_referee` | 260 | `a79f28836f23a323` | `a79f28836f23a323` | byte-identical |
| X-HIERARCHY-LINK6 | `x_hierarchy_link6_verify` | 89 | `8780abc6c4e388cf` | `8780abc6c4e388cf` | byte-identical |

**All sixteen reproduce byte for byte** (`verification/reproduce_run.txt`). This shows the seat's outputs are what its sealed
scripts compute. It says nothing about whether the scripts compute the right thing; § 1 and § 3 address that.


## 3. The record-level claims

| claim | what the record requires | main's finding |
|---|---|---|
| **BANK-2 earns I-37** | I-37's row: the frame's Higgs triplet S(τ) shown to be the 10's doublet pair within the dictionary (given Λ), holomorphy derived, then a prediction | BANK-2 works inside an imported Hořava–Witten E8 boundary. It identifies 8³₄'s meridian reflection with P₁₀ and chooses the sign that keeps the doublets. It never connects frame C's triplet S(τ) to the doublets, derives no holomorphy (it imports 4D N = 1), and makes no prediction. **NOT EARNED.** The agy lane's C5, C13 and C37 make related claims; C13's Schur-uniqueness argument for the shared S is the nearest to I-37's criterion and is owed a reading at source |
| **BANK-1 retires SE1–SE3 and GM1–GM4** | a retirement needs the entry to follow from what remains | **SE1:** replaced by "minimal volume over all cusped manifolds", the record's own listed alternative (GENESIS SE1 row): a swap, not a retirement. **SE2:** passing to the orientable cover is the same choice, renamed "the unique index-2 subgroup". **SE3:** the first non-abelian quotient's prime is 5, the same 5 as the discriminant and the knot's determinant; a re-expression, with its own rule ("take the least non-abelian quotient"). **GM1–GM4** (the iteration on ℤ², the unit shears, aperiodicity, the punctured-torus carrier) are not addressed; BANK-1 starts from a manifold instead. **NOT RETIRED.** Net count unchanged; the chain is registered as an alternative foundation |
| **BANK-2 retires Postulate D** | the four orbifold bits derived | the bits are replaced by the reflection's identification and a sign choice. **NOT RETIRED** |
| **BANK-4 closes B1970's lepton–down gate and B1965–B1969's single-point wall** | the split and an aligned hierarchical mixing derived in frame C | the single point's rank 2 is B1659/B1739, and the E[5] tie is SM-C13. The split comes from averaging over K5 ⊕ K6 at one bulk modulus τ₈⁺ (Im τ = 8/5), with frame C's channel norms dropped. LINK4's own ledger prices that construction at 2 bits (locus assignment), 1 bit (connection lift) and 6.17 bits (word), plus τ. **NOT CLOSED**: a model with at least 9 priced bits and a chosen modulus. B1965–B1969 are single-doublet results (agy-002's scope note), and that wall is answered by agy-002's A2-P879 and the agy lane's C1, owed a reading at source (P-879) |
| **BANK-5 solves the mixing's size** | an aligned mixing of the size needed, derived | it rests on a spin-½ Liouville Kähler metric (an imported physics premise), the chosen τ₈⁺, and a Γ₀(2) "singleton slot" criterion that keeps (2,0,3) and (3,0,2). LINK4's F6 calls the spin-cover Gramian flavour-blind; LINK5's Liouville metric is not; the seat does not reconcile them. BANK-10's A2-OW27-F2 evaluates (3,0,2), the equivariant branch, against agy-002's intervals and reports that it hits all three; the other equivariant branch is not evaluated against them, and the choice between the two is priced R1 = 1 bit [corrected 2026-11-24, Review 86: it read 'prefers (3,0,2) because it hits all 3', which is not in the source]. **NOT SOLVED**; recorded as a model output at a chosen point |
| **BANK-6, BANK-7** | — | computations inside an imported string-phenomenology stack: gaugino condensation, a nilpotent Polonyi term, DKL, Split-SUSY and MSSM running, inflation. Registered by name; nothing in the record changes |
| **BANK-8: the floor is 2.0 bits + 1 continuous + 1 anchor + 1 structural postulate** | an input count closed under what is imported | the "structural postulate" absorbs Hořava–Witten, F-theory and 4D N = 1 SUSY. The 2.0 bits omit LINK4's own priced 9.17 bits and τ. The chosen rationals (BANK-6's and BANK-7's constants) are not counted. **NOT REGISTERED as the record's floor**; recorded as the seat's own count, with these corrections |
| **BANK-9, BANK-10 (the peer audits)** | — | reproductions of other seats' numbers by the same family of scripts; registered as the seat's verification records (Tier B/C), each to be taken item by item when cited |

## What it means

- **The seat's mathematics is mostly right.** Three statements are corrected:
  - the minimal-volume attribution;
  - the 10-fold versus 5-fold cover;
  - the sign of the projection.
- **The record-level conclusions are not.** Each replaces a choice with another choice, imports a framework, or selects by agreement with targets.
- The parameter-free reading it asks for is therefore not established. Every input it removes reappears as a priced bit, a chosen constant or an imported structure.
- **What is worth keeping:**
  - the Gieseking start as an alternative foundation (the same count);
  - K5 as the record's act line;
  - the agy-002 and agy lane answers on P-879, owed a reading at source.

## What is open

- **The answers on P-879,** read at source: agy-002's A2-P879 and the agy lane's C1. This is Tier A.
- **The agy lane's C13 Schur-uniqueness argument for a shared S,** against I-37's criterion. This is Tier A.
- **The web seat's W-D2 § 3:** the lepton–down relation Y_lep(R + s1) = λ Y_down(R − s1)ᵀ and its window.
