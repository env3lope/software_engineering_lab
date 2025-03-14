import math

a = int(input("Введіть коефіцієнт 'а': "))
b = int(input("Введіть коефіцієнт 'b': "))
c = int(input("Введіть коефіцієнт 'c': "))


def solve_equation(a, b, c):
    a2 = 2 * a
    discriminant = (b**2) - (4 * a * c)
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (a2)
        x2 = (-b - math.sqrt(discriminant)) / (a2)
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        return None

roots = solve_equation(a, b, c)

if roots is None:
    print("Коренів немає")
elif len(roots) == 1:
    print(f"Корень рівняння {a}x^2 + {b}x + {c}: {roots[0]:.3f}")
else:
    print(
        f"Корені рівняння {a:}x^2 + {b}x + {c}: x1 = {roots[0]:.3f}, x2 = {roots[1]:.3f}")
