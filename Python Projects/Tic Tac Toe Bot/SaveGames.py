# Writing the code to save the position of the board, and make the position of board.

import math


def find_prime_numbers(N):
    prime = [True for i in range(N+1)]
    p = 2
    while p*p <= N:
        if prime[p] == True:
            for i in range(p*p, N+1, p):
                prime[i] = False
        p += 1
    PRIMES = [p for p in range(2, N+1) if prime[p]]
    return PRIMES


def find_factors(number):
    factors = {}
    for i in range(2, round(math.sqrt(number))):
        power = 0
        while number % i == 0:
            power += 1
            number /= i
        if power > 0:
            factors[i] = power
    return factors


def convert_board_to_number(BOARD=[]):
    # Board is a list consisting of n*2 elements, n being the number of rows and columns of the size of the board
    # We need 2*n^2 prime numbers for our code, and we're assuming N <= 7, in that case, we will just need the first 100 prime numbers, and to do that, we're gonna use
    # The SieveOfEratosthenes, and we know that we can get the first 100 prime numbers in under 1000

    PRIMES = find_prime_numbers(1000)
    # This ensures we have 2*n^2 elements, as a board is always going to have n^2 elements.
    PRIMES = PRIMES[:2*len(BOARD)]
    x_primes = PRIMES[:len(BOARD)]
    o_primes = PRIMES[len(BOARD):]

    NUMBER = 1

    for index, element in enumerate(BOARD):
        if element == "X":
            NUMBER *= x_primes[index]
        elif element == "O":
            NUMBER *= o_primes[index]

    return NUMBER


def convert_number_to_board(NUMBER, N):
    # Where N is the number of rows/columns of the board.
    factors = find_factors(NUMBER)

    PRIMES = find_prime_numbers(1000)
    PRIMES = PRIMES[:2*N*N]
    x_primes = PRIMES[:N*N]
    o_primes = PRIMES[N*N:]

    BOARD = [['-']*N for i in range(N)]

    for factor in factors.keys():
        if factor in x_primes:
            index = x_primes.index(factor)
            BOARD[index//N][index % N] = "X"
        elif factor in o_primes:
            index = o_primes.index(factor)
            BOARD[index//N][index % N] = "O"

    return BOARD


def main():
    x = convert_board_to_number([
        'X', 'O', '_',
        'X', 'X', 'X',
        'O', 'O', 'X'
    ])
    print(x)

    x = convert_number_to_board(x, 3)
    print(x)


if __name__ == "__main__":
    main()
