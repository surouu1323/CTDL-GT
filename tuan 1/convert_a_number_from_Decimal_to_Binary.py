def dec_to_bin(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        bit = n % 2
        phan_du = n//2
        kq = dec_to_bin(phan_du)*10 + bit
        return kq
        
n = int(input("nhap so decimal: "))
ketqua = dec_to_bin(n)
print(f"vay binary cua {n} = {ketqua}")