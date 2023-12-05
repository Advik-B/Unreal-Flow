from protobuf.nodes_pb2 import (
    BaseNode,
    NodeGraph,
    NodeType
)

node_graph = NodeGraph()

for i in range(10):
    node = node_graph.nodes.add()
    node.id = i
    node.name = f"Node {i}"
    node.description = f"Node {i} description"
    node.type = NodeType.PRINT

    if i > 0:
        connection = node_graph.connections.add()
        connection.from_id = i - 1
        connection.to_id = i

print(node_graph)

# Export to file
with open("node_graph.bin", "wb") as f:
    f.write(node_graph.SerializeToString())

