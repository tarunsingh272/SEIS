# h6_3.py

def fibonacci(N):
    if N <= 1:
        return N
    return fibonacci(N-1) + fibonacci(N-2)

def main():
    num = int(input("Enter the integer N: "))
    print(fibonacci(num))

main()