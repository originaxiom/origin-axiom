# Testing Roadmap for Origin Axiom

**Created:** 2026-01-11
**Purpose:** Provide a comprehensive, actionable plan for implementing automated testing across all phases
**Target:** 50-70% code coverage on core src/ modules

---

## CURRENT STATE

**Existing Tests:**
- ✅ `/home/user/origin-axiom/phase2/src/phase2/modes/test_constraints.py` (4 test functions)
- ❌ No other test files in the codebase

**Test Infrastructure:**
- ✅ `pytest>=8.0` declared in phase1/pyproject.toml
- ✅ `[tool.pytest.ini_options]` configured
- ❌ No actual test files in phase1/tests/, phase3/tests/, etc.
- ❌ No CI/CD pipeline

**Assessment:** Critical gap - only 1 test file with 4 tests across entire 14,442-line codebase.

---

## TESTING STRATEGY

### Test Types

**1. Unit Tests (Priority: HIGH)**
- Test individual functions in isolation
- Fast execution (<1s per test)
- Cover edge cases and error conditions
- Target: Core computation functions

**2. Integration Tests (Priority: MEDIUM)**
- Test Snakemake workflows on small datasets
- Verify end-to-end pipelines
- Check that config changes propagate correctly
- Target: Complete figure generation

**3. Numerical Regression Tests (Priority: MEDIUM)**
- Store golden outputs for key computations
- Verify that code changes don't alter results
- Use tolerance-based comparison for floating point
- Target: Critical claims-linked computations

**4. Property-Based Tests (Priority: LOW)**
- Use hypothesis for mathematical properties
- Test that constraints preserve invariants
- Generate randomized inputs
- Target: Complex mathematical functions

**5. Schema Validation Tests (Priority: LOW)**
- Test phase0 JSON schemas
- Validate ledger system logic
- Target: Governance infrastructure

---

## PHASE-BY-PHASE ROADMAP

### Phase 1: Toy Ensembles (Estimated: 1 week)

**Priority:** HIGH - Foundation for later phases

**Files to Test:**
- `phase1/src/phase_floor.py` (308 lines)
- `phase1/src/utils_meta.py` (metadata utilities)
- `phase1/src/lattice_driver.py` (if applicable)

**Test Coverage Goals:**
- Core functions: 80%
- Plotting functions: 40% (structural only)
- Metadata functions: 60%

**Example Tests:** See Section "EXAMPLE TEST FILES" below

**Deliverables:**
```
phase1/tests/
├── __init__.py
├── test_phasor_sum.py          # Unit tests for phasor_sum
├── test_utils_meta.py           # Tests for metadata utilities
├── test_integration_figA.py     # Integration test for Figure A
└── conftest.py                  # Shared fixtures
```

---

### Phase 2: Mode-Sum + FRW (Estimated: 1.5 weeks)

**Priority:** HIGH - Already has 1 test file, expand coverage

**Files to Test:**
- `phase2/src/phase2/modes/mode_model.py` (~300 lines)
- `phase2/src/phase2/modes/constraints.py` (already has tests)
- `phase2/src/phase2/cosmology/run_frw.py` (FRW integration)
- `phase2/src/phase2/config_helpers.py` (_req, _req_float, _req_int)

**Test Coverage Goals:**
- Config helpers: 90% (critical for reproducibility)
- Mode model: 70%
- Constraints: 90% (already partially covered)
- FRW integration: 50%

**Example Tests:** See Section "EXAMPLE TEST FILES" below

**Deliverables:**
```
phase2/tests/
├── __init__.py
├── test_mode_model.py           # Unit tests for mode_model
├── test_config_helpers.py       # Tests for _req, _req_float, etc.
├── test_frw_integration.py      # Tests for FRW functions
├── test_constraints.py          # EXPAND existing file
├── test_integration_pipeline.py # Full Snakemake workflow test
├── test_regression_claim221.py  # Regression test for Claim C2.21
└── conftest.py
```

---

### Phase 3: Mechanism Module (Estimated: 1 week)

**Priority:** HIGH - Core mechanism needs solid tests

**Files to Test:**
- `phase3/src/phase3_mech/vacuum_model.py` (~200 lines)
- `phase3/src/phase3_mech/measure_v1.py` (measure functions)
- `phase3/src/phase3_mech/instability_penalty_v1.py` (penalty functions)

**Test Coverage Goals:**
- Vacuum model: 80%
- Measure functions: 70%
- Instability penalty: 60%

**Example Tests:** See Section "EXAMPLE TEST FILES" below

**Deliverables:**
```
phase3/tests/
├── __init__.py
├── test_vacuum_model.py         # Tests for amplitude functions
├── test_measure.py              # Tests for measure diagnostics
├── test_instability_penalty.py  # Tests for penalty calculations
├── test_integration_baseline.py # Integration test for baseline scan
└── conftest.py
```

---

### Phase 4: FRW Diagnostics (Estimated: 3-4 days)

**Priority:** MEDIUM - Diagnostic stub, less critical

**Files to Test:**
- FRW mapping functions
- Viability scan logic
- Corridor extraction

**Test Coverage Goals:**
- Core diagnostics: 60%
- Mapping functions: 70%

**Deliverables:**
```
phase4/tests/
├── __init__.py
├── test_frw_mappings.py
├── test_viability_scan.py
└── conftest.py
```

---

### Phase 0: Governance (Estimated: 3-4 days)

**Priority:** LOW - Governance layer, less computation-heavy

**Files to Test:**
- `phase0/phase0_ledger.py` (ledger system)
- `phase0/schemas/*.json` (JSON schema validation)

**Test Coverage Goals:**
- Ledger system: 60%
- Schema validation: 80%

**Deliverables:**
```
phase0/tests/
├── __init__.py
├── test_ledger.py
├── test_schemas.py
└── conftest.py
```

---

### Phase 5: Interface (Estimated: 2 days)

**Priority:** LOW - Interface layer

**Files to Test:**
- Interface contract functions
- Dashboard utilities

**Test Coverage Goals:**
- Interface functions: 50%

---

## EXAMPLE TEST FILES

### Example 1: `phase1/tests/test_phasor_sum.py`

```python
"""
Unit tests for phase1 phasor_sum function.

Tests cover:
- Basic functionality
- Edge cases (small n_modes, extreme twist values)
- Error conditions
- Determinism with fixed seeds
"""

from __future__ import annotations

import numpy as np
import pytest

from phase1.src.phase_floor import phasor_sum


class TestPhasorSum:
    """Tests for the phasor_sum function."""

    def test_basic_sum_deterministic(self):
        """Test that phasor_sum is deterministic with fixed seed."""
        rng1 = np.random.default_rng(42)
        rng2 = np.random.default_rng(42)

        result1 = phasor_sum(rng1, n_modes=100, twist=np.pi)
        result2 = phasor_sum(rng2, n_modes=100, twist=np.pi)

        assert result1 == result2, "Same seed should produce identical results"

    def test_output_is_complex(self):
        """Test that output is a complex number."""
        rng = np.random.default_rng(42)
        result = phasor_sum(rng, n_modes=50, twist=0.5)

        assert isinstance(result, complex)

    def test_magnitude_bounded_by_n_modes(self):
        """Test that |sum| <= n_modes (triangle inequality)."""
        rng = np.random.default_rng(42)
        n_modes = 100
        result = phasor_sum(rng, n_modes=n_modes, twist=np.pi)

        assert abs(result) <= n_modes, f"|sum| = {abs(result)} should be <= {n_modes}"

    def test_zero_twist_vs_pi_twist_differ(self):
        """Test that twist parameter affects the result."""
        rng1 = np.random.default_rng(42)
        rng2 = np.random.default_rng(42)

        result_zero = phasor_sum(rng1, n_modes=100, twist=0.0)
        result_pi = phasor_sum(rng2, n_modes=100, twist=np.pi)

        # With same seed but different twist, results should differ
        assert result_zero != result_pi, "Different twist should produce different results"

    def test_twist_fraction_affects_result(self):
        """Test that twist_fraction parameter affects the result."""
        rng1 = np.random.default_rng(42)
        rng2 = np.random.default_rng(42)

        result_half = phasor_sum(rng1, n_modes=100, twist=np.pi, twist_fraction=0.5)
        result_quarter = phasor_sum(rng2, n_modes=100, twist=np.pi, twist_fraction=0.25)

        assert result_half != result_quarter

    def test_small_n_modes(self):
        """Test edge case with small n_modes."""
        rng = np.random.default_rng(42)
        result = phasor_sum(rng, n_modes=2, twist=0.1)

        assert isinstance(result, complex)
        assert abs(result) <= 2

    def test_large_n_modes(self):
        """Test with large n_modes (should exhibit cancellation)."""
        rng = np.random.default_rng(42)
        n_modes = 10000
        result = phasor_sum(rng, n_modes=n_modes, twist=0.0, twist_fraction=0.5)

        # With many random phasors, expect |sum| << n_modes
        # Allow for statistical fluctuation: |sum| should be O(sqrt(n_modes))
        assert abs(result) < n_modes * 0.1, f"Large n_modes should exhibit cancellation"

    def test_negative_n_modes_raises(self):
        """Test that negative n_modes raises ValueError."""
        rng = np.random.default_rng(42)

        with pytest.raises(ValueError, match="n_modes must be positive"):
            phasor_sum(rng, n_modes=-10, twist=0.0)

    def test_zero_n_modes_raises(self):
        """Test that zero n_modes raises ValueError."""
        rng = np.random.default_rng(42)

        with pytest.raises(ValueError, match="n_modes must be positive"):
            phasor_sum(rng, n_modes=0, twist=0.0)

    def test_twist_fraction_out_of_range_raises(self):
        """Test that twist_fraction outside (0,1) raises ValueError."""
        rng = np.random.default_rng(42)

        with pytest.raises(ValueError, match="twist_fraction must be in"):
            phasor_sum(rng, n_modes=10, twist=0.0, twist_fraction=0.0)

        with pytest.raises(ValueError, match="twist_fraction must be in"):
            phasor_sum(rng, n_modes=10, twist=0.0, twist_fraction=1.0)

        with pytest.raises(ValueError, match="twist_fraction must be in"):
            phasor_sum(rng, n_modes=10, twist=0.0, twist_fraction=1.5)

    def test_extreme_twist_values(self):
        """Test with extreme twist values (large positive and negative)."""
        rng = np.random.default_rng(42)

        # Large positive twist
        result_large = phasor_sum(rng, n_modes=50, twist=100.0)
        assert isinstance(result_large, complex)

        # Large negative twist
        rng = np.random.default_rng(42)
        result_neg = phasor_sum(rng, n_modes=50, twist=-100.0)
        assert isinstance(result_neg, complex)


class TestRunTrials:
    """Tests for the run_trials function."""

    def test_run_trials_basic(self):
        """Test basic run_trials functionality."""
        from phase1.src.phase_floor import run_trials

        raw, floored = run_trials(
            seed=42,
            n_trials=10,
            n_modes=50,
            twist=np.pi,
            eps=1e-5,
            twist_fraction=0.5,
            enabled=True
        )

        assert len(raw) == 10
        assert len(floored) == 10
        assert np.all(raw >= 0.0), "Raw residuals should be non-negative"
        assert np.all(floored >= 0.0), "Floored residuals should be non-negative"

    def test_floor_enforced_when_enabled(self):
        """Test that floor is enforced when enabled=True."""
        from phase1.src.phase_floor import run_trials

        eps = 1e-3
        raw, floored = run_trials(
            seed=42,
            n_trials=100,
            n_modes=50,
            twist=np.pi,
            eps=eps,
            twist_fraction=0.5,
            enabled=True
        )

        # All floored values should be >= eps
        assert np.all(floored >= eps), f"All floored values should be >= {eps}"

        # Some raw values should be < eps (due to cancellation)
        assert np.any(raw < eps), "Some raw values should fall below floor"

    def test_floor_not_enforced_when_disabled(self):
        """Test that floor is not enforced when enabled=False."""
        from phase1.src.phase_floor import run_trials

        eps = 1e-3
        raw, floored = run_trials(
            seed=42,
            n_trials=100,
            n_modes=50,
            twist=np.pi,
            eps=eps,
            twist_fraction=0.5,
            enabled=False
        )

        # When disabled, floored should equal raw
        assert np.allclose(raw, floored), "When disabled, floored should equal raw"

    def test_determinism_with_seed(self):
        """Test that same seed produces identical results."""
        from phase1.src.phase_floor import run_trials

        raw1, floored1 = run_trials(
            seed=42, n_trials=20, n_modes=50, twist=np.pi,
            eps=1e-5, twist_fraction=0.5, enabled=True
        )

        raw2, floored2 = run_trials(
            seed=42, n_trials=20, n_modes=50, twist=np.pi,
            eps=1e-5, twist_fraction=0.5, enabled=True
        )

        assert np.allclose(raw1, raw2), "Same seed should produce identical raw results"
        assert np.allclose(floored1, floored2), "Same seed should produce identical floored results"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

---

### Example 2: `phase2/tests/test_config_helpers.py`

```python
"""
Unit tests for phase2 config helper functions.

These functions are critical for reproducibility - they enforce
that all required config keys are present and valid, with no hidden defaults.
"""

from __future__ import annotations

import pytest

from phase2.modes.mode_model import _req, _req_float, _req_int


class TestReqHelper:
    """Tests for the _req function (required config value fetcher)."""

    def test_fetch_top_level_key(self):
        """Test fetching a top-level key."""
        cfg = {"key1": "value1", "key2": 42}
        assert _req(cfg, "key1") == "value1"
        assert _req(cfg, "key2") == 42

    def test_fetch_nested_key(self):
        """Test fetching a nested key with dotted path."""
        cfg = {
            "mode_sum": {
                "cutoff": {
                    "value": 100.0,
                    "type": "sharp"
                }
            }
        }
        assert _req(cfg, "mode_sum.cutoff.value") == 100.0
        assert _req(cfg, "mode_sum.cutoff.type") == "sharp"

    def test_missing_top_level_key_raises(self):
        """Test that missing top-level key raises ValueError."""
        cfg = {"key1": "value1"}

        with pytest.raises(ValueError, match="Missing required config key: 'missing_key'"):
            _req(cfg, "missing_key")

    def test_missing_nested_key_raises(self):
        """Test that missing nested key raises ValueError."""
        cfg = {"mode_sum": {"cutoff": {"value": 100.0}}}

        with pytest.raises(ValueError, match="Missing required config key: 'mode_sum.cutoff.type'"):
            _req(cfg, "mode_sum.cutoff.type")

    def test_missing_intermediate_key_raises(self):
        """Test that missing intermediate key raises ValueError."""
        cfg = {"mode_sum": {"other": "value"}}

        with pytest.raises(ValueError, match="Missing required config key: 'mode_sum.cutoff.value'"):
            _req(cfg, "mode_sum.cutoff.value")

    def test_empty_config_raises(self):
        """Test that empty config raises ValueError."""
        cfg = {}

        with pytest.raises(ValueError, match="Missing required config key"):
            _req(cfg, "any.key")


class TestReqFloat:
    """Tests for the _req_float function."""

    def test_fetch_float_value(self):
        """Test fetching a float value."""
        cfg = {"epsilon": 1e-6}
        result = _req_float(cfg, "epsilon")
        assert isinstance(result, float)
        assert result == 1e-6

    def test_fetch_int_as_float(self):
        """Test that integer values are converted to float."""
        cfg = {"value": 42}
        result = _req_float(cfg, "value")
        assert isinstance(result, float)
        assert result == 42.0

    def test_fetch_string_number_as_float(self):
        """Test that numeric strings are converted to float."""
        cfg = {"value": "3.14"}
        result = _req_float(cfg, "value")
        assert isinstance(result, float)
        assert result == 3.14

    def test_nested_float(self):
        """Test fetching nested float value."""
        cfg = {"mode_sum": {"cutoff": {"value": 100.5}}}
        result = _req_float(cfg, "mode_sum.cutoff.value")
        assert result == 100.5

    def test_non_numeric_string_raises(self):
        """Test that non-numeric string raises ValueError."""
        cfg = {"value": "not_a_number"}

        with pytest.raises(ValueError, match="must be float-like"):
            _req_float(cfg, "value")

    def test_inf_raises(self):
        """Test that infinity raises ValueError."""
        cfg = {"value": float('inf')}

        with pytest.raises(ValueError, match="must be finite"):
            _req_float(cfg, "value")

    def test_nan_raises(self):
        """Test that NaN raises ValueError."""
        cfg = {"value": float('nan')}

        with pytest.raises(ValueError, match="must be finite"):
            _req_float(cfg, "value")

    def test_negative_inf_raises(self):
        """Test that negative infinity raises ValueError."""
        cfg = {"value": float('-inf')}

        with pytest.raises(ValueError, match="must be finite"):
            _req_float(cfg, "value")

    def test_missing_key_raises(self):
        """Test that missing key raises ValueError."""
        cfg = {}

        with pytest.raises(ValueError, match="Missing required config key"):
            _req_float(cfg, "missing")


class TestReqInt:
    """Tests for the _req_int function."""

    def test_fetch_int_value(self):
        """Test fetching an integer value."""
        cfg = {"n_modes": 100}
        result = _req_int(cfg, "n_modes")
        assert isinstance(result, int)
        assert result == 100

    def test_fetch_float_as_int(self):
        """Test that float values are converted to int."""
        cfg = {"value": 42.0}
        result = _req_int(cfg, "value")
        assert isinstance(result, int)
        assert result == 42

    def test_fetch_string_number_as_int(self):
        """Test that numeric strings are converted to int."""
        cfg = {"value": "123"}
        result = _req_int(cfg, "value")
        assert isinstance(result, int)
        assert result == 123

    def test_nested_int(self):
        """Test fetching nested integer value."""
        cfg = {"global": {"seed": 12345}}
        result = _req_int(cfg, "global.seed")
        assert result == 12345

    def test_float_with_decimal_truncates(self):
        """Test that float with decimal part is truncated."""
        cfg = {"value": 42.7}
        result = _req_int(cfg, "value")
        assert result == 42  # Python int() truncates

    def test_non_numeric_string_raises(self):
        """Test that non-numeric string raises ValueError."""
        cfg = {"value": "not_a_number"}

        with pytest.raises(ValueError, match="must be int-like"):
            _req_int(cfg, "value")

    def test_missing_key_raises(self):
        """Test that missing key raises ValueError."""
        cfg = {}

        with pytest.raises(ValueError, match="Missing required config key"):
            _req_int(cfg, "missing")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

---

### Example 3: `phase3/tests/test_vacuum_model.py`

```python
"""
Unit tests for phase3 vacuum model functions.

Tests cover:
- Deterministic configuration generation
- Amplitude computation
- Scanning functions
- Edge cases and invariants
"""

from __future__ import annotations

import numpy as np
import pytest

from phase3_mech.vacuum_model import (
    make_vacuum_config,
    amplitude_unconstrained,
    scan_amplitude_unconstrained,
)


class TestMakeVacuumConfig:
    """Tests for make_vacuum_config function."""

    def test_baseline_v1_deterministic(self):
        """Test that baseline_v1 config is deterministic."""
        cfg1 = make_vacuum_config("baseline_v1")
        cfg2 = make_vacuum_config("baseline_v1")

        assert np.allclose(cfg1.alphas, cfg2.alphas), "Alphas should be identical"
        assert np.array_equal(cfg1.sigmas, cfg2.sigmas), "Sigmas should be identical"

    def test_baseline_v1_has_256_modes(self):
        """Test that baseline_v1 has 256 modes."""
        cfg = make_vacuum_config("baseline_v1")

        assert len(cfg.alphas) == 256
        assert len(cfg.sigmas) == 256

    def test_alphas_in_valid_range(self):
        """Test that alphas are in [0, 2π)."""
        cfg = make_vacuum_config("baseline_v1")

        assert np.all(cfg.alphas >= 0.0)
        assert np.all(cfg.alphas < 2.0 * np.pi)

    def test_sigmas_are_small_positive_integers(self):
        """Test that sigmas are small positive integers."""
        cfg = make_vacuum_config("baseline_v1")

        # Per the code: rng.integers(1, 5, ...) generates integers in [1, 5)
        assert np.all(cfg.sigmas >= 1)
        assert np.all(cfg.sigmas < 5)
        assert cfg.sigmas.dtype == np.int64 or cfg.sigmas.dtype == int

    def test_unknown_config_name_raises(self):
        """Test that unknown config name raises ValueError."""
        with pytest.raises(ValueError, match="Unknown vacuum configuration name"):
            make_vacuum_config("unknown_config")

    def test_config_is_frozen(self):
        """Test that VacuumConfig is immutable (frozen dataclass)."""
        cfg = make_vacuum_config("baseline_v1")

        with pytest.raises(Exception):  # FrozenInstanceError or AttributeError
            cfg.alphas = np.zeros(256)


class TestAmplitudeUnconstrained:
    """Tests for amplitude_unconstrained function."""

    def test_returns_non_negative_float(self):
        """Test that amplitude is non-negative float."""
        cfg = make_vacuum_config("baseline_v1")
        amp = amplitude_unconstrained(theta=0.0, cfg=cfg)

        assert isinstance(amp, float)
        assert amp >= 0.0

    def test_bounded_by_unity(self):
        """Test that amplitude is bounded by 1.0 (max of unit phasors average)."""
        cfg = make_vacuum_config("baseline_v1")

        # Test at multiple theta values
        for theta in [0.0, np.pi/4, np.pi/2, np.pi, 2*np.pi]:
            amp = amplitude_unconstrained(theta=theta, cfg=cfg)
            assert amp <= 1.0, f"Amplitude at θ={theta} should be <= 1.0"

    def test_amplitude_varies_with_theta(self):
        """Test that amplitude varies with theta (not constant)."""
        cfg = make_vacuum_config("baseline_v1")

        thetas = np.linspace(0, 2*np.pi, 20)
        amps = [amplitude_unconstrained(theta=t, cfg=cfg) for t in thetas]

        # Amplitude should vary (not all equal)
        assert len(set(amps)) > 1, "Amplitude should vary with theta"

        # Should have some variation (std > 0)
        assert np.std(amps) > 0.0

    def test_theta_zero_vs_two_pi(self):
        """Test amplitude at θ=0 vs θ=2π."""
        cfg = make_vacuum_config("baseline_v1")

        amp_0 = amplitude_unconstrained(theta=0.0, cfg=cfg)
        amp_2pi = amplitude_unconstrained(theta=2*np.pi, cfg=cfg)

        # Due to periodicity of exp(i*sigmas*theta), these may be close but not identical
        # due to numerical precision
        # Just check they're both valid
        assert amp_0 >= 0.0
        assert amp_2pi >= 0.0

    def test_negative_theta(self):
        """Test that negative theta works."""
        cfg = make_vacuum_config("baseline_v1")
        amp = amplitude_unconstrained(theta=-np.pi, cfg=cfg)

        assert isinstance(amp, float)
        assert amp >= 0.0

    def test_large_theta(self):
        """Test that large theta values work."""
        cfg = make_vacuum_config("baseline_v1")
        amp = amplitude_unconstrained(theta=100.0, cfg=cfg)

        assert isinstance(amp, float)
        assert amp >= 0.0


class TestScanAmplitudeUnconstrained:
    """Tests for scan_amplitude_unconstrained function."""

    def test_returns_correct_length_arrays(self):
        """Test that scan returns arrays of correct length."""
        cfg = make_vacuum_config("baseline_v1")
        n_grid = 50

        thetas, amps = scan_amplitude_unconstrained(cfg, n_grid=n_grid)

        assert len(thetas) == n_grid
        assert len(amps) == n_grid

    def test_theta_range_default(self):
        """Test that default theta range is [0, 2π]."""
        cfg = make_vacuum_config("baseline_v1")
        thetas, amps = scan_amplitude_unconstrained(cfg, n_grid=100)

        assert np.isclose(thetas[0], 0.0)
        assert np.isclose(thetas[-1], 2.0 * np.pi)

    def test_theta_range_custom(self):
        """Test custom theta range."""
        cfg = make_vacuum_config("baseline_v1")
        theta_min = -np.pi
        theta_max = np.pi

        thetas, amps = scan_amplitude_unconstrained(
            cfg, n_grid=100, theta_min=theta_min, theta_max=theta_max
        )

        assert np.isclose(thetas[0], theta_min)
        assert np.isclose(thetas[-1], theta_max)

    def test_all_amplitudes_non_negative(self):
        """Test that all scanned amplitudes are non-negative."""
        cfg = make_vacuum_config("baseline_v1")
        thetas, amps = scan_amplitude_unconstrained(cfg, n_grid=100)

        assert np.all(amps >= 0.0)

    def test_all_amplitudes_bounded(self):
        """Test that all amplitudes are <= 1.0."""
        cfg = make_vacuum_config("baseline_v1")
        thetas, amps = scan_amplitude_unconstrained(cfg, n_grid=100)

        assert np.all(amps <= 1.0)

    def test_amplitudes_vary_in_scan(self):
        """Test that amplitudes show variation across scan."""
        cfg = make_vacuum_config("baseline_v1")
        thetas, amps = scan_amplitude_unconstrained(cfg, n_grid=100)

        # Should have non-trivial variation
        assert np.std(amps) > 0.0
        assert len(np.unique(amps)) > 10  # At least some variety

    def test_small_n_grid(self):
        """Test edge case with small n_grid."""
        cfg = make_vacuum_config("baseline_v1")
        thetas, amps = scan_amplitude_unconstrained(cfg, n_grid=2)

        assert len(thetas) == 2
        assert len(amps) == 2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

---

### Example 4: `phase2/tests/test_integration_pipeline.py`

```python
"""
Integration test for Phase 2 Snakemake pipeline.

This test runs a minimal version of the Phase 2 workflow on a small dataset
to verify end-to-end functionality.
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path

import pytest
import yaml


@pytest.mark.integration
@pytest.mark.slow
class TestPhase2Pipeline:
    """Integration tests for Phase 2 Snakemake workflow."""

    @pytest.fixture
    def temp_phase2_dir(self):
        """Create a temporary directory for Phase 2 test runs."""
        temp_dir = Path(tempfile.mkdtemp(prefix="phase2_test_"))
        yield temp_dir
        # Cleanup
        if temp_dir.exists():
            shutil.rmtree(temp_dir)

    @pytest.fixture
    def minimal_config(self, temp_phase2_dir):
        """Create a minimal test configuration."""
        config = {
            "global": {"seed": 42},
            "mode_sum": {
                "n_modes": 10,  # Small for fast test
                "cutoff": {
                    "value": 5.0,
                    "type": "sharp"
                },
                "epsilon": 1e-5,
                "phase_type": "uniform",
                "phase_value": "0.0"
            },
            "outputs": {
                "run_dir": str(temp_phase2_dir / "runs")
            }
        }

        config_path = temp_phase2_dir / "test_config.yaml"
        config_path.write_text(yaml.safe_dump(config))
        return config_path

    def test_pipeline_runs_without_error(self, minimal_config, temp_phase2_dir):
        """Test that the pipeline runs to completion without errors."""
        # This is a simplified example - adjust based on actual Snakefile structure

        # Run a minimal Snakemake workflow
        # You may need to adjust this based on your actual Snakefile targets
        result = subprocess.run(
            ["snakemake", "-c", "1", "--configfile", str(minimal_config), "all"],
            cwd=temp_phase2_dir,
            capture_output=True,
            text=True
        )

        # Check that the command succeeded
        assert result.returncode == 0, f"Pipeline failed: {result.stderr}"

    def test_output_files_created(self, minimal_config, temp_phase2_dir):
        """Test that expected output files are created."""
        # Run pipeline
        subprocess.run(
            ["snakemake", "-c", "1", "--configfile", str(minimal_config), "all"],
            cwd=temp_phase2_dir,
            check=True
        )

        # Check that run directory was created
        runs_dir = temp_phase2_dir / "runs"
        assert runs_dir.exists(), "Runs directory should be created"

        # Check that at least one run directory exists
        run_dirs = list(runs_dir.glob("*"))
        assert len(run_dirs) > 0, "At least one run directory should exist"

    def test_metadata_files_present(self, minimal_config, temp_phase2_dir):
        """Test that metadata files are created."""
        # Run pipeline
        subprocess.run(
            ["snakemake", "-c", "1", "--configfile", str(minimal_config), "all"],
            cwd=temp_phase2_dir,
            check=True
        )

        # Find the run directory
        runs_dir = temp_phase2_dir / "runs"
        run_dirs = list(runs_dir.glob("*"))
        assert len(run_dirs) > 0

        run_dir = run_dirs[0]

        # Check for expected metadata files
        assert (run_dir / "meta.json").exists(), "meta.json should exist"
        assert (run_dir / "params.json").exists(), "params.json should exist"
        assert (run_dir / "summary.json").exists(), "summary.json should exist"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "integration"])
```

---

### Example 5: `phase2/tests/test_regression_claim221.py`

```python
"""
Numerical regression test for Phase 2 Claim C2.21.

This test ensures that the computed value for Claim C2.21 remains stable
across code changes. If this test fails, it indicates that a code change
has altered the numerical output, which requires investigation.
"""

from __future__ import annotations

import numpy as np
import pytest

# Import the relevant computation function
# (Adjust based on actual Phase 2 structure)
# from phase2.modes.mode_model import compute_claim_221


@pytest.mark.regression
class TestClaimC221Regression:
    """Regression test for Claim C2.21 numeric value."""

    # Golden value from canonical run (phase2/CLAIMS.md)
    # This should match the value in the claims documentation
    GOLDEN_R_RAW = 1.8640648476264552
    TOLERANCE = 1e-12  # Tight tolerance for exact reproducibility

    @pytest.mark.skip(reason="Needs implementation - adjust based on actual Phase 2 API")
    def test_claim_221_value_unchanged(self):
        """
        Test that Claim C2.21 numeric value matches golden value.

        If this test fails:
        1. Check if the code change was intentional
        2. If intentional, verify correctness and update golden value
        3. If unintentional, this is a regression bug
        4. Update CLAIMS.md if golden value changes
        """
        # Load canonical config
        # config = load_phase2_config("phase2.yaml")

        # Run computation
        # result = compute_claim_221(config)
        # r_raw = result.residual_raw

        # Compare to golden value
        # assert np.isclose(r_raw, self.GOLDEN_R_RAW, rtol=0, atol=self.TOLERANCE), \
        #     f"Claim C2.21 value changed: expected {self.GOLDEN_R_RAW}, got {r_raw}"

        pass  # Remove this when implementing


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-m", "regression"])
```

---

## PYTEST CONFIGURATION

### Recommended `pyproject.toml` additions for each phase:

```toml
[tool.pytest.ini_options]
minversion = "8.0"
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "-v",
    "--strict-markers",
    "--strict-config",
    "--tb=short",
]
markers = [
    "unit: Unit tests (fast)",
    "integration: Integration tests (slower, may run Snakemake)",
    "regression: Numerical regression tests",
    "slow: Slow tests (skip with -m 'not slow')",
]

[tool.coverage.run]
source = ["src"]
omit = [
    "*/tests/*",
    "*/test_*.py",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if __name__ == .__main__.:",
    "raise AssertionError",
    "raise NotImplementedError",
]
```

---

## RUNNING TESTS

### Basic Usage

```bash
# Run all tests in a phase
cd phase1
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run only unit tests (fast)
pytest -m unit

# Run excluding slow tests
pytest -m "not slow"

# Run specific test file
pytest tests/test_phasor_sum.py

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_phasor_sum.py::TestPhasorSum::test_basic_sum_deterministic
```

### Integration with CI

```bash
# Full test suite with coverage (for CI)
pytest --cov=src --cov-report=xml --cov-report=term -m "not slow"

# Quick smoke test
pytest -m unit -x  # Stop on first failure
```

---

## COVERAGE GOALS & TRACKING

### Target Coverage by Phase

| Phase | Target Coverage | Priority | Estimated Time |
|-------|----------------|----------|----------------|
| Phase 0 | 60% | LOW | 3-4 days |
| Phase 1 | 80% (core) / 60% (overall) | HIGH | 1 week |
| Phase 2 | 70% (core) / 60% (overall) | HIGH | 1.5 weeks |
| Phase 3 | 70% (core) / 60% (overall) | HIGH | 1 week |
| Phase 4 | 60% | MEDIUM | 3-4 days |
| Phase 5 | 50% | LOW | 2 days |

### Measuring Coverage

```bash
# Generate HTML coverage report
cd phase1
pytest --cov=src --cov-report=html
open htmlcov/index.html  # View in browser

# Generate terminal report
pytest --cov=src --cov-report=term-missing

# Generate XML for CI tools
pytest --cov=src --cov-report=xml
```

---

## SHARED TESTING UTILITIES

### `conftest.py` Template

Create a `conftest.py` in each phase's `tests/` directory:

```python
"""
Shared fixtures and utilities for Phase X tests.
"""

from __future__ import annotations

import tempfile
from pathlib import Path

import numpy as np
import pytest


@pytest.fixture
def temp_output_dir():
    """Provide a temporary directory for test outputs."""
    with tempfile.TemporaryDirectory(prefix="phase_test_") as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def fixed_rng():
    """Provide a fixed RNG for deterministic tests."""
    return np.random.default_rng(42)


@pytest.fixture
def minimal_config():
    """Provide a minimal valid configuration for testing."""
    return {
        "global": {"seed": 42},
        # Add phase-specific minimal config
    }
```

---

## TIMELINE & MILESTONES

### Week 1: Foundation (Phase 1 + Phase 2 basics)
- **Days 1-3:** Implement Phase 1 unit tests (phasor_sum, utils_meta)
- **Days 4-5:** Implement Phase 2 config helper tests (critical for reproducibility)
- **Deliverable:** ~30 test functions, 50%+ coverage on Phase 1 core

### Week 2: Phase 2 Expansion
- **Days 1-3:** Phase 2 mode_model and constraints tests
- **Days 4-5:** Phase 2 integration tests (Snakemake workflow)
- **Deliverable:** Phase 2 at 60%+ coverage

### Week 3: Phase 3 + Setup CI
- **Days 1-3:** Phase 3 vacuum model tests
- **Days 4-5:** Set up GitHub Actions CI, configure pre-commit hooks
- **Deliverable:** Phase 3 at 60%+ coverage, CI running

### Week 4: Polish & Remaining Phases
- **Days 1-2:** Phase 4 tests (diagnostic stub)
- **Days 3-4:** Phase 0 governance tests (schemas, ledger)
- **Day 5:** Documentation, coverage review, final polish
- **Deliverable:** All phases tested, CI green

---

## SUCCESS CRITERIA

**Minimum Viable Test Suite (MVTS):**
- ✅ 50+ test functions across all phases
- ✅ 50%+ coverage on phase1, phase2, phase3 core modules
- ✅ All critical computation functions tested
- ✅ Config helpers fully tested (90%+ coverage)
- ✅ CI pipeline running tests on every PR
- ✅ At least 1 integration test per phase
- ✅ At least 1 regression test for key claims

**Ideal State:**
- ✅ 100+ test functions
- ✅ 70%+ coverage on phase1, phase2, phase3
- ✅ Property-based tests for mathematical invariants
- ✅ Full integration test suite
- ✅ Regression tests for all major claims
- ✅ Documentation on testing practices

---

## NEXT STEPS

1. **Review this roadmap** with project stakeholders
2. **Start with Phase 1** - implement `test_phasor_sum.py` using the example above
3. **Run first tests** - ensure pytest infrastructure works
4. **Iterate phase by phase** - follow the timeline
5. **Set up CI** - integrate with GitHub Actions (see CI_CD_WORKFLOWS.md)
6. **Maintain test suite** - add tests for any new code

---

## RELATED DOCUMENTS

- **CODE_AUDIT_2026-01.md** - Full audit report with testing gap analysis
- **IMPLEMENTATION_PLAN.md** - Prioritized action items
- **.github/workflows/*.yml** - CI/CD configuration files

---

**End of Testing Roadmap**
