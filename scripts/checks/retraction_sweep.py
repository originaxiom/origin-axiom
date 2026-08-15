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
# frontier/B967_ is the sweep's OWN arc -- a record ABOUT retractions, so mentions
# there are correct by the same principle as docs/RETRACTIONS.md.
EXEMPT_PREFIXES = ("frontier/B967_", "frontier/B964_", "frontier/B963_", "frontier/B965_", "frontier/B943_",
                   "frontier/B941_", "frontier/B942_", "frontier/B723_", "frontier/B892_",
                   )
# NOTE: "docs/views/" and "docs/atlas/" were exempt until 2026-08-15 and must not be
# re-added. They are DERIVED VIEWS OF LIVE VERDICTS, not retraction records, so
# exempting them hid a retracted phrase sitting unbannered in VERDICT_LEDGER.md.

# A line is a MENTION (allowed) if it carries any of these near the phrase.
CUE_WINDOW = 300   # chars either side of the phrase in which a mention cue counts

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
    """Every tracked text artifact a retracted claim can live in.

    WAS: git ls-files "*.md" only. That left ALL 25 tracked .tex files outside the
    fence -- including papers/structure_paper/arxiv/main.tex, the paper this gate
    exists to protect -- and every arc_verdict.json. A retraction gate blind to the
    manuscript is not a gate. Widened 2026-08-15 after an inventory agent found the
    hole; the sweep's previous "0 violations" was reported over an incomplete corpus
    and should not have been quoted as clean.
    """
    pats = ["*.md", "*.tex", "*.json"]
    out = []
    for pat in pats:
        r = subprocess.run(["git", "ls-files", pat], cwd=ROOT,
                           capture_output=True, text=True)
        out += [p for p in r.stdout.split("\n") if p.strip()]
    return sorted(set(out))


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
                        m = rx.search(line)
                        if not m:
                            continue
                        # The cue must be NEAR the phrase. Matching it anywhere on the
                        # line made the fence decorative on exactly the longest,
                        # most claim-dense rows: VERDICT_LEDGER row B997 carries the
                        # retracted "whole exceptional series" AND, ~2000 characters
                        # away, an unrelated "must not be quoted as one" -- which
                        # suppressed the hit.
                        lo = max(0, m.start() - CUE_WINDOW)
                        hi = min(len(line), m.end() + CUE_WINDOW)
                        if not MENTION_CUES.search(line[lo:hi]):
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
