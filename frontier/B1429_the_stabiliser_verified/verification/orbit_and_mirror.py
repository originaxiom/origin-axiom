import warnings; warnings.filterwarnings("ignore")
import snappy

def cs(M):
    try:
        return float(M.chern_simons())
    except Exception:
        return None

for n in ("m004", "m003"):
    M = snappy.Manifold(n)
    Mm = snappy.Manifold(n); Mm.reverse_orientation()
    a, b = cs(M), cs(Mm)
    print("%-6s CS=%+.10f  mirror CS=%+.10f  sum=%+.2e  |  mod 1/2: %.6f vs %.6f"
          % (n, a, b, a + b, a % 0.5, b % 0.5))

print()
print("fixed points of x -> -x on R/(1/2)Z (i.e. 2x = 0 mod 1/2):")
for x in (0.0, 0.125, 0.25, 0.375):
    print("   x=%.3f   -x mod 1/2 = %.3f   fixed = %s" % (x, (-x) % 0.5, abs(((-x) % 0.5) - x) < 1e-12))
