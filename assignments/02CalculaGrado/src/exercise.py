def calcula_grado(valor):
    if valor<=1 and valor>=0:
        if valor>0.9 :
            return "A"
        elif valor>0.8 :
            return "B"
        elif valor>0.7 :
            return "C"
        elif valor>0.6 :
            return "D"
        elif valor<0.6 :
            return "F"
    else:
        return("score incorrecto")
def main():
    #escribe tu código abajo de esta línea
    x = float(input("Ingresa Un valor entre 0.0 y 1.0: "))
    print(calcula_grado(x))

if __name__=='__main__':
    main()
