# B1815 referee (hostile, read-only, 2026-10-29) — saved by main from the referee's hand-back

**Verdict: PASS WITH CORRECTIONS.** The theorem ν_p = (1−p)M + pF₊M is correct. It was checked:
- line by line;
- by an exact rational test (exact_stationarity.py): the defect is identically 0 at p = 0, 1/10, 1/3, 1/2, 3/4, 9/10
  and 1; the moved-side control gives 0.05; the unequal-pair walk fits no side weight;
- by an independent exact-integer simulation up to p = 1 (walk_exit_fixedK.py): P(Im τ > 2) 0.1666–0.1683 against
  0.1676, and P(Im τ > 3) 0.0343–0.0351 against 0.0346.

**Main's verification:** exact_stationarity.py regenerated on main identically (main_rerun/). The brane and parity
refutations were recomputed by main.

## Required (applied in B1815's FINDINGS)
1. "The record's adopted dynamics" overclaims: GM5b adopts legality of inverses, not a walk or weights, and B1663 § 3
   firewalls the walk. It is the record's walk model, a firewalled reading.
2. The walk gives an endpoint law; the τ-law needs the arclength placement (CHOSEN). Every X_n(i) is Γi.
3. "No longer a continuum" is false: unequal pairs give Denjoy laws, and the s-family remains.
4. The bracket:
   - B1704's 89–95 was misused (trivial fermions hold τ at i or on the unit arc; 89–95 scalars hold it in the band only
     without gauge fields; 595–672 with them; 689–780 with the graviton);
   - "only the continuous measures sit between" is false;
   - it is a READING, and the potential is W62's frame at the half-period line.
5. The brane bullet: K_[0,1] = R and K_[1,0] = L⁻¹, but L is conjugate to no K_[p,q], so word length does not count
   branes. P-482's statement is false.
6. The quarter by word length alternates with the parity of the cut: even cuts 0.318–0.327, odd cuts 0.172–0.176. No
   limit.
7. The provenance of the KS rerun at p = 0.75; why it was rerun.
8. § 5 should carry P-180's contradiction, THE_WEAVE's gloss and the costs (§ 320, W57).

## Recommended (applied)
- **Uniqueness:** the support generates the group at every p.
- **M's digits:** a₀ can be 0.
- **A shape control:** the unequal-pair walk.
- **"B1663's T2 and T4(b)"**, not "its sealed results".
- **Check 5's bridge sentence.**
- **T2(a):**
  - T's slope is built in;
  - any element outside SL(2, ℤ) already excludes Minkowski's class (x + 1/3: digit-1 frequency 0.415, mean 5.54).
- **T3:**
  - cite the wide sweep and B169's isomonodromy flow;
  - Fenchel–Nielsen and earthquake flows preserve Weil–Petersson.
- **"At least two" metrics**, with the WP estimate π²/Y³.
- **Seen first:** P-469, P-474, P-477, P-480, B21.
- **"Our depth"'s source.**
- **The Guivarc'h–Le Jan attribution wording.**
- **The length bias reaches B1663's ray averages** (about −0.35%).
- **"Cubically"** only with its units.

Scripts and outputs are beside this file.
