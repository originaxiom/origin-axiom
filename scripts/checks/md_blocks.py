"""md_blocks — exclude a markdown BLOCK, not a markdown LINE.

WHY THIS EXISTS (B1049). Four arcs independently wrote the same idiom: to measure a gap without
counting the rows the measuring arc itself wrote, drop every LINE naming this arc or a later one,
then search what remains. **Prose wraps, and the idiom does not.**

  THE_LADDER, written by B1043:

      - ... **B1032** already corrected the rung to name **two** live routes; **B1043** adds that the
        phi-fixed cluster's own open question (B141 Item 4) was closed by B564 -- which is about the
        `SL(3)` phi-fixed locus, **not** about generations, and changes no rung.

  The AUTHOR token (`B1043`) is on line 1; the CITATION (`B141`) is on line 2. A per-line filter
  drops line 1 and keeps line 2, so **B141 reads as curated by nobody**. B1037's band count fell
  37 -> 36 and its lock went RED -- and stayed red for five arcs, because gates do not cover locks
  and the full suite is 48 minutes. B1031 and B1032 carry the identical defect and are green only
  because neither of them happens to count B141.

THE RULE THIS ENCODES: an exclusion by authorship is a statement about a BLOCK of prose -- a bullet
and its continuation lines, a table row, a paragraph. Filtering by line is filtering by an artifact
of the text width.

DECLARED SHARING, not shadow sharing. B1035 found 227 frontier files doing `sys.path` surgery into
two arcs that had become infrastructure while still filed as research. This module is the opposite:
it lives in `scripts/checks/` with the other instruments, it is imported by name, and its consumers
are listed here -- B1031, B1032, B1037, B1048.
"""
import re

_BLOCK_START = re.compile(r"^([-*+]\s|\d+\.\s)")


def blocks(text):
    """[(joined_text, [lines])] — a bullet plus its wrapped continuation, a table row, a heading,
    a blank line, or a paragraph. Every input line appears in exactly one block, in order."""
    out, cur = [], []

    def flush():
        if cur:
            out.append(("\n".join(cur), list(cur)))
            cur.clear()

    for ln in text.splitlines():
        s = ln.strip()
        if (not s) or s.startswith(("#", "|", ">")) or _BLOCK_START.match(s):
            flush()
            cur.append(ln)
            if (not s) or s.startswith(("#", "|")):
                flush()          # headings, table rows and blanks are one-line blocks
        else:
            cur.append(ln)
    flush()
    return out


def drop_blocks(text, rx):
    """`text` with every block matching `rx` removed. The line-level equivalent is what B1049
    found broken; use this instead."""
    return "\n".join(ln for txt, lns in blocks(text) if not rx.search(txt) for ln in lns)


def drop_blocks_from(paths, rx, read):
    """Convenience for the CURATED-blob shape all four consumers use."""
    return "\n".join(drop_blocks(read(p), rx) for p in paths)
