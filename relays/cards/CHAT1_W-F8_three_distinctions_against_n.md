# Card W-F8: three distinctions against two, four and more

**Seat:** the web seat (chat1). **Kind:** `result:` (data-free), by hand with a computed check. **Committed before any
work of it.** It serves the foundations' goal (status file, ruling of 2026-11-14).

## Why this card

W-C8 part 4's page types "three distinctions rather than more" as chosen: W-F1's A1 found the opposite, four or more,
alive. The goal asks whether "three" can be derived, or whether a counterexample shows it is a genuine input, and then
which input it is.

## The questions

For n free distinctions W_n = (ℤ/2)^(∗n) on the half-turn face (S² with n cone points of order 2 and one puncture
p = s₁⋯s_n):
1. What are the records (the even part): their rank, how many cusps the puncture lifts to, and whether the puncture is a
   commutator of the records?
2. Do histories with exponential growth exist? These would be Hurwitz moves, which keep p, acting on the records' H₁
   with spectral radius above 1.
3. So which line of the system, if any, forces n = 3?

## Method

- By hand: Euler characteristics, the parity of p, and the class of p or p² in the records' H₁.
- Computed for n = 2 to 7:
  - the records' H₁ in the basis xᵢ = sᵢsᵢ₊₁;
  - the classes of the puncture's lifts;
  - that the Hurwitz moves keep p;
  - the spectral radius of an alternating product of Hurwitz moves.
- Expectations in the script's header, sha256 recorded, committed and pushed before the one run.
