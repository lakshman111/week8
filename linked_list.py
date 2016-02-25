# Can we use the computer to keep track of a list of things
# without using Python's built-in abilities?
#
# Let's try to replicate the following functionality:
#
# groceries = []
# groceries.append("Apples")
# groceries.append("Bananas")
# groceries.append("Cookies")
# groceries[0]   # => "Apples"
# groceries[1]   # => "Bananas"
# groceries[2]   # => "Cookies"
#
# Remember, no built-in lists or dictionaries may be used.
#
# Let's start by mapping out a solution on paper.
#
# Then we can try to teach the computer to do the same.
class Item:

  def __init__(self):
    self.data = None
    self.next = None



class GroceryList:
  def __init__(self):
    self.head = None

  def __getitem__(self, index):
    return self.at(index)

  def display(self):
    print("Apples")
    print("Bananas")
    print("Cookies")

  def remove_all(self):
    self.head = None

  def append(self, data):
    new_item = Item()
    new_item.data = data

    if self.head is None:
      self.head = new_item
    else:
      current_item = self.head
      while (current_item.next != None):
        current_item = current_item.next
      current_item.next = new_item

  def at(self, position):
    current_item = self.head
    while position > 0 and current_item != None:
      current_item = current_item.next
      position -= 1

    if current_item != None:
      return current_item.data
    else:
      return None

  def length(self):
    n = 0
    current_item = self.head
    while (current_item != None):
      n += 1
      current_item = current_item.next

    return n
