#Phương trình bậc nhất: ax+b=0
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
x=-b/a
if (a>0):
    print("Ta có PT:",a,"x","+",b,"=0")
    print("x=",x)
else:
    print("PT vô nghiệm")
    
from datetime import datetime 
import calendar 
day=int(input("Nhập ngày:"))
month=int(input("Nhập tháng:"))
year=int(input("Nhập năm:"))
date= datetime(year,month,day)
print ((calendar.monthrange(year,month)))
    
import math
x=int(input("Nhập số x:"))
y=int(input("Nhập số y:"))
print("UCLN của 2 số trên là:",math.gcd(x,y))