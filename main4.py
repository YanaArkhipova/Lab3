a=int(input("1 додатнє ціле число: "))
b=int(input("2 додатнє ціле число: "))
n=a*b
while b!=0:
    k=a%b
    a=b
    b=k
print(n//a)
