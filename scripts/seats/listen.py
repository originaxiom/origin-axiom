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


def git(*args, cwd=None):
    r = subprocess.run(["git", *args], capture_output=True, text=True, cwd=cwd)
    return r.returncode, r.stdout.strip(), r.stderr.strip()


def memory(cwd):
    rc, out, _ = git("rev-parse", "--absolute-git-dir", cwd=cwd)
    if rc != 0:
        return None
    d = pathlib.Path(out) / "oa_seat_listener"
    d.mkdir(exist_ok=True)
    return d


def messages(page):
    """the page's messages of main, as {number: text}: each runs from its '### M<n>' line to the next heading of its level or above"""
    found = {}
    heads = list(MESSAGE.finditer(page))
    for k, m in enumerate(heads):
        end = heads[k + 1].start() if k + 1 < len(heads) else len(page)
        nxt = re.search(r"^#{1,2} ", page[m.end():end], re.M)
        body = page[m.start():(m.end() + nxt.start()) if nxt else end]
        found[int(m.group(1))] = body.rstrip() + "\n"
    return found


def look_seat(seat, cwd, remote, peek):
    """(status, text): 0 and the unread messages, 3 and nothing, or 2 and why it could not look"""
    mem = memory(cwd)
    if mem is None:
        return 2, "there is no git repository here"
    rc, _, err = git("fetch", "--quiet", remote, "main", cwd=cwd)
    if rc != 0:
        return 2, "the fetch of main failed" + (": " + err.splitlines()[-1] if err else "")
    path = "docs/seats/%s.md" % seat
    rc, blob, _ = git("rev-parse", "%s/main:%s" % (remote, path), cwd=cwd)
    if rc != 0:
        return 2, "main has no page %s" % path
    state_file = mem / ("%s.json" % seat)
    state = json.loads(state_file.read_text(encoding="utf-8")) if state_file.is_file() else {"blob": None, "read": 0}
    if state["blob"] == blob:
        return 3, ""
    rc, page, _ = git("show", "%s/main:%s" % (remote, path), cwd=cwd)
    ms = messages(page)
    new = {n: t for n, t in ms.items() if n > state["read"]}
    rc, head, _ = git("rev-parse", "--short=9", "%s/main" % remote, cwd=cwd)
    out = ["YOUR PAGE ON MAIN HAS CHANGED (%s, main at %s)." % (path, head)]
    if new:
        out.append("Messages of main you have not read: %s. Newest first:\n" % ", ".join("M%d" % n for n in sorted(new)))
        out += [new[n] for n in sorted(new, reverse=True)]
    else:
        out.append("No new message: main changed the page elsewhere (your cards, or what it waits for). Read the page.")
    if not peek:
        state_file.write_text(json.dumps({"blob": blob, "read": max([state["read"]] + list(ms))}), encoding="utf-8")
    return 0, "\n".join(out)


def look_main(cwd, remote, peek):
    mem = memory(cwd)
    if mem is None:
        return 2, "there is no git repository here"
    rc, _, err = git("fetch", "--quiet", "--prune", remote, cwd=cwd)
    if rc != 0:
        return 2, "the fetch failed: " + (err.splitlines()[-1] if err else "")
    rc, out, _ = git("for-each-ref", "--format=%(refname:short) %(objectname:short=9)", "refs/remotes/%s" % remote, cwd=cwd)
    heads = {}
    for line in out.splitlines():
        name, sha = line.split()
        if name not in ("%s/main" % remote, "%s/HEAD" % remote, remote):
            heads[name] = sha
    state_file = mem / "main.json"
    first = not state_file.is_file()
    old = json.loads(state_file.read_text(encoding="utf-8")) if not first else {}
    moved = ["%s  %s -> %s" % (n, old.get(n, "(new)"), s) for n, s in sorted(heads.items()) if old.get(n) != s]
    gone = ["%s  %s -> (gone)" % (n, s) for n, s in sorted(old.items()) if n not in heads]
    if not peek:
        state_file.write_text(json.dumps(heads), encoding="utf-8")
    if first or not (moved or gone):
        return 3, ""
    return 0, "SEATS' BRANCHES HAVE MOVED (names and commits only; read each as its lane is read):\n" + "\n".join("  " + x for x in moved + gone)


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
        status, text = look_main(a.repo, a.remote, a.peek) if a.main else look_seat(a.seat, a.repo, a.remote, a.peek)
        if status == 0:
            print(text, flush=True)
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
