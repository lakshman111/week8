from binary_tree import GroceryList

groceries = GroceryList()
groceries.append("Cookies")
groceries.append("Apples")
groceries.append("Zucchini")
groceries.append("Butter")
groceries.append("Milk")
groceries.append("Carrots")
groceries.append("Pizza")
groceries.append("Potatoes")

assert groceries.contains("Cookies")
assert groceries.contains("Milk")
assert not groceries.contains("Broccoli")

groceries.display()
