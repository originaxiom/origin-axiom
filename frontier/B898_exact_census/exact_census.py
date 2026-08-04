"""B898 (N3): the EXACT signature census of the torus C.

B893's census was float-with-tolerance (borderline generic-complex counts
1, 1, 7). Here: charpoly of ad(x_n) over Q (the ad matrices are exact
rational), factored over Q; each irreducible factor classified exactly --
all-real roots (Sturm), purely imaginary (even poly whose s = t^2 roots are
all real negative), or generic complex. Exact counts replace the census.
"""
import io, contextlib, json, os
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(open(os.path.join(HERE, "..", "B854_centralizer_exact",
                                   "e6_centralizer.py")).read(),
                 "b854", "exec"), globals())
print("frame rebuilt", flush=True)

t = sp.Symbol("t")
out = {}
for n in ns:
    M = sp.Matrix(ADS[n])
    cp = M.charpoly(t).as_expr()
    print(f"charpoly({n}) done", flush=True)
    fl = sp.factor_list(cp)
    zero = real = imag = cplx = 0
    facs = []
    for f, mult in fl[1]:
        p = sp.Poly(f, t)
        d = p.degree()
        if d == 1 and p.all_coeffs()[-1] == 0:      # the factor t
            zero += mult
            facs.append(("t", mult)); continue
        nreal = len(p.real_roots())
        if nreal == d:
            real += d*mult; facs.append((str(f)[:60], mult, "REAL")); continue
        # purely imaginary test: even polynomial with s-roots all negative real
        coeffs = p.all_coeffs()
        is_even = all(c == 0 for c in coeffs[1::2])
        if is_even:
            s = sp.Symbol("s")
            ps = sp.Poly(f.subs(t, sp.sqrt(s)).expand(), s)
            sroots = ps.real_roots()
            if len(sroots) == ps.degree() and all(r < 0 for r in sroots):
                imag += d*mult
                facs.append((str(f)[:60], mult, "IMAGINARY")); continue
        cplx += d*mult
        facs.append((str(f)[:60], mult, "COMPLEX/MIXED", nreal))
    out[str(n)] = {"zero": zero, "real": real, "imaginary": imag,
                   "complex_or_mixed": cplx, "factors": facs}
    print(n, "->", {k: v for k, v in out[str(n)].items() if k != "factors"},
          flush=True)
json.dump(out, open(os.path.join(HERE, "results.json"), "w"), indent=1,
          default=str)
print("saved", flush=True)
