"""import networkx as nx
import matplotlib.pyplot as plt

# 生成WS小世界图，和RandWire论文一致
G = nx.watts_strogatz_graph(n=32, k=6, p=0.1, seed=42)

# 看邻接矩阵（后面可以直接拿去搭DAG网络）
adj = nx.to_numpy_array(G)
print(adj.shape)

# 画图
nx.draw(G, pos=nx.circular_layout(G), node_size=80)
plt.show()"""

import snap
G = snap.GenSmallWorld(Nodes=100, NodeOutDeg=4, RewireProb=0.1)
