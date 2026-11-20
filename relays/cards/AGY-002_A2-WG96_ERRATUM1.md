# AGY-002 Erratum 1: Card A2-WG96 Producer v1 Execution Failure and v2 Remediation

- **Card:** `AGY-002 / A2-WG96` (`relays/cards/AGY-002_A2-WG96_ej5-mapping-class-family-modes-vs-weave-g96-triplet.md`)
- **Superseded Producer Artifact:** `relays/a2_wg96/verify_a2_wg96.py` (commit `380a50c54`, untouched)
- **Replacement Producer Artifact:** `relays/a2_wg96_v2/verify_a2_wg96_v2.py` (fresh custody directory; `v1` left sealed and unmodified)

## Defect Found During Execution of Sealed Producer v1

Immediately after sealing `relays/a2_wg96/verify_a2_wg96.py` (`380a50c54`) and running `python3 -B relays/a2_wg96/verify_a2_wg96.py`, execution aborted before producing `verify_a2_wg96_out.json` due to three implementation defects in `v1`:

1. **Missing `import cmath` and allowlist entry:** `v1` referenced `cmath.exp(...)` inside the `SL(2, Z)` / `B_3` unitary lifting helper without importing `cmath` at module top or listing `"cmath"` in `check_ast_and_custody`'s allowed module set (`NameError: name 'cmath' is not defined`).
2. **Wrong `mpmath` Hermitian eigensolver call:** `v1` called `mp.eigsy(G_sum)` inside `eval_sec_Y_G`, which only supports real symmetric matrices; for complex Hermitian Gram matrices `Y_w * Y_w^H`, `mpmath` requires `mp.eighe(G_sum)`.
3. **Module docstring escape:** `v1` used a non-raw triple-quoted docstring containing LaTeX brace escapes (emitting a Python `SyntaxWarning`).

## Disposition

- Keep `relays/a2_wg96/verify_a2_wg96.py` and `relays/a2_wg96/SCRIPT_SHA256.txt` untouched at commit `380a50c54` (no `verify_a2_wg96_out.json` exists in `relays/a2_wg96/`).
- Seal `relays/a2_wg96_v2/verify_a2_wg96_v2.py` under fresh commit-before-run custody with:
  - `r"""..."""` raw module docstring;
  - `import cmath` and `"cmath"` added to `check_ast_and_custody` allowed imports;
  - `mp.eighe(G_sum)` replacing `mp.eigsy(G_sum)` for complex Hermitian Gram matrices.
