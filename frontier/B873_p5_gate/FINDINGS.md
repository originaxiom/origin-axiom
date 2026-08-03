# B873 — gate P5 PASSED: menu completeness verified mechanically, and winner-safety turns out to be CITATION-FREE

cc banking seat, 2026-08-03. Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.
**Not preregistered** — the cascade's last external import, gated by an exhaustive adversarial
sweep with every kill computed.

## 1. What P5 was

The fused cascade (B861→B871) imported its option menus from the classification literature. A
chain missing from a menu breaks uniqueness **silently** — P5 was flagged from B859 on as the
single external spine.

## 2. The gate — five computed layers

1. **Regular menus recomputed from the affine diagrams** (Borel–de Siebenthal prime-mark
   removals + mark-1 Levi): E6 → {A1+A5, A2³, D5+u1}; D5 → {A1²A3, D4+u1, A4+u1};
   A4 → {A3+u1, A1A2+u1}. Central charges exact; all conformal at level 1.
2. **The adversarial c-match scan**: every abstract product of simples + u1's (rank ≤ rank g,
   exact Fraction c-arithmetic, closing levels in closed form) that conformally c-matches the
   target. **Every match with dim ≥ winner — 19 across the three steps — is DISPOSED with a
   named, computed kill**: −1∈W registerability (embedding-independent), the full-rank regular
   bound, or the **derived-fit kill** (a full-rank subalgebra is regular, so its semisimple part
   must fit inside the derived algebra of a big-enough maximal regular — rank/dim exclusion;
   this disposes A1+A4@27 into D5 and A2+A2@16, A1²A2@14 into A4, which the bound alone misses).
   **No UNKILLED rows; no surviving winner-dim ties.**
3. **The A1-level cap is a theorem, not a hope**: an embedded sl2's conformal level is its
   Dynkin index ≤ the principal sl2's index = rank·h(h+1)/6 = **156 / 60 / 20** for E6/D5/A4,
   all under the scan's 200.
4. **The special (S-)candidates** from Dynkin's cited tables, with conformality COMPUTED
   (closed-form forced levels: F4 and SO(9) fail, the rest pass) and **Dynkin-index
   T-arithmetic cross-checks all passing** (C4's 27 = Λ²(8)−1 at x=1; A2+G2 at x=(2,1);
   B2-adjoint at x=3; B3+A1 at x=(1,2); B2 ⊂ A4 at x=2).
5. **Registerability on the completed menus**: every conformal completion is killed by −1∈W
   (G2₃, Sp(8), F4, SO(8)×U(1), SO(7)×SO(3), SO(5)×SO(5), SO(5)₃, SO(9), SO(5)₂) except
   **A2+G2 — registerable but dim 22 < 46: cannot win**. Winners on the completed menus:
   **SO(10)×U(1), SU(5)×U(1), SM — unchanged and unique.**

## 3. The import-status surprise

**Winner-safety needs no citation.** Conformality forces an exact c-match; the scan is
exhaustive (cap theorem above); and every ≥-winner match dies by a *computed* kill — the Dynkin
tables were never needed above the winner line. The citation (Dynkin 1952 / de Graaf 2011
S-subalgebra tables + Slansky's 27 = (3,7)+(6̄,1)) now underwrites only the **sub-winner
completeness** of the menu listing — cosmetic for the cascade's uniqueness claim.

**After B871 + this arc, the selection spine carries zero load-bearing imports**: the principle
is B861's, its gate is B871's B599 datum, termination is B863's, the false-positive control is
B869's, the lift is B870's, and the menus are — above the winner — exhaustively self-verified.

## 4. Honest boundaries

- The scan enumerates *abstract* c-matching products; disposal shows none can beat the winner.
  Existence of the sub-winner specials still rests on the cited tables (unneeded for uniqueness).
- Provenance: the machinery was drafted in a scratch pass this session and **hardened here**:
  the scratch version printed the ≥-winner impostors without disposing the sub-bound ones
  (27 into D5; 16, 14 into A4) and never enumerated winner-dim ties — both closed in this arc.
- Conformal embeddings at level 1 are the relevant class (the cascade's steps are level-1
  chains, B861); nothing here re-examines higher-level exotica beyond the c-scan's reach.

`tests/test_b873_p5_gate.py`
