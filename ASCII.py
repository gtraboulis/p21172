def binary(string_in):
    # Converts ASCII characters in input string to 7-bit binary and keeps first 2 and last 2 bits
    j, k = [], []
    for i in string_in:
        j.append(ord(i)) # ASCII number of letter
    for i in j:
        k.append(bin(i)[2:].zfill(7)) # 7-bit binary of ASCII number, excluding 0b
    
    for i in range(len(k)):
        j[i] = k[i][:2] + k[i][-2:]
    
    return j # List of 4-bit binary numbers as strings

def bin_to_int(list_in):
    # Converts list of binary strings to 16-bit integers and discards excess digits
    string = ""
    for i in list_in:
        string = string + i
    
    while len(string) % 16 != 0:
        string = string[:-1]
    
    no_numbers = int(len(string) / 16)
    numbers = []
    for i in range(no_numbers):
        numbers.append(int(string[16*i:16*(i+1)], 2)) # Selects 16-bit blocks and converts to decimal
    
    return numbers

# Reading input file
with open("ASCIItext.txt") as f:
    text = f.read()
    
numbers = bin_to_int(binary(text))
divisors = [2, 3, 5, 7, 10]
percentages = []

# Finding percentage of numbers divided exactly by each divisor
for a in divisors:
    counter = 0
    for b in numbers:
        if b % a == 0:
            counter += 1
    percentages.append(100 * counter / len(numbers))

for i in range(len(divisors)):
    print("Percentage of numbers divisible by {} is {:.3f}".format(divisors[i], percentages[i]))