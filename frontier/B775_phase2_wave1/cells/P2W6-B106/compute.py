"""P2W6-B106 (OI-141) -- rank-4 Fix(T_1^2) census completion + the exact c=i point.

QUESTION (B106 FINDINGS, D3/D4, left open):
  (Q1) the CONJUGATE A-variety relations M^k L = 1 are reported ABSENT on both rank-4
       Dehn-filling components; "exhaustiveness over all rank-4 spectra needs the symbolic
       Fix(T_1^2) -- open; the conjugate could in principle live on a spectrum the census
       didn't search."
  (Q2) the secondary component's scalar c = i is "numerical (~5e-15), not proved" -- the
       exact c=i point.

METHOD (single-t bundle equation; sln_toolkit substrate).  A bundle rep is (A,B,t) with
  t A t^-1 = A^2 B,  t B t^-1 = A B,  B = A^-2 t A t^-1,
eliminating B to the 16-variable equation  (*) t A^-2 t A = A^-1 t A t.

WHAT THIS CELL COMPUTES (all in-sandbox):
  S1  the fibered-group substrate: Gamma = F_2 x|_phi Z with exact normal forms (w,k) = w t^k.
  S2  the CONJUGATION MAP Phi  (exact, in Gamma, hence every rank, every rep):
        alpha in Aut(F_2): a->b, b->a^-1  satisfies  alpha phi alpha^-1 = iota_{ab^-1} o phi^-1
        => (A,B,t) |-> (B, A^-1, A B^-1 t^-1) maps bundle reps to bundle reps
        => mu' = A^-1 mu^-1 A,  L' = A^-1 L A
        => L = c mu^k  <=>  L' mu'^k = c   (the CONJUGATE relation, same c).
      So M^k L = 1 is NEVER absent: it is the Phi-image of M^k = L.  Q1 answered.
  S3  rank-4 instantiation: exact/numeric certificates that Phi(principal) carries M^4 L = 1
      and Phi(secondary) M^3 L = 1, and that these are NEW components (the Phi-image has a
      MOVING A-spectrum -- exactly what an A-spectrum-indexed search cannot see).
  S4  the exact c point: t is unique up to mu_4 (Schur), t -> lam t sends c -> c lam^-k, so c
      is well defined only in mu_4 / mu_4^k = Z/gcd(k,4).  k=4 (principal): c=-1 INVARIANT.
      k=3 (secondary): gcd(3,4)=1 => c is PURE GAUGE; all four values occur; the banked
      "c=i" is the value of the det(t)**0.25 principal branch at realize-seed 0 (seed 1
      gives -i).  Invariant content: L^4 = M^12.
  S5  exhaustiveness of the census over ALL rank-4 spectra: attempted and WALLED.  The
      ideal-theoretic dimension of (*) is dominated by the REDUCIBLE stratum; stripping it
      needs one Rabinowitsch variable per A-invariant coordinate subspace, 2^n - 2 of them,
      so the census ideal is 12 + 14 = 26 variables at rank 4 -- one past the named 25-var
      Groebner wall (L22/B199).  Rank 3 (6 + 6 = 12 vars) is the control and it works.

Structural / character-variety mathematics only. No SM values, nothing to CLAIMS.md.
Env: pyenv python3 (sympy/numpy). COMPACT output.
"""
from __future__ import annotations

import itertools
import json
import pathlib
import signal
import time

import numpy as np
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parents[4]
HERE = pathlib.Path(__file__).resolve().parent
inv = np.linalg.inv
I4 = np.eye(4, dtype=complex)
W3 = np.exp(2j * np.pi / 3)
Z8 = np.exp(1j * np.pi / 4)
SPEC = {"principal": np.array([1, 1, W3, W3 ** 2]),
        "secondary": np.array([Z8 ** k for k in (1, 3, 5, 7)])}
KEXP = {"principal": 4, "secondary": 3}
R = {}
LOG = []


def say(s=""):
    print(s)
    LOG.append(s)


# ===========================================================================
# S1 -- the fibered group Gamma = F_2 x|_phi Z, exact normal forms
# ===========================================================================
INVLET = {"a": "A", "A": "a", "b": "B", "B": "b"}


def red(w):
    """free reduction of a word in a,A,b,B"""
    out = []
    for c in w:
        if out and out[-1] == INVLET[c]:
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def winv(w):
    return red("".join(INVLET[c] for c in reversed(w)))


def sub(w, ima, imb):
    """apply the endomorphism a->ima, b->imb to the word w"""
    m = {"a": ima, "A": winv(ima), "b": imb, "B": winv(imb)}
    return red("".join(m[c] for c in w))


PHI = lambda w: sub(w, "aab", "ab")        # phi(a)=a^2 b, phi(b)=ab  (the B73/B106 convention)
PSI = lambda w: sub(w, "aB", "bAb")        # phi^-1
ALPHA = lambda w: sub(w, "b", "A")         # alpha: a->b, b->a^-1
IOTA = lambda v, w: red(v + w + winv(v))   # inner


def phik(w, k):
    f = PHI if k >= 0 else PSI
    for _ in range(abs(k)):
        w = f(w)
    return w


def gmul(x, y):
    """(w1,k1)*(w2,k2) in Gamma = F_2 x|_phi Z, element = w t^k, t w = phi(w) t"""
    return (red(x[0] + phik(y[0], x[1])), x[1] + y[1])


def ginv(x):
    return (phik(winv(x[0]), -x[1]), -x[1])


def gprod(*xs):
    out = ("", 0)
    for x in xs:
        out = gmul(out, x)
    return out


def s1_substrate():
    ok = {}
    ok["phi_psi_inverse"] = all(PSI(PHI(w)) == w and PHI(PSI(w)) == w for w in ("a", "b", "ab", "aBb"))
    # t a t^-1 = a^2 b and t b t^-1 = ab in Gamma
    T = ("", 1)
    ok["rel_a"] = gprod(T, ("a", 0), ginv(T)) == ("aab", 0)
    ok["rel_b"] = gprod(T, ("b", 0), ginv(T)) == ("ab", 0)
    # alpha in Aut(F_2): alpha^2 = the elliptic involution a->a^-1,b->b^-1
    ok["alpha_order"] = ALPHA(ALPHA("a")) == "A" and ALPHA(ALPHA("b")) == "B"
    return ok


# ===========================================================================
# S2 -- the conjugation map Phi (exact theorem, in Gamma)
# ===========================================================================
def s2_conjugation_theorem():
    out = {}
    # (i) alpha phi alpha^-1 = iota_{ab^-1} o phi^-1   on both generators
    ainv = lambda w: sub(w, "B", "a")      # alpha^-1: a->b^-1, b->a
    lhs = {x: ALPHA(PHI(ainv(x))) for x in ("a", "b")}
    rhs = {x: IOTA("aB", PSI(x)) for x in ("a", "b")}
    out["alpha_conjugates_phi_to_phi_inverse"] = lhs == rhs
    out["inner_word_w"] = "aB"             # w = a b^-1
    # (ii) the monodromy of the alpha-twisted rep: t' = w t^-1 = a b^-1 t^-1
    tp = ("aB", -1)
    ok = all(gprod(tp, (ALPHA(x), 0), ginv(tp)) == (ALPHA(PHI(x)), 0) for x in ("a", "b"))
    out["t_prime_is_monodromy"] = ok
    # (iii) mu' = A^-1 mu^-1 A  and  L' = A^-1 L A
    mu = ("A", 1)                          # mu = a^-1 t
    mup = gmul((winv(ALPHA("a")), 0), tp)  # mu' = alpha(a)^-1 t'
    out["mu_prime"] = mup
    out["mu_prime_equals_conj_mu_inv"] = mup == gprod(("A", 0), ginv(mu), ("a", 0))
    L = red("abAB")
    Lp = red(ALPHA("a") + ALPHA("b") + winv(ALPHA("a")) + winv(ALPHA("b")))
    out["L_prime"] = Lp
    out["L_prime_equals_conj_L"] = Lp == IOTA("A", L)
    # (iv) consequence: L = c mu^k  <=>  L' mu'^k = c   (same c) -- exact, all ranks
    out["conjugate_relation_forced"] = (out["mu_prime_equals_conj_mu_inv"]
                                        and out["L_prime_equals_conj_L"]
                                        and out["t_prime_is_monodromy"])
    return out


# ===========================================================================
# S3 -- rank-4 instantiation
# ===========================================================================
def bundle_residual(A, B, t):
    return max(float(np.max(np.abs(t @ A @ inv(t) - A @ A @ B))),
               float(np.max(np.abs(t @ B @ inv(t) - A @ B))))


def relation_scan(A, B, t, ks=(2, 3, 4, 5)):
    mu = inv(A) @ t
    comm = A @ B @ inv(A) @ inv(B)
    hits = {}
    for k in ks:
        for lab, M in ((f"M^{k}=L", comm @ np.linalg.matrix_power(inv(mu), k)),
                       (f"M^{k}L=1", comm @ np.linalg.matrix_power(mu, k))):
            c = np.trace(M) / 4
            dev = float(np.max(np.abs(M - c * I4)))
            if dev < 1e-6:
                hits[lab] = (complex(np.round(c, 9)), dev)
    return hits


def s3_rank4(df):
    out = {}
    for name, spec in SPEC.items():
        rows = []
        for seed in (0, 1, 2):
            got = df.realize_bundle_rep(spec, seed=seed)
            if got is None:
                continue
            A, B, t = got
            Ap, Bp, tp = B, inv(A), A @ inv(B) @ inv(t)          # the exact Phi map
            tpn = tp / np.linalg.det(tp) ** 0.25
            rows.append({
                "seed": seed,
                "orig_res": bundle_residual(A, B, t),
                "orig": {k: [str(v[0]), v[1]] for k, v in relation_scan(A, B, t).items()},
                "phi_res": bundle_residual(Ap, Bp, tpn),
                "phi": {k: [str(v[0]), v[1]] for k, v in relation_scan(Ap, Bp, tpn).items()},
                "trA_phi_image": complex(np.round(np.trace(Ap), 6)),
                "specB_phi_image": [complex(np.round(z, 6)) for z in np.sort_complex(np.linalg.eigvals(Bp))],
            })
        out[name] = rows
    return out


def s3_new_component_exact():
    """EXACT (over Q(omega)): on the B89 principal family tr B MOVES, while spec(A) is frozen.
    Hence Phi(principal) -- whose A-spectrum is spec(B) -- is a DIFFERENT component, invisible
    to any search that fixes the A-spectrum."""
    w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2                    # primitive cube root
    t12, t21, t22, s = sp.symbols("t12 t21 t22 s")
    D = sp.diag(w, w ** 2)
    T = sp.Matrix([[w * t22, t12], [t21, t22]])
    P = -D * T
    Rm = sp.Matrix([[t12 * t21 * (w + 1) - t22 ** 2, s],
                    [s * t21 / t12, t22 ** 2 + w * (t22 ** 2 - t12 * t21)]])
    t = sp.Matrix(sp.BlockMatrix([[P, sp.eye(2)], [Rm, T]]))
    A = sp.diag(1, 1, w, w ** 2)
    Ai = A.inv()
    star = sp.simplify(sp.expand(t * Ai * Ai * t * A - Ai * t * A * t))
    on_variety = all(sp.simplify(e) == 0 for e in star)
    B = sp.simplify(Ai * Ai * t * A * t.inv())
    trB = sp.simplify(sp.expand(B.trace()))
    d = {v: sp.simplify(sp.diff(trB, v)) for v in (t12, t21, t22, s)}
    moves = any(x != 0 for x in d.values())
    pts = []
    for vals in ((sp.Rational(1, 2), 2, 3, 1), (1, 1, 2, sp.Rational(3, 2)), (2, sp.Rational(1, 3), 1, 1)):
        sb = dict(zip((t12, t21, t22, s), vals))
        pts.append(sp.nsimplify(sp.simplify(trB.subs(sb))))
    return {"b89_family_on_variety_exact": bool(on_variety),
            "trB_nonconstant_exact": bool(moves),
            "trB_at_3_exact_points": [str(sp.simplify(x)) for x in pts],
            "distinct": len({sp.simplify(x - pts[0]) == 0 for x in pts}) > 1 or
                        any(sp.simplify(x - pts[0]) != 0 for x in pts)}


# ===========================================================================
# S4 -- the exact c point
# ===========================================================================
def s4_exact_c(df):
    """c is the mu_4 LIFT scalar.  t is unique up to lam with lam^4=1 (Schur + det t = 1);
    t -> lam t sends mu -> lam mu, so c -> c lam^-k.  Hence c is well defined only in
    mu_4/mu_4^k = Z/gcd(k,4).  Exactly: det L = 1 = c^4 (det mu)^k = c^4, so c^4 = 1 always."""
    out = {"c4_is_1_exact": "det[A,B]=1 and det(mu)=1 => c^4=1 (exact)",
           "gauge_class": {name: f"mu_4/mu_4^{KEXP[name]} = Z/{np.gcd(KEXP[name], 4)}" for name in SPEC}}
    per = {}
    for name, spec in SPEC.items():
        k = KEXP[name]
        seeds = {}
        for seed in (0, 1, 2):
            got = df.realize_bundle_rep(spec, seed=seed)
            if got is None:
                continue
            A, B, t = got
            comm = A @ B @ inv(A) @ inv(B)
            vals = []
            for m in range(4):
                mu = inv(A) @ ((1j ** m) * t)
                M = comm @ np.linalg.matrix_power(inv(mu), k)
                c = np.trace(M) / 4
                dev = float(np.max(np.abs(M - c * I4)))
                vals.append((str(complex(np.round(c, 9))), dev))
            seeds[seed] = {"c_over_the_4_lifts": [v[0] for v in vals],
                           "max_dev": max(v[1] for v in vals),
                           "distinct_c_values": len({v[0] for v in vals})}
        per[name] = seeds
    out["per_component"] = per
    out["c_is_invariant"] = {name: all(s["distinct_c_values"] == 1 for s in per[name].values())
                             for name in per}
    out["banked_c_is_seed_dependent"] = {
        name: sorted({s["c_over_the_4_lifts"][0] for s in per[name].values()}) for name in per}
    return out


# ===========================================================================
# S5 -- census exhaustiveness: the ideal, the junk stratum, the wall
# ===========================================================================
class TO(Exception):
    pass


def _alarm(sig, frm):
    raise TO()


def gb_timed(eqs, vs, p, limit):
    signal.signal(signal.SIGALRM, _alarm)
    signal.setitimer(signal.ITIMER_REAL, limit)
    t0 = time.time()
    try:
        G = sp.groebner(eqs, *vs, order="grevlex", modulus=p)
        signal.setitimer(signal.ITIMER_REAL, 0)
        return G, time.time() - t0, False
    except TO:
        return None, time.time() - t0, True
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)


def build_star(spec, p, n, gauge_row=0):
    """(*) in the gauge  t[gauge_row,:] = (1,...,1)  (scale + torus), cleared of denominators:
       eq(i,j) = sum_k (a_i a_j - a_k^3) * prod_{l!=k} a_l^2 * t_ik t_kj."""
    a = list(spec)
    T = sp.symbols("t0:%d" % (n * n))
    tt = lambda i, j: sp.Integer(1) if i == gauge_row else T[n * i + j]
    E = []
    for i in range(n):
        for j in range(n):
            c = []
            for k in range(n):
                pr = 1
                for l in range(n):
                    if l != k:
                        pr = pr * a[l] * a[l] % p
                c.append((a[i] * a[j] - pow(a[k], 3, p)) * pr % p)
            e = sp.expand(sum(int(c[k]) * tt(i, k) * tt(k, j) for k in range(n)))
            if e != 0:
                E.append(e)
    V = [T[n * i + j] for i in range(n) for j in range(n) if i != gauge_row]
    return E, V, T, tt


def dim_from_gb(G, V):
    lms = [sp.Poly(g, *V).monoms()[0] for g in G.exprs]
    idx = list(range(len(V)))
    for r in range(len(V), -1, -1):
        for U in itertools.combinations(idx, r):
            S = set(U)
            if all(any(m[i] > 0 for i in idx if i not in S) for m in lms):
                return r
    return -1


def irr_conditions(T, tt, spec, p, n, gauge_row=0):
    """A = diag(distinct) => the A-invariant subspaces are the 2^n-2 proper coordinate
    subspaces; <A,B> is irreducible iff for every such S some entry of B leaves S.
    B = A^-2 t A t^-1, so (numerator of) B_{ij} is polynomial in t and adj(t).
    Returns the list of 2^n-2 linear-in-B forms whose non-vanishing must be saturated."""
    M = sp.Matrix(n, n, lambda i, j: tt(i, j))
    adj = M.adjugate()
    ai = [pow(int(x), p - 2, p) for x in spec]
    A = sp.diag(*[int(x) for x in spec])
    A2i = sp.diag(*[int(ai[i] * ai[i] % p) for i in range(n)])
    Bnum = sp.expand(A2i * M * A * adj)          # = det(t) * B
    forms = []
    for r in range(1, n):
        for S in itertools.combinations(range(n), r):
            Sset = set(S)
            f = sp.expand(sum(int(1 + (7 * i + 5 * j) % (p - 1)) * Bnum[i, j]
                              for j in Sset for i in range(n) if i not in Sset))
            forms.append(f)
    return forms


def s5_wall(p4=17, p3=13, limit=90.0):
    out = {}
    # (a) rank-4: raw and det-saturated dimensions -- known Dehn-filling spectrum vs random
    rng = np.random.default_rng(3)
    known4 = (2, 8, 15, 9)            # zeta_8 = 2 mod 17 -> the SECONDARY spectrum, exactly
    assert (2 * 8 * 15 * 9) % p4 == 1
    rnd4 = []
    while len(rnd4) < 3:
        x = [int(rng.integers(1, p4)) for _ in range(3)]
        x.append(pow(x[0] * x[1] * x[2], p4 - 2, p4))
        if len(set(x)) == 4 and tuple(x) != known4:
            rnd4.append(tuple(x))
    tab = []
    for lab, sp4 in [("known(secondary)", known4)] + [(f"random{i}", s) for i, s in enumerate(rnd4)]:
        E, V, T, tt = build_star(sp4, p4, 4)
        G, el, to = gb_timed(E, V, p4, limit)
        draw = dim_from_gb(G, V) if G is not None else None
        Mm = sp.Matrix(4, 4, lambda i, j: tt(i, j))
        y = sp.Symbol("y")
        G2, el2, to2 = gb_timed(E + [sp.expand(y * Mm.det() - 1)], V + [y], p4, limit)
        dsat = dim_from_gb(G2, V + [y]) if G2 is not None else None
        tab.append({"spec": list(sp4), "label": lab, "dim_raw": draw, "t_raw": round(el, 1),
                    "dim_det_sat": dsat, "t_det_sat": round(el2, 1)})
    out["rank4_dimension_table"] = tab
    known_row = tab[0]
    out["junk_dominates"] = bool(known_row["dim_det_sat"] is not None and any(
        r["dim_det_sat"] is not None and r["dim_det_sat"] >= known_row["dim_det_sat"] for r in tab[1:]))
    # (b) the variable count of the census-grade (irreducibility-saturated) ideal
    out["census_ideal_vars"] = {"rank3": (9 - 3) + (2 ** 3 - 2), "rank4": (16 - 4) + (2 ** 4 - 2),
                                "named_wall_at": 25}
    # (c) rank-3 CONTROL: the full irreducibility-saturated ideal (12 vars) at the KNOWN
    #     SL(3) Dehn-filling spectrum {1,i,-i} (B71 W1) and at random spectra
    i3 = None
    for x in range(1, p3):
        if (x * x) % p3 == p3 - 1:
            i3 = x
    known3 = (1, i3, p3 - i3)
    rnd3 = []
    while len(rnd3) < 3:
        x = [int(rng.integers(1, p3)) for _ in range(2)]
        x.append(pow(x[0] * x[1], p3 - 2, p3))
        if len(set(x)) == 3 and tuple(sorted(x)) != tuple(sorted(known3)):
            rnd3.append(tuple(x))
    tab3 = []
    for lab, s3 in [("known(W1={1,i,-i})", known3)] + [(f"random{i}", s) for i, s in enumerate(rnd3)]:
        E, V, T, tt = build_star(s3, p3, 3)
        forms = irr_conditions(T, tt, s3, p3, 3)
        ys = sp.symbols("y0:%d" % len(forms))
        E2 = E + [sp.expand(ys[i] * forms[i] - 1) for i in range(len(forms))]
        G, el, to = gb_timed(E2, V + list(ys), p3, limit)
        tab3.append({"spec": list(s3), "label": lab, "nvars": len(V) + len(ys),
                     "dim_irr": (dim_from_gb(G, V + list(ys)) if G is not None else None),
                     "t": round(el, 1), "timeout": to})
    out["rank3_control"] = tab3
    kd = tab3[0]["dim_irr"]
    out["rank3_control_discriminates"] = bool(
        kd is not None and all(r["dim_irr"] is not None and r["dim_irr"] < kd for r in tab3[1:]))
    # (d) rank-4 the same formulation: the wall curve vs the number of saturation variables
    E, V, T, tt = build_star(known4, p4, 4)
    forms = irr_conditions(T, tt, known4, p4, 4)
    curve = []
    for m in (0, 2, 4, 7, 10, 14):
        ys = sp.symbols("z0:%d" % m) if m else ()
        E2 = E + [sp.expand(ys[i] * forms[i] - 1) for i in range(m)]
        G, el, to = gb_timed(E2, V + list(ys), p4, limit)
        curve.append({"n_sat_vars": m, "nvars": len(V) + m, "t": round(el, 1),
                      "timeout": to, "dim": (dim_from_gb(G, V + list(ys)) if G is not None else None)})
        if to:
            break
    out["rank4_wall_curve"] = curve
    out["rank4_full_saturation_walls"] = bool(curve[-1]["timeout"] or curve[-1]["n_sat_vars"] < 14)
    return out


# ===========================================================================
def main():
    import importlib.util
    spec = importlib.util.spec_from_file_location("df", ROOT / "frontier/B73_sl4_apoly/dehn_filling.py")
    df = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(df)

    say("P2W6-B106 -- rank-4 Fix(T_1^2) census completion + the exact c=i point")
    say("=" * 78)

    say("\n[S1] Gamma = F_2 x|_phi Z substrate (exact normal forms)")
    R["S1"] = s1_substrate()
    say("     " + json.dumps(R["S1"]))

    say("\n[S2] THE CONJUGATION MAP Phi -- exact, in the group (hence every rank, every rep)")
    R["S2"] = s2_conjugation_theorem()
    for k, v in R["S2"].items():
        say(f"     {k}: {v}")
    say("     => (A,B,t) |-> (B, A^-1, A B^-1 t^-1);  mu' = A^-1 mu^-1 A;  L' = A^-1 L A")
    say("     => L = c mu^k  IMPLIES  L' mu'^k = c.   M^k L = 1 is the Phi-image of M^k = L.")

    say("\n[S3] rank-4 instantiation (B73 reps; Phi in closed form)")
    R["S3"] = s3_rank4(df)
    for name, rows in R["S3"].items():
        for r in rows:
            say(f"     {name:9} seed{r['seed']}: res={r['orig_res']:.1e} {list(r['orig'])} "
                f"|  Phi: res={r['phi_res']:.1e} {list(r['phi'])}  trA(Phi)={r['trA_phi_image']}")
    R["S3_exact"] = s3_new_component_exact()
    say("     EXACT (Q(omega), B89 family): " + json.dumps({k: str(v) for k, v in R["S3_exact"].items()}))

    say("\n[S4] the exact c point")
    R["S4"] = s4_exact_c(df)
    say("     " + R["S4"]["c4_is_1_exact"] + " ; gauge class " + json.dumps(R["S4"]["gauge_class"]))
    for name, seeds in R["S4"]["per_component"].items():
        for sd, d in seeds.items():
            say(f"     {name:9} seed{sd}: c over the 4 lifts = {d['c_over_the_4_lifts']} "
                f"(distinct={d['distinct_c_values']}, dev<={d['max_dev']:.1e})")
    say("     c invariant? " + json.dumps(R["S4"]["c_is_invariant"]))
    say("     banked-branch c across seeds: " + json.dumps(R["S4"]["banked_c_is_seed_dependent"]))

    say("\n[S5] census exhaustiveness over ALL rank-4 spectra -- attempt")
    R["S5"] = s5_wall()
    for r in R["S5"]["rank4_dimension_table"]:
        say(f"     rank4 {r['label']:17} spec={r['spec']} dim_raw={r['dim_raw']} "
            f"dim_det_sat={r['dim_det_sat']}  ({r['t_raw']}s / {r['t_det_sat']}s)")
    say(f"     junk (reducible) stratum dominates the dimension: {R['S5']['junk_dominates']}")
    say("     census-grade ideal variable count: " + json.dumps(R["S5"]["census_ideal_vars"]))
    for r in R["S5"]["rank3_control"]:
        say(f"     rank3 CONTROL {r['label']:19} nvars={r['nvars']} dim_irr={r['dim_irr']} "
            f"({r['t']}s, timeout={r['timeout']})")
    say(f"     rank-3 control discriminates the Dehn-filling spectrum: {R['S5']['rank3_control_discriminates']}")
    for r in R["S5"]["rank4_wall_curve"]:
        say(f"     rank4 saturation curve: sat_vars={r['n_sat_vars']:2d} nvars={r['nvars']:2d} "
            f"t={r['t']:6.1f}s timeout={r['timeout']} dim={r['dim']}")

    # =======================================================================
    # VERDICT GATE  (both branches must be able to fire and to fail)
    # =======================================================================
    g_conj = bool(R["S2"]["conjugate_relation_forced"])
    g_rank4_conj = all(
        any(lab.endswith("L=1") for lab in r["phi"]) for rows in R["S3"].values() for r in rows if r["phi_res"] < 1e-6)
    g_newcomp = bool(R["S3_exact"]["b89_family_on_variety_exact"] and R["S3_exact"]["trB_nonconstant_exact"])
    g_c = bool(R["S4"]["c_is_invariant"]["principal"] and not R["S4"]["c_is_invariant"]["secondary"]
               and len(R["S4"]["banked_c_is_seed_dependent"]["secondary"]) > 1)
    g_exhaustive = bool(R["S5"]["rank3_control_discriminates"]
                        and not R["S5"]["rank4_full_saturation_walls"])
    g_wall = bool(R["S5"]["junk_dominates"] and R["S5"]["rank4_full_saturation_walls"]
                  and R["S5"]["rank3_control_discriminates"]
                  and R["S5"]["census_ideal_vars"]["rank4"] > R["S5"]["census_ideal_vars"]["named_wall_at"])
    gates = {"conjugate_theorem_exact": g_conj, "rank4_conjugates_exhibited": g_rank4_conj,
             "phi_image_is_a_new_component_exact": g_newcomp, "c_point_exact": g_c,
             "census_exhaustive": g_exhaustive, "wall_named_and_demonstrated": g_wall}
    if g_conj and g_rank4_conj and g_newcomp and g_c and g_exhaustive:
        verdict, why = "RESOLVED-A", "census completed (component list certified) AND the c point exact"
    elif g_conj and g_rank4_conj and g_c and g_wall:
        verdict, why = "RESOLVED-B", ("the c point is exact and the D3 conjugate question is CLOSED by the "
                                      "exact Phi theorem, but full exhaustiveness over all rank-4 spectra "
                                      "hits a named wall (26-var irreducibility-saturated census ideal)")
    else:
        verdict, why = "UNRESOLVED", "neither the exhaustive census nor a demonstrated wall"
    R["gates"] = gates
    R["verdict"] = verdict
    R["reason"] = why

    say("\n" + "=" * 78)
    say("GATES: " + json.dumps(gates))
    say(f"VERDICT: {verdict} -- {why}")
    say("Structural only: no SM values, nothing to CLAIMS.md, pin untouched.")

    (HERE / "output.txt").write_text("\n".join(LOG) + "\n")
    (HERE / "results.json").write_text(json.dumps(json.loads(json.dumps(R, default=str)),
                                                  separators=(",", ":")) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
