#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$root"

ts="$(date '+%Y-%m-%d %H:%M:%S %z')"
git_hash="$(git rev-parse --short HEAD 2>/dev/null || echo 'UNKNOWN')"
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || echo 'UNKNOWN')"

phase="phase2"
report="$root/$phase/AUDIT_REPORT.md"

if [ ! -d "$root/$phase" ]; then
  echo "ERROR: $phase/ does not exist at repo root: $root"
  exit 1
fi

mkdir -p "$root/$phase"

h1 () { printf -- "\n# %s\n" "$1"; }
h2 () { printf -- "\n## %s\n" "$1"; }
code () { printf -- "\n\`\`\`%s\n%s\n\`\`\`\n" "${1:-}" "${2:-}"; }

{
  h1 "Phase 2 Structural Audit (P2-A1)"
  printf -- "\n- Generated: %s\n- Git: %s (%s)\n- Repo: %s\n" "$ts" "$git_hash" "$branch" "$root"

  h2 "1) High-level inventory"
  code "" "$(ls -la "$root/$phase" 2>&1 || true)"

  h2 "2) Presence checks (non-fatal)"
  for f in README.md SCOPE.md CLAIMS.md ASSUMPTIONS.md REPRODUCIBILITY.md PROGRESS_LOG.md pyproject.toml; do
    if [ -f "$root/$phase/$f" ]; then
      printf -- "- OK: %s/%s\n" "$phase" "$f"
    else
      printf -- "- MISSING: %s/%s\n" "$phase" "$f"
    fi
  done

  h2 "3) Directory tree (depth 4)"
  if command -v tree >/dev/null 2>&1; then
    code "" "$(tree -a -L 4 "$root/$phase" 2>&1 || true)"
  else
    code "" "$(find "$root/$phase" -maxdepth 4 -print 2>&1 || true)"
  fi

  h2 "4) TODO / FIXME / XXX / TBD sweep"
  code "" "$(rg -n 'TODO|FIXME|XXX|TBD' "$root/$phase" -S 2>&1 || echo 'No matches.')"

  paper_dir="$root/$phase/paper"
  h2 "5) Paper build + structure"
  if [ -d "$paper_dir" ]; then
    printf -- "\n### 5.1 Paper directory listing\n"
    code "" "$(ls -la "$paper_dir" 2>&1 || true)"

    if [ -f "$paper_dir/main.tex" ]; then
      printf -- "\n### 5.2 main.tex spine (inputs/includes)\n"
      code "" "$(rg -n '^[^%]*(\\input\\{|\\include\\{|\\subfile\\{)' "$paper_dir/main.tex" 2>/dev/null || echo 'No inputs/includes found (or different structure).')"

      printf -- "\n### 5.3 Labels / refs / cites quick stats\n"
      code "" "$(
        echo "labels:"; rg -n -F '\label{' "$paper_dir" -S | wc -l | tr -d ' '
        echo "refs:";   rg -n -F '\ref{'   "$paper_dir" -S | wc -l | tr -d ' '
        echo "cites:";  rg -n -F '\cite{'  "$paper_dir" -S | wc -l | tr -d ' '
      )"

      printf -- "\n### 5.4 Build attempt (latexmk) + hygiene checks\n"
      ( cd "$paper_dir" && latexmk -C main.tex >/dev/null 2>&1 || true )

      build_out="$( (cd "$paper_dir" && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex) 2>&1 || true )"
      code "" "$build_out"

      pat='undefined references|Citation .*undefined|Warning--empty journal|LaTeX Error|!  Undefined control sequence'
      log_hit=0
      for f in "$paper_dir/main.log" "$paper_dir/main.blg"; do
        if [ -f "$f" ]; then
          hits="$(rg -n "$pat" "$f" 2>/dev/null || true)"
          if [ -n "$hits" ]; then
            log_hit=1
            printf -- "\nMatches in %s:\n" "$(basename "$f")"
            code "" "$hits"
          fi
        fi
      done

      if [ "$log_hit" -eq 0 ]; then
        printf -- "\nResult: OK (no hygiene-pattern hits)\n"
      else
        printf -- "\nResult: NOT clean (see matches above)\n"
      fi
    else
      printf -- "\nPaper exists but main.tex is missing at: %s\n" "$paper_dir/main.tex"
    fi
  else
    printf -- "\nNo paper directory at: %s\n" "$paper_dir"
  fi

  h2 "6) Claims discipline scan (generic)"
  code "" "$(rg -n 'claims-to-artifacts|artifact|provenance|non-claims|falsif|reproduc' "$root/$phase" -S 2>&1 || echo 'No matches.')"

  h2 "7) Git status snapshot (informational)"
  code "" "$(git status --porcelain=v1 2>&1 || true)"

  h2 "8) Next recommended Phase 2 rungs (after audit)"
  printf -- "\n- P2-S1: Define Phase 2 paper spine + section contract (order, naming, invariants)\n"
  printf -- "- P2-S2: Claims map hardening (CLAIMS.md -> paper table -> artifact paths)\n"
  printf -- "- P2-S3: Provenance enforcement (git hash, params, seed, environment) in every run artifact\n"
  printf -- "- P2-S4: Rewrite passes (structure first, then math/rigor), zero new claims until audits pass\n"

} > "$report"

echo "Wrote: $report"
