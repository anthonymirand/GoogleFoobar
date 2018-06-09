# Modified source code from:
# http://en.wikipedia.org/wiki/Ford-Fulkerson_algorithm/
# http://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

class Graph:
  def __init__(self,graph):
    self.graph = graph
    self.row = len(graph)

  '''
  Returns true if there is a path from source 's' to sink 't' in
  residual graph. Also fills parent[] to store the path
  '''
  def BFS(self, s, t, parent):
    # Mark all the vertices as not visited
    visited = [ False ] * (self.row)
    # Create a queue for BFS
    queue = []
    # Mark the source node as visited and enqueue it
    queue.append(s)
    visited[s] = True

    # Standard BFS Loop
    while queue:
      # Dequeue a vertex from queue and print it
      u = queue.pop(0)
      # Get all adjacent vertices of the dequeued vertex u
      # If a adjacent has not been visited, then mark it
      # visited and enqueue it
      for index, value in enumerate(self.graph[u]):
        if not visited[index] and 0 < value:
          queue.append(index)
          visited[index] = True
          parent[index] = u

    # If we reached sink in BFS starting from source, then return
    # true, else false
    return True if visited[t] else False

  def FordFulkerson(self, source, sink):
    # This array is filled by BFS and to store path
    parent = [ -1 ] * (self.row)
    max_flow = 0 # There is no flow initially

    # Augment the flow while there is path from source to sink
    while self.BFS(source, sink, parent):
      # Find minimum residual capacity of the edges along the
      # path filled by BFS. Or we can say find the maximum flow
      # through the path found.
      path_flow = float("Inf")
      s = sink
      while s != source:
        path_flow = min(path_flow, self.graph[parent[s]][s])
        s = parent[s]
      # Add path flow to overall flow
      max_flow += path_flow
      # update residual capacities of the edges and reverse edges
      # along the path
      v = sink
      while v != source:
        u = parent[v]
        self.graph[u][v] -= path_flow
        self.graph[v][u] += path_flow
        v = parent[v]

    return max_flow


def answer(entrances, exits, path):
  '''
  It is important to note that this problem is a multiple source/multiple sink
  max-flow problem. Each of the entrances is a source and each of the exits is
  a sink. We can reduce this problem to a single source/single sink max-flow
  problem by creating a super sink and super source. We can add a super source
  and super sink node to the beginning and end of the provided adjacency matrix,
  and set the capacities to the sum(sink capacities) and 2000000 (maximum number
  of bunnies). The algorithm is modified from the Geeks for Geeks
  Ford-Fulkerson algorithm for computing maximum flow on a directed graph.
  '''

  # Extend horizontally to account for sink/source
  for i, row in enumerate(path):
    path[i] = [0] + row + [0]
  # Add super source with capacities
  path = [[0] * len(path[0])] + path
  for entrance in entrances:
    path[0][entrance + 1] = sum(path[entrance + 1])
  # Add super sink with capacities
  path = path + [[0] * len(path[0])]
  for exit in exits:
    path[exit + 1][-1] = 2000000

  g = Graph(path)
  return g.FordFulkerson(0, len(path) - 1)

