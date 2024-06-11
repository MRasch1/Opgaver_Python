import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    sqrt_discriminant = math.sqrt(discriminant)
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    return (x1, x2)

# Test cases
print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 1))
print(solve_quadratic(1, 0, -4))
print(solve_quadratic(1, 0, 4))
