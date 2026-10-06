# B1484 — ONE OBJECT GATES BOTH NEAREST APPROACHES: the weak-mixing-angle crossing needs the colour triplet split from the Higgs doublet, no flat line can do it on any state, and that is the same missing frame the chirality count needs

**Verdict: PROVED** — for three arithmetic statements (§1), general in their stated hypotheses. What they imply for the
programme (§2) is a reading of the record against them and is stated as such. Scope: frame none (one-loop running by
field content; the weights of the 27 of E₆); reach general; hypotheses: one-loop, a single unification scale, matter
kept or removed by its invariance under flat abelian lines. cc (main), 2026-10-07. Not sealed: nothing here is a
prediction — the numbers were computed once as a pre-check of the crossing plan's second option and are landed so they
are not lost. The measured inputs are data, cited as data. **0 of 19.**

## 0. Seen first, and literature

`VERDICT topic-sweep /unification ratio|doublet.triplet|triplet split|b_1|beta coefficient|desert/: 21 of 1356 arcs on main match (NEGATIVE 6, OPEN 2, PROVED 13)` — read at the level of the verdict lines, and in the FINDINGS for B298, B299, B987, B1206: **the record already knows the doublet–triplet problem and has placed it.** B298: "the doublet-triplet split is *external* (needs a color choice)"; B299: the split "requires choosing which SU(3)"; B987: the 10 contains "both the Higgs doublets and two colour triplets. Splitting them — doublets light, triplets superheavy — is the classic GUT doublet–triplet splitting problem"; B1206 and B952 repeat it ("a 1e14 tuning, unsolved in minimal models"). On the crossings: B915 (the desert, MISS at 16σ), B1244 and B1245 (its kill is scoped to "object boundary + pure SM desert"; "the 16-sigma desert miss is group-independent by construction"), B925–B927 (internal thresholds and a Pati–Salam enlargement with a tuned scale, killed). On the SM seat's line, verified in B1303: "none of Y₉'s 706 464 Standard-Model Wilson lines projects out a single colour triplet D — by theorem, because w_D = −2 w_Q" and "exactly one light Higgs pair, one light colour-triplet pair". **What is not on the record and is added here:** the ratio by spectrum with its coefficients derived (§1 S1), that the triplet identity is a fact of the 27 and so holds on every state (S3), and the link from the split to the frame of the right parity (§2). The other matches (B655, B884, B897, B1009, B1209, B1216, B1295, B1334, B1453) use the words in other senses or in bodies I did not open. **Literature:** the one-loop
coefficients are textbook; **they are derived here from the field content** (`verification/unification_ratio.py`
reproduces (41/10, −19/6, −7) and (33/5, 1, −3) from the representations), per the owner's rule of 2026-10-06. That a
supersymmetric spectrum with split Higgs multiplets unifies is the classical observation of the early 1990s; it is
reproduced here, not claimed.

## 1. The three statements (`verification/unification_ratio.py` → `unification_ratio.json`)

**S1 — the ratio.** If the three gauge couplings meet at one scale, then at any lower scale
(1/α₂ − 1/α₃)/(1/α₁ − 1/α₂) = B := (b₂ − b₃)/(b₁ − b₂), whatever the meeting scale and the coupling there.

| spectrum between the meeting scale and M_Z | (b₁, b₂, b₃) | B | α_s(M_Z) it implies |
|---|---|---|---|
| **measured** (1/α_em = 127.95, sin²θ_W = 0.23122, α_s = 0.1180) | | **0.7172** | 0.1180 |
| the Standard Model alone — the desert of B915 | (41/10, −19/6, −7) | 115/218 = 0.5275 | 0.0711 |
| supersymmetric, Higgs doublets light and colour triplets heavy | (33/5, 1, −3) | 5/7 = 0.7143 | 0.1168 |
| supersymmetric, one light Higgs pair **and** one light colour-triplet pair (a complete 5 + 5̄) | (7, 1, −2) | 1/2 | 0.0673 |
| supersymmetric, three complete 27s light | (9, 3, 0) | 1/2 | 0.0673 |

**S2 — complete multiplets are invisible to the ratio.** A complete 5 + 5̄ adds (1, 1, 1) and a complete 10 + 1̄0̄ adds
(3, 3, 3) (per chiral pair: ½ and 3⁄2 each): B depends only on the gauge sector and on *incomplete* multiplets. With the
gauge sector alone, B = 3/6 = ½.

**S3 — the triplet's weights.** Under the three abelian directions of E₆ that commute with SU(3) × SU(2) — Y, χ, ψ — the
quark doublet has weights Q = (1/6, −1, 1) and the colour triplet D = (−1/3, 2, −2) = **−2·Q**; the Higgs doublet
H_u = (1/2, 2, −2) differs from D only in Y. So every character of that torus trivial on Q is trivial on D.

## 2. What follows (a reading of the record against §1)

- **B915's miss was the desert's, not the boundary's.** The record's boundary value sin²θ_W = 3/8 with a spectrum whose
  Higgs multiplets are split gives 0.7143 against 0.7172 measured. That is the classical supersymmetric result, so it is
  *reproduced, not predicted*; what the programme would have to add is a *derivation of the split*.
- **The split is what the record has called "external" since B298** — the classic doublet–triplet problem (B987).
  §1 says what it is worth: the whole distance between 0.5 and 0.714.
- **The record's own closing does not split.** Its light content is "one light Higgs pair, one light colour-triplet
  pair" (sm:B1283, verified in B1303): a complete multiplet, B = ½, a miss as large as the desert's, at any scale.
- **No flat abelian line splits it on any state.** sm:B1300's reason, "w_D = −2 w_Q", is S3 — a fact about the 27, not
  about the closing Y₉ or the member m004. Wherever matter survives by being *invariant* under flat lines, a line that
  keeps Q keeps D. *Scope, said plainly: abelian lines in the torus commuting with SU(3) × SU(2), matter kept by
  invariance. Not covered: non-abelian lines, a mass for D from a coupling, and any frame in which matter is counted by
  an index.*
- **So the weak-mixing-angle crossing is gated by the same object as the chirality count:** a frame in which matter is
  *counted by an index* rather than *kept by invariance* — a bulk of dimension ≡ 2 (mod 4) with a bundle that is not flat
  (GENESIS GAP6, v1.12). In such a frame the survival of Q does not require w_Q = 0, and S3 no longer ties D to it.
  This is lead **L250**.

## 3. Disclosed

One loop; thresholds, two-loop terms and the value of the supersymmetric scale move 0.7143 by amounts comparable to its
distance from 0.7172, so "0.714 against 0.717" is agreement at the level of the approximation, not a measurement of
anything. The measured inputs are quoted, not derived. §2 is a reading: it uses sm:B1283's light content as banked.
