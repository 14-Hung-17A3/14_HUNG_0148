a=int(input("Nhập vào một số nguyên (Kết thúc khi nhập số ):"))
tong=0
while a>0:
    tong+=a
    print(tong)
    a+=1
    if a==0:
        break
    print("Kết thúc !!")