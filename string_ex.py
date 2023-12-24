str1 = "This is Python test "
int1 = 45
str2 = "FILE"
# string type
print(type(str1),type(int1))

# string method
print(str1.upper())
print(str1.lower())
print(str1.strip())
print(str1.replace("T","f"))
print(str1.split())
print(str1[1:7])   # Slicing
print(str2[:2])
print(str2[2:])
print(str2[:-2])
print(str2[-2:])
print(str1[6:-4])
print(str1[-6:-4])
print(str1[5])  # indexing
print(str1+ "   " +str2)
print(str1.isupper())
print(str2.islower())
print(str2.isdigit())
print(str1.isalpha())
print(str1.isalnum())
print(str1.istitle())
print(str1.find("T"))







# String format
print(f" {str1}", int1, f'{str2}')




