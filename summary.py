# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk



LANGUAGE = "english"
#SENTENCES_COUNT = 10
SENTENCES_COUNT = 5

class AutomaticSummarization:
    def __init__(self):
            # url = "https://en.wikipedia.org/wiki/Automatic_summarization"
            # parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
            # or for plain text files
            parser = PlaintextParser.from_file("autosum.txt", Tokenizer(LANGUAGE))
            # parser = PlaintextParser.from_string("""Check this out.""".encode('utf-8').strip(), Tokenizer(LANGUAGE))
            stemmer = Stemmer(LANGUAGE)

            summarizer = Summarizer(stemmer)
            summarizer.stop_words = get_stop_words(LANGUAGE)
            #sum = str("");
            
            self.sentence = ""

            for sentence in summarizer(parser.document, SENTENCES_COUNT):
                #sum += sentence.
                print(sentence)
                self.sentence += " " + str(sentence)
            #print(sum)

            #self.sentence = sentence
    
    def return_sentence(self):
        return self.sentence

#