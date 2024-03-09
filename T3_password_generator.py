import random
import string

def generate_password(length=12, include_digits=True, include_special_chars=True):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    if length < 1:
        raise ValueError("Password length must be at least 1")

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))

        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
        password = generate_password(length, include_digits, include_special_chars)
        print("Generated Password:", password)

    except ValueError as e:
        print(f"Error: {e}")
