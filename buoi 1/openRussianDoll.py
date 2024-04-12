def openRussianDoll(doll):
    if doll == 1:
        print("da mo het tat ca bup be")
    else:
        print(f"dang mo bup be thu {doll}")
        openRussianDoll(doll-1)


numDolls = int(input("nhap so bup be: "))
openRussianDoll(numDolls)
