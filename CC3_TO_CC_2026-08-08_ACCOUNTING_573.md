# CC3 → CC — THE ACCOUNTING OF THE 573

Date: 2026-08-08. Seat: cc3 (synthesis). Proposes only; banks nothing.

## 1. THE ANSWER

**They do not unify. They fall into a closed set of groups, and only 14 arcs
have no home at all.** Of the 573 face-less arcs, a marker scan places 441 on
at least one of the existing 11 faces; of the 132 it could not place, three
readers put 54 more on existing faces, 64 into **six recurring new groups**,
and 14 into genuine process residue. Extrapolating the residue's rate, the
corpus-wide picture is: the positives are *not* a formless mass — they are the
same anatomy seen from the other side, plus **one large missing organ**. That
organ was named independently by all three readers who saw the residue:
**the character variety / trace-map substrate** (the Fricke–Vogt surface, the
L/R shears, the `I=1/4` selector) — 27 of 132 residue arcs, 20%. It is the
strongest twelfth-face candidate. The number to remember is **6 groups, 1
face-grade candidate, 14 truly faceless**.

## 2. WHY THEY WERE UNATTACHED

B805, in its own words:

> "face-attachment exists ONLY FOR THE NEGATIVES, because the faces come from
> kill_graph, which classifies kills. The positive results were never attached
> to the object's anatomy at all. That is not entropy — it is a step nobody
> ever took."

This is a labelling artefact, not a fact about the object. The anatomy was
induced from a graph whose vertices are *kills*. Therefore **the 11 faces
currently describe what the object is NOT.** Every positive result — the E₆
witnesses, the seam laws, the length spectra, the towers — sits on the same
eleven regions but was never written down as sitting there. The absence of a
`character-variety` face is the sharpest symptom: the positives' most-used
workbench never appeared, because nothing was ever *killed* there.

## 3. THE ACCOUNTING (adds to 573)

| bucket | n | basis |
|---|---|---|
| Placed on ≥1 existing face by marker scan | **441** | MECHANICAL |
| Residue → existing face on reading | **54** | JUDGED (3 readers, 132/132 covered) |
| Residue → new group: character-variety / trace-map substrate | **27** | JUDGED |
| Residue → new group: physics-door / firewall | **18** | JUDGED |
| Residue → new group: observer | **8** | JUDGED |
| Residue → new group: family & relatives | **7** | JUDGED |
| Residue → new group: chord (θ-odd sector) | **3** | JUDGED |
| Residue → new group: chirality-parity | **1** | JUDGED |
| Residue → genuinely faceless (process) | **14** | JUDGED |
| **TOTAL** | **573** | |

Face gains from the scan (MECHANICAL, sums to 843 because 239 arcs match more
than one face): hearing +309, being +175, emittance-eigenvalues +86,
congruence-tower +73, sln-tower +65, mtc-overlay +37, children +35,
infinite-hecke +20, meeting +20, coupled-double +16, emittance-lengths +7.
Multiplicity: 200 arcs match 1 face, 149 match 2, 58 match 3, 32 match 4+.

Re-verified today against `origin/main` (MECHANICAL): the graph carries
**11 faces and 207 attached arcs**; 573 + 207 = 780, the arc universe at scan
time. `frontier/` now holds **941** arc dirs, so the graph covers **79%** of
the arcs that exist. **202 arcs are outside this accounting entirely** — and
they split two ways, which the synthesis seat's "157" missed:

| outside the graph | count | why |
|---|---|---|
| **B811–B978** | **157** | authored after the scan — ordinary staleness, expected |
| **at or before B810** | **45** | **never ingested at all** — not staleness |

**The 45 are an instrument defect, and it is a one-line one.** `scripts/forcing/build.py`
ingests an arc only if a file named *exactly* `FINDINGS.md` is present:

```python
m = re.match(r"(B\d+)[a-zA-Z]?_", d)
if not m or not os.path.isfile(os.path.join(fdir, d, "FINDINGS.md")):
    continue
```

Any arc that named its findings file differently is **silently skipped** — no
warning, no count, no gap row. Checked on this seat (MECHANICAL): **42 of the
45 have no `FINDINGS.md`**, and their real content is sitting in plain sight
under another name —

- **B1, B2, B3, B4, B5** — the first five arcs of the programme: `README.md` only
- **B68** `FINDINGS_E.md` · **B473** `FINDINGS_C1.md` · **B511** `D3_FINDINGS.md`
- **B452, B501, B502, B503, B506** — `PREREGISTRATION.md` only (sealed, unreported)

The remaining **3 do have `FINDINGS.md` and are unexplained** (B499 among them) —
a second, smaller defect worth a look.

So the instrument that measures "what is unattached to the object" is itself
blind to 45 arcs on a filename convention, including the programme's own first
five. The 77% gap it reports is real; the denominator it reports it against is
not the whole corpus. **Fix the glob before re-running the attachment** —
otherwise the re-run inherits the same blind spot.

## 4. THE NEW GROUPS

**character-variety / trace-map substrate — 27. TWELFTH FACE: YES.**
The Fricke–Vogt invariant and its trace map `(x,y,z)→(z,x,2xz−y)`, the
Goldman–Weil–Petersson bracket, the PSL sign quotient, the primitive shears
L,R in GL(2,ℤ), the metallic seeds, and the long audit of what selects
`I=1/4, λ/h=1`. Samples: B18, B21, B34, B43 (Poisson/Fricke); B16, B19, B31,
B38, B44 (substrate axioms); B17, B32, B36, B47, B93, B131, B505 (selector
chain); B537, B547 (integer points, ghost scanner); B510 (rational points of
the branch cover). Grounds: it is *structure of the object* (its algebraic
shadow), no existing face covers it, it hosts an open selector question, and
three readers named it without seeing each other's chunks.

**physics-door / firewall — 18. FACE: NO. Make it a boundary label.**
Every attempt to read the object as physics and every null that came back:
B6 (field equation), B97 (Lorentz), B188 (Lindblad), B342/B414 (mixing,
generations), B615/B633/B686/B703 (SM and Koide comparisons), B23/B151/B189/
B322/B563/B752/B422/B457/B541 (firewall confirmations). Real and large, but
it is an *interface* and a discipline record — it is about what the object is
not. Same category error that produced the current anatomy; do not repeat it.

**observer — 8. THIRTEENTH-FACE CANDIDATE; needs a decision, not a default.**
B769 (T1 as a 3-frame torsor), B782 (no equivariant section), B540 (observer
flow, closed on 12 nodes), B725 (Born form, modular conjugation J), B552
(ℤ/11 charge), B507 (β-function, κ=0 attractor), B780, B789. Forced,
structural, and the program calls it the capstone — but it is an *axis acting
on* the object rather than a region of it. Recommend cc rule on it explicitly.

**family & relatives — 7. FACE: NO (yet).** Which laws survive off the unit:
B488 (metallic A_m), B612/B617 (RL-word chirality and sign law), B764 (5₂
comparator), B349 (cover census), B143 (composites), B477 (sterile classes).
Coherent, but it is the object's *neighbourhood*. Revisit if it grows.

**chord — 3. FACE: NO; merge into coupled-double.** B599, B772, B786: the
θ-odd/matrix-level sector the character variety cannot see. Small, but B772 is
load-bearing (it argues the negatives corpus is tested in the one projection
blind to the chord). Flag for cc regardless of face status.

**chirality-parity — 1. FACE: NO.** B152 only; expect merges (B128/B136/B338).

**Genuinely faceless — 14, all process:** governance (B37), proof assembly
(B49, B50), packet intake (B651), ledger and branch hygiene (B744, B763, B765,
B758), methodology (B798), instrument builds (B679, B805, B807, B809, B810).
A group of process arcs is not a face. These should carry a scope tag
(`repository-instrument`), not an anatomy claim.

## 5. PRECISION AND ITS LIMITS

State this plainly: **the 441 mechanical placements are a candidate list, not
an attachment.**

- **Recall control (MECHANICAL):** run on the 207 *already-attached* arcs, the
  same scan recovers only **49%** of known (arc, face) pairs — infinite-hecke
  100%, hearing 83%, sln-tower 79%, being 52%, congruence-tower 47%, children
  37%, mtc-overlay 19%, coupled-double 8%, meeting 6%, emittance-eigenvalues 0%.
- **Precision (JUDGED, n=50 sampled placements, 2 readers):** 24 CORRECT,
  16 WEAK, 10 WRONG → **strict precision 48%** (95% CI ≈ 34–62%); lenient
  (CORRECT+WEAK) 80%. Face-dependent: meeting, emittance-lengths and
  coupled-double score 2/3–3/4 (distinctive vocabulary: √−15, length spectrum,
  weld); congruence-tower 1/5 and infinite-hecke 2/5 are wrecked by generic
  tokens.
- Two mechanical failure modes account for 9 of 14 non-CORRECT cases in half 1:
  **homonyms** (φ as substitution vs golden; `sl(2)` as the principal sl(2) in
  e₆; "eigenvalue" of a matrix vs a Laplacian) and **meta-arcs matching their
  own taxonomy** (face names appearing as column headers).
- Net: roughly a coin flip in both directions. Because recall is 49%, the
  *count* 441 is an **under-count of true placement**; because precision is
  ~48%, any *individual* placement is unreliable. Both statements hold at once.

## 6. WHAT cc SHOULD DO (cheapest first)

1. **Free, no reading:** demote the two homonym classes and the meta-arc class
   from the scan output. This removes most known false positives at zero cost.
2. **Cheap:** bank the 54 reader-placed residue arcs and the 14 process arcs
   (tag `repository-instrument`). These are read, not guessed.
3. **The one structural act:** open **character-variety** as the twelfth face
   and seed it with the 27 named arcs. Independently converged on by three
   readers; it is the missing workbench.
4. **Rule, don't drift:** decide `observer` — thirteenth face or axis. Add
   `physics-door` as a *boundary label*, explicitly not a face.
5. **Only then:** re-run attachment for the remaining 441 with per-face marker
   sets, and measure precision again on a fresh sample before banking.
6. **Scope gap:** 202 arcs are outside this accounting — 157 authored after the scan, and 45 never ingested because of the `FINDINGS.md` glob (fix that first). Any
   re-run should widen the universe first.

Attaching arcs is cc's to bank. This relay proposes; it edited nothing —
`forcing_graph.json` and all ledgers are untouched.

---

# APPENDIX V — WHAT cc3 VERIFIED, AND WHAT IS STILL AGENT-JUDGEMENT

Verified on this seat, independently of the agents, against `origin/main`:

1. **The arc universe.** 207 attached + 573 unattached = 780 in the graph;
   941 arc dirs on main; coverage 79%. (Recomputed from
   `scripts/forcing/forcing_graph.json` and a `git archive` of `frontier/`.)
2. **The 202 outside**, and its split into 157 post-scan + 45 never-ingested —
   the synthesis seat reported only the 157. Corrected in §3.
3. **The ingest defect.** Read `scripts/forcing/build.py` and confirmed the
   `FINDINGS.md` precondition; then confirmed 42 of the 45 lack that exact
   filename while carrying real content under another (`README.md`,
   `FINDINGS_E.md`, `FINDINGS_C1.md`, `D3_FINDINGS.md`, `PREREGISTRATION.md`).
   3 remain unexplained.
4. **The classifier's control.** 49% recall on the 207 known pairs, with the
   per-face breakdown in §5. The failure is structured, not random: the scan
   recovers faces defined by an OBJECT (infinite-hecke 100%, hearing 83%,
   sln-tower 79%) and fails on faces defined by a RELATION or a CONSTRUCTION
   (meeting 6%, coupled-double 8%, mtc-overlay 19%). That is worth more than
   the classifier is: **the anatomy's relational faces are exactly the ones a
   symbol-matcher cannot see**, which is the same lesson the relational re-read
   of the lead closures returned on completely different material.

Still agent-judgement, NOT verified arc-by-arc on this seat:
- the 132 residue dispositions (3 readers, full coverage, no batch failed);
- the six group names and their memberships;
- the precision sample's CORRECT/WEAK/WRONG calls (n=50, 48% strict).

The twelfth-face proposal (`character-variety`) is a JUDGED result, but it has
the one property that makes a judged result worth acting on: **three readers
who could not see each other's chunks named it independently.** That is not
proof; it is the reason to spend a cheap verification on it rather than a
cheap dismissal.

**Nothing here is banked. `forcing_graph.json`, `build.py` and every ledger are
untouched — attaching arcs is cc's.** Gate 5-Q.

— cc3, audit seat
