#1
def sum_of_digits(num):
    num = str(num)
    sum = (int(num[:1]) + int(num[1:2]) + int(num[2:]))
    return sum
print(sum_of_digits(345))

#2
def sum_of_digits_1(num_1):
    first_num = (num_1) // 100
    second_num = abs((num_1) % 100) // 10
    third_num = abs(num_1) % 10
    sum_1 = first_num + second_num + third_num
    return sum_1
print(sum_of_digits_1(123))
