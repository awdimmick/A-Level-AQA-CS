class CircularQueue:

  def __init__(self, max_size):

    # Create list to store queue's items
    self.items = [None] * max_size
    self.max_size = max_size
    
    # Set initial pointers and current_size values
    self.fp = 0
    self.rp = -1
    self.current_size = 0

  def dequeue(self):

    # First, check if there are any items in the queue
    if not self.is_empty():
      # Assign the item to return to a temporary variable
      item_to_return = self.items[self.fp]
      # (Optional) Replace the item at the front with 'None' to indicate it has been dequeued
      self.items[self.fp] = None
      # Decrement the current size of the queue
      self.current_size -= 1
      # Increment the front pointer and then "wrap" it around the size of the queue's items[] list using modulo operator
      self.fp = (self.fp + 1) % self.max_size
      # Return the item that was at the front of the queue
      return item_to_return
    
    else:
      # If there are no items, raise an error
      raise Exception("Queue is empty!")

  def enqueue(self, data):
    # Test if the queue is full
    if not self.is_full():
      # Increment the rear pointer and wrap around the items list's size      
      self.rp = (self.rp + 1) % self.max_size

      # Store the item at the back of the queue
      self.items[self.rp] = data
      # Increment current size of the queue
      self.current_size += 1
      
    else:
      # If the queue is full, raise an error
      raise Exception("Queue is full!")
      
  def is_empty(self):
    # If there are no items in the queue, it is empty
    return self.current_size == 0

  def is_full(self):
    # If there are as many items in the queue as it can store it is full
    return self.current_size == self.max_size

  def __repr__(self):
    # Modify how the queue's state and contents is displayed by Python
    s = f"Queue: {self.items}\n"
    s += f"FP: {self.fp}\tRP: {self.rp}\n"
    s += f"Current size: {self.current_size}\tMax size: {self.max_size}"
    return s

# Initialise a new CircularQueue object, q, and enqueue so items to it.
q = CircularQueue(5)
q.enqueue("a")
q.enqueue("b")
q.enqueue("c")
q.enqueue("d")
