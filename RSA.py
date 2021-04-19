import math  # for gcd
import random


#prime list
def prime_list(num):
    prime_numbers=[]
    for n in range(num + 1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                prime_numbers.append(n)
    return prime_numbers

# This function computes LCM
def Lcm(x, y):
   lcm = (x*y)//math.gcd(x,y)
   return lcm

def Choise_E(lcm):
    nprime_num=[]
    list=prime_list(lcm)          #list of prime numbers
    for i in range(1, lcm):
        liste.append(i)           #general list

    for eleman in nprime_num:
        nprime_num.remove(eleman) #list of non-prime numbers


    durum=False
    while(durum==False):
        i=random.choice(list)
        if(math.gcd(i,lcm)==1):     #Retrieves a random element from a list of prime numbers.
            e=i
            durum=True
        else:
            sayi = random.choice(liste)       # Retrieves a random element from a non-prime list.
            if (math.gcd(sayi, lcm) == 1):
                e = sayi
                durum=True

    return e

#modular multiplicative inverse
def mod(e,lcm):
    x=pow(e, -1, lcm)
    return x


"""#alternative modular multiplicative inverse### 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

"""

#converts the string to an ascii character
def Ascii_converter(text):
    message=[]
    for letter in text:
        ascii = ord(letter)
        message.append(ascii)
    return message

def RSA_Encryption(text):
    print("original text:",text)
    c_message = Ascii_converter(text)
    encrypted_message = []

    for m in c_message:
        c = (m ** e) % n
        encrypted_message.append(c)

    return encrypted_message

def RSA_Decryption(text):
    D_text = []
    for c in text:
        m = (c ** d) % n
        D_text.append(chr(m))

    Decryption_text=""
    for i in D_text:
        Decryption_text += i


    return Decryption_text


liste=prime_list(100)
# 1) We will choose 2 prime numbers
p=random.choice(liste)
q=random.choice(liste)
print("p = "+str(p) +" " "q = "+str(q))

#################################
# 2) n = p * q
n= p*q
#print("n = ",n)
#################################
# 3) λ(n) = lcm(p − 1, q − 1)
lcm=Lcm(p-1,q-1)
print("lcm = ",lcm)
#################################
#4) 1 < e < λ(n) and gcd(e, λ(n)) = 1

e=Choise_E(lcm)
#print("e = ", e)

#################################

# 5) d**e ≡ 1 (mod λ(n))
d=mod(e,lcm)
#print("d = ", d)

#################################


print("(n="+str(n)+",e="+str(e)+") --> Public Key")
print("(n="+str(n)+",d="+str(d)+") --> Private Key")
text=RSA_Encryption("pelin")
print("Encryption text:",text)
print("Decryption text:",RSA_Decryption(text))






