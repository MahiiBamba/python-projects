# Random Password Generator (Beginner Level)

import random
import string

def main():
    print("Random Password Generator")
    print("========================")
    
    try:
        password_length = int(input("Enter desired password length: "))
        
        if password_length <= 0:
            print("Error: Password length must be a positive number.")
            return
        elif password_length < 4:
            print("Warning: Short passwords are not secure.")
        elif password_length > 50:
            print("Warning: Very long passwords might be hard to remember.")
            
    except ValueError:
        print("Error: Please enter a valid number for password length.")
        return
    
    print("\nSelect character types to include:")
    
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    if not (include_lowercase or include_uppercase or include_numbers or include_symbols):
        print("Error: You must select at least one character type.")
        return
    
    char_pool = ""
    if include_lowercase:
        char_pool += string.ascii_lowercase
    if include_uppercase:
        char_pool += string.ascii_uppercase
    if include_numbers:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation
    
    try:
        password = "".join(random.choice(char_pool) for _ in range(password_length))
        
        print("\nYour generated password is:")
        print(password)
        
        strength = "Weak"
        if password_length >= 8 and (include_lowercase + include_uppercase + include_numbers + include_symbols) >= 3:
            strength = "Strong"
        elif password_length >= 6 and (include_lowercase + include_uppercase + include_numbers + include_symbols) >= 2:
            strength = "Medium"
        
        print(f"Password strength: {strength}")
        
    except Exception as e:
        print(f"An error occurred while generating the password: {e}")

if __name__ == "__main__":
    main()