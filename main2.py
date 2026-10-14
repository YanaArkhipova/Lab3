n= int(input("Ціле число: "))
k=0
for i in range (10, n):
    a=i//10
    b=i%10
    s=a**2+b**2
    if s%n==0:
        print(i, end=" ")
        k+=1
if k==0:
    print("Чисел де сума квадратів цифр яких ділиться на n націло не існує")
