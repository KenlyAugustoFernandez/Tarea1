centrimetros = float (input("ingrese la longituda en centimetros"))
Unidad_objetivo = input("opciones para elegir: metros, yardas, varas, pulgadas, pies\nA que unidad desea convertir: ")
if Unidad_objetivo == "metros":
    metros = centrimetros / 100
    print (metros, "metros")
elif Unidad_objetivo == "yardas":
    yardas = centrimetros / 91.44
    print (yardas, "yardas")
elif Unidad_objetivo == "varas":
    varas = centrimetros / 50.8
    print (varas, "varas")
elif Unidad_objetivo == "pulgadas":
    pulgadas = centrimetros / 2.54
    print (pulgadas, "pulgadas")
elif Unidad_objetivo == "pies":
    pies = centrimetros / 30.48
    print (pies, "pies")
else:
    print("opcion incorrecta")
    
