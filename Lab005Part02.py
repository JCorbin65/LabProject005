user_n = int(input("Enter a decimal number: "))

def decimal_to_binary(n):
    if n == 0:
        return ''
    else:
        return decimal_to_binary(n // 2) + str(n % 2)

def niszero(n):
    if n == 0:
        return n
    else:
        return decimal_to_binary(n)

print(niszero(user_n))

user_b = (input("Enter a binary integer: "))

def binary_to_decimal(b):
    if b == '':
        return 0
    else:
        return binary_to_decimal(b[:-1]) * 2 + int(b[-1])

print(binary_to_decimal(user_b))