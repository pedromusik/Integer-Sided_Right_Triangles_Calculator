import math

def get_min_length():
    while True: 
        try:
            min_length = int(input("What is the minimum dimension of the triangle side you want? "))
            print("\n")
        except ValueError:
            print("Invalid character! Please enter a valid number.\n")
            continue
        if min_length <= 0:
            print("Invalid number! Please enter a positive number.\n")
        else:
            return min_length

def get_max_length():
    while True: 
        try:
            max_length = int(input("What is the maximum dimension of the triangle side you want? "))
            print("\n")
        except ValueError:
            print("Invalid character! Please enter a valid number.\n")
            continue
        if max_length <= 0:
            print("Invalid number! Please enter a positive number.\n")
        else:
            return max_length

def pythagorean_theorem(min_length, max_length):
    for i in range(min_length, max_length + 1):
        for j in range(i, max_length + 1):
            hypotenuse = math.sqrt(pow(i, 2) + pow(j, 2))
            if hypotenuse == int(hypotenuse):
                print("Size of the legs: ", i, " and ", j, "\nSize of the hypotenuse: ", int(hypotenuse), "\n")

def main(): 
    print("\n\033[34mRight-angled Triangle Calculator with Integer Sides\n\033[0m")
    min_length = get_min_length()
    max_length = get_max_length()
    pythagorean_theorem(min_length, max_length)

if __name__ == '__main__':
    main()
