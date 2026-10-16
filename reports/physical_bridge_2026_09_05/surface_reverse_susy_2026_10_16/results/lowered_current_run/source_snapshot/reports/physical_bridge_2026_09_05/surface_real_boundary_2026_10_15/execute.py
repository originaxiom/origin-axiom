"""Reuse the existing presealed capture instrument with this packet's pins."""
import importlib.util
from pathlib import Path
HERE=Path(__file__).resolve().parent
path=HERE.parent/'surface_mode_transport_2026_10_15/execute.py'
spec=importlib.util.spec_from_file_location('real_boundary_capture',path)
capture=importlib.util.module_from_spec(spec);spec.loader.exec_module(capture)
capture.HERE=HERE;capture.ROOT=HERE.parents[2]
if __name__=='__main__':raise SystemExit(capture.main())
