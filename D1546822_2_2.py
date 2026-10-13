A = int(input('A:'))
B = int(input('B:'))
S = int(input('S:'))
if (0<=A<=1 and 0<=B<=1 and 0<=S<=1):
    if (A==1 and B==0):
        if (S==1):
            print('第一個閘輸出:1')
            print('允許啟動:1')
        else:
            print('第一個閘輸出:1')
            print('允許啟動:0')
    elif (A==0 and B==1):
        if (S==1):
            print('第一個閘輸出:1')
            print('允許啟動:1')
        else:
            print('第一個閘輸出:1')
            print('允許啟動:0')
    else:
        print('第一個閘輸出:0')
        print('允許啟動:0')
else:
    print('輸入錯誤')