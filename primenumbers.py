def is_prime(number):
    if number % 6 == 1 or number % 6 == 5:
        if prp(number) == True:
            if num_of_factors(number) == 2:
                return True
    return False

def num_of_factors(number):
    factors = 0
    for i in range(1, int(number**0.5)+1, 2):
        if number % i == 0:
            factors+=1
    return factors*2

def primes_below(start, limit):
    for i in range(start+1, limit):
        if is_prime(i) == True:
            with open("primes.csv", "a") as primes_file:
                primes_file.write(f"\n{i}")

def prp(pp):
    if pp % 2 == 1:
        npp = factorise(pp-1)
        s = npp[0]
        d = npp[1]
        a = 2
        bool1 = (a**d) % pp == 1
        bool2 = (a**d) % pp == -1

        if bool1 == True or bool2 == True:
            return True
        return False


def factorise(number):
    power_of_2 = 0
    remainder = 0
    while number % 2**power_of_2 == 0:
        power_of_2 += 1
    power_of_2 -= 1
    remainder = number % 2**power_of_2

    return [power_of_2, remainder]

def get_last_prime():
    with open("primes.csv", "r") as primes_file:
        primes = primes_file.readlines()
        last_prime = list(primes)[-1]
    return int(last_prime)

primes_below(get_last_prime(), 100000000)