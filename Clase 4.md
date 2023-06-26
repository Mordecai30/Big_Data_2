# La API de Twitch
Twitch cuenta con muchos servidores que conjuntamente utilizan y gestionan una gran base de datos. La API habilitada por Twitch tiene establecidos aquellos datos que pueden ser obtenidos por los usuarios de una forma u otra. De esta forma regula la corriente de datos tanto en forma de *inputs* como de *outputs*. 

## Conexión con la API

### Protocolos de acceso para desarrolladores
Existen métodos más complejos que permiten la comunicación con la API a través del uso de protocolos https predefinidos por la propia empresa para su API. Esto exige más tiempo debido a que se debe definir de cero el código necesario para lograr solicitar i recopilar datos.

### Librerías externas
Como el uso de estas API está muy extendido debido a la gran popularidad de las aplicaciones existen diversas librerías creadas por otros usuarios con el objetivo de agilizar el proceso de desarrollo de código y facilitar su uso a usuarios más principiantes. 

## Importar la API a nuestro código
Para importar la API no solo necesitaremos importarla dentro del código sino que también serán necesarios los tokens de identificación que nos permitirán validar nuestra identidad con la API al hacer las solicitudes.

```Python
from twitchAPI.twitch import Twitch #Importa la seva llibreria

twitch = Twitch('my_app_key', 'my_app_secret') #Valores de nuestros identificadores de api.
print(twitch.get_users(logins=['your_twitch_username']))
```

## Funciones recursivas
Las funciones recursivas son aquellas que definimos para utilizar más tarde y agilizar un proceso o necesidad que surge con frecuencia dentro de nuestro código. Pueden servir para convertir ciertos datos en strings o agilizar el proceso de creación de dataframes al recopilar datos, por poner algún ejemplo.

```Python
variable = "hola"

def loquesea(valor):
	print(valor)

loquesea(variable)
```

Para que esta función pueda ser utilizada con diversos valores o variables utilizamos lo que se llaman *Dummy Variables*, al definir la función explicaremos como procesaremos los datos utilizando la *dummy variable* pero al llamar la función definiremos qué variable queremos que sea utilizado. En el caso de nuestro código de ejemplo **valor** sería el *dummy* mientras que variable sería, nunca mejor dicho, la variable tratada. En este caso el tratamiento de la variable solo incluye imprimir el valor utilizando un print().

### Try
Los try harán que la función o fragmento de código trate de hacer algo, en caso de no poder irá a la siguiente parte del código o aquello que le hayamos especificado que debe hacer.

```Python
from twitchAPI.twitch import Twitch #Carrega la seva llibreria  
import datetime #per importar a l'hora en que hem llançat l'escript  
#import json  
import pandas as pd #La importem perque ens permeti fer el data frame  
import time  

now =datetime.datetime.now() #aquesta funció serveix per mostrar l'hora de petició  
twitch = Twitch('xxxx', 'xxxx') #Li dono les credencials  
  
llista_dataframes = [] #treiem aquest element de la llista perquè sino es maxacarà  
cursor_dummy = None #Quan la api rep que el cursor es None sap que és la primera pàgina  
  
def crida(cursor):  
  
    '''streams = twitch.get_streams(first=20, language= "es") #Agafem els primers 20 directes en idioma espanyol  
    print(streams) #Ens crea diccionaris    '''    '''data = streams["data"] #Una llista de coses  
  
    for d in data:        print(d)'''    streams = twitch.get_streams(first=20, language="ca",after=cursor)  # Agafo només el primer directe i l'emmagatzemo a streams, L'after demana una nova petició  
    '''with open("output_file.json", 'w', encoding='utf-8') as f:  
        json.dump(streams, f, ensure_ascii=False, indent=4) això ens ho carreguem perque ja no volem crear cap arxiu json    '''    dades = streams["data"]  # La data és tot  
    cursor = streams["pagination"]["cursor"]  
  
    for dada in dades:  
        captured_at = now  
        user_id = dada["user_id"]  
        user_name = dada["user_name"]  
        game_id = dada["game_id"]  
        game_name = dada["game_name"]  
        title = dada["title"]  
        viewer_count = dada["viewer_count"]  
        started_at = dada["started_at"]  
        is_mature = dada["is_mature"]  
  
        df = pd.DataFrame({  
            "captured_at": captured_at,  
            "user_id": user_id,  
            "user_name": user_name,  
            "game_id": game_id,  
            "game_name": game_name,  
            "title": title,  
            "viewer_count": viewer_count,  
            "started_at": started_at,  
            "is_mature": is_mature,  
  
        }, index=[0])  # per indicar a Pandas l'index de la primera fila, que és 0  
        llista_dataframes.append(df)  
  
        #Ara intentem agafar el cursor per a la següent pàgina  
        try:  
            cursor= streams["pagination"]["cursor"]  
            print(cursor)  
            print(f"Fent una nova consulta. Total de streams: {len(llista_dataframes)}")  
            time.sleep(0.12)```



