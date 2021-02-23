L1 = 50
L2 = 57

def calculateIndex(l1,l2):
    return l2*L1 + l1

def calculatel(I):
    return [int(I%L1), int((I - I%L1)/L1)]

condi_use = []
index_use = []
ctoi_result = []
itoc_result = []

def readl():
    global condi_use
    with open('input_coordinates_7_1.txt','r') as reader:
        isfirstline = 1
        while True:
            line = reader.readline()
            if isfirstline:
                isfirstline = 0
                continue
            if (not line):
                break
            k = line.split("\t")
            for kk in k:
                kkk = kk.split("\n")
                condi_use.append(int(kkk[0]))
                
def readi():
    global index_use
    with open('input_index_7_1.txt','r') as reader:
        isfirstline = 1
        while True:
            line = reader.readline()
            if isfirstline:
                isfirstline = 0
                continue
            if (not line):
                break
            k = line.split("\t")
            for kk in k:
                kkk = kk.split("\n")
                index_use.append(int(kkk[0]))
            
def main():
    i = 0
    j = 0
    while (i + 1 < len(condi_use)):
        ctoi_result.append(calculateIndex(condi_use[i],condi_use[i+1]))
        i += 2
    while (j < len(index_use)):
        itoc_result.append(calculatel(index_use[j]))
        j += 1
    with open("output_index_7_1.txt",'w') as out_i:
        out_i.write("index\n")
        for one in ctoi_result:
            out_i.write(str(one) + "\n")
    with open("output_coordinates_7_1.txt",'w') as out_c:
        out_c.write("x1 x2\n")
        i = 0
        for each in itoc_result:
            out_c.write(str(each[0]) + " " + str(each[1]) + "\n")

    

readl()
readi()
main()

