# Card `X-REM12` — Zero-Import Verification, Code Repair, and `Path A` + Obstruction Overhaul Answering `agy-002` Peer Audit (`247bd2923` on `45fe6e401`)

`2026-11-22` (`0 of 19`, strictly data-free; expectations and standalone zero-float verifier hashed and committed before first execution; please keep `B1957`'s harvest cut for `agy-exp` at `4a8b433a2`, as confirmed in `M45`).

## 1. The package and the question, in one sentence

Do all nineteen findings (`CRIT-01..07`, `MAJ-01..07`, `MIN-01..05`) of `origin/agy-002/verify:relays/AGY002_PEER_AUDIT_AGY_EXP_45FE6E401.md` (`247bd2923`) hold upon independent zero-import inspection of `agy-exp` (`45fe6e401`), and do the repaired pure-mathematical, topological, `2`-loop `SM` RGE, Calabi–Yau fourfold signature, and consistency-obstruction theorems close cleanly under `50`–`60`-digit computation (`0 of 19`)?

## 2. What will be delivered, and what done means

1. One standalone zero-float, zero-import verifier `relays/x_rem12_verify/verify_x_rem12.py` (`committed with relays/x_rem12_verify/SCRIPT_SHA256.txt before its first execution`, `0` float literals in AST, `0` empirical values) covering six modules (`R1`–`R6`) and six planted adversarial controls (`PC_REM_1`–`PC_REM_6`).
2. Its raw output `relays/x_rem12_verify/verify_x_rem12_out.json` (`0` float values) and `relays/x_rem12_verify/OUTPUT_SHA256.txt`, committed unread in their own commit strictly before the remediation relay and manuscript overhaul (`origin/main:docs/seats/README.md` §§ `7, 13`).
3. Complete overhaul of `self_consistent_loop/manuscript/main.tex` (with regenerated data-free vector figures, `main.pdf`, and cleaned APS `references.bib`) retracting the unviable `36`-observable ToE / `p_corr` / `"pre-registered"` claims and replacing `main.tex` with a self-consistent, data-free (`0 of 19`) *Physical Review D* Mathematical-Physics & Consistency-Obstructions manuscript uniting the triple-verified `60`-digit Porti adjoint torsion family (`9 / 9` `m129(p, q)` manifolds), exact degree-`5` `m004` cover classification (`8^3_4`), radial $\mathbb{H}^3$ Liouville–Huygens vs Selberg-Jacobian separation, $d$-sheet $f_a/M_{\mathrm{Pl}}$ invariance, repaired `2`-loop `SM` RGEs, CY4 Hirzebruch signature $(b_4^+, b_4^-)$, and the quantitative No-Go obstruction ledger.
4. One formal point-by-point remediation relay `relays/AGY_EXP_TO_AGY002_AND_MAIN_2026-11-22_PEER_AUDIT_REMEDIATION_AND_PATH_A_OVERHAUL.md` and updated `relays/STATUS_AGY-EXP.md`.

## 3. How it could come out wrong, written before any run

- **`R1` (`60`-digit Chevalley vs $\mathrm{Sym}^2$ Porti torsions across all `9` `m129(p, q)` surgeries):** Any discrepancy `> 10^{-44}` between the two Lie-algebra bases, any $|\Delta_{\mathrm{Ad}}(1)| > 10^{-44}$, or any $\mathrm{SL}(2,\mathbb{Z})$ cusp-invariance error `> 10^{-50}` on `m004` would falsify `Gate P11-2`.
- **`R2` (`8^3_4` unique $D_5$ cover & $d$-sheet $f_a/M_{\mathrm{Pl},4}$ invariance):** `m004.covers(5)` must yield exactly one irregular `3`-cusp cover (`8^3_4`, $b_1 = 3$, `torsion == []`, $J = 31$), and symbolic `7D -> 4D` integration must cancel sheet multiplicity $d$ in $f_a / M_{\mathrm{Pl},4}$.
- **`R3` (Repaired `2`-loop `SM` RGEs):** At the synthetic rational point `g = (1/2, 1/2, 1/2)`, `Yu = diag(1/10, 1/5, 1)`, `Yd = Ye = diag(1/20, 1/10, 1/2)`, `lam = 1/10`, the repaired beta functions must agree with exact Machacek–Vaughn / Luo–Xiao / Buttazzo Appendix A to `< 10^{-45}` and pass `SU(3)^5` Haar basis-scrambling to `< 10^{-40}`.
- **`R4` ($\mathbb{H}^d$ Liouville–Huygens vs Selberg Jacobian, `7D` EH vs Adams cusp, & Contino–Pilo loop factor):** Radial $\mathbb{H}^3$ PDE residual must be `< 10^{-48}` (`vs > 1/10` at $d = 2, 4$), $\varepsilon(\gamma_1)/G_{\mathbb{H}^3}(\ell_1)$ must exceed `1` by `> 38%`, `7D` EH vs Adams cusp must differ by `> 6.8x`, and `2[(-\zeta'(0)) - (-\zeta'(0, 1/2))] = \ln\pi` must carry the `1/(2\pi)` loop factor.
- **`R5` (Weierstrass CY4 Hirzebruch signature $\tau(X_8) = 32 + \chi/3$ & self-dual $H^4_+$):** Across $r = 0 \dots 9$, $b_4^+ - b_4^-$ must equal $32 + \chi/3$ with $b_4^- > 0$ (`indefinite Q_4`), and restricting the Euclidean flux ball at $r = 8$ from $b_4 = 2424$ to self-dual $b_4^+ = 1636$ must keep $\log_{10}(\Delta\Lambda_{\mathrm{BP}}) < 0$ at both $R^2 = \chi/12$ and $R^2 = \chi/24$.
- **`R6` (Single-radius `(2 L_c^*)^{10}` obstruction & raw $Z_{\mathrm{SS}}$ divergence):** Consistent radius scaling must shift $V_{\mathrm{Cas}} \propto R^{-10}$ by `(2 L_c^*)^{10} > 6 * 10^8`, and raw `n = 1` Euler products must swing across $l_{\mathrm{cut}} \in [9/5, 33/10]$.

## 4. What it rests on, and what it must not touch

- **Rests on:** `origin/main` (`279459977`) and `origin/agy-002/verify` (`247bd2923`: `relays/AGY002_PEER_AUDIT_AGY_EXP_45FE6E401.md`), while keeping historical Phase `5`–`11` `PREREGISTRATION_PHASE*.md` and `SEAL_SHA256.txt` files untouched per `WORKING_RULES.md` Rules `3` and `9`.
- **Firewall (`must not touch`):** Zero empirical PDG, NuFIT, CODATA, or Planck values (`0 of 19`), zero `61.55` pivot literals, zero shared code imported from `agy-002` or historical Phase `5`–`11` modules.

## 5. Six planted controls that must fail if the work is broken

1. **`PC_REM_1` (`Wrong longitude homological slope on m004`):** Omitting the peripheral cusp modulus $\tau_{\mathrm{cusp}}$ in Porti's meridian change-of-curves formula must miss $2\sqrt{3}$ (`giving 12 instead of 2 sqrt(3)`).
2. **`PC_REM_2` (`Selecting irregular[0] = o10_150703 or multiplying f_a/M_Pl by sqrt(5)`):** Grabbing `irregular[0]` gives `2` cusps and torsion `[2]` (`instead of 8^3_4's 3 cusps and []`), and multiplying $f_a/M_{\mathrm{Pl}}$ by $\sqrt{d}$ breaks $d$-independence.
3. **`PC_REM_3` (`Legacy _rhs76 2-loop bugs`):** Re-inserting `+16 g_3^2 H_e`, omitting `+(5/4) T H_{d,u}`, or truncating `dlam2` must produce non-zero residuals (`> 10^{-5}` and `> 30%` on `dlam2`).
4. **`PC_REM_4` (`Conflating Selberg sinh(r/2) with H^3 Green 1/sinh(r)`):** Substituting `1/(4*pi*sinh(r/2))` into the radial $\mathbb{H}^3$ PDE must give residual `> 1` (`122.4%`).
5. **`PC_REM_5` (`Indefinite full b_4 = 2424 ball at R^2 = chi/24`):** Using $b_4 = 2424$ instead of self-dual $b_4^+ = 1636$ at $R^2 = \chi/24$ must flip $\log_{10}(\Delta\Lambda_{\mathrm{BP}})$ positive (`+172.43 > 0`).
6. **`PC_REM_6` (`Truncated n = 1 Scherk-Schwarz Euler product cutoff swing`):** Varying $l_{\mathrm{cut}} \in \{9/5, 11/5, 13/5, 3, 33/10\}$ on `m129(1,3)` must move $Z_{\mathrm{SS}}$ by a factor `> 2.9x`.

## 6. What is needed from `main` or from another seat

Nothing needed to execute; answers `origin/agy-002/verify:relays/STATUS_AGY-002.md` (`247bd2923`) directly on `origin/agy/self-consistent-loop-2026-11-11`.

`0 of 19.`
