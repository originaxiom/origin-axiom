# Implementation Plan - Origin Axiom Testing & Improvements

**Created:** 2026-01-11
**Purpose:** Priority-ordered action plan for addressing audit findings
**Timeline:** 4-6 weeks for critical items, ongoing for maintenance

---

## EXECUTIVE SUMMARY

This plan addresses the findings from the January 2026 code audit. The primary focus is implementing comprehensive automated testing (the critical gap), followed by dependency management improvements and long-term maintenance strategies.

**Critical Path:** Testing infrastructure → Phase 1 tests → Phase 2 tests → CI/CD → Phase 3 tests

---

## PRIORITY LEVELS

- **P0 (Critical):** Must be done first, blocks other work or poses significant risk
- **P1 (High):** Important for project health, should be done soon
- **P2 (Medium):** Valuable improvements, schedule when capacity allows
- **P3 (Low):** Nice to have, defer if needed

---

## P0: CRITICAL PRIORITIES (Week 1-2)

### P0.1: Set Up Testing Infrastructure (Day 1)

**Objective:** Establish pytest infrastructure across all phases

**Tasks:**
1. Create test directories for each phase:
   ```bash
   mkdir -p phase1/tests phase2/tests phase3/tests phase4/tests phase0/tests
   ```

2. Add `__init__.py` to each test directory:
   ```bash
   touch phase1/tests/__init__.py
   touch phase2/tests/__init__.py
   touch phase3/tests/__init__.py
   touch phase4/tests/__init__.py
   touch phase0/tests/__init__.py
   ```

3. Create `conftest.py` in each test directory (use templates from TESTING_ROADMAP.md)

4. Update `pyproject.toml` for phases 2-5 to match phase1 pytest configuration:
   ```toml
   [build-system]
   requires = ["setuptools>=65"]
   build-backend = "setuptools.build_meta"

   [project]
   name = "phaseX"
   version = "0.1.0"
   dependencies = [
       # Add actual dependencies
   ]

   [project.optional-dependencies]
   dev = [
       "pytest>=8.0",
       "pytest-cov>=4.0",
       "hypothesis>=6.0",
   ]

   [tool.pytest.ini_options]
   minversion = "8.0"
   testpaths = ["tests"]
   python_files = ["test_*.py"]
   python_classes = ["Test*"]
   python_functions = ["test_*"]
   addopts = ["-v", "--strict-markers", "--strict-config", "--tb=short"]
   markers = [
       "unit: Unit tests (fast)",
       "integration: Integration tests (slower)",
       "regression: Numerical regression tests",
       "slow: Slow tests",
   ]
   ```

5. Verify pytest works:
   ```bash
   cd phase1 && pytest --collect-only
   cd phase2 && pytest --collect-only
   ```

**Success Criteria:**
- ✅ All test directories exist
- ✅ pytest collects tests without errors
- ✅ `pytest --version` shows 8.0+

**Time Estimate:** 2-3 hours

---

### P0.2: Implement Phase 1 Core Tests (Days 2-4)

**Objective:** Establish testing patterns with Phase 1 (foundation for other phases)

**Tasks:**
1. Implement `phase1/tests/test_phasor_sum.py`
   - Use template from TESTING_ROADMAP.md
   - Test `phasor_sum` function thoroughly
   - Cover edge cases, error conditions, determinism
   - Target: 15-20 test functions

2. Implement `phase1/tests/test_utils_meta.py`
   - Test metadata utilities (git_commit_hash, make_run_id, etc.)
   - Verify provenance tracking functions
   - Target: 10-15 test functions

3. Run tests and measure coverage:
   ```bash
   cd phase1
   pytest --cov=src --cov-report=html --cov-report=term
   ```

4. Iterate to achieve 60%+ coverage on phase1/src/

**Success Criteria:**
- ✅ 25+ test functions in Phase 1
- ✅ All tests passing
- ✅ 60%+ coverage on phase1/src/ core functions
- ✅ No test execution errors

**Time Estimate:** 2-3 days

**Files to Create:**
- `phase1/tests/test_phasor_sum.py` (~200 lines)
- `phase1/tests/test_utils_meta.py` (~150 lines)
- `phase1/tests/conftest.py` (~50 lines)

---

### P0.3: Implement Phase 2 Config Helper Tests (Days 5-6)

**Objective:** Test critical config validation functions (no hidden defaults)

**Tasks:**
1. Implement `phase2/tests/test_config_helpers.py`
   - Use template from TESTING_ROADMAP.md
   - Test `_req`, `_req_float`, `_req_int` exhaustively
   - Cover missing keys, invalid types, edge cases
   - Target: 20+ test functions

2. Run tests:
   ```bash
   cd phase2
   pytest tests/test_config_helpers.py -v
   ```

3. Achieve 90%+ coverage on config helper functions

**Success Criteria:**
- ✅ 20+ test functions for config helpers
- ✅ All tests passing
- ✅ 90%+ coverage on _req, _req_float, _req_int
- ✅ Confidence that config validation is robust

**Time Estimate:** 1-2 days

**Files to Create:**
- `phase2/tests/test_config_helpers.py` (~250 lines)
- `phase2/tests/conftest.py` (~50 lines)

---

### P0.4: Expand Phase 2 Constraints Tests (Day 7)

**Objective:** Build on existing test_constraints.py

**Tasks:**
1. Read existing `phase2/src/phase2/modes/test_constraints.py`

2. Add more test cases:
   - Edge cases for epsilon values (very small, very large)
   - Numerical precision tests
   - Complex number edge cases
   - Boundary conditions

3. Move test file to proper location:
   ```bash
   mv phase2/src/phase2/modes/test_constraints.py phase2/tests/test_constraints.py
   ```

4. Update imports as needed

5. Expand to 10-15 test functions (currently has 4)

**Success Criteria:**
- ✅ 10+ test functions in test_constraints.py
- ✅ All tests passing
- ✅ 90%+ coverage on constraints.py

**Time Estimate:** 1 day

---

## P1: HIGH PRIORITIES (Week 2-3)

### P1.1: Implement Phase 2 Mode Model Tests (Days 8-10)

**Objective:** Test core Phase 2 mode-sum computation

**Tasks:**
1. Implement `phase2/tests/test_mode_model.py`
   - Test ModeSumInputs and ModeSumResult dataclasses
   - Test mode computation functions
   - Test that inputs are properly validated
   - Target: 15-20 test functions

2. Measure coverage:
   ```bash
   cd phase2
   pytest --cov=src/phase2/modes --cov-report=term
   ```

3. Iterate to achieve 70%+ coverage on mode_model.py

**Success Criteria:**
- ✅ 15+ test functions
- ✅ 70%+ coverage on mode_model.py
- ✅ All tests passing

**Time Estimate:** 2-3 days

**Files to Create:**
- `phase2/tests/test_mode_model.py` (~300 lines)

---

### P1.2: Implement Phase 3 Vacuum Model Tests (Days 11-13)

**Objective:** Test core Phase 3 mechanism functions

**Tasks:**
1. Implement `phase3/tests/test_vacuum_model.py`
   - Use template from TESTING_ROADMAP.md
   - Test make_vacuum_config determinism
   - Test amplitude_unconstrained function
   - Test scan functions
   - Target: 20+ test functions

2. Implement `phase3/tests/test_measure.py`
   - Test measure diagnostic functions
   - Target: 10-15 test functions

3. Run tests and measure coverage:
   ```bash
   cd phase3
   pytest --cov=src --cov-report=html
   ```

**Success Criteria:**
- ✅ 30+ test functions in Phase 3
- ✅ 70%+ coverage on vacuum_model.py
- ✅ 60%+ coverage on measure_v1.py
- ✅ All tests passing

**Time Estimate:** 2-3 days

**Files to Create:**
- `phase3/tests/test_vacuum_model.py` (~350 lines)
- `phase3/tests/test_measure.py` (~200 lines)
- `phase3/tests/conftest.py` (~50 lines)

---

### P1.3: Set Up CI/CD Pipeline (Days 14-15)

**Objective:** Automate testing on every commit/PR

**Tasks:**
1. Create `.github/workflows/test-phase1.yml` (see CI/CD section below)

2. Create `.github/workflows/test-phase2.yml`

3. Create `.github/workflows/test-phase3.yml`

4. Create `.github/workflows/test-all.yml` (runs all phases)

5. Test workflows:
   - Push to a feature branch
   - Verify that CI runs
   - Check that tests pass in CI environment

6. Add status badge to README.md:
   ```markdown
   ![Tests](https://github.com/originaxiom/origin-axiom/workflows/tests/badge.svg)
   ```

**Success Criteria:**
- ✅ CI runs on every push
- ✅ All tests pass in CI
- ✅ Status badge in README
- ✅ CI fails appropriately when tests fail

**Time Estimate:** 1-2 days

**Files to Create:**
- `.github/workflows/test-phase1.yml`
- `.github/workflows/test-phase2.yml`
- `.github/workflows/test-phase3.yml`
- `.github/workflows/test-all.yml`

**See:** CI/CD_WORKFLOWS.md for full configurations

---

### P1.4: Pin Dependencies (Day 16)

**Objective:** Ensure reproducibility across environments

**Tasks:**
1. For each phase, activate working environment and generate freeze file:
   ```bash
   cd phase1
   pip freeze > requirements-freeze.txt
   ```

2. Update pyproject.toml for each phase with actual dependencies:
   ```toml
   [project]
   dependencies = [
       "numpy==1.26.3",
       "scipy==1.11.4",
       "matplotlib==3.8.2",
       "pyyaml==6.0.1",
   ]
   ```

3. Document Python version requirements:
   - Test with Python 3.10, 3.11, 3.12
   - Document minimum supported version

4. Create root-level `requirements-dev.txt`:
   ```
   pytest>=8.0
   pytest-cov>=4.0
   hypothesis>=6.0
   ruff>=0.1.0
   mypy>=1.7
   ```

5. Update per-phase REPRODUCIBILITY.md with environment setup:
   ```markdown
   ## Environment Setup

   **Python:** 3.10-3.12

   **Install dependencies:**
   ```bash
   pip install -e .[dev]
   # or
   pip install -r requirements-freeze.txt
   ```

**Success Criteria:**
- ✅ requirements-freeze.txt exists for phase1, phase2, phase3
- ✅ pyproject.toml has complete dependencies for each phase
- ✅ Documentation updated
- ✅ Can create fresh environment and reproduce results

**Time Estimate:** 1 day

---

## P2: MEDIUM PRIORITIES (Week 4-5)

### P2.1: Implement Integration Tests (Days 17-19)

**Objective:** Test end-to-end workflows

**Tasks:**
1. Implement `phase2/tests/test_integration_pipeline.py`
   - Use template from TESTING_ROADMAP.md
   - Test Snakemake workflow on minimal dataset
   - Verify output files are created
   - Check metadata files
   - Target: 3-5 integration tests

2. Mark as `@pytest.mark.integration` and `@pytest.mark.slow`

3. Configure CI to run integration tests on a schedule (nightly) but not on every PR

**Success Criteria:**
- ✅ 3+ integration tests
- ✅ Tests verify end-to-end workflow
- ✅ CI configured to run integration tests appropriately

**Time Estimate:** 2-3 days

**Files to Create:**
- `phase2/tests/test_integration_pipeline.py` (~200 lines)
- Similar for phase1, phase3

---

### P2.2: Implement Regression Tests for Key Claims (Days 20-21)

**Objective:** Prevent unintended changes to claim numeric values

**Tasks:**
1. Identify key claims with binding numeric values:
   - Phase 2: Claim C2.21 (R_raw = 1.8640648476264552)
   - Phase 1: Key lattice existence results
   - Phase 3: Binding regime diagnostics

2. Implement regression tests:
   - `phase2/tests/test_regression_claim221.py` (use template)
   - Store golden values
   - Test with tight tolerance

3. Document update procedure:
   ```markdown
   ## Updating Regression Tests

   If a regression test fails:
   1. Investigate why the value changed
   2. If change is intentional and verified correct:
      - Update golden value in test
      - Update value in CLAIMS.md
      - Document reason in commit message
   3. If change is unintentional, fix the bug
   ```

**Success Criteria:**
- ✅ Regression tests for top 3-5 claims
- ✅ Tests fail when values change
- ✅ Documentation on update procedure

**Time Estimate:** 2 days

**Files to Create:**
- `phase2/tests/test_regression_claim221.py`
- Similar for other phases

---

### P2.3: Extract Shared Plotting Utilities (Days 22-24)

**Objective:** Reduce code duplication across phases

**Tasks:**
1. Identify common plotting patterns:
   - Figure styling (consistent fonts, colors)
   - Axis labeling conventions
   - Saving with provenance metadata

2. Create `phase1/src/shared_plotting.py`:
   ```python
   def setup_origin_axiom_style():
       """Apply consistent styling for Origin Axiom figures."""
       ...

   def save_figure_with_metadata(fig, path, run_id, ...):
       """Save figure with consistent metadata."""
       ...
   ```

3. Refactor phase1, phase2, phase3 plotting code to use shared utilities

4. Add tests for shared utilities

**Success Criteria:**
- ✅ Shared plotting module created
- ✅ At least 2 phases refactored to use it
- ✅ No change in output figures
- ✅ Tests for shared utilities

**Time Estimate:** 2-3 days

---

### P2.4: Complete Phase 4 and Phase 5 Tests (Days 25-27)

**Objective:** Achieve basic test coverage for remaining phases

**Tasks:**
1. Phase 4 tests:
   - Test FRW mapping functions
   - Test viability scan logic
   - Target: 15+ test functions, 60% coverage

2. Phase 5 tests:
   - Test interface contract functions
   - Target: 10+ test functions, 50% coverage

**Success Criteria:**
- ✅ Phase 4 at 60% coverage
- ✅ Phase 5 at 50% coverage
- ✅ All tests passing

**Time Estimate:** 2-3 days

---

### P2.5: Complete Stage 2 Integration Plan (Days 28-30)

**Objective:** Finalize promotion path for Stage 2 work

**Tasks:**
1. Review `docs/FRW_CORRIDOR_PROMOTION_GATE_v1.md`

2. Define concrete promotion criteria:
   - What tests must pass?
   - What documentation is required?
   - What review process?

3. Create promotion checklist:
   ```markdown
   ## Stage 2 → Phase Promotion Checklist

   - [ ] All tests passing
   - [ ] Coverage >= 60%
   - [ ] CLAIMS.md updated
   - [ ] Paper appendix includes claim table
   - [ ] Provenance complete
   - [ ] Gate validation passes
   - [ ] Peer review complete
   ```

4. Update ROADMAP.md with promotion timeline

**Success Criteria:**
- ✅ Clear promotion criteria documented
- ✅ Checklist for promotion
- ✅ Timeline in ROADMAP.md

**Time Estimate:** 2-3 days

---

## P3: LOW PRIORITIES (Week 6+)

### P3.1: Add Code Linting and Formatting

**Objective:** Enforce consistent code style

**Tasks:**
1. Configure ruff for linting:
   ```toml
   [tool.ruff]
   line-length = 100
   target-version = "py310"
   select = ["E", "F", "I", "N", "W", "UP"]
   ignore = ["E501"]  # Line too long (already set line-length)
   ```

2. Configure black for formatting:
   ```toml
   [tool.black]
   line-length = 100
   target-version = ['py310', 'py311', 'py312']
   ```

3. Configure mypy for type checking:
   ```toml
   [tool.mypy]
   python_version = "3.10"
   warn_return_any = true
   warn_unused_configs = true
   disallow_untyped_defs = false  # Start lenient, tighten over time
   ```

4. Set up pre-commit hooks:
   ```yaml
   # .pre-commit-config.yaml
   repos:
     - repo: https://github.com/astral-sh/ruff-pre-commit
       rev: v0.1.9
       hooks:
         - id: ruff
     - repo: https://github.com/psf/black
       rev: 23.12.1
       hooks:
         - id: black
   ```

5. Run on entire codebase:
   ```bash
   ruff check . --fix
   black .
   ```

**Success Criteria:**
- ✅ Linting configuration in pyproject.toml
- ✅ Pre-commit hooks set up
- ✅ CI runs linting checks
- ✅ Codebase passes linting

**Time Estimate:** 1-2 days

---

### P3.2: Standardize Docstring Format

**Objective:** Consistent documentation style

**Tasks:**
1. Choose numpy docstring convention:
   ```python
   def function(param1: int, param2: float) -> str:
       """
       Brief description.

       Longer description if needed.

       Parameters
       ----------
       param1 : int
           Description of param1
       param2 : float
           Description of param2

       Returns
       -------
       str
           Description of return value
       """
   ```

2. Document convention in CONTRIBUTING.md

3. Gradually convert existing docstrings (low priority, do during normal maintenance)

**Success Criteria:**
- ✅ Convention documented
- ✅ New code follows convention
- ✅ Existing critical functions converted

**Time Estimate:** Ongoing

---

### P3.3: Consolidate Documentation

**Objective:** Improve documentation navigation

**Tasks:**
1. Create `docs/INDEX.md`:
   ```markdown
   # Origin Axiom Documentation Index

   ## Getting Started
   - [README.md](../README.md) - Project overview
   - [REPRODUCIBILITY.md](../docs/REPRODUCIBILITY.md) - How to reproduce results

   ## Governance
   - [CLAIMS_INDEX.md](CLAIMS_INDEX.md) - Global claims registry
   - [PHASES.md](PHASES.md) - Phase definitions
   - [GATES_AND_STATUS.md](GATES_AND_STATUS.md) - Gate status

   ## Development
   - [TESTING_ROADMAP.md](../TESTING_ROADMAP.md) - Testing strategy
   - [IMPLEMENTATION_PLAN.md](../IMPLEMENTATION_PLAN.md) - Action items
   - [CODE_AUDIT_2026-01.md](CODE_AUDIT_2026-01.md) - Audit report

   ...
   ```

2. Add cross-references between related docs

3. Mark historical vs. authoritative docs

**Success Criteria:**
- ✅ docs/INDEX.md exists
- ✅ Easy to navigate documentation
- ✅ Clear which docs are authoritative

**Time Estimate:** 1 day

---

### P3.4: Phase 0 Governance Tests

**Objective:** Test governance infrastructure

**Tasks:**
1. Implement `phase0/tests/test_ledger.py`
   - Test ledger append operations
   - Test claim validation
   - Target: 10+ test functions

2. Implement `phase0/tests/test_schemas.py`
   - Test JSON schema validation
   - Test that valid inputs pass
   - Test that invalid inputs fail
   - Target: 10+ test functions

**Success Criteria:**
- ✅ 20+ tests for Phase 0
- ✅ 60% coverage on ledger system

**Time Estimate:** 3-4 days

---

### P3.5: Property-Based Testing

**Objective:** Use hypothesis for mathematical properties

**Tasks:**
1. Install hypothesis:
   ```bash
   pip install hypothesis
   ```

2. Add property-based tests for mathematical invariants:
   ```python
   from hypothesis import given, strategies as st

   @given(st.integers(min_value=1, max_value=10000))
   def test_phasor_sum_bounded(n_modes):
       """Property: |sum| <= n_modes for any n_modes."""
       rng = np.random.default_rng(42)
       result = phasor_sum(rng, n_modes=n_modes, twist=0.0)
       assert abs(result) <= n_modes
   ```

3. Focus on:
   - Amplitude bounds
   - Constraint preservation
   - Numerical stability

**Success Criteria:**
- ✅ 5+ property-based tests
- ✅ Tests catch edge cases

**Time Estimate:** 2-3 days

---

## ONGOING MAINTENANCE

### M1: Regular Dependency Updates

**Frequency:** Quarterly

**Tasks:**
1. Update dependencies:
   ```bash
   pip list --outdated
   pip install --upgrade numpy scipy matplotlib
   pip freeze > requirements-freeze.txt
   ```

2. Run full test suite:
   ```bash
   pytest --cov=src
   ```

3. Re-run gate validation:
   ```bash
   bash scripts/phase1_gate.sh
   bash scripts/phase2_gate.sh
   ```

4. Update PROGRESS_LOG.md with dependency updates

---

### M2: Monthly Gate Validation

**Frequency:** Monthly

**Tasks:**
1. Run all gate scripts:
   ```bash
   for script in scripts/phase*_gate.sh; do
       echo "Running $script"
       bash "$script"
   done
   ```

2. Verify all gates pass

3. If any gates fail, investigate and fix

---

### M3: Test Coverage Review

**Frequency:** Quarterly

**Tasks:**
1. Generate coverage reports for all phases:
   ```bash
   cd phase1 && pytest --cov=src --cov-report=html
   cd phase2 && pytest --cov=src --cov-report=html
   cd phase3 && pytest --cov=src --cov-report=html
   ```

2. Identify uncovered critical functions

3. Add tests to improve coverage

**Target:** Maintain 60%+ coverage on all core modules

---

### M4: Regression Test Updates

**Frequency:** As needed (when claims change)

**Tasks:**
1. When a claim's numeric value changes:
   - Verify change is intentional
   - Update regression test golden value
   - Update CLAIMS.md
   - Document in commit message

2. When adding new claims:
   - Add regression test
   - Document golden value

---

## TIMELINE SUMMARY

| Week | Focus | Deliverables |
|------|-------|--------------|
| 1 | Testing infrastructure + Phase 1 | 25+ tests, 60% coverage on Phase 1 |
| 2 | Phase 2 core tests + Phase 3 start | 40+ tests, 70% coverage on Phase 2 core |
| 3 | Phase 3 completion + CI/CD | CI pipeline running, Phase 3 at 70% |
| 4 | Integration tests + Regression tests | End-to-end workflows tested |
| 5 | Phase 4/5 + Stage 2 planning | All phases tested |
| 6+ | Polishing, linting, documentation | Production-ready test suite |

---

## SUCCESS METRICS

**After 2 weeks:**
- ✅ 50+ test functions across Phase 1 and Phase 2
- ✅ 60%+ coverage on Phase 1 and Phase 2 core modules
- ✅ CI pipeline running
- ✅ Dependencies pinned

**After 4 weeks:**
- ✅ 100+ test functions across all phases
- ✅ 60%+ coverage on Phase 1, 2, 3 core modules
- ✅ Integration tests for main workflows
- ✅ Regression tests for key claims
- ✅ Grade improves from C to B+ on testing

**After 6 weeks:**
- ✅ 150+ test functions
- ✅ 70%+ coverage on core computation modules
- ✅ All priorities P0, P1, P2 complete
- ✅ Code linting and formatting in place
- ✅ Grade improves from A- to A overall

---

## RISK MITIGATION

**Risk:** Testing takes longer than estimated
- **Mitigation:** Focus on P0 and P1 items first, defer P2/P3 if needed

**Risk:** Tests reveal bugs in existing code
- **Mitigation:** Expected! Fix bugs as discovered, document in PROGRESS_LOG.md

**Risk:** CI costs become significant
- **Mitigation:** Use GitHub Actions free tier (2000 minutes/month), optimize test execution time

**Risk:** Team capacity constraints
- **Mitigation:** This plan is designed for 1-2 developers over 4-6 weeks. Can be parallelized if more developers available.

---

## RESOURCE REQUIREMENTS

**Personnel:**
- 1-2 developers
- Part-time (can be done alongside other work)

**Tools:**
- pytest, pytest-cov (free, open source)
- GitHub Actions (free tier sufficient)
- ruff, black, mypy (free, open source)

**Compute:**
- GitHub Actions: ~500-1000 minutes/month for CI
- Local development: Standard Python environment

---

## TRACKING PROGRESS

### Weekly Checkpoints

Create weekly progress reports in PROGRESS_LOG.md:

```markdown
## Week 1 Progress (2026-01-13 to 2026-01-19)

**Completed:**
- ✅ P0.1: Testing infrastructure set up
- ✅ P0.2: Phase 1 core tests implemented (25 test functions)
- ⏳ P0.3: Phase 2 config helper tests (in progress)

**Blockers:**
- None

**Next Week:**
- Complete P0.3 and P0.4
- Start P1.1 (Phase 2 mode model tests)
```

### Coverage Tracking

Track coverage metrics over time:

| Date | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Overall |
|------|---------|---------|---------|---------|---------|
| 2026-01-11 (baseline) | 0% | <5% | 0% | 0% | <2% |
| 2026-01-19 (Week 1) | 60% | 30% | 0% | 0% | 30% |
| 2026-01-26 (Week 2) | 65% | 70% | 40% | 0% | 55% |
| 2026-02-02 (Week 3) | 70% | 75% | 70% | 30% | 65% |
| Target (Week 6) | 75% | 75% | 75% | 60% | 70%+ |

---

## NEXT STEPS

**Immediate (Today):**
1. Review this plan with stakeholders
2. Begin P0.1 (set up testing infrastructure)
3. Create feature branch: `feature/testing-infrastructure`

**This Week:**
1. Complete P0.1-P0.4 (testing infrastructure + Phase 1/2 core tests)
2. Open draft PR with initial tests
3. Validate CI workflow configuration

**This Month:**
1. Complete P0 and P1 priorities
2. Merge testing PR
3. Begin P2 priorities

---

## RELATED DOCUMENTS

- **CODE_AUDIT_2026-01.md** - Full audit report
- **TESTING_ROADMAP.md** - Detailed testing strategy with examples
- **.github/workflows/** - CI/CD configurations (to be created)

---

**End of Implementation Plan**
