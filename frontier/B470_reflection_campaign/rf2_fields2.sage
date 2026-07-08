import snappy
bodies = {2:"RLRRLL", 3:"RLRRLLRL", 4:"RLRRLLRLRLRRLL"}
for n, w in sorted(bodies.items()):
    M = snappy.Manifold("b++" + w)
    try:
        gens = M.trace_field_gens()
        fld = gens.find_field(prec=400, degree=32, optimize=True)
        if fld:
            K = fld[0]
            print(f"BODY n={n}: trace field deg {K.degree()}, disc {K.discriminant()}", flush=True)
        else:
            print(f"BODY n={n}: not found (prec 400, degree 32)", flush=True)
    except Exception as e:
        print(f"BODY n={n}: error {e}", flush=True)
print("DONE", flush=True)
