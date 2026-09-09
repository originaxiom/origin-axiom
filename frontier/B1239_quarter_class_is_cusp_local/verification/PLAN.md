# B1239 plan (drafted while B1237's suite ran, 2026-09-02) — codex R040 + fc R42–R48/Phase C-D

## R040 (free deck ⇒ CS = 0): what the certificate actually checks
- codex's `free_deck_cs.py` "closed theorem" block is a hard-coded parity chain (alpha=0, eta=0 → 2cs≡0 mod 2): it
  computes NOTHING — the theorem rests on two citations (Kawauchi 1981 Thm III; CGHN 2003 p.14, 3η = 2cs + τ mod 2).
- The census block is real: 1260 NonorientableCuspedCensus → orientation_cover() → chern_simons() classified mod 1/2
  into zero / quarter / other at TOLERANCE 1e-6 (double precision); requires counts == {zero: 1260}.
## The structure to type in B1239 (my reading; verify on bench)
- (a) FREE from Mostow + oddness: the deck involution of an orientation double cover is an orientation-reversing
  ISOMETRY of the cover M; cs(−M) = −cs(M), so 2cs ≡ 0 in whatever group CS lives in. Closed: cs ∈ {0, 1/2} mod 1.
  Cusped (SnapPy's CS is mod 1/2): cs ∈ {0, 1/4} mod 1/2. This much is a theorem in both cases — no citation needed.
- (b) THE CONTENT is excluding the nonzero class (1/2 closed; 1/4 cusped). Codex's chain does it for CLOSED via
  Kawauchi (Tor H1 = A ⊕ A ⇒ τ even) + CGHN. For cusped there is no chain — the census (quarter count = 0 in
  1260/1260) is the evidence. Codex's ask (grade separately; don't promote) is right, and (a) sharpens what the
  census tests: it tests the ABSENCE of the 1/4 class, not "cs ≡ 0 mod 1/2" bare.
- (c) Rerun on bench: same census, CS at higher precision (`M.chern_simons()` after `high_precision()`), record max
  residual; also count how many covers are distinct manifolds (isometry classes) — codex only checked distinct NAMES.
- (d) Closed-case computed control: take a closed nonorientable manifold (e.g. fillings of nonorientable census
  members), form the orientation double cover, compute CS (Dehn-filled; SnapPy gives closed CS mod 1) and check the
  1/2 class is empty on a finite sample; and check Tor H1 = A ⊕ A on the same sample (Kawauchi's conclusion, computed).
- (e) Scope: only the CS/k-blind sub-arrow of B1234; relate to L194/A6 (CS = 0 at 40/40).
## fc R42–R48 / Phase C-D (502c115d): each recomputed before banking
R42 m=12 class count (3 SL / 2 GL; B8148's GL wrong), R43 Vol(4₁) digit slip, R44 B549 = E7 Perron eigenvector,
R45 arithmetic MATCH, R46/R47 certificate passes, #1207 up-Yukawa disagreement, R48 B511 D3.3 (NaN in committed
script; 60-digit exact trace map reproduces in substance), Phase C 59 rerun packets, Phase D 38 certificate packets,
W-E part 5 (1535 absence claims), GUE rerun. Plus fc's ask: the 48-pair SUPERSEDED_UNMARKED table (L197 input).
