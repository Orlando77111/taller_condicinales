
x= int(input("Digite el valor de x: "))
y= int(input("Digite el valor de y: "))

if x==0:
    if y==0:
        print("La coordenada esta en el origen.")
    else:
        print("La coordenada esta en el eje Y")
else:
    if y==0:
        print("La coordenada esta en el eje x.")
    else:
        if x>0:
            if y>0:
                print("La coordenada esta en el cuadrante 1.")
            else:
                print("La coordenada esta en el cuadrante 4.")
        else:
            if y<0:
                print("La coordenada esta en el cuadrante 3.")
            else:    
                print("La coordenada esta en el cuadrante 2.")
                     