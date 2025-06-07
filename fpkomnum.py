import numpy as np
from sympy import Rational, factorial, simplify

def compute_diff_table(y_vals):
    n = len(y_vals)
    diff = np.zeros((n, n))
    diff[:, 0] = y_vals
    for j in range(1, n):
        for i in range(n - j):
            diff[i, j] = diff[i + 1, j - 1] - diff[i, j - 1]
            if j <= 4:
                print(f"diff[{i}, {j}] = {round(diff[i, j], 2)}")
    return diff

def stirling_interpolation(x_vals, y_vals, x0_val, x_target_val):
    x_vals = np.array(x_vals, dtype=float)
    y_vals = np.array(y_vals, dtype=float)

    h = x_vals[1] - x_vals[0]
    print(f"\nAll h are equal: h = {h}")

    idx = np.where(x_vals == x0_val)[0][0]
    S = round((x_target_val - x0_val) / h, 2)
    print(f"S = {S}")

    diff = compute_diff_table(y_vals)

    print("\nCalculating Stirling Interpolation")
    result = y_vals[idx]
    print(f"f0 = {result}")

    delta1 = (diff[idx][1] + diff[idx - 1][1]) / 2
    term1 = round(S * delta1,2)
    print(f"Term i=1: {term1}")
    result += term1

    delta2 = diff[idx - 1][2]
    term2 = round((round((S * (S - 1))/2, 2) * delta2),2)
    print(f"Term i=2: {term2}")
    result += term2
    
    delta3 = (diff[idx - 1][3] + diff[idx - 2][3]) / 2
    term3 = round((round((S * (S - 1) * (S - 2))/6, 2) * delta3),2)
    print(f"Term i=3: {term3}")
    result += term3

    delta4 = diff[idx - 2][4]
    term4 = round(((x_target_val/4) * round((S * (S - 1) * (S - 2))/6,2) * delta4),2)
    print(f"Term i=4: {term4}")
    result += term4

    y_interp = round(result, 2)
    return y_interp

x_vals = [3, 6, 9, 12, 15, 18, 21, 24, 27]
y_vals = [-741, -186, 32121, 184956, 634575, 1673874, 3741549, 7451256, 13620771]

x0 = 15
xt = 16
yt = 897104

hasil = stirling_interpolation(x_vals, y_vals, x0, xt)

print(f"\nf({xt}) = {hasil}")
print(f"Et ={abs((yt - hasil)/yt) * 100 : .2f}")