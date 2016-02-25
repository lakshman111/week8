from linked_list import GroceryList

groceries = GroceryList()
groceries.append("Cookies")
groceries.append("Apples")
groceries.append("Zucchini")
groceries.append("Butter")
groceries.append("Milk")
groceries.append("Carrots")
groceries.append("Pizza")
groceries.append("Potatoes")

assert 8 == groceries.length()
assert "Apples" == groceries[1]

groceries.display()
