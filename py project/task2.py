import argparse
import secrets
import string


def generate_password(length, use_upper, use_lower, use_digits, use_special):
    # Validate the minimum length
    if length < 10:
        raise ValueError("Password length must be at least 10 characters.")

    # Build a character set based on user input
    character_set = ""

    if use_upper:
        character_set += string.ascii_uppercase
    if use_lower:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if not character_set:
        raise ValueError("You must select at least one type of character.")

    # Generate the random password
    password = "".join(secrets.choice(character_set) for _ in range(length))

    return password

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    digits = input("Include digits? (yes/no): ").lower() == 'yes'
    special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    try:
        password = generate_password(length, uppercase, lowercase, digits, special_chars)
        print("Generated Password:", password)
    except ValueError as e:
        print(e)