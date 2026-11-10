#!/usr/bin/env python3
"""Attack E, the computable part: the hand of a departure, and what a history with no hand carries in place of a
spin structure. SnapPy and integers; nothing is measured. Sealed with PREREGISTRATION.md before it was run.

    python3 -B walls_and_pin.py

Bundles: 'b++W' is the bundle of the two-act word W; 'b-+W' is the bundle of W followed by the exchange (the
library's convention, checked on the tick alone: 'b-+L' is m000, non-orientable, and its orientation cover is m004)."""
import itertools, warnings
warnings.filterwarnings("ignore")
import snappy

out = []
def say(s=""):
    out.append(s); print(s, flush=True)
def alt(seq): return "".join(("L" if i % 2 == 0 else "R") * c for i, c in enumerate(seq))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
def mul(A, C): return (A[0]*C[0]+A[1]*C[2], A[0]*C[1]+A[1]*C[3], A[2]*C[0]+A[3]*C[2], A[2]*C[1]+A[3]*C[3])
def mat(seq):
    M = (1, 0, 0, 1)
    for c in seq: M = mul(M, (c, 1, 1, 0))
    return M
def cs(M):
    try: return float(M.chern_simons())
    except Exception as e: return "not defined (%s)" % str(e).strip("b'\"")[:40]
def half(x):                      # the invariant is defined modulo 1/2: reduce to (-1/4, 1/4]
    if not isinstance(x, float): return x
    y = x % 0.5
    return y - 0.5 if y > 0.25 else y

# ---------------------------------------------------------------- controls
m004 = snappy.Manifold("m004"); m000 = snappy.Manifold("m000")
T1 = snappy.Manifold("b-+L")
assert snappy.Manifold("b++LR").is_isometric_to(m004) and T1.is_isometric_to(m000) and not T1.is_orientable()
assert T1.orientation_cover().is_isometric_to(m004)
say("controls passed: b++LR is m004; b-+L is m000, non-orientable, with m004 as its orientation cover")

# ---------------------------------------------------------------- H14, H15: the hand and the Chern-Simons invariant
say("\nH14, H15  THE GROUND AND ITS FIRST DEPARTURES: own mirror image?  Chern-Simons invariant (defined modulo 1/2)")
say("    %-22s %-16s %-10s %-9s %-12s %s" % ("history (runs)", "word", "volume", "symm.", "own mirror", "Chern-Simons, reduced"))
rows = [("ground, 1 period", (1, 1)), ("ground, 2 periods", (1, 1, 1, 1)), ("ground, 3 periods", (1,) * 6)]
for k in (1, 2, 3):
    rows.append(("run of 6, %d more" % k, (6, 1) + (1, 1) * k))
for k in (1, 2):
    rows.append(("(2,2,2), %d more" % k, (2, 2, 2, 1) + (1, 1) * k))
rows.append(("(2,1,1,1,2)", (2, 1, 1, 1, 2, 1, 1, 1)))
rows.append(("(2,3) not a palindrome", (2, 3, 1, 1)))
res = {}
for label, seq in rows:
    w = alt(seq); M = snappy.Manifold("b++" + w); Mm = snappy.Manifold("b++" + swap(w))
    Gs = M.symmetry_group()
    c1 = cs(M); c2 = cs(Mm)
    res[label] = (c1, c2)
    say("    %-22s %-16s %-10.6f %-9d %-12s %s" % (label, w if len(w) <= 16 else w[:13] + "...", float(M.volume()), Gs.order(), bool(Gs.is_amphicheiral()),
        ("%+.9f" % half(c1)) if isinstance(c1, float) else c1))
    say("    %-22s %-16s %-10.6f %-9s %-12s %s" % ("   its letter-swap", "", float(Mm.volume()), "", "", ("%+.9f" % half(c2)) if isinstance(c2, float) else c2))
ok = [l for l, (a, b) in res.items() if isinstance(a, float) and isinstance(b, float)]
say("    a history's value plus its swap's, reduced modulo 1/2: %s" % {l: "%.2e" % abs(half(res[l][0] + res[l][1])) for l in ok})

# ---------------------------------------------------------------- H16: a history with no hand
say("\nH16  HISTORIES WITH AN ODD NUMBER OF RUNS (no hand): what stands in place of a spin structure")
say("    A spin structure on the fibre is one of four quadratic forms on its mod-2 homology; three are even, one is odd.")
say("    A structure on the bundle restricts to a form the history keeps. kept = how many of the four the history keeps.")
def kept_forms(M2):
    a, b, c, d = (x % 2 for x in M2)
    n = 0
    for qa, qb in itertools.product((0, 1), repeat=2):
        q = {(0, 0): 0, (1, 0): qa, (0, 1): qb, (1, 1): (qa + qb + 1) % 2}
        img_a = (a, c); img_b = (b, d)                       # the images of the two basis vectors
        if q[img_a] == qa and q[img_b] == qb: n += 1
    return n
def h1_mod2(M):
    H = M.homology(); r = 0
    for e in H.elementary_divisors():
        if e == 0 or e % 2 == 0: r += 1
    return 2 ** r
def comps(n):
    if n == 0: yield (); return
    for r in range(1, n + 1):
        for rest in comps(n - r): yield (r,) + rest
seen = set(); agree = tot = 0; table = []
for n in range(1, 7):
    for c in comps(n):
        if len(c) % 2 == 0: continue
        key = min(c[i:] + c[:i] for i in range(len(c)))
        if key in seen: continue
        seen.add(key)
        M = snappy.Manifold("b-+" + alt(key))
        k = kept_forms(mat(key)); h = h1_mod2(M); tot += 1; agree += (2 * k == h)
        table.append((key, bool(M.is_orientable()), str(M.homology()), k, h, cs(M)))
for row in table[:14]:
    say("    runs %-14s orientable %-5s H1 %-14s kept %d   H^1(bundle; Z/2) has %d elements   Chern-Simons: %s" % row)
say("    histories checked (to 6 letters, an odd number of runs): %d; none orientable: %s; 2 x kept = |H^1(Z/2)| on %d of %d" % (
    tot, not any(r[1] for r in table), agree, tot))
say("    Chern-Simons defined on none of them: %s" % all(not isinstance(r[5], float) for r in table))
ctl = []
for seq in ((1, 1), (2, 1), (2, 2), (3, 1), (6, 1, 1, 1), (2, 2, 2, 1)):
    M = snappy.Manifold("b++" + alt(seq)); ctl.append((seq, kept_forms(mat(seq)), h1_mod2(M)))
say("    control on two-act histories (spin structures): (runs, kept, |H^1(Z/2)|): %s" % ctl)
say("    the tick alone keeps %d form(s): the odd one only; L.R keeps %d" % (kept_forms(mat((1,))), kept_forms(mat((1, 1)))))

open(__file__.replace(".py", "_out.txt"), "w").write("\n".join(out) + "\n")
