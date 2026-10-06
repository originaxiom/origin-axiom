# PREREGISTRATION — which half of the 2T door is Pin⁺ (web seat, 2026-10-06). Sealed BEFORE computing.
Follows `chat1_2026-10-06_register_test` (P2c, R1). Setting and convention taken from sm:B1382 §1, not chosen here:
pi1(m004) = <a,b | abABaBAbaB>, holonomy (Riley/B1141) a -> A = [[1,1],[0,1]], b -> B = [[1,0],[-omega,1]];
the deck ("beat") a -> a, b -> b^-1 a b a^-1 b; pi1(m000) = <pi1(m004), t | t g t^-1 = beat(g), t^2 = a>;
G_eps = {(M,k)}, (M1,k1)(M2,k2) = (M1 conj^k1(M2) eps^(k1 k2), k1+k2); Pin⁺ = G_+ (reflections lift to involutions).
B1382 S4: the lift rho1 (a -> +A, tr mu = +2) extends into G_+ only; rho2 (a -> -A) into G_- only.

## Reduction mod sqrt(-3) (the 2T door): c is invisible (omega = omegabar = 1 in F3), so G_+ reduces to SL(2,3) x Z/2
with no cocycle and G_- keeps the sign. Hence, for psi: pi1(m004) ->> SL(2,3), an extension t -> A_t needs
A_t psi(g) A_t^-1 = psi(beat g) and: A_t^2 = +psi(a) (Pin⁺, "honest") or A_t^2 = -psi(a) (Pin⁻, "sign").

## Predictions (each with its kill)
Q1 (independent replication of P2/R1 in a different presentation, deck explicit): 48 surjections; 24 Pin⁺-extendable,
   24 Pin⁻-only, 0 needing an outer automorphism; m004's Z/2 character swaps the halves 48/48. KILL: any other count.
Q2 (control): the Riley relator abABaBAbaB holds exactly over Z[omega] and mod 3; psi1 = rho1 mod sqrt(-3)
   (a -> [[1,1],[0,1]], b -> [[1,0],[2,1]]) is a surjection; B1382's intertwiner W = [[1,-omega],[0,1]] reduces to
   W3 = [[1,2],[0,1]] and intertwines psi1 with psi1 o beat. KILL (of the setup): any failure.
Q3 (THE TEST): psi1 (reduction of the Pin⁺ lift rho1) lies in the Pin⁺ half, with W3 itself satisfying W3^2 = +psi1(a);
   psi2 = psi1 (x) chi (reduction of rho2) lies in the Pin⁻ half. KILL: the opposite assignment.
## Consequence, conditional and stated now
If Q3 passes: under sm:B1383's finding that physics fixes Pin⁺ (in the role where the parent is a background), physics
selects the 24-element half of the E6 entrance that contains the geometric reduction. In B1383's other deck roles the
selection is the other half or undetermined — the role, not the half, is then the open bit. Not a physical claim.
## Scope
frame: F-MC entrance; object: m004, m000; reach: single; hypotheses: B1382's presentation, deck and convention.
