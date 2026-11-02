import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt, networkx as nx
G = nx.balanced_tree(2, 3); fig, axs = plt.subplots(1, 4, figsize=(11, 3), dpi=150)
pos_h = {}
for n in G.nodes:
    d = len(nx.shortest_path(G, 0, n)) - 1; pos_h[n] = d
lv = {}; 
for n, d in pos_h.items(): lv.setdefault(d, []).append(n)
hier = {n: (i - (len(ns)-1)/2, -d) for d, ns in lv.items() for i, n in enumerate(ns)}
grid = {n: (n % 4, -(n // 4)) for n in G.nodes}
layouts = [("Force-directed\n(spring)", nx.spring_layout(G, seed=3)), ("Circular", nx.circular_layout(G)), ("Hierarchical\n(tree)", hier), ("Grid", grid)]
graphs=[G, nx.cycle_graph(10), G, nx.convert_node_labels_to_integers(nx.grid_2d_graph(3,4))]
layouts[1]=("Circular", nx.circular_layout(graphs[1])); layouts[3]=("Grid", {i:(i%4,-(i//4)) for i in range(12)})
for ax, (t, p), g in zip(axs, layouts, graphs):
    nx.draw(g, p, ax=ax, node_size=60, node_color="#1F77B4", edge_color="#555", width=1)
    ax.set_title(t, fontsize=12)
fig.tight_layout(); fig.savefig("u2_layouts.png")
