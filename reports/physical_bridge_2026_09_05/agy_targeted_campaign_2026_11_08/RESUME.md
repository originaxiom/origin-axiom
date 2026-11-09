# `RESUME.md` — Compact Restart File (`AGY-00b2a-r2` Completed; Stopped for Physical Review)

## 1. Current Campaign State & Governance
- **Active Branch / Seat:** `agy/audit-2026-11-02` (AGY Exploration Seat).
- **Completed Checkpoint:** `AGY-00b2a-r2` (`INPUT_LEDGER.md`, `RESUME.md`, and return relay `relays/AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_R2_TINY_SOURCE_REPAIRS.md`), released by `REVIEW_AGY_00B2A_R1_17F75_2026_11_09.md` (`60700070b46ded3ac9c06b92567fcf9cf0a376e95e407f895e05e885f147a050`) and `START_HERE.md` (`58b68e8c5e54e3143edaa59c458286e322357ce6035ae46e78b05bb616fdd374`) at `2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`.
- **Canonical Baseline:** `GENESIS.md` at `217e37c4f37bd80998f3c3e10cad358023f58114` (`0 of 19` confirmed Standard Model parameters).
- **Physical Revision Base:** `be1b2e92e64eb488870ec1b27a3b0841fd026845` (plus later unreviewed commits `2b572014cdbbb4ef8a9287b0d7b18eb98e5816a2`, `9a2bd40b3cf0a4d675a3c7013f83873d620a7bde`, and `9fae0324819155290794cb2014e6504318ed9380`).
- **Execution Gate:** `scientific_execution_authorized = false`. Zero scientific code edits, imports, collection, or test runs were performed.

## 2. Accepted & Current Artifacts (Exact Pins)
1. **`MODEL_MANIFEST.md` (`AGY-00a-r1`, accepted at `d1b2303969050925d4b548ed21ec862208107b9f`, byte-preserved):**
   - Commit: `6552aec6894a4a94a2ced785ac3af8c25f801ba8`
   - SHA256: `811956e0ffc5ca9f141c57e6eb5e98bc576aa5b8e7fe18909c4fc2cd9136ebdb`
   - Read with the 4 reading notes of `REVIEW_AGY_00A_R1_655_2026_11_08.md` (`c6942f5f1516b7600765bcafafb991f4ec35375dda9f345367ae3b255aebb458`).
2. **`CLAIM_DEPENDENCIES.md` (`AGY-00b1-r1`, accepted at `400244e32c737d9b947546e2b12fec5ab57c9627`, byte-preserved):**
   - Commit: `43af86dbecb335ddd0952533dc2680d4a4e7f64a`
   - SHA256: `eb68f876fdf5b842c471738d7fc1c672f685db1a552d30ad669d7f1dba02802a`
3. **Preserved Historical Relays (`9d0a31e8d`, `ac0897123`, `17f75dba0`):**
   - `relays/AGY_TO_PHYSICAL_2026-11-08_AGY_00B1_R2_RELAY_CORRECTION_AND_RESUME.md`: `630ef5653e5a55ceaeb54e263f6f1e6d7253f856f9cf193f7a37d7e7166b7af0` (`315` words)
   - `relays/AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_CANDIDATE_INPUT_LEDGER_AND_RESUME.md`: `ac8ea28f25b9d51d085217a59e222bc0113370bd6b88169a5cad86fc3dee229d` (`192` words)
   - `relays/AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_R1_LEDGER_SOURCE_CORRECTIONS.md`: `67cec6e3b7079ba87a4d386c25f797c72eb830a707c65bc940c1f1035314a286` (`234` words)
4. **`INPUT_LEDGER.md` (`AGY-00b2a-r2`, awaiting review):**
   - Path: `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/INPUT_LEDGER.md`
   - SHA256: `98bf93b4be89297901e8f9718f88ea526105b717310df63b75e21deb282713e5` (`1497` words, `<= 1500` limit)
5. **`AGY-00b2a-r2` Return Relay:**
   - Path: `relays/AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_R2_TINY_SOURCE_REPAIRS.md` (`<= 250` words)

## 3. Summary of `INPUT_LEDGER.md` (`R1`–`R7` & `T1`–`T4` Addressed)
- **Row Count vs. Inputs & Source Hashes (`R6,R7,T4`):** Distinguishes the 12 audit rows (`L01`–`L12`) from independent physical input counts (`[RFM]`) and records exact full 64-character SHA256s at `be1b2e92e`/`d1b230396` for `[CA]`, `[PM]`, `[EL]`, `[RFM]/[RC]`, and `REVIEW_AGY_00A_R1_655_2026_11_08.md` (`c6942f5f1516b7600765bcafafb991f4ec35375dda9f345367ae3b255aebb458`).
- **Parent, Carrier, Scales & Coherent Lifts (`L01`–`L07`, `R3`–`R6,T2,T3`):** Records $F_2=\langle a,b\rangle$ as a declared faithful free-register premise (`L01`); 4D $\mathcal{N}=1$ fields depending on $\Sigma_{1,1}$ with `[CA]`'s curved functional, Killing form $\kappa$, local covariance, and flat Yang–Mills normalization (`L02`); quaternion holonomies and bare precursor $K(a)=A,K(b)=B=DA$ (order 32) with $A^4=B^4=\mathrm{Zeta}$, $(AB)^2=P$ ($P=\exp(-i\pi H/2),P^2=1\implies(AB)^4=1$), $[A,B]=\mathrm{Zeta}\,P$, and $\mathrm{Zeta}=+1$ on $120$ integer-root/Cartan and $-1$ on $128$ half-root dimensions (`[EL]`§§3–4) vs. the candidate's coherent $\operatorname{Pin}(2)/Q_8$ transport (`L03`); $\tau\in\mathbb{H}$, cusp metric $\Omega=\ell/y$ in $w=x+iy$ (or $\Omega=\ell/(r\ln(1/r))$ in $z,r=|z|$), and unreduced scales $(\ell,g_6)$ with one anchor as a mission target (`L04`); $\eta=\mathcal{O}$, `[C02]`§§3–5 pricing of the chosen EM circle $h(\theta)$ and $\operatorname{Pin}(2)$ factorization $h^2=C^{-1}$ yielding $h_4,\mathrm{Zeta}\,h_4$ (plus later `[PC09]` separating the connected-$\operatorname{SU}(4)$ $3+1$ calculation from an `OPEN` outer Clifford witness), and $Q=\frac{2}{3}(e_1+e_2+e_3)$ giving $4_{A_3}$ charges $(1,-1/3,-1/3,-1/3)$ (`L05,L06`); balanced $\Phi_0$ and $\chi=(0,0)$ vs. order-3 $\chi_3\neq0$, which leaves the complementary $\operatorname{U}(3)$ singlet at multiplicity 3 and removes the coloured triplet's extra middle section (multiplicity $3\to2$, coherent $24\to18$; bare $16$ is a separate bare lift, `[C05]`§5) (`L07`).
- **End Law, Multiplicities, Vector/Fermion Weights & Deformations (`L08`–`L12`, `R1,R2,R6,T1`):** Distinguishes reviewed $128$ coercivity (`6290484f28`,`V1` open) from later unreviewed parabolic/matter counts (`L08`); 4-slot mass map $M$ and $P_v$ (`L09`); compatible multiplicity 3 per representation ($3\times8=24$ in $(16,4)\oplus(\overline{16},\overline{4})$ and $3\times6=18$ in $(10,6)$) (`L10,Q2`); half-root vector carrier $V_{3/2}\otimes V_{3/2}$ with $\mu=-2$ plane $(-3/2,-1/2),(-1/2,-3/2)$ paired under $w_R=Jz_-$ with $\mu=+2$ $(+3/2,+1/2),(+1/2,+3/2)$ at $m_0^2=7/(2\ell^2)$ ($|g_R|=|g_L|>0$), where the middle down-quark spin pair is $u':(-3/2,+3/2),v':(+3/2,-3/2)$ ($\mu=0$) and the up spin pair is $u':(-2,0),v':(0,-2)$ ($\mu=-2$) in both the down and independent conjugate-down left sectors (while down form representatives sit at $(+3/2,+3/2),\mu=+3$) (`L11`); and later unreviewed `2b572014c`/`9fae03248` (`[NC09],[CP09]`), where $\Theta=LJ_0$ keeps the $\mu=\mp2$ vector masses paired throughout the small cyclic spin family (`L12,Q1`).

## 4. Next Action upon Restart
- **STOP.** Wait for physical-seat review of `AGY-00b2a-r2` and explicit release of the next microtask in `START_HERE.md` / `TASKS.json`.
