"""Loader for MAIN's FR-FIB functions (B1656 frame), exactly as the brief names them:
frontier/B1821_*/verification/cm_zero_line.py, mods()['B'].  Nothing from the agy lane is imported."""
import glob, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[4]
V = pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1821_*" / "verification"))[0])
sys.path.insert(0, str(V))
import cm_zero_line as CZ  # noqa: E402

def B():
    return CZ.mods()["B"]

def direction(name, tau):
    return CZ.direction(name, tau)

SECTORS = {"up": (1, -4), "down": (1, 2), "lepton": (-3, 6)}
