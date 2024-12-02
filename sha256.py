import hashlib
 def hash_password(password):
    sha256 = hashlib.sha256()
    return sha256.hexdigest()
 password = input("Enter your password: ")
 hashed_password = hash_password(password)
 print(f"SHA-256 Hashed Password: {hashed_password}”)
