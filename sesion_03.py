# loop
mi_list = [1,2,3,4,5]
for i in mi_list:
  print("El numero es: ", i)
  resul = 0
  for i in mi_list:
    resul += i
    print(f"El resultado de la suma de mi_lista es: (resul) ")
    for i in range(2,9) : 
      print(i)
      mi_list_2 = ["lunes", "martes", "miercoles", "jueves", "viernes"]
      for i in mi_list_2:
        if i != "lunes":
          print(f"feliz(i)!")
#while loop
i = 0
while i < 5:
  i +=1
  if i==3:
    continue
    print(i)
    if i==4:
      break
    else:
      print("i es ahora mayir o igual a 5")
# practica 2
# dada la lista mi_lista = [lunes, jueves, miercoles, jueves, viernes]
# imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
# pista: usa los dos tipos de loops while y for en el mismo programa para lograrlo
# resultado:
# martes
# miercoles
# jueves
# viernes
# martes
# miercoles
# jueves
# viernes
# martes
#miercoles
#jueves
#viernes

i = 0
mi_lista_2 = ["lunes", "martes", "miercoles", "miercoles", "jueves", "viernes"]
while i< 3:
  i += 1

for d in mi_lista_2:
  if d != "lunes"
  print(d)
