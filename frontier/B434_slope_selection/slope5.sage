import snappy, math
M0 = snappy.Manifold('4_1'); M0.chern_simons()
print("== the exceptional-slope boundary (forced by topology) ==")
for p in range(0,7):
    M=M0.copy(); M.dehn_fill((p,1))
    try:
        v=float(M.volume()); sol=M.solution_type()
        hyp = "HYPERBOLIC" if (v>0.3 and "geometric" in sol) else "exceptional"
        print(f"  4_1({p},1): vol {v:.6f}  [{sol[:20]}] -> {hyp}")
    except Exception as e: print(f"  4_1({p},1): ERR")
print("\n== the first hyperbolic pair (+-5): the minimal chirality-generating input ==")
for s in (5,-5):
    M=M0.copy(); M.dehn_fill((s,1))
    v=float(M.volume()); cs=float(M.chern_simons()); cs=cs-math.floor(cs)
    K=M.trace_field(prec=200, degree=12)
    print(f"  4_1({s},1): vol {v:.8f}  CS mod1 {cs:.8f}")
    print(f"      trace field: {K.defining_polynomial() if K else 'not found'}  disc {K.discriminant().factor() if K else ''}")
print("\n== control: trace fields of the NEXT slopes (+-6,+-7) ==")
for s in (6,-6,7,-7):
    M=M0.copy(); M.dehn_fill((s,1))
    K=M.trace_field(prec=200, degree=16)
    print(f"  4_1({s},1): trace field {K.defining_polynomial() if K else '?'}  disc {K.discriminant().factor() if K else '?'}")
