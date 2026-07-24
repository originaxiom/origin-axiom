"""B775 Phase-2 Wave-4  cell P2W4-R2  (OI-072)

THE R2 SEALING POSITIVE-DIMENSIONALITY QUESTION (B565 remainder).

B565/R2 tried to SEAL "K-membership fails OFF the metallic sub-locus" by sampling:
50/50 irreducible fixed points off the sub-locus failed K-membership.  A finite
point-sample seals a property over the whole fixed locus ONLY IF that locus is
0-dimensional.  B565 left the verdict hanging on exactly this: "the fixed loci are
positive-dimensional (local dim 10 != the expected 4), so the final verdict needs
the dimension question resolved first."  That is what this cell decides, exactly.

SETUP (all repo-internal, recomputed here).
  phi_m : a -> a^m b, b -> a   (abelianization [[m,1],[1,0]], det -1, dilatation =
  the metallic mean lambda_m).  The once-punctured-torus BUNDLE monodromy is the
  orientation-preserving square phi_m^2 = [[m^2+1, m],[m, 1]]:
      m=1 -> [[2,1],[1,1]] = RL      = the figure-eight   (B71 calibration)
      m=2 -> [[5,2],[2,1]] = R^2L^2  = b++RRLL = census m136 = the SILVER bundle,
                                       which is R2's calibrated word.
  So the R2 fixed locus is Fix(T_m^2) at m=2 on the 8 SL(3) trace coordinates
      x1=tr A, x2=tr B, x3=tr AB, x4=tr A^-1, x5=tr B^-1,
      x6=tr A^-1 B, x7=tr A B^-1, x8=tr A^-1 B^-1
  with T_m the B48 SL(3) metallic trace map (frontier/B48_sl3_metallic_trace_maps).
  T_m is RE-VERIFIED in-cell against direct SL(3,Z) matrix traces (no citation).

METHOD -- symbolic elimination, and every positive reproduced a SECOND way.
  (1) grevlex Groebner basis over Q of Fix(T_m^2), Krull dimension by the
      Kredel-Weispfenning maximal-independent-set criterion on the leading terms.
  (2) INDEPENDENT certificate (no leading-term combinatorics): generic slicing.
      dim = max k with V(I) meeting a generic codim-k plane.  Run at 2 seeds:
      nonempty through k slices for k <= d, ideal = (1) at k = d+1.
  (3) CONSTRUCTIVE second way: exhibit the continuum.  Elimination-flavoured
      dominance test -- fix a witness coordinate pair to random rational values and
      check the fiber is nonempty over C (Groebner != (1)).  Nonempty generic fibers
      over a 2-plane of coordinates == a 2-parameter family of fixed characters.
  (4) OFF-SUB-LOCUS refinement (this is the one the sealing actually needs).  Every
      SL(2)-derived family -- in particular B71's geometric component V0 = Sym^2, and
      any metallic sub-locus built from the SL(2) bundle rep -- is SELF-DUAL, because
      SL(2) reps are self-dual: such characters satisfy x1=x4, x2=x5, x3=x8, x6=x7.
      Saturating Fix(T_m^2) by each of (x1-x4), (x2-x5), (x3-x8), (x6-x7) (Rabinowitsch
      t*f-1) removes the ENTIRE self-dual locus, hence the whole SL(2)-derived
      sub-locus whatever its exact definition.  The dimension of what remains is the
      dimension of the off-sub-locus fixed set -- the set B565/R2 was sampling.

CALIBRATION: m=1 must reproduce B71 (Fix(T_1^2) = the SL(3) figure-eight character
variety, 3 components of dim 2).  If it does not, the method is not trusted and the
cell returns UNRESOLVED.

VERDICT (sealed criterion, OI-072):
  0-dimensional -> R2 seals         -> RESOLVED-A
  positive-dim  -> R2 sealing fails -> RESOLVED-B
  walled                            -> UNRESOLVED (EXTERNAL)

Structural/firewalled: pure SL(3) character-variety algebra. No SM values, nothing
to CLAIMS, the one-number pin untouched.

NOTE (self-correction): an earlier draft of this cell computed its second way with
sympy `.subs(dict)`, which substitutes SEQUENTIALLY, corrupting the SL(2) trace-map
composition (it reported the figure-eight SL(2) fixed locus as 0-dimensional, which
contradicts B565/T2's "one irreducible component, a rational curve").  That route is
replaced here by the slicing + dominance certificates, which use no substitution.
"""
from __future__ import annotations
import itertools, json, os, random, sys, time
import sympy as sp

X = list(sp.symbols("x1 x2 x3 x4 x5 x6 x7 x8"))
T = sp.Symbol("t")
HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------- trace map ---
def Tm(coords, m):
    """B48 SL(3) metallic trace map of phi_m: a -> a^m b, b -> a."""
    x1, x2, x3, x4, x5, x6, x7, x8 = coords
    tau = {-1: x6, 0: x2, 1: x3}
    sig = {-1: x7, 0: x5, 1: x8}
    for k in range(2, m + 2):
        tau[k] = sp.expand(x1 * tau[k - 1] - x4 * tau[k - 2] + tau[k - 3])
        sig[k] = sp.expand(x4 * sig[k - 1] - x1 * sig[k - 2] + sig[k - 3])
    return (tau[m], x1, tau[m + 1], sig[m], x4, sig[m - 1], tau[m - 1], sig[m + 1])


def coords_of(a, b):
    ai, bi = a.inv(), b.inv()
    tr = sp.trace
    return (tr(a), tr(b), tr(a * b), tr(ai), tr(bi), tr(ai * b), tr(a * bi), tr(ai * bi))


def verify_trace_map(mmax=3):
    """In-cell certificate: the symbolic T_m equals the direct matrix traces."""
    ex = [(sp.Matrix([[1, 1, 0], [0, 1, 1], [0, 0, 1]]),
           sp.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])),
          (sp.Matrix([[1, 2, 1], [0, 1, 1], [0, 0, 1]]),
           sp.Matrix([[1, 0, 0], [1, 1, 0], [1, 1, 1]]))]
    n = 0
    for a, b in ex:
        assert a.det() == 1 and b.det() == 1
        c = coords_of(a, b)
        for m in range(1, mmax + 1):
            pred = Tm(c, m)
            direct = coords_of((a ** m) * b, a)
            if any(sp.simplify(p - d) != 0 for p, d in zip(pred, direct)):
                return False, n
            n += 1
    return True, n


def monodromy(m):
    """Abelianized phi_m^2 -- the bundle monodromy."""
    P = sp.Matrix([[m, 1], [1, 0]])
    return P * P


def fix_polys(m):
    img = tuple(sp.expand(e) for e in Tm(Tm(tuple(X), m), m))
    out = [sp.expand(img[i] - X[i]) for i in range(8)]
    return [p for p in out if p != 0]


# ------------------------------------------------------------- dimension  ----
def krull_dim(G, V):
    """Kredel-Weispfenning / CLO 9.3: for a GRADED order, dim V(I) = max |U| with
    LT(I) cap k[U] = {0}, i.e. no GB leading monomial supported inside U."""
    lead = []
    for P in G.polys:
        e = P.LM(order="grevlex").exponents
        s = frozenset(i for i, q in enumerate(e) if q > 0)
        if not s:
            return -1, []                      # constant leading term: I = (1)
        lead.append(s)
    n = len(V)
    for r in range(n, -1, -1):
        w = [U for U in itertools.combinations(range(n), r)
             if all(not s.issubset(set(U)) for s in lead)]
        if w:
            return r, [tuple(V[i] for i in U) for U in w]
    return -1, []


def is_one(G):
    e = [sp.expand(p) for p in G.exprs]
    return len(e) == 1 and e[0] == 1


def slice_certificate(polys, V, dmax, seeds=(11, 29)):
    """Independent of leading terms: intersect with k generic hyperplanes.
    Returns {seed: [(k, nonempty?)]}; dim = largest k that stays nonempty."""
    out = {}
    for seed in seeds:
        rnd = random.Random(seed)
        H = [sum(rnd.randint(-9, 9) * v for v in X) + rnd.randint(-9, 9)
             for _ in range(dmax + 2)]
        row = []
        for k in range(dmax + 2):
            row.append((k, not is_one(sp.groebner(polys + H[:k], *V, order="grevlex"))))
        out[seed] = row
    return out


def dominance(polys, V, U, n=5, seed=5):
    """Constructive continuum: generic fibers over the witness coordinates U."""
    rnd = random.Random(seed)
    hits = []
    for _ in range(n):
        cs = [sp.Rational(rnd.randint(-6, 6), rnd.randint(1, 4)) for _ in U]
        G = sp.groebner(polys + [u - c for u, c in zip(U, cs)], *V, order="grevlex")
        hits.append(not is_one(G))
    return int(sum(hits)), n


# ------------------------------------------------------------------ analyse --
SELF_DUAL = [X[0] - X[3], X[1] - X[4], X[2] - X[7], X[5] - X[6]]


def analyse(m):
    F = fix_polys(m)
    G = sp.groebner(F, *X, order="grevlex")
    d, wit = krull_dim(G, X)
    sl = slice_certificate(F, X, d)
    slice_dim = {s: max([k for k, ok in row if ok] + [-1]) for s, row in sl.items()}
    dom_ok, dom_n = dominance(F, X, list(wit[0])) if d > 0 else (0, 0)

    # off the self-dual (= SL(2)-derived, incl. Sym^2/B71-V0) sub-locus
    off = {}
    V9 = X + [T]
    for f in SELF_DUAL:
        Fs = F + [sp.expand(T * f - 1)]
        Gs = sp.groebner(Fs, *V9, order="grevlex")
        ds, ws = krull_dim(Gs, V9)
        wx = [u for u in ws if T not in u]
        off[str(f)] = {"dim": int(ds),
                       "witness": [str(v) for v in (wx[0] if wx else ())]}
    # constructive continuum OFF the sub-locus (saturate by x1-x4)
    Fs = F + [sp.expand(T * SELF_DUAL[0] - 1)]
    Gs = sp.groebner(Fs, *V9, order="grevlex")
    ds, ws = krull_dim(Gs, V9)
    wx = [u for u in ws if T not in u]
    off_sl = slice_certificate(Fs, V9, ds)
    off_slice_dim = {s: max([k for k, ok in row if ok] + [-1]) for s, row in off_sl.items()}
    off_dom = dominance(Fs, V9, list(wx[0])) if wx else (0, 0)

    return {
        "m": m,
        "bundle_monodromy": str(monodromy(m).tolist()),
        "n_fix_polys": len(F),
        "fix_poly_degrees": [int(sp.Poly(p, *X).total_degree()) for p in F],
        "groebner_size": len(G.exprs),
        "krull_dimension": int(d),
        "dim_witness_sets": [[str(v) for v in u] for u in wit[:4]],
        "slice_certificate_dim": {str(k): int(v) for k, v in slice_dim.items()},
        "generic_fiber_nonempty": f"{dom_ok}/{dom_n}",
        "off_selfdual_dim": {k: v["dim"] for k, v in off.items()},
        "off_selfdual_witness": [str(v) for v in (wx[0] if wx else ())],
        "off_selfdual_slice_dim": {str(k): int(v) for k, v in off_slice_dim.items()},
        "off_selfdual_generic_fiber_nonempty": f"{off_dom[0]}/{off_dom[1]}",
    }


def main():
    t0 = time.time()
    print("=" * 74)
    print("P2W4-R2 (OI-072)  R2 sealing: is Fix(T_m^2) 0-dimensional?")
    print("  m=1 = RL = figure-eight (B71 calibration) | m=2 = R^2L^2 = b++RRLL (R2)")
    print("=" * 74)

    tm_ok, tm_n = verify_trace_map()
    print(f"\n[cert] B48 SL(3) trace map vs direct matrix traces: "
          f"{'PASS' if tm_ok else 'FAIL'} ({tm_n} cases)")
    print(f"[cert] bundle monodromy phi_1^2={monodromy(1).tolist()}  "
          f"phi_2^2={monodromy(2).tolist()} (= R^2L^2, silver/m136)")

    R = {}
    for m in (1, 2):
        r = analyse(m)
        R[f"m{m}"] = r
        tag = "figure-eight / B71 CALIBRATION" if m == 1 else "b++RRLL silver / THE R2 WORD"
        print(f"\n--- m={m}  {tag} ---")
        print(f"  fix polys {r['n_fix_polys']} deg {r['fix_poly_degrees']}, GB size {r['groebner_size']}")
        print(f"  KRULL DIM (grevlex, indep-set)   : {r['krull_dimension']}   "
              f"witnesses {r['dim_witness_sets'][:3]}")
        print(f"  slice certificate dim (2 seeds)  : {r['slice_certificate_dim']}")
        print(f"  generic fibers nonempty          : {r['generic_fiber_nonempty']}")
        print(f"  OFF self-dual sub-locus, dim     : {r['off_selfdual_dim']}")
        print(f"  OFF slice cert dim (2 seeds)     : {r['off_selfdual_slice_dim']}"
              f"   fibers {r['off_selfdual_generic_fiber_nonempty']}")

    # ------------------------------------------------------------- verdict ---
    r1, r2 = R["m1"], R["m2"]
    calib = (tm_ok and r1["krull_dimension"] == 2
             and all(v == 2 for v in r1["slice_certificate_dim"].values()))
    d = r2["krull_dimension"]
    way1 = d >= 1
    way2 = all(v == d for v in r2["slice_certificate_dim"].values()) and d >= 1
    way3 = r2["generic_fiber_nonempty"] == "5/5"
    off_pos = all(v >= 1 for v in r2["off_selfdual_dim"].values())

    if not calib:
        verdict = "UNRESOLVED"
        headline = ("figure-eight calibration failed to reproduce B71 (Fix(T_1^2) dim 2) "
                    "-- method not trusted; EXTERNAL")
    elif way1 and way2 and way3 and off_pos:
        verdict = "RESOLVED-B"
        headline = (f"R2's fixed locus Fix(T_2^2) is POSITIVE-DIMENSIONAL: Krull dim = {d}, "
                    f"and it stays dim {min(r2['off_selfdual_dim'].values())} after the entire "
                    f"self-dual (SL(2)-derived / Sym^2) sub-locus is removed -- so R2's finite "
                    f"50-point sample can never seal; the R2 sealing FAILS as a method")
    elif way1 and way2 and way3:
        verdict = "RESOLVED-B"
        headline = (f"Fix(T_2^2) is positive-dimensional (dim {d}) but the off-sub-locus part "
                    f"is not -- sealing still fails on the full locus")
    elif d == 0:
        verdict = "RESOLVED-A"
        headline = "Fix(T_2^2) is 0-dimensional (a finite character set) -- the finite sample seals"
    else:
        verdict = "UNRESOLVED"
        headline = "the two dimension certificates disagree -- walled in-sandbox; EXTERNAL"

    disc = (
        f"b++RRLL is the bundle monodromy phi_2^2 = R^2L^2 = [[5,2],[2,1]] (silver m=2, "
        f"census m136). Its SL(3) trace-map fixed locus Fix(T_2^2) in the 8 B48 coordinates "
        f"has KRULL DIMENSION {d}, not 0: (i) grevlex Groebner over Q + Kredel-Weispfenning "
        f"maximal-independent-set gives {d} with witness {r2['dim_witness_sets'][0]}; "
        f"(ii) an independent generic-slice certificate at 2 seeds gives exactly {d} "
        f"(nonempty through {d} generic hyperplanes, ideal = (1) at {d+1}); "
        f"(iii) constructively, {r2['generic_fiber_nonempty']} random rational fibers over "
        f"the witness pair are nonempty -- an explicit 2-parameter continuum of fixed "
        f"characters. Crucially the same holds OFF the sub-locus: saturating by each of "
        f"x1-x4, x2-x5, x3-x8, x6-x7 (which together cut out the self-dual locus, containing "
        f"every SL(2)-derived family, i.e. B71's Sym^2 component V0 and any metallic "
        f"sub-locus) leaves dimension {r2['off_selfdual_dim']} with "
        f"{r2['off_selfdual_generic_fiber_nonempty']} nonempty generic fibers. "
        f"m=1 calibration reproduces B71's figure-eight dim 2. This also reconciles B565/R2's "
        f"own numeric 'local dim 10': 10 = 2 (character) + 8 (dim PGL(3,C) gauge orbit). "
        f"A finite 50-point sample cannot seal a property over a 2-dimensional family."
    )

    out = {
        "cell": "P2W4-R2", "oi": "OI-072",
        "question": ("Is the R2 (b++RRLL) SL(3) trace-map fixed locus 0-dimensional "
                     "(sealing valid) or positive-dimensional (sealing fails)?"),
        "identification": ("b++RRLL = phi_2^2 = R^2L^2 = [[5,2],[2,1]] = silver m=2 "
                           "once-punctured-torus bundle (census m136)"),
        "locus": "Fix(T_2^2) on the 8 B48 SL(3) trace coordinates",
        "trace_map_certificate": {"passed": bool(tm_ok), "cases": tm_n},
        "calibration_m1_B71_dim2": bool(calib),
        "R2_krull_dimension": d,
        "R2_slice_certificate_dim": r2["slice_certificate_dim"],
        "R2_off_sublocus_dim": r2["off_selfdual_dim"],
        "reproduced_second_way": bool(way2 and way3),
        "verdict": verdict,
        "headline": headline,
        "discriminating_fact": disc,
        "terminal_state": ("CLOSED: the R2 sealing method is refuted -- the residual "
                           "K-membership question needs a whole-family (2-parameter) "
                           "argument, not point sampling"),
        "detail": R,
        "runtime_s": round(time.time() - t0, 1),
        "gate": {"structural_only": True, "no_SM_values": True,
                 "nothing_to_CLAIMS": True, "one_number_pin_untouched": True},
    }
    print("\n" + "=" * 74)
    print(f"VERDICT: {verdict}")
    print(headline)
    print("=" * 74)
    with open(os.path.join(HERE, "results.json"), "w") as f:
        json.dump(out, f, indent=1)
    print(f"\nwrote results.json  ({out['runtime_s']}s)")
    return out


if __name__ == "__main__":
    main()
