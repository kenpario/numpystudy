import numpy as np

rng = np.random.default_rng()

print(rng.integers(low=1, high=7, size=(3, 2)))
print(np.random.uniform(low=-1, high=1, size=10))

array = np.array([1, 2, 3, 4, 5])
array_choice = rng.choice(array, size=(2,3))

rng.shuffle(array)

print(array)
print(array_choice)
