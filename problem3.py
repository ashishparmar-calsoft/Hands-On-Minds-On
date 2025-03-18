from math import gcd, cos, sin, pi

def is_rational_angle(numerator, denominator):
    """
    Checks if cos(pi * numerator / denominator) and sin(pi * numerator / denominator) are rational.
    This occurs when the angle is a rational multiple of pi and denominator is a power of 2.
    """
    while denominator % 2 == 0:
        denominator //= 2
    if denominator == 1:
        return True
    return False

def generate_hypocycloid_points(R, r):
    """
    Generate all distinct integer-coordinate points (x, y) on the hypocycloid.
    """
    points = set()
    g = gcd(R, r)  # Ensures periodicity
    k = 0
    while k < 2 * r:
        if is_rational_angle(k, 2 * r):
            t = (k * pi) / r
            x = int((R - r) * cos(t) + r * cos((R - r) * t / r))
            y = int((R - r) * sin(t) - r * sin((R - r) * t / r))
            points.add((x, y))
        k += g
    return points

def S(R, r):
    """
    Computes the sum of absolute values of x- and y-coordinates for C(R, r).
    """
    total = 0
    for x, y in generate_hypocycloid_points(R, r):
        total += abs(x) + abs(y)
    return total

def T(N):
    """
    Computes T(N) = sum of S(R, r) for all 3 <= R <= N and 1 <= r < R/2.
    """
    total = 0
    R = 3
    while R <= N:
        r = 1
        while r <= R // 2:
            total += S(R, r)
            r += 1
        R += 1
    return total

# Compute T(10^6)
N = 10
result = T(N)
print("T(10) =", result)
