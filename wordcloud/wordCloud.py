import stylecloud
import pandas as pd

# modelsList = ['FR_CS_C20', 'FR_CS_1720', 'FR_CS_1316', 'FR_CS_C21', 'FR_CS_1821', 'FR_CS_1417']
# modelsList = ['ES_CS_C20']
modelsList = ['EN_CS_C21']
model = modelsList[0]

df = pd.read_csv(f'Prediction/petitions_en_20221_predicted_{model}.csv')
df = df[df['dominant topic'] != "None"]
df['year'] = pd.DatetimeIndex(df.date).year
if len(model.split('_')[-1]) == 4:
    bYear = '20' + model.split('_')[-1][:2]
    eYear = '20' + model.split('_')[-1][2:]

    df = df[(df.year >= float(bYear)) & (df.year <= float(eYear))]
else:
    year = '20' + model.split('_')[-1][1:]

dict_names = {
    'Protection Animale': 'protectionAnimale',
    'Environnement' : 'environnement',
    'Justice' : 'justice',
    'Politique' : 'politique',
    'Santé' : 'sante',
    'Justice Economique' : 'justiceEconomique',
    'Education': 'education',
    'Droit de l’enfance' : 'droitEnfance',
    'Covid19' : 'covid19',
    'Vie Locale' : 'vieLocale',
    'Droit des femmes' : 'droitFemme' ,
    'Mobilité' : 'mobilite',
    'Sport' : 'sport',
    'Médias' : 'medias',
    'Santé - Précaution Ondes' : 'santePrecautionOnde',
    'salud' : 'salud',
    'protección de animales' : 'proteccionAnimale',
    'justicia': 'justicia',
    'justicia económica' : 'justiciaEconomica',
    'educación' : 'educcacion',
    'política' : 'politica',
    'medio ambiente' : 'medioAmbiente',
    'derechos de la mujer' : 'derechosDeLaMujer',
    'derecho del niño' : 'derechoDelNino',
    'movilidad': 'movilidad',
    'vida local' : 'vidaLocal',
    'covid19': 'covid19',
    'ocio' : 'ocio',
    'turismo': 'turismo',
    "Education": 'education',
    "Women's right": 'womenRight',
    "Animal protection": 'animalProtection',
    "Justice": 'justice',
    "Sport": 'sport',
    "Children's right": 'childrenRight',
    "City": 'city',
    "Politics": 'politics',
    "Economic Justice": 'ecomomicJustice',
    "Covid": 'covid',
    "Environment": 'environment',
    "Entertainment": 'entertainment'
}

frMask_dict = {
    "Environnement":"fas fa-leaf",
    "Vie_Locale":"fas fa-university",
    "Education":"fas fa-graduation-cap",
    "Justice":"fas fa-gavel",
    "Justice_Economique":"fas fa-euro-sign",
    "Droit_des_femmes":"fas fa-female",
    "None":"fas fa-times",
    "Mobilité":"fas fa-car-side",
    "Droit_de_l'enfance":"fas fa-child",
    "Sport_et_Médias":"fas fa-baseball-ball",
    "Sport":"fas fa-baseball-ball",
    "Politique":"fas fa-comments",
    "Santé":"fas fa-heartbeat",
    "Protection_Animale":"fas fa-paw",
    "Covid19":"fas fa-virus",
    "Médias":"fas fa-tv",
    "Santé_-_Précaution_Ondes": "fas fa-broadcast-tower"
}

esMask_dict = {
    'salud': "fas fa-heartbeat",
    'protección_de_animales': "fas fa-paw",
    'justicia': "fas fa-gavel",
    'justicia_económica': "fas fa-euro-sign",
    'educación': "fas fa-graduation-cap",
    'política': "fas fa-comments",
    'medio_ambiente': "fas fa-leaf",
    'derechos_de_la_mujer': "fas fa-female",
    'derecho_del_niño': "fas fa-child",
    'movilidad': "fas fa-car-side",
    'vida_local': "fas fa-university",
    'covid19': "fas fa-virus",
    'ocio': "fas fa-baseball-ball",
    'turismo': "fas fa-umbrella-beach"
}

enMask_dict = {
    "Education": "fas fa-graduation-cap",
    "Women's right": "fas fa-female",
    "Animal protection": "fas fa-paw",
    "Justice": "fas fa-gavel",
    "Sport": "fas fa-baseball-ball",
    "Children's right":"fas fa-child",
    "City":"fas fa-university",
    "Politics":"fas fa-comments",
    "Economic Justice":"fas fa-dollar-sign",
    "Covid":"fas fa-virus",
    "Environment":"fas fa-leaf",
    "Entertainment": "fas fa-tv"

}

themes = df['dominant topic'].unique()


for topic in themes:
    if topic == 'Entertainment':
        petition = list(df[df['dominant topic'] == topic]['processed_text'])
        petition_word = [str(text).split() for text in petition]
        flatlist = [item for sublist in petition_word for item in sublist]
        
        texte = ' '.join(flatlist)
        name = dict_names[topic]
        text_file = open(f'wordcloud/{name}.txt', "w")
        n = text_file.write(texte)
        text_file.close()
        
        stylecloud.gen_stylecloud(file_path=f'wordcloud/{name}.txt',
                            icon_name=enMask_dict[topic],
                            palette='cartocolors.qualitative.Pastel_3',
                            background_color='white',
                            output_name=f'wordcloud/{model}/{name}.png',
                            max_words=250,
                            collocations=False,
                            stopwords = True
                            )
        print(topic)   