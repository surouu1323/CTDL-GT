

numb = int(input("nhap so muon dao : "))
res = 0

while(numb != 0):
    a = numb % 10
    res = res * 10 + a
    numb = numb // 10
     
print(res)