# R49 — cloud's `spacetime64.py`: the certificate's own count contradicts its printed verdict ("no hypercharge room")

**Certificate** (`outside_bench/certificates/spacetime64.py`, re-fired by `a2_glue64.py`; memos 27 "THE_64_ORGANIZED" and
33 "THE_64_GLUED"): exact weight decomposition of the 64-dimensional complement of so(3,1) ⊕ su(3) inside e6 by
(h₁,h₂)-weight and colour content. Its docstring states the intent: "ZERO color-singlet (0,0)-weight outside the
algebra — i.e. NO room where a hypercharge u(1) could organize (the rep-side refinement of memo 11's z = 0)", and its
line 89 prints `color-singlet (0,0) content in the complement: <n> (0 = NO hypercharge room; matches memo 11)`.

**Rerun here (`spacetime64_output.txt`, exit 0; the Phase D agent flagged the same):** the complement's weight table is
reproduced (64 = 2 Cartan + 54 coloured + 8 neutral), and the printed count is **2, not 0**:
`color-singlet (0,0) content in the complement: 2 (0 = NO hypercharge room; matches memo 11)`. The two are the row
`(0, 0, 'cartan') : 2` — the two Cartan directions of e6 not used by so(3,1) ⊕ su(3). The script has no assertion on
the value, so it exits 0 with a verdict string its own number falsifies.

**Why the 2 is real, not a bookkeeping slip.** rank e6 = 6; so(3,1)_ℂ ≅ sl₂ ⊕ sl₂ has rank 2 and su(3) rank 2, so the
subalgebra's roots span a rank-4 sublattice and exactly a 2-dimensional subspace of the Cartan is orthogonal to all of
them. Those two Cartan elements have (h₁,h₂)-weight (0,0), are colour singlets, and commute with every root vector of
the subalgebra (all its roots vanish on them): they centralise so(3,1) ⊕ su(3). So the centraliser has dimension ≥ 2 —
two abelian directions, i.e. room for two commuting u(1)s, one of which is where a hypercharge would sit. This is the
same rank count the seat recorded from main (B952: rank deficit 2; R44: centraliser of su(3)+su(2) in e6 is 9-dim,
of which 3 are Cartan).

**What "memo 11's z = 0" can mean.** Memo 11's z = 0 is the centraliser of the full fork A2³ (rank 6), which is indeed
zero; the docstring transfers that to the smaller subalgebra so(3,1) ⊕ su(3), where it is false. The 64-glued theorem
of memo 33 (θ a bracket-equivariant bijection sl₃(S0) ↔ sl₃(S1), 3 ↔ 3̄ on the 54) does not depend on the "0"; only the
"no hypercharge room" sentence does.

**Verdict: the certificate's declared verdict is CONTRADICTED by its own output** (count 2 ≠ 0); the underlying theorem
(the 64's decomposition and gluing) reproduces. For cc: the sentence "no room where a hypercharge u(1) could organize"
should not be carried from memo 27/33 into main; the object's e6 leaves two u(1)s of room next to so(3,1) ⊕ su(3),
exactly as the rank count says. Whether the object selects one of them is B1160/B8143's question, not this one.

**Addendum — `a2_glue64.py` rerun here (`a2_glue64_output.txt`, exit 0):** every gluing check prints True: θ maps all 8
basis elements of sl₃(S0) into span(sl₃(S1)), the induced 8×8 map has rank 8 (bijection), bracket equivariance on all 64
pairs, grading match on all 6 roots, θ(T1) an exact sl₂-triple in sl₃(S1), every coloured image on a single colour
weight with w → −w everywhere (3 ↔ 3̄), and Σ preserves the Lorentz double / colour sl₃ / fork setwise (6/8/14). So
memo 33's theorem reproduces on this bench, and B1140's "NOT checked" fence on the antilinear gluing (sweep #1186) is
discharged on the outside-bench head and verified here. The same run re-prints the "(0,0) content: 2 (0 = NO
hypercharge room)" line — the contradiction above travels with it.
