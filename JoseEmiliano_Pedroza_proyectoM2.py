# min = 4
# max = 8
# palabra = input("Ingrese una palabra min 4 caracteres, maximo 8 ")
# total_caracteres = len(palabra)
# if len(palabra) in range(min, max):
#     print("La palabra es correcta")
# elif len(palabra) < min:
#     print(f"Demasiado corta, tiene ", total_caracteres, "caracteres")
# elif len(palabra) > max:
#     print(f"Demasiado larga, tiene", total_caracteres, "caracteres")

#########################################################################################################


x = float(input("Ingrese el valor de x "))
y = float(input("Ingrese el valor de y "))

if x == 0 and y == 0:
    print("El punto se encuentra en el origen, favor de ingresar valores mayores o menores a 0")
else:
    if x > 0 and y > 0:
        print ("El punto esta en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto esta en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto esta en el Cuadrante III")
    elif x > 0 and y < 0:
        print("El punto esta en el Cuadrante IV")