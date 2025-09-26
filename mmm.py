import statistics


data = [12, 45, 83, 52]

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)

average = (mean + median + mode) / 3
print(int(average))
