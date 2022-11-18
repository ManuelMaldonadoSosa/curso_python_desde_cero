

edad={"jorge":22,"ana":21,"manuel":32}
personas={"apellidos":["maldonado","perez"],"nombre":["manuel","juan"]}
print(edad)
#Leemos un valor de una llave
print(edad["jorge"])
edad["jorge"]=23
print(edad["jorge"])
edad["ana"]=30
edad["juan"]= [1,2,3]

print(edad)
#edad_juan=edad.pop("juan")
print(edad)
#print(edad_juan)
print("jorge"in edad)

for l in edad.keys():
    print(l)
    print(f"{edad[l]}")
print("*********")
for v in edad.values():
    print(v)

for l,v in edad.items():
    print(f"La edad de {l} es: {v}")


