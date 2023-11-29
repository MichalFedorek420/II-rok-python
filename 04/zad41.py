def f(n):
    counter = 0
    prime_candidate = 10
    primes = []
    if n > 1:
        while counter < n:
            for i in range(2,prime_candidate):
                if prime_candidate % i == 0:
                    prime_candidate += 1
                    counter += 1
                    print(i)
f(10)
