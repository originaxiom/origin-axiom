"""The push-before-read guard: a manifest is refused until it is committed and its commit is on origin/main, and when its
hash is not the one given, or the working file differs from the commit."""
import hashlib, json, pathlib, subprocess, sys
import pytest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / 'scripts' / 'stepb')); sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from guard import require_pushed_manifest


def git(cwd, *a):
    subprocess.run(["git", "-C", str(cwd), *a], check=True, capture_output=True)


def test_refuses_until_pushed(tmp_path):
    origin = tmp_path / "origin.git"; work = tmp_path / "work"
    subprocess.run(["git", "init", "--bare", "-b", "main", str(origin)], check=True, capture_output=True)
    subprocess.run(["git", "init", "-b", "main", str(work)], check=True, capture_output=True)
    git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t")
    git(work, "remote", "add", "origin", str(origin))
    per = {"a.jsonl.gz": "0" * 64}
    h = hashlib.sha256("".join("%s  %s\n" % (v, n) for n, v in sorted(per.items())).encode()).hexdigest()
    man = work / "MANIFEST.json"; man.write_text(json.dumps({"per_file": per, "sha256_of_the_manifest": h}))
    with pytest.raises(SystemExit):
        require_pushed_manifest(man, h)                     # not committed
    git(work, "add", "MANIFEST.json"); git(work, "commit", "-m", "m")
    (work / "x").write_text("x"); git(work, "add", "x"); git(work, "commit", "-m", "x"); git(work, "push", "origin", "main")
    git(work, "fetch", "origin")
    assert require_pushed_manifest(man, h)["files"] == 1
    with pytest.raises(SystemExit):
        require_pushed_manifest(man, "f" * 64)              # not the hash given
    man.write_text(man.read_text() + " ")
    with pytest.raises(SystemExit):
        require_pushed_manifest(man, h)                     # the working file differs from its commit


def test_refuses_an_unpushed_commit(tmp_path):
    origin = tmp_path / "origin.git"; work = tmp_path / "work"
    subprocess.run(["git", "init", "--bare", "-b", "main", str(origin)], check=True, capture_output=True)
    subprocess.run(["git", "init", "-b", "main", str(work)], check=True, capture_output=True)
    git(work, "config", "user.email", "t@t"); git(work, "config", "user.name", "t"); git(work, "remote", "add", "origin", str(origin))
    (work / "x").write_text("x"); git(work, "add", "x"); git(work, "commit", "-m", "x"); git(work, "push", "origin", "main"); git(work, "fetch", "origin")
    per = {"a.jsonl.gz": "1" * 64}
    h = hashlib.sha256("".join("%s  %s\n" % (v, n) for n, v in sorted(per.items())).encode()).hexdigest()
    man = work / "MANIFEST.json"; man.write_text(json.dumps({"per_file": per, "sha256_of_the_manifest": h}))
    git(work, "add", "MANIFEST.json"); git(work, "commit", "-m", "m")
    with pytest.raises(SystemExit):
        require_pushed_manifest(man, h)                     # committed, not pushed
