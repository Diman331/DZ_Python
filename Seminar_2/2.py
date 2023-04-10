# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

print("| X | Y | Z | ¬(X ∧ Y) ∨ Z |")
print("|---|---|---|--------------|")

for X in range(2):
    for Y in range(2):
        for Z in range(2):
            result = not(X and Y) or Z
            print(f"| {X} | {Y} | {Z} |      {int(result)}       |")
