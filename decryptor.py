import re
def Purify(x,key):
    x=list(x)
    while "[" in x and x[x.index("[")+3].isnumeric():
        ind=x.index("[")
        space=int(x[ind+3])
        #print(ind)
        #print(x[space])
        #print(x[ind-space:ind+4])
        x[ind-space:ind+4]=' '
    st=""
    for i in x:
        st+=i
    print(st)
    key_pos=re.findall("[0-9]+", key)
    #print(key_pos)
    actual_key=""
    for i in key:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz":
            actual_key+=i
    for i in key_pos:
        x[int(i)]=""
    decrypt=""
    for i in x:
            decrypt+=i
    print(decrypt)
def Expulsion(resst2,key):
    #print(resst2)
    for i in resst2:
        if not i.isdigit() and ord(i)>len(resst2):
            #print(ord(i),len(resst2))
            resst2 = resst2.replace(i, chr(ord(i) - len(resst2)))
    #print(resst2)
    resst2=resst2.split("0x")
    #print(resst2)
    dec=""
    for i in resst2:
        if i!="" :
            if i[-1] not in"!@#$%^&*()_+-={}[]:'?><:.," and ord(i[-1])!=34:
                dec+=chr(int(i,16))
            elif i[-1] in"!@#$%^&*()_+-={}[]:'?><:.," or ord(i[-1])==34:
                dec+=chr(int(i[:-1],16))+i[-1]

    Purify(dec,key)
def Delocation(x,key):
    res=""
    count=0
    for i in x:
        if count%2==0:
            for j in i:
                if not j.isspace():
                    res+=j
        else:
            for j in i[::-1]:
                if not j.isspace():
                    res+=j
    #print(res)
    Expulsion(res,key)
def Transpose(A,key):
    #print(A)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    #print(A)
    return Delocation(A,key)
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
    return Transpose(matrix,key)
def Extract(x,key=""):
    closest_square = 0
    i = 1
    while True:
        if i ** 2 >= len(x):
            break
        else:
            i += 1
    closest_square = i ** 2
    x += " " * (closest_square - len(x))
    matrix = []
    sub_matrix = []
    for j in x:
        if len(sub_matrix) != i:
            sub_matrix.append(j)

        if len(sub_matrix) == i:
            matrix.append(sub_matrix)
            sub_matrix = []
    ord_matrix=[]
    ord_sub=[]
    for i in matrix:
        for j in i:
            if ord(j)!=32:
                ord_sub.append(chr(ord(j)-128000))
        ord_matrix.append(ord_sub)
        ord_sub=[]
    #print(ord_matrix)
    return rotate(ord_matrix,key)
dec_in=input(">>>")
key_in=input("KEY:")
Extract(dec_in[:-4],key_in)