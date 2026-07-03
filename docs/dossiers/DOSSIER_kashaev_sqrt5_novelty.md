# Specialist dossier — the ℚ(√5) content of ⟨4₁⟩_N at 5|N (NOT SENT; outreach dormant)

**The claim to adjudicate (novelty check).** The Kashaev invariant of the figure-eight,
⟨4₁⟩_N = Σ_k Π_{j≤k}(2 − qʲ − q⁻ʲ), q = e^{2πi/N}, is NOT a rational integer at general N;
exact Galois components (trace projections, Ramanujan sums; frontier/B384/kashaev_smalls.py):

    ⟨4₁⟩_5 = 46 + 2√5;  √5-parts at N = 15, 25, 45, 135: 2023/4, 13100, 71150671/4,
    129870648314553074968 — NONZERO AT EVERY 5|N LEVEL tested; zero √5-subfield otherwise
    (N = 7, 9, 27, 81 rational parts 113, 258, 79576, 4784926648467).

**The context making this interesting.** The same 5|N levels are exactly where the
quantized golden cat map tower (= our theta model; ord(W₁@N) = π(N)/2, the Pisano identity)
carries its golden value sector; the figure-eight's monodromy IS that cat map. A
Pisano-valuation ladder was tested and KILLED (registered): the bridge exists at field
level, not valuation level.

**What a specialist is asked.** (i) Is the algebraic (non-rational) nature of ⟨4₁⟩_N at
composite N, and specifically its ℚ(√5)-content at 5|N, known (Habiro ring /
Garoufalidis–Zagier quantum modularity circles)? (ii) Is there a known Galois-equivariance
statement for ⟨4₁⟩ at non-prime roots explaining the √5-part's growth?

**Reproduce:** `python3 frontier/B384_kashaev_bridge/kashaev_smalls.py` (~2 min, exact) ·
locks `pytest tests/test_b384_kashaev.py`.
