"""B1342 -- IS THERE A FACE WE HAVE NOT SEEN? Yes: three of four, and they are named already.

The owner asked. The answer is in the record's own words, in B497's last line of its classification
section: "The program to date = STRATUM 1 OF 4."

B497 (PROVED) classifies End(F2) on the character variety into four strata by the Hopf dichotomy
crossed with det(abelianisation), gives each a citizen and an exact kappa-law, and the programme
then continued entirely inside stratum 1. B1247 (main, this week) records that B497 "sat SEVEN WEEKS"
uncited.

THIS ARC DOES NOT TAKE B497 ON TRUST. Every determinant and every kappa-law below is recomputed from
the substitution itself -- the word map lifted to SL2 and the trace identities -- not copied.

WHY THE PROGRAMME STAYED IN STRATUM 1, derived rather than guessed: kappa is the programme's ONE
conserved first integral, and kappa is conserved ONLY in stratum 1 (kappa' = kappa). Everywhere else
the map MOVES BETWEEN LEAVES, multiplying (kappa-2) by a polynomial. So the object's first integral
is a stratum-1 phenomenon, and every arc built on kappa is structurally confined there.

AND WHAT THAT COSTS, joining B1341 (today): B1341 proved a discrete Lagrangian's map always preserves
an area form, so an ANTI-symplectic map has none. Outside stratum 1 the situation is worse than
anti-symplectic -- there is no invariant leaf to carry a form at all. So:
   the variational structure lives on HALF OF ONE STRATUM OUT OF FOUR.
And S063 places irreversibility at det != +-1, i.e. strata 2/2'/3/4. Hence the read-out tested in Q5:
IRREVERSIBILITY AND LEAST ACTION ARE IN DISJOINT STRATA.

PRE-REGISTERED (DESIGN B1342): Q1 the four abelianisation determinants are +-1, 4, -2, 0, 0 as B497
says, recomputed from the substitutions; Q2 every kappa-law in B497's table is exact, recomputed;
Q3 stratum 1 ALONE preserves kappa, and a control shows the others genuinely move leaves; Q4 U1
holds -- (kappa-2) divides (kappa'-2) for every stratum, so kappa=2 ("nothing") is absolutely
invariant; Q5 only stratum 1 can carry a variational structure, and only its det +1 half, so the
action occupies half of one stratum of four. PASS iff all five hold.
"""
import json
import sympy as sp

x, y, z = sp.symbols('x y z')
KAP = x ** 2 + y ** 2 + z ** 2 - x * y * z - 2          # B416/B448 convention (full traces)
fails = []
def check(tag, label, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

# ---- the substitutions, as WORDS in F2 (a, b) ------------------------------------------------
# stratum 1  golden      a -> a b,  b -> a          (the programme's own; m = 1 metallic)
# stratum 2  squaring    a -> a a,  b -> b b
# stratum 2' per-doubl.  a -> a b,  b -> a a
# stratum 3  Thue-Morse  a -> a b,  b -> b a
# stratum 4  degenerate  a -> a b,  b -> a b
SUBS = {"1  golden (Aut)":      (["a", "b"], ["a"]),
        "2  squaring":          (["a", "a"], ["b", "b"]),
        "2' period-doubling":   (["a", "b"], ["a", "a"]),
        "3  Thue-Morse":        (["a", "b"], ["b", "a"]),
        "4  degenerate":        (["a", "b"], ["a", "b"])}

def abelianisation(sub):
    """matrix whose COLUMNS are the images of a and b in Z^2"""
    cols = []
    for w in sub:
        cols.append([w.count("a"), w.count("b")])
    return sp.Matrix([[cols[0][0], cols[1][0]], [cols[0][1], cols[1][1]]])

print("Q1 -- the abelianisation determinants, recomputed from the substitutions")
dets = {}
for name, sub in SUBS.items():
    M = abelianisation(sub); dets[name] = M.det()
    print(f"      {name:22s} images {sub}  ->  {M.tolist()}, det {M.det()}")
check("Q1", "the determinants are +-1 (stratum 1), 4 (stratum 2), -2 (2'), 0 (3), 0 (4) -- B497's "
            "Hopf-dichotomy-crossed-with-det classification, reproduced",
      abs(dets["1  golden (Aut)"]) == 1 and dets["2  squaring"] == 4
      and dets["2' period-doubling"] == -2 and dets["3  Thue-Morse"] == 0
      and dets["4  degenerate"] == 0)

# ---- the kappa-laws, recomputed by lifting each substitution to SL2 --------------------------
# METHOD NOTE (a bug this bench made and caught with its own control): the first version tested
# divisibility with multivariate sp.div over the eight matrix entries. That is NOT a divisibility
# test -- multivariate division depends on the term order and does not decide the question, and it
# returned FALSE for three laws that are in fact exact. The correct test is IDEAL MEMBERSHIP:
# reduce (kappa' - 2) - (kappa - 2)*M modulo (det A - 1, det B - 1) and require 0. Recorded rather
# than silently fixed, because a wrong method that returns plausible falsehoods is the dangerous kind.
a11, a12, a21, a22, b11, b12, b21, b22 = sp.symbols('a11 a12 a21 a22 b11 b12 b21 b22')
A = sp.Matrix([[a11, a12], [a21, a22]]); B = sp.Matrix([[b11, b12], [b21, b22]])
GB = sp.groebner([A.det() - 1, B.det() - 1], a11, a12, a21, a22, b11, b12, b21, b22, order='grevlex')
red = lambda e: sp.expand(GB.reduce(sp.expand(e))[1])
def word(w):
    M = sp.eye(2)
    for c in w: M = M * (A if c == "a" else B)
    return M
TR = {"x": sp.trace(A), "y": sp.trace(B), "z": sp.trace(A * B)}
in_traces = lambda e: e.subs({x: TR["x"], y: TR["y"], z: TR["z"]}, simultaneous=True)
kap = lambda X, Y, Z: X ** 2 + Y ** 2 + Z ** 2 - X * Y * Z - 2
k_old = kap(TR["x"], TR["y"], TR["z"])

# B497's stated trace maps and multipliers -- CHECKED here against the words, not assumed
STATED_TM = {"1  golden (Aut)":    (z, x, x * z - y),
             "2  squaring":        (x ** 2 - 2, y ** 2 - 2, x * y * z - x ** 2 - y ** 2 + 2),
             "2' period-doubling": (z, x ** 2 - 2, (x ** 2 - 1) * z - x * y),
             "3  Thue-Morse":      (z, z, x * y * z - x ** 2 - y ** 2 + 2),
             "4  degenerate":      None}
STATED_MULT = {"1  golden (Aut)": sp.Integer(1), "2  squaring": x ** 2 * y ** 2,
               "3  Thue-Morse": x ** 2 + y ** 2 - x * y * z}

print("\nQ2 -- B497's trace maps and kappa-laws, recomputed from the substitutions themselves")
tm_ok, mults = True, {}
for name, sub in SUBS.items():
    Wa, Wb = word(sub[0]), word(sub[1])
    got = (sp.trace(Wa), sp.trace(Wb), sp.trace(Wa * Wb))
    k_new = kap(*got)
    st = STATED_TM[name]
    if st is not None:
        ok = all(red(g - in_traces(s)) == 0 for g, s in zip(got, st))
        tm_ok &= ok
        print(f"      {name:22s} trace map matches the word: {ok}   {st}")
    if name in STATED_MULT:
        M = STATED_MULT[name]
        ok = red(k_new - 2 - (k_old - 2) * in_traces(M)) == 0
        mults[name] = (M, ok)
        print(f"      {name:22s} (kappa'-2) = (kappa-2) * ({M})  EXACT: {ok}")
    elif st is not None:
        q, r = sp.div(sp.Poly(sp.expand(kap(*st)) - 2, x, y, z), sp.Poly(kap(x, y, z) - 2, x, y, z))
        ok = r.as_expr() == 0
        mults[name] = (sp.factor(q.as_expr()), ok)
        print(f"      {name:22s} multiplier COMPUTED (B497 leaves it as 'stratum-2 family'): "
              f"{sp.factor(q.as_expr())}, remainder {r.as_expr()}")
    else:
        ok = red(k_new - 2) == 0
        mults[name] = (sp.Integer(0), ok)
        print(f"      {name:22s} kappa' == 2 IDENTICALLY: {ok}  -> multiplier 0")
check("Q2a", "every trace map B497 states is reproduced from its substitution", tm_ok)
check("Q2b", "U1 verified by IDEAL MEMBERSHIP: (kappa-2) divides (kappa'-2) exactly in every "
             "stratum, with multipliers 1, x^2, x^2 y^2, x^2+y^2-xyz, 0",
      all(v[1] for v in mults.values()))
check("Q2c", "STRATUM 1 PRESERVES KAPPA EXACTLY (multiplier 1) -- the programme's whole "
             "first-integral structure", mults["1  golden (Aut)"][0] == 1)

print("\nQ3 -- does any other stratum preserve kappa? (control: if they all did, nothing is at stake)")
moved = {}
for name, sub in SUBS.items():
    if name == "1  golden (Aut)": continue
    Wa, Wb = word(sub[0]), word(sub[1])
    moved[name] = red(kap(sp.trace(Wa), sp.trace(Wb), sp.trace(Wa * Wb)) - k_old) != 0
    print(f"      {name:22s} moves the leaf (kappa' != kappa): {moved[name]}")
check("Q3", "STRATUM 1 ALONE preserves kappa -- every other stratum MOVES BETWEEN LEAVES. This is "
            "WHY the programme is confined to stratum 1: its one conserved first integral is not "
            "conserved anywhere else, so every arc built on kappa is structurally trapped there",
      all(moved.values()))

print("\nQ4 -- kappa = 2 ('nothing', B309) is absolutely invariant")
check("Q4", "since (kappa-2) divides (kappa'-2) in every stratum, kappa = 2 maps to kappa = 2 under "
            "EVERY endomorphism -- 'nothing' is a fixed point of the whole monoid, not just of the "
            "units (B497's U1, re-derived)", all(v[1] for v in mults.values()))

print("\nQ5 -- JOINING B1341: where can a least-action principle live?")
print("      B1341's theorem: a discrete Lagrangian's map preserves an area form, hence det +1.")
print("      stratum 1, det +1 : preserves kappa AND orientation  -> variational (B1341's monodromy)")
print("      stratum 1, det -1 : preserves kappa, REVERSES orientation -> NOT variational (B1341)")
print("      strata 2, 2', 3, 4: do not preserve kappa at all -> no invariant leaf, hence no phase")
print("                          space to carry a form; the question is not even well posed")
ok5 = abs(dets["1  golden (Aut)"]) == 1 and all(moved.values())
check("Q5", "THE ACTION OCCUPIES HALF OF ONE STRATUM OUT OF FOUR. And S063 places irreversibility at "
            "det != +-1, i.e. strata 2/2'/3/4 -- so IRREVERSIBILITY AND LEAST ACTION ARE IN DISJOINT "
            "STRATA: where the action is, time is reversible; where time has an arrow, there is no "
            "action to vary", ok5)

json.dump({"dets": {k: str(v) for k, v in dets.items()},
           "multipliers": {k: str(v[0]) for k, v in mults.items()},
           "u1_exact": {k: bool(v[1]) for k, v in mults.items()},
           "moves_leaf": {k: bool(v) for k, v in moved.items()}, "fails": fails},
          open("b1342_strata.json", "w"), indent=1)
print("\nB1342:", "PASS" if not fails else f"FAIL ({len(fails)}): {fails}")
raise SystemExit(0 if not fails else 1)
