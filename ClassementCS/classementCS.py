import pandas as pd

modelsList = ['FR_CS_C20', 'FR_CS_1720', 'FR_CS_1316', 'FR_CS_C21', 'FR_CS_1821', 'FR_CS_1417']

# for model in modelsList:
#     df = pd.read_csv(f'Prediction/petitions_fr_20221_predicted_{model}.csv')
#     themes = df['dominant topic'].unique()
#     dico = {}
#     print(model)
#     for theme in themes:
#         dico[theme] = df[df['dominant topic'] == theme]['total_signature_count'].sum()
    
#     dicoClassement = {k: v for k, v in sorted(dico.items(), reverse=True, key=lambda item: item[1])}

#     df_classement = pd.DataFrame(dicoClassement.items(), columns=['theme_NMF','total_signature_count'])
#     df_classement.to_csv(f"ClassementCS/classement_{model}.csv", index= False)

model = 'ES_CS_C20'
df = pd.read_csv(f'Prediction/petitions_es_20221_predicted_{model}.csv')
themes = df['dominant topic'].unique()
dico = {}
print(model)
for theme in themes:
    dico[theme] = df[df['dominant topic'] == theme]['total_signature_count'].sum()

dicoClassement = {k: v for k, v in sorted(dico.items(), reverse=True, key=lambda item: item[1])}

df_classement = pd.DataFrame(dicoClassement.items(), columns=['theme_NMF','total_signature_count'])
df_classement.to_csv(f"ClassementCS/classement_{model}.csv", index= False)