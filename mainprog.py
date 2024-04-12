# Myiah Stubbs
def encode(ogpass):
    # creating string to put encoded password(ecdpass) result
    ecdpass = ''
    # each num in the original password(ogpass)
    for item in ogpass:
        # adding 3 to num
        a = int(item) + 3
        # if num goes over 9, loops back to 0
        if a > 9:
            ecdpass += str(a - 10)
        # otherwise just puts the num
        else:
            ecdpass += str(a)
    return ecdpass
 def decode(ecdpass):
    ogpass = ''
    
    for char in ecdpass:
        
        a = int(char) - 3
        
        if a < 0:
            ogpass += str(a + 10)
        
        else:
            ogpass += str(a)
    return ogpass


def main():
    option = 0
    while option != 3:
        # menu
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n"
              "")
        # ask for menu option
        option = int(input("Please enter an option: "))
        # encoder
        if option == 1:
            ogpass = input("Please enter your password to encode: ")
            ecdpass = encode(ogpass)
            print("Your password has been encoded and stored!\n"
                  "")
        # decoder
        elif option == 2:
            if ecdpass:
                ogpass = decode(ecdpass)
                print(f"The encoded password is {ecdpass}, and the original password is {ogpass}.\n")
            else:
                print("No password has been encoded yet.\n")
        # Exit condition
        elif option == 3:
            print("Exiting program.")
        else:
            print("Invalid option, please choose again.\n")

if __name__ == '__main__':
    main()
