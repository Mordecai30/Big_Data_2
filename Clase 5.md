# Ejercicio 2: Importación de Dataset y Trabajo con Datos

Para poder trabajar con dataframes y datasets vamos a utilizar pandas. Una librería de Python especialmente creada para manipular y analizar datos.

```Python

import pandas as pd  
  
df = pd.read_csv('dataset_youtube.csv') #Importem el dataset amb Pandas  
  
files = df.shape[0] #Per conéixer quantes files té el dataset  
columnes = df.shape[1]  #Per conéixer quantes columnes té el dataset  
  
items_columnes = df.columns #Esbrinar quines columnes componen el dataset  
  
df.drop(['position','channelId','publishedAt','publishedAtSQL','videoDescription', 'tags', #Netejem les dades amb data.drop eliminant les columnes que desitjem  
       'videoCategoryId', 'videoCategoryLabel', 'duration', 'durationSec',  
       'dimension', 'definition', 'caption', 'defaultLanguage',  
       'defaultLAudioLanguage', 'thumbnail_maxres', 'licensedContent', 'dislikeCount', 'favoriteCount',],axis=1, inplace=True) #Axis 1 significa que son columnes i no files  
  
canals = df["channelTitle"]  
canals_unics = df.channelTitle.unique()#El títol de la columna a mig per a treure els canals únics  
print(canals_unics)  
  
df_1 = df.loc[df['channelTitle']== 'NPR Music'] #Posem en una variable tots els values que corresponguin a NPR Music  
df_2 = df.loc[df['channelTitle']== 'KEXP']  
  
  
print(f"El canal NPR té un total de: {df_1.shape[0]}vídeos") #NPR  
print(f"El canal KEXP Music té un total de: {df_2.shape[0]}vídeos")#KEXP  
  
prom_espectadors_1 =  {round(df_1['viewCount'].mean(),2)}  
prom_espectadors_2 =  {round(df_2['viewCount'].mean(),2)}  
  
print(f"El promig d'espectadors de NPR és de: {prom_espectadors_1}") #NPR  
print(f"El promig d'espectadors de KEXP Music és de: {prom_espectadors_2}") #KEXP  
  
#Ara caldria fer el mateix amb les variables de Comentaris i Likes seguint el mateix procés  
print(f"El promig de comentaris de NPR és de: {round(df_1['commentCount'].mean(),2)}") #NPR  
print(f"El promig de comentaris de KEXP Music és de: {round(df_2['commentCount'].mean(),2)}") #KEXP  
  
print(f"El promig de likes de NPR és de: {round(df_1['likeCount'].mean(),2)}") #NPR  
print(f"El promig de likes de KEXP Music és de: {round(df_2['likeCount'].mean(),2)}") #KEXP  
  
#Calcula la desviación de cada vídeo sobre el promedio de especatadores/comentarios/likes  
  
list_desviacio = []  
for index, row in df_1.iterrows(): #Iterem sobre cada línea per descobrir la desviacio  
       desviacio = prom_espectadors_1-row["viewCount"]  
       list_desviacio.append(desviacio)  
df_1["desviacio"]  = list_desviacio  
print(df_1)  
#df_1.to_csv("exemple.csv")
```

# Ejercicio con dataset de Twitch 2023
Con este primer fragmento de código cargaremos el archivo csv donde tenemos los datos almacenados. Para hacerlo utilizaremos la función pd.read_csv() que nos permite leer archivos csv ágilmente. Cabe destacar que hay diversos parámetros que podemos definir dentro de la variable para la lectura correcta de los datos. 

```Python
import pandas as pd  
import time  
  
#Columnes en el dataset  
inici = time.time()  
  
df= pd.read_csv("feb-full-2023.csv",sep='\t')#Aquest dataset està separat per tabuladors, aleshores el separador es \t. Aquest dataset no el podem obrir amb excel ni amb l'ordinador  
#quan fem un read csv el que agada es l'arxiu i el carrega a la RAM.  

#Com no volem carregar tot l'arxiu complet agafem una mostra
#sample = df.sample(frac=0.1) # No ens serveix perque no estalviem el temps de càrrega


final = time.time()
print(final-inici)```

Cargar el archivo entero puede suponer un gasto de recursos excesivo y ralentizar el procesado de los datos. Existen varias formas de agilizar el recurso de leer los datos como puede ser reducir el número de filas o columnas que queremos que lea:

```Python
df= pd.read_csv("feb-full-2023.csv",sep='\t',nrows=2) #Nombre de files que volem extreure

for col in df.columns:
	print(col)
```

Como vamos a trabajar con datos de Twitch necesitaremos plantearnos objetivos de trabajo con tal de definir nuestra metodología y por ende nuestro código.

### Hallar el stream más visto
```Python
stream_mes_vist = max(df["viewer_count"])
```
Dentro de la variable de stream_mes_vist tenemos el stream que cuenta con el valor **max**imo dentro de la fila de *viewer_count*. Ahora necesitaremos encontrar a quién corresponde este resultado.

```Python

posicio = max(df["viewer_count"]).idxmax() #Busca quina posició ocupa el màxim en el dataset total
print = (df["captured_at"].iloc(posicio),
		 df["streamer_name"].iloc(posicio),
		 df["streamer_title"].iloc(posicio),
		 df["viewer_count"].iloc(posicio))```

Utilizando inicialmente idmax encontramos la posición de este stream en específico. Esta id la utilizaremos en la función iloc para obtener el resto de datos de la fila directamente. Así obtendremos cuando fue el stream, el título del stream y el nombre del streamer.

#### Extrayendo los datos de la Kings League
```Python
dades_kings_league = df[df["streamer_name"] == "kingsleague"]
dades_kings_league.to_csv("kingsleague.csv",index=False)```

Dentro de dades_kings_league almacenaremos todos los datos capturados que correspondan al streamer kingsleague.

Para extraer los datos utilizaremos chunks ya que hace el proceso más ágil y exige menos potencia al ordenador.

```Python
df= pd.read_csv("feb-full-2023.csv",sep='\t',usecols=["captured_at","viewer_count","game_name","stream_title"],chunksize=1000)

llista_kings_league = []
for chunk in df: #Creem un loop que itera per cada chunk de les df
	dades_kings_league = chunk[chunk["streamer_name"] == "kingsleague"]
	print (dades_kings_league)
	llista_kings_league.append (dades_kings_league)

final_frame = pd.concat(llista_kings_league)
final_frame.to_csv("kingsleague.csv", index = False)
```

Una vez definido el df de donde extraemos los datos creamos una lista donde iremos almacenando todo.

Con el ```for chunk in df``` generamos un loop donde iremos entrando a cada chunk del archivo y extrayendo los datos relacionados con nuestro streamer.

