import snappy
for name in ["m004","m003","m015","m009"]:
    M = snappy.Manifold(name)
    n = M.num_tetrahedra(); r = M.num_cusps()
    G = [list(map(int,row)) for row in M.gluing_equations(form='log')]
    print("="*70)
    print(name, "tets",n,"cusps",r,"vol",M.volume(),"H1",M.homology())
    print("  gluing_equations log rows:", len(G))
    for idx,row in enumerate(G):
        tag = "edge" if idx<n else ("merid" if (idx-n)%2==0 else "longi")
        print(f"   {idx:2d} {tag:6s} {row}")
    cs=[sum(row[c] for row in G[:n]) for c in range(3*n)]
    print("  edge column sums:", cs)
    print("  cusp_info:", M.cusp_info())
