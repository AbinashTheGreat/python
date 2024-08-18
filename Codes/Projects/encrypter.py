def welcome():
    print("-----------------------------------------------")
    print("-----Welcome--To--The-Encrypter----------------")
    print("-----------------------------------------------")

def menu():
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit The Program")


def encrypt():
    welcome()
    menu()
    def encrypter(target):
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        shift = 7
        encrypted_text = []
        for i in target.lower():
            index = alphabets.find(i)
            if index == -1:
                encrypted_text.append(i)
            else:
                # modular arithmetic it ensures if the the number exceeds 26 
                # then it returns the exceeded number or else just return 
                # the same number e.g 5%26 gives 5 but 28%26 gives 3
                new_index = (index + shift) % 26 
                encrypted_text.append(alphabets[new_index])
        print(encrypted_text)
    try:
        option = int(input("Please choose any option:=> "))
        if option == 1:
            st_enter = input("Please enter the text to encrypt:=> ")
            encrypter(st_enter)
        elif option == 2:
            print("Decryption not implemented yet.")
        elif option == 3:
            print("Exiting the program.")
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")
encrypt()
