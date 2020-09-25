
# number = input("Enter a number: ")

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "Fizz-Buzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return "Not a Fizz or a Buzz"

print(fizz_buzz(1))