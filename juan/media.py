print ("vamos verificar sua media")
num1 = float(input("digite seu 1º numero"))
num2 = float(input("digite seu 2º numero"))

premedia = num1 + num2 
media = premedia / 2

if media >= 7.0:
    print (f"você passou {media}")
else:
    print(f"nao passou {media}")