#!/usr/bin/env python3
"""Import the owner's exact recovery ZIP. Never run archived research programs."""
from __future__ import annotations
import argparse
import hashlib
import io
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import zipfile

BRANCH = 'chatgpt/weave-physics-archive-2026-10-11'
ARCHIVE = 'Weave_All_13_Runs_Artifact_Archive.zip'
ARCHIVE_BYTES = 1266286
ARCHIVE_SHA256 = 'afdf14b8b0691db97345d5b947fb2bbea08de4872140667e1ccdcef860c1011e'
PREFIX = 'chatgpt_weave_2026_10_11/'
DEST = 'reports/chatgpt_weave_2026_10_11'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def gitsha(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def relative_path(name: str) -> str:
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and str(p) == name,
            'Noncanonical archive path: ' + repr(name))
    require(not any(x in ('..', '.', '.git') for x in p.parts), 'Unsafe path: ' + name)
    require('\\' not in name and '\0' not in name, 'Unsafe path: ' + repr(name))
    return name


def read_and_verify(archive: Path) -> tuple[dict, dict, dict[str, bytes]]:
    raw = archive.read_bytes()
    require(len(raw) == ARCHIVE_BYTES and sha256(raw) == ARCHIVE_SHA256,
            'Recovery ZIP does not match the original byte count and SHA-256; refusing import.')
    payload: dict[str, bytes] = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        require(z.testzip() is None, 'Recovery ZIP CRC error')
        require(sum(i.file_size for i in z.infolist()) < 10_000_000, 'Expansion too large')
        for info in z.infolist():
            require(not info.is_dir(), 'Unexpected directory record')
            require(info.filename.startswith(PREFIX), 'Unexpected archive prefix')
            name = relative_path(info.filename[len(PREFIX):])
            require(name not in payload, 'Duplicate archive member: ' + name)
            kind = stat.S_IFMT(info.external_attr >> 16)
            require(kind in (0, stat.S_IFREG), 'Nonregular file: ' + name)
            payload[name] = z.read(info)
    require(len(payload) == 291, 'Wrong recovery member count')
    manifest = json.loads(payload['MANIFEST.json'])
    inventory = json.loads(payload['SOURCE_INVENTORY.json'])
    require(len(manifest['files']) == 289, 'Wrong manifest size')
    expected: set[str] = set()
    for row in manifest['files']:
        name = relative_path(row['path'])
        require(name not in expected, 'Duplicate manifest entry: ' + name)
        expected.add(name)
        data = payload[name]
        require(len(data) == row['bytes'] and sha256(data) == row['sha256']
                and gitsha(data) == row['git_blob_sha'], 'Manifest mismatch: ' + name)
        require(row['mode'] in ('100644', '100755'), 'Unexpected mode: ' + name)
    require(set(payload) == expected | {'MANIFEST.json', 'SHA256SUMS.txt'},
            'Unaccounted recovery files')
    sums: dict[str, str] = {}
    for line in payload['SHA256SUMS.txt'].decode('utf-8').splitlines():
        digest, name = line.split('  ', 1)
        require(name not in sums, 'Duplicate SHA256SUMS name')
        sums[name] = digest
        require(sha256(payload[relative_path(name)]) == digest, 'SHA256SUMS mismatch: ' + name)
    require(set(sums) == expected | {'MANIFEST.json'}, 'SHA256SUMS population differs from manifest')
    archives = inventory['original_archives']
    require(len(archives) == 14, 'Expected fourteen original archives')
    require(sorted(x['run'] for x in archives if x['run']) == list(range(1, 14)),
            'All thirteen runs must occur exactly once')
    count = 0
    for entry in archives:
        data = payload[entry['path']]
        require(sha256(data) == entry['sha256'], 'Original ZIP hash mismatch')
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            require(z.testzip() is None, 'Original ZIP CRC error')
            rows = [m for m in inventory['members'] if m['archive'] == entry['archive']]
            actual = [i.filename for i in z.infolist() if not i.is_dir()]
            require(len(actual) == len(set(actual)) == len(rows), 'Original member count mismatch')
            require(set(actual) == {m['zip_member'] for m in rows}, 'Original member population mismatch')
            for member in rows:
                require(z.read(member['zip_member']) == payload[member['path']],
                        'Extracted original member differs: ' + member['path'])
                count += 1
    require(count == 254, 'Expected 254 original member files')
    for entry in inventory['standalone_copies']:
        require(sha256(payload[entry['archived_path']]) == entry['sha256'],
                'Standalone snapshot mismatch')
    return manifest, inventory, payload


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo-root', type=Path, default=Path.cwd())
    parser.add_argument('--verify-staged', action='store_true')
    args = parser.parse_args()
    root = args.repo_root.resolve()
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        require(os.environ.get('GITHUB_REF') == 'refs/heads/' + BRANCH,
                'This importer may run only on the archive branch')
        require(os.environ.get('GITHUB_REPOSITORY') == 'originaxiom/origin-axiom',
                'Unexpected repository')
    manifest, inventory, payload = read_and_verify(root / ARCHIVE)
    dest = root / DEST
    require(not dest.is_symlink(), 'Destination is a symlink')
    dest.mkdir(parents=True, exist_ok=True)
    modes = {row['path']: row['mode'] for row in manifest['files']}
    for name, data in payload.items():
        p = dest / name
        for parent in (p, *p.parents):
            require(not parent.is_symlink(), 'Symlink in destination: ' + str(parent))
            if parent == root:
                break
        if args.verify_staged:
            require(p.is_file() and p.read_bytes() == data, 'Working copy mismatch: ' + name)
        else:
            if p.exists():
                require(p.is_file() and p.read_bytes() == data,
                        'Existing file differs; refusing overwrite: ' + name)
            else:
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_bytes(data)
            p.chmod(0o755 if modes.get(name) == '100755' else 0o644)
    if args.verify_staged:
        result = subprocess.run(['git', 'ls-files', '--stage', '-z', '--', DEST],
                                cwd=root, check=True, capture_output=True)
        staged = {}
        for record in result.stdout.split(b'\0'):
            if not record:
                continue
            meta, path = record.split(b'\t', 1)
            mode, blob, stage = meta.decode().split()
            require(stage == '0', 'Unmerged archive entry')
            staged[path.decode()] = (mode, blob)
        for name, data in payload.items():
            require(staged.get(DEST + '/' + name) ==
                    (modes.get(name, '100644'), gitsha(data)),
                    'Git index changed original bytes or mode: ' + name)
    receipt = {
        'status': 'VERIFIED', 'archive_branch': BRANCH,
        'recovery_zip': ARCHIVE, 'recovery_zip_bytes': ARCHIVE_BYTES,
        'recovery_zip_sha256': ARCHIVE_SHA256,
        'numbered_runs': 13, 'original_archives': 14,
        'original_member_files': 254, 'recovery_member_files': len(payload),
        'manifest_files': len(manifest['files']),
        'standalone_snapshots': len(inventory['standalone_copies']),
        'all_original_member_bytes_match': True,
        'all_manifest_sha256_and_git_blobs_match': True,
        'git_index_verified': args.verify_staged,
        'scientific_programs_executed': False,
        'complete_chat_export_included': False,
    }
    (dest / 'RESTORE_RECEIPT.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
