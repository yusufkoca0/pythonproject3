import sys
#dictionaries
encdic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9,
          "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18,
          "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, " ": 27}
decdic = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h", 9: "i",
          10: "j", 11: "k", 12: "l", 13: "m", 14: "n", 15: "o", 16: "p", 17: "q", 18: "r",
          19: "s", 20: "t", 21: "u", 22: "v", 23: "w", 24: "x", 25: "y", 26: "z", 27: " "}
#dictionaries

#classes
class Undefinedparameter(Exception):
    pass
class CannotRead(Exception):
    pass
class Empty(Exception):
    pass
#classes

#functions

#This function checks if the given key or input file is txt or not
def istxt(file):
    file_location_list = file.split("/")
    file_extension = file_location_list[-1].split(".")
    if file_extension[1] == "txt":
        return True
    else:
        return False
#This function takes the message and splits it into suitable matrixes for the key
def getMessageMatrix(mess):
    templist1 = []
    returnlist = []
    for i in range(len(message)):
        if i % len(keymatrix) != (len(keymatrix)-1):
            templist1.append(mess[i])
        else:
            templist1.append(mess[i])
            returnlist.append(templist1)
            templist1 = []
    return returnlist

#This function gets the atrix multiplication of key and message or inverse of the key and encoded message
def getMatrixMultiplication(key, mess):
    result = []
    for i in range(len(mess)):
        result.append([])
        for j in range(len(mess[0])):
            result[i].append(0)
    for k in range(len(mess)):
        for i in range(len(key[0])):
            for j in range(len(key)):
                result[k][i] += int(key[i][j])*mess[k][j]
    return result

#This function calculates the minor matrixes of any nxn matrix
def getMinor(matrix):
    minorlist = []
    list2 = []
    list3 = []
    checkset = set()
    for i in range(len(matrix)):
        checkset.add(i)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in checkset:
                if i != k:
                    for l in checkset:
                        if j != l:
                            list2.append(matrix[k][l])
                    list3.append([m for m in list2])
                    list2.clear()
            minorlist.append([n for n in list3])
            list3.clear()
    return minorlist

#This function is used for calcualting determinant of matrixes that are larger than 2x2
def getDeterminantMinor(matrix, i, j):
    minorlist = []
    list2 = []
    checkset = set()
    for k in range(len(matrix)):
        checkset.add(k)
    for k in checkset:
        if i != k:
            for l in checkset:
                if j != l:
                    list2.append(matrix[k][l])
            minorlist.append([m for m in list2])
            list2.clear()
    return minorlist

#This function gets the determinant of each nxn matrix
def getDeterminant(matrix):
    sign = 1
    determinant = 0
    #First it checks the length of the matrix, if it's 2x2 it calculates it with a single line
    if len(matrix) == 2:
        determinant = matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
        return determinant
    #If it is not 2x2 it does the calculation below, it multiplies each value in the first row with their minor matrixes
    else:
        for i in range(len(matrix)):
            determinant += sign*matrix[0][i]*getDeterminant(getDeterminantMinor(matrix, 0, i))
            sign = sign*(-1)
        return determinant

#This function takes the inverse of any nxn matrix
def getInverse(matrix):
    #first it gets the determinant by using getDeterminant function
    matrixdet = getDeterminant(matrix)
    matrixcofactor = []
    sign = 1
    #Then it checks the length of the matrix if it's 2x2 it's easy it just uses one line of code
    if len(matrix) == 2:
        matrixcofactor = [[(matrix[1][1])/matrixdet, ((-1)*matrix[0][1])/matrixdet], [((-1)*matrix[1][0])/matrixdet, (matrix[0][0])/matrixdet]]
    #If it is not 2x2 it goes and does the calculations below
    else:
        #It finds the minor matrix for each value in the matrix
        matrixminor = getMinor(matrix)
        #Then it finds the determinant of each minor matrix
        for i in range(len(matrixminor)):
            matrixminor[i] = getDeterminant(matrixminor[i])
        #Then it makes some preparation to calculate cofactor of first matrix
        for i in matrix:
            matrixcofactor.append([])
        #Then it calculates the cofactor (basically it reverses each diagonal from bottom left to top right, and it takes the negative of each second value)
        for i in range(len(matrixminor)):
            matrixcofactor[i%len(matrix)].append(matrixminor[i])
        if len(matrix)%2 == 0:
            for i in range(len(matrixcofactor)):
                for j in range(len(matrixcofactor)):
                    matrixcofactor[i][j] = sign*matrixcofactor[i][j]
                    sign = sign*(-1)
                sign = sign*(-1)
        else:
            for i in range(len(matrixcofactor)):
                for j in range(len(matrixcofactor)):
                    matrixcofactor[i][j] = sign*matrixcofactor[i][j]
                    sign = sign*(-1)
        #Then it divides each value in the cofactor by the determinant of the original matrix
        for i in range(len(matrixcofactor)):
            for j in range(len(matrixcofactor)):
                matrixcofactor[i][j] = matrixcofactor[i][j]/matrixdet
    return matrixcofactor
#functions


#errors

#This try block is parameter related errors
try:
    operation = sys.argv[1]
    key = sys.argv[2]
    inputfile = sys.argv[3]
    outputfile = sys.argv[4]
    if len(sys.argv) > 5:
        raise IndexError
    if operation == "enc" or operation == "dec":
        pass
    else:
        raise Undefinedparameter
except IndexError:
    print("Parameter number error")
    exit()
except Undefinedparameter:
    print("Undefined parameter error")
    exit()

#This try block is for input file related errors
try:
    f=open(inputfile, "r")
    if istxt(inputfile) == False:
        raise CannotRead

    message = f.readlines()
    if message == []:
        raise Empty

    if operation == "enc":
        message[0] = message[0].lower()
        message = [i for i in message[0]]
        for i in range(len(message)):
            message[i] = encdic[message[i]]
    elif operation == "dec":
        message = message[0].split(",")
        for i in range(len(message)):
            message[i] = int(message[i])
except FileNotFoundError:
    print("Input file not found error")
    exit()
except CannotRead:
    print("The input file could not be read error")
    exit()
except Empty:
    print("Input file is empty error")
    exit()
except KeyError:
    print("Invalid character in input file error")
    exit()

#This try block is for key file related errors
try:
    g=open(key, "r")
    if istxt(key) == False:
        raise CannotRead
    keymatrix = [line.replace("\n", "").replace(" ", "").split(",") for line in g.readlines()]
    if keymatrix == []:
        raise Empty
    for i in range(len(keymatrix)):
        for j in range(len(keymatrix)):
            keymatrix[i][j] = int(keymatrix[i][j])
            if keymatrix[i][j] <=0:
                raise ValueError
except FileNotFoundError:
    print("Key file not found error")
    exit()
except CannotRead:
    print("Key file could not be read error")
    exit()
except Empty:
    print("Key file is empty error")
    exit()
except ValueError:
    print("Invalid character in key file error")
    exit()
#errors

f.close()
g.close()

#encoding-decoding
if operation == "enc":
    #encoding process
    while len(message) % len(keymatrix) != 0:
        message.append(27)
    messagematrix = getMessageMatrix(message)
    encodedmessage = getMatrixMultiplication(keymatrix, messagematrix)
    h = open(outputfile, "w+")
    for i in range(len(encodedmessage)):
        for j in range(len(encodedmessage[i])):
            if i == (len(encodedmessage)-1) and j == (len(encodedmessage[i])-1):
                h.write(str(encodedmessage[i][j]))
            else:
                h.write(str(encodedmessage[i][j]))
                h.write(",")
    h.close()
    #encoding process

    #decoding process
elif operation == "dec":
    messagematrix = getMessageMatrix(message)
    inversekeymatrix = getInverse(keymatrix)
    decodedmessage = getMatrixMultiplication(inversekeymatrix, messagematrix)
    h = open(outputfile, "w+")
    for i in range(len(decodedmessage)):
        for j in range(len(decodedmessage[i])):
            h.write(decdic[decodedmessage[i][j]])
    h.close()
    #decoding process
exit()

#encoding-decoding
