from protobuf.nodes_pb2 import (
    BaseNode,
    NodeGraph,
    NodeType,
    PrintNode,
)

node_graph = NodeGraph()

for i in range(10):
    # Add PrintNode
    print_node = PrintNode()
    print_node.base.name = f"PrintNode_{i}"
    print_node.base.type = NodeType.PRINT
    print_node.message = f"Hello World {i}"
    node_graph.nodes.append(print_node)



print(node_graph)

# Export to file
with open("node_graph.bin", "wb") as f:
    f.write(node_graph.SerializeToString())

