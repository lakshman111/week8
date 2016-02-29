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

assert "Milk" in groceries

assert groceries.contains("Milk")
assert groceries.contains("Carrots")
assert groceries.contains("Pizza")

assert not groceries.contains("Broccoli")

groceries.display(groceries.root)
