import pandas as pd
import pickle


def loadModel(modelPath):
    # On charge le vectorizer et le modele nmf
    with open(modelPath, 'rb') as model:
        (vectorizer, nmf) = pickle.load(model)

    return (vectorizer, nmf)

def loadKeywords(keywordPath):
    return pd.read_csv(keywordPath)

def loadModels():
    frNmfPath = "models/fr/"
    esNmfPath = "models/es/"
    enNmfPath = "models/en/"

    return {
            'fr-FR': {
                'FR_CS_C20' : {
                    'model': loadModel(frNmfPath + "Model_FR_CS_C20.pickle"),
                    'keywords': loadKeywords(frNmfPath + "df_keywords_FR_CS_C20.csv"),
                },
                'FR_CS_1316' : {
                    'model': loadModel(frNmfPath + "Model_FR_CS_1316.pickle"),
                    'keywords': loadKeywords(frNmfPath + "df_keywords_FR_CS_1316.csv"),
                },
                'FR_CS_1720' : {
                    'model': loadModel(frNmfPath + "Model_FR_CS_1720.pickle"),
                    'keywords': loadKeywords(frNmfPath + "df_keywords_FR_CS_1720.csv")
                },
                'FR_CS_1821' : {
                    'model': loadModel(frNmfPath + "Model_FR_CS_1821.pickle"),
                    'keywords': loadKeywords(frNmfPath + "df_keywords_FR_CS_1821.csv")
                },
                'FR_CS_C21' : {
                    'model': loadModel(frNmfPath + "Model_FR_CS_C21.pickle"),
                    'keywords': loadKeywords(frNmfPath + "df_keywords_FR_CS_C21.csv")
                },
                'FR_CS_1417' : {
                    'model': loadModel(frNmfPath + "Model_FR_CS_1417.pickle"),
                    'keywords': loadKeywords(frNmfPath + "df_keywords_FR_CS_1417.csv")
                }
            },
            'es-ES': {
                'ES_CS_C20' : {
                    'model': loadModel(esNmfPath + "Model_ES_CS_C20.pickle"),
                    'keywords': loadKeywords(esNmfPath + "df_keywords_ES_CS_C20.csv")
                }
            },
            'en-US': {
                'EN_CS_C21' : {
                    'model': loadModel(enNmfPath + "Model_EN_CS_C21.pickle"),
                    'keywords': loadKeywords(enNmfPath + "df_keywords_EN_CS_C21.csv")
                }
            }
    }