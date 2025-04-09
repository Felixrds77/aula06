negativos = 0
for z in range(1,11,1):
    n = int(input("digite um numero:"))
    if n<0:
        negativos =  negativos + 1
else:
    print(f"total de numeros negativos é {negativos}")