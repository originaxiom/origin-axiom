#!/usr/bin/env python3
"""B1494 -- the fixed-point companion of a word state, built on main: for the state b+eLR-word (SnapPy's bundle notation:
'b++LLLR' is +LLLR, 'b+-LR' is -LR = m003) the cover of degree |T| in which the cusp lifts to |T| cusps, T the torsion of
H1 (|T| = |2 - tr phi|); recorded with its H1, b1 - ends, |Sym|, volume ratio and isosig.  Usage: companions.py +LLLR -LR ...
or companions.py --census MAXLEN (every own-level word to that length, both signs, |T| <= TMAX)."""
import sys, json, pathlib, itertools
import snappy
HERE = pathlib.Path(__file__).resolve().parent


def bundle_name(state):
    eps, word = state[0], state[1:]; return "b+" + ("+" if eps == "+" else "-") + word


def torsion_order(M):
    H = M.homology(); return int(H.order()) if hasattr(H, "order") and H.betti_number() == 0 else _torsion_from_str(str(H))


def _torsion_from_str(s):
    n = 1
    for part in s.replace(" ", "").split("+"):
        if part.startswith("Z/"): n *= int(part[2:])
    return n


def companion(state):
    M = snappy.Manifold(bundle_name(state)); T = _torsion_from_str(str(M.homology())); assert M.num_cusps() == 1
    found = [C for C in M.covers(T) if C.num_cusps() == T] if T > 1 else [M]
    rows = []
    for C in found:
        H = C.homology(); rows.append(dict(degree=T, cusps=C.num_cusps(), H1=str(H), b1=H.betti_number(), b1_minus_ends=H.betti_number() - T,
                                          sym=C.symmetry_group().order(), chiral=not C.symmetry_group().is_amphicheiral(), volume_ratio=float(C.volume() / M.volume()), isosig=C.triangulation_isosig()))
    return dict(state=state, bundle=bundle_name(state), H1_state=str(M.homology()), T=T, n_candidates=len(found), companions=rows)


def census_words(maxlen):
    sys.path.insert(0, str(HERE.parents[1] / "B1434_the_architecture_census" / "verification"))
    import architecture_census as ac
    return ac.states(maxlen)


if __name__ == "__main__":
    out = []
    if sys.argv[1] == "--census":
        maxlen = int(sys.argv[2]); tmax = int(sys.argv[3]) if len(sys.argv) > 3 else 12
        for w in census_words(maxlen):
            for eps in "+-":
                M = snappy.Manifold(bundle_name(eps + w)); T = _torsion_from_str(str(M.homology()))
                if T > tmax: print(eps + w, "|T| =", T, "skipped (> %d)" % tmax, flush=True); continue
                r = companion(eps + w); out.append(r); print(r["state"], "|T| =", T, "candidates", r["n_candidates"], [(c["H1"], c["b1_minus_ends"], c["sym"]) for c in r["companions"]], flush=True)
        json.dump(out, open(HERE / f"companions_len{maxlen}.json", "w"), indent=1)
    else:
        for st in sys.argv[1:]:
            r = companion(st); out.append(r); print(json.dumps(r, indent=1))
        json.dump(out, open(HERE / "companions_named.json", "w"), indent=1)
