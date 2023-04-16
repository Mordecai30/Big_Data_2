import pandas as pd

# Llegim el document
df = pd.read_csv("/Users/santi/Documents/Uni/Dataset Twitch/feb_23_es_simple.csv", sep='\t', usecols=["captured_at","viewer_count", "game_name", "streamer_name" ], nrows=1010000) #utilitzem nrows per reduir temps de processament mentres desenvolupem el codi
#Amb l'ús del usecols i del nrow reduim el consum de memoria i optimitzem el desenvolupament del codi ja que podem veure els resultats més ràpidament.

print("Les categories de les columnes són:") #Amb això podem veure amb facilitat si el programa ha llegit correctament les columnes solicitades. Pot ser eliminat.
for col in df.columns:
    print(col)

#--------------------------------------------------------------------------------------------------------------------------------------
#¿Cuál ha sido la evolución de espectadores (captura a captura) durante el periodo?

df1 = df[['captured_at', 'viewer_count']] #Aquest dataframe recull totes les captures i els espectadors de cada stream, ho utilitzarem per unir els espectadors totals de la plataforma durant la hora d'una captura
df2 = df1.groupby(['captured_at']) ["viewer_count"].sum().reset_index() #groupby agrupa alló que té el mateix valor, ho utilitzem per sumar els diversos resultats de cada 'captured_at' com esmento a la línia anterior
#print(df2) #ens mostra la taula generada perque poguem comprovar que està funcionant correctament.
df2 = df2.to_csv("EspectadorsCapturaACaptura", index=True) #Exportem el dataframe

#--------------------------------------------------------------------------------------------------------------------------------------------
#¿Cuáles son las categorías más vistas y en las que más horas de directo se han realizado?
Categories = pd.DataFrame(df) #definim el dataframe abans de començar per evitar problemes 
Categories = df['game_name'].value_counts().reset_index() #Aquest dataframe fa referència a la quantitat de cops que apareix cada 'game_name' a la llista (cada cop que apareix als 'captured_at')
Categories.rename(columns={'index': 'game_name','game_name':'Captures'}, inplace=True) #modifiquem el nom de les columnes per deixar ben classificades les columnes del dataframe (al modificar-les el nom es torna erroni)
#print(Categories)

Espectadors = pd.DataFrame(df)
Espectadors = df.groupby(['game_name'])["viewer_count"].sum().reset_index() #amb això agrupem totes les categories utilitzant el viewer count per sumar el total d'espectadors
#print(Espectadors)

Combinacio = pd.merge(Categories,Espectadors, on='game_name') #utilitzant merge combinen els dos dataframes anteriors per cohesionar les dades
Combinacio.to_csv('Combinació', index=True)
#-----------------------------------------------------------------------------------------------------------------------

#¿Como han evolucionado (captura a captura) estas categorias a lo largo del mes?
df5 = df.groupby(['captured_at','game_name'])['viewer_count'].sum().reset_index() #agrupem per captures i nom del joc i seguidament afegim el recompte d'espectadors que aconsegueix cada categoria a cada captura (aixi podem veure la seva evolució)
df5 = df5.to_csv("EvolucióCapturaACaptura", index=True)

#------------------------------------------------------------------------------------------------------------------------

#¿Cuál es la distribución de los streamers si los clasificamos por volumenes de audiencia y horas realizadas?
df6= pd.DataFrame(df)
df6 = df.groupby(['streamer_name']) ["viewer_count"].sum().reset_index() #El dataframe 6 recull tots els streamers que apareixen a la taula juntament a laa quantitat total de visites que acumulen dins el dataset
df6.to_csv('EspectadorsStreamers', index=True)

df7 = pd.DataFrame(df)
df7 = df['streamer_name'].value_counts().reset_index() #El dataframe 7 emmagatzema tots els streamers juntament amb la quantitat de captures a les que apareixen.
df7.rename(columns={'index': 'streamer_name','streamer_name':'Captures'}, inplace=True) #renombrem les columnes per tenir-ho més ordenat de cara al dataframe i per poder-ho combinar sense problemes
df7.to_csv('HoresStream', index=True)
#print(df7)

df8 = pd.merge(df7,df6,on='streamer_name')
df8.to_csv('StreamersHores+Viewers', index=True)
#-----------------------------------------------------------------------------------------------------------------------------

#¿Cuál ha sido la evolución (captura a captura) de la desviación estándar en el volúmen de espectadores?
#¿En qué momentos las audiencias se encuentran más polarizadas y en qué momentos la distribución es más uniforme?

desviacio = df.groupby(['captured_at']) ["viewer_count"].std().round(4).reset_index() #AA desviacio estem definint un dataframe on hem agrupat totes les captures ocorregues simultànimament i hem comptabilitzat la quantitat d'espectadors totals d'aquella franja. Utilitzem el round per arrodonir la quantitat de ecimals a 3.
desviacio.to_csv('Desviacio', decimal=',' ,index=True)

