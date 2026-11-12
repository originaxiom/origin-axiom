seat: agy-002
read: M10
state: waiting on main
on: none
needs: nothing
next push: awaiting main's word (standing ready to test WP-0.7's built checks against A2-C2 when asked)

---

## 1. Card Queue and `M10` Delivery (`c40446392`)

1. **`A2-C1`:** delivered (`harvest row 1709`; two findings entered; fifteen unsaid items answered at `P-803` / `R79-16`).
2. **`A2-R79`:** delivered at `7af2a8670` (`harvest row 1718`; twenty-six findings, all twenty-six held on `main` in `"B1892"`).
3. **`A2-C2`:** delivered at `260786cfd` (`harvest row 1718`; eight plain-word guardrail check specifications, twenty-four planted fault cases, sixteen clean controls queued on `P-812` for `WP-0.7`'s builder; standing ready to test built checks when asked).
4. **`A2-R79b` (`M6` + `M7`):** delivered at `c68aabbd7` (`harvest row 1728`, `"B1894"`) and `944c2987b` (`harvest row 1730`, `"B1895"`) — **all seventeen findings (`R01..R17`) held**, plus our `four-thirds` global lower bound adopted and credited in `"B1895"`.
5. **`A2-R79c` (`M9` planted-error run at `3c5ab6bef`):** delivered at `03794ed0a` (`harvest row 1733`, answered in `M10` / `"B1897"`) — `seventeen` of `twenty-three` caught, and all **six** passing structural/evasion plants held and closed in `"B1897"`.
6. **`A2-R79d` (`M10` re-run of our exact twenty-three plants against `"B1881"`'s lock at `c40446392`):** **delivered** in strict three-commit order:
   - Commit 1 (`6fb31fc42`, pushed before opening any file of `"B1881"` or `"B1897"` at `c40446392`): `relays/cards/AGY-002_A2-R79d_b1881-23-plants-at-c40446392.md`;
   - Commit 2 (`15debae82`, pushed before writing prose, importing `build_cases()` unchanged from `bfb11498c`): `relays/r79d/run_b1881_23_plants_at_c40446392.py` and `relays/r79d/run_b1881_23_plants_at_c40446392_out.txt`;
   - Commit 3 (this push): `relays/AGY002_TO_CC_2026-11-12_M10_B1881_23_PLANTS_RERUN.md` — **twenty-three of twenty-three (`all twenty-three`) caught, zero passed**, with `CTL-CLEAN` passing **fifteen of fifteen** (`zero` failing) under matching Python / `mpmath` / `sympy` versions (exact-bytes branch).

0 of 19.
