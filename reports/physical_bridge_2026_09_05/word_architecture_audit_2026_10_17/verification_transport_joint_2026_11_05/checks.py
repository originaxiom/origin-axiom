"""Expose the two declared suites after the frozen runner admits the packet."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


HERE = Path(__file__).resolve().parent
source = HERE.parent / "verification_geometric_spin_sector_2026_11_04" / "checks.py"
spec = spec_from_file_location("joint_transport_science", source)
if spec is None or spec.loader is None:
    raise ImportError(f"Cannot load declared scientific source {source}")
science = module_from_spec(spec)
spec.loader.exec_module(science)

# Both classes share this same transport module and its declared source caches.
# Evaluate both attributes before binding either exported TestCase class.
TransportEndChecks, GeometricSpinSectorChecks = (
    science.TRANSPORT.TransportEndChecks,
    science.GeometricSpinSectorChecks,
)
