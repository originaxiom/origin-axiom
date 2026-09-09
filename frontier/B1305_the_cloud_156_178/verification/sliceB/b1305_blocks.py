"""B1305 slice B, Q2 -- what exactly is mirror-odd in Gukov-Manolescu's F_K (DESIGN_B sealed fa793cf2). Data source: the cloud's block
generator xi_recursion_fast.py (GM's recursion (171)-(172) for the figure-eight), executed in the pinned worktree at N blocks; main's own
check on its output: for every k <= N the block Xi_k has lowest exponent -floor((k-1)^2/4), highest +floor((k-1)^2/4), and is
PALINDROMIC (the mirror q -> 1/q fixes the amphichiral knot's blocks). Hence c_low = -1/16, c_high = +1/16, centre (c_low + c_high)/2 = 0:
the mirror-odd quantity is the CENTRE of the exponent range (GM's c is the lowest edge; it is -1/16 on an amphichiral knot and is not
itself mirror-odd), and the WIDTH (c_high - c_low)/2 = 1/16 is mirror-even. Usage: b1305_blocks.py <worktree> [N]"""
import sys, os, json, io, contextlib
root = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 20
path = os.path.join(root, "outside_bench", "certificates", "xi_recursion_fast.py")
src = open(path).read()
g = {"__name__": "xi_gen", "__file__": path}
sys.argv = [path, str(N)]
buf = io.StringIO()
cwd = os.getcwd(); os.chdir(os.path.dirname(path))
try:
    with contextlib.redirect_stdout(buf): exec(compile(src, path, "exec"), g)
finally:
    os.chdir(cwd)
block = g["block"]
fails = []
rows = []
for k in range(1, N + 1):
    lo, coeffs = block(k)
    hi = lo + len(coeffs) - 1
    w = (k - 1) ** 2 // 4
    pal = coeffs == coeffs[::-1]
    rows.append(dict(k=k, lo=lo, hi=hi, expected=w, palindromic=pal, edge=coeffs[0], width=len(coeffs)))
    if not (lo == -w and hi == w and pal): fails.append(k)
    if k <= 8 or k == N: print(f"  k={k:2d}: exponents [{lo:+d}, {hi:+d}]  (+-floor((k-1)^2/4) = {w})  palindromic {pal}  edge coeff {coeffs[0]}  width {len(coeffs)}")
ok = not fails
print(f"  all {N} blocks: lowest = -floor((k-1)^2/4), highest = +floor((k-1)^2/4), palindromic: {ok}")
print(f"  => c_low = -1/16, c_high = +1/16 (m = 2k-1: floor((k-1)^2/4) = m^2/16 + O(m)); mirror-odd CENTRE = 0; mirror-even half-WIDTH = 1/16")
json.dump(dict(N=N, rows=rows, ok=ok), open(os.path.join(cwd, "b1305_blocks.json"), "w"), indent=1)
print("Q2:", "PASS" if ok else f"FAIL (k = {fails})"); sys.exit(0 if ok else 1)
