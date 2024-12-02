import random

def load_words(file_path):
   
    with open(file_path, 'r') as file:
        words = file.read().splitlines()  # Read all lines into a list
    return words

def genPass(words, words_count=4):
   
    if len(words) < words_count:
        raise ValueError("Not enough words in the file to generate a password.")
    return ''.join(random.sample(words, words_count)) 

def main():
    
    dictionary_file = r'C:\Users\dimit\OneDrive\Desktop\pyth\listofrandomwords.txt'
    words = load_words(dictionary_file)
    password = genPass(words)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
