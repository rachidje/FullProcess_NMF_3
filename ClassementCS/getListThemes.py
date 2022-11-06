import pandas as pd

modelsList = ['FR_CS_C20', 'FR_CS_1720', 'FR_CS_1316', 'FR_CS_C21', 'FR_CS_1821', 'FR_CS_1417', 'ES_CS_C20']

themes = []

for model in modelsList:
    df = pd.read_csv(f'classement_{model}.csv')
    [themes.append(th) for th in list(df.theme_NMF) if th not in themes]

for th in themes:
    print(th)