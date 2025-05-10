# Unit-IV Graph Theory: Basic terminology for undirected and directed graphs, multigraphs andweighted graphs, paths and circuits, Eulerian paths and circuits, Hamiltonian paths and circuits, PlanarGraphs, Graph Colouring, Cut sets. Trees: Introduction to Trees, Tree terminology, Prefix codes.

import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations
import heapq

print("=== Graph Theory ===")

# 1. Basic Terminology: Undirected Graph
print("\n--- Undirected Graph ---")
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 3), (3, 0)])
print("Nodes:", G.nodes())
print("Edges:", G.edges())

# 2. Directed Graph
print("\n--- Directed Graph ---")
DG = nx.DiGraph()
DG.add_edges_from([(0, 1), (1, 2), (2, 0)])
print("Directed edges:", DG.edges())

# 3. Multigraph
print("\n--- Multigraph ---")
MG = nx.MultiGraph()
MG.add_edges_from([(0, 1), (0, 1), (1, 2)])
print("Multigraph edges:", MG.edges())

# 4. Weighted Graph
print("\n--- Weighted Graph ---")
WG = nx.Graph()
WG.add_weighted_edges_from([(0, 1, 2.5), (1, 2, 1.0)])
for (u, v, wt) in WG.edges(data='weight'):
    print(f"Edge ({u},{v}) has weight {wt}")

# 5. Paths and Circuits
print("\n--- Path Check ---")
print("Path from 0 to 3 in G:", nx.has_path(G, 0, 3))
print("All paths from 0 to 3:", list(nx.all_simple_paths(G, 0, 3)))

# 6. Eulerian Path and Circuit
print("\n--- Eulerian Check ---")
print("Is Eulerian:", nx.is_eulerian(G))
if nx.is_eulerian(G):
    print("Eulerian Circuit:", list(nx.eulerian_circuit(G)))

# 7. Hamiltonian Path (Brute-force approach)
print("\n--- Hamiltonian Path ---")
def is_hamiltonian(graph):
    n = len(graph.nodes())
    for perm in permutations(graph.nodes()):
        if all((perm[i], perm[i+1]) in graph.edges() or (perm[i+1], perm[i]) in graph.edges() for i in range(n-1)):
            return True, perm
    return False, None

h, path = is_hamiltonian(G)
print("Has Hamiltonian Path:", h)
if h:
    print("Hamiltonian Path:", path)

# 8. Planar Graph
print("\n--- Planar Graph ---")
is_planar, _ = nx.check_planarity(G)
print("Is Planar:", is_planar)

# 9. Graph Coloring (Greedy)
print("\n--- Graph Coloring ---")
colors = nx.coloring.greedy_color(G, strategy="largest_first")
print("Coloring:", colors)

# 10. Cut Sets
print("\n--- Cut Sets ---")
cut_nodes = list(nx.articulation_points(G))
cut_edges = list(nx.bridges(G))
print("Articulation Points:", cut_nodes)
print("Bridges (Cut Edges):", cut_edges)

# 11. Trees and Terminology
print("\n=== Trees ===")
T = nx.balanced_tree(r=2, h=2)  # Binary tree of height 2
print("Is Tree:", nx.is_tree(T))
print("Tree Nodes:", T.nodes())
print("Tree Edges:", T.edges())

# 12. Prefix Codes (Huffman Coding)
print("\n--- Prefix Codes (Huffman Tree) ---")
frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}

heap = [[wt, [sym, ""]] for sym, wt in frequencies.items()]
heapq.heapify(heap)

while len(heap) > 1:
    lo = heapq.heappop(heap)
    hi = heapq.heappop(heap)
    for pair in lo[1:]:
        pair[1] = '0' + pair[1]
    for pair in hi[1:]:
        pair[1] = '1' + pair[1]
    heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

print("Huffman Codes:")
for p in sorted(heap[0][1:], key=lambda p: (len(p[-1]), p)):
    print(f"{p[0]}: {p[1]}")

# Optional: Visualize Graph
def draw_graph(G, title="Graph"):
    plt.figure(figsize=(5, 4))
    nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=800)
    plt.title(title)
    plt.show()

# Draw example graph
draw_graph(G, title="Example Undirected Graph")
draw_graph(T, title="Binary Tree")

