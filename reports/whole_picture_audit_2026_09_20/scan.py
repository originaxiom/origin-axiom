"""Read-only Git content discovery, not semantic absence or science verification.

Run with Python >=3.9; writes only the requested generated JSON receipt.
Searches unique reachable text blobs, including superseded/deleted versions.
One path per historical blob is discovery metadata, not a complete rename map.
"""
import collections
import gzip
import json
import pathlib
import subprocess
import sys

PATTERNS = {
    "extension": "nonsemisimple|non-semisimple|non-split|nonsplit|semisimplification|representation stack",
    "boundary_domain": "self-adjoint extension|operator domain|finite-width|resolved fermion",
    "common_action": "common model|common-model|parent action|source-to-action|source_action",
    "mirror_gap": "mirror gapp|mirror remov|symmetric mass generation|mirror quartic",
    "tbrane": "t-brane|tbrane|pantev|moment map|noncommuting",
    "inflow": "anomaly inflow|anomaly match|anomaly-match|mass inflow",
    "class_selection": "class is the object|family as the object|stabiliser|stabilizer",
    "boundary_index": "3d index|3d-index|tetrahedron index|saturated lattice",
    "partial_fill": "partial filling|partially fill|partial dehn|multi-cusped cover",
    "state_selection": "spontaneous|nontracial|non-tracial|state selection",
    "evidence_dependence": "base rate|base-rate|five names|compression",
    "neutral_cusp": "neutral cusp|cusp neutral|continuous spectrum|scattering determinant",
    "curved_g2": "curved cone|curved-cone|acharya-witten|torsion-free g2|maximal-isotropy",
    "charge_lattice": "cocharacter|line operator|global form|hypercharge normalization",
    "threshold": "friedmann-witten|friedmann--witten|analytic torsion|threshold",
    "tower_scale": "tower growth|tower-growth|growth rate|dimensional transmutation|renormalization group",
    "flavor": "hollow texture|canonical normaliz|canonical normalis|yukawa",
    "gravity": "spin-two|spin-2|graviton|universal coupling",
    "laboratory": "photonic|polariton|mirror-isospectral|cross-hand",
    "nonabelian_rank": "non-abelian holonomy|nonabelian holonomy|beyond-sl|exact hypercharge",
    "higher_module": "t12835|higher-sym|higher sym|unrun modules",
    "hamiltonian": "trace-map action|hamiltonian|reflection positivity|hilbert space",
    "gerbe": "tannakian|gerbe|neutrality obstruction",
    "scattering_scope": "one-loop|one loop|b8112|b8129|boundary-graviton",
}
TEXT = {".md", ".txt", ".tex", ".py", ".rb", ".json", ".rst", ".out", ".log", ".sage", ".toml", ".yaml", ".yml"}


def git(*args):
    return subprocess.check_output(["git", *args])


def main(output):
    refs = git("for-each-ref", "--format=%(refname)", "refs/heads", "refs/remotes", "refs/tags").decode().splitlines()
    tips, tip_blobs = [], set()
    known = {}
    for ref in refs:
        if ref.endswith("/HEAD"):
            continue
        files = 0
        for line in git("ls-tree", "-r", "-z", ref).split(b"\0"):
            if not line:
                continue
            meta, path = line.split(b"\t", 1)
            _, kind, sha = meta.split()
            if kind != b"blob":
                continue
            key, name = sha.decode(), path.decode(errors="replace")
            known.setdefault(key, name)
            tip_blobs.add(key)
            files += 1
        tips.append({"ref": ref, "commit": git("rev-parse", ref + "^{commit}").decode().strip(), "files": files})
    for line in git("rev-list", "--objects", "--all").decode(errors="replace").splitlines():
        sha, _, name = line.partition(" ")
        known.setdefault(sha, name)
    eligible = {sha: name for sha, name in known.items() if pathlib.PurePosixPath(name).suffix.lower() in TEXT}
    cat = subprocess.Popen(["git", "cat-file", "--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    patterns = {key: [term.encode() for term in value.split("|")] for key, value in PATTERNS.items()}
    hits = {key: [] for key in patterns}
    stats = collections.Counter()
    skips = []
    for sha, name in eligible.items():
        cat.stdin.write((sha + "\n").encode()); cat.stdin.flush()
        header = cat.stdout.readline().decode().strip().split()
        if len(header) != 3:
            raise RuntimeError(header)
        _, kind, size = header
        size = int(size)
        data = cat.stdout.read(size)
        if len(data) != size or cat.stdout.read(1) != b"\n":
            raise RuntimeError("short git object")
        if kind != "blob":
            stats["non_blob_candidates"] += 1
            continue
        stats["eligible_text_blobs"] += 1
        if size > 5_000_000 or b"\0" in data:
            skips.append({"blob": sha, "path": name, "bytes": size, "reason": "size>5MB or binary"})
            continue
        stats["scanned_blobs"] += 1
        stats["scanned_bytes"] += size
        if sha in tip_blobs:
            stats["scanned_tip_blobs"] += 1
        lower = data.lower()
        for key, needles in patterns.items():
            positions = [lower.find(term) for term in needles]
            match = min((p for p in positions if p >= 0), default=-1)
            if match >= 0:
                hits[key].append({"blob": sha, "path": name, "at_ref_tip": sha in tip_blobs,
                                  "line": data.count(b"\n", 0, match) + 1})
        if stats["scanned_blobs"] % 5000 == 0:
            print(f"Scanned {stats['scanned_blobs']} unique text versions", flush=True)
    cat.stdin.close(); cat.wait()
    result = {"purpose": "lexical discovery only; not exhaustive semantic reading, absence proof, or result verification",
              "head": git("rev-parse", "HEAD").decode().strip(), "refs": tips,
              "reachable_commits": int(git("rev-list", "--all", "--count")),
              "unique_tip_blobs": len(tip_blobs), "patterns": PATTERNS,
              "stats": dict(stats), "skipped": skips, "hits": hits}
    encoded = (json.dumps(result, indent=2) + "\n").encode()
    pathlib.Path(output).write_bytes(gzip.compress(encoded, mtime=0) if str(output).endswith('.gz') else encoded)
    print(json.dumps({"stats": result["stats"], "skipped": len(skips), "topics": {k: len(v) for k,v in hits.items()}}, indent=2))


if __name__ == "__main__":
    main(sys.argv[1])
