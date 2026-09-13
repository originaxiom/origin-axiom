"""OUTSIDE BENCH -- PARI/GP arrives, validated against a PROVED bench result.

No seal: this records a capability and a validation. Every number below is either
produced by the new tool in this run, or quoted from B1093's banked FINDINGS.md.

B1093 proved, BY HAND and without PARI ("no PARI; sympy + hand-rolled algorithms"),
five facts about K = Q[x]/(x^3 - 12x - 5), the field classifying B990's rational orbit.
PARI is asked for the same five. A new tool's first job is to agree with what the
bench already proved the hard way.

Run: python3 outside_bench/certificates/pari_arrives.py
"""
import re
import shutil
import subprocess

GP = shutil.which("gp")

BANKED = {                       # quoted from frontier/B1093_route_a_arithmetic/FINDINGS.md
    "disc": "6237 = 3^4 * 7 * 11",
    "index": "Z[theta] = O_K  (Dedekind's criterion at the sole candidate p = 3)",
    "signature": "totally real (the signature map is surjective; sign vectors fill {+-1}^3)",
    "class_number": "h(K) = 1 PROVED (Minkowski bound (2/9)sqrt(6237) ~ 17.55; all EIGHT "
                    "prime ideals of norm <= bound exhibited PRINCIPAL)",
    "units": "N(theta^2 + 2 theta - 4) = +1 and N(3 theta^2 + 6 theta + 2) = -1",
    "narrow": "h+ = h = 1",
}

SCRIPT = """
K = nfinit(x^3 - 12*x - 5);
print("disc=", K.disc);
print("index=", K.index);
print("sign=", K.sign);
B = bnfinit(x^3 - 12*x - 5);
print("h=", B.no);
print("cyc=", B.cyc);
print("fu=", B.fu);
print("narrow=", bnfnarrow(B));
quit
"""

print("=" * 78)
print("PARI/GP ARRIVES -- validated against B1093, a PROVED hand computation")
print("=" * 78)

if GP is None:
    print("  gp NOT FOUND -- this certificate cannot run.")
    raise SystemExit(1)
ver = subprocess.run([GP, "--version"], capture_output=True, text=True)
banner = (ver.stdout + ver.stderr).strip().split("\n")
print(f"\n  gp at {GP}")
for line in banner[:3]:
    print(f"    {line.strip()}")

r = subprocess.run([GP, "-q"], input=SCRIPT, capture_output=True, text=True, timeout=600)
out = dict(re.findall(r"^(\w+)=\s*(.*)$", r.stdout, re.M))
print(f"\n  raw gp output:")
for k, v in out.items():
    print(f"    {k:8s} = {v}")

print("\n" + "-" * 78)
print("THE FIVE FACTS B1093 PROVED BY HAND, ASKED OF THE NEW TOOL")
print("-" * 78)
checks = []


def check(label, got, want, banked):
    ok = got == want
    checks.append(ok)
    print(f"\n  [{'OK ' if ok else 'FAIL'}] {label}")
    print(f"         B1093 (hand, PROVED): {banked}")
    print(f"         PARI (this run)     : {got}")
    return ok


check("field discriminant", out["disc"], "6237", BANKED["disc"])
check("Z[theta] = O_K  (index 1)", out["index"], "1", BANKED["index"])
check("totally real  (r1, r2) = (3, 0)", out["sign"], "[3, 0]", BANKED["signature"])
check("class number", out["h"], "1", BANKED["class_number"])
check("class group trivial", out["cyc"], "[]", BANKED["class_number"])
u = out["fu"]
has_u1 = "x^2 + 2*x - 4" in u
has_u2 = "3*x^2 + 6*x + 2" in u
checks.append(has_u1 and has_u2)
print(f"\n  [{'OK ' if has_u1 and has_u2 else 'FAIL'}] the two fundamental units, as elements")
print(f"         B1093 (hand, PROVED): {BANKED['units']}")
print(f"         PARI (this run)     : {u}")
print(f"         theta^2 + 2theta - 4 present: {has_u1};  3theta^2 + 6theta + 2 present: {has_u2}")
nar = out["narrow"].startswith("[1,")
checks.append(nar)
print(f"\n  [{'OK ' if nar else 'FAIL'}] narrow class number")
print(f"         B1093 (hand, PROVED): {BANKED['narrow']}")
print(f"         PARI (this run)     : {out['narrow']}  (leading 1 = h+ = 1)")

print("\n" + "=" * 78)
print(f"  {sum(checks)} of {len(checks)} checks agree.")
print("  A tool that reproduces a hand proof is usable; one that does not is not.")
assert all(checks)
print("=" * 78)
