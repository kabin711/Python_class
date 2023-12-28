
# First Method
def Vowel(result):
    if result == 'a':
        print("vowel")
    elif result == 'e':
        print("vowel")
    elif result == 'i':
        print("vowel")
    elif result == 'o':
        print("vowel")
    elif result == 'u':
        print("vowel") 
    else:
        print("not y")


char_1 = input("Enter your alphabet: ")
print(Vowel(char_1))

# Alternative method
def is_vowel(res):
    if res in ['a','e','i','o','u']:
        print("vowel")
    elif res == 'y':
        print("Not vowel")
    else:
        print("Neither vowel nor consonant")

input_1 = input("Enter your alphabet: ")
print(is_vowel(input_1))
