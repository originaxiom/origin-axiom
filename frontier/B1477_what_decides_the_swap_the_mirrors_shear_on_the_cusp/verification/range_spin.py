#!/usr/bin/env python3
"""B1477 cells C2/C3: on every ONE-CUSPED amphichiral manifold of the range (C1's output) -- every spin structure s:
  (a) the peripheral signs  tr rho_s(L), tr rho_s(Mu)  (L the rational longitude, Mu a dual class);
  (b) the cusp obstruction of Theorem A: the mirror is rhombic and tr rho_s(L) = -2  =>  s is fixed by no mirror;
  (c) the odd torsion's realness (R_1 at t = 2, 3, 0.6; H_1 of rank one only) -- necessary for invariance;
  (d) the spin-signed trace spectrum's conjugation symmetry to the sealed cutoff -- necessary for invariance.
A spin structure is CERTIFIED NON-INVARIANT if (b), or (c) fails, or (d) fails."""
import sys, json, pathlib, multiprocessing, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
CUTOFF = 2.5


def one(arg):
    name, rhombic = arg
    import cusp_shear as CSH, signed_spectrum as SP
    from mpmath import mpf
    R, SQ = CSH.R, CSH.SQ
    out = dict(name=name, rhombic=rhombic)
    try:
        sh = CSH.shear(name); out["k_parity_exact"] = sh.get("k_parity_exact"); out["k_parity_geometric"] = sh.get("k_parity_geometric"); out["cs_class"] = sh.get("cs_class")
        g = CSH.longitude_signs(name); out["h1"] = g.get("h1"); out["n_spin"] = g.get("n_spin"); out["signs"] = [(r["tr_L"], r["tr_Mu"]) for r in g.get("rows", [])]
        out["all_L_minus"] = g.get("all_L_minus"); out["n_L_plus"] = g.get("n_L_plus")
        out["theoremA_certifies"] = (sum(1 for r in g["rows"] if abs(r["tr_L"] + 2) < 1e-6) if rhombic else 0)
    except Exception as e:
        out["error_signs"] = repr(e)[:200]
    try:
        pk, err = CSH.setup_rank1(name)
        if err: out["torsion"] = err
        else:
            chars = SQ.characters(pk); gens = pk["gens"]; rows = []
            for chi in chars:
                pk2 = dict(pk); pk2["rho"] = {x: chi[x] * pk["rho"][x] for x in gens}; W = R.Wada(pk2, 1); real = True
                for t in (mpf(2), mpf(3), mpf("0.6")):
                    z = W.value(t)
                    if z is None: real = None; break
                    z = complex(z)
                    if min(abs(z.imag), abs(z.real)) > 1e-9 * max(1, abs(z)): real = False
                rows.append(real)
            out["torsion_real"] = sum(1 for x in rows if x); out["torsion_rows"] = rows
    except Exception as e:
        out["error_torsion"] = repr(e)[:200]
    try:
        sp = SP.spectrum(name, CUTOFF); out["spectrum_geodesics"] = sp["geodesics"]; out["spectrum_symmetric"] = sp["n_symmetric"]; out["spectrum_n_spin"] = sp["n_spin"]
    except Exception as e:
        out["error_spectrum"] = repr(e)[:200]
    return out


if __name__ == "__main__":
    workers = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    rows = [json.loads(l) for l in open(HERE / "range_census.jsonl") if l.strip()]
    allm = [(r["name"], r["rhombic_parity"] == 1) for r in rows if r.get("amphichiral") and r.get("cusps") == 1]
    FAMILY = {"m003", "m207", "s955", "s957", "s960", "t12838", "o10_150695", "m004", "m206", "s961", "t12839", "o10_150696", "o10_150707"}
    mem = allm[:400] + [m for m in allm[400:] if m[0] in FAMILY]     # the sealed cap: the first 400 in census order, and the family's thirteen whatever their position
    outp = HERE / "range_spin.jsonl"; done = set()
    if outp.exists(): done = {json.loads(l)["name"] for l in open(outp) if l.strip()}
    todo = [m for m in mem if m[0] not in done]
    print("one-cusped amphichiral members:", len(mem), "todo:", len(todo), flush=True)
    with multiprocessing.Pool(workers) as pool, open(outp, "a") as fh:
        for r in pool.imap_unordered(one, todo):
            fh.write(json.dumps(r, default=str) + "\n"); fh.flush()
            print("%-12s CS %-8s rhombic %-5s spin %s  L-signs all -2: %s  thmA certifies %s  torsion-real %s  spectrum-symmetric %s" % (
                r["name"], r.get("cs_class"), r["rhombic"], r.get("n_spin"), r.get("all_L_minus"), r.get("theoremA_certifies"), r.get("torsion_real", r.get("torsion")), r.get("spectrum_symmetric")), flush=True)
    print("DONE", flush=True)
