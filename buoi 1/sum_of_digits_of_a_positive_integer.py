def sum_of_digits_of_a_positive_integer(n):
    assert n >=0 and int(n) == n

    if n==0:
        return 0
    else:
        hang_dv = n%10
        conlai = n // 10
        tong = sum_of_digits_of_a_positive_integer(conlai)+ hang_dv
        print(f"phan thua {n}: {tong}")
        return tong
        
n = int(input("nhap n: "))
ketqua = sum_of_digits_of_a_positive_integer(n)
print(f"tong so {n} = {ketqua}")