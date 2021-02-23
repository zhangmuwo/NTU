from sklearn.neural_network import MLPRegressor
import numpy as np
P = []
X = []
Y = []
with open('test_data.txt','r') as reader:
        isfirstline = 1
        while True:
            line = reader.readline()
            p = []
            if isfirstline:
                isfirstline = 0
                continue
            if (not line):
                break
            k = line.split("\t")
            for kk in k:
                kkk = kk.split("\n")
                p.append(float(kkk[0]))
            P.append(p)
with open('train_data.txt','r') as reader:
        isfirstline = 1
        while True:
            line = reader.readline()
            x = []
            if isfirstline:
                isfirstline = 0
                continue
            if (not line):
                break
            k = line.split("\t")
            for kk in k:
                kkk = kk.split("\n")
                x.append(float(kkk[0]))
            X.append(x)
with open('train_truth.txt','r') as reader:
        isfirstline = 1
        while True:
            line = reader.readline()
            y = []
            if isfirstline:
                isfirstline = 0
                continue
            if (not line):
                break
            k = line.split("\t")
            for kk in k:
                kkk = kk.split("\n")
                Y.append(float(kkk[0]))
            



P = np.array(P)
X = np.array(X)
Y = np.array(Y)






def main():
    clf = MLPRegressor(
    hidden_layer_sizes=(4,4,4,4))
    clf.fit(X, Y)
    print("The score is", clf.score(X[:10][:],Y[:10]))
    result = clf.predict(P)
    with open("test_predicted.txt",'w') as out_c:
        out_c.write("y\n")
        i = 0
        for each in result:
            stre = '{:e}'.format(each)
            out_c.write(stre + "\n")

main()


