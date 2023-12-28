# fruits = ["apple" , "banana"]
# fruit = ["gauva"]
# index_of_apple = fruits.index("apple")
# print(index_of_apple)
# fruit.extend(fruits)
# print(fruit)

# # List comprehensive
# squares = [x**2 for x in range(1, 6)]
# print(squares)

# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)


# # input value
# num1 = input("Enter first number: ")

# # tuple
# # fruits =("apple" , "banana")
# # (red , *yellow) = fruits
# # print(red)
# # print(yellow)

# function

def demoadd(num1,num2):
    total = num1 + num2
    return total

print("Adding two number: ")
result = demoadd(3,5)
print(result)


def listadd(numbers):
    total = 0
    for n in numbers:
        if n % 2 != 0:
            total = total + n
    return total
    
numbers = [1,2,3,4,5,6]
print("Adding all element of list: ")
print(listadd(numbers))




