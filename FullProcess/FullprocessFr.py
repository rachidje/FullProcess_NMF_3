#!/usr/bin/python
# -*-coding:utf-8 -*S
from spacy.lang.char_classes import ALPHA, ALPHA_LOWER, ALPHA_UPPER, HYPHENS
from spacy.lang.char_classes import CONCAT_QUOTES, LIST_ELLIPSES, LIST_ICONS
from FullProcess.fullProcess_functions import loadInputs, load_obj
from FullProcess.customStopWords import getStopwordsList
from spacy.util import compile_infix_regex
import spacy
import re


class FullProcessText:
    language = 'fr-FR'
    nlp = spacy.load('fr_core_news_lg')
    nlp.max_length = 2000000
    dico_merge = load_obj('FullProcess/', 'dico_merge_fr_v3_2021')
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
            if (len(word.lemma_) > 2) or (word.lemma_ == "19") or (word.lemma_ == "2") or (word.lemma_ == "3") or (word.lemma_ == "5"): #on perd OM/OL (foot) ; DG ; As ; km/cm/dc/ml/cl, TV. On garde "19" pour le bigram "covid 19" et "2", "3", "5" pour les chaînes télé
                spacy_tokens.append(word.lemma_)

        return ' '.join(spacy_tokens)

    def correction_err(self, mot):
        if mot in self.mots_erreur[0]:
            # return re.sub('er$','ée',mot) # on remplace le er final par ée
            return  mot[:-2] + "ée" # supp last 2 letters & put "ée"
        elif mot in self.mots_erreur[1]:
            return re.sub('er$','é',mot)
        elif mot in self.mots_erreur[2]:
            return mot[:-1]
        elif mot in self.mots_erreur[3]:
            return mot[:-2]
        elif mot in self.mots_erreur[4]:
            return mot[:-3]
        elif mot in self.mots_erreur[5]:
            return re.sub('el$','elle',mot)
        elif mot in self.mots_erreur[6]:
            return re.sub('er$','ent',mot)
        elif mot in self.mots_erreur[7]:
            return re.sub('er$','ant',mot)
        elif mot in self.mots_erreur[8]:
            return mot + "e"
        elif mot in self.mots_erreur[9]:
            return mot[:-1] + "er" # supp last letter and put "er"
        # elif mot in self.mots_erreur[10]:
        #     return re.sub('ée$','er',mot)
        elif mot in self.mots_erreur[10]:
            return mot[:-2] + "er" # supp last 2 letters and put "er"
        elif mot in self.mots_erreur[11]:
            return mot[:-3] + "er" # supp last 3 letters and put "er"
        else :
            return mot

    def correction_accent(self, mot):
        if mot in self.mots_accent[0]:
            return mot.replace('e','è',1) # on remplace le premier e par un è
        elif mot in self.mots_accent[1]:
            return re.sub('o','ô',mot) # on remplace les o par des ô
        elif mot in self.mots_accent[2]:
            return mot.replace('e','ê',1) # on remplace le premier e par des ê
        elif mot in self.mots_accent[3]:
            return re.sub('e','é',mot) # on remplace le e par des é
        elif mot in self.mots_accent[4]:
            return re.sub('i','î',mot) # on remplace les i par des î
        elif mot in self.mots_accent[4]:
            return mot.replace('u','û',1) # on remplace le premier u par des û
        elif mot in self.mots_accent[5]:
            return mot.replace('e','é',1) # on remplace le premier e par un é
        elif mot in self.mots_accent[6]:
            return re.sub('e$','é',mot)
        else :
            return mot
        
    def correction_lemma(self, mot):
        new_mot = self.correction_err(mot)
        return self.correction_accent(new_mot)

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
        new_text = text.replace("’","'").lower()
        new_text = new_text.replace("en train de","")
        # new_text = new_text.replace(" télé "," télévision ")
        new_text = new_text.replace(" tv "," télévision ")
        new_text = new_text.replace("ile de france","ile-de-france")
        new_text = new_text.replace("île de france","île-de-france")
        new_text = new_text.replace("tout le monde","")
        new_text = new_text.replace("à terre","")
        new_text = new_text.replace("en ligne","")
        new_text = new_text.replace("-vous "," ")
        new_text = new_text.replace("-nous "," ")
        new_text = new_text.replace("-on "," ")
        new_text = new_text.replace("-moi "," ")
        new_text = new_text.replace("sous réserve","")
        new_text = new_text.replace("nous avions","")
        new_text = new_text.replace("s'il vous plaît","")
        new_text = new_text.replace("(e)s", " ")
        new_text = new_text.replace("(e)"," ")
        new_text = new_text.replace("(e"," ")
        new_text = new_text.replace("au sein ","au_sein ")

        new_text = self.spacyProcess(str(new_text).lower())

        wordslist = [self.correction_lemma(word) for word in str(new_text).split()]

        new_wordslist = self.compute_wordlists_ngram2(wordslist)
        new_wordslist = [word for word in new_wordslist if word not in self.more_stopwords]
        new_wordslist = self.maj_tiret_wordlist2(new_wordslist)
        
        return ' '.join(new_wordslist)
        