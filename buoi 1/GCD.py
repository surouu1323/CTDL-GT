def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)
        
a = int(input("nhap so t1: "))
b = int(input("nhap so t2 : "))
ketqua = GCD(a,b)
print(f"vay GCD({a},{b}) = {ketqua}")