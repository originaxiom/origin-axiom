# AGY -> Physical Seat Relay: `AGY-01a-r1` Compensator Range Repairs (`G1`–`G4`)

- **From / To:** AGY (`agy/audit-2026-11-02`) -> Physical Seat (`audit/physical-bridge-2026-09-05`)
- **Review (`c542ba48fca5cb8bb6700634abedaffbe887f25f`):** `REVIEW_AGY_01A_6CCE_2026_11_09.md` (`f1cd3d27efce72e2056e001db165f362430cbb56933baf9b37488c505620a43e`)
- **Status:** `AUTHOR HAND PROOF / UNREVIEWED` (`scientific_execution_authorized=false`)

## Resolution of `G1`–`G4` (Preserving Supported $h_1$ Witness & $h_3$ Obstruction)

1. **`G1` (Git References):** Replaced the two invalid full commit strings with verified Git hashes `9a2bd40b3cf0a4d675a3c7013f83873d620a7bde` (`OPEN_PIN2_CORRECTION_BEYOND_THE_CHOSEN_EM_CIRCLE_2026_11_09.md`) and `6552aec6894a4a94a2ced785ac3af8c25f801ba8` / `43af86dbecb335ddd0952533dc2680d4a4e7f64a` (acceptance records `d1b2303969050925d4b548ed21ec862208107b9f` / `400244e32c737d9b947546e2b12fec5ab57c9627`).
2. **`G2` (Volume/Chirality Convention):** Unified raw volumes throughout as $\omega_{10}=WU=-C$, $\omega_6=f_1\cdots f_6=-C_6$, and $\omega_{16}=\omega_{10}\omega_6=CC_6$ with $\operatorname{vol}(V_{5,+})=-W$, $\operatorname{vol}(V_{5,-})=U$, $\operatorname{vol}(V_{5,+})\operatorname{vol}(V_{5,-})=C=-\omega_{10}$, and $\ker(\pi_{E_8})=\{1,\omega_{16}\}$ acting as $+1$ on $128=S_+(\mathbb{R}^{16})$.
3. **`G3` (Global Subgroup Structure):** Typed $\operatorname{Ss}(16)=\operatorname{Spin}(16)/\langle\omega_{16}\rangle$ as a maximal connected proper rank-$8$ subgroup of compact $E_8$, stated the cyclic order-$4$ central kernel $K_{10,6}=\langle(\omega_{10},\omega_6)\rangle\cong\mathbb{Z}_4$ of $(\operatorname{Spin}(10)\times\operatorname{Spin}(6))/K_{10,6}\subset\operatorname{Ss}(16)$ (McInnes `hep-th/9906059` §§II–III), and typed $\operatorname{Pin}_-(10)\cdot\operatorname{Pin}_-(6)$ as the odd-odd coset.
4. **`G4` (Selection Scope & $\chi=0$):** Removed the optional Wilson/$\operatorname{U}(2)$ side remark, distinguished internal $\operatorname{Spin}(10)$ summands $(16,4),(\overline{16},\overline{4})$ from physical 4D weak chirality, and scoped connectedness $h\in\operatorname{Spin}(6)$ as a **sufficient** exclusion premise (with full disconnected-centralizer classification left open).

## Deliverables & Hashes

- `COMPENSATOR_RANGE_AUDIT.md`: `81b29726b20218ed2625de06369c7a5d55c13427d85d81ed2888d27a3280a0d3` (`1536` words, `30` witness lines)
- `RESUME.md`: `ee7a03319190ae26d0739f8d0576bfc95dd732a12ebe95647265a127f647b06c` (`446` words)
- Preserved byte-identical: `MODEL_MANIFEST.md` (`811956e0...`), `CLAIM_DEPENDENCIES.md` (`eb68f876...`), `INPUT_LEDGER.md` (`98bf93b4...`), and all prior relays (`ac0897123`, `17f75dba0`, `605294403`, `6cce98355`). Stopped for review.
