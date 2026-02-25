# Instrucciones funcion calculadora

# Cree un función en python llamada calculadora, la cual debe 
# tomar los parámetros (num_1, num_2, operacion) y debe ser 
# capaz de realizar toda la lógica de un calculadora simple 
# como: sumar, restar, multiplicar y dividir.
# Nota: Las entradas serán proporcionadas por el usuario.
# Pista: Este código es un ejemplo de una suma 

print("====Mi calculadora====")
numero_1 = float(input("Escriba el valor del primer numero: "))
numero_2 = float(input("Escriba el valor del segundo numero: "))
op = input("cual operacion deseas hacer? +, -, *, /, -> ")

def suma(numero_1, numero_2):
    return numero_1 + numero_2

if op == "+":
    resultado = suma(numero_1, numero_2)
    print("El resultado de la suma es: ", resultado)

    def res(numero_1, numero_2):
        return numero_1 - numero_2
    
    if op == "-":
        resultado = res(numero_1, numero_2)
        print("El resultado de la resta es: ", resultado)

def mul(numero_1, numero_2):
    
    return numero_1 * numero_2

if op == "*":
    resultado = mul(numero_1, numero_2)
    print("El resultado de la multiplicacion es: ", resultado)

def div(numero_1, numero_2):
    return numero_1 / numero_2

if op == "/":
    resultado = div(numero_1, numero_2)
    print("El resultado de la suma es: ", resultado)