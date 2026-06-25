import numpy as np

ages = np.array([[21, 17, 19, 20, 26, 30, 56],
                 [39, 40, 22, 14, 55, 66, 98]])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages <= 50)]
seniors = ages[ages >= 50]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
adults2 = np.where(ages >= 18, ages, 0)

print(teenagers)
print(seniors)
print(adults)
print(evens)
print(odds)
print(adults2)
