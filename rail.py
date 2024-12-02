def encrypt(text, key):
  
    rails = []
    for i in range(key):
        rails.append('') 

    down = True  
    r = 0 

    for char in text:
        rails[r] += char  
        if r == 0:
            down = True  
        elif r == key - 1:
            down = False 
        r += 1 if down else -1  

    return ''.join(rails)  


def decrypt(cipher, key):
   
    rails = []
    for i in range(key):
        rails.append('') 
    lengths = [0] * key  
    down = True
    r = 0

  
    for _ in cipher:
        lengths[r] += 1
        if r == 0:
            down = True
        elif r == key - 1:
            down = False
        r += 1 if down else -1

   
    idx = 0
    for i in range(key):
        rails[i] = cipher[idx:idx + lengths[i]]
        idx += lengths[i]


    plain = []
    down = True
    r = 0
    pos = [0] * key

    for _ in cipher:
        plain.append(rails[r][pos[r]])
        pos[r] += 1
        if r == 0:
            down = True
        elif r == key - 1:
            down = False
        r += 1 if down else -1

    return ''.join(plain)


if __name__ == "__main__":
    print("Rail Fence Cipher")
    mode = int(input("Choose mode: 1 for encrypt, 0 for decrypt: "))
    text = input("Enter the text: ")
    key = int(input("Enter the key (number of rails): "))

    if mode == 1:
        result = encrypt(text, key)
        print(f"Encrypted Text: {result}")
    elif mode == 0:
        result = decrypt(text, key)
        print(f"Decrypted Text: {result}")
    else:
        print("Invalid mode. Please choose 1 for encrypt or 0 for decrypt.")
