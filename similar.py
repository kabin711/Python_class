def similar(random):
    random = ''.join(char *2 for char in random)
    return random


char_1 = input("Enter value: ")
result1 = similar(char_1)
print(result1)  

# result2 = similar("123a!")
# print(result2)  # Output: 112233aa!!
