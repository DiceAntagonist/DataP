def main():
    choice = int(input("1 for Encrypt/ 0 for Decrypt"))
    x = input("Enter text:")
    key = int(input("Enter key"))
    finaltext = ""
    
    if (choice == 1):
        for i in x:
             a = ord(i) + key
             finaltext = finaltext + chr(a)
             print(finaltext)
       
    elif (choice == 0):
        for i in x:
            a = ord(i) - key
            finaltext = finaltext + chr(a)
            print(finaltext)
            
    else:
        print("Incorrect Choice")
    
    
    
main()
