A = int(input('A:'))
B = int(input('B:'))
if (0<=A<=1 and 0<=B<=1):
    if (A==1 or B==1):
        print("OR:1")
    else:
        print("OR:0")
    if (A*B==1):
        print("AND:1")
    else:
        print("AND:0")
    if (A==1 and B==0):
        print("XOR:1")
    if (A==0 and B==1):
        print("XOR:1")
    else:
        print("XOR:0")
else:
    print('輸入錯誤')