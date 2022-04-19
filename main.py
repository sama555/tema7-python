#nivel global
#importa el modulo.nombredelArchivo
import operaciones.calculadora

def main():
    sum = operaciones.calculadora.suma(4,8)
    res =operaciones.calculadora.resta(9,5)
    mul = operaciones.calculadora.multiplicacion(9,8)
    div = operaciones.calculadora.division(6,8)
    print('Suma ',sum)
    print('Resta ', res)
    print('Multiplicacion ',mul)
    print('Division ', div)

if __name__ == '__main__':
    main()