import json, math, sys, warnings
warnings.filterwarnings("ignore")
import snappy
PI2 = math.pi ** 2
d = json.load(open(sys.argv[1]))
def lr(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
def sym(w): return lr(swap(w)) in (w, lr(w[::-1]))
ch = sorted((abs(v[1]), w) for w, v in d.items() if not sym(w))
print("chiral threads with |CS| < 1e-4:", [(w, c) for c, w in ch if c < 1e-4])
print("count chiral with |CS| < 1e-3:", sum(1 for c, w in ch if c < 1e-3), " < 1e-2:", sum(1 for c, w in ch if c < 1e-2))
for c, w in ch[:4]:
    M = snappy.ManifoldHP("b++" + w)
    cv = M.complex_volume()
    print(w, len(w), "double:", d[w][1], " HP Im cvol:", cv.imag(), " HP vol:", M.volume())
