file_numbers = open("numbers.txt")
sum_elem = 0
for line in file_numbers:
    line = line.split()
    for elem in line:
        sum_elem += int(elem)

file_numbers.close()
sum_elem = str(sum_elem)

file_sum_elem = open("answer.txt", "w")
file_sum_elem.write(sum_elem)

