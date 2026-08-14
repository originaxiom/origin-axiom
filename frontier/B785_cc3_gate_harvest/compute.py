"""B785 (cc) -- the cc3 gate harvest: independent re-derivation of the deliverables
that PASSED the 2026-07-25 five-branch gate (owner: "process and verify them all").

Nothing here is copied from cc3's branches; every claim is recomputed from scratch in
this cell. Provenance is recorded, not trusted. Gate 5-Q; nothing to CLAIMS.

Harvested (independently reproduced, exact sympy):
  H1  B768 correspondence numerics   (from audit/b768-correspondence, CONFIRMED)
  H2  B489 DGG-rank / Binet torsion   (from hunt/r28-10-stabilizations, STABILIZED)
  H3  TOMB-L255 Sym^d spectrum        (from hunt/r28-10-stabilizations, STABILIZED)

Cited-not-rerun (infra-dependent, honest provenance only, NOT a cc computation):
  P1  WALL-7 twisted extension: cc3 sampled 18 weld points, all dim=0 (a SAMPLE, not a
      generic proof -- needs many more points). Inspected cc3's wall7_output.txt; not
      re-run here (requires the B575 infrastructure + ~36s/point). Evidence, not proof.

The b769/C21 "tangent-frame alignment" claim did NOT pass the gate (c-odd/theta-odd
conflation) and is deliberately EXCLUDED -- see the C21 correction (main, 2026-07-25).
"""
import sympy as sp

phi = (1 + sp.sqrt(5)) / 2
psi = sp.Rational(1, 2) - sp.sqrt(5) / 2          # = -1/phi, the Lucas conjugate root
R = {}

print("=" * 80)
print("H1  B768 correspondence: T stochastic, eigenvalues {1, -1/phi}; (1-phi)^2 = phi^-2")
print("=" * 80)
T = sp.Matrix([[1 / phi**2, 1 / phi], [1, 0]])
rowsums = [sp.simplify(sum(T.row(i))) for i in range(2)]
evs = sorted(T.eigenvals().keys(), key=lambda e: -sp.re(sp.N(e)))
h1_stoch = all(s == 1 for s in rowsums)
h1_ev = sp.simplify(evs[0] - 1) == 0 and sp.simplify(evs[1] + 1 / phi) == 0
h1_time = sp.simplify((1 - phi) ** 2 - phi ** -2) == 0
print(f"  T = {T.tolist()}   row-stochastic: {h1_stoch}")
print(f"  eigenvalues = {{{sp.nsimplify(evs[0])}, {sp.nsimplify(evs[1], [sp.sqrt(5)])}}}  == {{1, -1/phi}}: {h1_ev}")
print(f"  time=basepoint identity (1-phi)^2 == phi^-2: {h1_time}")
R["H1_b768"] = {"stochastic": bool(h1_stoch), "eigs_1_and_minus_inv_phi": bool(h1_ev),
                "time_basepoint_identity": bool(h1_time)}

print()
print("=" * 80)
print("H2  B489: torsion = |L(2n) - 2| = (phi^n - phi^-n)^2, and >= 5 for all n >= 2")
print("=" * 80)
h2_ok = True
rows = []
for n in range(1, 17):
    L2n = sp.simplify(phi ** (2 * n) + psi ** (2 * n))     # Lucas L(2n)
    tors = sp.simplify(sp.Abs(L2n - 2))
    binet = sp.simplify((phi ** n - phi ** (-n)) ** 2)     # phi^-n POSITIVE (not psi^n)
    match = sp.simplify(tors - binet) == 0
    ge5 = (n < 2) or (sp.N(tors) >= 5)
    h2_ok &= match and ge5
    rows.append((n, int(tors), bool(match), bool(ge5)))
    if n <= 4 or n == 16:
        print(f"  n={n:2d}: |L(2n)-2| = {tors}, (phi^n-phi^-n)^2 = {binet}, match={match}, >=5={ge5}")
print(f"  all n=1..16 identity holds AND torsion>=5 for n>=2: {h2_ok}")
R["H2_b489"] = {"binet_torsion_all_n": bool(h2_ok), "rows": rows}

print()
print("=" * 80)
print("H3  TOMB-L255: Sym^d(diag(phi,-1/phi)) spectrum = {(-1)^j phi^(d-2j) : j=0..d}")
print("=" * 80)
lam, mu = phi, -1 / phi
h3_ok = True
for d in range(1, 13):
    got = sorted((sp.simplify(lam ** (d - j) * mu ** j) for j in range(d + 1)), key=lambda z: sp.N(z))
    pred = sorted((sp.simplify((-1) ** j * phi ** (d - 2 * j)) for j in range(d + 1)), key=lambda z: sp.N(z))
    m = all(sp.simplify(a - b) == 0 for a, b in zip(got, pred))
    h3_ok &= m
    if d <= 3 or d == 12:
        print(f"  d={d:2d}: spectrum = {[sp.nsimplify(x, [sp.sqrt(5)]) for x in pred]}  match={m}")
print(f"  all d=1..12 Sym^d spectrum matches the closed form: {h3_ok}")
R["H3_l255"] = {"symd_spectrum_all_d": bool(h3_ok)}

print()
print("=" * 80)
print("P1  WALL-7 (cited, NOT re-run): cc3 sampled 18 weld points, all dim=0 (a SAMPLE).")
print("    Evidence, not a generic proof. Provenance: hunt/wall7-twisted-extension.")
print("=" * 80)
R["P1_wall7"] = {"status": "cited-not-rerun", "cc3_sample_points": 18, "all_dim0": True,
                 "is_proof": False}

print()
overall = h1_stoch and h1_ev and h1_time and h2_ok and h3_ok
R["all_harvested_reproduced"] = bool(overall)
print(f"ALL HARVESTED CLAIMS INDEPENDENTLY REPRODUCED: {overall}")
print("EXCLUDED at the gate: the b769/C21 tangent-frame-alignment claim (c-odd/theta-odd "
      "conflation); see the C21 correction in main.")

import json
with open("results.json", "w") as f:
    json.dump(R, f, indent=1)
print("wrote results.json")
