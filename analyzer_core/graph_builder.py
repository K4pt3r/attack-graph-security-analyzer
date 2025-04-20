import networkx as nx
from loader import NetworkLoader

class GraphBuilder:
    def __init__(self, devices, connections):
        self.devices = devices
        self.connections = connections
        self.graph = nx.Graph()

    def build_graph(self):
        for device in self.devices:
            has_vuln = any(s.get("vulnerability") for s in device.get("services", []))
            self.graph.add_node(
                device['id'],
                label=device['name'],
                type=device['type'],
                services=device.get("services", []),
                vulnerable=has_vuln
            )

        for link in self.connections:
            self.graph.add_edge(link['from'], link['to'])

        return self.graph

if __name__ == "__main__":
    loader = NetworkLoader("data/generated_topologies/sample_topology.json")
    loader.load()
    builder = GraphBuilder(loader.get_devices(), loader.get_connections())
    graph = builder.build_graph()
    print(f"Graph has {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")
