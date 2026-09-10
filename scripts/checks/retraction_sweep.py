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
                   # added 2026-09-10 (B1326), same principle as the arcs above: each of these
                   # IS a retraction record for the 83-of-83 family closure -- B1181 the retracted
                   # arc and its addendum, B1235 the arc that retracted it, B1163 the addenda it
                   # corrected, B1326 the sweep's own widening. Quoting the phrase there is right.
                   "frontier/B1181_", "frontier/B1235_", "frontier/B1163_", "frontier/B1326_",
                   "docs/atlas/", "docs/views/")

# A line is a MENTION (allowed) if it carries any of these near the phrase.
MENTION_CUES = re.compile(
    r"retract|corrected|correction|withdraw|formerly|no longer|was wrong|is false|"
    r"scope error|banner|struck|do not bank|must not|never claim|~~|obsolete|\bfalse\b|"
    r"registry|registered here|the phrase|as a general claim|amend|originally|"
    r"27-only|scoped by|partially retracted|read before quoting|"
    # added 2026-09-06 (Review 55): B1188's correction banner reads "... as \"<phrase>.\" **Wrong direction**",
    # a mention the cue list did not recognise once the sweep could finally see the phrase.
    r"wrong direction|described .{0,40} as|"
    # added 2026-09-10 (B1326): a line calling a method orientation-blind is discussing the
    # defect, not asserting the claim -- CAMPAIGN_STATUS names B1181's phrase in exactly that way.
    r"orientation-blind|38/112|38 of 112|"
    # added 2026-09-07 (the doc-currency read at B1296): "refuted" -- the corpus's commonest retraction
    # verb -- was not a cue, so every line that SAYS a phrase is refuted (B1253 FINDINGS: "It is refuted";
    # CAMPAIGN_STATUS: "this arc's own headline REFUTED") read as a live use the moment the phrase was
    # registered. Same E66 shape as the Review-55 widening above: the enforcement narrower than its rule.
    r"refuted", re.I)


def _phrases():
    out = []
    if not os.path.exists(REGISTRY):
        return out
    with open(REGISTRY, encoding="utf-8") as fh:
        for line in fh:
            # FORMAT 1 (the original numbered table):  | 7 | `phrase` | arc | why |
            m = re.match(r"\|\s*\d+\s*\|\s*`([^`]+)`", line)
            if m:
                out.append(m.group(1).strip()); continue
            # FORMAT 2 (used from 2026-08-28 on):  | "phrase" <tail> | arc, date | why |
            # WIDENED 2026-09-06 (Review 55, blocker). The registry grew a second table shape and
            # this parser only knew the first, so it read 9 of 21 rows -- the gate that CERTIFIES
            # retraction discipline was blind to 12 phrases, among them "cell 2 is queued and
            # unrun", live in docs/ERROR_LEDGER.md at the time. Error class E66, inside the
            # instrument the corpus's mechanical greens rest on.
            #
            # THE TAIL IS LOAD-BEARING AND A NAIVE WIDENING IS WRONG. Some rows retract a PHRASE
            # ("excess transitive reach" (of the Omega-DAG...)); others retract only a READING of a
            # phrase that is otherwise perfectly legitimate -- "sin^2 theta_W = 3/8" READ AS
            # selecting E6/the knot. Sweeping the bare number would red ~25 correct uses across
            # README, GOVERNANCE and twelve docs. So: take the phrase only when the tail is EMPTY
            # or a PARENTHETICAL scope note; skip when the tail restricts a reading. A "/"-joined
            # tail carries a second retracted phrase and both are taken.
            m = re.match(r'\|\s*["\u201c]([^"\u201d]+)["\u201d](.*?)\|', line)
            if m:
                phrase, tail = m.group(1).strip(), m.group(2).strip()
                if not tail or tail.startswith("("):
                    out.append(phrase)
                # else: a READING is retracted, not the phrase, and the bare phrase stays
                # legitimate. Two live examples, both of which a naive widening got WRONG here
                # before this comment was written:
                #   * "sin^2 theta_W = 3/8" READ AS selecting E6/the knot -- the NUMBER is fine and
                #     appears correctly in README, GOVERNANCE and twelve docs (~25 uses);
                #   * "the class restricts to c" / eps described as "mirror-odd" -- MIRROR-ODD is a
                #     correct, load-bearing term for the ORIENTATION bit (B1168, B1169); only its
                #     application to eps was retracted.
                # Sweeping either bare phrase reds correct work. When a row retracts a reading, the
                # registry must add a separate row for any phrase it wants swept.
    return out


def _tracked_md():
    """Every tracked prose surface -- .md AND .tex.

    Widened 2026-09-10 (B1326). B1181's retracted "83 of 83" survived in THE PAPER for a week,
    and this sweep could not have caught it even had the phrase been registered: main.tex is
    .tex, and the glob was "*.md" only. A sweep that cannot see the project's flagship document
    is a sweep with a hole the size of the thing it most needs to guard.
    """
    r = subprocess.run(["git", "ls-files", "*.md", "*.tex"], cwd=ROOT,
                       capture_output=True, text=True)
    return [p for p in r.stdout.split("\n") if p.strip()]


def _flatten(line):
    """See through the markup the surface is written in.

    A phrase registered as "all 83 members" does not match "all $83$ members"; the paper reads
    the second. Strip TeX math delimiters and common wrappers, normalise ligatures, collapse
    whitespace -- matching on the flattened line, reporting the real line number.
    """
    for a, b in (("\ufb00", "ff"), ("\ufb01", "fi"), ("\ufb02", "fl"),
                 ("\ufb03", "ffi"), ("\ufb04", "ffl")):
        line = line.replace(a, b)
    line = re.sub(r"\\(?:emph|textbf|textit|mathbf|text|mathrm)\s*\{", "", line)
    line = line.replace("~", " ")          # a TeX tie is a space, not nothing
    line = re.sub(r"[${}]", "", line)
    line = re.sub(r"\s+", " ", line)
    return line


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
                    flat = _flatten(line)
                    mention = MENTION_CUES.search(line) or MENTION_CUES.search(flat)
                    for phrase, rx in phrases:
                        if rx.search(flat) and not mention:
                            violations.append((rel, n, phrase))
        except OSError:
            continue
    return violations


if __name__ == "__main__":
    v = sweep()
    print(f"registered retracted phrases: {len(_phrases())}")
    print(f"tracked .md/.tex files swept: {len(_tracked_md())}")
    print(f"live-claim violations: {len(v)}")
    for rel, n, p in v[:25]:
        print(f"  {rel}:{n}  ->  {p!r}")
