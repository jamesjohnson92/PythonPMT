#!/usr/bin/env python

import sys
from collections import namedtuple


phrase = namedtuple("phrase","english,logprob")

def translationModel(filename,prune):
    sys.stderr.write("Reading transaltion model file ....%s" %(filename))
    tm = {}
    for line in open(filename):
        (f,e,logprob) = line.strip().split("|||")
        tm.setdefault(tuple(f.split()),[]).append(phrase(e,float(logprob)))
    for f in tm:
        tm[f].sort(key = lambda x : -x.logprob)
        del tm[f][prune:]
    return tm





