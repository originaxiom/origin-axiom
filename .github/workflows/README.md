# GitHub Actions CI/CD Workflows

This directory contains automated workflows for continuous integration and testing of the Origin Axiom repository.

## Workflows Overview

### Test Workflows

**`test-phase1.yml`, `test-phase2.yml`, `test-phase3.yml`**
- **Trigger:** Push to main/develop/claude/* branches, or PR affecting phase files
- **Purpose:** Run unit tests for individual phases
- **Matrix:** Tests across Python 3.10, 3.11, 3.12
- **Coverage:** Uploads coverage reports to Codecov, fails if coverage < 50%
- **Duration:** ~2-5 minutes per phase

**`test-all.yml`**
- **Trigger:** Push to main/develop, PRs, nightly schedule (2 AM UTC)
- **Purpose:** Comprehensive test suite across all phases
- **Jobs:**
  - `test-all-phases`: Run all phase tests in parallel
  - `integration-tests`: Run slow integration tests (nightly only)
  - `gate-validation`: Run gate validation scripts
  - `summary`: Aggregate results
- **Duration:** ~10-15 minutes

### Code Quality Workflows

**`lint.yml`**
- **Trigger:** Push to any branch, PRs
- **Purpose:** Check code style and type hints
- **Tools:**
  - `ruff`: Fast Python linter (checks PEP 8, imports, naming)
  - `mypy`: Static type checker (non-blocking)
- **Duration:** ~1-2 minutes

### Build Workflows

**`build-papers.yml`**
- **Trigger:** Push/PR affecting paper LaTeX files
- **Purpose:** Verify LaTeX papers compile successfully
- **Builds:** Phase 0, 1, 2, 3 papers
- **Artifacts:** Uploads generated PDFs
- **Duration:** ~3-5 minutes

## Workflow Triggers

| Workflow | Push (main/develop) | Push (feature) | Pull Request | Nightly | Manual |
|----------|---------------------|----------------|--------------|---------|--------|
| test-phase1 | ✅ (if phase1/* changed) | ✅ (if phase1/* changed) | ✅ | ❌ | ✅ |
| test-phase2 | ✅ (if phase2/* changed) | ✅ (if phase2/* changed) | ✅ | ❌ | ✅ |
| test-phase3 | ✅ (if phase3/* changed) | ✅ (if phase3/* changed) | ✅ | ❌ | ✅ |
| test-all | ✅ | ❌ | ✅ | ✅ | ✅ |
| lint | ✅ | ✅ | ✅ | ❌ | ✅ |
| build-papers | ✅ (if paper/* changed) | ❌ | ✅ | ❌ | ✅ |

## Running Tests Locally

Before pushing, run tests locally to catch issues early:

```bash
# Run tests for a specific phase
cd phase1
pytest --cov=src --cov-report=term -v

# Run only fast tests (skip integration)
pytest -m "not slow"

# Run with coverage threshold check
pytest --cov=src --cov-report=term --cov-fail-under=50

# Run linting
ruff check phase1 phase2 phase3
ruff format phase1 phase2 phase3

# Run type checking
cd phase2 && mypy src --ignore-missing-imports
```

## CI Status Badges

Add these to your README.md to show CI status:

```markdown
![Tests](https://github.com/originaxiom/origin-axiom/workflows/All%20Tests/badge.svg)
![Lint](https://github.com/originaxiom/origin-axiom/workflows/Lint/badge.svg)
[![codecov](https://codecov.io/gh/originaxiom/origin-axiom/branch/main/graph/badge.svg)](https://codecov.io/gh/originaxiom/origin-axiom)
```

## Understanding Test Failures

### When a test fails in CI:

1. **Check the workflow run:** Click on the failing check in your PR
2. **View the job logs:** Expand the failing job to see detailed output
3. **Reproduce locally:**
   ```bash
   cd phase2
   pytest tests/test_mode_model.py::TestModeSumInputs::test_basic_validation -v
   ```
4. **Fix and push:** Make changes, run tests locally, push fix

### Common failure causes:

- **Import errors:** Missing dependencies in pyproject.toml
- **Coverage threshold:** Tests pass but coverage < 50%
- **Python version differences:** Code works on 3.11 but not 3.10
- **Path issues:** Tests work locally but fail in CI (check absolute paths)

## Coverage Reporting

Coverage reports are uploaded to Codecov for Python 3.11 runs:

- **View coverage:** https://codecov.io/gh/originaxiom/origin-axiom
- **Per-phase coverage:** Available with flags (phase1, phase2, phase3)
- **Coverage threshold:** Currently set to 50%, will increase over time

## Workflow Configuration

### Modifying workflows:

1. Edit `.yml` files in this directory
2. Test changes on a feature branch first
3. Validate YAML syntax: https://www.yamllint.com/
4. Monitor first run after changes

### Adding new phases:

When adding phase4 tests:

1. Copy `test-phase3.yml` to `test-phase4.yml`
2. Replace all `phase3` with `phase4`
3. Update `test-all.yml` matrix to include phase4

### Adjusting coverage thresholds:

As test coverage improves, increase thresholds:

```yaml
- name: Check coverage threshold
  run: |
    cd phase2
    coverage report --fail-under=60  # Increase from 50 to 60
```

## Performance Optimization

### Caching

Workflows use pip caching to speed up dependency installation:

```yaml
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
    cache: 'pip'  # Caches pip packages
```

### Selective testing

Phase-specific workflows only run when relevant files change:

```yaml
on:
  push:
    paths:
      - 'phase2/**'  # Only run if phase2 files changed
```

### Parallel execution

`test-all.yml` uses matrix strategy to run phases in parallel:

```yaml
strategy:
  matrix:
    phase: ['phase1', 'phase2', 'phase3']
```

## Cost Management

GitHub Actions free tier provides:
- **2,000 minutes/month** for public repos
- **Unlimited** for public repositories (as of 2024)

Expected usage:
- **Per PR:** ~10-20 minutes (phase tests + lint + build)
- **Nightly:** ~20-30 minutes (integration tests + gates)
- **Monthly:** ~1,000-1,500 minutes (well within free tier)

To reduce usage:
- Use `paths` filters to skip irrelevant runs
- Mark slow tests with `@pytest.mark.slow` and skip in fast CI
- Run integration tests only nightly

## Troubleshooting

### Workflow not triggering:

- Check branch name matches trigger pattern
- Verify file paths match `paths` filter
- Check if workflow is disabled in Actions tab

### Tests pass locally but fail in CI:

- Check Python version (CI uses 3.10, 3.11, 3.12)
- Verify all dependencies in pyproject.toml
- Check for hardcoded absolute paths
- Ensure deterministic behavior (fixed seeds)

### Coverage upload fails:

- Verify `coverage.xml` is generated
- Check Codecov token (if private repo)
- Ensure codecov action is up to date

## Security

### Secrets management:

Currently no secrets are required. If adding protected operations:

```yaml
- name: Deploy artifacts
  env:
    API_TOKEN: ${{ secrets.API_TOKEN }}
  run: |
    # Use secret here
```

Add secrets in: Settings → Secrets and variables → Actions

### Pull request security:

- Workflows from forks run with limited permissions
- No secrets are exposed to fork PRs
- Manual approval required for first-time contributors

## Maintenance

### Regular updates:

**Quarterly:**
- Update action versions (@v4 → @v5)
- Update Python versions in matrix
- Review and adjust coverage thresholds

**After major changes:**
- Update workflows when adding new phases
- Adjust coverage targets as tests improve
- Add new workflow jobs as needed

### Monitoring:

- Check CI status weekly
- Review failed runs promptly
- Monitor GitHub Actions usage in Insights

## Related Documentation

- **TESTING_ROADMAP.md**: Comprehensive testing strategy
- **IMPLEMENTATION_PLAN.md**: Priority-ordered action items
- **CODE_AUDIT_2026-01.md**: Audit report with testing recommendations

---

**Questions or Issues?**
- CI failing unexpectedly: Check workflow run logs
- Need to add new workflow: Copy existing and modify
- Coverage questions: See TESTING_ROADMAP.md

**End of CI/CD Workflows README**
