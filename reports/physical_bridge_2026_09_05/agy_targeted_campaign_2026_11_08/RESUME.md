# AGY Campaign Handoff & Durable State (`RESUME.md`)

- **Date:** `2026-11-09`
- **Active Campaign Directory:** `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/`
- **Completed Microtask:** `AGY-01a-r1` (`REVIEW_AGY_01A_6CCE_2026_11_09.md` at `c542ba48fca5cb8bb6700634abedaffbe887f25f`, SHA256 `f1cd3d27efce72e2056e001db165f362430cbb56933baf9b37488c505620a43e`; `START_HERE.md`, SHA256 `b2d56e4317dd738831f204b1c1d3f548be9355e038bde2112e5961d519c44b07`; `TASKS.json`, SHA256 `0afe195709212ea78353bd71bcd75202592cc97cd176c8086e37e5950dbcf5d8`)
- **Scientific Execution Status:** `scientific_execution_authorized = false` (no scientific code, CAS, imports, test collection, or runs executed)

---

## 1. Preserved Accepted Baseline & Historical Relays (`G1`)

1. **`MODEL_MANIFEST.md`:** Preserved byte-for-byte at accepted `6552aec6894a4a94a2ced785ac3af8c25f801ba8` state (SHA256 `811956e0ffc5ca9f141c57e6eb5e98bc576aa5b8e7fe18909c4fc2cd9136ebdb`), accepted at `d1b2303969050925d4b548ed21ec862208107b9f`.
2. **`CLAIM_DEPENDENCIES.md`:** Preserved byte-for-byte at accepted `43af86dbecb335ddd0952533dc2680d4a4e7f64a` state (SHA256 `eb68f876fdf5b842c471738d7fc1c672f685db1a552d30ad669d7f1dba02802a`), accepted at `400244e32c737d9b947546e2b12fec5ab57c9627`.
3. **`INPUT_LEDGER.md`:** Preserved byte-for-byte at accepted `605294403ecdd26666f3902881558e4bf6b85e93` state (SHA256 `98bf93b4be89297901e8f9718f88ea526105b717310df63b75e21deb282713e5`), accepted at `99a0364f2f17ffb02923042a7e9edd4a0e1af99d` (`REVIEW_AGY_00B2A_R2_605294_2026_11_09.md`, SHA256 `5454ef0dcb42f51bcce00567cfbaa54532f8e3b7de5df4afc9892eeb37d63e6d`).
4. **Historical Relays:** All prior relays (`ac0897123`, `17f75dba0`, `605294403`, and `6cce98355` `AGY_TO_PHYSICAL_2026-11-09_AGY_01A_COMPENSATOR_RANGE_AUDIT.md`, SHA256 `462342ae9a52f72907f36c50462781cfac2882f9a2cdb2a8ac376a90b50c99cd`) preserved byte-identical.

---

## 2. Completed Deliverable for `AGY-01a-r1` (`G1`–`G4` Resolved)

- **`COMPENSATOR_RANGE_AUDIT.md`:**
  - **SHA256:** `81b29726b20218ed2625de06369c7a5d55c13427d85d81ed2888d27a3280a0d3` (`1536` words via `wc -w`, `30` displayed witness equation lines, within the `<= 1800` word and `<= 70` equation-line bounds; marked `AUTHOR HAND PROOF / UNREVIEWED`).
  - **Preserved Core Constructive Calculation (`6cce98355669f9d9c587035846ec7c0b20daffa0`):** Retained the explicit real frame $U_{\text{real}}$, orientation sign $\delta = -1$ ($A U A^{-1} = W = -C U = \mathrm{Zeta}\,C U$), passing outer witness $h_1 = U f_1$ ($(A h_1)^2 = K_\pi$, circle inversion, scalar compensation, $[A',B'] = \mathrm{Zeta}\,P$, unbroken $\mathfrak{so}(5) \subset A_3$), and central obstruction $(A h_3)^2 = \mathrm{Zeta}\,K_\pi \neq K_\pi$ for the particular product $h_3 = U f_1 f_2 f_3$.
  - **Resolution of `G1`–`G4`:**
    - **`G1` (Git References):** Replaced the two invalid full commit strings with the verified Git object hashes `9a2bd40b3cf0a4d675a3c7013f83873d620a7bde` (for `OPEN_PIN2_CORRECTION_BEYOND_THE_CHOSEN_EM_CIRCLE_2026_11_09.md`) and `6552aec6894a4a94a2ced785ac3af8c25f801ba8` / `43af86dbecb335ddd0952533dc2680d4a4e7f64a` (with acceptance records `d1b2303969050925d4b548ed21ec862208107b9f` / `400244e32c737d9b947546e2b12fec5ab57c9627`).
    - **`G2` (Volume/Chirality Convention):** Unified raw volumes throughout as $\omega_{10} = W U = -C$, $\omega_6 = f_1\cdots f_6 = -C_6$, and $\omega_{16} = \omega_{10}\omega_6 = C C_6 = \exp(2\pi i(1/2)^8_{D_8})$ with $\operatorname{vol}(V_{5,+}) = -W$, $\operatorname{vol}(V_{5,-}) = U$, $\operatorname{vol}(V_{5,+})\operatorname{vol}(V_{5,-}) = C = -\omega_{10}$, and $\ker(\pi_{E_8}) = \{1,\omega_{16}\}$ acting as $+1$ on $128 = S_+(\mathbb{R}^{16})$, so $h_1\omega_{10}h_1^{-1} = -\omega_{10}$ ($h_1 C h_1^{-1} = -C$) and $h_1\omega_6 h_1^{-1} = -\omega_6$.
    - **`G3` (Global Subgroup Structure):** Typed $\operatorname{Ss}(16) = \operatorname{Spin}(16)/\langle\omega_{16}\rangle$ as a maximal connected proper rank-$8$ subgroup of compact $E_8$, identified the cyclic order-$4$ central kernel $K_{10,6} = \langle(\omega_{10},\omega_6)\rangle = \{(1,1),(\omega_{10},\omega_6),(-1,-1),(-\omega_{10},-\omega_6)\} \cong \mathbb{Z}_4$ of $(\operatorname{Spin}(10)\times\operatorname{Spin}(6))/K_{10,6} \subset \operatorname{Ss}(16)$ (McInnes `hep-th/9906059` §§II–III), and typed $\operatorname{Pin}_-(10)\cdot\operatorname{Pin}_-(6)$ as the odd-odd coset in $\operatorname{Ss}(16)\subset E_8$.
    - **`G4` (Selection Scope & $\chi=0$ Boundary):** Removed the uncoupled Wilson/$\operatorname{U}(2)$ side remark (keeping $\chi=0$), distinguished internal $\operatorname{Spin}(10)$ half-spinor labels $(16,4),(\overline{16},\overline{4})$ from physical 4D weak chirality, and scoped connectedness $h \in \operatorname{Spin}(6)$ as a **sufficient** extra premise excluding $h_1$ (while leaving full disconnected-centralizer classification open).

---

## 3. Stopping Point & Next Dependency

- **Stop Condition:** Reached at completion of `AGY-01a-r1`. Awaiting physical-seat review before any subsequent microtask is released.
