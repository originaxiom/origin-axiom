"""Public-surface hygiene checks for validation-facing docs."""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_PATHS = [
    ROOT / "README.md",
    ROOT / "CLAIMS.md",
    ROOT / "CHANGELOG.md",
    ROOT / "PROGRESS_LOG.md",
    ROOT / "REPRODUCIBILITY.md",
    ROOT / "docs",
    ROOT / "papers",
]

STALE_REFERENCES = [
    "OUTREACH_KIT",
    "EXTERNAL_REVIEW_INDEX",
    "REVIEW_RESPONSE_LEDGER",
    "REVIEW_WORKFLOW",
    "EXTERNAL_REVIEW_BRIEF",
    "REVIEWER_GUIDE",
    "reviewer-001",
]

RAW_TRANSCRIPT_MARKERS = [
    "Claude responded:",
    "You said:",
    "/remote-control",
    "⏺",
    "❯",
]

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def iter_public_markdown():
    for path in PUBLIC_PATHS:
        if path.is_file():
            yield path
        elif path.is_dir():
            yield from path.rglob("*.md")


def read_public_markdown():
    return {path: path.read_text(encoding="utf-8") for path in iter_public_markdown()}


def test_no_stale_outreach_artifact_references():
    docs = read_public_markdown()
    offenders = []
    for path, text in docs.items():
        for marker in STALE_REFERENCES:
            if marker in text:
                offenders.append(f"{path.relative_to(ROOT)} contains {marker}")
    assert offenders == []


def test_no_email_addresses_or_reviewer_placeholders():
    docs = read_public_markdown()
    offenders = []
    for path, text in docs.items():
        if EMAIL_RE.search(text):
            offenders.append(f"{path.relative_to(ROOT)} contains email-shaped text")
        if "reviewer-" in text:
            offenders.append(f"{path.relative_to(ROOT)} contains reviewer placeholder")
    assert offenders == []


def test_no_raw_transcript_markers_in_public_docs():
    docs = read_public_markdown()
    offenders = []
    for path, text in docs.items():
        for marker in RAW_TRANSCRIPT_MARKERS:
            if marker in text:
                offenders.append(f"{path.relative_to(ROOT)} contains raw transcript marker {marker!r}")
    assert offenders == []
