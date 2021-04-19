import random
import math

def array(min,max,n):
    arr=[]
    while(len(arr)<n):
        num=random.randint(min+1,max)
        if(num>sum(arr)):
            arr.append(num)
            min=sum(arr)
            max=sum(arr)+10
    return arr

def ChoiseQandR(arr):
    total=sum(arr)
    q = random.randint(total+1,(total+1)+100)
    mood=False
    while(mood==False):
        r = random.randint(1,q-1)
        if (math.gcd(r, q) == 1):
            mood=True
    return q,r

def publicKey(arr,q,r):
    publicKey_arr=[]
    for num in arr:
        new_num=(num*r)%q
        publicKey_arr.append(new_num)
    return publicKey_arr

def Ascii_converter(text):
    message=[]
    for letter in text:
        ascii = ord(letter)
        message.append(ascii)
    return message

def Binary_converter(num,n):
    output = ""
    while (num > 0):
        output = "{}{}".format(num % 2, output)
        num = num // 2
    while (len(output) != n):
        output = "0" + output

    return output

#modular multiplicative inverse
def mod(e,lcm):
    x=pow(e, -1, lcm)
    return x

def sil(arr,num):
    list=arr[:]
    for i in arr:
        if(i>num):
            list.remove(i)
    return list

def MerkleH_Encryption(PKey,text,n):
    binary_txt=[]
    total_list=[]

    for i in text:
        txt=Ascii_converter(i)
        binary_txt.append(Binary_converter(txt[0],n))
    for i in binary_txt:
        total = 0
        for j in range(len(PKey)):
            total += PKey[j] * int(i[j])
        total_list.append(total)
    return total_list

def MerkleH_Decryption(q,r,ce,arr):
    Decryption_char = ""

    s=mod(r,q)

    for c in ce:
        Decryption_text = ""
        list = []
        new_arr = arr[:]
        c_rev=(c*s)%q

        while (c_rev!=0):
            new_arr=sil(new_arr,c_rev)
            maxi = max(new_arr)
            c_rev = c_rev - maxi
            list.append(maxi)
        for i in arr:
            for j in list:
                if (i == j):
                    Decryption_text += "1"
                    break
                if(i!=j and list.index(j)==2):
                    Decryption_text += "0"

        Decryption_num = int(Decryption_text, 2)
        Decryption_char += chr(Decryption_num)


    return Decryption_char


#Main
#arr=[2, 7, 11, 21, 42, 89, 180, 354]

n=8 #8 bit

arr=array(0,10,n)
print("Array =",arr)
q,r=ChoiseQandR(arr)
#q,r=881,588

PKey=publicKey(arr,q,r)
print("Public Key =",PKey)

c=MerkleH_Encryption(PKey,"Merhaba",n)
print("Encryption number:",c)
print("Decryption text:",MerkleH_Decryption(q,r,c,arr))



