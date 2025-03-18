
# https://projecteuler.net/problem=301
def nim_game(size_of_heap):
    xor_result = size_of_heap ^ 2* size_of_heap ^ 3* size_of_heap

    if xor_result ==0:
        return "First player will lose."
    else:
        return "First player can win."

n = int(input("Enter the heap size :>>>   "))
print(nim_game(n))
