# Vigenere Cipher is the cipher text which is formed using the key that is a x character key word

print("--------------------\n--------------------\n--------------------\n")
print("In this program, we will encrypt the plain text using Vigenere Cipher.\n")
print("---------------------------------------------------------------------------------\n")

plainText = input("Enter the plain text to be encrypted:\n")
print("\n\n")
key = input("Enter the key string used to encrypt the text:\n")

n = len(key)
keyVals = [(ord(i)%32 - 1) for i in key]
cipherText = ""

for i in range(len(plainText)):
    ch = plainText[i]
    if ch.isalpha():
        ch = chr((ord(ch)%32 + keyVals[i%n] - 1)%26 + (ord(ch)//32)*32 + 1)
    elif ch.isnumeric():
        ch = chr((ord(ch) +keyVals[i%n] - 48)%10 + 48)
    cipherText += ch

print("The cipherText is:", cipherText)
