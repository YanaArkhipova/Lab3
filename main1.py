n=int(input("Введіть ціле число 1 < n <= 100: "))
for i in range(1, n + 1):
    if n<1 or n>100:
         print("1 < n ≤ 100!!!")
         break
    elif i%2 !=0:
         continue
    print(i, end=" ")
