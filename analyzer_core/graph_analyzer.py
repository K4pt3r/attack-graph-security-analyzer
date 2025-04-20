import networkx as nx
from typing import List, Dict

class GraphAnalyzer:
    def __init__(self, graph: nx.Graph):
        self.graph = graph

    def find_vulnerable_nodes(self) -> List[str]:
        return [n for n, attr in self.graph.nodes(data=True) if attr.get("vulnerable")]

    def shortest_path_to_vuln(self, source: str) -> Dict[str, List[str]]:
        paths = {}
        for node in self.find_vulnerable_nodes():
            try:
                path = nx.shortest_path(self.graph, source=source, target=node)
                paths[node] = path
            except nx.NetworkXNoPath:
                continue
        return paths

    def rank_nodes_by_degree(self) -> List[str]:
        return sorted(self.graph.nodes(), key=lambda n: self.graph.degree(n), reverse=True)

    def get_critical_paths(self) -> List[List[str]]:
        critical_paths = []
        vulnerable_nodes = self.find_vulnerable_nodes()
        for src in vulnerable_nodes:
            for dst in vulnerable_nodes:
                if src != dst:
                    try:
                        path = nx.shortest_path(self.graph, source=src, target=dst)
                        critical_paths.append(path)
                    except nx.NetworkXNoPath:
                        continue
        return critical_paths
