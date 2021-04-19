import string
#alphabet = string.ascii_uppercase
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #j yok..

def create_matrix(key):
    matrix =[]
    liste = []
    key=key.upper()

    for i in range(5):
        for word in key:    #anahtarı gezer
            if word not in liste and word in alphabet: #listede yoksa ekler
                liste.append(word)
                if (len(liste)%5==0):
                    row=[]
                    for i in range(len(matrix)*5,len(liste)):
                        row.append(liste[i])
                    matrix.append(row)



        for word in alphabet:  #alfabeyi gezer
            if word not in liste: # listede yoksa ekler
                liste.append(word)
                if(len(liste)%5==0):
                    row = []
                    for i in range(len(matrix) * 5, len(liste)):
                        row.append(liste[i])
                    matrix.append(row)


    #for i in range(5):
    #    print(matrix[i])

    return matrix

def convert_text(text):
    text = text.upper().replace(" ", "")
    new_text = ""
    for i in range(len(text)):
        if (text[i] == text[i - 1]):
            new_text += 'X'
        new_text += text[i]
    if len(new_text) % 2 != 0:
        new_text += 'X'

    ##for output
    print("original text:",end="")
    for i in range(len(new_text)):

        if (i % 2 == 0):
            print(end=" ")
            print(new_text[i], end="")
        else:
            print(new_text[i], end="")
    #

    last_text = []
    print("\n")
    for i in range(0, len(new_text), 2):
        last_text.append(new_text[i:i + 2])

    return last_text



def  playfair_Encryption(text, key):
   playfair_Encryption=""
   text=convert_text(text)
   matrix=create_matrix(key)

   for i in text:
       for j in range(len(matrix)):
           if i[0] in matrix[j]:
              column = (matrix[j].index(i[0]))
              row = j

           if i[1] in matrix[j]:
              column2 = (matrix[j].index(i[1]))
              row2 = j

    #if the letters appear on the same row of your table
       # , replace them with the letters to their immediate right respectively
       if(row==row2):
           if(column==4):
               playfair_Encryption += matrix[row][0]
               playfair_Encryption += matrix[row2][column2 + 1]
           if (column2 == 4):
               playfair_Encryption += matrix[row][column + 1]
               playfair_Encryption += matrix[row2][0]
           else:
               playfair_Encryption += matrix[row][column+1]
               playfair_Encryption += matrix[row2][column2 + 1]


        #If the letters appear on the same column of your table
       # , replace them with the letters immediately below respectively
       elif(column==column2):
           if (row == 4):
               playfair_Encryption += matrix[0][column]
               playfair_Encryption += matrix[row2+1][column2]
           if (row2 == 4):
               playfair_Encryption += matrix[row+1][column]
               playfair_Encryption += matrix[0][column2]
           else:
               playfair_Encryption += matrix[row+1][column]
               playfair_Encryption += matrix[row2+1][column2]

       #If the letters are not on the same row or column
       # , replace them with the letters on the same row respectively
       # but at the other pair of corners of the rectangle defined by the original pair.
       else:
           playfair_Encryption += matrix[row][column2]
           playfair_Encryption += matrix[row2][column]


   print("Encryption text:",end="")
   for i in range(len(playfair_Encryption)):
       if (i % 2 == 0):
           print(end=" ")
           print(playfair_Encryption[i], end="")
       else:
           print(playfair_Encryption[i], end="")
   print("\n")



def  playfair_Decryption(text, key):

   playfair_Decryption=""
   matrix=create_matrix(key)

   last_text = []
   for i in range(0, len(text), 2):
       last_text.append(text[i:i + 2])
   text=last_text

   for i in text:
       for j in range(len(matrix)):
           if i[0] in matrix[j]:
              column = (matrix[j].index(i[0]))
              row = j
           if i[1] in matrix[j]:
              column2 = (matrix[j].index(i[1]))
              row2 = j


       if(row==row2):
           if(column==0):
               playfair_Decryption += matrix[row][4]
               playfair_Decryption += matrix[row2][column2 - 1]
           if (column2 == 0):
               playfair_Decryption += matrix[row][column - 1]
               playfair_Decryption += matrix[row2][4]
           else:
               playfair_Decryption += matrix[row][column - 1]
               playfair_Decryption += matrix[row2][column2 - 1]



       elif(column==column2):
           if (row == 0):
               playfair_Decryption += matrix[4][column]
               playfair_Decryption += matrix[row2-1][column2]
           if (row2 == 0):
               playfair_Decryption += matrix[row-1][column]
               playfair_Decryption += matrix[4][column2]
           else:
               playfair_Decryption += matrix[row-1][column]
               playfair_Decryption += matrix[row2-1][column2]

       else:
           playfair_Decryption += matrix[row][column2]
           playfair_Decryption += matrix[row2][column]


   print("Decryption text:",end="")
   for i in range(len(playfair_Decryption)):
       if (i % 2 == 0):
           print(end=" ")
           print(playfair_Decryption[i], end="")
       else:
           print(playfair_Decryption[i], end="")




#INPUT
playfair_Encryption("Hide the gold in the tree stump","Playfair Example")
playfair_Decryption("BMODZBXDNABEKUDMUIXMMOUVIF","Playfair Example")


#OUTPUT
"""
original text: HI DE TH EG OL DI NT HE TR EX ES TU MP

Encryption text: BM OD ZB XD NA BE KU DM UI XM MO UV IF

Decryption text: HI DE TH EG OL DI NT HE TR EX ES TU MP
"""