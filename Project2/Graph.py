import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self, num_vertices):
        """Create a graph with adjacency matrix representation."""
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]
    
    def add_edge(self, u, v, weight):
        """Add an undirected edge between u and v with given weight."""
        self.graph[u][v] = weight
        self.graph[v][u] = weight
    
    def get_edges(self):
        """Return list of all edges (u, v, weight)."""
        edges = []
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                if self.graph[u][v] > 0:
                    edges.append((u, v, self.graph[u][v]))
        return edges
    
    def visualize(self, title="Graph Visualization", highlight_path=None):
        """Visualize the graph using networkx with edge weights."""
        G = nx.Graph()
        
        # Add all edges
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                if self.graph[u][v] > 0:
                    G.add_edge(u, v, weight=self.graph[u][v])
        
        plt.figure(figsize=(12, 9))
        pos = nx.spring_layout(G, seed=42, k=1.5, iterations=50)
        
        # Draw nodes
        node_colors = ['lightcoral' if highlight_path and i in highlight_path 
                      else 'lightblue' for i in range(self.num_vertices)]
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                               node_size=700, alpha=0.9, edgecolors='black', linewidths=2)
        
        # Draw edges
        edge_colors = []
        edge_widths = []
        for u, v in G.edges():
            if highlight_path and u in highlight_path and v in highlight_path:
                idx_u = highlight_path.index(u)
                idx_v = highlight_path.index(v)
                if abs(idx_u - idx_v) == 1:  # Adjacent in path
                    edge_colors.append('red')
                    edge_widths.append(4)
                else:
                    edge_colors.append('gray')
                    edge_widths.append(1.5)
            else:
                edge_colors.append('gray')
                edge_widths.append(1.5)
        
        nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6, 
                              edge_color=edge_colors)
        
        # Draw vertex labels
        nx.draw_networkx_labels(G, pos, font_size=14, font_weight='bold')
        
        # Draw edge weights with background
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=11,
                                     font_weight='bold', bbox=dict(boxstyle='round,pad=0.3',
                                     facecolor='yellow', alpha=0.7))
        
        plt.title(title, fontsize=16, fontweight='bold', pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def __str__(self):
        result = "Adjacency Matrix Representation:\n"
        result += "     " + "".join([f"{i:4}" for i in range(self.num_vertices)]) + "\n"
        for i in range(self.num_vertices):
            result += f"{i:3}: "
            for j in range(self.num_vertices):
                if self.graph[i][j] == 0:
                    result += "   -"
                else:
                    result += f"{self.graph[i][j]:4}"
            result += "\n"
        return result