def ingresar_valores():
    valores = []
    for i in range(5):
        valor = float(input(f"Ingrese el valor {i+1}: "))
        valores.append(valor)
    return valores

def calcular_promedio(valores):
    return sum(valores) / len(valores)

def encontrar_menor(valores):
    return min(valores)

def comparar_suma_multiplicacion(valores):
    suma = sum(valores)
    multiplicacion = valores[0] * valores[2]
    if suma > multiplicacion:
        return "La suma es mayor que la multiplicación."
    elif suma == multiplicacion:
        return "La suma es igual a la multiplicación."
    else:
        return "La suma es menor que la multiplicación."

def main():
    valores = ingresar_valores()
    
    if len(set(valores)) < len(valores):
        print("Los valores deben ser distintos.")
    else:
        promedio = calcular_promedio(valores)
        menor = encontrar_menor(valores)
        comparacion = comparar_suma_multiplicacion(valores)
        
        print(f"El promedio es: {promedio}")
        print(f"El valor menor es: {menor}")
        print(comparacion)

main()
