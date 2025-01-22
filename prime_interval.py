def primes_in_interval(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            primes.append(num)
    return primes
x=int(input("Enter the start of the interval: "))
y=int(input("Enter the end of the interval: "))

print(f"Prime numbers between {x} and {y}:", primes_in_interval(x, y))