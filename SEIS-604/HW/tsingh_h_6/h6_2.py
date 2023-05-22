# h6_2.py

def factorial(N):
    if N == 0:
        return 1

    return N * factorial(N-1)

def main():
    num = int(input("Enter the integer N: "))
    print("Factorial of", num, "is", factorial(num))

main()