class QueueFullError(Exception):
  pass

class QueueEmptyError(Exception):
  pass

class LinearQueue:

  def __init__(self, max_size):

    self.items = [None] * max_size
    self.rp = -1
    self.fp = 0

  def enqueue(self, item):

    if self.is_full():
      raise QueueFullError
    
    self.rp += 1
    self.items[self.rp] = item

  def dequeue(self):

    if self.is_empty():
      raise QueueEmptyError
    
    self.fp += 1
    return self.items[self.fp - 1]

  def peek(self):
    return self.items[self.fp]
  
  def is_full(self):

    return self.rp == len(self.items) - 1

  def is_empty(self):

    return self.fp > self.rp

    
# Test it out

q = LinearQueue(5)

# Fill the queue

for c in "Hello":

  q.enqueue(c)

#print(q.peek())

# Print and empty the queue

while not q.is_empty():
  print(q.dequeue())
