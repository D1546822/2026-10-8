x = int(input('十進制的數:'))

if (0<=x<=15):
    print(f"轉換成二進制:{x//8}{x%8//4}{x%8%4//2}{x%2}")
    print(f"轉換成八進制:{x//8}{x%8}")
    if (x==10):
        y = 'A'
    elif (x==11):
        y = 'B'
    elif (x==12):
        y = 'C'
    elif (x==13):
        y = 'D'
    elif (x==14):
        y = 'E'
    elif (x==15):
        y = 'F'
    else:
        y = x
    print(f"轉換成十六進制:{y}")
else:
    print('輸入錯誤')