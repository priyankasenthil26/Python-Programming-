arr2 = [14, 16, 87, 36, 25, 89, 34]
M = 1
N = 3

sorted_arr2 = sorted(arr2)
nth_min = sorted_arr2[N-1]
mth_max = sorted_arr2[-M]

sum_val = nth_min + mth_max
diff_val = abs(mth_max - nth_min)

print(f"{M}st Maximum Number = {mth_max}")
print(f"{N}rd Minimum Number = {nth_min}")
print(f"Sum = {sum_val}")
print(f"Difference = {diff_val}")
