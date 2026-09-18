"""xB031 X1 -- THE CONTROL.  B1418's own m010 witness, through the byte-identical instrument.
If this fails, this arc reports NOTHING about the unrun modules."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from c2_reducible_index import control_m010
ok = control_m010()
print("X1 CONTROL", "PASS" if ok else "FAIL", "-- B1418's m010 witness I = +1 through this copy")
