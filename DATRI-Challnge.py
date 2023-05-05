import random
from random_word import RandomWords
import os
def string(x):
    res = ""
    for i in x:
        res += i
    return res


def Transpose(A,key):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    #print(A)
    return rotate(A,key)


def Insertion(x,key):
    res = ""
    count = 0
    for i in x:
        if count % 2 == 0:
            for j in i:
                res += chr(128000 + ord(j))
        else:
            for j in i[::-1]:
                res += chr(128500 + ord(j))
    key2=""
    for i in range(4):
        key2+=str(random.randrange(0,9))
        
    for i in key2:
        res+=chr(128000+ord(i))
    #print(res)
    return (res,key,key2)


def Assignment(x,key):
    closest_square = 0
    i = 1
    while True:
        if i ** 2 > len(x):
            break
        else:
            i += 1
    closest_square = i ** 2
    x+=" "*(closest_square-len(x))
    matrix = []
    sub_matrix = []
    for j in x:
        if len(sub_matrix) != i:
            sub_matrix.append(j)

        if len(sub_matrix)==i:
            matrix.append(sub_matrix)
            sub_matrix = []
    #for i in matrix:
        #print(i)
    return Transpose(matrix,key)
def rotate(matrix,key):
    for i in range(2):
          temp_matrix = []
          column = len(matrix)-1
          for column in range(len(matrix)):
             temp = []
             for row in range(len(matrix)-1,-1,-1):
                temp.append(matrix[row][column])
             temp_matrix.append(temp)
          for i in range(len(matrix)):
             for j in range(len(matrix)):
                matrix[i][j] = temp_matrix[i][j]
    return Insertion(matrix, key)



def Designation(x):
    replacements = ['allowance', 'assart', 'galaxy', 'space', 'spaceport', 'spaceship']

    x2 = []
    for i in x:
        x2.append(i)
    r = RandomWords()
    key = ""
    word = r.get_random_word()
    #print("Salt:",word)
    maxi=0
    i=0
    indexes=[]
    while i!=len(word):
        index=random.choice(range(len(word)))
        if index not in indexes:
            indexes.append(index)
            i+=1
    indexes=sorted(indexes)
    for index in indexes:
                key+=str(index)+word[index]
                x2.insert(index,word[index])
                maxi=index
                i+=1
    resst2=""
    for i in x2:
        resst2+=i
    #print("Salted:",resst2)
    cc_key = len(resst2)
    for i in resst2:
            if i.isspace():
                rand = random.choice(replacements)
                adder = rand + "[" + rand[:2] + str(len(rand))
                resst2 = resst2.replace(" ", adder)
                break
    #print("Space Salt:", resst2)
    resst2=list(resst2)
    for i in resst2:
        if i.isalpha() or i.isnumeric():
            resst2[resst2.index(i)] =  hex(ord(i))

    #print("Hexatation:",resst2)
    x=""
    for i in resst2:
        x+=i
    resst2=x
    for i in resst2:
        if i.isalpha():
            resst2 = resst2.replace(i, chr(ord(i)+len(resst2)))
    #print("Designation:",resst2)
    return Assignment(resst2,key)
st = input(">>>")
encrypt ,key,key2= Designation(st) 
print("Encrypted", encrypt)
os.chdir("C://Games")
file=open("key","w+")
file.write(key)
file.close()
file2=open("KeyH","w+")
file2.write(key2)
file2.close()
#print("Extraction:", Extract(encrypt,key))