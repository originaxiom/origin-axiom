#!/usr/bin/env python3
"""B8099 -- the 2+1 theory's completeness audit: what is present, what is missing, and
WHICH THEORY the question is about.

Owner-elected: 'complete the 3d theory' as an alternative to lifting to 3+1. Before building,
this measures. Every classical datum verified in-sandbox; every corpus claim cited to its arc.
Gate 5 untouched -- no measured physics value anywhere.
"""
import json, os, math
import snappy, mpmath as mp
mp.mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
FAIL = []
def gate(l, ok, d=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {l}" + (f"  {d}" if d else ""))
    if not ok: FAIL.append(l)

M = snappy.Manifold('4_1')
V = float(M.volume()); CS = float(M.chern_simons())
shapes = [complex(z) for z in M.tetrahedra_shapes('rect')]
w = complex(math.cos(math.pi/3), math.sin(math.pi/3))
def lob(t): return -mp.quad(lambda x: mp.log(abs(2*mp.sin(x))), [0, t])
Vtet = float(3*lob(mp.pi/3))

print("=" * 74); print("1. THE CLASSICAL DATUM -- verified here, not cited"); print("=" * 74)
gate("geometric solution (all tetrahedra positively oriented)",
     M.solution_type() == 'all tetrahedra positively oriented')
gate("two tetrahedra, one cusp", len(shapes) == 2 and M.num_cusps() == 1)
gate("both shapes are the REGULAR ideal tetrahedron e^{i pi/3}",
     all(abs(z - w) < 1e-9 for z in shapes))
gate("Vol(4_1) = 2 x 3*Lambda(pi/3) exactly", abs(V - 2*Vtet) < 1e-9,
     f"{V:.15f} vs {2*Vtet:.15f}")
gate("CS = 0 (amphichiral) -- the complex volume is PURELY REAL", abs(CS) < 1e-12,
     f"CS = {CS:.3e}")
gate("H_1 = Z (torsion-free)", str(M.homology()).replace(' ','') == 'Z')

print()
print("=" * 74); print("2. THE COMPLETENESS CHECKLIST"); print("=" * 74)
CHECK = [
 ("classical solution",        "PRESENT",  "verified here: 2 regular ideal tetrahedra, geometric"),
 ("cosmological constant",     "PRESENT",  "Lambda = -1 exactly (B259)"),
 ("the action",                "PRESENT",  "forced (B1012)"),
 ("boundary central charge",   "PRESENT",  "c = 6 sigma, derived twice (B1012; Brown-Henneaux)"),
 ("complex CS action Vol+iCS", "PRESENT",  "verified here: purely REAL, CS = 0"),
 ("the 3d-3d theory T[4_1]",   "PRESENT",  "B262: U(1) with 2 chirals, from the DGG dictionary"),
 ("state integral",            "PARTIAL",  "B262/B269 rungs; not a closed evaluation"),
 ("matter spectrum",           "AMBIGUOUS","T[4_1] gives 2 chirals; the corpus's E6 route gives the 27"),
 ("E6 as a DYNAMICAL gauge",   "MISSING",  "B262's own wall #2 -- open"),
 ("E6 state integral",         "MISSING",  "OPEN_PROBLEMS, flagged SPECIALIST"),
 ("the 4d lift",               "MISSING",  "B262's own wall #4"),
]
for name, st, note in CHECK:
    print(f"  {st:<10} {name:<26} {note}")
present = sum(1 for _,s,_ in CHECK if s == "PRESENT")
gate("six of eleven requirements PRESENT", present == 6, f"{present}/11")

print()
print("=" * 74); print("3. THE HEADLINE -- there are TWO theories, not one"); print("=" * 74)
print("""  The corpus attaches TWO different 3d theories to the SAME manifold:

    (A)  T[4_1]  = U(1) with 2 chirals        -- 3d-3d/DGG, from the triangulation (B262).
                                                  ABELIAN. Standard type (A_1).
    (B)  the E6 structure                     -- from the corpus's own charge-frame route,
                                                  with the 27 as matter.

  These are NOT the same theory, and B262 knew it: its wall #2 is literally
  'is E6 ever dynamical'. So 'complete the 3d theory' is AMBIGUOUS until answered,
  and the two branches have very different novelty:

    completing (A) is largely LITERATURE -- DGG built T[4_1]; the L173 discipline applies,
      and reproducing it is a re-derivation, not a result.
    completing (B) is THE PROGRAMME -- and 3d-3d does NOT reach it: the E6 state integral
      is an open problem flagged SPECIALIST, not a computation we can run.

  CONSEQUENCE FOR THE LIFT QUESTION: 3d-3d takes a 3-MANIFOLD to a 3d theory. It is not a
  lift to 3+1 and cannot become one -- 4d from the same 6d theory needs a RIEMANN SURFACE
  (class S), not a 3-manifold. The dimensional question is untouched by this route.""")

print()
print("=" * 74); print("4. WHAT CS = 0 BUYS, AND COSTS"); print("=" * 74)
print("""  The object's complex CS action is purely real, so the ENTIRE content of the classical
  action is the VOLUME. No CS phase, no theta-like term. That is a genuine simplification
  -- and it is also why the arithmetic-CS lane (C5) reduces to the VOLUME analogue: there
  is no CS term left to be the analogue of.""")

RES = {"volume": V, "chern_simons": CS, "complex_volume_purely_real": abs(CS) < 1e-12,
       "vol_equals_two_regular_ideal_tetrahedra": abs(V - 2*Vtet) < 1e-9,
       "regular_ideal_shape": True, "n_tetrahedra": 2, "n_cusps": 1,
       "checklist": [{"requirement": n, "status": s, "note": d} for n, s, d in CHECK],
       "n_present": present, "n_total": len(CHECK),
       "two_theories": {"A": "T[4_1] = U(1) + 2 chirals (3d-3d/DGG, B262) -- ABELIAN",
                        "B": "the E6 structure with the 27 (the corpus's own route)"},
       "headline": "'complete the 3d theory' is AMBIGUOUS until (A) or (B) is named; completing A is largely literature, completing B is the programme and 3d-3d does not reach it",
       "3d3d_is_not_a_4d_lift": "3d-3d takes a 3-manifold to a 3d theory; 4d from the same 6d theory needs a Riemann surface (class S), so the dimensional question is untouched",
       "scope": ("An AUDIT, not a construction. Classical data verified in-sandbox; corpus "
                 "statuses cited to their arcs and NOT re-derived. Says nothing about whether "
                 "either theory can be completed -- it says which question is being asked. "
                 "No measured physics value; Gate 5 untouched.")}
json.dump(RES, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)
print("\n  results.json written")
if FAIL: raise SystemExit(f"FAILED: {FAIL}")
print("\n  ALL CHECKS PASS")
