import string
alphabet = string.ascii_uppercase

def Key_generation(text, key):
    key = list(key)
    if len(text) == len(key):
        return (key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return key


def vigenere_Encryption(text, key):
    encrypted_message =''

    for i in range(len(text)):
        encrypted_message += alphabet[(alphabet.index(text[i])
                                       + alphabet.index(key[i])) % 26]

    print("The encrypted message is:", encrypted_message)



# original text
def vigenere_Decryption(cipher_text, key):
    dencrypted_message = ''
    for i in range(len(cipher_text)):
        dencrypted_message += alphabet[(alphabet.index(cipher_text[i])
                                        - alphabet.index(key[i]) +26) % 26]

    print("The dencrypted message is:", dencrypted_message)


text = input("Your message:").upper()
keyword= input("Key:").upper()
key = Key_generation(text, keyword)


mood=False
while (mood==False):
    x=int(input("Do you want to encrypt(1) or decrypt(2) your message?"))

    if(x==1):
        vigenere_Encryption(text,key)
        mood=True
    elif(x==2):
        vigenere_Decryption(text,key)
        mood=True
    else:
        print("Please enter a valid number..!")

