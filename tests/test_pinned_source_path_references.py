"""Immutable cross-branch copy citations resolve by evidence, not exemptions."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import os

P=Path(__file__).resolve().parents[1]/'scripts/checks/check_path_references.py'
sp=importlib.util.spec_from_file_location('pinned_path_checker',P)
C=importlib.util.module_from_spec(sp);sp.loader.exec_module(C)

def fixture(tmp_path,monkeypatch):
    root=tmp_path/'synthetic-repo';root.mkdir()
    def git(*args):return subprocess.check_output(['git','-C',str(root),*args],
                                                  env=dict(os.environ,GIT_CONFIG_GLOBAL=os.devnull))
    git('init','-q');git('config','user.name','originaxiom');git('config','user.email','test@example.invalid')
    (root/'docs').mkdir();content=b'Foreign evidence: `docs/target.md`\n'
    (root/'docs/source.md').write_bytes(content);(root/'docs/target.md').write_text('actual target\n')
    git('add','docs/source.md','docs/target.md');git('commit','-qm','synthetic original source')
    commit=git('rev-parse','HEAD').decode().strip()
    (root/'copy').mkdir();(root/'copy/source.md').write_bytes(content)
    row={'reference':commit,'source_path':'docs/source.md','copied_path':'copy/source.md',
         'sha256':hashlib.sha256(content).hexdigest()}
    (root/'copy/SOURCE_CUSTODY.json').write_text(json.dumps([row]))
    monkeypatch.setattr(C,'ROOT',str(root))
    return root,commit,row

def test_immutable_original_blob_and_present_target_resolve(tmp_path,monkeypatch):
    root,commit,row=fixture(tmp_path,monkeypatch)
    assert C.pinned_source_reference('copy/source.md')==commit
    assert C.source_target_exists(commit,'docs/target.md')
    assert not C.source_target_exists(commit,'docs/missing.md')

def test_mutated_copy_cannot_borrow_original_paths(tmp_path,monkeypatch):
    root,commit,row=fixture(tmp_path,monkeypatch)
    (root/'copy/source.md').write_text('changed text\n')
    assert C.pinned_source_reference('copy/source.md') is None

def test_matching_copy_hash_does_not_allow_wrong_original_blob(tmp_path,monkeypatch):
    root,commit,row=fixture(tmp_path,monkeypatch)
    row['source_path']='docs/target.md'
    (root/'copy/SOURCE_CUSTODY.json').write_text(json.dumps([row]))
    assert C.pinned_source_reference('copy/source.md') is None

def test_mutable_branch_reference_is_rejected(tmp_path,monkeypatch):
    root,commit,row=fixture(tmp_path,monkeypatch)
    row['reference']='HEAD'
    (root/'copy/SOURCE_CUSTODY.json').write_text(json.dumps([row]))
    assert C.pinned_source_reference('copy/source.md') is None

def test_no_manifest_and_parent_traversal_fail_closed(tmp_path,monkeypatch):
    root,commit,row=fixture(tmp_path,monkeypatch)
    assert C.pinned_source_reference('docs/source.md') is None
    assert not C.source_target_exists(commit,'../target.md')
