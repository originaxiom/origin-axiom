# Origin Axiom Code Audit - January 2026

**Audit Date:** 2026-01-11
**Auditor:** Claude (Sonnet 4.5)
**Repository:** https://github.com/originaxiom/origin-axiom/
**Commit:** fc02677 (Docs/Stage2: surface overview and joint plan companion docs)

---

## EXECUTIVE SUMMARY

This is an exceptionally well-organized and rigorously documented scientific research codebase. The project demonstrates **outstanding governance, reproducibility infrastructure, and scientific rigor** with a disciplined claims-tracking system that is rare in academic research. However, there are notable gaps in automated testing and some technical debt in dependency management.

**Overall Grade: A- (Excellent, with room for improvement in testing)**

---

## GRADING BREAKDOWN

| Component | Grade | Assessment |
|-----------|-------|------------|
| Governance & Claims Discipline | A+ | World-class, should be a model |
| Reproducibility Infrastructure | A+ | Among the best systems seen |
| Documentation | A+ | Exceptional thoroughness |
| Intellectual Honesty | A+ | Rare scientific integrity |
| Code Quality | A- | Modern, clean, professional |
| Automated Testing | C | Critical gap - only 1 test file |
| Organization & Structure | A | Clear, consistent, well-designed |

**Overall: A- (Excellent)**

---

## 1. DIRECTORY STRUCTURE & ORGANIZATION

### What Exists

**Phase Directories (phase0-5):**
- **phase0/**: Governance & specification layer (contracts, schemas, ledger system)
- **phase1/**: Toy ensembles (locked) - phasor and lattice models
- **phase2/**: Mode-sum model + bounded FRW diagnostics (under audit)
- **phase3/**: Mechanism module - vacuum non-cancellation floor
- **phase4/**: FRW toy diagnostics - cosmological mapping
- **phase5/**: Interface & sanity layer - cross-phase consistency

**Stage 2 Directories:**
- `stage2/frw_corridor_analysis/`: FRW corridor families and overlaps
- `stage2/mech_measure_analysis/`: Mechanism measure diagnostics
- `stage2/joint_mech_frw_analysis/`: Joint theta-grid analysis
- `stage2/frw_data_probe_analysis/`: Data probe audit
- `stage2/theta_star_analysis/`: Theta-star alignment diagnostics

**Support Directories:**
- `docs/`: 17 comprehensive markdown files covering governance, claims, roadmap
- `experiments/`: Archived experimental work (phase3_flavor_v1)
- `scripts/`: Build and gate validation scripts (19 scripts)
- `artifacts/`: Canonical PDF outputs for all phases (6 PDFs present)

### Organization Excellence

✅ **Clear phase separation** with explicit scoping documents
✅ **Consistent structure** across phases (paper/, src/, outputs/, workflow/)
✅ **Explicit archival** of non-canonical work (experiments/)
✅ **Downstream diagnostics** clearly separated (stage2/)
✅ **Comprehensive documentation** at every level

**Assessment:** The directory structure demonstrates mature software architecture with clear separation of concerns.

---

## 2. PROGRAMMING LANGUAGES & TOOLS

### Primary Stack

**Python (Primary Language):**
- ~70 Python files totaling ~14,442 lines of code
- Modern Python 3.10-3.13 with type hints (`from __future__ import annotations`)
- Uses numpy, scipy, matplotlib, pandas, pyyaml
- Modular package structure with proper `__init__.py` files

**Snakemake (Workflow Management):**
- ✅ 5 Snakefiles found (phase1, phase2, phase3, phase4, experiments)
- ✅ Sophisticated reproducibility with content-based signatures
- ✅ Run ID tracking and provenance metadata
- ✅ Smart caching to avoid unnecessary reruns

**LaTeX (Documentation):**
- 15+ .tex files for papers
- Professional multi-section structure
- References, appendices, claims tables

**Shell Scripts:**
- 19 gate validation and build scripts in `/scripts`
- Clear naming conventions (phase*_gate.sh, build_*.sh)

### Code Quality Observations

**Strengths:**
- ✅ Type hints in modern Python code
- ✅ Dataclasses for structured data (`@dataclass(frozen=True)`)
- ✅ Clear function documentation
- ✅ Explicit error handling with informative messages
- ✅ No hidden defaults - required config keys raise errors
- ✅ Deterministic behavior with explicit seeds

**Example from `/home/user/origin-axiom/phase2/src/phase2/modes/mode_model.py`:**
```python
def _req(cfg: Dict[str, Any], path: str) -> Any:
    """
    Fetch a required config value by dotted path.
    Raises a ValueError with a clear message if missing.
    """
```

This "no hidden defaults" philosophy is excellent for reproducibility.

**Areas for Improvement:**
- Type hint coverage inconsistent (good in newer code, missing in older files)
- Some functions are lengthy (300+ lines in run scripts)
- Docstring format not standardized (mix of inline and block comments)

---

## 3. REPRODUCIBILITY INFRASTRUCTURE

### OUTSTANDING - This is a Model System

**Snakemake Workflows:**
- ✅ Content-based signatures prevent unnecessary reruns
- ✅ Each figure has `.run_id.txt` and `.sig.txt` sidecars
- ✅ Run directories contain complete provenance
- ✅ Paper PDFs built as part of pipeline

**Provenance Tracking:**
```
phase2/outputs/runs/figA_mode_sum_residual_20251227T223708Z/
  ├── meta.json          # Git commit, timestamp, Python version
  ├── params.json        # All input parameters
  ├── summary.json       # Key numeric results
  ├── raw/               # Raw data (.npz files)
  └── figures/           # Generated plots
```

**Dependency Management:**
- phase1 has `pyproject.toml` with proper dependencies
- phase2 has minimal `pyproject.toml` (needs improvement)
- `requirements-phase1-freeze.txt` exists

**Gate Scripts:**
- 19 validation scripts in `/scripts`
- `phase0_gate.sh`, `phase1_gate.sh`, etc.
- `phase2_verify_provenance.sh` checks artifact integrity
- `phase2_verify_claims_map.sh` validates claims consistency

**Reproducibility Documentation:**
- Global: `/home/user/origin-axiom/docs/REPRODUCIBILITY.md`
- Per-phase: `phase1/REPRODUCIBILITY.md`, `phase2/REPRODUCIBILITY.md`
- Clear instructions: `snakemake -c 1 all` from phase directories

### Minor Gaps

⚠️ **Dependency Pinning:**
- phase1 specifies `numpy>=1.24` (loose versioning)
- phase2 pyproject.toml has `dependencies = []` (incomplete)
- No global requirements.txt with exact versions
- **Recommendation:** Add `requirements-freeze.txt` per phase with exact versions

⚠️ **Environment Documentation:**
- No explicit conda/venv setup script
- Could benefit from environment.yml or setup instructions

**Assessment:** The reproducibility infrastructure is among the best I've seen in academic research. The minor gaps in dependency pinning are easily addressable.

---

## 4. DOCUMENTATION COMPLETENESS

### EXCEPTIONAL - Governance-Level Documentation

**Root Level:**
- ✅ README.md (300 lines) - comprehensive overview
- ✅ ROADMAP.md (219 lines) - phase-by-phase breakdown
- ✅ REPRODUCIBILITY.md (23 lines entry point)
- ✅ PROGRESS_LOG.md (3,879 lines!) - detailed chronological log

**Global Docs (17 files in /docs):**
- ✅ PROJECT_OVERVIEW.md - Stage I structure
- ✅ PHASES.md - per-phase definitions
- ✅ CLAIMS_INDEX.md - global claims map (150 lines)
- ✅ STATE_OF_REPO.md - current status
- ✅ GATES_AND_STATUS.md - gate index
- ✅ REPO_MAP_AND_ATLAS_v1.md - directory guide
- ✅ THETA_ARCHITECTURE.md - theoretical foundations
- ✅ FUTURE_WORK_AND_ROADMAP.md - Stage II directions
- ✅ ARCHIVE.md - deprecation policy
- ✅ FRW_CORRIDOR_PROMOTION_GATE_v1.md - promotion criteria

**Per-Phase Documentation:**

Each phase has:
- README.md - quickstart and structure
- SCOPE.md - explicit boundaries
- CLAIMS.md - formal claim registry (with IDs like P2-C01)
- REPRODUCIBILITY.md - how to rebuild
- ASSUMPTIONS.md - explicit assumptions
- ROLE_IN_PROGRAM.md (phase3) - integration story

**Stage 2 Documentation:**
- 8 markdown files in stage2/docs/
- STAGE2_OVERVIEW_v1.md (150+ lines)
- Per-belt summaries (FRW_CORRIDOR, MECH_MEASURE, etc.)

**Paper Documentation:**
- 6 canonical PDFs in artifacts/ (all phases)
- LaTeX sources with sections/ subdirectories
- Appendices with claims tables and provenance

### Documentation Quality

**Strengths:**
- ✅ Clear separation of canonical vs. non-canonical
- ✅ Explicit non-claims alongside claims
- ✅ Governance documents define program structure
- ✅ Version-stamped documents (v1 suffix)
- ✅ Cross-references between documents
- ✅ Honest about limitations and failures

**Example from Phase 2 CLAIMS.md:**
```markdown
## Explicit Non-Claims (binding)

Phase 2 explicitly does NOT claim:
- a derivation of the observed value of the cosmological constant,
- an exact numerical match to observation,
- a microscopic origin of the interference phase,
- a definitive resolution of the cosmological constant problem,
```

This level of intellectual honesty is **rare and commendable**.

**Areas for Improvement:**
- Some documentation overlap across 17 files in docs/
- Could benefit from a documentation index (docs/INDEX.md)
- Navigation between related documents could be clearer

**Assessment:** The documentation is exceptional in completeness and honesty. The 3,879-line PROGRESS_LOG.md demonstrates extraordinary commitment to transparency. Minor consolidation would improve navigation.

---

## 5. CLAIMS TRACKING & GOVERNANCE IMPLEMENTATION

### OUTSTANDING - Best-in-Class Scientific Rigor

**Hierarchical Claims System:**

**Phase 0 (Governance Layer):**
- Defines claim types: existence, robustness, scaling, bounded viability
- No physics claims - only method claims
- Schema definitions for theta filters (JSON schemas in phase0/schemas/)
- Ledger system with `phase0_ledger.py`

**Phase 1 (Toy Domain):**
- Claim IDs like P1-C01, P1-C02
- Claims restricted to toy models only
- Explicit: "No phenomenology, flavor physics, θ★, φ, or unification claims"

**Phase 2 (Mode-Sum + FRW):**
- 3 formal claims (C2.1, C2.2, C2.3)
- Each claim mapped to specific figures (A-E)
- Numeric outcomes documented: `R_raw = 1.8640648476264552`
- Provenance pointers to exact run directories
- Claims-to-paper mapping table in CLAIMS.md

**Phase 3 (Mechanism):**
- Claims in paper appendix (A_claims_table.tex)
- ROLE_IN_PROGRAM.md explains scope
- Explicit deferred work section

**Phase 4 (FRW Diagnostics):**
- Diagnostic stub with toy-level FRW masks
- Explicit: "No real-data claims"
- Non-binding corridors

**Global Claims Index:**
- `/home/user/origin-axiom/docs/CLAIMS_INDEX.md`
- Maps all claims across phases
- Distinguishes canonical vs. archived

**Governance Features:**

1. **Claim IDs:** Systematic naming (P0-C01, P2-C21)
2. **Artifact Binding:** Every claim linked to reproducible artifacts
3. **Evidence Requirements:** No claim valid without canonical artifact
4. **Status Labels:** Locked, Under Audit, Active, Diagnostic Stub
5. **Promotion Gates:** Explicit gates for Stage 2 → Phase promotion
6. **Archival Policy:** Clear rules for retiring experiments

**Execution Quality:**
- ✅ Claims indexed in global CLAIMS_INDEX.md
- ✅ Per-phase CLAIMS.md files with formal statements
- ✅ Explicit non-claims prevent over-interpretation
- ✅ Verification scripts check claims consistency
- ✅ Provenance traces claims to code

### This is Exemplary

This governance system should be a **model for other scientific projects**. The discipline around "what we claim vs. what we don't claim" is remarkable and demonstrates scientific maturity rarely seen in computational research.

**Assessment:** World-class governance that sets a new standard for rigorous computational science.

---

## 6. TEST COVERAGE & VALIDATION

### CRITICAL GAP - This is the Weakest Area

**Test Files Found:**
- ❌ Only 1 test file: `/home/user/origin-axiom/phase2/src/phase2/modes/test_constraints.py`
- ❌ No comprehensive test suite
- ❌ No pytest configuration beyond phase1 declaration
- ❌ No continuous integration (CI) setup visible

**Existing Test (test_constraints.py):**
```python
def test_no_change_when_above_floor() -> None:
    eps = 1e-6
    A = 3e-6 + 4e-6j  # |A| = 5e-6 > eps
    A2, act = enforce_global_floor(A, epsilon=eps, rng=_rng())
    assert A2 == A
    assert act.applied is False
```

✅ This test is well-written but isolated.

**Testing Infrastructure:**
- phase1/pyproject.toml declares `pytest>=8.0` and testpaths
- `[tool.pytest.ini_options]` present
- But no actual test files in `phase1/tests/`

**Validation Approaches Used Instead:**

1. **Gate Scripts:**
   - 19 validation scripts (phase*_gate.sh)
   - Structural audits (phase2_structural_audit.sh)
   - Claims verification (phase2_verify_claims_map.sh)
   - Provenance checking (phase2_verify_provenance.sh)

2. **Snakemake Workflows:**
   - Each run produces summary.json with numeric results
   - Signatures detect code changes
   - Manual validation against paper claims

3. **Provenance Checking:**
   - Git commit hashes tracked
   - Run directories contain full metadata
   - Reproducibility via re-running pipelines

### Why This Matters

While the gate scripts and reproducibility infrastructure provide strong validation, **automated unit tests are critical for**:
- Catching regressions during refactoring
- Validating edge cases
- Enabling confident code changes
- Onboarding new contributors
- Scientific correctness assurance

The lack of comprehensive testing is the **single biggest weakness** in this otherwise excellent codebase.

**Assessment:** This is the most significant gap. The project would benefit enormously from comprehensive unit and integration tests. See TESTING_ROADMAP.md for detailed recommendations.

---

## 7. ISSUES & GAPS IDENTIFIED

### Critical Issues

**1. Minimal Automated Testing** (Severity: HIGH)
- Only 1 test file across entire codebase
- No CI/CD pipeline
- **Impact:** Risk of undetected regressions, difficulty refactoring
- **Recommendation:** Implement comprehensive test suite (see TESTING_ROADMAP.md)

**2. Dependency Management Inconsistency** (Severity: MEDIUM)
- phase1 has proper pyproject.toml
- phase2 has stub pyproject.toml with no dependencies
- No exact version pinning
- **Impact:** Reproducibility at risk across different environments
- **Recommendation:**
  - Complete pyproject.toml for all phases
  - Add requirements-freeze.txt with exact versions from successful runs
  - Document Python version constraints

### Medium Issues

**3. Code Duplication** (Severity: LOW-MEDIUM)
- Similar plotting code across phases
- Could extract to shared utilities
- **Impact:** Maintenance burden, inconsistent styling
- **Recommendation:** Create shared plotting library in phase1 or root

**4. Documentation Sprawl** (Severity: LOW)
- 17 docs in /docs, many overlapping
- Some information duplicated across files
- **Impact:** Navigation difficulty, potential inconsistencies
- **Recommendation:** Consider consolidating or creating a documentation index

**5. Incomplete Stage 2 Integration** (Severity: LOW)
- Stage 2 work marked as "non-canonical"
- No clear promotion path yet finalized
- **Impact:** Unclear path for Stage 2 contributions
- **Recommendation:** Finalize FRW_CORRIDOR_PROMOTION_GATE_v1.md criteria

### Minor Issues

**6. Inconsistent Docstring Style** (Severity: LOW)
- Mix of block comments and docstrings
- No standardized format (numpy/google/sphinx)
- **Recommendation:** Adopt numpy docstring convention

**7. Large Run Directories Not Tracked** (Severity: NONE)
- outputs/runs/ in .gitignore (correct)
- But no strategy for long-term preservation
- **Recommendation:** Document archival strategy for canonical run directories

**8. No Code Linting Configuration** (Severity: LOW)
- pyproject.toml has ruff line-length setting only
- No flake8, mypy, or black configuration
- **Recommendation:** Add pre-commit hooks with ruff, mypy, black

---

## 8. WHAT'S EXCELLENT

### Governance & Scientific Rigor

1. **Claims Discipline:**
   - Systematic claim IDs
   - Explicit non-claims
   - Formal evidence requirements
   - **This is world-class**

2. **Reproducibility:**
   - Snakemake workflows with content signatures
   - Complete provenance tracking
   - Run IDs and metadata
   - Gate validation scripts
   - **Among the best I've seen**

3. **Documentation:**
   - 17 docs in /docs
   - Per-phase documentation
   - 3,879-line PROGRESS_LOG.md
   - Honest about limitations
   - **Exceptional thoroughness**

4. **Phase Separation:**
   - Clear boundaries between phases
   - Stage 2 as downstream diagnostics
   - Archived experiments properly segregated
   - **Excellent architecture**

### Code Quality

5. **Modern Python:**
   - Type hints
   - Dataclasses
   - No hidden defaults
   - Explicit error handling
   - **Professional quality**

6. **Configuration Management:**
   - YAML configs
   - Required key validation
   - Deterministic behavior
   - **Well-designed**

7. **Provenance System:**
   - meta.json, params.json, summary.json
   - Git commit tracking
   - UTC timestamps
   - **Comprehensive**

### Research Integrity

8. **Intellectual Honesty:**
   - Explicit non-claims
   - Limitations sections
   - Archived failed experiments
   - Negative results documented
   - **Rare and admirable**

9. **Falsifiability:**
   - Clear criteria for claims
   - Binding numeric outcomes
   - Reproducible artifacts
   - **True scientific rigor**

---

## 9. COMPARATIVE ASSESSMENT

### Strengths vs. Typical Academic Code

| Aspect | Origin Axiom | Typical Academic Code | Assessment |
|--------|-------------|---------------------|------------|
| Documentation | Exceptional (17 docs, 3879-line log) | Minimal README | **Far Superior** |
| Reproducibility | Outstanding (Snakemake, provenance) | Script with hardcoded paths | **Far Superior** |
| Claims Tracking | Systematic governance | None | **Unique Excellence** |
| Testing | Minimal (1 test file) | None | **Slightly Better** |
| Code Quality | High (type hints, no magic) | Variable | **Superior** |
| Dependencies | Loose pinning | Often missing | **On Par** |
| Version Control | Disciplined commits, .gitignore | Sporadic | **Superior** |

### This Project Should Be a Model

The **governance structure, claims discipline, and reproducibility infrastructure** are exemplary. Other research groups should study this as a model for how to conduct rigorous computational science.

The **lack of automated testing** is the main area where typical academic code and this project are both weak, though this project's gate scripts partially compensate.

---

## 10. RECOMMENDATIONS SUMMARY

See **IMPLEMENTATION_PLAN.md** for detailed, prioritized recommendations.

### Immediate Action (Critical)

1. **Implement Core Unit Tests** (2-3 weeks)
   - Target: 50%+ coverage on src/ directories
   - Focus: phase1, phase2, phase3 core functions

2. **Pin Dependencies** (1 day)
   - Complete pyproject.toml for all phases
   - Add exact version freezes

3. **Set Up CI Pipeline** (2-3 days)
   - GitHub Actions workflow
   - Run tests on PR
   - Build papers, run gates

### Medium Priority

4. **Complete Stage 2 Integration**
5. **Consolidate Documentation**
6. **Extract Shared Utilities**

### Long-Term

7. **Regular Maintenance Schedule**
8. **Onboarding Materials**
9. **Community Engagement**

---

## CONCLUSION

The **Origin Axiom repository is an outstanding example of rigorous computational science**. Its governance structure, claims discipline, reproducibility infrastructure, and documentation are **world-class and should serve as a model for other projects**.

The code quality is high, with modern Python practices, clear organization, and excellent provenance tracking. The intellectual honesty about limitations and explicit non-claims is rare and commendable.

The **primary weakness is the lack of comprehensive automated testing**, which is critical for long-term maintainability and scientific correctness. This gap is partially offset by extensive gate validation scripts and reproducibility checks, but proper unit and integration tests are needed.

**Overall Assessment: A- (Excellent)**

**Breakdown:**
- Governance & Claims: A+
- Documentation: A+
- Reproducibility: A+
- Code Quality: A-
- Testing: C
- Organization: A

With the addition of comprehensive testing and minor improvements to dependency management, this would be an **A+ project across all dimensions**.

---

## APPENDICES

### A. Key File Locations

**Governance:**
- `/home/user/origin-axiom/docs/CLAIMS_INDEX.md`
- `/home/user/origin-axiom/phase0/phase0_ledger.py`
- `/home/user/origin-axiom/artifacts/origin-axiom-phase0.pdf`

**Reproducibility:**
- `/home/user/origin-axiom/docs/REPRODUCIBILITY.md`
- `/home/user/origin-axiom/phase1/workflow/Snakefile`
- `/home/user/origin-axiom/scripts/phase2_verify_provenance.sh`

**Claims Documentation:**
- `/home/user/origin-axiom/phase1/CLAIMS.md`
- `/home/user/origin-axiom/phase2/CLAIMS.md`
- `/home/user/origin-axiom/phase3/paper/sections/A_claims_table.tex`

**Code Examples:**
- `/home/user/origin-axiom/phase2/src/phase2/modes/mode_model.py`
- `/home/user/origin-axiom/phase2/src/phase2/modes/test_constraints.py` (only test file)
- `/home/user/origin-axiom/phase3/src/phase3/measure.py`

### B. Statistics

- **Total Python Files:** ~70
- **Lines of Python Code:** ~14,442
- **Snakemake Workflows:** 5
- **Gate Scripts:** 19
- **Documentation Files:** 17 in docs/, ~30 across phases
- **Phase PDFs:** 6 (72KB - 494KB)
- **PROGRESS_LOG.md:** 3,879 lines

### C. Related Documents

- **TESTING_ROADMAP.md** - Detailed testing implementation plan with examples
- **IMPLEMENTATION_PLAN.md** - Prioritized action items with time estimates
- **.github/workflows/** - CI/CD configuration files

---

**End of Audit Report**
