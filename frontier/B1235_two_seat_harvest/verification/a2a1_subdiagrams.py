"""B1235 cell 4 -- how many A2+A1 sub-diagrams does E6's Dynkin diagram have? (seat D12: 'all ten give Z/6')"""
edges = {(1, 3), (3, 4), (4, 5), (5, 6), (2, 4)}          # Bourbaki E6
adj = {i: set() for i in range(1, 7)}
for u, v in edges: adj[u].add(v); adj[v].add(u)
count = 0
for u, v in edges:                                        # the A2 = an edge
    blocked = {u, v} | adj[u] | adj[v]
    count += sum(1 for w in range(1, 7) if w not in blocked)   # the A1 = a node not adjacent to it
print("A2+A1 sub-diagrams of E6:", count)
assert count == 10
