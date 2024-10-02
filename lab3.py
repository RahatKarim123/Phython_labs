n = int(input("Enter a number: "))


if n <= 1:
    print(n, "is not prime")
else:
    i = 2
    prime = True
    while i < n:
        if n % i == 0:
            prime = False
            break
        i += 1

    if prime:
        print(n, "is prime")
    else:
        print(n, "is not prime")

