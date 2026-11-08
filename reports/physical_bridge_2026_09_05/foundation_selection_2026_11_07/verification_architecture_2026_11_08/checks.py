"""Scientific bridge; imported by the custody runner only after admission."""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


source = Path(__file__).resolve().parent / "test_register_architecture.py"
spec = spec_from_file_location("architecture_scientific_checks", source)
if spec is None or spec.loader is None:
    raise ImportError("Cannot load the declared architecture controls")
science = module_from_spec(spec)
spec.loader.exec_module(science)
RegisterArchitectureControls = science.RegisterArchitectureControls
