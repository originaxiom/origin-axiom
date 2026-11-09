# `RESUME.md` — Compact Restart File (`AGY-00b2a-r1` Completed; Stopped for Physical Review)

## 1. Current Campaign State & Governance
- **Active Branch / Seat:** `agy/audit-2026-11-02` (AGY Exploration Seat).
- **Completed Checkpoint:** `AGY-00b2a-r1` (`INPUT_LEDGER.md`, `RESUME.md`, and return relay `relays/AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_R1_LEDGER_SOURCE_CORRECTIONS.md`), released by `REVIEW_AGY_00B2A_AC089_2026_11_09.md` (`f80def09cbfec127950e05cafca6882f76038af1397ec18374eb71bc9b0f6e90`), `REVIEW_AGY_00B2A_8CA2_INTAKE_2026_11_09.md` (`8b967096057a58e3b02fcc937c518c95d15136611bca5e2292f7e58a8462cee7`), and `START_HERE.md` (`6e2c90ed57b8a5710f20c23d06fd9a0f9b00e422ef41b17e54b17b576c9f5ef0`) at `29e09defa935cd9d33b7c7d4cb6b9d1a9de4b68f`.
- **Canonical Baseline:** `GENESIS.md` at `217e37c4f37bd80998f3c3e10cad358023f58114` (`0 of 19` confirmed Standard Model parameters).
- **Physical Revision Base:** `be1b2e92e64eb488870ec1b27a3b0841fd026845` (plus later unreviewed commits `2b572014cdbbb4ef8a9287b0d7b18eb98e5816a2`, `9a2bd40b3cf0a4d675a3c7013f83873d620a7bde`, and `9fae0324819155290794cb2014e6504318ed9380`).
- **Execution Gate:** `scientific_execution_authorized = false`. Zero scientific code edits, imports, collection, or test runs were performed.

## 2. Accepted & Current Artifacts (Exact Pins)
1. **`MODEL_MANIFEST.md` (`AGY-00a-r1`, accepted at `d1b2303969050925d4b548ed21ec862208107b9f`, byte-preserved):**
   - Commit: `6552aec6894a4a94a2ced785ac3af8c25f801ba8`
   - SHA256: `811956e0ffc5ca9f141c57e6eb5e98bc576aa5b8e7fe18909c4fc2cd9136ebdb`
   - Read with the 4 reading notes of `REVIEW_AGY_00A_R1_655_2026_11_08.md` (`ca7f22382bd8f89fdba496215c1ff4b180e3170b5c78f242c665417513fb36a7`).
2. **`CLAIM_DEPENDENCIES.md` (`AGY-00b1-r1`, accepted at `400244e32c737d9b947546e2b12fec5ab57c9627`, byte-preserved):**
   - Commit: `43af86dbecb335ddd0952533dc2680d4a4e7f64a`
   - SHA256: `eb68f876fdf5b842c471738d7fc1c672f685db1a552d30ad669d7f1dba02802a`
3. **Preserved Historical Relays (`9d0a31e8d` and `ac0897123`):**
   - `relays/AGY_TO_PHYSICAL_2026-11-08_AGY_00B1_R2_RELAY_CORRECTION_AND_RESUME.md`: `630ef5653e5a55ceaeb54e263f6f1e6d7253f856f9cf193f7a37d7e7166b7af0` (`315` words)
   - `relays/AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_CANDIDATE_INPUT_LEDGER_AND_RESUME.md`: `ac8ea28f25b9d51d085217a59e222bc0113370bd6b88169a5cad86fc3dee229d` (`192` words)
4. **`INPUT_LEDGER.md` (`AGY-00b2a-r1`, awaiting review):**
   - Path: `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/INPUT_LEDGER.md`
   - SHA256: `70148898fa2acdd4faccf1348039678d1ddc5305ffa1f22b9f89263fa1168868` (`1484` words, `<= 1500` limit)
5. **`AGY-00b2a-r1` Return Relay:**
   - Path: `relays/AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_R1_LEDGER_SOURCE_CORRECTIONS.md` (`<= 250` words)

## 3. Summary of `INPUT_LEDGER.md` (`R1`–`R7` Addressed)
- **Row Count vs. Inputs & Source Hashes (`R6,R7`):** Distinguishes the 12 audit rows (`L01`–`L12`) from independent physical input counts (`[RFM]`) and records exact full 64-character SHA256s at `be1b2e92e` for `[CA]`, `[PM]`, `[EL]`, and `[RFM]/[RC]`.
- **Parent, Carrier, Scales & Coherent Lifts (`L01`–`L07`, `R3`–`R6`):** Records $F_2=\langle a,b\rangle$ as a declared faithful free-register premise whose necessity from noncancellation remains open while `[RC06]` prices its operation set and $\Sigma_{1,1}$ carrier map (`L01`); 4D $\mathcal{N}=1$ fields depending on $\Sigma_{1,1}$ with the curved functional of `[CA]`, Killing form $\kappa$, local covariance, and flat Yang–Mills normalization (`L02`); quaternion holonomies and bare precursor $K(a)=A,K(b)=B=DA$ (order 32) with $A^4=B^4=\mathrm{Zeta}$, $(AB)^2=P$ ($P^2=1\implies(AB)^4=1$), $[A,B]=\mathrm{Zeta}\,P$, and $\mathrm{Zeta}=+1$ on $120$ integer-root/Cartan and $-1$ on $128$ half-root dimensions (`[EL]`§§3–4) vs. the corrected coherent $\operatorname{Pin}(2)/Q_8$ transport used by the fixed candidate (`L03`); $\tau\in\mathbb{H}$, cusp metric $\Omega=\ell/y$ in $w=x+iy$ (or $\Omega=\ell/(r\ln(1/r))$ in $z,r=|z|$), and unreduced scales $(\ell,g_6)$ where reducing to at most one dimensionful anchor remains a mission target (`L04`); $\eta=\mathcal{O}$, `[C02]`§§3–5 pricing of the chosen EM circle $h(\theta)$ and $\operatorname{Pin}(2)$ factorization $h^2=C^{-1}$ yielding $h_4$ and $\mathrm{Zeta}\,h_4$ (plus later `[PC09]` separating the connected-$\operatorname{SU}(4)$ $3+1$ calculation from an `OPEN` outer Clifford witness), and $Q=\frac{2}{3}(e_1+e_2+e_3)$ giving $4_{A_3}$ charges $(1,-1/3,-1/3,-1/3)$ (`L05,L06`); balanced $\Phi_0$ and $\chi=(0,0)$ (`L07`).
- **End Law, Multiplicities, Vector Carrier & Deformations (`L08`–`L12`, `R1,R2,R6`):** Distinguishes the independently source-reviewed $128$-sector coercivity at `6290484f28` (`[IR07]`, retaining `V1`) from later unreviewed parabolic/matter counts (`L08`); 4-slot mass map $M$ and $P_v$ (`L09`); candidate multiplicities of **3 copies** of the 8D charged sum $\mathbf{1}_{(+1)}\oplus\mathbf{1}_{(-1)}\oplus\mathbf{3}_{(-1/3)}\oplus\overline{\mathbf{3}}_{(+1/3)}$ (dimension $24$) and **3 copies** of the 6D up pair $\mathbf{3}_{(+2/3)}\oplus\overline{\mathbf{3}}_{(-2/3)}$ (dimension $18$), which count different representations with a compatible multiplicity of 3 per representation (`L10,Q2`); half-root gauge-profile vector carrier $V_{3/2}\otimes V_{3/2}$ with $\mu=-2$ plane $(-3/2,-1/2),(-1/2,-3/2)$ paired with $\mu=+2$ $(+3/2,+1/2),(+1/2,+3/2)$ at $m_0^2=7/(2\ell^2)$ and current witnesses $|g_R|=|g_L|>0$ (`L11`); and later unreviewed `2b572014c`/`9fae03248` (`[NC09],[CP09]`), where $\Theta=LJ_0$ keeps the $\mu=\mp2$ vector masses paired throughout the small cyclic spin family (`L12,Q1`).

## 4. Next Action upon Restart
- **STOP.** Wait for physical-seat review of `AGY-00b2a-r1` and explicit release of the next microtask in `START_HERE.md` / `TASKS.json`.
