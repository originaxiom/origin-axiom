# N1 interim analysis notes (cc2, 2026-07-16) — per-term Jeffrey data (D2)

GATE: the Jeffrey pipeline reproduces the ENTIRE banked ladder with no normalization
freedom: Z_J(13..19) = +1,+1,+1,0,+1,+1,+2 exactly (jeffrey_run.log). r=18,19 are new
disjoint-pipeline confirmations of Z6=+1 and the Z7=2 discovery.

P-N1-a (sealed): CONFIRMED. At r=16 all 25 Weyl classes contribute nonzero
individually (largest +-0.6667 from b4/b5); the zero is pure cross-class interference.

P-N1-b (sealed): REFUTED AS STATED — support is 25/25 at every r; no new support at 19.
The actual mechanism is sharper: the ENTIRE +2 surplus lives in ONE class, b1 =
charpoly x^6+x^3+1 = Phi_9 (order-9 Weyl elements, class size 5760 = |W|/9), with
det B_w = 361 = 19^2. Its term is +1/9 at every generic r and jumps to 2+1/9 at r=19
(per-element factor exactly 19 = sqrt(det)): the twisted sector's Gauss sum fully
constructively saturates on its fixed-point group (Z/19)^2. Everything else unchanged.

THE JUMP LAW (checked 150 cells = 25 classes x 6 non-generic r, vs the r=13 generic
row): |term(kappa)| / |term(generic)| = sqrt(kappa-part of det B_w):
  - odd primes: EXACT in all cases incl. partial powers (sqrt5 at r=15 on det 605;
    sqrt45 at 15 on det 180; sqrt1125 = 3*5*sqrt5 at 15 on det 1125): 130/150.
  - the 20 violations are ALL dyadic terms at r === 2 (mod 4) (r=14,18): observed
    jump = 2^floor(v2(detB)/4) (20/20: v2=4->2, v2=6->2, v2=8->4, v2=12->8), while at
    r=16 (v2(kappa)=4) the full sqrt(2-part) law holds (x64 on det 4096). The 2-adic
    local factor depends on v2(kappa); v2(kappa)=2 (kappa=20) undetermined -> the
    extension run discriminates.

STRUCTURAL IDENTITY (why it counts): det B_w = det(3I - w - w^(-1)) = |det(A1 (x) w - 1)|
on the coroot 12-torus (using tr A1 = 3, det A1 = 1) = #Fix(w-twisted A1-action) = the
w-sector's flat-connection count. So Z_k = (1/|W|) sum over classes of det(w) *
(Gauss sum over the sector's fixed-point group), and the ladder integers are the signed
resonance balance: generic total +1 (the abelian/Funar value, det(A1-I) = -1 unimodular);
kappa=16 makes the many dyadic sectors interfere destructively (total 0); kappa=19 makes
the single Phi_9 sector (19^2 fixed points) saturate constructively (+2 surplus, no
19-partner to cancel). Departures from +1 can ONLY happen at kappa sharing primes with
some det B_w — the complete resonance spectrum of the object is the multiset
{det B_w} = {1, 5, 16, 25, 45, 80, 81, 100, 121, 125, 180, 225, 245, 256, 320, 361,
400, 576, 605, 625, 1125, 1280, 1600, 4096} (primes 2,3,5,7,11,19 ONLY — so e.g. any
kappa coprime to 2*3*5*7*11*19 = generic rung: Z = +1 PREDICTED for all such kappa).

D1 characters (k<=6 landed, all sector-trace gates OK; k=7 running): noticed —
k=3 has NO invariant vectors in either sector (m_0 = 0 both) yet Z_3 = +1: Z is not
dim Fix; it is the signed Fourier count. k=6 odd: one distinguished +1 line + uniform
multiplicity-5 shells on non-multiples-of-3 mod 18.
