#!/bin/python3

# Shift Cipher or Caesar Cipher is the process of replacing or substituting the alphabet or number
# by the one 3 places to the right of it. It doesn't have to be 3, it is just the default, it can be any much farther we want.

# Julius Caesar used to communicate with his guards this way. That's why it is called Caesar Cipher.


def banner():
    print("--------------------\n--------------------\n--------------------\n")
    print("In this program, we will encrypt the plaintext using Caesar Cipher.\n")
    print("---------------------------------------------------------------------------------\n")

def encryptCaesar():

    banner()

    plainText = input("Enter the plaintext you wish to encrypt:\n(Only alphanumeric characters will be converted to ciphertext. Other special characters stay the same!)\n")
    key = int(input("Enter the key value (integer):\n(Shift by how many places, defaults to 3)\n").strip() or "3")

    cipherText = ""

    for i in range(len(plainText)):
        ch = plainText[i]
        if ch.isalpha():
            ch = chr((ord(ch)%32 + key - 1)%26 + (ord(ch)//32)*32 + 1)
        elif ch.isnumeric():
            ch = chr((ord(ch) + key - 48)%10 + 48)
        cipherText += ch
    
    print(f"Original Plaintext: {plainText}")
    print(f"Encrypted Ciphertext: {cipherText}")


if __name__ == "__main__":
    encryptCaesar()