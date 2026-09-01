# T4 — SEARCH LOG (prior art on the registerability-termination rule)

**Cell:** T4_prior_art · **Date:** 2026-09-01 · **Seat:** outside evaluation seat, compute cell
**Apparatus:** WebSearch (general web) + WebFetch (arXiv abs/html pages) + local `pdftotext`
on arXiv PDFs downloaded through the session proxy. All queries below were actually run;
summaries of what each returned are condensed from the live results.

## Bite control (MB12) — run FIRST in design, run during the sweep, PASSED

**Design.** The verdict criterion (KNOWN / PARTIAL / NOT-FOUND per half) can fail in both
directions: "KNOWN" fails if no verbatim passage exists; "NOT-FOUND" fails if a passage does
exist. A NOT-FOUND from a broken retrieval apparatus is worthless, so the bite control is a
**positive retrieval control**: search for a fact this repo has already independently established
as findable in the literature — the Z6 global form / SM-as-subgroup-of-SU(5) fact (dossier
entry 4, verdict KNOWN, anchored on Tong arXiv:1705.01853). If the apparatus cannot retrieve
that, every NOT-FOUND in this cell is void.

**Result: PASSED.** Query Q9 (below) returned Tong, "Line Operators in the Standard Model,"
arXiv:1705.01853 / JHEP 07 (2017) 104, first page of results, with the exact content: the SM
gauge group is SU(3)×SU(2)×U(1)/Γ, Γ ⊆ Z6 undetermined by experiment, and the Z6 quotient is
the subgroup of SU(5) preserving the 3+2 splitting of C^5. The apparatus retrieves known prior
art on this exact subject area; NOT-FOUND results below are therefore meaningful (within the
stated bound).

## Queries (in order run)

| # | Query (verbatim) | Key returns |
|---|---|---|
| Q1 | `"survival hypothesis" Georgi chiral fermions grand unified theory light fermions` | Survival hypothesis confirmed as standard 1979-80 GUT lore; hits: arXiv:hep-ph/0703195 (orbifold family unification, uses SH), arXiv:2604.08237, JHEP06(2024)018 (E6 unification), arXiv:2102.13465 (Britto MSc thesis, E6 GUT), Georgi CV |
| Q2 | `Barbieri Nanopoulos "survival hypothesis" E6 exceptional model grand unification 1980` | Barbieri & Nanopoulos, "An exceptional model for grand unification," Phys. Lett. 91B (1980) 369 (ScienceDirect); secondary sources phrasing SH as: achiral GUT fermions needed to recover SM chirality would be unacceptably heavy |
| Q3 | `Slansky 1981 "Group theory for unified model building" chiral fermions subgroup breaking chains E6 complex representations` | Slansky, Phys. Rep. 79 (1981) 1–128 confirmed as the chain/branching-rule compendium; ALSO surfaced arXiv:1504.03695 (Fonseca) — decisive |
| Q4 | `"chirality" "survival hypothesis" subgroup "vector-like" breaking chain Standard Model unique terminal minimal chiral gauge group` | Extended survival hypothesis (scalar sector, minimal fine-tuning) surfaced; arXiv:1110.3210 (GUT symmetry breaking review); no terminality statement |
| Q5 | `"every subgroup" OR "any subgroup" of the Standard Model gauge group fermions become "vector-like" chirality lost below` | Nothing matching the quantified statement; standard vector-like-fermion phenomenology only |
| Q6 | `Langacker 1981 physics reports "survival hypothesis" "remain massless" fermions "chiral" unbroken subgroup statement` | Langacker Phys. Rep. 72 (1981) 185 confirmed to exist; verbatim passage not retrievable (paywalled); not needed — SH wording obtained elsewhere |
| Q7 | `"Standard Model" "smallest" OR "minimal" chiral gauge theory "no chiral" subgroup below claim` | "Chiral Abelian gauge theories with few fermions" (arXiv:2001.11991, PRD 101, 095032) — minimal-chiral-theory literature exists but counts fermions for a FIXED group; no descent-terminality statement |
| Q8 | `E6 symmetry breaking chains chirality preserved "down to the standard model" endpoint unique enumeration selection rule independent` | E6 chain papers (trinification JHEP07(2023)011, JHEP06(2024)018 "realistic E6 through novel intermediate symmetries" — uses extended survival hypothesis and parities to keep SM chiral states light); all ASSUME the SM endpoint |
| Q9 | *(bite control)* `Tong "line operators" Standard Model gauge group SU(3)xSU(2)xU(1)/Z6 subgroup of SU(5) hypercharge` | **PASSED** — Tong arXiv:1705.01853 retrieved with the exact known content |
| Q10 | `Hewett Rizzo "low-energy phenomenology of superstring-inspired E6 models" 1989 chirality breaking chains survival hypothesis` | Hewett & Rizzo, Phys. Rep. 183 (1989) 193 confirmed; full text paywalled; nothing surfaced suggesting a terminality theorem in it (it is a phenomenology survey with the SM endpoint assumed) |
| Q11 | `Slansky "imaginary representations" OR "complex representations" subgroup chains chirality survives breaking E6 SO(10) tables` | Re-surfaced Fonseca 1504.03695 incl. the "12 distinct ways of embedding ... 5 pairs of chiral embeddings" count |
| Q12 | `"distinct ways of embedding" "SU(3)" "SU(2)" E6 "chiral embeddings"` | Pinned the count and the uniqueness claim to Fonseca 1504.03695 (also: ResearchGate figure from the same paper) |
| Q13 | `tumbling gauge theories Dimopoulos Raby Susskind cascade stops "vector-like" terminal endpoint breaking chain` | Raby, Dimopoulos, Susskind, "Tumbling gauge theories," Nucl. Phys. B169 (1980) 373: dynamical breaking iterated via most-attractive-channel "until one arrives at a QCD-like theory or the gauge group is fully broken" — a termination-at-vector-like concept, dynamical not group-theoretic, endpoint not claimed to be the SM |
| Q14 | `"all breaking chains" OR "every breaking chain" OR "all paths" E6 SO(10) "lead to the standard model" chirality forces endpoint` | arXiv:2204.03001 enumerates "all admissible breaking chains towards the Standard Model" for SO(10) — admissibility from the scalar sector/vacuum, SM as the assumed target; no chirality-terminality, no rule-space quantification |
| Q15 | `"survival hypothesis" Georgi 1979 "Towards a grand unified theory of flavor" statement quote fermions acquire mass unless chiral` | Georgi, Nucl. Phys. B156 (1979) 126 confirmed as the origin; full text paywalled; SH wording obtained from secondary sources (see FINDINGS) |
| Q16 | `"chirality index" OR "net chirality" subgroup branching classification "which subgroups" admit chiral fermions grand unified` | Chirality constrains GUT groups to those with complex reps (SO(10)-or-smaller orthogonal, E6-or-smaller exceptional) — the standard UPWARD constraint (Georgi–Glashow "Gauge theories without anomalies" PRD 6 (1972) 429 lineage); no downward terminality |

## Full texts consulted (beyond result snippets)

1. **arXiv:1504.03695** (Fonseca 2015, "On the chirality of the SM and the fermion content of
   GUTs") — full PDF downloaded, text-extracted, grepped exhaustively for `unique`,
   `chiral` (106 hits), `further break|below the|terminal|halt|stop` (**zero hits** for the
   termination direction). Verbatim passages quoted in FINDINGS.md.
2. **arXiv:2102.13465** (Britto MSc thesis 2017/2021, "A Mathematical Construction of an E6
   Grand Unified Theory") — full PDF downloaded, text-extracted; survival-hypothesis passages
   and the complex-representation/chirality demand quoted verbatim in FINDINGS.md; grepped for
   `terminal|unique.*chiral|maximal.*complex|vector-like`: no terminality statement.
3. **arXiv:2507.06368v2** ("Grand-unification Theory Atlas") — fetched via arXiv HTML; does
   not enumerate breaking chains; explicitly notes "it is not at all granted that their
   low-energy limit uniquely yields the SM"; no chirality-termination criterion.
4. **arXiv:hep-th/0112046** (Huang, Jiang, Li, Liao, 6D SUSY E6 breaking) — fetched; ruled
   out as the source of the embedding count; no relevant content.

## Sources confirmed to exist but not full-text readable from this bench (paywalled)

- Georgi, "Towards a Grand Unified Theory of Flavor," Nucl. Phys. B156 (1979) 126 (origin of SH).
- Barbieri & Nanopoulos, "An Exceptional Model for Grand Unification," Phys. Lett. 91B (1980) 369.
- Barbieri, Nanopoulos, Morchio, Strocchi, "Neutrino Masses in Grand Unified Theories," Phys. Lett. B90 (1980) 91.
- Langacker, "Grand Unified Theories and Proton Decay," Phys. Rep. 72 (1981) 185.
- Slansky, "Group Theory for Unified Model Building," Phys. Rep. 79 (1981) 1.
- Hewett & Rizzo, "Low-Energy Phenomenology of Superstring-Inspired E6 Models," Phys. Rep. 183 (1989) 193.
- del Aguila & Ibáñez, "Higgs Bosons in SO(10) and Partial Unification," Nucl. Phys. B177 (1981) 60 (extended survival hypothesis; scalar-sector rule).
- Raby, Dimopoulos, Susskind, "Tumbling Gauge Theories," Nucl. Phys. B169 (1980) 373.

**Bound of this search:** 16 web queries + 4 full texts, English-language web + arXiv,
one bench-day. Paywalled 1979-81 primary sources were characterized through verbatim quotes in
secondary sources (Britto thesis quoting Georgi [34] and Barbieri et al. [10]; multiple modern
papers restating SH). A specialist with library access to Slansky §"chains" and Hewett-Rizzo
could tighten the bound; the NOT-FOUND on terminality is a bounded claim, not a certificate.
