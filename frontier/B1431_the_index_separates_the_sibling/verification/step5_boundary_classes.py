"""
Step 5.  Verify ALL EIGHT published q-series for the figure-eight knot complement.

SOURCE (verbatim, p. 297-298):
  S. Garoufalidis, C. D. Hodgson, N. R. Hoffman, J. H. Rubinstein,
  "The 3D-index and normal surfaces", Illinois J. Math. 60 (2016) 289-352,
  https://doi.org/10.1215/ijm/1498032034
  (local copy: ghrs_normal_surfaces.pdf, text at ghrs_normal_surfaces.txt lines 430-470)

  "I_T(x mu + y lambda) = sum_{k in Z} q^k J_D(2k,k,x) J_D(2k-x+2y, k, -2y)
                        = sum_{k in Z} I_D(k-x, k) I_D(k+2y, k-x+2y)."

All I_D here are in the GAROUFALIDIS convention (arXiv:1208.1663 eq 1.2),
i.e. I^G(m,e), with I^G(m,e) = I^P(e,m) for the PROMPT's convention.
"""
from tet_index import I_delta, s_str, s_mul, s_add, s_shift, s_trunc, s_eq, sgn

X = 44                 # x-exponents; published data reaches x^20


def IG(m, e, Xmax=X):
    return I_delta(e, m, Xmax)


def delta_x(m, e):
    p = lambda t: max(0, t)
    return p(m) * p(m + e) + p(-m) * p(e) + p(-e) * p(-e - m) + max(0, m, -e)


def index_xy(x, two_y, Xmax=X):
    """GHRS: sum_k I_D(k-x,k) I_D(k+2y, k-x+2y).   two_y = 2y (an integer)."""
    tot = {}
    ks = [k for k in range(-80, 81)
          if delta_x(k - x, k) + delta_x(k + two_y, k - x + two_y) <= Xmax]
    assert ks and min(ks) > -78 and max(ks) < 78, "k-range not safely bounded"
    for k in ks:
        tot = s_add(tot, s_mul(IG(k - x, k, Xmax), IG(k + two_y, k - x + two_y, Xmax), Xmax))
    return tot, len(ks)


# published series, as {x-exponent: coeff}; x-exponent = 2 * (power of q)
PUB = {
    ("0",        0, 0): {0:1, 2:-2, 4:-3, 6:2, 8:8, 10:18, 12:18, 14:14, 16:-12, 18:-52, 20:-106},
    ("mu",       1, 0): {2:-2, 4:-2, 6:2, 8:8, 10:16, 12:16, 14:10, 16:-14, 18:-52, 20:-102},
    ("2mu",      2, 0): {2:-1, 4:-1, 6:3, 8:6, 10:12, 12:9, 14:3, 16:-19, 18:-50, 20:-88},
    ("lambda",   0, 2): {6:1, 8:2, 10:5, 12:2, 14:-3, 16:-16, 18:-32, 20:-52},
    ("4mu+lam",  4, 2): {2:1, 8:-1, 10:-2, 12:-5, 14:-8, 16:-10, 18:-11, 20:-6},
    ("lam/2",    0, 1): {3:-2, 7:4, 9:10, 11:14, 13:10, 15:-2, 17:-32, 19:-68},
    ("mu+lam/2", 1, 1): {2:-1, 4:-1, 6:2, 8:7, 10:11, 12:11, 14:3, 16:-17, 18:-49, 20:-88},
    ("2mu+lam/2",2, 1): {1:-1, 5:1, 7:4, 9:7, 11:7, 13:3, 15:-12, 17:-31, 19:-62},
}

print("=" * 78)
print("STEP 5: all eight published boundary classes of m004 (GHRS 2016, pp.297-298)")
print("   formula  I_T(x mu + y lam) = sum_k I_D(k-x,k) I_D(k+2y, k-x+2y)")
print("=" * 78)
allok = True
for (lab, x, two_y), pub in PUB.items():
    mine, nk = index_xy(x, two_y)
    hi = max(pub)
    m_t = {k: v for k, v in s_trunc(mine, hi).items() if v}
    p_t = {k: v for k, v in pub.items() if v}
    ok = (m_t == p_t)
    allok &= ok
    print(f"\n I_T({lab:<10}) [x={x}, 2y={two_y}]  {nk} lattice points   {'MATCH' if ok else '*** MISMATCH ***'}")
    print(f"   mine      : {s_str(mine, hi)}")
    if not ok:
        diff = {k: m_t.get(k, 0) - p_t.get(k, 0) for k in set(m_t) | set(p_t)
                if m_t.get(k, 0) != p_t.get(k, 0)}
        print(f"   published : {p_t}")
        print(f"   diff      : {diff}")

print("\n" + "=" * 78)
print(f"ALL EIGHT PUBLISHED SERIES REPRODUCED EXACTLY: {allok}")
print("=" * 78)

# extend the trivial class further than the literature prints it
print("\nThe trivial class pushed past the published range (GHRS stop at q^10):")
tot, nk = index_xy(0, 0, 60)
print("  I_m004(0,0)(q) =", s_str(tot, 50))
