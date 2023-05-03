import pandas as pd
import glob
import json

files = glob.glob("api_responses/*") #abrir todos los archivos

llista_dfs = []

for file in files:
    with open(file, encoding='utf-8') as jsonfile:
        dades = json.load(jsonfile)
        tweets = dades['data']
        emp = None
        for tweet in tweets: #amb l'ús d'un for generem un loop amb el que anirem accedint a la informació detallada de cada tuit per extreure-la
            autor_id = tweet['author_id'] #cadascuna d'aquestes variables que creem fa referència a una entrada al diccionari del tuit. D'aquesta formaa anem recollint la informació emmagatzemada
            like = tweet['public_metrics']['like_count'] #accedim dins del diccionar de public_metrics del tuit per coneixer informació sobre el tuit com els likes i els rts
            rt = tweet['public_metrics']['retweet_count']
            fecha = tweet['created_at']
            if 'entities' in tweet: #en cas de que la API detecti entitats com hastags farem que els extregui i els enllaci a la informació emmagatzemada sobre el tuit
                entitats = tweet['entities'] #emmagatzemem el que trobem a una variable
                if 'hashtags' in entitats:
                    tags = entitats['hashtags']
                    for hashtag in tags:
                        hashtags = hashtag['tag']
                else:
                    hashtags = None
            else:
                hashtags = None

            text = tweet['text'] #variable on emmagatzemem el contingut del tuit
            minus = text.lower() #modificant tot el text a minúscules evitem futurs errors i facilitem la cerca de termes com els noms dels candidats
            if minus.find('ada') >= 0: #utilitzant aquesta estructura gairebé switch busquem quins candidats han sigut esmentats a cada tuit.
                Ada = True
            elif minus.find('colau') >= 0:
                Ada = True
            else:
                Ada = False
            if minus.find('basha') >= 0:
                Basha = True
            elif minus.find('changue') >= 0:
                Basha = True
            else:
                Basha = False
            if minus.find('ernest') >= 0:
                Ernest = True
            elif minus.find('maragall') >= 0:
                Ernest = True
            else:
                Ernest = False
            if minus.find('jaume') >= 0:
                Jaume = True
            elif minus.find('collboni') >= 0:
                Jaume = True
            else:
                Jaume = False
            if minus.find('xavier') >= 0:
                Xavier = True
            elif minus.find('trias') >= 0:
                Xavier = True
            else:
                Xavier = False
            if minus.find('anna') >= 0:
                Anna = True
            elif minus.find('grau') >= 0:
                Anna = True
            else:
                Anna = False
            if minus.find('eva') >= 0:
                Eva = True
            elif minus.find('parera') >= 0:
                Eva = True
            else:
                Eva = False
            if minus.find('daniel') >= 0:
                Daniel = True
            elif minus.find('sirera') >= 0:
                Daniel = True
            else:
                Daniel = False
            df = pd.DataFrame({ #amb totes les variables i dades necessàries ja definides desenvolupem un dataframe on afegirem totes les variables recollides del tuit
                'text': text,
                'fecha': fecha,
                'like': like,
                'retweet': rt,
                'hashtags': hashtags,
                'Ada Colau': Ada,
                'Basha Changue': Basha,
                'Ernest Maragall': Ernest,
                'Jaume Collboni': Jaume,
                'Xavier Trias': Xavier,
                'Anna Grau': Anna,
                'Eva Parera': Eva,
                'Daniel Sirera': Daniel,

            }, index=[0])
            llista_dfs.append(df) #el dataframe (del tuit) és afegit a una llista de dataframes
df = pd.concat(llista_dfs) #mitjançant la funció de concatenar fem un dataframe unint els dataframes de cada tuit
df.to_csv('CandidatsEstudi.csv', sep ='\t') #exportem el dataframe extret a csv
