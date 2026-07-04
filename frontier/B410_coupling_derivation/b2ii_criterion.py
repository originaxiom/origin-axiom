"""B410 2b-ii -- derive the convolution-cancellation criterion.

s(√-15) content of a pair comes ONLY from products where the 3-side factor carries √-3
AND the 5-side factor carries √5 (√-3·√5 = √-15). So:
  pair is s-BRIGHT  <=>  EXISTS a convolution cell (A,B) and a split (a,b)+(a',b')=(A,B)
                        with X3(a,b) carrying √-3 and X5(a',b') carrying √5.
Derived criterion: bright <=> (√-3-active freqs of X3) convolves nonempty into support
with (√5-active freqs of X5). Test 5/5 separation dark-C vs bright controls."""
import json, os, sys
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "B358_seam_certification"))
sys.path.insert(0, os.path.join(HERE, "..", "B367_value_map"))
sys.path.insert(0, os.path.join(HERE, "..", "B386_crt_closed_form"))
import cyclo_engine as E
import seam_certification as SC
from step0_exact_matrices import build_theta_W, matrix_order
from tensor_gate import local_partrace_table

def active_freqs(m1, m2, side, comp):
    """freqs (a,b) where the local-side spectrum carries the given H-component (2=√-3, 1=√5)."""
    o1,_ = matrix_order(build_theta_W(m1)); o2,_ = matrix_order(build_theta_W(m2))
    T = local_partrace_table(3 if side == 3 else 5, 2, m1, m2, o1, o2)
    z1, z2 = 60//o1, 60//o2
    out = set()
    for a in range(o1):
        for b in range(o2):
            t = E.ZERO
            for j in range(o1):
                za = E.zeta((-z1*j*a) % 60)
                for l in range(o2):
                    t = E.add(t, E.mul(E.mul(za, E.zeta((-z2*l*b) % 60)), T[(j,l)]))
            sol = SC.solve_H(SC.H_avg(E.scal(Fr(1, o1*o2), t)))
            if sol and sol[comp] != 0: out.add((a, b, o1, o2))
    return out, o1, o2

PAIRS = [((1,3),"dark"),((1,4),"dark"),((3,5),"dark"),((3,4),"bright"),((2,3),"bright")]
res = {}
for (m1, m2), st in PAIRS:
    A3, o1, o2 = active_freqs(m1, m2, 3, 2)    # √-3-active on 3-side
    A5, _, _   = active_freqs(m1, m2, 5, 1)    # √5-active on 5-side
    # convolution: does some (a,b)+(a',b') land on ANY cell? (mod o1,o2)
    conv = set()
    for (a, b, _, _) in A3:
        for (a2, b2, _, _) in A5:
            conv.add(((a+a2) % o1, (b+b2) % o2))
    bright_pred = len(A3) > 0 and len(A5) > 0 and len(conv) > 0
    res[f"{m1},{m2}"] = dict(status=st, n3=len(A3), n5=len(A5),
                             conv_cells=len(conv), predict="bright" if bright_pred else "dark",
                             match=(("bright" if bright_pred else "dark") == st))
    print(f"({m1},{m2}) {st:7s}: |√-3-active X3|={len(A3)}, |√5-active X5|={len(A5)}, "
          f"conv={len(conv)} -> predict {'bright' if bright_pred else 'dark'} "
          f"{'OK' if res[f'{m1},{m2}']['match'] else 'MISS'}")
allok = all(v["match"] for v in res.values())
print("CRITERION 5/5:", allok)
res["all_match"] = allok
json.dump(res, open(os.path.join(HERE, "b2ii_criterion.json"), "w"), indent=1)
print("DONE")
