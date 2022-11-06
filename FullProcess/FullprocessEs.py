#!/usr/bin/python
# -*-coding:utf-8 -*S
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, HYPHENS
from spacy.lang.char_classes import CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from FullProcess.fullProcess_functions import load_obj, loadInputs
from FullProcess.customStopWords import getStopwordsList
from spacy.util import compile_infix_regex
import spacy
import re


class FullProcessText:
    language = 'es-ES'
    nlp = spacy.load('es_core_news_lg')
    nlp.max_length = 2000000
    dico_merge = load_obj('FullProcess/', 'dico_merge_es')
    stopwordsList = getStopwordsList(language)
    
    def __init__(self):
        self.updateSpacy_tokenizer()
        [self.mots_erreur, self.mots_accent, self.list_bigrams, self.list_trigrams, self.more_stopwords, self.mots_erreur_ngram] = loadInputs(self.language)

    def addCustomStopwords(self, stopwords):
        doc = self.nlp(' '.join(stopwords), disable=['ner','parser'])
        if isinstance(stopwords, list):
            for word in doc:
                if word.lemma_ not in self.stopwordsList:
                    self.stopwordsList.add(word.lemma_)

    def removeCustomStopwords(self, stopwords):
        doc = self.nlp(' '.join(stopwords), disable=['ner','parser'])
        if isinstance(stopwords, list):
            for word in doc:
                if word.lemma_ in self.stopwordsList:
                    self.stopwordsList.remove(word.lemma_)

    def delete_punct(self, text):
        list_new_text = []
        for word in text.split() :
            #word_without_punct = word.lower().translate(str.maketrans('', '', string.punctuation)) #nécessite import string
            del_prefix = re.sub(r'^[\W]*', '', word) #remove punct as prefixe
            del_sufix = re.sub(r'[\W]*$', '', del_prefix) #remove punct as suffixe
            list_new_text.append(del_sufix)
        return ' '.join(list_new_text) 

    def updateSpacy_tokenizer(self) :
        # modify tokenizer infix patterns
        infixes = (
            LIST_ELLIPSES
            + LIST_ICONS
            + [
                r"(?<=[0-9])[+\-\*^](?=[0-9-])",
                r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES),
                r"(?<=[{a}]),(?=[{a}])".format(a=ALPHA),
                # EDIT: commented out regex that splits on hyphens between letters:
                # #r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS),
                r"(?<=[{a}])(?:['])(?=[{a}])".format(a=ALPHA), #va séparer les mots avec ' (pb pour aujourd'hui, prud'homme, sot-l'y laisse, presqu'île, m'as-tu-vu, pin's, s'il te plaît, jusqu'à, les verbes avec s')
                r"(?<=[{a}0-9])[:<>=/](?=[{a}])".format(a=ALPHA),
            ]
        )
        
        infix_re = compile_infix_regex(infixes)
        self.nlp.tokenizer.infix_finditer = infix_re.finditer
        suffixes = self.nlp.Defaults.suffixes + ([r'''-~\\^|/=§'''])
        suffix_regex = spacy.util.compile_suffix_regex(suffixes)
        self.nlp.tokenizer.suffix_search = suffix_regex.search
        prefixes = self.nlp.Defaults.prefixes + ([r'''-.~\\^|/+]''',r'''[0-9]+'''])
        prefix_regex = spacy.util.compile_prefix_regex(prefixes)
        self.nlp.tokenizer.prefix_search = prefix_regex.search


    def spacyProcess(self, text):
        new_text = self.delete_punct(text)
        spacy_tokens = []
        doc = self.nlp(new_text, disable=['ner','parser'])#,'tagger'])
        for word in doc:
            if word.lemma_ in self.stopwordsList:
                continue
            if re.match(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', word.text.lower()): #url
                continue
            if re.match(r'^([0-9]+)$', word.text.lower()) and word.text.lower() != "19" and word.text.lower() != "2" and word.text.lower() != "3" and word.text.lower() != "5": #word with only digit
                continue
            if re.match(r'[^\x00-\x7F\x80-\xFF\u0100-\u017F\u0180-\u024F\u1E00-\u1EFF]', word.text.lower()): #non-latin chars
                continue
            if word.lemma_ == '-PRON-':
                continue
            if (len(word.lemma_) > 2) or (word.lemma_ == "19"):
                spacy_tokens.append(word.lemma_)

        return ' '.join(spacy_tokens)

    def correction_err(self, mot):
        pass

    def correction_accent(self, mot):
        pass
        
    def correction_lemma(self, mot):
        pass

    #Prends une liste de mots (unigram) en paramètre + la liste des bigrams et trigram à prendre en compte
    #Renvoie une nouvelle liste avec bigram et trigram (les espaces des ngrams sont remplacés par des _)
    def compute_wordlists_ngram2(self, wordslist):
        i=0
        wordlist_ngram = []
        while i < len(wordslist)-2: #loop on words from specific petition
            word = wordslist[i]
            next_word = wordslist[i+1]
            next_word2 = wordslist[i+2]
            bigram = word + ' ' + next_word
            trigram = word + ' ' + next_word + ' ' + next_word2

            if trigram in self.list_trigrams :
                wordlist_ngram.append(trigram.replace(' ','_'))
                i=i+3
            elif bigram in self.list_bigrams :
                wordlist_ngram.append(bigram.replace(' ','_'))
                i=i+2
            else :
                wordlist_ngram.append(word)
                i=i+1

        #gestion des derniers mots
        if i == len(wordslist)-1 :
            wordlist_ngram.append(wordslist[len(wordslist)-1])
        elif i == len(wordslist)-2 :
            if wordslist[len(wordslist)-2] + ' ' + wordslist[len(wordslist)-1] not in self.list_bigrams :
                wordlist_ngram.append(wordslist[len(wordslist)-2])
                wordlist_ngram.append(wordslist[len(wordslist)-1])
            else :
                wordlist_ngram.append(wordslist[len(wordslist)-2] + '_' + wordslist[len(wordslist)-1])                

        return wordlist_ngram

    #take a dict of transformation and a list of strings (words)
    #return a new list of strings with transformations (from dict) made
    def maj_tiret_wordlist2(self, liste):
        reslist = []
        for word in liste:
            if word in self.dico_merge:
                reslist.append(self.dico_merge[word])
            else :
                reslist.append(word)
        return reslist

    def fullProcess(self, text):
        new_text = text.replace("buenos aires","buenos_aires")
        new_text = self.spacyProcess(str(new_text).lower())

        wordslist = [word for word in str(new_text).split()]

        new_wordslist = self.compute_wordlists_ngram2(wordslist)
        new_wordslist = [word for word in new_wordslist if word not in self.more_stopwords]
        new_wordslist = self.maj_tiret_wordlist2(new_wordslist)
        
        return ' '.join(new_wordslist)
        