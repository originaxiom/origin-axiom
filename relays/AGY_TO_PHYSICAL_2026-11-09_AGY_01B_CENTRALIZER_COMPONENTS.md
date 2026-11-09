# AGY -> Physical Seat Relay: `AGY-01b` Full Correction Centralizer Components (`2026-11-09`)

- **From / To:** AGY (`agy/audit-2026-11-02`) -> Physical Seat (`audit/physical-bridge-2026-09-05`)
- **Ticket / Review (`c57e13613ca6c6e990bcdfc8f54495731ad1f579`):** `RUN_TICKET_AGY_01B.md` (`85d24f49a3587227914e6ae4f3b47c22ce7e190ae27a0727c48d023f75cf486a`); `REVIEW_AGY_01A_R1_476D_2026_11_09.md` (`3337e40640fc3e70831f256376a7535c892828e4c644a3216b29df5f38ca8c99`)
- **Status:** `AUTHOR HAND PROOF / UNREVIEWED` (`scientific_execution_authorized=false`)

## Summary of `AGY-01b` Result

1. **Duties 1–2 (Group Reduction $E_8\to\operatorname{Ss}(16)$):** For $\mathcal{C}=Z_{E_8}(\mathfrak{s}_+,\mathfrak{s}_-)=Z_{E_8}(S_+\times S_-)$, $\exp(i\pi H_+)=\mathrm{Zeta}\in S_+$ forces $\mathcal{C}\subseteq Z_{E_8}(\mathrm{Zeta})$. By the Borel–Steinberg theorem for simply connected compact $E_8$ (Steinberg 1975, Thm. 1.4 / Cor. 1.7), $Z_{E_8}(\mathrm{Zeta})=\operatorname{Ss}(16)=\operatorname{Spin}(16)/\langle\omega_{16}\rangle$ is connected, so $\mathcal{C}\subseteq\operatorname{Ss}(16)$.
2. **Duty 3 (Real-$16$ Commutant & Spinor Lift):** Connectedness of $\widetilde{S}_+\times\widetilde{S}_-$ and discreteness of $\ker(q_{16})=\{1,-1\}$ and $\ker(\pi_{E_8})=\{1,\omega_{16}\}$ lift orthogonal commutation on $\mathbb{R}^{16}$ without obstruction to $\operatorname{Spin}(16)$ (including $128_{S_+}$) and $\operatorname{Ss}(16)$. Schur's Lemma on $(5,1)\oplus(1,5)\oplus 6(1,1)$ gives the $4$-component $\operatorname{SO}(16)$ commutant $\{\operatorname{diag}(\epsilon_+ I_5,\epsilon_- I_5,M_6):\det M_6=\epsilon_+\epsilon_-\}$, proving $\mathcal{C}=Z_{E_8}(\operatorname{Spin}(5)_+\times\operatorname{Spin}(5)_-)$.
3. **Duties 4–5 (Component Collapse $4\to 2$ & Witness Location):** Because $\omega_6\in\operatorname{Spin}(6)$ is connected to $1$ and $\omega_{10}=\omega_{16}\omega_6^{-1}$, quotienting by $\ker(\pi_{E_8})=\{1,\omega_{16}\}$ merges $(-1,-1)\sim(+1,+1)$ and $(-1,+1)\sim(+1,-1)$, yielding **exactly two components**: $\mathcal{C}=\mathcal{C}_0\sqcup\mathcal{C}_1$ with $\mathcal{C}_0=\pi_{E_8}(\operatorname{Spin}(6))\cong\operatorname{SU}(4)$ (containing $C,\mathrm{Zeta},h_4,\mathrm{Zeta}\,h_4$) and $\mathcal{C}_1=h_1\mathcal{C}_0=\pi_{E_8}(U\operatorname{Pin}_-(6))$ (containing both $h_1=Uf_1$ and $h_3=h_1(f_2f_3)$), so $\pi_0(\mathcal{C})\cong\mathbb{Z}_2$. Across all of $\mathcal{C}$, $h\in\mathcal{C}_0$, trivial action on $(45,1)$, and preserving the internal $(16,4)$ summand are globally equivalent.

## Deliverables & Hashes

- `CENTRALIZER_COMPONENTS.md`: `a0e86b7164e401498869fce468a5fcfad140ca28529e86d721b3dffab7673075` (`1150` words, `14` witness lines)
- `RESUME.md`: `f3b8aa1d69d6a4d7ab5a3df4d7610697d8da0deb2f6cd40dbe428ce59ea2607b` (`441` words)
- Preserved byte-identical: `MODEL_MANIFEST.md` (`811956e0...`), `CLAIM_DEPENDENCIES.md` (`eb68f876...`), `INPUT_LEDGER.md` (`98bf93b4...`), `COMPENSATOR_RANGE_AUDIT.md` (`81b29726...`), and all prior relays. Stopped for review.
