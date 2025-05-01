n = 9
for i in range(1, n+1):
    for j in range(1, n+1):
        if j == 1:
            print(i , end= " " )
        elif  j == i or j == n-i+1:
            print(i, end = " ")
        elif j == n:
            print(i, end = " ")
        else:
            print(" ", end = " ")    
    print()
    