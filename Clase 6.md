Para utilizar la API de spotify utilizaremos una libreria que se llama spotipy que como mencionamos en [[Clase 4#Librerías externas|clases anteriores]] nos ayudará a agilizar el proceso de desarrollo del código.

Cada vez que solicitamos una petición a la API, aparte de la solicitud que hagamos nosotros también será necesario que mandemos nuestros tokens de validación para que la API pueda confirmar que somos nosotros y que podemos extraer los datos solicitados. 
```Python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
  
SPOTIPY_CLIENT_ID='xxxx'  
SPOTIPY_CLIENT_SECRET='xxxx'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlists = sp.user_playlists('spotify')  
while playlists:  
    for i, playlist in enumerate(playlists['items']):  
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))  
    if playlists['next']:  
        playlists = sp.next(playlists)  
    else:  
        playlists = None```

Con este primer fragmento de código definimos nuestros tokens y una variable donde almacenaremos nuestras credenciales para su uso posterior. Después extraeremos las playlists del usuario identificado y utilizaremos un while que nos permitirá ver los enlaces de cada playlists hasta que no queden más.

Ahora añadiremos una sección al código que nos permitirá extraer la información de las propias playlists:
```Python
import spotipy  
from spotipy.oauth2 import SpotifyClientCredentials  
import json  
  
SPOTIPY_CLIENT_ID='xxxx'  
SPOTIPY_CLIENT_SECRET='xxxx'  
  
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)  
sp = spotipy.Spotify(auth_manager=auth_manager)  
  
playlist = "3oopyXIZGLFtHjFYN9KbuI"  
  
#https://spotipy.readthedocs.io/en/2.22.1/#spotipy.client.Spotify.playlist_items  
  
query = sp.playlist_items(playlist, fields=None, limit=100, offset=0, market=None) #Sp. per imprimir les credencials  
  
print(query)  
  
with open('hola.json', 'w', encoding='utf-8') as f:  
    json.dump(query, f, ensure_ascii=False, indent=4)```

Utilizaremos el archivo json para almacenar toda la información que estamos extrayendo gracias a la API utilizando la función dump. 

Podemos utilizar un ```for i in query["items"]``` Para ver cada item que hay dentro de la query. Podemos desarrollar el código para obtener información adicional sobre los artistas:
```Python
for i in query["items"]:  
    artists = i["track"]["artists"] #Al ser una llista i no un claudàtor hem d'iterar tots els elements  
    for artist in artists:  
        artist_name = artist["name"]  
        artist_id = artist["id"]  
        print(artist_name,artist_id)```

Para cada artista de la playlist cogeremos su ID y lo utilizaremos para obtener otros artistas relacionados:
```Python
for i in query["items"]:  
    artists = i["track"]["artists"] #Al ser una llista i no un claudàtor hem d'iterar tots els elements  
    for artist in artists:  
        artist_name = artist["name"]  
        artist_id = artist["id"]  
        print(artist_name,artist_id)  
          
          
        related_artist = sp.artist_related_artist(artist_id) #funció per esbrinar els artistes recomanats  
  
        with open(f'{artist_id}hola.json', 'w', encoding='utf-8') as f: #Per cada artist id, crearà un arxiu json d'artistes relacionats  
            json.dump(related_artist, f, ensure_ascii=False, indent=4)```

Finalmente podemos añadir un ```time.sleep(1)``` Para que la API no se sature y evitar conflictos.