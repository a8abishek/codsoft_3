#Password generator
import random
import string

def generate_password(length):
    letters = string.ascii_letters  
    digits = string.digits          
    special_chars = string.punctuation
    
    all_chars = letters + digits + special_chars

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    print("Password Generator")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password(min length should be 6): "))
            if length <= 5:
                print("Please enter a number greater than 5.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
