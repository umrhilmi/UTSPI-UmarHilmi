#Nama       : Umar Hilmi
#NIM        : 221402077
#Nomor      : 5

def read_numbers_from_file(file_name):
    with open(file_name, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers

def print_sum_with_comma_separator(numbers):
    total_sum = sum(numbers)
    formatted_sum = "{:,.3f}".format(total_sum)
    print("Sum of numbers:", formatted_sum)

file_name = "input.txt"
numbers = read_numbers_from_file(file_name)
print_sum_with_comma_separator(numbers)
