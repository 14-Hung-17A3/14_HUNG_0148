#Hàm trả về phần nguyên của phép chia hai số nguyên
def chia_lay_nguyen(a,b):
    c=a//b
    return c 
a=int(input("a = "))
b=int(input("b = "))
c= chia_lay_nguyen(a,b)
print("Phần nguyên của",a,"chia",b,"là :",c)