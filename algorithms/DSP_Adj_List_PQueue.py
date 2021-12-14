"""
An implementation of Dijkstra's Shortest Path algorithm that utilises Node objects that each store their label, best-known distance from the start and 
previous node along that best-known path from the start, along with a priority queue to determine which nodes to visit next based on distance from the start.

The graph is implemented as a dictionary of nodes, representing an adjacency list, where each node is paired with another dictionary that pairs adjacent nodes with
distances from the current node (the key in the 'graph' dictionary), represented as integers.
"""

class Node:

  # Define a Node class to store the graph nodes. Each node includes a label, distance from start and previous node along path to the start.

  def __init__(self, label):
    self.label = label
    self.prev = None
    self.dist = None

  @property
  def path_from_start(self):

    path = self.label
    
    p = self.prev
    while p != None:
      path = p.label + path
      p = p.prev
      
    return f"Path from start to {self.label}: {path}, Distance: {self.dist}"

  def __repr__(self):
    return f"['{self.label}' ({self.dist} via {self.prev.label if self.prev is not None else '-'})]"

class PQueue:

  # Define a priority queue to store the nodes to visit, allowing us to dequeue the node with the shortest known distance from the starting node.

  def __init__(self):
    self.items = []

  def add(self, n:Node):
    
    # Only add items not already in the queue. Add to end of queue, we will worry about priority upon dequeueing
    if n not in self.items:
      self.items.append(n)

  def dequeue(self):
    
    n = None
    
    # If there is only 1 node in the queue, return it
    if len(self.items) == 1:
      n = self.items[0]
      del self.items[0]

    # If there are more than one nodes in the queue, find the node with the lowest distance and return it
    elif len(self.items) > 1:
      
      lowest_node_distance = self.items[0].dist
      lowest_node_index = 0
      i = 0

      while i < len(self.items):
        if self.items[i].dist < lowest_node_distance:
          lowest_node_distance = self.items[i].dist
          lowest_node_index = i

        i += 1

      n = self.items[lowest_node_index]
      del self.items[lowest_node_index]
    
    return n

  
  def set_distance(self, label, distance):
    # Find the item with the matching label and update its Priority
    for n in self.items:
      if n.label == label:
        n.dist = distance
        break

  def __repr__(self):
    output = "["
    for n in self.items:
      output += f"[Label: '{n.label}', Priority: {n.dist}], "
    return output + "]"

  def __len__(self):
    return len(self.items)

# Initialise nodes
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

# Define the graph, including distances between nodes as an adjacency list
graph = {
  a: {b:4, c:3, d:7},
  b: {a:4, d:1, f:5},
  c: {a:3, d:3, e:5},
  d: {a:7, b:1, c:3, e:2, f:2, g:7},
  e: {c:5, d: 2, g:2},
  f: {b:5, d:2, g:5},
  g: {d:7, e:2, f:5}
}

# Initialise priority queue to hold nodes to visit and visited queue to hold nodes already explored
queue = PQueue()
visited = []

# Set source and destiation nodes to find the shortest path between
source = a
destination = g

#### Let Dijkstra's magic begin...! ####


# Add the source (start) to the queue to begin there
source.dist = 0
queue.add(source)

# while there are nodes left to visit in the queue...
while len(queue) > 0:
  
  # Get the next node to visit with shortest distance from the source
  current_node = queue.dequeue()

  # Record that we have visited the current node so that it doesn't get visited again
  visited.append(current_node)

  # Get al of the adjacent nodes to the current nodes (as a dictionary in this case)
  adjacent_nodes = graph[current_node]

  # For each node that is adjacent to the current node
  for adj_n in adjacent_nodes:

    if adj_n not in visited:
      # calculate the distance to the adjacent node from the start via the currently visited node
      distance_via_current_node = current_node.dist + adjacent_nodes[adj_n]
      
      # If the distance from the start via the current node is shorter than known distance, update it and the the 'prev' field
      if adj_n.dist is None:
        adj_n.dist = distance_via_current_node
        adj_n.prev = current_node
      
      elif distance_via_current_node < adj_n.dist:
        adj_n.dist = distance_via_current_node
        adj_n.prev = current_node

      # Add adjacent node to queue for future visits
      queue.add(adj_n)


# Run the algorithm!    
if __name__ == "__main__":     
  print("Visited nodes list:")
  print("-------------------")
  print(visited)
  print()
  print(destination.path_from_start)
