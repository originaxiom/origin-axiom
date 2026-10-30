"""Step B's generator tests: scripts/stepb first on the path, and any foreign module of a generator module's name evicted
(the suite shares sys.modules within a worker; a bare-name clash would hand these tests another arc's module)."""
import pathlib, sys
GEN = pathlib.Path(__file__).resolve().parents[2] / "scripts" / "stepb"
sys.path.insert(0, str(GEN))
for _m in ['assemble', 'cells', 'census_io', 'clocks', 'compression', 'exact_tau', 'grid', 'guard', 'interp', 'kten', 'outcome', 'stepb_core', 'synth', 'p2_driver', 'calibration_driver', 'run_stepb', 'census_structure']:
    _mod = sys.modules.get(_m)
    if _mod is not None and not str(getattr(_mod, "__file__", "") or "").startswith(str(GEN)):
        del sys.modules[_m]
