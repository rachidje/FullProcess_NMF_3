from nltk.tokenize import RegexpTokenizer
from collections import Counter
import pandas as pd

def filterDf(df, years, nbSignatures):
    df_copy = df.copy()

    # interval de temps pour le CS
    if isinstance(years, list) and len(years) == 2:
        df_copy = df_copy[(df_copy.year >= years[0]) & (df_copy.year <= years[1])]
    elif isinstance(years, int):
        df_copy = df_copy[df_copy.year <= years]

    df_copy = df_copy[df_copy['total_signature_count'] > nbSignatures]
    df_copy = df_copy.dropna(subset=['final_content'])
    
    return df_copy

def wordFrequency(df):
    petitions_final = list(df['final_content'])

    wordlists_unigram_final = [str(text).split() for text in petitions_final]
    vocabulaire_final = [item for sublist in wordlists_unigram_final for item in sublist]
    top_words_final = pd.DataFrame(Counter(vocabulaire_final).most_common(len(vocabulaire_final)), columns=['word', 'frequency'])

    wordlists_unigram_unique = [list(set(petition)) for petition in wordlists_unigram_final]
    vocabulaire_unique_perPeti = [item for sublist in wordlists_unigram_unique for item in sublist]
    top_words_unique_perPeti = pd.DataFrame(Counter(vocabulaire_unique_perPeti).most_common(20000), columns=['word', 'frequency'])

    print(top_words_unique_perPeti[top_words_unique_perPeti.frequency == int(len(df)*0.005)].tail(5))

def space_tokenizer(texte):
    return texte.split(' ')

def top_words(topic, n_top_words):
    return topic.argsort()[:-n_top_words - 1:-1]

def topic_table(model, feature_names, n_top_words):
    topics = {}
    for topic_idx, topic in enumerate(model.components_):
        t = (topic_idx)
        topics[t] = [feature_names[i] for i in top_words(topic, n_top_words)]
    return pd.DataFrame(topics)

def whitespace_tokenizer(text): 
    pattern = r"(?u)\b\w\w+\b" 
    tokenizer_regex = RegexpTokenizer(pattern)
    tokens = tokenizer_regex.tokenize(text)
    return tokens

def unique_words(text):
    '''
    Funtion to remove duplicate words
    '''
    ulist = []
    [ulist.append(x) for x in text if x not in ulist]

    return ulist

def joinKeywords(df):
    topic_df = df.copy()
    # Joining each word into a list
    topic_df['topics'] = topic_df.apply(lambda x: [' '.join(x)], axis=1)
    # Removing the list brackets
    topic_df['topics'] = topic_df['topics'].str[0]
    # tokenize
    topic_df['topics'] = topic_df['topics'].apply(lambda x: whitespace_tokenizer(x))
    # Removing duplicate words
    topic_df['topics'] = topic_df['topics'].apply(lambda x: unique_words(x))
    # Joining each word into a list
    topic_df['topics'] = topic_df['topics'].apply(lambda x: [' '.join(x)])
    # Removing the list brackets
    topic_df['topics'] = topic_df['topics'].str[0]

    return topic_df