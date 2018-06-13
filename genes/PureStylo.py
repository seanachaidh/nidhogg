#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 19:28:09 2018

@author: pieter
"""

#SKLEARN
from sklearn.cluster import AgglomerativeClustering
from nltk.probability import FreqDist
from nltk import ngrams

from unittest import TestCase


example_booklist = [    ]


# Wij gebruiken prob_classify voor dit

class PureStylo:
    
    def train(self, bookset):
        
        self.agg = AgglomerativeClustering(n_clusters = len(bookset))
        bookX = []
        
        for b in bookset:
            databook = ngrams(b, self.gramn)
            fdist = FreqDist(databook)
            common = fdist.most_common(100)
            
            inputlist = []
            for c in common:
                inputlist.append(c[0])
                inputlist.append(c[1])
            bookX.append(inputlist)
        self.agg.fit(bookX)
            

    def classify(self, book):
        grams = ngrams(book, self.gramn)
        fdist = FreqDist(grams)
        common = fdist.most_common(100)
        
        X = []
        for c in common:
            X.append(c[0])
            X.append(c[1])
        
        return self.agg.predict(X)
        
    def __init__(self, gramn):
        self.gramn = gramn
        
# END OF CLASS

class TestPureStylo(TestCase):
    def setUp(self):
        self.model = PureStylo()
        

#Begin of testrunner
def testrun():
    pass
