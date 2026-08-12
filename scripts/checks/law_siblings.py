"""law-siblings — a restored law must not leave a same-law arc in debt in another band.

B1043's defect: B1039 restored B141's Item 4 as an OPEN conjecture while B564 had CLOSED it, by
the very route B141 named. B564 sits four bands away and B141 carries no forward pointer, so
reading the in-band bodies -- campaign step 1, done correctly -- could not reach it. The band
sweep groups arcs by BANKING DATE; a law is a statement about WHAT AN ARC SAYS.

The fix is a TOPIC search per restoration, run mechanically instead of remembered. Following the
repo's own posture for this shape (B821/B823, the blind-arc gate): candidates are TRIAGED, not
capped, and the gate fails only on UNTRIAGED ones -- it asks for a judgement, not a number. A
hard-fail on every candidate would fire on right answers and train readers to ignore it (E34's
recorded reason for leaving that class ungated).

  sweep()  -> [(law, arc, why)] for candidates with no row in docs/consolidation/LAW_SIBLINGS.md
"""
import glob
import json
import os
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
LAW_MAP = ROOT / "docs" / "LAW_MAP.md"
REGISTRY = ROOT / "docs" / "consolidation" / "LAW_SIBLINGS.md"
CURATED = ["docs/LAW_MAP.md", "docs/THE_FRAMEWORK.md", "docs/THEOREM_LEDGER.md", "CLAIMS.md",
           "docs/THE_LADDER.md"]

# Topic fingerprints, one per restored law. Hand-authored ON PURPOSE and kept beside the gate:
# an auto-extracted fingerprint would drift with the prose and silently stop matching, which is
# the failure mode this instrument exists to prevent. Adding a restoration adds a row here.
FINGERPRINTS = {
    "the tower (B1038)":
        r"\brho_n\b|ρ_n|Sym\^n|two-sequence|trace-map Jacobian|stabilization recursion",
    "phi-fixed reducibility (B1039)":
        r"phi-fixed|φ-fixed|\bQ8\b|quaternion group|reducible tower|finiteness versus density",
    "the metallic exponent (B1039)":
        r"degree=rank|\[A,B\]\s*=\s*[+-]?\s*mu|meridian|metallic exponent|order-determined",
    # WIDENED B1045, on the instrument's first use against a new band. B485 states the SAME
    # polynomial as B1040's metallic degree -- Delta_m(a) = a^2-(m^2+2)a+1 is the char poly of
    # M_m^2, whose root is lambda_m^2 -- in ALEXANDER-POLYNOMIAL language, and NO fingerprint
    # reached it. A fingerprint catches restatements in the SAME vocabulary; a genuine TRANSLATION
    # between vocabularies escapes it. That limitation is real and is stated in the registry.
    "isomonodromy (B1040)":
        r"isomonodrom|Painlev|Schlesinger|Vieta|Jimbo|Fricke cubic"
        r"|dynamical degree|lambda_m\^?2|λ_m|Alexander law|m\^2\s*\+\s*2|metallic degree",
    # ADDED B1047. The occasion is the coverage measurement below, not a new restoration: B1029's
    # row was already on LAW_MAP and had NO fingerprint, so the first independent cluster this
    # instrument was pointed at belonged to a law it could not see.
    "the seam is the ends' class field (B1029)":
        r"Hilbert class field|class field|genus field|sqrt\(?-15\)?|√−15|√-15"
        r"|Q\(sqrt-15\)|ℚ\(√−15\)|reduced forms|prime discriminant",
    # ADDED B1047, for the law B1047 itself restores -- the instrument's own standing rule that
    # "adding a restoration adds a row here", applied to the arc that added the rule's first
    # independent use.
    "the seam's darkness is termwise (B1047)":
        r"termwise|s-dark|seam-dark|product strata|full-field product|doubly-elliptic"
        r"|annihilat|s-orthogonal",
}


def _arcs():
    out, seen = {}, set()
    for d in sorted(glob.glob(str(ROOT / "frontier" / "B*"))):
        m = re.match(r"B(\d+)_", os.path.basename(d))
        p = pathlib.Path(d) / "arc_verdict.json"
        if not m or not p.is_file():
            continue
        b = "B" + m.group(1)
        if b in seen:
            continue
        seen.add(b)
        try:
            out[b] = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
    return out


# A row that REGISTERS a sibling is not a row that CONSOLIDATES it. B1043's LAW_MAP row names all
# eight candidates it found; counting those as citations made this sweeper report ZERO on its
# first run -- E37 (self-measurement) inside the instrument built to prevent E37's cousin. Rows
# that exist to record the debt are excluded at construction, which is E37's own standing rule.
# Excluded by PURPOSE, not by mention. A LAW_MAP row is ONE LINE, so dropping every line that
# names the registrar also drops that row's real citations -- which happened on the first
# attempt and made B117/B122/B121/B118 read as uncited. Only the dedicated registry ROWS
# (identified by their headline) and the registry file are excluded.
_REGISTRY_ROW = re.compile(r"THE BAND IS THE WRONG UNIT|LAW SIBLINGS —|law-siblings\b.*gate")
# Arcs that AUTHOR this instrument discuss every law by name and match every fingerprint.
REGISTRARS = {"B1043", "B1044"}


def _curated_blob():
    out = []
    for p in CURATED:
        f = ROOT / p
        if f.is_file():
            out.append("\n".join(ln for ln in f.read_text(encoding="utf-8").splitlines()
                                 if not _REGISTRY_ROW.search(ln)))
    return "\n".join(out)


def candidates():
    """Every PROVED, non-instrument arc matching a restored law's fingerprint and cited on no
    curated surface. These are the arcs a band-wise sweep structurally cannot see."""
    arcs = _arcs()
    blob = _curated_blob()

    def cited(b):
        return bool(re.search(rf"\b{b}\b", blob) or re.search(rf"frontier/{b}_", blob))

    out = []
    for law, pat in FINGERPRINTS.items():
        rx = re.compile(pat, re.I)
        for b, d in sorted(arcs.items(), key=lambda kv: int(kv[0][1:])):
            if b in REGISTRARS:
                continue
            if d.get("verdict") != "PROVED" or d.get("instrument"):
                continue
            if cited(b):
                continue
            claim = d.get("claim_one_line") or ""
            if rx.search(claim):
                out.append((law, b, claim[:110]))
    return out


def triaged():
    if not REGISTRY.is_file():
        return set()
    rows = set()
    for ln in REGISTRY.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\|\s*`?(B\d+)`?\s*\|", ln.strip())
        if m:
            rows.add(m.group(1))
    return rows


def sweep():
    """Untriaged candidates -- the gate's failure set."""
    done = triaged()
    return [(law, b, why) for law, b, why in candidates() if b not in done]


if __name__ == "__main__":
    cs, miss = candidates(), sweep()
    print("law-siblings: %d candidate(s) across %d laws; %d untriaged"
          % (len(cs), len(FINGERPRINTS), len(miss)))
    for law, b, why in cs:
        mark = "UNTRIAGED" if any(b == m[1] for m in miss) else "triaged  "
        print("  [%s] %-32s %-6s %s" % (mark, law, b, why))
