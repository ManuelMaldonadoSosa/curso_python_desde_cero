# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

tup=(10,12,13,14,15,16,9,13)
tup2=(12,)
tup_2=(("Manuel","Maldonado",123456),("Juan","Perez",234567))
lista1=[1,2,3]
def cuadrado(n):
  return n**2

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    #Acceso a valores de tuplas
    a=tup[1]
    print(tup[1])
    print(a)
    #Consultar si un valor se encuentra dentro de la tupla
    resultado=10 in tup
    print(resultado)
    print(10 in tup)
    #print(type(tup2))
    #Consultar si un valor no esta en la tupla
    print(10 not in tup)
    #Concatenar dos tuplas
    tup3=tup+tup2
    print(tup3)
    #Concatenar una tupla n veces
    #tup4=tup*3
    #print(tup4)
    #Rebanada de tuplas
    print(tup[0:5:2])
    print(tup[2:5])
    #Obtenemos la longitud de una tupla
    longitud_tup=len(tup)
    print(longitud_tup)
    #obtenemos el minimo de una tupla
    min_tup=min(tup)
    print(min_tup)
    #obtenemos el maximo de una tupla
    max_tup=max(tup)
    print(max_tup)
    #Buscamos con index el valor x en la tupla
    print("************")
    a=13
    b=tup[2:5]
    if a in tup:
        if a in b:
            posicion=tup.index(a,2,4)
            print(posicion)
        else:
            print("Esta fuera del rango de consulta pero se encuentra en la tupla")
    else:
        print(f"No se encuentra {a} en la tupla")

    #Utilizamos count para contar la cantidad de ocurrencias de x en la tupla
    print("--------")
    print(tup.count(13))
    for t in tup_2:
        for t2 in t:
            print(t2)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
   # for l in lista1:
   #     print(l)
   #     print(f" El cuadrado de {l} es : {cuadrado(l)}")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
