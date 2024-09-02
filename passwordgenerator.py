import string
import random

def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''
    
    # Combine all selected character sets
    all_chars = lowercase_chars + uppercase_chars + numbers + special_chars
    
    if not all_chars:
        raise ValueError("At least one character type must be selected")
    
    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def main():
    # Get user input
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        # Generate and print the password
        password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
        print(f"Generated Password: {password}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
