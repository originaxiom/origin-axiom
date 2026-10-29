"""Main's check of T1's (d): the share of threads with #L = #R (mod 4), by trace and by word length (B1814's enumerators)."""
import importlib.util, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sp = importlib.util.spec_from_file_location("c3", next(ROOT.glob("frontier/B1814_*/verification/census.py"))); C = importlib.util.module_from_spec(sp); sp.loader.exec_module(C)
for lab, ws in (("by trace <= 400", C.classes_by_trace(400)), ("by trace <= 200", C.classes_by_trace(200)),
                ("by word length <= 16", C.classes_by_moves(16)), ("by word length <= 14", C.classes_by_moves(14))):
    print("%-22s classes %6d  share with #L = #R mod 4: %.4f" % (lab, len(ws), sum(1 for w in ws if (w.count("L") - w.count("R")) % 4 == 0) / len(ws)))
