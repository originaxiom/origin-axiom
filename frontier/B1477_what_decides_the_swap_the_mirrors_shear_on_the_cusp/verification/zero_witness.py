#!/usr/bin/env python3
"""B1477 cell C4: existence at CS = 0.  For every zero-class amphichiral manifold of B1476's lists (the cusped ones
outside the family, the 37 closed): every orientation-reversing automorphism found by B1474's matrix route (word length
5, 6, 7) with its sign character eta, and for EVERY spin structure chi the mirror partner (eta.chi) o tau^-1.  A fixed chi
is an exhibited mirror-invariant spin structure (a witness -- existence is proved by it).  Non-existence is never read off
the search: a spin structure is CERTIFIED NON-INVARIANT only by the spin-signed trace spectrum (asymmetric to the sealed
cutoff) or the odd torsion (B1476's r92 certificate, rank one).  Member verdict: EXISTS (a witness) / NONE-CERTIFIED (every
spin structure certified non-invariant) / UNDECIDED."""
import sys, json, pathlib, warnings; warnings.filterwarnings("ignore")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import cusp_shear as CSH, signed_spectrum as SP
import spin_swap as SS
R, SQ, CS = CSH.R, CSH.SQ, CSH.CS
CUTOFF = 3.0


def witness(nm):
    pk, err = CS.setup_any(nm)
    if err: return dict(name=nm, error=err)
    gens = pk["gens"]; chars = SQ.characters(pk); sols, L = [], None
    for L in (5, 6, 7):
        sols = SS.find_tau(pk, L=L)
        if sols: break
    fixed = set(); bad = 0
    for s in sols:
        for chi in chars:
            try: p = SQ.mirror_partner(chi, s["tau"], s["eta"], chars)
            except AssertionError: bad += 1; continue
            if all(p[x] == chi[x] for x in gens): fixed.add(tuple(chi[x] for x in gens))
    out = dict(name=nm, h1=pk["h1"], n_spin=len(chars), L=L, n_tau=len(sols), partner_failures=bad, invariant=sorted(fixed), exists=bool(fixed),
               geometric_lift_fixed=(tuple([1] * len(gens)) in fixed))
    try:
        sp = SP.spectrum(nm, CUTOFF); out["spectrum_geodesics"] = sp["geodesics"]; out["spectrum_n_spin"] = sp["n_spin"]; out["spectrum_symmetric"] = sp["n_symmetric"]
        out["spectrum_rows"] = [(r["symmetric"], r["mismatch"], r["first_asymmetric_length"]) for r in sp["rows"]]
    except Exception as e:
        out["error_spectrum"] = repr(e)[:200]
    out["verdict"] = "EXISTS" if fixed else ("NONE-CERTIFIED" if out.get("spectrum_symmetric") == 0 and out.get("spectrum_n_spin") else "UNDECIDED")
    return out


if __name__ == "__main__":
    lists = json.load(open(CSH.FR / "B1476_the_spin_swap_phase_1c_the_quarter_law_the_pin_bit_and_what_a5_chose" / "verification" / "census_lists.json"))
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    todo = []
    if which in ("cusped", "all"): todo += [(r["name"], "cusped") for r in lists["cusped"] if not r["in_family"] and r["cls"] == "zero"]
    if which in ("closed", "all"): todo += [(r["name"], "closed") for r in lists["closed"]]
    outp = HERE / ("zero_witness_%s.json" % which); out = json.load(open(outp)) if outp.exists() else {}
    for nm, kind in todo:
        if nm in out: continue
        v = witness(nm); v["kind"] = kind; out[nm] = v
        print("%-22s %-7s spin %s  tau %s (L=%s)  invariant %s  spectrum-symmetric %s of %s  -> %s" % (nm, kind, v.get("n_spin"), v.get("n_tau"), v.get("L"), len(v.get("invariant", [])), v.get("spectrum_symmetric"), v.get("spectrum_n_spin"), v.get("verdict", v.get("error"))), flush=True)
        json.dump(out, open(outp, "w"), indent=1, default=str)
    print("DONE", flush=True)
