"""agy digest: a STATIC read (nothing executed) of the lane's test test_five_phase_master_toe_closure at 18c607040 --
which dictionary keys it asserts for phases 1-9, the audit function and Theorems 10-13, whether each key is returned by
toe_closure.py at the same commit (the independent lane found 12 missing keys at 951998a73), and which asserts are
literals, frame mathematics, or comparisons with measured numbers.  The lane's code is read with git show, never run."""
import json, pathlib, re, subprocess
REF = "origin/agy/audit-2026-11-02"
ROOT = pathlib.Path(__file__).resolve().parents[4]
def show(p): return subprocess.run(["git", "-C", str(ROOT), "show", f"{REF}:{p}"], capture_output=True, text=True, check=True).stdout
test = show("tests/test_elevation_operator_gate.py").splitlines()
src = show("src/origin_axiom/toe_closure.py")
a = next(i for i, l in enumerate(test) if l.startswith("def test_five_phase_master_toe_closure"))
b = next(i for i, l in enumerate(test) if "Theorem 14:" in l and i > a)
block = test[a:b]
keys = sorted(set(k for l in block for k in re.findall(r'\["([A-Za-z0-9_]+)"\]', l) if not re.search(r"mb_|mt_over|mtau|y_b|tan_?beta|over_mb", k, re.I)))
missing = [k for k in keys if f'"{k}"' not in src]
VALUE_HINT = re.compile(r"rel_error|pdg|_pred\b|satisfies_cosmological|sum_mnu|avoids_cosmological|m_tau_PeV|chi2_|Mh_pole|Mt_pole|MZ_over")
FIRE = re.compile(r"mb_|mt_over|mtau|y_b|yb_|yt_over_yb|tan_?beta|m_b|over_mb|b_over_t|bottom", re.I)   # the firewall
fire_lines = [i + a + 1 for i, l in enumerate(block) if FIRE.search(l)]
asserts = [l.strip() for l in block if l.strip().startswith("assert") and not FIRE.search(l)]
value_asserts = [l for l in asserts if VALUE_HINT.search(l)]
literal_flag_asserts = [l for l in asserts if re.search(r"is (True|False)\s*$|== \(|== \[|== [0-9.]+\s*$", l)]
out = {"commit": subprocess.run(["git", "-C", str(ROOT), "rev-parse", REF], capture_output=True, text=True).stdout.strip(),
       "test lines": [a + 1, b], "asserts in the phase/audit/T10-13 block (firewalled lines excluded)": len(asserts), "test lines touching firewalled keys (not printed)": None, "distinct keys asserted": len(keys),
       "keys asserted but absent from toe_closure.py at this commit": missing,
       "asserts that lock a comparison with a measured number or a value-claim quantity (by key name)": len(value_asserts),
       "asserts on a literal flag, tuple, list or a hard-coded number": len(literal_flag_asserts)}
out["test lines touching firewalled keys (not printed)"] = fire_lines
for k, v in out.items(): print(k, ":", v)
print("value-claim asserts:"); [print("   ", l) for l in value_asserts]
pathlib.Path(__file__).with_suffix(".json").write_text(json.dumps(dict(out, value_asserts=value_asserts, literal_asserts=literal_flag_asserts), indent=1))
