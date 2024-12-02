import string
from itertools import product

def brute_force_attack(target_password):
    characters = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    for length in range(1, len(target_password) + 1):
        for guess_tuple in product(characters, repeat=length):
            guess = ''.join(guess_tuple)
            attempts += 1
            if guess == target_password:
                return f"Password found: {guess} in {attempts} attempts"
    return "Password not found"

def main():
    target_password = input("Enter the password to be cracked: ")
    result = brute_force_attack(target_password)
    print(result)

if __name__ == "__main__":
    main()
