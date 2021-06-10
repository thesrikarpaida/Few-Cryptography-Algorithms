# Affine Cipher encryption is the process of encrypting the data by multiplying each character
# with a key in Zn* and then adding a key in Zn.

print("--------------------\n--------------------\n--------------------\n")
print("In this program, we will encrypt the plain text using Affine Cipher.\n")
print("---------------------------------------------------------------------------------\n")

plainText = input("Enter the text (only alphabets) you want to encrypt:\n")
k1, k2 = input("Enter the key pair (space separated):").split() # k1 is multiplied and k2 is added

k1, k2 = int(k1), int(k2)
cipherText = ""

for i in range(len(plainText)):
    ch = plainText[i]
    ch = chr(((ord(ch)%32 - 1)*k1 + k2)%26 + (ord(ch)//32)*32 + 1)
    # The above single line can replace the below 2 if conditions that have been quoted
    '''
    if ch.islower():
        ch = chr(((ord(ch) - 97)*k1 + k2)%26 + 97)
    elif ch.isupper():
        ch = chr(((ord(ch) - 65)*k1 + k2)%26 + 65)
    '''
    #elif ch.isnumeric():
        #ch = chr((ord(ch)*k1 + k2 - 48)%10 + 48)
    cipherText = cipherText + ch

print("The encrypted text is:",cipherText)