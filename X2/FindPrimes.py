class FindPrimes:

    def __init__(self):
        self._PrimeToFind = 100
        self._MaxPrime = 15000

    def get_prime_to_find(self):
        prime = -1
        while (prime < 0) & (prime < self._MaxPrime):
            response = input("What is the largest prime you wish to find?")

            try:
                prime = int(response)  # TODO BEN handle non numeric entries

                #self._MaxPrime = prime
                self._PrimeToFind = prime
            except ValueError:
                print("Enter a numeric value")
                prime = -1

    def nth_prime(self, n):
        count = 1
        last_prime = 2
        next_num = 3
        while count < n:
            if len(calculatefactors(next_num)) == 1:
                last_prime = next_num
                count += 1
            next_num += 2 #check odd numbers, started at 2
        return last_prime


def calculatefactors(n):
    primes = []
    for i in range(2, n+1):
        if n % i == 0:
            primes.append(i)
    return primes


