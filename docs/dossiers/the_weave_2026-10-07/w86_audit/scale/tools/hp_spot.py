"""High-precision (ManifoldHP, quad-double) spot check of a {word: [Vol, CS]} table: a seeded random sample plus the
most ill-conditioned words (longest runs). Reports max |dVol| and max |dCS mod pi^2|, and solution types."""
import json, sys, math, random, warnings
warnings.filterwarnings("ignore")
import snappy, mpmath as mp
mp.mp.dps = 50
T = json.load(open(sys.argv[1])); N = int(sys.argv[2])
words = sorted(T)
def maxrun(w):
    best = cur = 1
    ww = w + w
    for i in range(1, len(ww)):
        cur = cur + 1 if ww[i] == ww[i - 1] else 1
        best = max(best, min(cur, len(w)))
    return best
random.seed(20261014)
sample = set(random.sample(words, N))
sample |= set(sorted(words, key=lambda w: -maxrun(w))[:60])
pi2 = mp.pi ** 2
mv = mc = 0.0; worst = None; nong = []
for w in sorted(sample, key=lambda w: (len(w), w)):
    M = snappy.ManifoldHP("b++" + w)
    v = mp.mpf(str(M.volume()).replace(" ", ""))
    im = mp.mpf(str(M.complex_volume().imag()).replace(" ", ""))
    d = (mp.mpf(T[w][1]) - im) / pi2
    d = abs(d - mp.nint(d)) * pi2
    if abs(float(v) - T[w][0]) > mv: mv = abs(float(v) - T[w][0])
    if float(d) > mc: mc, worst = float(d), w
    if M.solution_type() != "all tetrahedra positively oriented": nong.append(w)
print(json.dumps({"n_checked": len(sample), "max_abs_dVol": mv, "max_abs_dCS_mod_pi2": mc, "worst_cs_word": worst,
                  "non_geometric_HP": nong}, indent=1))
