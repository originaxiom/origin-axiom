"""Exact q-series checks (B1691's own qseries.py, exact over Q(i)) of two facts the referee uses:
(1) D2R.D2R = -(5/144) E4 (DR.DR) identically, so a = D2R - (5/288) E4 R has a.a = 0 identically (B1691 addendum's 'pole' t = -5/288);
(2) DR.DR is a multiple of eta^6 (the bilinear form's character), so the identity in (1) is forced by dim eta^6 M_4 = 1."""
import io, json, contextlib, importlib.util, pathlib, sys
from fractions import Fraction as F
Bdir = sorted(pathlib.Path(__file__).resolve().parents[3].glob("B1691_*"))[0] / "verification"
sys.path.insert(0, str(Bdir))
spec = importlib.util.spec_from_file_location("te", Bdir / "the_exponents.py"); te = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(te)
S, B, dot, e4 = te.S, te.B, te.dot, te.e4
lhs = dot(B[2], B[2]) + e4 * dot(B[1], B[1]) * S.c(F(5, 144))
a = [B[2][i] - e4 * B[0][i] * S.c(F(5, 288)) for i in range(3)]
aa = dot(a, a)
eta6 = (te.th2 * te.th3 * te.th4) * (te.th2 * te.th3 * te.th4) * S.c(F(1, 4))
ratio = dot(B[1], B[1]) * eta6.inv()
out = {"D2R.D2R + (5/144) E4 DR.DR: lowest surviving power of x (None = identically 0 to x^240)": lhs.ord() if lhs.ord() is None or lhs.ord() <= 200 else ">200",
       "a.a for a = D2R - (5/288) E4 R: lowest power (None/>200 = identically 0)": aa.ord() if aa.ord() is None or aa.ord() <= 200 else ">200",
       "DR.DR / eta^6: powers present up to x^150": sorted(k for k in ratio.d if k <= 150), "DR.DR / eta^6 constant": [str(x) for x in ratio.d.get(0, (0, 0))]}
(pathlib.Path(__file__).with_name("exact_identities.json")).write_text(json.dumps(out, indent=1, default=str))
print(json.dumps(out, indent=1, default=str))
