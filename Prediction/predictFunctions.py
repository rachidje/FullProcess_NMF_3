# from ScoreFormat.scoresFormat import ScoresFormat
import numpy as np
from pprint import pprint

def space_tokenizer(texte):
    return texte.split(' ')

def getPredictionArray(model,textLemmatized):
    """
    La fonction se charge de faire passer le texte lemmatiser dans notre pipeline vectorizer, nmf model
    :param model:
    :param textLemmatized: type string
    :return: un numpy array de scores
    """

    vectorizer = model[0]
    vectorizer.tokenizer = space_tokenizer

    nmf = model[1]
    # On transform notre text lemmatized
    vec_new = vectorizer.transform([textLemmatized])
    # On applique notre modele nmf
    predictionScores = nmf.transform(vec_new)

    return predictionScores

def getDicoScores(predictionsScores, df_keywords, thresholdScore = 0.0098, thresholdSum = 0.02):
    """
    La fonction se charge de mapper le numpy array de scores avec le topic que represente chaque score
    en s'aidant du DataFrame Keywords du model en question
    :param predictionsScores:
    :param df_keywords:
    :return: dictionnaires de themes et leurs scores
    """

    # Initialisation d'un dico vide
    dicoThemes = {}
    for idx, score in np.ndenumerate(predictionsScores):
        # on recupere le nom du theme en fonction de l'id du score
        theme = df_keywords.iloc[idx[1]]['Topic']
        # print(idx, score, theme)
        # si le theme est deja present dans le dico on somme les valeur
        if theme in dicoThemes.keys():
            dicoThemes[theme] += score
        else:
            # sinon on affecte le score au theme en question
            dicoThemes[theme] = score

    return dicoThemes