class Graph:
    """Graph using adjacency list."""
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, v1, v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.adj[v1].append(v2)

    def display(self):
        print("Graph adjacency list:")
        for v in self.adj:
            print(f"{v} -> {self.adj[v]}")


# ---------- TESTS ----------
if __name__ == "__main__":
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.display()
    assert g.adj["A"] == ["B", "C"]
    assert g.adj["B"] == ["D"]
    print("✅ All Graph test cases passed successfully!")
