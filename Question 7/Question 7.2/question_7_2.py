L1 = 4
L2 = 8
L3 = 5
L4 = 9
L5 = 6
L6 = 7




def calculateIndex(l1,l2,l3,l4,l5,l6):
    return l1 + l2 * L1 + l3 * L1 * L2 + l4 * L1 * L2 * L3 + l5 * L1 * L2 * L3 * L4 + l6 * L1 * L2 * L3 * L4 * L5

def calculatel(I):
    l1 = I % (L1 * L2 * L3 * L4 * L5) % (L1 * L2 * L3 * L4) % (L1 * L2 * L3) % (L1 * L2) % L1
    l2 = (I % (L1 * L2 * L3 * L4 * L5) % (L1 * L2 * L3 * L4) % (L1 * L2 * L3) % (L1 * L2) - l1) / L1
    l3 = (I % (L1 * L2 * L3 * L4 * L5) % (L1 * L2 * L3 * L4) % (L1 * L2 * L3) - l2 * L1 - l1) / (L1 * L2)
    l4 = (I % (L1 * L2 * L3 * L4 * L5) % (L1 * L2 * L3 * L4) - l3 * L1 * L2 - l2 * L1 - l1) / (L1 * L2 * L3)
    l5 = (I % (L1 * L2 * L3 * L4 * L5) - l4 * L1 * L2 * L3 - l3 * L1 * L2 - l2 * L1 - l1) / (L1 * L2 * L3 * L4)
    l6 = (I - l5 * L1 * L2 * L3 * L4 - l4 * L1 * L2 * L3 - l3 * L1 * L2 - l2 * L1 - l1) / (L1 * L2 * L3 * L4 * L5)
    return [int(l1),int(l2),int(l3),int(l4),int(l5),int(l6)]

condi_use = []
index_use = []
ctoi_result = []
itoc_result = []

def readl():
    global condi_use
    with open('input_coordinates_7_2.txt','r') as reader:
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
    with open('input_index_7_2.txt','r') as reader:
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
    while (i + 5 < len(condi_use)):
        ctoi_result.append(calculateIndex(condi_use[i],condi_use[i+1],condi_use[i+2],condi_use[i+3],condi_use[i+4],condi_use[i+5]))
        i += 6
    while (j < len(index_use)):
        itoc_result.append(calculatel(index_use[j]))
        j += 1
    with open("output_index_7_2.txt",'w') as out_i:
        out_i.write("index\n")
        for one in ctoi_result:
            out_i.write(str(one) + "\n")
    with open("output_coordinates_7_2.txt",'w') as out_c:
        out_c.write("x1 x2\n")
        i = 0
        for each in itoc_result:
            out_c.write(str(each[0]) + " " + str(each[1]) + " " + str(each[2]) + " " + str(each[3]) + " " + str(each[4]) + " " + str(each[5]) + "\n")

    

readl()
readi()
main()

