# B1840 — DECLARATION: THE PRINCIPLED ENDS, fixed before B1839's look is read (P-685)

cc (main), 2026-11-05, at the owner's word ("its important that were prepared for a closure").

**Committed and pushed before main reads any output of B1839's `look.py`.** At this commit B1839's census is running;
its look has not run.

## Why

B1839's read-out 5 will show the data's minimum χ²_six at each of 23 cut levels. If THE END CARD fails, the next step is
to derive the level rather than choose it, and a derivation stated after that profile is seen is a look-elsewhere choice.
So the levels that count as derived are fixed here, by a principle and a formula, with no data. The web seat is asked for
its own list under the same rule (`docs/handoffs/CC_TO_CHAT1_2026-11-05_PREPARE_THE_CLOSURE_THE_PRINCIPLED_ENDS.md`).
Entries it commits before main reads B1839's look join this list as E4 onward, with their commit named in a dated note.

## The ends (L_h is the horoball level of B1667's geometry at the reduced τ)

| entry | L_h(τ) | the principle |
|---|---|---|
| E1 | L₂(τ), B1667's `geometry()` | B1667's canonical cusp: the collar lemma's length-2 horocycle, one of the fibre's two canonical cusp neighbourhoods (P-266's reason, on record; LAW_MAP, "THE CANONICAL CUSP"). |
| E2 | ln 2 | The largest round disc about the puncture that the Dirichlet cell holds: its inradius is ½ (B1838 § 2b). This is the shallowest end at which the small-cut expansion's own disc is embedded. It is entered under P-266's reopening clause, with this rule stated. Since L_max < ln 2 at every apex (0.6445–0.6562 in B1839's census), the horoball there is embedded too. |
| E3 | L_max(τ) | The maximal embedded horoball (δ = 0). It is already B1839's read-out 2 and is listed so that the family is complete. |

**Not entered, with the reason:**
- **The density Higgs's cancelling radius** G₂^{−1/2} = 0.551 (the web seat's POST HOC 2): e^{−L} = 0.551 exceeds
  e^{−L_max} ≈ 0.52, so no embedded horoball has it. It concerns the principal value's constant, not the norms.
- **The zeta-regularised end** (the agy lane's Theorem 81): its scale constant is degenerate with L (B1838 § 2b). Its
  honest normalisations, γ + log π − ½ log Im τ and γ − log 2, are not horoball levels of this geometry.

## How the list will be used

- **A later sealed card** re-reads the six at each entry's exact norms. It uses B1839's instruments (its split quadrature and
  Higgs-twist class cache) with L_h set by the entry's formula, under B1839's matched null with the end fixed per entry.
  The K entries are priced in the null: each target chooses its best entry.
- **That card is written after this list closes,** and before any of its entries' norms are computed.
- **If B1839 passes** with a fitted δ*, the same card asks whether δ* coincides with a principled entry. That is what would
  turn the joint from FITTED into derived.

## Seen first

- `VERDICT topic-sweep /principled end|canonical end|cut level|collar|inradius|length.2 horocycle|derived end/ (full text): 21 of 1586 arcs on main match (NEGATIVE 6, OPEN 1, PROVED 14); 24 register rows match (DECLINED 1, DONE 19, QUEUED 4)`.
  It turned up P-266 (DECLINED). Its reason states that the fibre's canonical cusp neighbourhoods are the maximal embedded
  horoball and the collar lemma's length-2 horocycle (E3 and E1). It declines B486's 2√3, the 3-manifold's longitude and
  not a horocycle of the fibre, and reopens only for a rule that names a third canonical end. E2 is entered with its rule.
  It also turned up P-433 (B1691's ω table at the canonical end radius) and P-481 (B1816's Weil–Petersson clock).
- B1838 (§ 2b: the inradius; L₂ − L_max = π(1 − 2/A_cusp); the zeta end);
- B1667 (L_max, L₂);
- B1839 (the card; its δ grid);
- the web seat's POST HOC 2 (B1837's dated note of 2026-11-05);
- P-421, P-402 (L₂ small-cut, χ²_six 30.6 on record).

## Disclosed

- **Known before this list:** the small-cut L₂ gives χ²_six 30.6 (P-402), and at L₂ the exact norm is within 0.6% of the
  small-cut form (B1838 § 2b). So E1's six are close to foreknown as poor. It is listed because the principle, not the
  outcome, decides entry.
- **Not computed and not read:** no χ²_six at any exact end other than the web seat's reproduced E2 rows. Nothing of
  B1839's look.

> *Dated note 2026-11-05 (S305c): the list closes. The web seat's list was committed before B1839's look ran
> (`relays/chat1_2026-11-05_ends/principled_levels.py` 4e22173b2 → output 8fec64340 → relay 046946dfc, on
> `origin/chat1/web-seat`), re-run by main on its tree to every printed digit (residuals at 10⁻¹¹–10⁻¹³ aside;
> `audit/chat1_s305b/`). It confirms E1–E3 and adds:*
> - ***E4: L₄ = L₂ − π/2, the area-4 horocycle*** *— the largest cusp neighbourhood every torsion-free Fuchsian group embeds:
>   the traces of Tⁿγ step by λ∣c∣ and must miss (−2, 2), so λ∣c∣ ≥ 4 and the horoball of area 4 (h = λ/4) is embedded; the
>   thrice-punctured sphere attains it. Main re-derived the bound by hand and the formula from B1667's convention
>   L = (2π/λ)(h − Im B): δ₄ = L₄ − L_max = π(½ − 2/A_cusp) ≥ 0 exactly because A_cusp ≥ 4. Entered as E4.*
> - *E3 read anew: the maximal horoball's boundary passes through a half-period (the rotation by π about it swaps the two
>   tangent horoballs), so L_max = ln 2 − Re g(½) where ½ is the contact (to 1.7 × 10⁻¹¹ at B1667's 54 points; ½ is the
>   contact at 53, (τ − 1)/2 ties at ω) — E2 and E3 are one principle, the cut through the nearest half-period, flat and
>   hyperbolic.*
> - *A correction to main's relay: the cancelling radius is 0.525–0.564 at B1667's points (0.551 is its large-Im τ limit
>   √3/π); L_c < L_max at all 54, so the exclusion stands.*
> - *Excluded by the seat, as here: the zeta end; the per-channel equality levels (three depths matched to the ansatz);
>   any one-loop stationary level (none on record with its scale fixed by the geometry).*
>
> ***Disclosed for E4:*** *at B1839's 223 apexes (its census's accessory geometry, data-free) δ₁ = 1.665–1.782, δ₂ =
> 0.037–0.049, δ₄ = 0.094–0.211. δ₄'s range overlaps where B1838 § 2b's per-channel equality levels put a single cut
> (about 0.16–0.30 above L_max), which was computable before this list; E4 is admitted on its theorem, not its place. The
> list is closed at four entries (K = 4); main reads B1839's look only after this note is on origin.*

