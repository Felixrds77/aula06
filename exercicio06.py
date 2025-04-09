intervalodentro = 0
intervalofora = 0
for z in range(1,11,1):
    n = int(input("digite um numero:"))
    if 10 <= n <= 20:
        intervalodentro =  intervalodentro + 1
    else :
        intervalofora = intervalofora + 1
print(f"dentro do intervalo tem {intervalodentro} numeros")
print(f"fora do intervalo tem {intervalofora} numeros")