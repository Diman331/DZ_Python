assortment = {"Сливочное", "Бурёнка", "Вафелька", "Сладкоежка"}
in_stock = {"Сливочное", "Вафелька", "Сладкоежка"}

out_of_stock = assortment - in_stock

print("Закончилось:", ", ".join(out_of_stock))
