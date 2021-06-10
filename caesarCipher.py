# Shift Cipher or Caesar Cipher is the process of replacing or substituting the alphabet or number
# by the one 2 places to the right of it. It doesn't have to be 2, it can be any much farther we want.

# Julius Caesar used to communicate with his guards this way. That's why it is called Caesar Cipher.

print("--------------------\n--------------------\n--------------------\n")
print("In this program, we will encrypt the plain text using Caesar Cipher.\n")
print("---------------------------------------------------------------------------------\n")

plainText = input("Enter the plain text to be encrypted:\n(It has to be alphanumeric!!Others won't be changed in this code)\n")
k = int(input("Enter the key value:(Number of places you want to shift the text)\n"))

cipherText = ""

for i in range(len(plainText)):
    ch = plainText[i]
    if ch.isalpha():
        ch = chr((ord(ch)%32 + k - 1)%26 + (ord(ch)//32)*32 + 1)
    elif ch.isnumeric():
        ch = chr((ord(ch) + k - 48)%10 + 48)
    cipherText = cipherText + ch

print("The encrypted text is:",cipherText)