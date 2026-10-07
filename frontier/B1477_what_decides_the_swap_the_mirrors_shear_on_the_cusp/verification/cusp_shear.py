#!/usr/bin/env python3
"""B1477 instrument: the shear of the mirror on the cusp, and the sign of the longitude on every lift.

For a one-cusped hyperbolic M with rational longitude L (the primitive peripheral class dying in H_1(M;Q)) and a dual
class Mu (L.Mu = 1), an orientation-reversing isometry f acts on H_1(T) by  f(L) = e L,  f(Mu) = -e Mu + k L.
k mod 2 does not depend on the choice of Mu.  Two routes:
  (exact)      from SnapPy's complete list of self-isometries and their integer cusp maps;
  (geometric)  2 Re(z) = k (mod 2) for the cusp shape z = translation(Mu) / translation(L).
sigma_s(L) = tr rho_s(L) / 2 = +-1 on every SL(2,C) lift rho_s (every spin structure)."""
import sys, json, pathlib, itertools, warnings; warnings.filterwarnings("ignore")
import snappy
FR = next(p for p in pathlib.Path(__file__).resolve().parents if p.name == "frontier")
for d in ("B1471_the_cancellation_is_a_theorem_of_amphichirality", "B1474_the_spin_swap_phase_1a_fix_or_swap_by_the_matrix_route",
          "B1475_the_spin_swap_phase_1b_does_the_swap_carry_a_quantity", "B1476_the_spin_swap_phase_1c_the_quarter_law_the_pin_bit_and_what_a5_chose"):
    sys.path.insert(0, str(FR / d / "verification"))
import realness as R, spin_quantity as SQ
setup_rank1 = R.setup         # realness.setup (phi, H_1 of rank one); since R60-7 census_swap no longer replaces it at import
import census_swap as CS      # setup_any: the lift repaired, any H_1 rank (used explicitly below)


def dual(a, b):
    """(c, d) with a d - b c = 1"""
    for c in range(-abs(b) - 2, abs(b) + 3):
        for d in range(-abs(a) - 2, abs(a) + 3):
            if a * d - b * c == 1: return c, d
    raise ValueError((a, b))


def rational_longitude(M):
    """the primitive (a, b), in the framing basis (meridian, longitude), of the peripheral class dying in H_1(M; Q):
    every homomorphism phi: pi_1 -> Q (a null vector of the relators' exponent matrix) vanishes on it"""
    import sympy as sp
    G = M.fundamental_group(); gens, rels = G.generators(), G.relators()
    mw, lw = G.peripheral_curves()[0]
    Rm = sp.Matrix([R.expvec(r, gens) for r in rels]); ns = Rm.nullspace()
    P = sp.Matrix([[sum(v[i] * x for i, x in enumerate(R.expvec(w, gens))) for w in (mw, lw)] for v in ns])
    ker = P.nullspace()
    if len(ker) != 1: raise ValueError("peripheral image of rank %d" % (2 - len(ker)))
    v = ker[0]; L = sp.ilcm(*[sp.Rational(x).q for x in v]); v = [int(x * L) for x in v]; g = sp.igcd(*v)
    return v[0] // g, v[1] // g


def shear(name):
    M = snappy.Manifold(name)
    if M.num_cusps() != 1: return dict(name=name, error="cusps %d" % M.num_cusps())
    a, b = rational_longitude(M)
    c, d = dual(a, b)
    out = dict(name=name, longitude=(a, b), dual=(c, d))
    # exact route: every self-isometry's cusp map, rewritten in the basis (Mu, L)
    isos = M.is_isometric_to(M, return_isometries=True)
    rows = []
    for iso in isos:
        cm = iso.cusp_maps()[0]; p, q, r, s = int(cm[0, 0]), int(cm[0, 1]), int(cm[1, 0]), int(cm[1, 1])
        det = p * s - q * r
        # SnapPy: columns are the images of (meridian, longitude) in the framing basis
        def img(x, y): return (p * x + q * y, r * x + s * y)
        fL = img(a, b); fMu = img(c, d)
        # coordinates in the basis (Mu, L): v = x Mu + y L with (x, y) solving  x (c,d) + y (a,b) = v
        def coords(v): return (v[0] * b - v[1] * a) // (c * b - d * a), (c * v[1] - d * v[0]) // (c * b - d * a)
        xL, yL = coords(fL); xM, yM = coords(fMu)
        rows.append(dict(det=det, fL=(xL, yL), fMu=(xM, yM), preserves_longitude=(xL == 0 and abs(yL) == 1), k=yM))
    out["isometries"] = len(rows); out["reversing"] = [r for r in rows if r["det"] == -1]; out["preserving"] = [r for r in rows if r["det"] == 1]
    out["amphichiral"] = bool(out["reversing"])
    ks = sorted({r["k"] % 2 for r in out["reversing"]}); out["k_parity_exact"] = ks[0] if len(ks) == 1 else (None if not ks else "MIXED")
    out["k_parity_preserving"] = sorted({r["k"] % 2 for r in out["preserving"]})
    # geometric route
    tm, tl = M.cusp_translations()[0]; tm, tl = complex(tm), complex(tl)
    z = (c * tm + d * tl) / (a * tm + b * tl); two = 2 * z.real
    out["shape"] = (z.real, z.imag); out["two_re"] = two; out["two_re_residual"] = abs(two - round(two))
    out["k_parity_geometric"] = (round(two) % 2) if abs(two - round(two)) < 1e-7 else None
    out["cs"] = float(M.chern_simons()); x = out["cs"] % 0.5
    out["cs_class"] = "zero" if min(x, 0.5 - x) < 1e-7 else ("quarter" if abs(x - 0.25) < 1e-7 else "other")
    return out


def longitude_signs(name):
    """sigma_s(L) and sigma_s(Mu) for every spin structure s, from the repaired lift (any H_1 rank)"""
    pk, err = CS.setup_any(name)
    if err: return dict(error=err)
    a, b = rational_longitude(pk["M"]); c, d = dual(a, b)
    mw, lw = pk["G"].peripheral_curves()[0]
    inv = lambda w: w[::-1].swapcase()
    def pw(x, y): return (mw * x if x >= 0 else inv(mw) * (-x)) + (lw * y if y >= 0 else inv(lw) * (-y))
    Lw, Muw = pw(a, b), pw(c, d)
    chars = SQ.characters(pk); gens = pk["gens"]; rows = []
    for chi in chars:
        rho = {g: chi[g] * pk["rho"][g] for g in gens}
        tL = complex(R.word_mat(Lw, rho)[0, 0] + R.word_mat(Lw, rho)[1, 1]); tM = complex(R.word_mat(Muw, rho)[0, 0] + R.word_mat(Muw, rho)[1, 1])
        rows.append(dict(chi=[chi[g] for g in gens], tr_L=round(tL.real, 9), tr_Mu=round(tM.real, 9), im=max(abs(tL.imag), abs(tM.imag))))
    return dict(h1=pk["h1"], L_word=Lw, n_spin=len(rows), rows=rows,
                all_L_minus=all(abs(r["tr_L"] + 2) < 1e-6 for r in rows), n_L_plus=sum(1 for r in rows if abs(r["tr_L"] - 2) < 1e-6))


if __name__ == "__main__":
    for nm in sys.argv[1:]:
        s = shear(nm); print(json.dumps({k: v for k, v in s.items() if k not in ("reversing", "preserving")}, default=str))
        if "error" not in s:
            print("   reversing:", [(r["fL"], r["fMu"]) for r in s["reversing"]][:8])
            g = longitude_signs(nm); print("   H1", g.get("h1"), "L word", g.get("L_word"), "signs (tr L, tr Mu):", [(r["tr_L"], r["tr_Mu"]) for r in g.get("rows", [])])
