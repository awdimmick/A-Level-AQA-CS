class PQNode:
  
  def __init__(self, value, priority):

    self.value = value
    self.priority = priority

class PQueue:

  def __init__(self, size):

    self.items = [None] * size
    self.rp = 0

  def is_empty(self):

    all_none = True
    
    for item in self.items:
      if item is not None:
        all_none = False

    return all_none

  def is_full(self):
    return self.rp == len(self.items) - 1
  
  def enqueue(self, value, priority):

    self.items[self.rp] = PQNode(value, priority)
    self.rp += 1

  def dequeue(self):

    lowest_index = 0

    # Deals with the exceptional case where the first item is None 
    # (and therefore later check of its priority will fail)
    while self.items[lowest_index] is None:
      lowest_index += 1

    for i in range(len(self.items)):

      if self.items[i] is not None and self.items[i].priority < self.items[lowest_index].priority:

        lowest_index = i

    item = self.items[lowest_index]

    self.items[lowest_index] = None

    return item

pq = PQueue(5)
pq.enqueue("A", 1)
pq.enqueue("B", 3)
pq.enqueue("C", 1)
pq.enqueue("D", 2)

while not pq.is_empty():
  print(pq.dequeue().value)
