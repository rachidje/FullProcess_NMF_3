import pickle
import pandas as pd
from FullProcess.inputs_fr import getInputs as frInputs
from FullProcess.inputs_es import getInputs as esInputs
from FullProcess.inputs_en import getInputs as enInputs

def load_obj(path, name):
    '''
    Chargement du dico en format pickel
    '''
    with open(path + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def getDataframe(path_file):
    '''
    Fonction qui renvoie un DataFrame filtrer par annees et nettoyer
    :param path_file str
    :param years List | int 
    '''
    df = pd.read_csv(path_file)
    df = df.dropna(subset=['description'])
    try:
        df['year'] = pd.DatetimeIndex(df.date).year
    except AttributeError:
        pass
    df = df.drop_duplicates(subset= ['patent_code'])

    df['title_description'] = df['title'] + " " + df['description']

    return df

def loadInputs(lang):
    if lang == 'fr-FR':
        return frInputs()
    elif lang == 'es-ES':
        return esInputs()
    elif lang == 'en-US':
        return enInputs()
