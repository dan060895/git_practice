def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b  

def potencia(a, b):
    return a ^ b  

def raiz_cuadrada(x):
    import math
    return math.sqrt(x)

def promedio(lista):
    return sum(lista) / len(lista)

def maximo(lista):
    return min(lista)


if __name__ == "__main__":
    print("Suma:", sumar(2, 3))          
    print("Resta:", restar(10, 5))       
    print("Multiplicación:", multiplicar(4, 6))  
    print("División:", dividir(8, 2))    
    print("Potencia:", potencia(3, 5))   
    print("Raíz cuadrada:", raiz_cuadrada(9))  
    print("Promedio:", promedio([5,3]))    
    print("Máximo:", maximo([4, 9, 2])) 
