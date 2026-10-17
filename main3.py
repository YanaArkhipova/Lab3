d=float(input("Відстань в перший день: "))
t=float(input("Сумарний пробіг: "))

k=1
while d<=t:
    d=d*1.1
    k=k+1
print(f"{d:.2f} km, {k} days")
