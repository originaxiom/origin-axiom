"""Does a BROADER invariant sweep find a second object-level distinguisher for m004?

Paper IV states: of SEVEN elementary invariants, exactly one separates m004 within its
Q(sqrt-3) shape-field family -- H_1 = Z. Seven is a small sample, and the claim is stronger
than the test. This widens the sweep. If any additional invariant separates, the paper is
wrong as written and must be corrected.
"""
import sys
try:
    import snappy
except ImportError:
    print("SKIP: snappy unavailable"); sys.exit(0)

FAM = ["m003","m004","m202","m203","m206","m207","m208",
       "m410","m412","s118","s119","s594","s595","s596"]

def safe(f, default=None):
    try: return f()
    except Exception: return default

rows = {}
for n in FAM:
    M = snappy.Manifold(n)
    Mc = M.copy(); safe(lambda: Mc.reverse_orientation())
    rows[n] = dict(
        homology      = str(M.homology()),
        volume        = round(M.volume(), 9),
        tets          = M.num_tetrahedra(),
        cusps         = M.num_cusps(),
        sym_order     = safe(lambda: M.symmetry_group().order()),
        chern_simons  = safe(lambda: round(M.chern_simons(), 9)),
        cusp_shape    = safe(lambda: complex(round(M.cusp_info('shape')[0].real, 7),
                                             round(M.cusp_info('shape')[0].imag, 7))),
        alexander     = safe(lambda: str(M.alexander_polynomial())),
        fundamental_n = safe(lambda: (M.fundamental_group().num_generators(),
                                      M.fundamental_group().num_relators())),
        length_min    = safe(lambda: round(min(complex(g.length).real
                                               for g in M.length_spectrum(2.0)), 7)),
        h1_is_Z       = str(M.homology()).replace(" ", "") == "Z",
        amphichiral   = safe(lambda: bool(M.is_isometric_to(Mc))),
        solution_type = safe(lambda: M.solution_type()),
    )

m4 = rows["m004"]
others = [n for n in FAM if n != "m004"]
print("invariants swept: %d   family size: %d\n" % (len(m4), len(FAM)))
print("  %-16s %-30s %s" % ("invariant", "m004", "also held by"))
separators = []
for k in m4:
    same = [n for n in others if rows[n][k] == m4[k]]
    if not same:
        separators.append(k)
    print("  %-16s %-30s %s" % (k, str(m4[k])[:30],
                                ("NONE  <== SEPARATES" if not same else "%d others" % len(same))))
print("\n  SEPARATORS: %s" % separators)
print("  Paper IV claims exactly one, H_1 = Z.")
extra = [s for s in separators if s not in ("h1_is_Z", "homology")]
if extra:
    print("  *** ADDITIONAL SEPARATORS FOUND: %s -- Paper IV is wrong as written ***" % extra)
else:
    print("  No additional separator among the wider set. Paper IV's claim survives a broader sweep.")
