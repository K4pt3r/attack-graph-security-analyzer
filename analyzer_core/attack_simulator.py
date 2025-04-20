import networkx as nx
from attacker_models import AttackerModel

class AttackSimulator:
    def __init__(self, graph: nx.Graph, attacker: AttackerModel):
        self.graph = graph
        self.attacker = attacker

    def simulate(self):
        compromised_nodes = set()
        queue = list(self.attacker.initial_access)

        while queue:
            current = queue.pop(0)
            compromised_nodes.add(current)

            for neighbor in self.graph.neighbors(current):
                if neighbor not in compromised_nodes:
                    if self.graph.nodes[neighbor].get("vulnerable"):
                        queue.append(neighbor)

        return compromised_nodes

if __name__ == "__main__":
    from loader import NetworkLoader
    from graph_builder import GraphBuilder
    from attacker_models import AttackerType

    loader = NetworkLoader("data/generated_topologies/sample_topology.json")
    loader.load()
    graph = GraphBuilder(loader.get_devices(), loader.get_connections()).build_graph()

    attacker = AttackerModel(AttackerType.INTERNAL, [loader.get_devices()[0]['id']])
    simulator = AttackSimulator(graph, attacker)
    result = simulator.simulate()

    print(f"Скомпрометировано {len(result)} узлов: {result}")
