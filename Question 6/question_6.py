import numpy as np


poly_use = 0
point_use = 0

def readf():
    col = []
    with open('input_question_6_polygon','r') as reader:
        
        while True:
            line = reader.readline()
            if (not line):
                break
            k = line.split(" ")
            for kk in k:
                kkk = kk.split("\n")
                col.append(int(kkk[0]))
        global poly_use
        length = int(len(col))
        poly_use = np.zeros((int(length/2), 2), dtype=int)
        i = 0
        j = 0
        k = 0
        while (i < length/2):
            j = 0
            while (j < 2):
                poly_use[i][j] = col[k]
                j = j + 1
                k = k + 1
            i = i + 1
def readp():
    col = []
    with open('input_question_6_points','r') as reader:
        
        while True:
            line = reader.readline()
            if (not line):
                break
            k = line.split(" ")
            for kk in k:
                kkk = kk.split("\n")
                if (kkk[0] != ''):
                    col.append(int(kkk[0]))
        global point_use
        length = int(len(col))
        point_use = np.zeros((int(length/2), 2), dtype=int)
        i = 0
        j = 0
        k = 0
        while (i < length/2):
            j = 0
            while (j < 2):
                point_use[i][j] = col[k]
                j = j + 1
                k = k + 1
            i = i + 1
            
def findXmax():
    maxX = poly_use[0][0]
    for each in poly_use:
        maxX = max(each[0],maxX)
    return maxX

def findXmin():
    minX = poly_use[0][0]
    for each in poly_use:
        minX = min(each[0],minX)
    return minX

def findYmax():
    maxY = poly_use[0][1]
    for each in poly_use:
        maxY = max(each[1],maxY)
    return maxY

def findYmin():
    minY = poly_use[0][1]
    for each in poly_use:
        minY = min(each[1],minY)
    return minY
    



def checkin(x,y):
    maxX = findXmax()
    maxY = findYmax()
    minX = findXmin()
    minY = findYmin()
    if x < minX or x > maxX or y < minY or y > maxY:
        return False
    i = 0
    t = False
    while i + 1 < len(poly_use):
        if ((poly_use[i][1] > y > poly_use[i + 1][1]) or (poly_use[i + 1][1] > y > poly_use[i][1])):
            k = (poly_use[i][0] - poly_use[i + 1][0])/(poly_use[i][1] - poly_use[i + 1][1])
            b = poly_use[i][0] - k * poly_use[i][1]
            if (x < k * y + b):
                t = not t
        i += 1
    return t
    
def main():
    i = 0
    result = []
    while (i < len(point_use)):
        t = checkin(point_use[i][0], point_use[i][1])
        if (t):
            result.append(" Inside\n")
            print(str(point_use[i][0]) + " " + str(point_use[i][1]) + " Inside\n")
        else:
            result.append(" Outside\n")
            print(str(point_use[i][0]) + " " + str(point_use[i][1]) + " Outside\n")
        i = i + 1
    with open("output_question_6",'w') as out:
        i = 0
        while (i < len(point_use)):
            out.write(str(point_use[i][0]) + " " + str(point_use[i][1]) + result[i])
            i += 1
    out.close()
        
readf()
readp()
main()
