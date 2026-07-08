import snappy
words = {3:"RLR", 4:"RLRRL", 5:"RLRRLRLR", 6:"RLRRLRLRRLRRL"}
bodies = {3:"RLRRLLRL", 4:"RLRRLLRLRLRRLL"}
for label, table in [("LETTER", words), ("BODY", bodies)]:
    for n, w in sorted(table.items()):
        M = snappy.Manifold("b++" + w)
        try:
            gens = M.trace_field_gens()
            fld = gens.find_field(prec=200, degree=12, optimize=True)
            if fld:
                K = fld[0]
                print(f"{label} n={n}: trace field deg {K.degree()}, disc {K.discriminant()}", flush=True)
            else:
                print(f"{label} n={n}: not found at prec/degree cap", flush=True)
        except Exception as e:
            print(f"{label} n={n}: error {e}", flush=True)
print("DONE", flush=True)
