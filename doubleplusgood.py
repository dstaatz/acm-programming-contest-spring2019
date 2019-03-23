# doubleplusgood.py

digits = input().split("+")
num_pluses = len(digits) - 1
iterations = 2**num_pluses
pluses = 0
unique_values = []
for i in range(iterations):
    to_add = []
    to_add.append(digits[0])
    index = 0
    for i in range(len(digits)-1):
        if 2**i & pluses:
            to_add[index] += digits[i+1]
        else:
            to_add.append(digits[i+1])
            to_add[index] = int(to_add[index])
            index += 1
    to_add[index] = int(to_add[index])
    value = sum(to_add)
    pluses += 1
    if value not in unique_values:
        unique_values.append(value)
print(len(unique_values))