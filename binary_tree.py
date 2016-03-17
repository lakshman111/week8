# Let's build a data structure using a binary tree.
class TreeNode:

  def __init__(self):
    self.data = None
    self.left = None
    self.right = None


class GroceryList:

  def __init__(self):
    self.root = None

  def append(self, data):
    new_node = TreeNode()
    new_node.data = data

  # # if you wanted to use recursion
  # def append(self, data, node):
  #   new_node = TreeNode()
  #   new_node.data = data

  #   if self.root is None:
  #     self.root = new_node
  #   else:
  #     if new_node.data < node.data:
  #       if node.left is None:
  #         node.left = new_node
  #       else:
  #         self.append(data, node.left)
  #     else:
  #       if node.right is None:
  #         node.right = new_node
  #       else:
  #         self.append(data, node.right)

    # GO OVER THIS
    if self.root is None:
      self.root = new_node
    else:
      current_node = self.root
      while current_node != None:
        if new_node.data < current_node.data:
          if current_node.left is None:
            current_node.left = new_node
            break
            # OR
            # current_node = None
          else:
            current_node = current_node.left
        else:
          if current_node.right is None:
            current_node.right = new_node
            break
          else:
            current_node = current_node.right

# call this to do "display" recursively
# groceries.display(groceries.root)
  
  # GO OVER THIS
  def display(self, node):
    if node != None:
      # now put in alphabetical order
      self.display(node.left)
      print(node.data)
      self.display(node.right)

  # special function that is called when we use "in" to call
  def __contains__(self,data):
    return self.contains(data)
  
  def contains(self, data):
    current_node = self.root
    # stop when you are at the end or when you found it
    while current_node != None and current_node.data != data:
      if data < current_node.data:
        current_node = current_node.left
      else:
        current_node = current_node.right

    return current_node != None
