import secrets
import string

def rand_pass(length=16):
    characters = string.ascii_letters + string.digits +string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

random_password = rand_pass()
print('Randmon Generated Password is: ', random_password)