#!/usr/bin/env python3
"""xB002 cell 2 - the discriminating computation for L54: within the shape-field family,
which members are covers of m004?  A degree-n cover has volume exactly n * vol(m004).
If class members exist at NON-integer volume ratio, a cover census cannot reach them,
so a statement proved over covers-to-index-6 is not a statement about the class."""
import snappy, json, pathlib

V4 = None
def main():
    global V4
    fam = json.loads(pathlib.Path(__file__).with_name("xb002_results.json").read_text())["family"]
    V4 = float(snappy.Manifold("m004").volume())
    print(f"vol(m004) = {V4:.10f}\n")
    print(f"{'member':>7} {'volume':>13} {'ratio to m004':>14} {'integer ratio?':>15}")
    non_integer, integer = [], []
    for nm in fam:
        v = float(snappy.Manifold(nm).volume())
        r = v / V4
        isint = abs(r - round(r)) < 1e-7
        (integer if isint else non_integer).append((nm, round(r, 6)))
        print(f"{nm:>7} {v:>13.9f} {r:>14.6f} {str(isint):>15}")
    print(f"\ninteger-ratio members (cover-eligible): {[n for n,_ in integer]}")
    print(f"NON-integer-ratio members (NOT covers):  {[n for n,_ in non_integer]}")
    assert non_integer, "expected family members at non-integer volume ratio"
    print(f"\n{len(non_integer)} of {len(fam)} family members cannot be covers of m004 on volume alone.")
    print("A cover census -- at index 6 or any index -- cannot reach them.")
    print("VERIFIED")

if __name__ == "__main__":
    main()
