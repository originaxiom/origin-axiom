#!/usr/bin/env python3
"""R04 POST-DIFF cross-check (written AFTER opening the arcs' scripts).

Two purposes:
 1. Run the ARCS' exact generation objects (B861 uses the 16 alone at step 2 and
    10+5bar at step 3; my blind run used the full 27-content at every step)
    through MY conjugation instrument -- verdicts must agree.
 2. Verify the reconciliation lemma: adding a self-conjugate multiset S to M
    never changes chiral(M) (conjugation is additive and Counter addition is
    cancellative), so the full-27 vs generation-slice conventions provably
    agree at steps 2 and 3.  Checked numerically on the actual contents.
"""
from collections import Counter
import importlib.util, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("blind", os.path.join(HERE, "r04_blind_recompute.py"))
blind = importlib.util.module_from_spec(spec)
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(blind)

C, chiral, conj_content = blind.C, blind.chiral, blind.conj_content

# --- the arcs' exact objects, re-labelled in my atom scheme -----------------
# B861 step 2: the 16 alone under SU(5)xU(1) and Pati-Salam
arc_step2 = {
    "SU(5)xU(1)": C(("su5.10",), ("su5.5b",), ("su5.1",)),
    "Pati-Salam": C(("su4.4", "su2.2", "su2.1"), ("su4.4b", "su2.1", "su2.2")),
}
# B861 step 3: the generation 10+5bar under SU(4)xU(1) and SM
arc_step3 = {
    "SU(4)xU(1)": C(("su4.6",), ("su4.4",), ("su4.4b",), ("su4.1",)),
    "SM": C(("su3.3", "su2.2"), ("su3.3b", "su2.1"), ("su3.3b", "su2.1"),
            ("su3.1", "su2.2"), ("su3.1", "su2.1")),
}
print("arcs' exact generation objects under MY instrument:")
for name, M in {**arc_step2, **arc_step3}.items():
    print("  %-12s chiral=%s" % (name, chiral(M)))
assert chiral(arc_step2["SU(5)xU(1)"]) and chiral(arc_step2["Pati-Salam"])
assert not chiral(arc_step3["SU(4)xU(1)"]) and chiral(arc_step3["SM"])

# --- reconciliation lemma, checked on the actual differences ----------------
# step 2 difference: full 27-content minus the 16 = branched(10) + branched(1)
diff2_su5 = blind.step2["SU(5)xU(1)"] - arc_step2["SU(5)xU(1)"]
diff2_ps = blind.step2["Pati-Salam"] - arc_step2["Pati-Salam"]
# step 3 difference: full 27-content minus (10+5bar)
diff3_su4 = blind.step3["SU(4)xU(1)"] - arc_step3["SU(4)xU(1)"]
diff3_sm = blind.step3["SM"] - arc_step3["SM"]
for tag, D in [("step2 SU(5) slice", diff2_su5), ("step2 PS slice", diff2_ps),
               ("step3 SU(4) slice", diff3_su4), ("step3 SM slice", diff3_sm)]:
    sc = (D == conj_content(D))
    print("  difference multiset %-18s self-conjugate: %s  %s" % (tag, sc, dict(D)))
    assert sc, "convention gap would NOT be verdict-neutral: " + tag
print("LEMMA HOLDS: every convention difference is a self-conjugate addition;")
print("full-27 and generation-slice conventions provably give identical verdicts.")
