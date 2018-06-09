# Blossom Algorithm is an algorithm in graph theory for constructing maximum
# matchings on graphs
# Pseudocode from: https://en.wikipedia.org/wiki/Blossom_algorithm

def maximum_matching(graph):
  non_matching_edges = [ [ x, y ]
                         for x in range(len(graph))
                         for y in range(len(graph[x]))
                         if graph[x][y] == 1 ]
  matching_edges = []
  non_matching = [ x for x in range(len(graph)) ]

  path_found = True
  while path_found: # can find an augmented path
    path_found = False
    for i in non_matching:
      visited = []
      path = []
      node = i
      edge_not_in_matching = True

      # Blossom algorithm defines an augmented path as a path with edges
      # alternating between in the matching and not in the matching
      # Every time we add an edge to the path, we flip 'edge_not_in_matching'
      while 1:
        find_unvisited = False
        visited.append(node)
        index = 0

        # Check node if not visited and edge is in matching/non-matching search
        for j in range(len(graph[node])):
          if j not in visited and graph[node][j] != 0:
            if ((edge_not_in_matching and [node, j] in non_matching_edges) or
              (not edge_not_in_matching and [node, j] in matching_edges)):
              edge_not_in_matching = not edge_not_in_matching
              index = j
              find_unvisited = True
              break

        if find_unvisited:
          path.append(node)
          node = index
        elif not path:
          break
        else: # backtrack
          node = path.pop()
          edge_not_in_matching = not edge_not_in_matching

        # If found node:
        # 1. if edge was not in augmented path, add the edge
        # 2. if edge was in augmented path, remove the edge
        # Add first/last edge to path since the matching includes them
        if node in non_matching and node != i:
          path.append(node)
          path_found = True
          for j in range(len(path) - 1):
            if [ path[j], path[j + 1] ] in matching_edges:
              matching_edges.remove([path[j], path[j + 1]])
              matching_edges.remove([path[j + 1], path[j]])
              non_matching_edges.append([path[j], path[j + 1]])
              non_matching_edges.append([path[j + 1], path[j]])
            else:
              non_matching_edges.remove([path[j], path[j + 1]])
              non_matching_edges.remove([path[j + 1], path[j]])
              matching_edges.append([path[j], path[j + 1]])
              matching_edges.append([path[j + 1], path[j]])
          non_matching.remove(path[0])
          non_matching.remove(path[len(path) - 1])
          break

  return len(non_matching)

def answer(banana_list):
  pairs = [ [ 0 for y in banana_list ] for x in banana_list ]
  loop_found = False

  for i in range(len(pairs)):
    for j in range(len(pairs[i])):
      guard_1, guard_2 = banana_list[i], banana_list[j]
      # Odd sums loop forever
      if (guard_1 + guard_2) % 2 == 1:
        loop_found = True
        pairs[i][j] = 1
        continue
      # Same number will not loop
      if guard_1 == guard_2:
        continue
      # Loop if numbers are different powers of two
      while guard_1 % 2 == 0 and guard_2 % 2 == 0:
        guard_1 /= 2
        guard_2 /= 2
      if guard_1 % 2 != guard_2 % 2:
        loop_found = True
        pairs[i][j] = 1
        continue
      # If numbers are same powers of two, divide/multiply until
      # one of first two cases is reached
      while guard_1 != guard_2 and (guard_1 + guard_2) % 2 != 1:
        temp = max(guard_1, guard_2)
        guard_1 = min(guard_1, guard_2)
        guard_2 = temp - guard_1
        guard_2 /= 2
      if (guard_1 + guard_2) % 2 == 1:
        loop_found = True
        pairs[i][j] = 1

  if not loop_found:
    return len(banana_list)
  return maximum_matching(pairs)
