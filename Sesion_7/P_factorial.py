from Factorial_3 import fcn_factorial as f


def main():
    n = int(input("Ingrese el numero de grupos: "))
    m = int(input("Ingrese el numero de muestras: "))
    result = (f(n)/(f(m)*f(n-m)))
    print(f'El numero de combianciones posibles es: {result}')


if __name__=="__main__":
        main() 