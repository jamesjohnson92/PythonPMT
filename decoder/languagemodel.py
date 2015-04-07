#!/usr/bin/env python
import sys
from collections import namedtuple

# Simple  Language Model

ngram_stats = namedtuple("ngram_stats","logprob,backoff")

class LM:
    def __init__(self,filename):
        sys.stderr.write("Reading language model from %s..\n" % (filename))
        self.table = {}
        for line in open(filename):
            entry = line.strip().split("\t")
            if len(entry) > 1 and entry[0] != "ngram" :
                (logprob, ngram, backoff) = (float(entry[0]),tuple(entry[1].split()),float(entry[2] if len(entry)==3 else 0.0))
                self.table[ngram] = ngram_stats(logprob,backoff)

    def begin(self):
         return ("<s>",)

    def score(self,state,word):
        ngram = state + (word,)
        score = 0.0
        while len(ngram) > 0 :
            if ngram in self.table:
                return (ngram[-2:],score + self.table[ngram].logprob)
            else:
                score += self.table[ngram[:-1]].backoff if len(ngram) > 1 else 0.0
                ngram = ngram[1:]
        return ((), score + self.table[('<unk>',)].logprob)

    def end(self,state):
        return self.score(state,"</s>")[1]






