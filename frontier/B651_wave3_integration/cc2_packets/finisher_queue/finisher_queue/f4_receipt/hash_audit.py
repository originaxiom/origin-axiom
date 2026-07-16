"""F4 hash audit: recompute sha256 for every ARTIFACT_HASHES.txt entry in
frontier/B649_silver_holonomy and compare (independent of cc's tooling)."""
import hashlib
import os

B649 = "<seat-workdir>/origin-axiom/frontier/B649_silver_holonomy"
manifest = os.path.join(B649, "ARTIFACT_HASHES.txt")

results = []
with open(manifest) as fh:
    for line in fh:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        parts = line.split("  ", 1)
        if len(parts) != 2:
            parts = line.split(" ", 1)
        claimed_hash, rest = parts[0].strip(), parts[1].strip()
        fname = rest.split(" ")[0]
        path = os.path.join(B649, fname)
        with open(path, "rb") as f:
            actual = hashlib.sha256(f.read()).hexdigest()
        match = (actual == claimed_hash)
        results.append((fname, claimed_hash, actual, match))

n_ok = sum(1 for r in results if r[3])
print(f"{n_ok}/{len(results)} hashes match\n")
for fname, claimed, actual, match in results:
    status = "OK" if match else "MISMATCH"
    print(f"  [{status}] {fname}")
    if not match:
        print(f"      claimed: {claimed}")
        print(f"      actual:  {actual}")
