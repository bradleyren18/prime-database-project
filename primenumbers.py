# print(2)
# print(3)

def is_prime(number):
    if number % 6 == 1 or number % 6 == 5:
        if num_of_factors(number) == 2:
            return True
    return False

def num_of_factors(number):
    factors = 0
    for i in range(1, int(number**0.5), 2):
        if number % i == 0:
            factors+=1
    return factors*2

def primes_below(start, limit):
    for i in range(start+1, limit):
        if is_prime(i) == True:
            with open("primes.csv", "a") as primes_file:
                primes_file.write(f"\n{i}")
            # print(i)

def get_last_prime():
    with open("primes.csv", "r") as primes_file:
        primes = sorted(primes_file, reverse=True)
        last_prime = primes[0]
    return int(last_prime)

primes_below(get_last_prime(), 10000000)