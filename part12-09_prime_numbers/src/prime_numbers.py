# Write your solution here
def prime_numbers():
    primes = []  # store primes found so far
    num = 2      # start generating from 2 upward

    while True:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            yield num

        num += 1

if __name__ == '__main__':   
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))    
