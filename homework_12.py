#1
def sum_of_digits():
    num = input('Enter number: ')
    sum = (int(num[:1]) + int(num[1:2]) + int(num[2:]))
    return sum
print(sum_of_digits())

#2
def sum_of_digits_1():
    num_1 = (input('Enter number: '))
    first_num = int(num_1) // 100
    second_num = (int(num_1[1:])) // 10
    third_num = (int(num_1[2:])) // 1
    sum_1 = first_num + second_num + third_num
    return sum_1
print(sum_of_digits_1())
