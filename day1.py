total_diff = 0

with open('input1.txt', 'r') as file:
    set1 = []
    set2 = []

    for line in file:
        left, right = line.strip().split()

        set1.append(int(left))
        set2.append(int(right))

    set1 = sorted(set1)
    set2 = sorted(set2)

    total_diff = sum(abs(a - b) for a, b in zip(set1, set2))

print(total_diff)

