pos_sum = 0
pos_count = 0
neg_sum = 0
neg_count = 0

print("Enter numbers (-1 to stop):")

while True:
    user_input = input().strip()
    if user_input == "":
        continue

    try:
        num = int(user_input)
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if num == -1:
        break
    elif num > 0:
        pos_sum += num
        pos_count += 1
    elif num < 0:
        neg_sum += num
        neg_count += 1

# Calculate averages
pos_avg = pos_sum // pos_count if pos_count > 0 else 0
neg_avg = neg_sum // neg_count if neg_count > 0 else 0

print("avg negative number is", neg_avg, ", avg positive number is", pos_avg)
