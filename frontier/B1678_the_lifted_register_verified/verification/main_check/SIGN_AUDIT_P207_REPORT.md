# P-207 sign audit: M_of (pointwise lift) vs the multiplicative lift, per arc

Method. A sandbox copy of the frontier arcs (`sb/`, repo untouched) with `M_of` in B1617's module replaced (env switch) by the
multiplicative lift: for any automorphism that is a word in L, R, L^-1, R^-1 (all words to length 7 tabulated, consistency
asserted), M = (+/-) M_of such that M equals the product of the letters' lifts (compose order f = x1 o x2 -> M_x2 M_x1, the order that
reproduces M_of up to sign). Every script of the eight arcs that touches M_of was re-run in this mode (`run_all.sh`,
`out/mult/`) and its JSON compared to the stored one (`cmp.py`). Baseline mode reproduces all 12 stored JSONs byte-for-number
(`out/orig`, `cmp.py stored out/orig`). Automorphisms that are not words (iota, conj(a), conj(b)) have no multiplicative lift; for them
see section "Inner automorphisms and iota".

## Sign of M_of against the multiplicative lift, per composite used (T, 3x3)
| automorphism | word | M_of vs letters | where used |
|---|---|---|---|
| U (H1 = [[0,-1],[1,1]]) | l R | + | B1617 (weave_at_omega.py:69-90), B1618 (weighted_at_omega.py:30-33, post_seal_odd_weight.py:24-26) |
| LR = compose(L,R) | L R | + | B1621 clock_and_tick.py:50 |
| S~ = R L^-1 R (H1 = [[0,-1],[1,0]]) | R l R | **-** | B1630 weave_at_i.py:53-64, post_seal_generic.py:20-22; B1632 w45_on_main.py:54-56, post_seal_projective.py:25-26; B1634 w50_on_main.py:82, post_seal_w50.py:279 |
| H1 = I words (Delta^4 = conj(c) etc.) | any | + (B1634 P2: 2336 words, all agree) | B1634 w50_on_main.py:58, post_seal_w50.py:109,137 |
| H1 = -I words (2 automorphisms) | any | **-** (B1634 P2: turns 1/4 vs 3/4 swapped) | B1634 post_seal_w50.py:137 (diagnostic only) |
| L, R | single | + | all |
Random check (`pairs_check.py`, `pairs_check.log`): M_of(fg) = -(M_of(g) M_of(f)) in 62 of 200 random pairs of positive words (the finding's 55
of 200 up to the sample), and M_of(word) = -(letter product) for 100 of 200 random positive words: the sign is real and frequent, but it is
trivial on U, LR and every H1 = I word, and non-trivial on S~ and the H1 = -I words.

## Inner automorphisms and iota (not words in L, R)
conj(a), conj(b), iota are lifted directly by M_of in B1617, B1618, B1620, B1621, B1630, B1634, B1641. Findings (`conj_relations.py`):
* The signs of M_of(conj a), M_of(conj b) are **pinned** by coherence with the letter lifts: M_L^-1 I_a M_L = I_a, M_L^-1 I_b M_L = I_b I_a,
  M_R^-1 I_a M_R = I_a I_b (= I_b I_a), M_R^-1 I_b M_R = I_b, all with sign +. Flipping I_a or I_b (either, or both) breaks one of them
  (I tested the flips as scenarios anyway, `out/f_inn_a_inn_b`, `summarize_flips.txt`: they relabel the line characters (-,-) -> (+,+),
  move the clock's mean in B1621 K3 from 7e-7 to 1.0, and change K in B1620, so they would change results; they are not coherent lifts, so they are not alternatives).
* Flipping iota changes nothing in any output except a bookkeeping index in B1620 post_seal_inner (sign_index 93 -> 84); B1617, B1618 identical.
* Not a section though: M_of(conj a) M_of(conj A) = -1 on V (the inverse letter is lifted with the opposite sign), and
  M_of(conj a) M_of(conj B) M_of(conj A) M_of(conj b) = +1 on T whereas M_of(conj(aBAb)) = word lift of Delta^4 = -1 (`b1641_check.py`). This
  is the central extension B1641 reports (spinorial around the commutator loop); it is a property of the lift, not of the M_of sign choice.

## Per arc
| arc | call sites of a composite lift (file:line) | sign-sensitive? | recomputed (multiplicative lift) vs stored | grade |
|---|---|---|---|---|
| B1617 | weave_at_omega.py:69 M_of(compose(L,R)) (Z0 check, not banked beyond a boolean); :90 U (word lR); iota/inn_a/inn_b single | no. U is + ; group order 48, T irreducible, chi_U = 0, U eigen-turns {1/4, 7/12, 11/12}, Z3 spectra | weave_at_omega.json IDENTICAL | UNAFFECTED |
| B1618 | weighted_at_omega.py:30-33, post_seal_odd_weight.py:24-26: U = compose(Linv,R) or compose(R,Linv) (whichever has H1 = [[0,-1],[1,1]]) | no (U sign +; eigenspaces taken at every 24th-root phase, a ± symmetric set) | weighted_at_omega.json, post_seal_odd_weight.json IDENTICAL | UNAFFECTED |
| B1620 | post_seal_inner.py:24 index_of(single inner automorphisms / iota); no composite | only through iota's label index | post_seal_inner.json IDENTICAL (iota flip: sign_index only) | UNAFFECTED |
| B1621 | clock_and_tick.py:50 T_of(compose(L,R)); :49 inner singles | no. T(LR): + ; eigenvalues {1,w,w^2}, rank-one mean | clock_and_tick.json IDENTICAL | UNAFFECTED |
| B1630 | weave_at_i.py:53-64 S (word RlR found by search), post_seal_generic.py:20-22 S~ = compose(compose(R,Linv),R) | partly. S~ carries the opposite sign: S's eigen-turns on T are moved by 1/2 | weave_at_i.json: Z4 S_eigen_turns_on_T [3/8,3/8,7/8] -> [3/8,7/8,7/8] (order 8 unchanged); everything else (Z1 order 32, Z2 clock line (-,-), Z3 cells, 1+2 pattern) and post_seal_generic.json IDENTICAL (cells run over all S-eigenvalue phases) | AFFECTED-BUT-RESULT-STANDS (FINDINGS Z4 "eigen-turns 3/8, 3/8, 7/8" becomes 3/8, 7/8, 7/8; the Z4 claim "S of finite order, order 8" and the verdict stand) |
| B1632 | w45_on_main.py:54-56 Sa = compose(compose(R,Linv),R), M_of(Sa); post_seal_projective.py:25-26 | yes. S~ sign | w45_on_main.json: C1 valid identifications 0 of 8 -> 4 of 8 (S2 = (ST)^3 True for identifications 0,3,5,6), C2/C3 become computable (e.g. chi_{3/2} = 0 for rho, T eigen-turns 1/8, 5/8, 7/8); post_seal_projective.json: only D1 scalar turns move; D2 rescaling counts and chi_{3/2} in {0,1} (five zeros, one 1) IDENTICAL | RESULT-CHANGES: sealed C1 "none of the eight identifications satisfies the Mp2(Z) relations exactly (projective only)" -> "four do". Already on the record: B1632 ADDENDUM 2026-10-09 / B1634 P6 / B1655; the claim_one_line carries "[REFUTED IN PART by B1634]". chi values stand |
| B1634 | w50_on_main.py:58 (f of every word with H1 = I, to N_MAX), :82 Sa; post_seal_w50.py:109,137 (H1 = +-I words), :279 S~ | yes for S~ only. V2 scalars (H1 = I, + sign) unaffected | w50_on_main.json: V3 equivalences alpha_48ths 36 -> 12 (four rows) and 24 -> 0 (four rows), i.e. the half turn; V1, V2, all other fields IDENTICAL. post_seal_w50.json: P6 "M_of_sign_vs_move_product" S~ "-" -> "+" (the self-diagnosis) , rest IDENTICAL | AFFECTED-BUT-RESULT-STANDS: the sealed V3 alpha for the S~ identifications moves by 1/2 turn; B1634 itself disclosed it (P6, FINDINGS "the sealed instrument inherited the error"), and its banked claim rests on the post-seal word-lift computation, which is unchanged |
| B1641 | w46_on_main.py:84-85 lift_of + W.move_matrix of conj(a), conj(b), conj(aBAb) (does not call M_of; its own lift_of path) | partly. a, b: sign pinned by coherence (above); conj(aBAb) = Delta^4: M_of -1 = word lift -1 (agrees), letter-product of inner lifts +1 | w46_on_main.json IDENTICAL (my patch does not reach this path; recomputed separately in `b1641_check.py`: word lift of Delta^4 on T = -1, M_of(conj c) = -1, product of the four inner-letter lifts = +1 = the geometric lift) | UNAFFECTED as banked (-1 vs the geometric +1 is the genuine central sign of the extension). Wording note: "the record's uniform lift acts on Delta^4 by -1" is right for the lift of the automorphism / the L,R word; the inner-letter product gives +1 because the inner lifts are not a homomorphism with the L,R lifts (the obstruction itself) |

## Summary
* RESULT-CHANGES: B1632 C1 (0 valid -> 4 valid identifications), already corrected in the record by B1634/B1655 (verdict "NEGATIVE as sealed" is the sealed instrument's output).
* AFFECTED-BUT-RESULT-STANDS: B1630 Z4 eigen-turns (3/8,3/8,7/8 -> 3/8,7/8,7/8), B1634 sealed V3 alpha (half turn; disclosed in B1634 P6).
* UNAFFECTED: B1617, B1618, B1620, B1621, B1641.
* Not covered: words longer than 7 letters are not tabulated in the patch (B1634 P2 checked length 12 for H1 = +-I). Arcs outside the eight (e.g. downstream citations of B1630's 3/8,3/8,7/8) were not scanned.

Files: `common.py`, `run_all.sh`/`run_all2.sh`, `cmp.py`, `summarize.py`, `conj_relations.py`, `b1641_check.py`, `pairs_check.py`; outputs `out/{orig,mult,f_iota,f_inn_a_inn_b}`, `summarize_flips.txt`, `pairs_check.log`. The sandbox `sb/`, `sb2/` are patched copies of the frontier arcs.
