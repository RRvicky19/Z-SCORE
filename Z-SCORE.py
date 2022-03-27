from statistics import NormalDist
c=0
while(c==0):
    m = int(input("Enter the mu"))
    s = int(input("Enter the sigma"))
    dis = NormalDist(mu = m,sigma=s)
    print("If u need from infinity to Particular value give -1")
    data1 = int(input("Enter the data 1 :"))
    data2 = int(input("Enter the data 2 :"))
    print(dis.pdf(data2)-dis.pdf(data1))
    print("Want to try again Enter 1 else 0")
    c=int(input())