def hexhex(x):
    if x == 10:
        y = "A"
    elif x == 11:
        y = "B"
    elif x == 12:
        y = "C"
    elif x == 13:
        y = "D"
    elif x == 14:
        y = "E"
    elif x == 15:
        y = "F"
    else:
        y = "?"

    return y

value = int(input("Enter number between 0 - 255: "))
if value >= 0 and value =< 255:
    pass
else:
    print("try again")
    quit
fnum = value // 16
bnum = value % 16
def poo(a):
    if a < 10:
        return a
    else:
        b = hexhex(a)
        return b

first = str(poo(fnum))
second = str(poo(bnum))
hexValue = first + second
print(hexValue)

