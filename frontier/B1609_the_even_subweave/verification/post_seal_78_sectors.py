#!/usr/bin/env python3
"""B1609 -- POST-SEAL (disclosed): the sealed E3 predicted the Z/3 sectors of the 78 on Gamma (30, 24, 24) but the sealed
instrument computed the sectors of the 27 only.  Computed here with the repaired instrument's functions, for every
decomposition of E2.  Writes post_seal_78_sectors.json."""
import json, pathlib, importlib.util
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("es", HERE / "even_subweave.py"); es = importlib.util.module_from_spec(spec); spec.loader.exec_module(es)
dec = {"E6 (principal)": [16, 8, 0], "E6(a1)": [12, 8, 4], "E6(a3)": [8, 6, 4, 4, 0], "78 through the principal sl2": [22, 16, 14, 10, 8, 2]}
out = {n: {"omega^0": -sum(es.chi_Gamma(k) for k in kk), "omega": -sum(es.chi_Gamma(k, "omega") for k in kk),
           "omega^2": -sum(es.chi_Gamma(k, "omega2") for k in kk), "level2": -sum(es.chi_Gamma2(k) for k in kk),
           "std_sector_on_SL": -sum(es.chi_SL(k, "std") for k in kk)} for n, kk in dec.items()}
json.dump(out, open(HERE / "post_seal_78_sectors.json", "w"), indent=1); print(json.dumps(out, indent=1))
