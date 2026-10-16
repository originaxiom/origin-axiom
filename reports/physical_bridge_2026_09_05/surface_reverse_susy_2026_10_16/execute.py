"""Credited immutable source/tree/index capture for source reverse map."""
# BANKED IDENTITY: both children replay actual source and root identities
# before returning new scientific records; this wrapper checks pins/tree.
# PRIOR ART: credited surface_mode_transport immutable capture, unmodified.
import importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('reverse_capture',HERE.parent/'surface_mode_transport_2026_10_15/execute.py')
capture=importlib.util.module_from_spec(sp);sp.loader.exec_module(capture)
capture.HERE=HERE;capture.ROOT=HERE.parents[2]
if __name__=='__main__':raise SystemExit(capture.main())
