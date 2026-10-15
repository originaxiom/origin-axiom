# threads (Lyndon words in L, R, length 2..8) -> hyperbolic matrices -> binary quadratic forms (c, d-a, -b), disc t^2-4;
# bucketed by the primitive discriminant (t^2-4)/g^2, g the form's content (corrected after the referee: first version bucketed by t^2-4)
import numpy as np, math, json, collections
from sympy import factorint
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1; m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n: w.append(w[len(w) - m])
        while w and w[-1] == k - 1: w.pop()
L = np.array([[1,0],[1,1]]); R = np.array([[1,1],[0,1]])
def mat(w):
    M = np.eye(2, dtype=int)
    for ch in w: M = M @ (L if ch == "L" else R)
    return M
words = [w for w in lyndon(8) if len(w) >= 2]
bydisc = collections.defaultdict(list)
for w in words:
    M = mat(w); a,b,c,d = M.flatten(); t = a + d; D = t*t - 4
    g = math.gcd(math.gcd(int(c), int(d-a)), int(b))
    Dp = int(D) // (g*g)            # the primitive form's discriminant: composition acts here
    bydisc[Dp].append((w, g))
mirror = lambda w: w.translate(str.maketrans("LR","RL"))
print(len(words), "threads;", len(bydisc), "distinct primitive discriminants")
multi = {D: v for D, v in bydisc.items() if len(v) > 1}
for D in sorted(multi):
    ws = [x[0] for x in multi[D]]
    # canonical Lyndon rep of mirror
    def lyn(s):
        rots = [s[i:]+s[:i] for i in range(len(s))]; return min(rots)
    pairs = sum(1 for w in ws if lyn(mirror(w)) in ws and lyn(mirror(w)) != w)//2
    selfm = sum(1 for w in ws if lyn(mirror(w)) == w)
    print(f"disc {D:5d} = {factorint(D)}  threads {len(ws)}: {ws}  (mirror pairs {pairs}, self-mirror {selfm}, content gcds {[x[1] for x in multi[D]]})")
single = sorted(D for D, v in bydisc.items() if len(v) == 1)
print("discriminants with one thread:", [int(x) for x in single])
