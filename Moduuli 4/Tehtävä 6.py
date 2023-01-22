import random
n_point = int(input("Anna arvottavien pisteiden määrä:"))
n_in_circle = 0
for i in range(n_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <1:
        n_in_circle += 1
pi_approx = 4 * n_in_circle / n_points
print("Piin likiarvo ", pi_approx)