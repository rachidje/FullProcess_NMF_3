import spacy
from FullProcess.FullprocessFr import FullProcessText
from FullProcess.fullProcess_functions import *
from operator import itemgetter
from tqdm import tqdm
tqdm.pandas()

loadSpacyConfig = {
    'fr': {
        'dico_merge': load_obj('FullProcess/', 'dico_merge_fr_v3_2021'),
        'nlp': spacy.load('fr_core_news_lg')
    },
    'es': {
        'dico_merge': load_obj('FullProcess/', 'dico_merge_es'),
        'nlp': spacy.load('es_core_news_lg')
    },
    'en': {
        'dico_merge': load_obj('FullProcess/', 'dico_merge_us'),
        'nlp': spacy.load('en_core_web_lg')
    },
}

path_petitions_file = "/home/rachidj/Dropbox/Wassati/scraping/00_DatasetCombiner/petitions_fr_combi20231.csv"
# path_petitions_file = "/home/rachidj/Dropbox/Wassati/scraping/changeOrg_v1/es-ES/00_Petitions/change_es-ES_202110.csv"
# path_petitions_file = "/home/rachidj/Dropbox/Wassati/scraping/changeOrg_v1/en-US/01_Petitions_Classified/change_us_20221.csv"
language = 'fr'

dico_merge, nlp = itemgetter('dico_merge', 'nlp')(loadSpacyConfig[language])


# on instancie un objet FullProcessText
fpt = FullProcessText()

# On recupere le dataframe
df = getDataframe(path_petitions_file)
listid = df[df.theme.str.contains("halloween|halloween-day-off|sprite|cranberry-sprite")]["id"]
df = df[~df.id.isin(listid)]

df['final_content'] = df.title_description.progress_apply(lambda x : fpt.fullProcess(str(x)))
df = df.dropna(subset=['final_content'])

df.to_csv(f"processed_petitions/petitions_{language}_20231_processed.csv", index= False)
print(len(df))
