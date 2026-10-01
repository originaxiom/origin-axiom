#!/usr/bin/env python3
"""Reads the sealed run's per-level records (couplings_*.json) and decides P1-P8 as sealed.  Written after the run;
it computes nothing."""
import json, glob, sys, collections, pathlib
HERE = pathlib.Path(__file__).resolve().parent
ALLOWED10 = ["Q.Q", "Q.uc", "Q.dc", "Q.L", "uc.ec", "uc.dc", "ec.L", "dc.dc", "dc.L", "L.L"]
TRIP = ["Q.Q", "uc.ec", "uc.dc", "Q.L"]
BLOCKS = {"ten.ten": ["Q.Q", "Q.uc", "uc.ec"], "ten.five": ["Q.dc", "Q.L", "uc.dc", "ec.L"], "five.five": ["dc.dc", "dc.L", "L.L"],
          "ten.nu": ["Q.nuc", "uc.nuc", "ec.nuc"], "five.nu": ["dc.nuc", "L.nuc"]}
def read(d):
    P = dict(P1=True, P2=True, P3=False, P4=True, P5=True, P6=False, P7=True, P8=True)
    tot = disagree = own = 0; levels = []; p5 = collections.Counter(); witness = {}
    counts = collections.Counter(); one_module = collections.Counter(); block_uniform = collections.Counter(); fibre_trivial = 0
    for f in sorted(glob.glob(str(pathlib.Path(d) / "couplings_*.json"))):
        lv = json.load(open(f)); pats = collections.Counter(); name = "%s %d" % (lv["state"], lv["k"])
        for bg in lv["backgrounds"]:
            tot += 1; pr = bg["pairs"]
            if any(isinstance(v, dict) for v in pr.values()): disagree += 1; continue
            nz = {k: v[3] for k, v in pr.items()}; allowed = {k: v for k, v in pr.items() if v[0]}
            key = [tuple(x) for x in bg["key"]]
            one_module[(key[1] == key[2] == key[3]) and (key[4] == key[5])] += 1
            for b, names in BLOCKS.items():
                vals = {nz[n] for n in names if n in nz}
                if vals: block_uniform[len(vals) == 1] += 1; counts[(b, vals.pop() if len(vals) == 1 else "mixed")] += 1
            if not nz["Q.uc"]: P["P1"] = False; witness.setdefault("P1_no", name)
            if nz["Q.dc"] != nz["ec.L"]: P["P2"] = False; witness.setdefault("P2_no", name)
            if nz["Q.uc"] and not nz["Q.dc"] and not nz["ec.L"]: P["P3"] = True; witness.setdefault("P3_yes", name)
            for k, v in allowed.items():
                fibre_trivial += bool(v[2])
                if not v[2]:
                    p5[(v[3], v[4])] += 1
                    if v[3] != v[4]: P["P5"] = False; witness.setdefault("P5_no", name)
            if nz["Q.uc"] and not any(nz[k] for k in TRIP): P["P6"] = True; witness.setdefault("P6_yes", name)
            if lv["k"] == 1:
                own += 1
                if not nz["Q.uc"]: P["P7"] = False
            if not any(v[3] for v in allowed.values()): P["P8"] = False; witness.setdefault("P8_no", name)
            pats["".join("Y" if nz[k] else "0" for k in ALLOWED10)] += 1
        if len(pats) > 1: P["P4"] = False; witness.setdefault("P4_no", name)
        levels.append(dict(state=lv["state"], k=lv["k"], backgrounds=len(lv["backgrounds"]), cells=lv["cells"], primes=lv["primes"], patterns=dict(pats)))
    return dict(levels=len(levels), backgrounds=tot, prime_disagreements=disagree, own_level_backgrounds=own, predictions=P, witnesses=witness,
                pattern_columns=ALLOWED10, per_level=levels,
                P5_table={"Y_nonzero=%s,h_t_nonzero=%s" % k: v for k, v in p5.items()}, allowed_pairs_with_fibre_trivial_higgs=fibre_trivial,
                sector_modules_coincide={str(k): v for k, v in one_module.items()},
                blocks={"%s:%s" % k: v for k, v in sorted(counts.items(), key=str)}, blocks_uniform={str(k): v for k, v in block_uniform.items()})
if __name__ == "__main__":
    d = sys.argv[1] if len(sys.argv) > 1 else str(HERE)
    r = read(d); json.dump(r, open(HERE / "interaction_census_summary.json", "w"), indent=1)
    print({k: r[k] for k in ("levels", "backgrounds", "prime_disagreements", "own_level_backgrounds", "predictions", "witnesses", "P5_table", "sector_modules_coincide", "blocks", "blocks_uniform")})
