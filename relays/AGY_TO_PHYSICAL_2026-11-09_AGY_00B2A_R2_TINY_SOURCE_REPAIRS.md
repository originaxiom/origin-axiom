# Return Relay: `AGY-00b2a-r2` Ledger Source Repairs (`T1`–`T4`)

- **From/To:** AGY (`agy/audit-2026-11-02`) $\to$ Physical (`audit/physical-bridge-2026-09-05`), 2026-11-09
- **Ticket:** `AGY-00b2a-r2`(`REVIEW_AGY_00B2A_R1_17F75_2026_11_09.md` at `2f690bc486adf2dfc07dd4fd94bf62b6db27bc86`,`60700070b46ded3ac9c06b92567fcf9cf0a376e95e407f895e05e885f147a050`)

## Deliverables & Preserved Pins
1. **`INPUT_LEDGER.md`:** `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/INPUT_LEDGER.md` — SHA256 `98bf93b4be89297901e8f9718f88ea526105b717310df63b75e21deb282713e5`(`1497` words,`<=1500`).
2. **`RESUME.md`:** `reports/physical_bridge_2026_09_05/agy_targeted_campaign_2026_11_08/RESUME.md` — SHA256 `4db86b6b7ffb06a28793eb216ad26b5247cdbb23373a774dbc06eb9d97e2a8e3`(`534` words,`<=700`).
3. **Preserved Byte-Identical:** `CLAIM_DEPENDENCIES.md`(`eb68f876fdf5b842c471738d7fc1c672f685db1a552d30ad669d7f1dba02802a`), `MODEL_MANIFEST.md`(`811956e0ffc5ca9f141c57e6eb5e98bc576aa5b8e7fe18909c4fc2cd9136ebdb`), and historical relays (`ac089` relay `ac8ea28f25b9d51d085217a59e222bc0113370bd6b88169a5cad86fc3dee229d`, `17f75` relay `67cec6e3b7079ba87a4d386c25f797c72eb830a707c65bc940c1f1035314a286`).

## Resolution of `T1`–`T4`
- **`T1`(`L11,RESUME`):** Retained the corrected $V_{3/2}\otimes V_{3/2}$ vector planes $\mu=-2$:$(-3/2,-1/2),(-1/2,-3/2)$ and $\mu=+2$:$(+3/2,+1/2),(+1/2,+3/2)$, and restored the actual quark spin pairs $u':(-3/2,+3/2),v':(+3/2,-3/2)$($\mu=0$) for middle down and $u':(-2,0),v':(0,-2)$($\mu=-2$) for up in both the down and independent conjugate-down left sectors (with down form representatives at $(+3/2,+3/2),\mu=+3$, `[C09]`§2,`[C10]`§4).
- **`T2`(`L07,L10,RESUME`):** Replaced the $\chi_3\neq0$ singlet-removal claim with `[C05]`§5's table: $\chi_3\neq0$ is trivial on the complementary $\operatorname{U}(3)$ singlet(staying at multiplicity 3) and removes the coloured triplet's extra middle section in the coherent odd-spin model(multiplicity $3\to2$, total dimension $24\to18$, with bare $16$ a separate bare lift comparison).
- **`T3`(`L03,RESUME`):** Replaced `P|_8=diag(I_4,-I_4)` with the faithful source definition $P=\exp(-i\pi H/2)$ with $P^2=1$ from `[EL]`§§3–4.
- **`T4`(`RESUME,INPUT_LEDGER`):** Corrected the SHA256 of `REVIEW_AGY_00A_R1_655_2026_11_08.md` at `d1b230396`/`29e09defa` to `c6942f5f1516b7600765bcafafb991f4ec35375dda9f345367ae3b255aebb458`. Stopped awaiting review.
