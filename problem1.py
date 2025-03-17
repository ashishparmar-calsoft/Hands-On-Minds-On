
'''
https://projecteuler.net/problem=51
Problem :- (Prime Digit Replacements) By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family. '''

from collections import Counter


def To_replace(pattern):
    replaced_numbers = []
    for i in range(10):
        num = int(pattern.replace("*",str(i)))
        if check_prime(num):
            replaced_numbers.append(num)
    return replaced_numbers


def check_prime(number):
    if number<=1:
        return False

    sqrt = int((number**0.5)+1)
    for i in range(2,sqrt):
        if number%i==0:
            return False
    return True

pattern = "56**3"
if "*" not in pattern:
    print("This pattern has not 8 family prime numbers")
else:
    prime_numbers = To_replace(pattern)

def find_first_repeating_digit_number(numbers):
    """Find the first number where any digit appears two or more times."""
    for num in numbers:
        digit_counts = Counter(str(num))  # Count digit occurrences
        if any(count >= 2 for count in digit_counts.values()):  
            return num  # Return first number that meets the condition
    return None


if len(prime_numbers)>7:
    prime_numbers.sort()
    print(prime_numbers)
    print(find_first_repeating_digit_number(prime_numbers))
else:
    print("This pattern has not 8 family prime numbers")