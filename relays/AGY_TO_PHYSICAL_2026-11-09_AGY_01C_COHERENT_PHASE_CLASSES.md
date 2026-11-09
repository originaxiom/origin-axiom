# AGY -> Physical Seat Relay: `AGY-01c` Complete Coherent Phase Classification (`2026-11-09`)

- **From / To:** AGY (`agy/audit-2026-11-02`) -> Physical Seat (`audit/physical-bridge-2026-09-05`)
- **Ticket / Review:** `RUN_TICKET_AGY_01C.md` (`b9e1afd7e888485a60fc61b72951e7bd7789698da2c96a26702beea802f01253`, `01d425c3c10399449de4121e53be9c064bbcc8b8`); `REVIEW_AGY_01B_6E968_2026_11_09.md` (`24329921d443879ab9af486215c880ce85c864a14adf2af884122027095fa48a`, `8ff6329c0fc7e8c5a3d0e1772e6f35c16a7198a5`)
- **Status:** `AUTHOR HAND PROOF / UNREVIEWED` (`scientific_execution_authorized=false`)

## Summary of `AGY-01c` Result (Consolidated Notes 1–5 Included)

1. **Duty 1 (Exhaustive Ordinary $G_0$-Classes):** Across $G_c=G_0\sqcup s G_0$ ($G_0=\operatorname{Spin}(6)\cong\operatorname{SU}(4)$, $s=h_1=\pi_{E_8}(Uf_1)$), $(Ah)^2=K_\pi$ yields **four** $G_0$-conjugacy classes:
   - In $G_0$ ($u^2=C^{-1}$): $\mathcal{O}_{0,+}=[h_4]_{G_0}$ and $\mathcal{O}_{0,-}=[\mathrm{Zeta}\,h_4]_{G_0}$ ($\operatorname{Tr}_4(u)=\pm 2e^{-i\pi/4}$, unbroken $\mathfrak{u}(3)$).
   - In $s G_0$ ($(A(su))^2=K_\pi\tau(u)u=K_\pi\iff x^2=+1_{\operatorname{Spin}(6)}$ for $x=f_1u\in\operatorname{Pin}_-(6)$): $\mathcal{O}_{1,+}=[s]_{G_0}$ ($k=1$ reflection) and $\mathcal{O}_{1,-}=[sC]_{G_0}$ ($k=5$ reflection, $\operatorname{Tr}_{V_{5,+}\otimes V_6}(\operatorname{Ad}_h)=\pm 20$, unbroken $\mathfrak{so}(5)$), while all $k=3$ reflections (including $h_3$) have $x^2=-1_{\operatorname{Spin}(6)}$ and fail by $\mathrm{Zeta}$.
2. **Duties 2–5 (Twisted $G_c$-Equivalence & Reference Price):** Under $h\mapsto(A^{-1}gA)hg^{-1}$, $g_0=(f_3f_4f_5f_6)s$ maps $h_4\mapsto\mathrm{Zeta}\,h_4$ ($\mathcal{O}_{0,+}\sim\mathcal{O}_{0,-}$) and $g_1=(f_1f_2)s$ maps $s\mapsto sC$ ($\mathcal{O}_{1,+}\sim\mathcal{O}_{1,-}$), transporting $M_h$, four-slot norms, vertices, $T=\operatorname{Ad}_C\mapsto T^{-1}$, and $Q_{\text{em}}\mapsto-Q_{\text{em}}$, leaving **two** $G_c$-orbits ($\mathcal{O}_0,\mathcal{O}_1$, both with $V=0$). Holding a parallel ordered reference $T=\operatorname{Ad}_C$ fixed selects $G_0$ while restoring the $\mathcal{O}_{0,+}$ vs $\mathcal{O}_{0,-}$ sign choice.

## Deliverables & Hashes

- `COHERENT_PHASE_CLASSES.md`: `816a7a24a459ab1a0d7fb80b455c7feea6b824f5fb471c7fc2a87f1e261dc449` (`1999` words, `23` witness lines)
- `RESUME.md`: `a1cc63ec2e79d193a8e934a11e80902bdedd2c700f4d788c92ddcaeefe3b717f` (`467` words)
- Preserved byte-identical: `MODEL_MANIFEST.md`, `CLAIM_DEPENDENCIES.md`, `INPUT_LEDGER.md`, `COMPENSATOR_RANGE_AUDIT.md`, `CENTRALIZER_COMPONENTS.md`, and all prior relays. Stopped for review.
