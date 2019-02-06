#!/usr/bin/env python3
import sys
from itertools import islice, takewhile, permutations, starmap, count
from operator import mul
from functools import reduce

def problem1():
    return sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1, 1000)))

assert 233168 == problem1()

def fib(a, b):
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b

assert [1, 2, 3, 5, 8, 13] == list(islice(fib(1,2), 6))

def problem2():
    return sum(filter(lambda x: x % 2 == 0, takewhile(lambda x: x < 4000001, fib(1, 2))))

assert 4613732 == problem2()

def factors(n):
    i = 2
    factors = []
    while i <= n:
        if n % i == 0:
            factors.append(i)
            n /= i
        i += 1
    return factors

assert [2, 3] == factors(12)
assert [13] == factors(13)
assert [2, 3, 4] == factors(24)

def problem3():
    return max(factors(600851475143))

assert 6857 == problem3()

def is_palindrome(i):
    return str(i) == str(i)[::-1]

def problem4():
    return max(
            filter(is_palindrome,
                starmap(lambda a, b: a * b,
                    permutations(range(100, 1000), 2))))

assert 906609 == problem4()

def problem5():
    def is_divisble(i):
        for d in range(11, 20):
            if i % d:
                return False
        return True

    r = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 2

    return next(filter(is_divisble, count(r, 20)), 1)

assert 232792560 == problem5()

def problem6():
    s = sum(range(1, 101))
    ss = sum([i*i for i in range(1, 101)])
    return s*s - ss

assert 25164150 == problem6()

def is_prime(n):
    if n == 1 or n == 2:
        return True

    if not n & 1:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

assert is_prime(1)
assert is_prime(2)
assert is_prime(3)
assert not is_prime(4)
assert is_prime(7)

def primes(limit=1000000):
    yield 2
    sieve = [False, False] + [True] * (limit - 2)
    for i in range(3, limit, 2):
        if sieve[i]:
            yield i
            for j in range(i*i, limit, i * 2):
                sieve[j] = False

assert [2, 3, 5, 7, 11, 13] == list(islice(primes(), 6))

def problem7():
    return next(islice(primes(), 10000, 10001))

assert 104743 == problem7()

def partitions(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

assert [[1, 2], [3, 4]] == list(partitions([1, 2, 3, 4], 2))

def product(l):
    return reduce(mul, l)

assert 24 == product([1, 2, 3, 4])

def problem8():
    n = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

    m = 0
    for i in range(0, len(n) - 13):
        m = max(m, product(int(i) for i in n[i:i + 13]))

    return m

assert 23514624000 == problem8()

def problem9():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if a*a + b*b == c*c:
                return a * b * c

assert 31875000 == problem9()

def problem10():
    return sum(primes(2000000))

assert 142913828922 == problem10()
