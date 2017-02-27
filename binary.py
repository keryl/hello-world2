def binary_converter(num):
 
    if not (0 <= num <= 255):
        return 'Invalid input'
 
    binary = ''
 
    while True:
 
        quotient = num / 2
        rem = num % 2
 
        if rem == 0:
            binary = '0' + binary
 
        else:
            binary = '1' + binary
 
        if quotient == 0:
            return binary
        else:
            num = quotient

