import numpy as np

list_use = np.zeros((10, 20), dtype=int)
col = []

groupnumber = 0

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def gettop(self):
        return self.stack[-1]
        
    def getline(self):
        return len(self.stack)
        
    def isempty(self):
        return (len(self.stack) == 0)

stack = Stack()

def readf():
    with open('input_question_4','r') as reader:
        
        while True:
            line = reader.readline()
            if (not line):
                break
            for k in line:
                if (k == "\t" or k == '\n'):
                    continue
                col.append(k)

    i = 0
    j = 0
    k = 0 
    while (i < 10):
        j = 0
        while (j < 20):
            list_use[i][j] = col[k]
            j = j + 1
            k = k + 1
        i = i + 1

def checkfour(x,y):
    if (x - 1 > 0) and (list_use[x-1][y] == 1):
        stack.push([x-1,y])
    if (x + 1 < 10) and (list_use[x+1][y] == 1):
        stack.push([x+1,y])
    if (y - 1 > 0) and (list_use[x][y-1] == 1):
        stack.push([x,y-1])
    if (y + 1 < 20) and (list_use[x][y+1] == 1):
        stack.push([x,y+1])
    
def change(x,y):
    if (groupnumber  == 0):
        list_use[x][y] = 999
    else:
        list_use[x][y] = groupnumber + 1 

def  outputfile():
    with open("output_question_4",'w') as out:
        i = 0
        j = 0
        while (i < 10):
            j = 0
            while (j < 20):
                if (j == 19):
                    out.write(str(list_use[i][j]) + "\n")
                else:
                    out.write(str(list_use[i][j]) + "\t")
                j += 1
            i += 1

def main():
    
    readf()
    i = 0
    j = 0
    while (i < 10):
        j = 0
        while (j < 20):
            if (list_use[i][j] == 1):
                change(i,j)
                checkfour(i,j)
                while (not stack.isempty()):
                    tem = stack.pop()
                    temi = tem[0]
                    temj = tem[1]
                    change(temi,temj)
                    checkfour(temi,temj)
                global groupnumber      
                groupnumber = groupnumber + 1
            j += 1
        i += 1
    i = 0
    j = 0
    while (i < 10):
        j = 0
        while (j < 20):
            if (list_use[i][j] == 999):
                list_use[i][j] = 1
            j += 1
        i += 1
    outputfile()
                    
            
                
main()
print(list_use)

