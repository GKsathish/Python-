def Roman(number):
    numbers = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}
    rom = ""
    for key in numbers.keys():
        count = int(number / key)
        rom += numbers[key] * count
        number -= key * count
    return rom


n = int(input())
print(Roman(n))