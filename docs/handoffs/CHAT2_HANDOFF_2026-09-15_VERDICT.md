# CHAT-2's HANDOFF (2026-09-15) — main's verdict, positives and negatives verified

*Received 2026-09-15 as `chat2_handoff.zip` (sha256 `37ce67c012f3f427…`, seven files), archived beside this file under
`chat2_handoff_2026-09-15/` with main's own `sign_check_exact.py`. Owner: "verify, both positives and negatives; don't
let anything important slip just because the seat was misinformed." Every number below was recomputed here.*

## 1. The two items the seat flagged

**The sign check (R4b) — VERIFIED, conclusion holds with larger margins.** Chat-2's script counts each 16 of SO(10) as a
Dirac pair (it is one Weyl multiplet), counts the complex scalar twice, and approximates the SO(8)/SU(4) branching.
Recomputed with exact branching (16 → 8_s + 8_c; 8_s, 8_c → 4 + 4̄; 4 → 3 + 1; 10 → 8_v + 1 + 1 → 6 → 3 + 3̄) and the
standard one-loop formula b = (11/3)C₂ − (2/3)Σ_Weyl T − (1/3)Σ_complex-scalar T: **b = 25.00, 17.67, 10.33, 6.67** at
SO(10), SO(8), SU(4), SU(3) (control: the textbook SM b₃ = 7 reproduced). Chat-2's 20.67, 9.33, 6.00 undercounted b; every
sign is positive either way. R4b survives the sign check. What the check does NOT establish: which scale rule to fire (the
five candidates remain the seat's open step), and the Higgs content beyond one complex 10 (the seat's own caveat 2).

**The WDD identification — the seat's ORIGINAL reading was right; its self-flag is a transcription error; and its
conclusion is REVERSED by main's record.** Every E₆ weighted Dynkin diagram is symmetric under the diagram automorphism
(α₁↔α₆, α₃↔α₅), so a single zero can sit only at α₄ or α₂; "zero at α₃ alone" is not a diagram of any orbit (the seat's
displayed table row has four chain entries where E₆ has five). Computed here from the root system: (2,2,2,0,2,2) gives the
78 = [17, 15, 11, 11, 9, 7, 5, 3], eight pieces = the 70-dimensional orbit's centraliser (consistent); (2,0,2,2,2,2) gives nine
pieces against a centraliser of 8 (not an sl₂ grading); the principal reproduces [23, 17, 15, 11, 9, 3]. So E₆(a₁) has its
zero at the trivalent α₄, exactly as `frontier/B1256_sl2_embedding/FINDINGS.md` records. **But the seat's "h¹ = 1, same as
principal, hatch closed" misreads Menal-Ferrer–Porti:** acyclicity holds for the even-dimensional (Sym^odd) summands only;
each nontrivial odd-dimensional summand contributes one H¹ class per cusp (main's record, two primes: h¹(Sym^even) = 1,
h¹(Sym^odd) = 0). On the adjoint that is **h¹ = 6 under the principal and 8 under the subregular**, and on the 27 B1256
already banks the subregular as **13 + 9 + 5 — three chiral classes with no assumption about the spin lift — registered as
the unearned input I-25.** The "escape hatch" the seat reports closed is the embedding main's own record favours. This is
the item that would have slipped.

## 2. The rest of the handoff, verified

| item | seat's claim | main's verdict |
|---|---|---|
| Nesting theorem drill(M(A₁)) = M(A₂) | WITHDRAWN by the seat | refuted on the cloud lane (B1346 §6) and here (drilled manifold: 2 cusps, isometric to m129; m136 has one cusp; volume 3.6638623767 real). Closed. |
| 3b minimum compression | Vol(A₁A₂) = 5.6254 < 5.6937, "3.4 % for (1,2), 9.8 % for (1,3)" | volumes reproduce exactly (b++LRLLRR = 5.625378; b++LR + b++LLRR = 5.693746; excess −0.068367); the percentages are wrong: **−1.20 %** for (1,2), **−2.90 %** for (1,3); the ordering (the parabolic pair compresses least) holds. |
| 3c the ζ₁₅ ratio tr(Par·W₁W₂)/tr(Par·W₂W₁) | exact root of unity | NOT VERIFIED — Par, W₁, W₂ are undefined in the handoff; send the matrices. |
| 3d volume conjecture for 4₁ | verified live | standard (proved for 4₁); not the object's. |
| 4a generations = 3 | OPEN via I-25/I-26 | agreed; and see §1: I-25's subregular reading is the live route the seat mis-closed. |
| 4b proton decay p → K⁺ν̄ | testable, not distinctive | agreed; generic to SO(10)/E₆. |
| P1–P9, P11, P12 nulls (~8 000 candidates) | NULL with controls | consistent with V-3 and B685/B701; not re-run here (the sealed V-3 scan is the record's instrument); the named near-miss \|η(ω)\|²⁴ = 0.004805 vs m_e/m_μ = 0.004836 reproduces (0.65 %, a miss). |
| P10a/P10b | NULL by acyclicity, h¹ = 1 both | **WRONG as stated** (§1); the value-null survives (dimensions are not parameters), the typing does not. |
| M11 verdict (cost of a closing) | cc3's C3 refuted; dimensionful half vacuous by MB12; all ambiguities 2-torsion so every cost ratio is 1; "no closing costs ln 3"; the KS-entropy ratios ln 2/2 = 0.3466 and ln 2/log φ² = 0.7202 are numbers without a referent | sound and consistent with the record (B700/B701 torsor, B698/B699, the Klein four-group of ℚ(√5, √−3)); the two ratios recomputed; the Dehn-slope exception correctly left open. REGISTERED; the near-miss pair goes to the hint ledger as the seat asks. |
| L153 amendment v2 (B1024's sealed prereg) | C-i naturality, C-ii null in the seal, C-iii joint rank; k = 2 governs | arithmetic verified (generating pairs 6/16, triples 42/64; 1.415 and 0.608 bits); the τ-fixed nodes α₂, α₄ correct; the B928 citation matches. REGISTERED as a pre-compute amendment; adding it to the sealed cell is main's decision under the re-seal rule (original hash recorded). |
| Chowla–Selberg first attempt | wrong, self-caught | noted; the corrected value reproduces. |

## 3. Disposition
**VERIFIED-DIFFERS.** Positives verified: the sign check (with corrected numbers), the WDD placement, the compression
ordering, the M11 and L153 documents. Negatives verified: the nesting withdrawal. Reversed: the "subregular hatch closed"
reading (the record has it open and named, I-25). Unverified pending inputs: 3c. Reply HELD (owner: all sends hold); this
document is the reply. No arc number (lineage decision pending).

## Addendum (2026-09-15, chat-2's reply, owner-relayed)
The seat owns all three corrections in full and rewrites its P10 rows: "NULL by theorem, both embeddings" is withdrawn; the
subregular channel is alive and is the programme's own route (I-25/B1256); everything else in its scorecard stands. Its
stated lesson — verify the theorem invoked, not only the computation performed — is the E58 shape (a result cited from a
paraphrase), recorded as such. **One precision for the seat's rewrite:** the counts are exact, not "much larger". On the
adjoint, one cusp: h¹ = 6 under the principal embedding (six odd-dimensional summands) and 8 under the subregular (eight).
On the 27: h¹ = 3 under both — principal 17 + 9 + 1 gives 1 + 1 + 1 (the trivial summand contributes the abelian class;
verified here at 500 bits), subregular 13 + 9 + 5 gives 1 + 1 + 1 with no trivial summand, which is why B1256 calls the
subregular reading assumption-free. The difference between the embeddings is not the size of h¹ on the 27 but what the three
classes are typed as.
