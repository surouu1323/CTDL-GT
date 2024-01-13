def calculate_power_of_a_number_using_recursion(a,n):
    assert n >=0 and int(n) == n
    assert a >=0 and int(a) == a

    # a^0 = 1
    if n==0:
        print(f"{a}^0 = 1")
        return 1
    else:
        kq = a * calculate_power_of_a_number_using_recursion(a,n -1)
        print(f"{a}^{n} = {a} * {a}^{n-1} = {kq}")
        return kq   
        
a = int(input("nhap co so: "))
n = int(input("nhap so mu : "))
ketqua = calculate_power_of_a_number_using_recursion(a,n)
print(f"vay {a}^{n} = {ketqua}")