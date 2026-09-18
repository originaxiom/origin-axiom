import snappy
for nm in ["m004","m003"]:
    M=snappy.Manifold(nm); G=M.symmetry_group()
    print(nm, G, "order",G.order())
    try:
        for iso in G.isometries():
            print("   ",iso.cusp_maps() if hasattr(iso,'cusp_maps') else iso)
    except Exception as e:
        print("   isometries() ->",e)
