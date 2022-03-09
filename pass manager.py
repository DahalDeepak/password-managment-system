    #encryption part ciser cypher depend on shift
from ctypes import sizeof


def encrypt (password, shift): 
    encrypted = ""
    for i in range (len(password)):
        char = password[i]
        if (char.isupper()):
            encrypted += chr((ord(char) + shift - 65) % 26 + 65)
        elif (char.isdigit()):
            newNum = (int(char) + shift) % 10
            encrypted += str(newNum)
        elif (char.islower()):
            encrypted += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted += char
    return encrypted
def decrypt (password, shift): #defining decryptor
    decrypted = ""
    for i in range(len(password)):
        char = password[i]
        if (char.isupper()):
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        elif (char.isdigit()):
            originalNum = (int(char) - shift) % 10
            decrypted += str(originalNum)
        elif (char.islower()):
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            decrypted += char
    return decrypted

#file = open("password.txt","r")
##file.close()

print("Welcome to password manager application")
password_input = input("Enter pin for password manger: ")
if password_input == "1":
  
  print("correct")
 #Fror menu
  menu = ""
  while (menu != '1' or menu != '2'):
    menu= input("Looking for a password or saving a new one?"
             "\n1. Input new password"
             "\n2. View saved passwords"
             "\n3. Exit \n")
    if (menu=='1'):
        softwareName=input("Enter the name of the software you are using.")
        username = input("Enter your username for this software.")
        password = input("Enter your password for this software.")
        shift = 2             #sifter value is 2

        f = open("securePasswordFile.txt", "a")
        f.write(encrypt(softwareName,shift)+";|"+encrypt(username,shift)+";|"+encrypt(password,shift)+"\n")
        f.close()
        print("Data encrypted and saved to file.")
    if (menu == '2'):
        #Functionality for Viewing saved passwords.
     
        print("Decrypting data in file")
        f = open("securePasswordFile.txt", "r")
        
        print("  Software\t Username\t Password\n")
        
        for x in f:
            shift = 2
            oneResult = x.split(";|")
            print("|",decrypt(oneResult[0], shift)+"\t\t "+decrypt(oneResult[1], shift)+"\t\t "+decrypt(oneResult[2] , shift))
            
        f.close()
        
    if (menu == '3'):
      exit()
else: 
  print("you have incorrect pin or master key")
