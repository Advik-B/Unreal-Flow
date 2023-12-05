from proto.nodes_pb2 import *
g = [*globals().keys()]
for global_ in g:
    if global_.startswith("__"):
        continue
    print(global_)

print(IOpin)
