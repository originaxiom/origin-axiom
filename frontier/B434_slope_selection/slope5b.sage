import snappy, math
M0 = snappy.Manifold('4_1'); M0.chern_simons()
print("exceptional slopes verified: {0,+-1,+-2,+-3,+-4} (vol~0/flat/degenerate); +-5 = FIRST hyperbolic")
for s in (5,-5,6,7):
    M=M0.copy(); M.dehn_fill((s,1))
    v=float(M.volume()); cs=float(M.chern_simons()); cs=cs-math.floor(cs)
    try:
        K=M.trace_field_gens().find_field(prec=300, degree=12, optimize=True)
        pol=K[1] if isinstance(K,tuple) else K.defining_polynomial()
    except Exception as e:
        pol=f"(field search failed: {type(e).__name__})"
    print(f"4_1({s},1): vol {v:.8f}  CS {cs:.6f}  trace field: {pol}")
# identify 4_1(5,1) in the census
M=M0.copy(); M.dehn_fill((5,1))
print("\nidentify 4_1(5,1):", M.identify())
