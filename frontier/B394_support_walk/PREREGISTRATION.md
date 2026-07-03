# B394 (Closure II / M2) — PRE-REGISTRATION: the support walk, the 405 rung

**Committed BEFORE the 405 computation. The data (banked): the m=1 single-seed constant is
exactly 1/4 on four cells of spacing ord/4 at every level; the support residues walk:**

    level 15  (spacing  5):  r ≡ 1  (mod 5)
    level 45  (spacing 15):  r ≡ 1  (mod 15)
    level 135 (spacing 45):  r ≡ 29 (mod 45)   [5-part −1, 9-part 2]

**The fitted rule (registered):** by CRT on the spacing 3^{k−1}·5 — the 3-part follows
(3^{k−2}+1)/2 (giving 1, 2, 5, … at levels 45, 135, 405), the 5-part follows +1, +1, −1
with the registered continuation −1 at 405 (period-4 flip candidate).

**PRIMARY PREDICTION (405, spacing 135 = 27·5, ord 540):** support ≡ 59 (mod 135) — i.e.
cells {59, 194, 329, 464}, every value exactly 1/4.
**Named alternative (if the 5-part flips back to +1):** support ≡ 86 (mod 135).
KILL: neither — bank the actual support (the rule then needs a deeper 3-adic form).

Machinery: numpy F_p singles at 405 (2 primes ≡ 1 mod 1620, small-prime int64 with chunked
matmul — the census_big.py pattern; ζ-coverage verified). Locks from output JSON.
