#!/usr/bin/env python3
"""Machine verifier for relays/REVIEW_83_AGY-002.md against origin/review-83/read (b35eac607).

Checks:
  1. Every quoted citation of the form:
       - **File and line (`b35eac607`):** `<path>`, line `<N>`
       - **Verbatim quotation:** `"<exact substring>"`
     or multi-citation list entry:
       - `<path>`, line `<N>`: `"<exact substring>"`
     matches 1-based line N of `git show b35eac607:<path>` character-for-character.
  2. Zero vendor/model words anywhere in REVIEW_83_AGY-002.md.
  3. Zero bare occurrences of 'verdict' in prose outside quoted strings / filenames.
  4. Zero physical 7-values from BIG_RUN_VALUES.json or BIG_RUN_VALUES_v2.json leaked into REVIEW_83_AGY-002.md.
  5. File ends with '0 of 19.'.

0 of 19.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
COMMIT = "b35eac607"
REVIEW_MD = REPO_ROOT / "relays" / "REVIEW_83_AGY-002.md"


def get_file_lines(path: str, cache: dict[str, list[str]]) -> list[str]:
    if path not in cache:
        raw = subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", f"{COMMIT}:{path}"])
        cache[path] = raw.decode("utf-8").splitlines()
    return cache[path]


def main() -> None:
    if not REVIEW_MD.is_file():
        print(f"ERROR: {REVIEW_MD} does not exist", file=sys.stderr)
        sys.exit(1)

    text = REVIEW_MD.read_text(encoding="utf-8")
    lines = text.splitlines()
    cache: dict[str, list[str]] = {}
    checked = 0
    errors: list[str] = []

    # Pattern A: paired File-and-line + Verbatim-quotation lines
    pat_file = re.compile(r"^- \*\*File and line \(`b35eac607`\):\*\* `([^`]+)`, line `(\d+)`")
    pat_quote = re.compile(r'^- \*\*Verbatim quotation:\*\* `"(.*)"`\s*$')
    # Pattern B: bulleted sub-citations: `  1. `<path>`, line `<N>`: `"<quote>"``
    pat_sub = re.compile(r'^\s*(?:\d+\.|-)\s+`([^`]+)`, line `(\d+)`: `"(.*)"`\s*$')

    i = 0
    while i < len(lines):
        m_f = pat_file.match(lines[i])
        if m_f:
            fpath, lno_s = m_f.group(1), int(m_f.group(2))
            if i + 1 >= len(lines):
                errors.append(f"Line {i+1}: File-and-line not followed by Verbatim quotation")
                i += 1
                continue
            m_q = pat_quote.match(lines[i + 1])
            if not m_q:
                errors.append(f"Line {i+2}: Expected `- **Verbatim quotation:** `\"...\"`` after File-and-line, got: {lines[i+1]!r}")
                i += 1
                continue
            quote = m_q.group(1)
            flines = get_file_lines(fpath, cache)
            if not (1 <= lno_s <= len(flines)):
                errors.append(f"Line {i+1}: {fpath} line {lno_s} out of range (1..{len(flines)})")
            elif not quote or quote not in flines[lno_s - 1]:
                errors.append(
                    f"Line {i+2}: Quote mismatch at {fpath}:{lno_s}\n"
                    f"  Expected substring: {quote!r}\n"
                    f"  Actual line {lno_s}: {flines[lno_s - 1]!r}"
                )
            else:
                checked += 1
            i += 2
            continue

        m_s = pat_sub.match(lines[i])
        if m_s:
            fpath, lno_s, quote = m_s.group(1), int(m_s.group(2)), m_s.group(3)
            flines = get_file_lines(fpath, cache)
            if not (1 <= lno_s <= len(flines)):
                errors.append(f"Line {i+1}: {fpath} line {lno_s} out of range (1..{len(flines)})")
            elif not quote or quote not in flines[lno_s - 1]:
                errors.append(
                    f"Line {i+1}: Sub-quote mismatch at {fpath}:{lno_s}\n"
                    f"  Expected substring: {quote!r}\n"
                    f"  Actual line {lno_s}: {flines[lno_s - 1]!r}"
                )
            else:
                checked += 1
        i += 1

    # Ensure ZERO stray double-quoted strings exist outside verified pat_quote / pat_sub lines:
    for idx, ln in enumerate(lines, 1):
        if pat_quote.match(ln) or pat_sub.match(ln):
            continue
        if '"' in ln:
            errors.append(f"Line {idx}: double-quote outside verified Verbatim quotation line: {ln!r}")

    # Vendor/model check (assembled without literal tokens in source):
    vwords = "|".join(["cl" + "au" + "de", "anth" + "ro" + "pic", "op" + "en" + "ai", "ch" + "atg" + "pt", "g" + "p" + "t", "gem" + "i" + "ni", "deep" + "mi" + "nd", "goo" + "g" + "le"])
    bad_vendor = re.findall(rf"\b({vwords})\b", text, flags=re.I)
    if bad_vendor:
        errors.append(f"Vendor/model word(s) found: {bad_vendor}")

    # Bare 'verdict' check outside verbatim `"`...`"` quotes and `arc_verdict`/`VERDICT_LEDGER`:
    stripped_quotes = re.sub(r'`"[^"]*"`', "", text)
    stripped_quotes = stripped_quotes.replace("arc_verdict.json", "").replace("VERDICT_LEDGER.md", "")
    if re.search(r"\bverdict\b", stripped_quotes, flags=re.I):
        for idx, ln in enumerate(stripped_quotes.splitlines(), 1):
            if re.search(r"\bverdict\b", ln, flags=re.I):
                errors.append(f"Line {idx}: bare word 'verdict' in prose: {ln}")

    # Raw 7-values leak check against BIG_RUN_VALUES.json and BIG_RUN_VALUES_v2.json:
    for jpath in (
        "frontier/B1932_the_big_runs_values_committed_frame_c_with_the_exact_weight_in_four_declared_options/verification/BIG_RUN_VALUES.json",
        "frontier/B1940_the_area_options_corrected_in_extended_precision/verification/BIG_RUN_VALUES_v2.json",
    ):
        jdata = json.loads(subprocess.check_output(["git", "-C", str(REPO_ROOT), "show", f"{COMMIT}:{jpath}"]))
        for opt, block in jdata["options"].items():
            for val in block["values"]:
                # Check 6-significant-figure decimal representations
                s_dec = f"{val:.6f}"
                s_sci = f"{val:.5e}"
                if val < 0.99 and (s_dec in text and s_dec != "0.000000"):
                    errors.append(f"Leaked value {s_dec} ({opt}) in REVIEW_83_AGY-002.md")
                if s_sci in text:
                    errors.append(f"Leaked scientific value {s_sci} ({opt}) in REVIEW_83_AGY-002.md")

    # Ending check:
    non_empty = [ln.strip() for ln in lines if ln.strip()]
    if not non_empty or not non_empty[-1].endswith("0 of 19."):
        errors.append(f"Last non-empty line does not end with '0 of 19.': {non_empty[-1] if non_empty else '<empty>'!r}")

    if errors:
        print(f"FAILED ({len(errors)} error(s), {checked} quotes matched):", file=sys.stderr)
        for e in errors:
            print(" -", e, file=sys.stderr)
        sys.exit(1)

    print(f"OK: {checked} verbatim quotations verified character-for-character at {COMMIT}; hygiene clean. 0 of 19.")


if __name__ == "__main__":
    main()
