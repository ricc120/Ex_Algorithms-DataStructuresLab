def connected_components(nodes, edges, disjoint_set):
    for node in nodes:
        disjoint_set.make_set(node)

    for u,v in edges:
        if disjoint_set.find_set(u) != disjoint_set.find_set(v):
            disjoint_set.union(u,v)

    components = {}
    for node in nodes:
        rep = disjoint_set.find_set(node).value
        if rep not in components:
            components[rep] = []
        components[rep].append(node)

    return list(components.values())
