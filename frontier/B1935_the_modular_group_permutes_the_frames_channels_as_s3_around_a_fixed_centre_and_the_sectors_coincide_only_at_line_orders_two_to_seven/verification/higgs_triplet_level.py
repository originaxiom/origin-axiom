"""B1935: the level of the frame's Higgs triplet, read from B1724's committed covariance (T's action on S's components).
Prints the eigenphases of T over 2 pi; eighth roots mean level 8, fifth roots would mean level 5."""
import json, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
d = json.loads((ROOT / "frontier/B1724_the_readings_covariance/verification/covariance.json").read_text())["part_a"]
PH = sorted(set([round(x, 9) for x in d["phase_i_over_2pi"]] + [round(x, 9) for x in d["eigenphases_over_2pi"]]))
if __name__ == "__main__":
    print("T's eigenphases on the Higgs triplet (over 2 pi):", PH, "; multiples of 1/8:", all(abs(8 * x - round(8 * x)) < 1e-9 for x in PH),
          "; multiples of 1/5:", all(abs(5 * x - round(5 * x)) < 1e-9 for x in PH))
