import math
import os 
import random
import time
import numpy
import urllib.request
# Global Variables
upperLetters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lowerLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
specials = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']',
    '{','}',':',';','\"',"\'",'.','<','>','?','/','|','\\','~','`']
allTogetherNow = numpy.concatenate((upperLetters, lowerLetters, numbers, specials))

if not os.path.isfile('commonPasswords.txt'): # Downloads the list of known common passwords, if the file does not exist.
    doDownload = input("Do you want to download the list of known common passwords? ").lower() # For security/privacy reasons it only downloads it with the users approval
    if(doDownload == "yes" or doDownload == "y"):
        print('Downloading starting.. \nPlease wait. This may take longer depending on your connection')
        txt = urllib.request.urlopen("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")
        with open('commonPasswords.txt','wb') as output:
            output.write(txt.read())
        print('Download Complete!')
        time.sleep(1)
    elif(doDownload == "no" or doDownload == "n"):
        print('Skipping download..')
        time.sleep(1)

space = "\n" * 50
# Prints many spaces to clear the terminal/interperter
print(space)
def calculateEntropy(password): # Calculates the entropy depending on what characters are in the password and the length of the password
    pool_size = 0
    for L in upperLetters:
        if L in password:
            pool_size += 26
    for l in lowerLetters:
        if l in password:
            pool_size += 26
    for n in numbers:
        if n in password:
            pool_size += 10
    for sus in specials:
        if sus in password:
            pool_size += 32
    E = math.log2(pool_size ** len(password))
    return E

def generatePassword(length): # Generates a password with a specfied length
    password = ""
    for i in range(length):
        password += allTogetherNow[random.randint(0,len(allTogetherNow)-1)]
    return password
def checkIfEasyPassword(password): # Open a text file of common passwords and check if the provided password is in there
    try:
        file = open('commonPasswords.txt', 'r')
        fileContents = file.read()
        if password in fileContents:
            return True
    except FileNotFoundError:
        return "Unable to check. File Missing."
    return False
def menu(): # Shows the main menu and asks the user for input
    print("1. Generate Password\n2. Calcuate Entropy of Password\n3. About and Important Information\n4. Quit")
    try:
        selection = int(input("Please select your choice(1,2,3,4): "))
        completeSelection(selection)
    except TypeError:
        print("Please Input a number and try again. ")    
def completeSelection(selection): # Takes the main menu number and completes the selected action
    print(space)
    if(selection <= 0):
        print("Please enter a number and try again.")
    elif(selection == 1): # Generate Password, Check for entropy, and check if its in file of common passwords
        try:
            pswLength = int(input("What would you like the length of your password to be? "))
        except ValueError:
            print("Please Enter a number and try again.")
            selection(1)
            return
        psw = generatePassword(pswLength)
        entropy = calculateEntropy(psw)
        print("Entropy: " + str(round(entropy,2)))
        print("Length: " + str(len(psw)))
        print("Password: " + psw)
        print("Password is in list of known passwords: " + str(checkIfEasyPassword(psw)))
    elif(selection == 2): # Ask user for password and calculate entropy
        uPSW = input("Please enter the password to calculate the entropy(strenth) of your password: ")
        entropy = round(calculateEntropy(uPSW),2)
        print("Entropy: " + str(round(entropy,2)))
        print("Length: " + str(len(uPSW)))
        print("Password: " + uPSW)
        print("Password is in list of known passwords: " + str(checkIfEasyPassword(uPSW)))
    elif(selection == 3): # Show information about this program
        print("This program was made in Janurary of 2023\nBy: Christian Francis\n\nRemember entropy isn\'t the be all and end all of password security\nUse https://haveibeenpwned.com/ to check if your password appeared in any data leaks\nCheck if your password is in any lists of known easy to guess passwords.")
    elif(selection == 4): # Stop execution of this program
        quit()
    else:
        print("Unreconized selection please try again.")
    print("\n------\n")
while True: 
    menu()