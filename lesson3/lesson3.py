import csv
import json

def f_1 (x):
    func1 = x/(x+100)
    return func1

def f_2 (x):
    func2 = 1/x
    return func2
def f_3 (x):
    func3 = 20*(f_1(x)+f_2(x))/x
    return func3

def generator (start,end):
    while start<end:
        yield start
        start+=1
def writecvs (dictionary):
    with open("data.csv","w") as file :
        writer = csv.writer(file)
        writer.writerows(

            (dictionary.items())
        )
    return print ("data.csv created or updated")
def readcvs (filename):
    rez_list = []
    with open(filename, "r") as File:
        reader = csv.reader(File,delimiter = ",")
        for row in reader:
            rez_list.append(row)
    return rez_list
def writejson (list):
    with open('data.json', 'w') as f:
        json.dump(list, f)
    return print ("data.json created or updated")
def main ():
    shag = generator(5,91)
    rez_1 = []
    rez_2 = []
    rez_3 = []
    dictionary= {}
    for i in shag :
        x_i = i
        rez_1.append("%.4f"%f_1(i))
        rez_2.append("%.4f"%f_2(i))
        rez_3.append("%.4f"%f_3(i))
        dictionary[x_i] =[("%.4f"%f_1(i)),("%.4f"%f_2(i)),("%.4f"%f_3(i))]
    print (rez_1)
    print(rez_2)
    print(rez_3)
    print (dictionary)
    writecvs(dictionary)
    data_list = readcvs("data.csv")
    print(data_list)
    writejson(data_list)

if __name__ == '__main__':
    main()
