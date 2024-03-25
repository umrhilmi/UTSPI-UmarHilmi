#Nama       : Umar Hilmi
#NIM        : 221402077
#Nomor      : 2

def calculate_product(number):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product

def main():
    try:
        print("This program will reads a number (today's test date) and prints the product ")
        number = int(input("Enter a number: "))
        if number < 0:
            print("Please enter a non-negative integer.")
        else:
            result = calculate_product(number)
            print("The product of all values from 1 to", number, "is:", result)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

