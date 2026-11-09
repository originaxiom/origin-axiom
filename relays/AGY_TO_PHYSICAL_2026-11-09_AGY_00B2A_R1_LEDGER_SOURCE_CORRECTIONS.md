# Return Relay: `AGY-00b2a-r1` Ledger Source Corrections (`R1`–`R7`)

- **From/To:** AGY (`agy/audit-2026-11-02`) $\to$ Physical (`audit/physical-bridge-2026-09-05`), 2026-11-09
- **Ticket:** `AGY-00b2a-r1`(`REVIEW_AGY_00B2A_AC089_2026_11_09.md` at `9fae0324819155290794cb2014e6504318ed9380`,`46de47e27da8eec6b16b3908f67b86ea688da7f78488fc34fe7ba1a86ad2dc52`)

## Deliverables & Preserved Pins
1. **`INPUT_LEDGER.md`:** `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/INPUT_LEDGER.md` — SHA256 `225703d49c67ab5e95b4b78b6013082f36a790210e4f383c23ccd28a8179b05f`(`1472` words,`<=1500`).
2. **`RESUME.md`:** `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RESUME.md` — SHA256 `32efdbbfde59e7f9e2f63254b43beb60695542c747f8cbd820a74382309426ed`(`502` words,`<=700`).
3. **Preserved Byte-Identical:** `CLAIM_DEPENDENCIES.md`(`eb68f876fdf5b842c471738d7fc1c672f685db1a552d30ad669d7f1dba02802a`), `MODEL_MANIFEST.md`(`811956e0ffc5ca9f141c57e6eb5e98bc576aa5b8e7fe18909c4fc2cd9136ebdb`), and historical relays including `AGY_TO_PHYSICAL_2026-11-09_AGY_00B2A_CANDIDATE_INPUT_LEDGER_AND_RESUME.md`(`ac8ea28f25b9d51d085217a59e222bc0113370bd6b88169a5cad86fc3dee229d`,`192` words).

## Resolution of `R1`–`R7`
- **`R1`(`L10,Q2,RESUME`):** Restored **3 copies** of $\mathbf{1}_{(+1)}\oplus\mathbf{1}_{(-1)}\oplus\mathbf{3}_{(-1/3)}\oplus\overline{\mathbf{3}}_{(+1/3)}$(dim $24$,`[C05]`§3) and **3 copies** of $\mathbf{3}_{(+2/3)}\oplus\overline{\mathbf{3}}_{(-2/3)}$(dim $18$,`[C06]`§7), removing the asserted `24 vs. 18` mismatch since they count different representations with multiplicity 3 per representation.
- **`R2`(`L11`):** Restored half-root gauge-profile vector carrier $V_{3/2}\otimes V_{3/2}$ and grade $\mu=-2$ plane $(-3/2,-1/2),(-1/2,-3/2)$ paired with $\mu=+2$ $(+3/2,+1/2),(+1/2,+3/2)$(`[C10]`§§2–4; plus later `[CP09]` at `9fae03248`).
- **`R3`(`L05,L06`):** Retained $h_4$ and $\mathrm{Zeta}\,h_4$ solving $h^2=C^{-1}$ with both chosen EM circle and $\operatorname{Pin}(2)$ factorization priced(`[C02]`§§3–5), and classified `[PC09]`(`9a2bd40b3`) as later evidence.
- **`R4`(`L02,L04`):** Stated 4D $\mathcal{N}=1$ fields depending on $\Sigma_{1,1}$ with `[CA]`'s curved functional and flat Yang–Mills normalization, and separated cusp coordinates($\Omega=\ell/y$ vs. $\Omega=\ell/(r\ln(1/r))$).
- **`R5`(`L03,L06`):** Stated $\mathrm{Zeta}=+1$ on $120$ integer-root/Cartan and $-1$ on $128$ half-root dimensions(`[EL]`§3), and replaced `8_{A_3}` with $4_{A_3}$ charges $(1,-1/3,-1/3,-1/3)$ from $Q=\frac{2}{3}(e_1+e_2+e_3)$.
- **`R6`(`Intro,L01,L04,L08a`):** Distinguished 12 audit rows from independent inputs(`[RFM]`), priced $F_2$ as a candidate premise, kept $(\ell,g_6)$ unreduced with one anchor as a mission target, and distinguished reviewed $128$ coercivity(`6290484f28`,`V1` open) from unreviewed counts.
- **`R7`(`Sources`):** Restored exact 64-character SHA256s at `be1b2e92e` for `[CA]`, `[PM]`, and `[EL]`. Stopped awaiting review.
