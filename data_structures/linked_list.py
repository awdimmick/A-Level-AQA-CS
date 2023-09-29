class Node:
  data = None
  next = None

head = Node()
head.data = "A"

def append_to_list(node, data):
  if node.next == None:    # Are we at the end of the list?
    node.next = Node()
    node.next.data = data

  else:
    append_to_list(node.next, data)

def print_list(node):
  print(node.data)
  if node.next != None:
    print_list(node.next)

def in_list(item, head):
  if head.data == item: 
    return True
  
  elif head.next == None:
    return False
  
  else:
    return in_list(item, head.next)

def in_list_iterative(item, head):
  
  current_node = head

  if current_node.data == item:
    return True
  
  while current_node.next != None:
    current_node = current_node.next
    if current_node.data == item:
        return True

  return False

def get_item_from_list(index, head):
  
  if head == None:
    raise IndexError

  elif index == 0:
    return head.data
  
  else:
    return get_item_from_list(index - 1, head.next)
  

def get_item_from_list_iterative(index, head):
  
  current_node = head

  while index > 0:
    current_node = current_node.next
    index -= 1

  if current_node == None:
    raise IndexError
  
  return current_node.data


append_to_list(head, "B")
append_to_list(head, "C")
append_to_list(head, "D")

print_list(head)
print(in_list("A", head))
print(in_list("D", head))
print(in_list_iterative("A", head))
print(in_list_iterative("D", head))

print(get_item_from_list(3, head))
print(get_item_from_list_iterative(3, head))