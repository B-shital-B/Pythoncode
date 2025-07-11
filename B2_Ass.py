# print("Enter 5 ele in list1:")
# list1=[int(input(f"Enter element in list:{i}")) for i in range(5)]
# print("Enter 5 ele in list2:")
# list2=[int(input(f"Enter element in list:{i}"))for i in range(5)]    
# if sorted(list1) == sorted(list2):
#     print("yes")
# else:
#    print("No")

# # Build dictionary from 5 individual inputs
def dictionary(name):
    freq = {}
    print(f"Enter 5 elements for {name}:")
    for i in range(5):
        val = int(input(f"Element {i+1}: "))
        freq[val] = freq.get(val, 0) + 1
    return freq

# Take input and create frequency dictionaries
dict1 = dictionary("dic 1")
dict2 = dictionary("dic 2")

# Compare both dictionaries
if dict1 == dict2:
    print("Yes")
else:
    print("No")



print("Enter 5 elements for Set 1:")
a1 = int(input("Element 1: "))
a2 = int(input("Element 2: "))
a3 = int(input("Element 3: "))
a4 = int(input("Element 4: "))
a5 = int(input("Element 5: "))

print("Enter 5 elements for Set 2:")
b1 = int(input("Element 1: "))
b2 = int(input("Element 2: "))
b3 = int(input("Element 3: "))
b4 = int(input("Element 4: "))
b5 = int(input("Element 5: "))

# Convert to sets
set1 = {a1, a2, a3, a4, a5}
set2 = {b1, b2, b3, b4, b5}

# Compare sets and lengths
if set1 == set2 and [a1, a2, a3, a4, a5].count(0) == [b1, b2, b3, b4, b5].count(0) and len([a1, a2, a3, a4, a5]) == len([b1, b2, b3, b4, b5]):
    print("Yes")
else:
    print("No")
