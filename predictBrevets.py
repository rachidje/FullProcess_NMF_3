from WassatiLib.divers.modules import getCurrentDate
import pandas
from FullProcess.fullProcess_functions import getDataframe
from Prediction.predictFunctions import getDicoScores, getPredictionArray
from models.loadModels import loadModels
from tqdm import tqdm

tqdm.pandas()


filename = f"processed_petitions/brevets_marocain_processed_{getCurrentDate(['year', 'month'])}.csv"
df = pandas.read_csv(filename)

models = loadModels()
language = 'fr-FR'
id_cs = 'FR_CS_C21'

def getAllScores(text):
    df_keywords = models[language][id_cs]['keywords']
    modelChoosen = models[language][id_cs]['model']

    npArray = getPredictionArray(modelChoosen, text)
    dico = getDicoScores(npArray, df_keywords)
    
    # On classe le dico par ses valeurs decroissantes
    dicoT = {k: v for k, v in sorted(dico.items(), reverse=True, key=lambda item: item[1])}

    dominant_topic = list(dicoT.keys())[0]
    score = list(dicoT.values())[0]

    return [dominant_topic ,score]

##### On lance le apply pour obtenir le dominant topic et le score dominant
print("Prediction des dominant topic")
df['dominant topic'] = df['final_content'].progress_apply(lambda text: getAllScores(text)[0])
print("Prediction des dominant score")
df['dominant score'] = df['final_content'].progress_apply(lambda text: getAllScores(text)[1])
df.to_csv(f"Prediction/brevets_marocains_predicted_{id_cs}.csv", index= False)