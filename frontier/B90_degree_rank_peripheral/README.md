# B90 — the uniform peripheral reduction of degree=rank (Task 1b)

Makes the **peripheral mechanism** of degree=rank (`[A,B]=(−1)ⁿ⁻¹μⁿ`, B77) explicit and **uniform in n**,
reducing the all-n proof to one clean collapse-lemma.

- **`probe.py`** — verifies **Lemma 1** (proved uniform, from the bundle relations):
  `λ=[A,B]=μX⁻¹μY⁻¹` and `XμX⁻¹=μA` (`X=AμA⁻¹`, `Y=A⁻¹μA`) on bundle reps at n=3,4, plus the collapse
  `λ=(−1)ⁿ⁻¹μⁿ` (`c=+1` at n=3, `−1` at n=4).
- **`FINDINGS.md`** — the derivation, the reduction, and "why exponent = rank" (A's degree-n
  Cayley–Hamilton).

**Result.** The longitude is the explicit cusp word `μX⁻¹μY⁻¹`, and the bundle gives the clean
conjugation law `XμX⁻¹=μA` — both **proved uniformly** (L1b verified exactly over ℚ(ω)). degree=rank for
all n is then exactly the **collapse-lemma** `L1a+L1b+deg-n min-poly(A) ⟹ λ=(−1)ⁿ⁻¹μⁿ` — PROVED n=3
(B71), n=4 (B89); the exponent = rank because A is an n×n matrix.

```bash
python frontier/B90_degree_rank_peripheral/probe.py
python -m pytest tests/test_b90_degree_rank_peripheral.py -q
```
No Origin-core claim; proven core P1–P16 untouched.
