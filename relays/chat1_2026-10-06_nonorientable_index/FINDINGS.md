# FINDINGS — the class index on m000's non-orientable levels (PREREG sha256 e88cac0f…, sealed before computing)
web seat, 2026-10-06. Frame F-CI extended by definition · objects m000, N3 (m000's 3-fold level), m004, M3 · reach single ·
F_13, every character of H1(N) and every reducible non-split 2-dim extension of two (264 systems). Own implementation.
| | prediction | outcome |
|---|---|---|
| L1a | twisted half-lives-half-dies r1(V) + r1(V*⊗w) = t1(V) on the non-orientable pair (N, Klein bottle) | **PASS 264/264** |
| L1b | the untwisted identity fails somewhere (V* is the wrong partner) | **WITNESSED**: fails 4/24 (m000), 34/240 (N3) |
| L2 | the register lemma I(M; p*V) = I_w(N;V) + I_w(N;V⊗w) | **PASS 264/264** |
| controls | Euler on N, M and cusps; B1297's orientable annihilator on M | **PASS 264/264** (after the fix below) |
| L3 | reported | every I_w(N;V) = 0 and every I(M; p*V) = 0 on these families |

## Definition this establishes for the record
On a non-orientable cusped N the class index is **I_w(V) = n(V) − n(V*⊗w)**, n(V) = a1 − r1 unchanged (orientation-free).
B1297's T1 becomes I_w(V*⊗w) = −I_w(V). It is not a chirality (chirality is not definable on N, 28dbd73f).
**The register lemma:** for the orientation double cover p: M → N, I(M; p*V) = I_w(N;V) + I_w(N;V⊗w) — the child's count is
the parent's twisted index summed over the two settings of the register. Proof: Shapiro for the pair (the Klein-bottle cusp
double-covered by the torus) and (p*V)* = p*(V*), with (V⊗w)*⊗w = V*; verified on 264 systems.

## The bug, recorded (WORKING_RULES: no negative or positive from a bug)
The first run deleted s1a = a·a as a trivial Schreier generator. The controls failed (0/24, 0/240), and the broken run
showed ±1 "chiral" counts on 72 systems over M3 — artifacts. Preserved in `run_FAILED_bug.txt`.

## What it means, at its scope
No system pulled back from a non-orientable level carries a count on these families: what is pulled back from the act alone
is silent. M3's banked firing backgrounds (B1432: 48) are built on M3's own characters and were not tested here. **Next, to
seal:** do M3's firing modules descend to N3 at all? If none descends, every count on the tower lives in the part the
register adds, in deck-exchanged pairs.
