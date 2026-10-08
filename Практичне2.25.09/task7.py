data = []
for x in input("Введіть числа через пробіл: ").split():
    data.append(float(x))
m = len(data)
total_sum = 0
for x in data:
    total_sum += x
mean = total_sum / m
variance_sum = 0
for x in data:
    variance_sum += (x - mean) ** 2
variance = variance_sum / (m - 1)
std_deviation = variance ** 0.5
print(mean)
print(variance)
print(std_deviation)