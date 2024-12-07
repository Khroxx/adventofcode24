safe = 0

with open('input2.txt', 'r') as file:
    for line in file:
        nmbers = line.split()

        id_numbers = list(map(int, line.split()))

        # line strictly increases
        increases = all(a < b for a, b in zip(id_numbers, id_numbers[1:]))
        # line strictly decreases
        decreases = all(a > b for a, b in zip(id_numbers, id_numbers[1:]))

        if increases or decreases:
            is_safe = True
            for a, b in zip(id_numbers, id_numbers[1:]):
                difference = abs(a - b)
                if difference < 1 or difference > 3:
                    is_safe = False
                    break
            if is_safe:
                print(id_numbers, "safe")
                safe += 1
            else:
                print(id_numbers, "unsafe")
        else:
            print(id_numbers, "unsafe")


# PART ONE SOLUTION
print(safe)
