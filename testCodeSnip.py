# filename: hello_toko.py

def greet_user(name):
    return f"Hello, {name}! Welcome to the Toko project."

def sum_numbers(a, b):
    return a + b

def main():
    name = input("Enter your name: ")
    print(greet_user(name))

    print("\nNow let's do a simple addition.")
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print(f"The sum is: {sum_numbers(x, y)}")
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
