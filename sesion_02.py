# tuplas
mi_tupla = (2, 4)
print("mi tupla: ", mi_tupla)

# lista
mi_lista = [1,3.1416, "valeria", mi_tupla]
print("el primer elemento de mi lista: ", mi_lista[0])

#diccionarios
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre": "valeria",
    "pi": 3.1416,
    "tel": "66-2235677"
}
print("llave para accesar a mi_lista", mi_diccionario["mi_lista"])
print("llave para accesar a pi", mi_diccionario["pi"])
print("llave para accesar a tel", mi_diccionario["tel"])
