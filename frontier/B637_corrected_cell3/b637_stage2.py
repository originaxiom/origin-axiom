"""B637 part 2b stage 2 — the class-level gates on the 3-form, then the
bent-weld doubles' tables (prereg 99815a48).

Gates on the unbent double (all must pass before any value is banked):
  G-A coboundary invariance in each slot (z -> z + delta v);
  G-B antisymmetry under slot transpositions (sign flip, two checks);
  G-C section independence (sig(mu lam) = LONG+a instead of a+LONG).
Then: the 10-component tables for m in {1, 5, 7, 11}.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
mod = {"__name__": "b637_module", "__file__": os.path.join(
    HERE, "b637_threeform.py")}
exec(compile(open(os.path.join(HERE, "b637_threeform.py")).read(),
             "b637_threeform.py", "exec"), mod)

K, K0, K1 = mod["K"], mod["K0"], mod["K1"]
freduce, inv = mod["freduce"], mod["inv"]
LONG = mod["LONG"]
side1, Side = mod["side1"], mod["Side"]
double_Y = mod["double_Y"]
apply_ = mod["apply"]

print("\n==== stage 2: the class-level gates (unbent double) ====", flush=True)
Yn, reps, sides_of, side2 = double_Y(None, verbose=False)


def Yval(z_a, z_b, z_c, prod1="aL", s2obj=side2):
    (a1, a2) = sides_of(z_a)
    (b1, b2) = sides_of(z_b)
    (c1, c2) = sides_of(z_c)
    om1 = side1.make_omega(a1, b1, c1)
    om2 = s2obj.make_omega(a2, b2, c2)
    MU1, LAM1 = "a", LONG
    P1 = freduce("a" + LONG) if prod1 == "aL" else freduce(LONG + "a")
    MU2, LAM2 = "a", inv(LONG)
    P2 = freduce("a" + inv(LONG))
    S1 = lambda g, h, gh: side1.S_eval(om1, g, h, gh)
    S2 = lambda g, h, gh: s2obj.S_eval(om2, g, h, gh)
    return (S1(MU1, LAM1, P1) - S1(LAM1, MU1, P1)) \
         - (S2(MU2, LAM2, P2) - S2(LAM2, MU2, P2))


y0 = Yn[(0, 1, 2)]
print(f"reference Y[012] = {y0}", flush=True)

# G-A: coboundary shifts per slot
lets4letters = None
def cob_shift(z, jvec):
    """z + delta(v): v supported at index jvec; the amalgam coboundary."""
    v = [K1 if t == jvec else K0 for t in range(27)]
    out = list(z)
    lets = {'a': mod["A27"], 'b': mod["B27"]}
    s2l = side2.lets
    segs = [('a', side1.lets['a'], 0), ('b', side1.lets['b'], 27),
            ('c', s2l['a'], 54), ('d', s2l['b'], 81)]
    for (_g, M, off) in segs:
        gv = apply_(M, v)
        for i in range(27):
            out[off + i] = out[off + i] + gv[i] - v[i]
    return out


ok_all = True
for slot in range(3):
    zs = [reps[0], reps[1], reps[2]]
    zs[slot] = cob_shift(zs[slot], 5)
    y = Yval(*zs)
    ok = (y - y0).is_zero()
    ok_all &= ok
    print(f"  G-A coboundary invariance, slot {slot}: {ok}", flush=True)

# G-B: antisymmetry
y_swap01 = Yval(reps[1], reps[0], reps[2])
y_swap12 = Yval(reps[0], reps[2], reps[1])
okB1 = (y_swap01 + y0).is_zero()
okB2 = (y_swap12 + y0).is_zero()
ok_all &= okB1 and okB2
print(f"  G-B antisymmetry (01 swap -> -Y): {okB1}", flush=True)
print(f"  G-B antisymmetry (12 swap -> -Y): {okB2}", flush=True)

# G-C: section independence
y_sec = Yval(reps[0], reps[1], reps[2], prod1="La")
okC = (y_sec - y0).is_zero()
ok_all &= okC
print(f"  G-C section independence (sig(mu lam) = LONG+a): {okC}", flush=True)

assert ok_all, "CLASS-LEVEL GATES FAILED — values are not banked"
print("ALL CLASS-LEVEL GATES PASS — the 3-form values are class-level.",
      flush=True)

print("\n==== the bent-weld doubles ====", flush=True)
tables = {"none": Yn}
for m in (1, 5, 7, 11):
    print(f"  D_bent(M; m={m}):", flush=True)
    Ym, _, _, _ = double_Y(m, verbose=False)
    tables[f"m={m}"] = Ym
    nz = 0
    for key in sorted(Ym):
        y = Ym[key]
        if not y.is_zero():
            nz += 1
        print(f"    Y[{key}] = {'0' if y.is_zero() else str(y)}", flush=True)
    print(f"    nonzero: {nz}/10", flush=True)

print("\nsummary (nonzero counts):", flush=True)
for tag, T in tables.items():
    print(f"  {tag}: {sum(1 for y in T.values() if not y.is_zero())}/10",
          flush=True)
print("B637 part 2b stage-2 DONE", flush=True)
