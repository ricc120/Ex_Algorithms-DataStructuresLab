def connected_components(nodes, edges, disjoint_set):
    ds = disjoint_set()
    for node in range(nodes):
        ds.make_set(node)

    for u,v in edges:
        if ds.find_set(u) != ds.find_set(v):
            ds.union(u, v)

    components = {}
    for node in range(nodes):
        rep = ds.find_set(node).value
        if rep not in components:
            components[rep] = []
        components[rep].append(node)

    return list(components.values())
