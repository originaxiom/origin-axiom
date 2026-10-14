"""Which cells of the thread frame are parameter-free? A structural read-out (chat1, 2026-10-14, night). No prediction;
no Yukawa, no mass is computed. A scratch run of the same calls preceded this committed run (disclosed).

The thread frame (FINDINGS_THREAD_FRAME.md) uses W72's construction: matter sections F_a of weight k in rho_R with one
unit each at the cusp, the theta triplet R at weight -1/2, B1644's coupling G_ab = (R.F_b)F_a + (R.F_a)F_b - (F_a.F_b)R,
of weight k_a + k_b - 1/2, and the Higgs's holomorphic mode h in rho' = rho_R (x) chi_i at that weight. A cell is
parameter-free when the matter sections and the Higgs mode are each unique.

  D1  rho_R's dimension table at -1/2, 3/2, 7/2 (quoted from the SM seat's W68 JSON, the_residual_charges_at_omega.json)
  D2  rho''s holomorphic dimensions at -3/2, 1/2, 5/2, 9/2, 13/2, by W45's formula and the collocation's null count
      (the SM seat's IW.chi and IW.dims, as W72's X3 calls them at 5/2)
  D3  the cells (k_left, k_right) in {-1/2, 3/2, 7/2}^2 with their Higgs weight and status

Run once:  python3 -B cells_readout.py > cells_readout_run.txt 2>&1   (writes cells_readout.json)
"""
import io, json, os, pathlib, subprocess, sys, tarfile, tempfile
from fractions import Fraction
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parents[1]
SMC = "87cf7f55111ec1f4019f302ffaa578376a9143e6"
TMP = pathlib.Path(tempfile.mkdtemp(prefix="cells_"))
blob = subprocess.run(["git", "-C", str(REPO), "archive", SMC, "docs/dossiers/the_weave_2026-10-07", "frontier"],
                      check=True, capture_output=True).stdout
tarfile.open(fileobj=io.BytesIO(blob)).extractall(TMP, filter="data")
DOSS = TMP / "docs" / "dossiers" / "the_weave_2026-10-07"
sys.path.insert(0, str(DOSS)); os.chdir(DOSS)
import the_surface_yukawa as SY  # noqa: E402

out = {"status": "structural read-out (chat1, 2026-10-14); no prediction; no Yukawa computed", "sm_seat_commit": SMC}
w68 = json.loads((DOSS / "the_residual_charges_at_omega.json").read_text())["read-outs"]["the dimension table"]
d1 = {}
for k in ("-1/2", "3/2", "7/2"):
    d1[k] = {"no unit": w68[f"k = {k}, u = (0, 0, 0)"]["dimension"],
             "one unit (each line)": [w68[f"k = {k}, u = {u}"]["dimension"] for u in ("(1, 0, 0)", "(0, 1, 0)", "(0, 0, 1)")]}
out["D1 rho_R (W68)"] = d1
rS2 = np.array([[complex(x) for x in row] for row in SY.RS2]); rT2 = np.array([[complex(x) for x in row] for row in SY.RT2])
d2 = {}
for k in (Fraction(-3, 2), Fraction(1, 2), Fraction(5, 2), Fraction(9, 2), Fraction(13, 2)):
    chi, lam = SY.IW.chi(k, rS2, rT2)
    null, gap = SY.IW.dims(rS2, rT2, k)
    d2[str(k)] = {"chi": round(float(chi), 9), "null count": int(null), "gap": gap}
out["D2 rho' holomorphic"] = d2
cells = {}
for kl in ("-1/2", "3/2", "7/2"):
    for kr in ("-1/2", "3/2", "7/2"):
        kh = Fraction(kl) + Fraction(kr) - Fraction(1, 2)
        mat_ok = d1[kl]["one unit (each line)"] == [1, 1, 1] and d1[kr]["one unit (each line)"] == [1, 1, 1]
        h = d2.get(str(kh), {}).get("null count")
        status = ("parameter-free" if mat_ok and h == 1 else
                  "no Higgs mode" if h == 0 else
                  "matter not unique (one free admixture per mode)" if (not mat_ok and h == 1) else
                  "Higgs not unique" if (h is not None and h > 1) else "not computed")
        cells[f"({kl}, {kr})"] = {"Higgs weight": str(kh), "Higgs dimension": h, "matter unique": mat_ok, "status": status}
out["D3 cells"] = cells
print(json.dumps(out, indent=1, default=str))
(HERE / "cells_readout.json").write_text(json.dumps(out, indent=1, default=str) + "\n")
