fin=int(input("Digite un hasta donde quiere que vaya la serie: "))
num1=int(input("Digite un numero"))
for num1 in range(1,fin+1):
    print(num1)
    if fin%num1==0:
        print("divisores",fin)