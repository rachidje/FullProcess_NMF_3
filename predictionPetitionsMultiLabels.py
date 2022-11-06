from Prediction.predictFunctions import getDicoScores, getPredictionArray

from FullProcess.FullprocessEn import FullProcessText as FPTEn
from FullProcess.FullprocessEs import FullProcessText as FPTEs
from FullProcess.FullprocessFr import FullProcessText as FPTFr

from FullProcess.inputs_fr import getInputs as frInputs
from FullProcess.inputs_es import getInputs as esInputs
from FullProcess.inputs_en import getInputs as enInputs

from WassatiLib.getArguments.parser import parser
from WassatiLib.divers.modules import getCurrentDate

from models.loadModels import loadModels
from tqdm import tqdm
import pandas as pd
import pickle
import spacy

tqdm.pandas()

currentDate = getCurrentDate(['month', 'year'])

# On charge les models fr et en
models = loadModels()

args = parser(l= 'language', f= 'file', i= 'id_cs') # exple de fichier: /home/rachidj/Dropbox/Wassati/scraping/00_DatasetCombiner/petitions_fr_combi20211.csv
language = args['language']
file = args['file']
id_cs = args['id_cs']

# # On recupere le(s) modele(s) et le(s) csv des keywords en fonction de la langue et du modele CS
modelChoosen = models[language][id_cs]['model']
df_keywords = models[language][id_cs]['keywords']

#### A mettre en commentaire si le df est deja fait
# df = pd.read_csv(args['file'])
# df['description'] = df['title'] + " " + df["description"]

#### A mettre en commentaire si le df n'est pas fait
df = pd.read_csv(f'processed_petitions/petitions_fr_20221_processed.csv')
df = df.dropna(subset=['final_content'])

df['dominant topic'] = ''
df['dominant score'] = ''

##### On creer les colonnes themes
themes = list(df_keywords['Topic'].unique())
print('nombre de themes', len(themes))

#### Chargement du dico_merge
def load_obj(path, name):
    with open(path + name + '.pkl', 'rb') as f:
        return pickle.load(f)

if language == 'fr-FR':
    dico_merge = load_obj('FullProcess/', 'dico_merge_fr_v3_2021')
    nlp = spacy.load('fr_core_news_lg')
    [mots_erreur, mots_accent, list_bigrams, list_trigrams, more_stopwords, mots_erreur_ngram] = frInputs()
    FPT = FPTFr()
elif language == 'es-ES':
    dico_merge = load_obj('FullProcess/', 'dico_merge_es')
    nlp = spacy.load('es_core_news_lg')
    [mots_erreur, mots_accent, list_bigrams, list_trigrams, more_stopwords, mots_erreur_ngram] = esInputs()
    FPT = FPTEs()
elif language == 'en-US':
    dico_merge = load_obj('FullProcess/', 'dico_merge_us')
    nlp = spacy.load('en_core_web_lg')
    [mots_erreur, mots_accent, list_bigrams, list_trigrams, more_stopwords, mots_erreur_ngram] = enInputs()
    FPT = FPTEn()


#### A mettre en commentaire si le df est deja fait
### On lance le fullProcess sur la colonne description
# df['processed_text'] = df['description'].progress_apply(lambda text: FPT.fullProcess(str(text)))
# df = df.dropna(subset= ['processed_text'])
# df.to_csv(f'Prediction/df_{language}_20221_{id_cs}_fullProcess.csv', index= False)

def getAllScores(text):
    npArray = getPredictionArray(modelChoosen, text)
    dico = getDicoScores(npArray, df_keywords)
    # On classe le dico par ses valeurs decroissantes
    dicoT = {k: v for k, v in sorted(dico.items(), reverse=True, key=lambda item: item[1])}

    dominant_topic = list(dicoT.keys())[0]
    score = list(dicoT.values())[0]

    return [dominant_topic, score, dicoT]

##### On lance le apply pour obtenir le dominant topic et le score dominant
print("Prediction des dominant topic")
df['dominant topic'] = df['final_content'].progress_apply(lambda text: getAllScores(text)[0])
print("Prediction des dominant score")
df['dominant score'] = df['final_content'].progress_apply(lambda text: getAllScores(text)[1])

#### On lance le apply pour avoir le score pour chaque theme
print("Prediction multilabels")
df['score_PCT'] = df['final_content'].progress_apply(lambda text: getAllScores(text)[-1])

df['label1'] = df["score_PCT"].apply(lambda x: list(x.keys())[0] if list(x.values())[0]>0 else "None")
df['label2'] = df["score_PCT"].apply(lambda x: list(x.keys())[1] if list(x.values())[1]>0 else "None")
df['label3'] = df["score_PCT"].apply(lambda x: list(x.keys())[2] if list(x.values())[2]>0 else "None")
df['label4'] = df["score_PCT"].apply(lambda x: list(x.keys())[3] if list(x.values())[3]>0 else "None")
df['label5'] = df["score_PCT"].apply(lambda x: list(x.keys())[4] if list(x.values())[4]>0 else "None")


df.to_csv(f"Prediction/petitions_{language}_20221_predicted_{id_cs}_multilabels.csv", index= False)