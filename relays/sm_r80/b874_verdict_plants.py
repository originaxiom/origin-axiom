"""Plant two false statements of computed mathematics into B874's verdict bracket (copy only) and report whether
tests/test_b874_ladder.py's new lock still passes.  Usage: plant874.py <copy root>"""
import json, pathlib, subprocess, sys
root = pathlib.Path(sys.argv[1]); vf = root / "frontier/B874_measurement_ladder/arc_verdict.json"
orig = vf.read_text(encoding="utf-8")
for old, new in [("four points, all imaginary, to 14 and to 18", "four points, all real, to 16 and to 26"),
                 ("so on the real line it is 12 at every point but the plane stratum's", "so on the real line it reaches 26")]:
    d = json.loads(orig); assert d["claim_one_line"].count(old) == 1, old
    d["claim_one_line"] = d["claim_one_line"].replace(old, new); vf.write_text(json.dumps(d, indent=1, ensure_ascii=False), encoding="utf-8")
    r = subprocess.run([sys.executable, "-B", "-m", "pytest", "-q", "-p", "no:cacheprovider", str(root / "tests/test_b874_ladder.py"),
                        "-k", "verdict_line_scopes"], capture_output=True, text=True, cwd=str(root))
    print("PLANTED %r -> %r: %s" % (old, new, r.stdout.strip().splitlines()[-1]))
vf.write_text(orig, encoding="utf-8")
