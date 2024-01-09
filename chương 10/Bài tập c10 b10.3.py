import math
#Nhập vào số nguyên n
print("Nhập n :")
n=int(input())
#Nhập vào số thực x
print("Nhập x :")
x=float(input())
S=math.pow((math.pow(x,2)+1),n)
print("S=(x*x + 1)^n =",S)