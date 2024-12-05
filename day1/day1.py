total_diff = 0
total_sim = []

with open('input1.txt', 'r') as file:
    set1 = []
    set2 = []

    for line in file:
        left, right = line.strip().split()

        set1.append(int(left))
        set2.append(int(right))

    set1 = sorted(set1)
    set2 = sorted(set2)

# Part One
    total_diff = sum(abs(a - b) for a, b in zip(set1, set2))

# Part Two
    for num in set1:
        x = [1 for x in set2 if x == num]
        total_sim.append(num * sum(x))

# Solution One
print(total_diff)


# Solution Two
print(sum(total_sim))
