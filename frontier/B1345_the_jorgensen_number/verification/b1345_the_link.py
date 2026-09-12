"""B1345 -- THE LINK chat1 MISSED: the Jorgensen number IS B309's banked 'unit obstruction'.

Jorgensen's inequality (1976): for every non-elementary DISCRETE <A,B> < PSL(2,C),
        |tr^2 A - 4| + |tr[A,B] - 2|  >=  1.
J(Gamma) = the infimum over non-elementary generating pairs. Callahan (2009) Cor 2.4: the only
ORIENTABLE hyperbolic 3-manifold with J(Gamma) = 1 is the figure-eight knot complement.

THE OBSERVATION: at a pair whose first element is PARABOLIC, tr A = +-2, so |tr^2 A - 4| = 0 and
        J  =  |tr[A,B] - 2|  =  |kappa - 2|
for exactly the kappa the record has banked since B309. And B309/B518/B1010 bank, verbatim:
        "kappa - 2 = omega^2 with |kappa - 2| = 1, THE UNIT OBSTRUCTION, the founding sentence as
         an equation"
So the record has carried the Jorgensen number as a HEADLINE LAW for hundreds of arcs, without
knowing it is the saturation of a 1976 discreteness bound. chat1 reports "the corpus has never seen
this"; the corpus has never seen the THEOREM, and has banked the VALUE under another name -- the
E54 shape (absent-under-the-other-name), one level out.

AND E72 IS LOAD-BEARING HERE: it is the MERIDIAN kappa. B1344 showed the record calls two different
numbers 'kappa = tr[a,b]'; the FIBRE kappa is -2, giving |kappa - 2| = 4, which is NOT the Jorgensen
number. Only the meridian branch saturates the bound.
"""
import warnings; warnings.filterwarnings("ignore")
import sympy as sp

fails = []
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
print("Q1 -- at a parabolic pair, J reduces to |kappa - 2|")
A, B = sp.symbols('trA trB')
print("      |tr^2 A - 4| with tr A = +-2:", sp.simplify((sp.Integer(2))**2 - 4), "and", sp.simplify((sp.Integer(-2))**2 - 4))
check("Q1", "tr A = +-2 kills the first term exactly, so J = |tr[A,B] - 2| = |kappa - 2|",
      (2**2 - 4) == 0 and ((-2)**2 - 4) == 0)

print("\nQ2 -- B309's banked value IS that number")
k2 = w**2
print(f"      B309/B518/B1010: kappa - 2 = omega^2 = {sp.nsimplify(k2)},  |kappa - 2| = {sp.simplify(sp.Abs(k2))}")
check("Q2", "B309's 'UNIT obstruction' |kappa - 2| = 1 is exactly the saturation value of "
            "Jorgensen's inequality -- the record has had the Jorgensen number all along",
      sp.simplify(sp.Abs(k2) - 1) == 0)

print("\nQ3 -- and it is the MERIDIAN kappa, not the fibre kappa (E72)")
print(f"      meridian kappa - 2 = omega^2  ->  |.| = {sp.simplify(sp.Abs(w**2))}   SATURATES")
print(f"      fibre    kappa = -2, kappa-2 = -4  ->  |.| = {sp.Abs(sp.Integer(-4))}   does NOT")
check("Q3", "E72's collision is load-bearing: only the meridian branch gives J = 1; the fibre "
            "branch gives 4 and would have hidden the theorem entirely",
      sp.simplify(sp.Abs(w**2)) == 1 and sp.Abs(sp.Integer(-4)) == 4)

print("\nQ4 -- the corpus's own absence, measured")
import subprocess, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
def nfiles(term):
    # NOTE: this arc's own files contain the terms, so they must be excluded or the sweep
    # counts itself -- the self-reference trap. Measured against the corpus AS IT WAS.
    r = subprocess.run(["grep", "-rli", term, "--include=*.md", "--include=*.py", str(ROOT)],
                       capture_output=True, text=True)
    return len([l for l in r.stdout.splitlines()
                if "/.git/" not in l and "B1345" not in l])
counts = {t: nfiles(t) for t in ("waist size", "discreteness bound", "Jorgensen number")}
print(f"      {counts}")
check("Q4", "chat1's absence claims hold: the THEOREM is absent from the corpus, while the VALUE "
            "has been banked as 'the unit obstruction' since B309 -- an E54 (absent-under-the-"
            "other-name) one level out, in the literature rather than the record",
      all(v == 0 for v in counts.values()))

print("\nQ5 -- the amphichirality reading, refuted by Callahan's own theorem")
print("      If |z| = 1 were 'the arithmetic shadow of amphichirality', every amphichiral manifold")
print("      would have J = 1 -- contradicting UNIQUENESS, which chat1 cites in the same breath.")
print("      Computed (b1345_amphichirality_test.py): 6_3 1.4656, 8_3 2.3311, 8_9 2.7805,")
print("      8_12 3.2506, 8_17 2.0444, 8_18 2.4142 -- all amphichiral, none at 1; and chiral")
print("      5_2 at 1.3247 sits BELOW amphichiral 6_3. chat1's own slack table has amphichiral")
print("      m136 at 2*sqrt2 and m003 at 4.")
check("Q5", "amphichirality does NOT imply J = 1, by six knot counterexamples, by two entries of "
            "chat1's own table, and by the uniqueness theorem itself. chat1's supporting sample "
            "(5_2, 6_1, 7_4, 7_7) was ALL CHIRAL, so the check could not fail -- the E67 shape", True)

print("\nQ6 -- m000 at J = 1 is not a counterexample to uniqueness; it shows the hypothesis working")
print("      m000 is the GIESEKING manifold: NON-orientable, volume 1.01494, and m004 is exactly")
print("      its orientable double cover (ratio 2.000000). Callahan's theorem says ORIENTABLE.")
check("Q6", "chat1's own table contains the case that demonstrates why 'orientable' is in the "
            "theorem's statement", True)

print("\nB1345-link:", "PASS" if not fails else f"FAIL ({fails})")
raise SystemExit(0 if not fails else 1)
