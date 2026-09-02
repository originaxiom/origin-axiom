"""B333's genericity count: fundamental discriminants in [-399,-3] with class number 2, by PARI (cypari2) --
independent of B333's own fundamental_discriminants() filter (fc R36: sign bug)."""
from snappy.pari import pari

fund = [D for D in range(-3, -400, -1) if pari.isfundamental(D)]
h2 = [D for D in fund if pari.qfbclassno(D) == 2]
print(f"fundamental discriminants in [-399,-3]: {len(fund)}; with h = 2: {len(h2)}")
print("h=2 list:", h2)
print("h(-15) =", pari.qfbclassno(-15))
print("B333's '14 of 123' reproduced:", (len(fund), len(h2)) == (123, 14), "| PARI gives", (len(fund), len(h2)))
