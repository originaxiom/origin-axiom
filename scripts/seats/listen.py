#!/usr/bin/env python3
"""The listener: how a seat hears main, and how main hears the seats, with nobody relaying by hand.

A SEAT runs, in its own clone and in the background:

    python3 scripts/seats/listen.py --seat chat1

Every ten minutes it fetches main and looks at one file, the seat's page docs/seats/<seat>.md.  While the page is as the
seat last read it, the listener says nothing and waits.  When the page has changed it prints the messages of main that the
seat has not read, remembers that it showed them, and exits with status 0: the seat's session is woken, reads, acts, and
starts the listener again.

MAIN runs:

    python3 scripts/seats/listen.py --main

It fetches every branch and exits when one that is not main has moved, appeared or gone, printing the names and the
commits and nothing of what the branches hold: some lanes are read only through a mask.

    --once        look once: status 0 if there is something new, 3 if there is not
    --interval N  seconds between looks (600 unless given)
    --peek        show what is new and do not remember having shown it

WHAT IT NEVER DOES: change a file of the working tree, move HEAD, merge, or push.  It fetches, and it keeps its memory in
the git directory, which is not tracked (oa_seat_listener/).

Status: 0 something new, shown; 2 it could not look (no repository, no such page, the fetch failed three times running);
3 nothing new (--once only).
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import time

MESSAGE = re.compile(r"^### M(\d+)\b.*$", re.M)


GIT_SECONDS = 180          # a fetch that stalls is a failure to look, not a silence (Review 79: the call had no time limit)


def git(*args, cwd=None):
    try:
        r = subprocess.run(["git", *args], capture_output=True, text=True, cwd=cwd, timeout=GIT_SECONDS)
    except subprocess.TimeoutExpired:
        return 124, "", "git %s did not answer within %d seconds" % (args[0] if args else "", GIT_SECONDS)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def recall(state_file, empty):
    """the listener's memory of one page or of the branches; (state, None), or (None, why) when the file is there and cannot be
    read (Review 79: a damaged file crashed the listener, where it should say that it could not look)"""
    if not state_file.is_file():
        return dict(empty), None
    try:
        s = json.loads(state_file.read_text(encoding="utf-8"))
        if not isinstance(s, dict):
            raise ValueError("not a table")
        return s, None
    except (OSError, ValueError) as ex:
        return None, "the listener's memory cannot be read (%s): %s. Remove it to start again from nothing" % (state_file, ex)


def memory(cwd):
    rc, out, _ = git("rev-parse", "--absolute-git-dir", cwd=cwd)
    if rc != 0:
        return None
    d = pathlib.Path(out) / "oa_seat_listener"
    d.mkdir(exist_ok=True)
    return d


def _fenced(page):
    """the spans of the page that lie inside a fenced block, where a line that begins with # is not a heading"""
    # CORRECTED 2026-11-12 (Review 79's second round; found by a reading on another family of model).  Any line that began
    # with three backticks or three tildes used to open or close a block.  So a block fenced with tildes that quoted one
    # fenced with backticks was closed early, and a line of prose that began with a span of code in three backticks opened a
    # block that never closed: every older message below it was dropped without a word.  A block now opens on a line that is a
    # fence and nothing else but its label (a backtick fence's label holds no backtick), and closes on a fence of the same
    # character, at least as long, with nothing after it.
    spans, start, char, size, at = [], None, None, 0, 0
    for line in page.split("\n"):
        m = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if m:
            fence, rest = m.group(1), m.group(2)
            if start is None:
                if not (fence[0] == "`" and "`" in rest):
                    start, char, size = at, fence[0], len(fence)
            elif fence[0] == char and len(fence) >= size and not rest.strip():
                spans.append((start, at + len(line))); start = None
        at += len(line) + 1
    if start is not None:
        spans.append((start, len(page)))
    return spans


def messages(page):
    """the page's messages of main, as {number: text}: each runs from its '### M<n>' line to the next heading of its level or
    above.  A line inside a fenced block is never a heading (Review 79: a '# comment' in a block of code cut a message short)."""
    fenced = _fenced(page)
    outside = lambda pos: not any(a <= pos < b for a, b in fenced)
    found = {}
    heads = [m for m in MESSAGE.finditer(page) if outside(m.start())]
    for k, m in enumerate(heads):
        end = heads[k + 1].start() if k + 1 < len(heads) else len(page)
        nxt = next((x for x in re.finditer(r"^#{1,2} ", page[m.end():end], re.M) if outside(m.end() + x.start())), None)
        body = page[m.start():(m.end() + nxt.start()) if nxt else end]
        found[int(m.group(1))] = body.rstrip() + "\n"
    return found


def _sum(text):
    import hashlib
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def look_seat(seat, cwd, remote, peek):
    """(status, text, remember): 0 and the unread messages, 3 and nothing, or 2 and why it could not look.

    `remember` is what stores the page as read.  The caller calls it AFTER the text has been printed, and not before
    (corrected 2026-11-12, Review 79: the page was stored as read before anything was shown, so a print that failed lost
    the message for good; and a page that could not be read was taken for an empty one and stored as read)."""
    mem = memory(cwd)
    if mem is None:
        return 2, "there is no git repository here", None
    rc, _, err = git("fetch", "--quiet", remote, "main", cwd=cwd)
    if rc != 0:
        return 2, "the fetch of main failed" + (": " + err.splitlines()[-1] if err else ""), None
    path = "docs/seats/%s.md" % seat
    rc, blob, _ = git("rev-parse", "%s/main:%s" % (remote, path), cwd=cwd)
    if rc != 0:
        return 2, "main has no page %s" % path, None
    state_file = mem / ("%s.json" % seat)
    state, why = recall(state_file, {"blob": None, "read": 0})
    if state is None:
        return 2, why, None
    if state.get("blob") == blob:
        return 3, "", None
    rc, page, err = git("show", "%s/main:%s" % (remote, path), cwd=cwd)
    if rc != 0:
        return 2, "main's page %s could not be read" % path + (": " + err.splitlines()[-1] if err else ""), None
    ms = messages(page)
    read, sums = int(state.get("read", 0)), state.get("sums") or {}
    new = {n: t for n, t in ms.items() if n > read}
    # a message already read whose text has changed since is shown again (Review 79: an amendment in place was never shown)
    amended = {n: t for n, t in ms.items() if n <= read and str(n) in sums and sums[str(n)] != _sum(t)}
    rc, head, _ = git("rev-parse", "--short=9", "%s/main" % remote, cwd=cwd)
    out = ["YOUR PAGE ON MAIN HAS CHANGED (%s, main at %s)." % (path, head)]
    if new:
        out.append("Messages of main you have not read: %s. Newest first:\n" % ", ".join("M%d" % n for n in sorted(new)))
        out += [new[n] for n in sorted(new, reverse=True)]
    if amended:
        out.append("Messages you had read that main has CHANGED since: %s. As they stand now:\n" % ", ".join("M%d" % n for n in sorted(amended)))
        out += [amended[n] for n in sorted(amended, reverse=True)]
    if not new and not amended and read and not sums:
        # CORRECTED 2026-11-12 (Review 79's second round): a memory written before this listener kept the messages' text has
        # nothing to compare with.  It used to say "No new message" and then store the new text, so that a message main had
        # changed in place was lost for good.
        out.append("No new message. This listener's memory was written by an older version and holds no record of the text of the "
                   "messages you had read, so it cannot tell whether main has changed one of them: read M1 to M%d on the page again." % read)
    elif not new and not amended:
        out.append("No new message: main changed the page elsewhere (your cards, or what it waits for). Read the page.")
    remembered = json.dumps({"blob": blob, "read": max([read] + list(ms)), "sums": {str(n): _sum(t) for n, t in ms.items()}})
    return 0, "\n".join(out), (None if peek else (lambda: state_file.write_text(remembered, encoding="utf-8")))


def look_main(cwd, remote, peek):
    mem = memory(cwd)
    if mem is None:
        return 2, "there is no git repository here", None
    rc, _, err = git("fetch", "--quiet", "--prune", remote, cwd=cwd)
    if rc != 0:
        return 2, "the fetch failed: " + (err.splitlines()[-1] if err else ""), None
    rc, out, err = git("for-each-ref", "--format=%(refname:short) %(objectname:short=9)", "refs/remotes/%s" % remote, cwd=cwd)
    if rc != 0:
        # CORRECTED 2026-11-12 (Review 79's second round): the answer was read whatever git returned.  When the command timed
        # out the list was empty, every branch was reported as gone, and the memory was emptied.
        return 2, "the branches could not be listed" + (": " + err.splitlines()[-1] if err else " (git returned %d)" % rc), None
    heads = {}
    for line in out.splitlines():
        name, sha = line.split()
        if name not in ("%s/main" % remote, "%s/HEAD" % remote, remote):
            heads[name] = sha
    state_file = mem / "main.json"
    first = not state_file.is_file()
    old, why = recall(state_file, {})
    if old is None:
        return 2, why, None
    moved = ["%s  %s -> %s" % (n, old.get(n, "(new)"), s) for n, s in sorted(heads.items()) if old.get(n) != s]
    gone = ["%s  %s -> (gone)" % (n, s) for n, s in sorted(old.items()) if n not in heads]
    remember = None if peek else (lambda: state_file.write_text(json.dumps(heads), encoding="utf-8"))
    if first and heads:
        # the first look has nothing to compare with.  It used to remember the branches and say nothing, so what a seat had pushed
        # before the listener was first started was never reported (Review 79).  It now shows where every branch is, once.
        return 0, ("FIRST LOOK: nothing to compare with. These branches are on the remote now (names and commits only); what each holds since "
                   "you last read it is yours to check:\n" + "\n".join("  %s  %s" % (n, s) for n, s in sorted(heads.items()))), remember
    if not (moved or gone):
        if remember:
            remember()                      # nothing is shown, so nothing can be lost by storing now
        return 3, "", None
    return 0, "SEATS' BRANCHES HAVE MOVED (names and commits only; read each as its lane is read):\n" + "\n".join("  " + x for x in moved + gone), remember


def main(argv=None):
    ap = argparse.ArgumentParser(description="the listener between main and the seats (see docs/seats/README.md)")
    who = ap.add_mutually_exclusive_group(required=True)
    who.add_argument("--seat", metavar="NAME", help="your seat's name, as your page under docs/seats/ is named")
    who.add_argument("--main", action="store_true", help="main's side: watch every seat's branch")
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--peek", action="store_true")
    ap.add_argument("--interval", type=int, default=600, metavar="SECONDS")
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--repo", default=".", help="the clone to look from (the current folder unless given)")
    a = ap.parse_args(argv)
    if a.seat and not re.fullmatch(r"[a-z0-9][a-z0-9-]*", a.seat):
        print("refused: a seat's name is lower-case letters, digits and hyphens", file=sys.stderr)
        return 2
    failures = 0
    while True:
        status, text, remember = look_main(a.repo, a.remote, a.peek) if a.main else look_seat(a.seat, a.repo, a.remote, a.peek)
        if status == 0:
            print(text, flush=True)
            if remember:
                remember()                  # stored as read only once it has been shown
            return 0
        if status == 2:
            failures += 1
            if a.once or failures >= 3:
                print("the listener could not look: " + text, file=sys.stderr)
                return 2
        else:
            failures = 0
            if a.once:
                return 3
        time.sleep(max(1, a.interval))


if __name__ == "__main__":
    sys.exit(main())
