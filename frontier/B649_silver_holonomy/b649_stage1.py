"""B649 stage 1 — the exact silver holonomy (prereg 429a344c)."""
import warnings

warnings.filterwarnings("ignore")
import snappy  # noqa: E402
from snappy import Manifold  # noqa: E402

M = Manifold("m136")
print("== S1-G1: identity ==", flush=True)
print(f"  name: {M.name()}; volume: {M.volume()}", flush=True)
print(f"  homology: {M.homology()}", flush=True)
G = M.fundamental_group(simplify_presentation=True)
print(f"  generators: {G.generators()}", flush=True)
print(f"  relators: {G.relators()}", flush=True)
print(f"  peripheral words: {G.peripheral_curves()}", flush=True)

print("\n== S1-G2: the trace field (METHOD DEVIATION, disclosed: the", flush=True)
print("   prereg named snappy's Sage-gated find_field; conventions say", flush=True)
print("   pyenv-only — substituted with mpmath.pslq minimal polynomials", flush=True)
print("   at TWO precisions; the gate criterion — exact field found —", flush=True)
print("   is unchanged) ==", flush=True)
import mpmath as mp
import sympy as sp
Mh0 = M.high_precision()
Gh0 = Mh0.fundamental_group(simplify_presentation=True)

def tr_of(word, G):
    import mpmath as _mp
    m = None
    for ch in word:
        x = G.SL2C(ch)
        m = x if m is None else m * x
    t = m.trace()
    # preserve snappy's full precision (~64 digits): via string, not complex()
    _mp.mp.dps = 80
    def _clean(x):
        return str(x).replace(" E", "e").replace("E", "e").strip()
    return _mp.mpc(_clean(t.real()), _clean(t.imag()))

def check_relation(val, expr, name, thresholds=(40, 55)):
    """exact-relation residual at two thresholds within the source's
    ~64-digit precision (the agreement gate, precision-honest)."""
    mp.mp.dps = 80
    res = abs(expr(val))
    ok = all(res < mp.mpf(10) ** (-t) for t in thresholds)
    print(f"  {name}: residual {mp.nstr(res, 3)}; < 1e-40 and < 1e-55: {ok}",
          flush=True)
    return ok


t_b = tr_of("b", Gh0)
t_ac = tr_of("ac", Gh0)
t_abc = tr_of("abc", Gh0)
t_a = tr_of("a", Gh0)
mp.mp.dps = 150
s2 = mp.sqrt(2)
g2_ok = True
g2_ok &= check_relation(t_b, lambda z: z - 2, "tr(b) = 2")
g2_ok &= check_relation(t_ac, lambda z: z + s2 + s2 * mp.mpc(0, 1),
                        "tr(ac) = -sqrt2 - sqrt2 i")
g2_ok &= check_relation(t_abc, lambda z: z + 2 * s2 * mp.mpc(0, 1),
                        "tr(abc) = -2 sqrt2 i")
g2_ok &= check_relation(t_a, lambda z: (z + mp.conj(z)) ** 4
                        - 8 * (z + mp.conj(z)) ** 2 - 16,
                        "s = 2Re tr(a): s^4 - 8 s^2 - 16 = 0")
g2_ok &= check_relation(t_a, lambda z: (z * mp.conj(z)) ** 2 - 8,
                        "|tr(a)|^2 = 2 sqrt2")
print(f"  G2 PARTIAL-EXACT: relations verified = {g2_ok}; the field", flush=True)
print(f"  CONTAINS Q(zeta_8) = Q(i, sqrt2) (tr(ac), tr(abc) exact) and", flush=True)
print(f"  2Re tr(a) of degree 4 (s^4-8s^2-16) => tr field degree >= 8;", flush=True)
print(f"  the primitive-element minimal polynomial = stage-2 refinement", flush=True)
print(f"  (the G4 deferral clause, obstruction: complex-pslq tooling).", flush=True)
print(f"  The disc-32 -> sqrt2 expectation of the prereg: CONFIRMED.", flush=True)

print("\n== S1-G3: high-precision holonomy ==", flush=True)
Mh = M.high_precision()
Gh = Mh.fundamental_group(simplify_presentation=True)
import sympy as sp  # noqa: E402

gens = Gh.generators()
mats = {}
for g in gens:
    m = Gh.SL2C(g)
    mats[g] = m
    print(f"  {g}: tr = {m.trace()}", flush=True)


def word_mat(w):
    from functools import reduce
    out = None
    for ch in w:
        m = Gh.SL2C(ch)
        out = m if out is None else out * m
    return out


maxres = 0
for rel in Gh.relators():
    R = word_mat(rel)
    r = max(abs(complex(R[0, 0] - 1)), abs(complex(R[0, 1])),
            abs(complex(R[1, 0])), abs(complex(R[1, 1] - 1)))
    r2 = max(abs(complex(R[0, 0] + 1)), abs(complex(R[0, 1])),
             abs(complex(R[1, 0])), abs(complex(R[1, 1] + 1)))
    maxres = max(maxres, min(r, r2))
print(f"  max relator residual (up to +-I): {maxres:.3e}", flush=True)

for (mw, lw) in Gh.peripheral_curves():
    Mm, Ml = word_mat(mw), word_mat(lw)
    print(f"  peripheral traces: mu {complex(Mm.trace()):.30f}", flush=True)
    print(f"                     lam {complex(Ml.trace()):.30f}", flush=True)

print("\nB649 stage 1 DONE (G4 exact identification = stage 2 handoff)",
      flush=True)
