from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import NMF
from Nmf.nmf_functions import *
import pandas as pd
import numpy as np
import pickle

# fr_C20 => max_f = 1873, min_df=201, max_df= 0.75 22 topics
# fr_1720=> max_f= 1953, min_df= 141 max_df=0.75 23 topics
# fr_1316=> max_f= 1685, min_df= 40 max_df=0.75 18 topics

# fr_c21=> max_f=2257, min_df= 249 max_df=0.75 23 topics
# fr_1821=> max_f= 2071, min_df= 178, max_df=0.75 24 topics
# fr_1417=> max_f= 1871, min_df= 57, max_df= 0.75 22 topics

# es_c20=> max_f= 1615, min_df= 95 max_df=0.75 22 topics
# en_C21=> max_f= 995 min_df= 591 max_df= 0.75 23 topics

years = 2021
nbSignatures = 0
max_features = 995
min_df = 591
max_df = 0.75
n_components = 23
df_keywords_path = "models/en/df_keywords_EN_CS_C21.csv"
model_pickle_path = 'models/en/Model_EN_CS_C21.pickle'

df = pd.read_csv("processed_petitions/petitions_en_20221_processed.csv")
df = filterDf(df, years, nbSignatures)
print(len(df))

vectorizer = TfidfVectorizer(
                            max_features = max_features,
                            min_df= min_df,
                            max_df= max_df,
                            #vocabulary= vocab_unique,
                            tokenizer = space_tokenizer
                            )

X = vectorizer.fit_transform(df["final_content"])
idx_to_word = np.array(vectorizer.get_feature_names())
features = vectorizer.get_feature_names()

#Apply NMF
nmf = NMF(n_components=n_components, solver='cd', init='nndsvd').fit(X)
W = nmf.transform(X)
H = nmf.components_

nTopWords= 20

topic_df = topic_table(nmf, features, nTopWords).T
topic_df = joinKeywords(topic_df)

wordFrequency(df)

print(topic_df)


##### Enregistrement du modele ########
# enregistrement du df_topic
topic_df.to_csv(df_keywords_path)

# on retire la fonction tokenizer avant l'enregistrement du model
vectorizer.tokenizer = None

# enregistrement du model 
model = make_pipeline(vectorizer, nmf)
pickle.dump(model, open(model_pickle_path, 'wb'))