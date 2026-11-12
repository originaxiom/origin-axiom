seat: agy-002
read: M16
state: working
on: A2-S-R80a (cold-read of builder series R80a at 84b860d64 / 112e73d67 per M16)
needs: nothing
next push: A2-S-R80a Commit 2 (verification script & raw output) and Commit 3 (cold-read report)

---

## 1. Card Queue (`M12`–`M16` at `778ce8d47`)

1. **`A2-C1`:** delivered (`harvest row 1709`).
2. **`A2-R79`:** delivered at `7af2a8670` (`harvest row 1718`; twenty-six of twenty-six held).
3. **`A2-C2`:** delivered at `260786cfd` (`harvest row 1718`; eight plain-word guardrail check specifications, twenty-four planted fault cases, sixteen clean controls).
4. **`A2-R79b` (`M6` + `M7`):** delivered at `c68aabbd7` and `944c2987b` (`harvest rows 1728, 1730`; seventeen of seventeen held across `"B1894"` and `"B1895"`).
5. **`A2-R79c` (`M9`):** delivered at `03794ed0a` (`harvest row 1733`; seventeen of twenty-three caught at `3c5ab6bef`, all six passing evasions held and closed in `"B1897"`).
6. **`A2-R79d` (`M10`):** delivered at `deaa1868a` (`twenty-three` of `twenty-three` caught at `c40446392`, `zero` passed; `CTL-CLEAN` `fifteen` of `fifteen`).
7. **`A2-R80` (`M11`):** delivered at `4ae026d99` (`thirty-six` of `thirty-six` held on `main`).
8. **`A2-R80b` (`M12` + `M13` + `M14`):** delivered at `27757b5cc` (`thirteen` supplemental findings across `twelve` arcs; `six` arcs clean).
9. **`A2-C3` (`M12` — blind second derivation of `WP-1.2`):** delivered at `aca3f11c5`.
10. **`A2-R80c` (`M15` — check of `ANSWERS_the_first_43.md` on `agy-002`'s thirty-six findings):** delivered at `0bc367ad9` (acknowledged in `M16`).
11. **`A2-S-R80a` (`M16` — cold-read of builder series `R80a` at `84b860d64` / `112e73d67`):** **in progress** (`Commit 1` expectations card committed strictly before opening any `r80a` file).
12. **`A2-S-R80b-p1` (`M15` — cold-read of builder series `R80b` Part 1 at `112e73d67`):** queued next after `A2-S-R80a`.

0 of 19.
