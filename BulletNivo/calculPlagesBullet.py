from numpy.lib.twodim_base import eye
import pandas as pd
from pprint import pprint

jsonPlages = {}

# frModelsList = ['FR_CS_1316', 'FR_CS_C20', 'FR_CS_1720', 'FR_CS_C21', 'FR_CS_1821', 'FR_CS_1417']
    

# for model in frModelsList:
#     df = pd.read_csv(f'Prediction/petitions_fr_20221_predicted_{model}.csv')
#     df['year'] = pd.DatetimeIndex(df.date).year
    
#     if len(model.split('_')[-1]) == 4:
#         bYear = '20' + model.split('_')[-1][:2]
#         eYear = '20' + model.split('_')[-1][2:]
#         print(bYear, eYear)

#         df = df[(df.year >= float(bYear)) & (df.year <= float(eYear))]
#     else:
#         year = '20' + model.split('_')[-1][1:]
#         print(year)

#         df = df[df.year <= float(year)]

#     themes = pd.read_csv(f'models/fr/df_keywords_{model}.csv')['Topic'].unique()

#     jsonPlages[model] = {}

#     for theme in themes:
#         # plageSeries = df[df[theme] != 0.0][theme].quantile(q=[0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52,0.56,0.60,0.64,0.68,0.72,0.76,0.80,0.84,0.88,0.92,0.96])
#         # jsonPlages[model][theme] = list(plageSeries.values) 
#         plageSeries = df[df['dominant topic'] == theme]['dominant score'].quantile(q=[0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52,0.56,0.60,0.64,0.68,0.72,0.76,0.80,0.84,0.88,0.92,0.96])
#         jsonPlages[model][theme] = list(plageSeries.values)

esModelsList = ['ES_CS_C21']

for model in esModelsList:
    df = pd.read_csv(f'Prediction/petitions_es_202110_predicted_ES_CS_C20.csv')
    df['year'] = pd.DatetimeIndex(df.date).year
    
    if len(model.split('_')[-1]) == 4:
        bYear = '20' + model.split('_')[-1][:2]
        eYear = '20' + model.split('_')[-1][2:]
        print(bYear, eYear)

        df = df[(df.year >= float(bYear)) & (df.year <= float(eYear))]
    else:
        year = '20' + model.split('_')[-1][1:]
        print(year)

        df = df[df.year <= float(year)]

    themes = pd.read_csv(f'models/es/df_keywords_ES_CS_C20.csv')['Topic'].unique()

    jsonPlages[model] = {}

    for theme in themes:
        # plageSeries = df[df[theme] != 0.0][theme].quantile(q=[0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52,0.56,0.60,0.64,0.68,0.72,0.76,0.80,0.84,0.88,0.92,0.96])
        # jsonPlages[model][theme] = list(plageSeries.values) 
        plageSeries = df[df['dominant topic'] == theme]['dominant score'].quantile(q=[0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52,0.56,0.60,0.64,0.68,0.72,0.76,0.80,0.84,0.88,0.92,0.96])
        jsonPlages[model][theme] = list(plageSeries.values)

# enModelsList = ['EN_CS_C21']

# for model in enModelsList:
#     df = pd.read_csv(f'Prediction/petitions_en_20221_predicted_{model}.csv')
#     df['year'] = pd.DatetimeIndex(df.date).year
    
#     if len(model.split('_')[-1]) == 4:
#         bYear = '20' + model.split('_')[-1][:2]
#         eYear = '20' + model.split('_')[-1][2:]
#         print(bYear, eYear)

#         df = df[(df.year >= float(bYear)) & (df.year <= float(eYear))]
#     else:
#         year = '20' + model.split('_')[-1][1:]
#         print(year)

#         df = df[df.year <= float(year)]

#     themes = pd.read_csv(f'models/en/df_keywords_{model}.csv')['Topic'].unique()

#     jsonPlages[model] = {}

#     for theme in themes:
#         # plageSeries = df[df[theme] != 0.0][theme].quantile(q=[0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52,0.56,0.60,0.64,0.68,0.72,0.76,0.80,0.84,0.88,0.92,0.96])
#         # jsonPlages[model][theme] = list(plageSeries.values) 
#         plageSeries = df[df['dominant topic'] == theme]['dominant score'].quantile(q=[0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52,0.56,0.60,0.64,0.68,0.72,0.76,0.80,0.84,0.88,0.92,0.96])
#         jsonPlages[model][theme] = list(plageSeries.values)

pprint(jsonPlages)
