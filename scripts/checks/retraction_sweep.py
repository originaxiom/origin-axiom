#!/usr/bin/env python3
"""L139 — the retraction sweep.

Retracting a claim does not retract its instances (B965: a retracted error survived
one hour in a row written the same day). This sweeps every tracked .md file for
registered retracted phrases used as LIVE CLAIMS, while allowing them as MENTIONS
inside retraction records, correction banners, quotations of former claims, and the
tests that enforce their absence.

Usage:  python3 scripts/checks/retraction_sweep.py            (report)
        imported by scripts/gates/gates.py as the `retraction-sweep` gate
"""
import os
import re
import subprocess

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
REGISTRY = os.path.join(ROOT, "docs", "RETRACTED_PHRASES.md")

# Files that ARE the retraction record: mentions there are correct, not violations.
EXEMPT_FILES = {
    "docs/RETRACTED_PHRASES.md",
    "docs/RETRACTIONS.md",
    "CHANGELOG.md",
    "PROGRESS_LOG.md",
    "docs/progress/REVIEWS.md",
}
EXEMPT_BASENAMES = ("PRIOR_ART_HYPERCHARGE.md", "PRIOR_ART_MAASS.md",
                    "PRIOR_ART_VEV.md", "PRIOR_ART_RANK_REDUCTION.md",
                    "O3_PRIOR_ART.md", "DRAFT_FINDINGS.md")
EXEMPT_PREFIXES = ("frontier/B964_", "frontier/B963_", "frontier/B965_", "frontier/B943_",
                   "frontier/B941_", "frontier/B942_", "frontier/B723_", "frontier/B892_",
                   "docs/atlas/", "docs/views/")

# A line is a MENTION (allowed) if it carries any of these near the phrase.
MENTION_CUES = re.compile(
    r"retract|corrected|correction|withdraw|formerly|no longer|was wrong|is false|"
    r"scope error|banner|struck|do not bank|must not|never claim|~~|obsolete|\bfalse\b|"
    r"registry|registered here|the phrase|as a general claim|amend|originally|"
    r"27-only|scoped by|partially retracted|read before quoting", re.I)


def _phrases():
    out = []
    if not os.path.exists(REGISTRY):
        return out
    with open(REGISTRY, encoding="utf-8") as fh:
        for line in fh:
            m = re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`", line)
            if m:
                out.append(m.group(1).strip())
    return out


def _tracked_md():
    r = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT,
                       capture_output=True, text=True)
    return [p for p in r.stdout.split("\n") if p.strip()]


def sweep():
    phrases = [(p, re.compile(re.escape(p), re.I)) for p in _phrases()]
    violations = []
    if not phrases:
        return violations
    for rel in _tracked_md():
        if (rel in EXEMPT_FILES or rel.startswith(EXEMPT_PREFIXES)
                or os.path.basename(rel) in EXEMPT_BASENAMES):
            continue
        path = os.path.join(ROOT, rel)
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                for n, line in enumerate(fh, 1):
                    for phrase, rx in phrases:
                        if rx.search(line) and not MENTION_CUES.search(line):
                            violations.append((rel, n, phrase))
        except OSError:
            continue
    return violations


if __name__ == "__main__":
    v = sweep()
    print(f"registered retracted phrases: {len(_phrases())}")
    print(f"tracked .md files swept: {len(_tracked_md())}")
    print(f"live-claim violations: {len(v)}")
    for rel, n, p in v[:25]:
        print(f"  {rel}:{n}  ->  {p!r}")
