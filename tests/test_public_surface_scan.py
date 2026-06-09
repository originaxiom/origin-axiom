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


# --- no per-chat / model AI labels in the living/governing docs (generic "AI-assisted" phrasing IS allowed) ---
# Scoped to the cleaned set; the historical backlog (append-only PROGRESS_LOG/CHANGELOG, papers ledger, older
# FINDINGS) carries legacy attributions and is a separate scheduled scrub — when done, widen this list.
LIVING_DOC_FILES = [ROOT / "REPRODUCIBILITY.md", ROOT / "docs" / "STRATEGIC_SYNTHESIS.md",
                    ROOT / "docs" / "OPEN_LEADS.md"]
LIVING_DOC_DIRS = [ROOT / "knowledge",
                   ROOT / "frontier" / "B143_interaction_feasibility",
                   ROOT / "frontier" / "B144_interaction_chirality",
                   ROOT / "frontier" / "B145_forced_chirality",
                   ROOT / "frontier" / "B146_b145_calibration"]

# Forbidden specific labels (NOT generic "AI assistant"/"AI-assisted", which are fine).
AI_LABEL_RE = re.compile(r"Chat[- ]?[12]\b|3-?chat|3-?voice|three[- ]voice|three independent runs|Opus 4|Claude",
                         re.IGNORECASE)


def _iter_living_docs():
    for f in LIVING_DOC_FILES:
        if f.is_file():
            yield f
    for d in LIVING_DOC_DIRS:
        if d.is_dir():
            for pat in ("*.md", "*.py"):
                yield from d.rglob(pat)


def test_no_ai_labels_in_living_docs():
    offenders = []
    for path in _iter_living_docs():
        m = AI_LABEL_RE.search(path.read_text(encoding="utf-8"))
        if m:
            offenders.append(f"{path.relative_to(ROOT)} contains AI label {m.group(0)!r}")
    assert offenders == [], offenders
