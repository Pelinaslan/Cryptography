import string
alphabet = string.ascii_lowercase

def caesar_Encryption(text,n):
    encrypted_message = ''

    for i in text:
        encrypted_message += alphabet[(alphabet.index(i)+n) % 26]

    print("The encrypted message is:", encrypted_message)

def ceaser_Decryption(text,n):
    dencrypted_message = ''

    for i in text:
        dencrypted_message += alphabet[(alphabet.index(i)-n) % 26]

    print("The dencrypted message is:", dencrypted_message)

n= int(input("Shift value:"))
text = input("Your message:").lower()

mood=False
while (mood==False):
    x=int(input("Do you want to encrypt(1) or decrypt(2) your message?"))

    if(x==1):
        caesar_Encryption(text,n)
        mood=True
    elif(x==2):
        ceaser_Decryption(text,n)
        mood=True
    else:
        print("Please enter a valid number..!")