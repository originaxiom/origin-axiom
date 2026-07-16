"""B647 cell 2 — chain-level swap equivariance (prereg d3e4faad).

M2-G1: for each S_eval appearing in Y, is
    S_side1(J-transported side-2 cocycles; a, LONG)
  = kconj( S_side2(original side-2 cocycles; a, LONG^{-1}) )
per evaluation (BEFORE antisymmetrization)? And the reverse transport.
Report per-pair TRUE/FALSE with defects; sanity: the antisymmetrized
differences must reproduce the banked cohomological law.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
B637 = os.path.join(HERE, "..", "B637_corrected_cell3")
mod = {"__name__": "b637_module",
       "__file__": os.path.join(B637, "b637_threeform.py")}
exec(compile(open(os.path.join(B637, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
side1 = mod["side1"]
double_Y = mod["double_Y"]
apply_ = mod["apply"]
kconj = mod["kconj"]
U27, U27i = mod["U27"], mod["U27i"]

Yn, reps, sides_of, side2 = double_Y(None, verbose=False)

P1 = freduce("a" + LONG)
MU2, LAM2 = "a", inv(LONG)
P2 = freduce("a" + inv(LONG))


def Jop(v):
    return apply_(U27, [kconj(x) for x in v])


def Jop_inv(v):
    return [kconj(x) for x in apply_(U27i, v)]


def jvec(zpair):
    # sides_of gives (v_letter1, v_letter2), each a 27-vector
    return (Jop(zpair[0]), Jop(zpair[1]))


def jvec_inv(zpair):
    return (Jop_inv(zpair[0]), Jop_inv(zpair[1]))


TRIPLES = [(1, 3, 4), (0, 2, 3), (1, 2, 3), (2, 3, 4)]
for (i, j, k2) in TRIPLES:
    (a1, a2), (b1, b2), (c1, c2) = map(sides_of,
                                       (reps[i], reps[j], reps[k2]))
    om2 = side2.make_omega(a2, b2, c2)
    om1J = side1.make_omega(jvec(a2), jvec(b2), jvec(c2))
    om1 = side1.make_omega(a1, b1, c1)
    om2J = side2.make_omega(jvec_inv(a1), jvec_inv(b1), jvec_inv(c1))

    print(f"== triple {(i, j, k2)} ==", flush=True)
    pairs = [("(mu,lam)", ("a", LONG, P1), (MU2, LAM2, P2)),
             ("(lam,mu)", (LONG, "a", P1), (LAM2, MU2, P2))]
    for nm, (g1, h1, gh1), (g2, h2, gh2) in pairs:
        B2 = side2.S_eval(om2, g2, h2, gh2)
        A1 = side1.S_eval(om1J, g1, h1, gh1)
        d = A1 - kconj(B2)
        print(f"  fwd {nm}: S1(J z2) == conj S2(z2): {d.is_zero()}"
              + ("" if d.is_zero() else f"  defect {d}"), flush=True)
        B1 = side1.S_eval(om1, g1, h1, gh1)
        A2 = side2.S_eval(om2J, g2, h2, gh2)
        d2 = A2 - kconj(B1)
        print(f"  rev {nm}: S2(Jinv z1) == conj S1(z1): {d2.is_zero()}"
              + ("" if d2.is_zero() else f"  defect {d2}"), flush=True)

print("\nB647 cell 2 DONE", flush=True)
