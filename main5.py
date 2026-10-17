a=int(input("Сума чисел: "))
b=int(input("Добуток чисел: "))
for x in range(1, a+1):
    y=a-x
    if x*y==b and x<=y:
        print(x, y)
