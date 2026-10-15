# The twisted thread-frame instrument (exploration, unsealed; excluded orders only)

`twisted_explore.py` carries B1656's twisted coupling vector along a thread in W72's and THETA2's cells, in the minimal
reading (matter and Higgs modes untwisted). It needs `forms.pkl`, which `build_forms.py` writes (W72's forms, as
LIFT builds them; about 14 minutes). Absolute paths are replaced by `<repo>` and `<scratch>` (WORKING_RULES §11).

**How it works.**
- The twisted vector is computed at the unreduced point of the thread's period, from theta constants of rational
  characteristic summed as series in τ.
- It is carried to the reduced point by the monomial map that carries B1654's R. The permutation comes from the
  tracked moves (T swaps j and k; S swaps i and j), and the factors are read off R itself.
- The first version matched channels by modulus. That cannot separate θ₃ from θ₄ high in the cusp, and it broke
  closure there. It was fixed before any use.

**Validation (`twisted_explore_run.txt`, `validate2_run.txt`):**
- **zero twist:** it reproduces THETA2's stored m₂/m₃ on LR and LLR in four cells to 10⁻¹³. Its R equals W72's R to
  10⁻¹⁵, and the transport factors satisfy |f| = |J|^(−1/2) to 10⁻¹⁵;
- **closure on closing lines:** 10⁻¹¹ (L·R²⁵, N = 5) and 10⁻¹⁴ (L·R⁹, N = 3);
- **the negative control:** a line the thread does not fix fails closure at 0.9995.

**The limitation found (`dbg2`, `dbg3`, `dbg4` and their runs).**
- At N = 5 on L·R²⁵, the down and lepton coupling vectors agree to 10⁻¹³ at every point, yet the integrated Yukawas
  differ by 46%.
- The cause is catastrophic cancellation in double precision at heights around 13: the matter forms span about 30
  orders of magnitude there.
- So this instrument is sound only for y ≲ 3–5, which is LIFT's range.
- The deep-cusp tower that the record's action favours (height N²/2: 13 at N = 5, 41 at N = 9) needs either
  arbitrary precision (W84 used 60 digits up to y = 4.9; y = 41 needs well over 100) or the analytic leading-exponent
  route, the cusp texture itself.

No N = 9 or N = 11 quantity was computed.
