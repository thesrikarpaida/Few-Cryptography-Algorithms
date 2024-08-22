# ROT-13 or Rotate13 is a simple substitution cipher where we replace a letter with the 13th letter after it in the alphabet.
# This cipher works on alphabets only.


print("--------------------\n--------------------\n--------------------\n")
print("In this program, we will encrypt the plain text using ROT-13 Cipher.\n")
print("---------------------------------------------------------------------------------\n")

plainText = input("Enter the plain text to be encrypted:\n")

cipherText = ""

for i in range(len(plainText)):
    ch = plainText[i]
    if ch.isalpha():
        ch = chr((ord(ch)%32 + 13)%26 + (ord(ch)//32)*32)
    cipherText += ch

print("The encrypted text is:", cipherText)
