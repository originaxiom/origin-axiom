#!/usr/bin/env python3
"""Check byte preservation without executing archived scientific scripts."""
from pathlib import Path
import hashlib,json,zipfile
root=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
gitsha=lambda b:hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()
manifest=json.loads((root/"MANIFEST.json").read_text())
for row in manifest["files"]:
 p=root/row["path"]
 if not p.is_file():raise SystemExit("Missing: "+str(p))
 b=p.read_bytes()
 if len(b)!=row["bytes"] or sha(b)!=row["sha256"] or gitsha(b)!=row["git_blob_sha"]:raise SystemExit("Byte mismatch: "+str(p))
inv=json.loads((root/"SOURCE_INVENTORY.json").read_text())
assert sorted(r["run"] for r in inv["original_archives"] if r["run"])==list(range(1,14))
count=0
for ar in inv["original_archives"]:
 assert sha((root/ar["path"]).read_bytes())==ar["sha256"]
 with zipfile.ZipFile(root/ar["path"]) as z:
  assert z.testzip() is None
  for m in [x for x in inv["members"] if x["archive"]==ar["archive"]]:
   assert z.read(m["zip_member"])==(root/m["path"]).read_bytes();count+=1
for r in inv["standalone_copies"]:assert sha((root/r["archived_path"]).read_bytes())==r["sha256"]
print(json.dumps({"status":"PASS","numbered_runs":13,"original_archives":len(inv["original_archives"]),"original_zip_members":count,"manifest_files":len(manifest["files"]),"standalone_matches":len(inv["standalone_copies"]),"all_sha256_and_git_blob_hashes_match":True,"scientific_code_executed":False,"full_chat_transcript_included":False},indent=2))
