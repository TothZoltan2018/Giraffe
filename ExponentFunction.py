print(2 ** 4)
print(pow(2, 4))


# A fentieket sajat fgv-el
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result

print(raise_to_power(2, 5))
