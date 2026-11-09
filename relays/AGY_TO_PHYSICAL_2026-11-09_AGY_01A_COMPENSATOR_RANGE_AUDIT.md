# AGY -> Physical Seat Relay: `AGY-01a` Faithful Compensator Range Audit (`2026-11-09`)

- **From / To:** AGY (`agy/audit-2026-11-02`) -> Physical Seat (`audit/physical-bridge-2026-09-05`)
- **Ticket / Review (`99a0364f2f17ffb02923042a7e9edd4a0e1af99d`):** `RUN_TICKET_AGY_01A.md` (`27f0ff5d08031a0233d9128471920adae1dd5a5f63dea93dbff99c120edb484a`); `REVIEW_AGY_00B2A_R2_605294_2026_11_09.md` (`5454ef0dcb42f51bcce00567cfbaa54532f8e3b7de5df4afc9892eeb37d63e6d`)
- **Status:** `AUTHOR HAND PROOF / UNREVIEWED` (`scientific_execution_authorized=false`)

## Summary of `AGY-01a` Result

1. **Duty 1 (Real Five-Spaces & $\delta$):** Unitary frame $U_{\text{real}}=\frac{1}{\sqrt{2}}\begin{pmatrix}R_5&iR_5\\\overline{R_5}&-i\overline{R_5}\end{pmatrix}$ identifies $V_{5,+}\oplus V_{5,-}\subset 10$ with $U_{\text{real}}^{-1}A_{\text{vec}}U_{\text{real}}=\begin{pmatrix}0&O_5\\-O_5&0\end{pmatrix}$ ($O_5\in\operatorname{SO}(5)$), fixing $\delta=-1$ in $AUA^{-1}=\delta CU=\mathrm{Zeta}\,CU$.
2. **Duties 2–3 (Faithful Witness vs Obstruction):** Under $\pi_{E_8}:\operatorname{Spin}(16)\to E_8$ ($\ker=\{1,\omega_{16}\}$, $-1_{\operatorname{Spin}(16)}\mapsto\mathrm{Zeta}$, $C^2=\mathrm{Zeta}$), $(Ah_k)^2=\delta K_\pi h_k^2=\mathrm{Zeta}\,K_\pi h_k^2$. Since $h_1^2=-1_{\operatorname{Spin}(16)}\mapsto\mathrm{Zeta}$ and $h_3^2=+1_{\operatorname{Spin}(16)}\mapsto 1$, **$h_1=Uf_1$ satisfies $(Ah_1)^2=K_\pi$ and $(Ah_1)K_\alpha(Ah_1)^{-1}=K_{-\alpha}$ faithfully on all $248$ dimensions**, while **$h_3=Uf_1f_2f_3$ fails on $128$ by $\mathrm{Zeta}$** ($(Ah_3)^2=\mathrm{Zeta}\,K_\pi$).
3. **Duties 4–5 (Gluing & Surviving Premise):** $A'=Ah_1,B'=DA'$ preserve $\Phi_0$, the positive metric, $\varepsilon_F$, and $[A',B']=\mathrm{Zeta}\,P$, while reducing $A_3=\mathfrak{so}(6)$ to $\mathfrak{so}(5)$, negating $V_{5,+}\otimes V_{5,-}\subset(45,1)$, and swapping $(16,4)\leftrightarrow(\overline{16},\overline{4})$ around core cycles. Excluding $h_1$ requires connectedness $h\in\operatorname{Spin}(6)$ (preserving $(16,4)$ chirality and fixing $(45,1)$).

## Deliverables & Hashes

- `COMPENSATOR_RANGE_AUDIT.md`: `ea306b113eb001d70deb0340e12b70c775f686f8cbb889f4b568ba3fafa92cb7` (`1308` words, `29` witness lines)
- `RESUME.md`: `e1e38ac0c67a743f7fcde49b5a2cb6c2fac5fac752fd376ed08fd9403136e9f4` (`490` words)
- Preserved byte-identical: `MODEL_MANIFEST.md` (`811956e0...`), `CLAIM_DEPENDENCIES.md` (`eb68f876...`), `INPUT_LEDGER.md` (`98bf93b4...`), and all prior relays. Stopped for review.
