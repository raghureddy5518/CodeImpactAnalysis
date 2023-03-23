from math_operations import add, subtract, multiply, power_of_two, power_of_three
from string_operations import string_length, capitalize, lowercase, reverse

def main():
    x = 5
    y = 3
    s = "Hello, world!"

    # Perform math operations
    print("x + y =", add(x, y))
    print("x - y =", subtract(x, y))
    print("x * y =", multiply(x, y))
    print("x^2 =", power_of_two(x))
    print("x^3 =", power_of_three(x))

    # Perform string operations
    print("Length of s:", string_length(s))
    print("Capitalized s:", capitalize(s))
    print("Lowercase s:", lowercase(s))
    print("Reversed s:", reverse(s))

if __name__ == "__main__":
    main()
