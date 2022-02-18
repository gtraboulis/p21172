import ast

# Reading file
with open("dictionaries.txt") as f:
    dict_strings = f.readlines()

# Turning strings into dictionaries
dicts = []
for i in dict_strings:
    dicts.append(ast.literal_eval(i))

# Making list of keys
keys = []
for i in dicts:
    for j,k in i.items():
        if j not in keys:
            keys.append(j)

# Asking user to select a key
select_key = False
while select_key == False:
    print(keys)
    select_key = input("Select a key from the above list:")

    if select_key not in keys:
        print("\nKey is not one of the options. Try again.") #New line for readability
        select_key = False
        
# Making list of values corresponding to key
val =[]
for i in dicts:
    val.append(i.get(select_key))

# Removing 'None' entries (only needed when keys are different between dictionaries)
values = [i for i in val if i]

maximum = max(values)
minimum = min(values)
mode =max(set(values), key=values.count) # Only outputs one value, not useful for multimodal distributions. Output is the smallest mode

print(maximum, minimum, mode)