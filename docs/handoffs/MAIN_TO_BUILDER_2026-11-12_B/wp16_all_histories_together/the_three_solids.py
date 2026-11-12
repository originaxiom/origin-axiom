#!/usr/bin/env python3
"""WP-1.6: the three-valent graph of the moves at levels 3, 4 and 5 is the tetrahedron, the cube and the dodecahedron.

Each level's graph (level_graphs_sparse.graph) is compared, as a graph, with the solid's own graph built from scratch
(networkx's constructions).  Control: at level 6 (24 vertices) it is none of the three, and at level 5 it is not the
other three-valent graph on 20 vertices that networkx builds (the Desargues graph)."""
import json, pathlib, sys
import networkx as nx
HERE = pathlib.Path(__file__).resolve().parent; sys.path.insert(0, str(HERE))
import level_graphs_sparse as LG
def as_graph(N):
    A = LG.graph(N).tocoo(); G = nx.MultiGraph()
    G.add_nodes_from(range(A.shape[0]))
    for i, j, v in zip(A.row, A.col, A.data):
        if i < j:
            for _ in range(int(v)): G.add_edge(int(i), int(j))
        elif i == j: G.add_edge(int(i), int(i))
    return G
out = {}
for N, name, solid in ((3, "the tetrahedron", nx.tetrahedral_graph()), (4, "the cube", nx.cubical_graph()), (5, "the dodecahedron", nx.dodecahedral_graph())):
    G = as_graph(N); simple = nx.Graph(G).number_of_edges() == G.number_of_edges() and nx.number_of_selfloops(G) == 0
    same = simple and nx.is_isomorphic(nx.Graph(G), solid)
    out[N] = {"vertices": G.number_of_nodes(), "edges": G.number_of_edges(), "no double edge and no loop": bool(simple), "is": name, "isomorphic": bool(same)}
    print("level %d: %d vertices, %d edges, simple: %s; it is %s: %s" % (N, G.number_of_nodes(), G.number_of_edges(), simple, name, same))
G6 = as_graph(6); c1 = not any(nx.is_isomorphic(nx.Graph(G6), s) for s in (nx.tetrahedral_graph(), nx.cubical_graph(), nx.dodecahedral_graph()))
c2 = not nx.is_isomorphic(nx.Graph(as_graph(5)), nx.desargues_graph())
print("controls: level 6 is none of the three: %s; level 5 is not the Desargues graph: %s" % (c1, c2))
G2 = as_graph(2); print("level 2: %d vertices, %d edges (two vertices joined three times)" % (G2.number_of_nodes(), G2.number_of_edges()))
out["controls"] = {"level 6 is none of the three": bool(c1), "level 5 is not the Desargues graph": bool(c2)}
json.dump(out, open(HERE / "the_three_solids.json", "w"), indent=1)
