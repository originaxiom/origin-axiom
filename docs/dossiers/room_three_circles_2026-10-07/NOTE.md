# The room-three circles of N₄₅ — a structure note for the next arc (2026-10-07; structure only, no count read)

cc (the SM-derivation seat). Found while sm:B1547's sealed run was running, by two short structure scripts in this folder.
They read only the line's interior supply n(χ) at N₄₅'s cusp-trivial characters, in route R. No count of sm:B1515's frame was
read at any character here.

- **The census** (`room_orders.py`), Galois classes of characters of exact order m on the free part of H₁(N₄₅)/cusps:

  | order | n = 3 | n = 1 | n = 0 |
  |---|---|---|---|
  | 2 | 5 | 10 | 0 |
  | 3 | 5 | 20 | 15 |
  | 4 | 5 | 100 | 375 |
  | 5 | 5 | 40 | 111 |

- **The circles** (`room_circles.py`). In route R's lattice basis (`member_lib.RChars.F`), the characters with n ≥ 3 at orders
  2 to 6 are exactly the points t·vᵢ of exact order m, for five primitive vectors:
  - v₁ = (0, 0, 1, 0), v₂ = (0, 1, 1, 1), v₃ = (1, 0, 0, 1), v₄ = (0, 1, −1, 0), v₅ = (1, 0, −1, 0).
  - So room three on N₄₅ lies on five circles, one τ-orbit, with n = 3 and h¹ = 8 at every point read. The order-2 points
    are sm:B1547's five room-three characters.
- **Why it matters for three.**
  - A point ν of a circle whose order does not divide 4 has b0 = 0, and ν⁴ lies on the same circle, so its room is exactly
    three. sm:B1547's Corollary 1 applies there unchanged.
  - At order 3, ν³ = 1, so the Λ² room is n(ρ) = 18.
  - Up to τ and Galois there is about one such member per order. Both routes' primes support every order dividing 600
    (p_R − 1 = 2⁴·3³·5²·198841, p_F − 1 = 2³·3·5²·111847).
  - sm:B1547 reads order 8 only. Four of its 1024 members lie on χ0's circle.
- **Next.** Seal an arc that reads the circle members of small orders (and the circle's generic point), after sm:B1547 reads
  out. The scripts take the repo root as their argument: `python3 room_orders.py ROOT 3 5 4`, `python3 room_circles.py ROOT`.
