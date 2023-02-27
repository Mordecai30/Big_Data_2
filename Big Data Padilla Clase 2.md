```Python
llista=["carles","jaume","antonio"]
nou_nom="julio"
llista=llista.append(nou_nom)
print(llista)
```
Append és una funció que serveix per afegir nous valors a una llista dins de Python. 

```Python
llista_noms = ["Carme","Joan"]
for nom in llista_noms:
	if nom==="Joan": ##condició perque al recòrrer la llista extregui el valor 
		print(nom)
```

```Python
numeros = [1,2,3,4,5,6,7,8,10,15]
for n in numeros:
	if n>6:
		print(f"{n} és menor que 6")
	elif n == 6: ##condició alterna 
		print(f"{n} és igual que  6")
	else: ##resta de resultats
		print(f"{n} és major que 6")

print(len(numeros)) ##len és una funció que serveix per calcular l'allargada
```

## Exercici 1
```Python
variable= "esto es un ejercicio"  
print(variable)  
aprovat = 8.75  
assignatura = "No m'enrecordo"  
print("En la assignatura" , assignatura , "he sacado un" , aprovat)
```
## Exercici 2
```Python
notas = ["5","7","6","4","8","2"]  
alumnos = ["jaume","carla","pere","adrià","rafael","agnès"]  

for nota, nom in zip(notas, alumnos): 
    nota=int(nota)  
    nota=nota+1  #1.  Debes sumar 1 punto a cada una de las notas.  
    print (nom, "ha tret un ", nota)  
    #2.  Imprime el resultado junto al nombre del correspondiente alumno de tal manera que: _var_alumno_ ha obtenido un _var_nota_".
```

**index és una funció que ens permet trobar la posició d'un valor dins d'una llista**. 
```Python
llista = {"adria","carla","joan", "pere"}

nom = "joan"

if nom in llista:
	print("sí")
	position=lista.index(nom)
else:
	print("no")
```
**set és una funció que permet trobar els valors no repetits dins una llista**
```Python
	llista = ["adria","carla","joan","pere","pere","carla"]
	valors_unics = set(llista)
	print(valors_unics)
	```

```Python
llista = [  
    "david",  
    "dani",  
    "marta",  
    "jaume",  
    "adria",  
    "carla",  
    "joan",  
    "pere",  
    "carla",  
    "pere",  
    "adria",  
    "quico",  
    "pere",  
    "joan",  
    "agustí",  
    "adria",  
    "joan",  
    "adria",  
    "siscu",  
    "carles",  
    "dani",  
    "carla"  
    ]  
  
#¿Cuantas personas han asistido a las jornadas de puertas abiertas?  
clean_llista=set(llista)  
conteo_llista=len(clean_llista)  
print(conteo_llista)  
#¿Cuantas personas han asistido a más de dos sesiones?  
llista_repetits=[]  
for nom in clean_llista:  
    contador=0  
    valor = llista.count(nom)  
    if valor>1:  
        contador=contador+1  
        print(nom,valor)  
        llista_repetits.append(nom)  
print(llista_repetits)  
#¿Qué porcentaje de los asistentes accede a más de dos sesiones? 
```

