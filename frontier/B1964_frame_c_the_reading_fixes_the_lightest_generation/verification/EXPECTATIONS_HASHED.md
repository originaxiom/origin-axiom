# B1964 — the grid check's SHA-256, recorded before its run

`light_directions.py` states its expectations K1 to K4 at its top. Its hash was taken before it ran.

`lemma.py` is exact symbolic algebra and was not hashed. Its first run printed L5 as False, because main's statement
wrote −2c₁E₁₂ where the matrix is +2c₁E₁₂. The sign was corrected and the docstring says so; the lemma's content, a
scalar multiple, is unchanged. The lock checks the script against this hash.

| script | SHA-256 before the run | UTC | note |
|---|---|---|---|
| `light_directions.py` | `57b04da8df35cfde0892cedbaa6444401fa25ca5234d908e504e9d2d017d783d` | 2026-11-19T09:11:34Z | written after the lemma; before its run |
