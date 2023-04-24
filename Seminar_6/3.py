import math

for denom in range(2, 12):
    for num in range(1, denom):
        if math.gcd(num, denom) == 1:
            print(f"{num}/{denom}")
