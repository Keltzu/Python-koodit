import random
N = int(input("Anna pisteiden määrä: "))
s_ympyrä = 0

for _ in range(N):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x**2 + y**2 < 1:
        s_ympyrä += 1

pi_arvo = 4 * s_ympyrä / N
print("piin likiarvo: ", pi_arvo)