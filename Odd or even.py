def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))


result = check_even_or_odd(num)
print(f"The number {num} is {result}.")