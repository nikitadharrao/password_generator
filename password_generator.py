import random
import string
import pyperclip  # 🔹 Added for clipboard support

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main
print("🔐 Random Password Generator")
length = int(input("Enter password length: "))
password = generate_password(length)
print("Your password is:", password)









