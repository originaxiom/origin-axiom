"""Immutable source/tree/index capture including failed source snapshots."""
# BANKED IDENTITY: no overwriting failed runs. PRIOR ART: source capture.
import importlib.util
from pathlib import Path
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('arena_capture', HERE.parent/'surface_all_boson_response_2026_10_16/execute.py')
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)
capture.HERE = HERE
capture.capture.HERE = HERE
capture.capture.ROOT = HERE.parents[2]
if __name__ == '__main__':
    raise SystemExit(capture.main())
