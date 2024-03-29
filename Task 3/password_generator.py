import random, string

def generate_password(len):
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for _ in range(len))
    return password

def main():
    print("Password Generator")

    while True:
        try:
            len = int(input("Enter the length of the password to generate: \n"))
            if len <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    password = generate_password(len)
    print("Generated Password is:\n", password)

if  __name__ == "__main__":
    main()