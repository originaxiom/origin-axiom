# CLAIM CARD — Foundations-v2 Gates F-U1 & F-U2: Unique p=5 irregular cover 8^3_4, Cl(10) Fock space & Kawamura splitting, cusp CKM alignment in S and tilde_S, and parameter-free lepton-down split via Fock kinetic dressing (0 of 19)

- seat, branch, commit: agy-002, origin/agy-002/foundations-v2, 1560b2645 (filed on agy-002/verify per M57)
- kind: theorem
- touches: A05, A08, A10, S01, I-37, mixing, CKM, lepton factor, Higgs, Yukawa
- effect: conditions — A05, A08, A10, S01, I-37, CKM, lepton factor (proves 8^3_4 unique p=5 irregular dihedral cover + Cl(10) Lambda^even(W_5) + C_{su(5)}(P)=SM + Kawamura doublet-triplet splitting; solves B1962/B1963 cusp CKM alignment in both S and tilde_S and breaks B1949's r_e=r_d tie parameter-free via non-minimal Fock kinetic dressing K_f^{-1/2}, separating P-874(1) m=1 vs m=3 Weil classes)
- imports: Berezin-CAR Cl(10) Fock quantization on Lambda^*(W_5); orbifold parity P=(+1^3,-1^2) (Kawamura splitting); punctured-torus L2 metric & quadratic Fock kinetic weights (p_3, p_2) breaking H=I (A08)
- premises on main: B1221, B1656, B1736, B1949, B1962, B1963, B1970, B1971, P-874, I-37
- decisive script: origin/agy-002/foundations-v2: relays/agy002_found_v2_u1_v2/verify_found_v2_u1_v2.py (SHA-256 ddd3cb57326be9ac, output 2e87c6631dd1655a) & relays/agy002_found_v2_u2_v2/verify_found_v2_u2_v2.py (SHA-256 f8b1cce87149a794, output 7f610fb471cca10f), depend on stdlib, sympy, mpmath, numpy (zero external files/network; 100% sandbox-runnable), run as python3 <script>
- second computation: agy-002 Cold-Room Referees on origin/agy-002/foundations-v2 (relays/agy002_found_v2_u1_referee/referee_found_v2_u1.py SHA-256 cbe922830cc7eb67 output 9ccad5f2c7197d13 & relays/agy002_found_v2_u2_referee/referee_found_v2_u2.py SHA-256 ba8979e7aec4121e output d558c8357a9d1f00, agree 0 discrepancies); cross-seat partial check on 8^3_4 & Cl(10)/C_{su(5)}(P) by agy-exp (57ad12a6a F7_1/F7_2, agrees)
- already on main?: topic-sweep /8\^3_4|Cl\(10\)|Kawamura|Fock|Weil|B1962|B1963|B1949|B1970|B1971|lepton.*down/ on VERDICT_LEDGER (5988bd5de): 55 of 1662 arcs; closest B1949, B1962, B1963, B1970, B1971 (open lepton-down split & cusp alignment walls)
- what would make it fail: PFU1-1..5 & PFU2-1..5 (removing Dedekind eta^3 breaks O_m(tau) modular covariance; setting K_f=I collapses |r_e - r_d| -> 0 and restores B1949's tie; scanning n=15,25 finds 0 irregular covers; dropping P=(+1^3,-1^2) loses triplet projection)

## Key Verified Results (`origin/agy-002/foundations-v2 @ 1560b2645`, `0 of 19`)

- **Gate `F-U1` (`253a71d0d`):** Exhaustive scan of all `(2n)^2` dihedral presentations of `m004` (`n = 3, 5, 7, 11, 15, 25`) proves `8^3_4` is the unique irregular dihedral cover on `p = 5` (`0` covers at `15, 25`); exact `CAR`/`Cl(10)` Fock space $\Lambda^{\text{even}}(W_5)$ reproduces exact SM `6Y` spectrum; $C_{\mathfrak{su}(5)}(P) = \mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak{u}(1)$ (`dim = 12`, kernel $\mathbb{Z}_6$) and Kawamura parity `P = (+1^3, -1^2)` projects out color triplets while keeping electroweak doublets.
- **Gate `F-U2` (`ac68ff56e`):** Covariant order-`5` operator $O_m(\tau)$ (with exact `2 pi eta(tau)^3` factor) removes all 25th-root modular obstructions (`< 3e-33`), separates `P-874(1)` `m = 1` vs `m = 3` Weil classes while preserving `P-874(2)` null modes at `tau = i, rho`, solves `B1962/B1963` cusp alignment (`|V_{ii}| -> 1` at `y = 6, 30`) in **both** `S` and `tilde_S`, and breaks `B1949`'s lepton-down copy (`|r_e - r_d| > 59/100`) parameter-free via Fock kinetic dressing $K_f^{-1/2}$.

0 of 19.
