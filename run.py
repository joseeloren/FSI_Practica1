# Search methods
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import search
import matplotlib.pyplot as plt
import numpy as np


ab = search.GPSProblem('A', 'B', search.romania)

mat = np.empty((4,2,))

print (search.branch_bound_subestimate_graph_search(ab,mat,3))
print (search.branch_bound_graph_search(ab,mat,2))
print (search.breadth_first_graph_search(ab,mat,0).path())
print (search.depth_first_graph_search(ab,mat,1).path())

fig, ax = plt.subplots()

# Hide axes
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Table from Ed Smith answer
collabel=("Nodos visitados", "Nodos expandidos")
rowlabel=("Búsqueda en Anchura", "Búsqueda en Profundidad", "Ramificación y acotación", "Ramificación y acotación con subestimación")
ax.table(cellText=mat,rowLabels=rowlabel,colLabels=collabel,loc='center')

#axs[1].plot(clust_data[:,0],clust_data[:,1])
plt.show()

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
