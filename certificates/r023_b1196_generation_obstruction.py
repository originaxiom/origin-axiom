#!/usr/bin/env python3
"""Independently rerun the two carrier dimensions used in OA-C1155.

This wrapper deliberately uses the banked B299 and B891 primary computations,
resolved relative to this file, then applies only the exact dimension
obstruction.  It can be launched from any working directory with the same
Python environment those two banked computations require (sympy + mpmath).
"""

from itertools import combinations
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
B299 = ROOT / "frontier" / "B299_trinification_triality" / "trinification_triality.py"
B891 = ROOT / "frontier" / "B891_matter_extension" / "matter_extension.py"


def run(script: Path) -> str:
    completed = subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
        timeout=360,
    )
    return completed.stdout


triality = run(B299)
matter = run(B891)

assert re.search(r"theta on the 27: 27 weights, #fixed=0, orbit sizes=\{3: 9\}", triality)
assert re.search(r"phi on the 27: 27 weights, #fixed=0, orbit sizes=\{3: 9\}", triality)

match = re.search(r"foreign 16s extracted: \[([0-9, ]+)\]", matter)
assert match is not None
foreign_dims = [int(item.strip()) for item in match.group(1).split(",")]
assert foreign_dims == [16, 16, 16]

block_dims = [9, 9, 9]
union_dims = sorted(
    {
        sum(choice)
        for width in range(len(block_dims) + 1)
        for choice in combinations(block_dims, width)
    }
)
assert union_dims == [0, 9, 18, 27]
assert all(dim not in union_dims for dim in foreign_dims)

print("trinification_blocks=[9, 9, 9]")
print("trinification_union_dimensions=" + repr(union_dims))
print("b891_foreign_eigenspace_dimensions=" + repr(foreign_dims))
print("16_not_in_any_9_block_union=True")
print("OA-C1155 CARRIER IDENTIFICATION: REFUTED")
print("R023 B1196 GENERATION OBSTRUCTION: PASS")
